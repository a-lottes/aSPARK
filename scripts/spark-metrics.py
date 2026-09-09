#!/usr/bin/env python3
"""Count what the SPARK loop actually produced on this machine.

Reads two independent sources and never invents a number:

  1. `.spark/` artifacts on disk — the loop's own output, hand-verifiable
     with `ls`. This is the primary source.
  2. Claude Code transcripts under `~/.claude/projects/` — role-agent runs
     and human gate decisions. Machine-local; skipped with an honest note
     when absent.

Anything that cannot be measured reports `n/a` with a plain-English reason
instead of a fabricated `0`. A zero here always means "counted, found none".

Usage:
    scripts/spark-metrics.py                      # search ~ for projects with .spark/
    scripts/spark-metrics.py ~/foo ~/bar          # only these projects
    scripts/spark-metrics.py --totals-only        # aggregate counts, no project named
    scripts/spark-metrics.py --no-transcripts     # disk artifacts only
    scripts/spark-metrics.py --format json        # a report a merge can consume
    scripts/spark-metrics.py --merge a.json b.json  # combine machines

Counting across machines: run it on each with `--format json`, collect the
reports, then combine them with `--merge a.json b.json`. Artifacts are
unioned on a stable per-project identity so a repository checked out twice
counts once; session figures, which really are distinct per machine, are
summed.

stdlib only, no dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

# A phase counts as reached when any one of its artifact names is present.
# The alternates are real: older loops wrote `review-report.md` before the
# template settled on `review.md`.
PHASES: dict[str, tuple[str, ...]] = {
    "spec": ("spec.md",),
    "plan": ("plan.md",),
    "review": ("review.md", "review-report.md"),
    "qa": ("qa.md", "qa-report.md"),
    "release": ("release.md", "release-notes.md"),
}

# Directories never worth descending into when searching for projects.
SKIP_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__", "Library",
    "Applications", ".Trash", ".cache", ".npm", ".cargo", "dist", "build",
    ".claude-worktrees", "site-packages",
}

# Bumped whenever the JSON report's shape changes. A merge across machines
# refuses mismatched versions rather than silently mis-adding them.
REPORT_SCHEMA = 1

CEREMONIES = {
    "spark", "story-time", "sprint-plan", "increment", "peer-review",
    "demo-day", "go-live", "charter", "look-and-feel", "next-steps",
}

CMD_RE = re.compile(r"<command-name>/?(?:aspark:)?([a-z\-]+)</command-name>")

# The preamble Claude Code prepends when it loads a skill from the plugin cache.
SKILL_RE = re.compile(r"Base directory for this skill:[^\n]*plugins/cache/aspark")


def user_text(record: dict) -> str:
    """Prose the user (or a skill preamble) actually sent.

    Tool results ride in the same `user` records, and a session that greps
    these very transcripts would otherwise detect itself as an aSPARK run.
    Only plain strings and `text` blocks count.
    """
    content = record.get("message", {}).get("content")
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "\n".join(
        block.get("text", "")
        for block in content
        if isinstance(block, dict) and block.get("type") == "text"
    )


# --------------------------------------------------------------------------
# git helpers
# --------------------------------------------------------------------------

def git(repo: Path, *args: str) -> str | None:
    """Run a git command in `repo`; None when git fails or isn't a repo."""
    try:
        out = subprocess.run(
            ("git", "-C", str(repo), *args),
            capture_output=True, text=True, timeout=60,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return out.stdout.strip() if out.returncode == 0 else None


def project_id(repo: Path) -> str | None:
    """A project's identity, stable across machines and clones.

    The root commit is the same hash in every clone of a repository, which
    makes it the one thing that survives a different path on a different
    machine. It is hashed rather than used raw so that an identifier can be
    passed around without naming — or pointing at — the repository it came
    from.

    None when the project is not a git repository: there is then nothing
    stable to key on, and a merge must say so instead of guessing.
    """
    root = git(repo, "rev-list", "--max-parents=0", "HEAD")
    if not root:
        return None
    return "g:" + hashlib.sha256(root.splitlines()[0].encode()).hexdigest()[:16]


def git_stats(repo: Path) -> dict:
    """Lines changed since the loop was adopted, plus the tag count.

    'Adopted' means the first commit that touched `.spark/`. Counting a
    repo's whole history would credit aSPARK with code written before it
    was ever installed — that is the one number most easily overstated, so
    it is deliberately bounded here.
    """
    if git(repo, "rev-parse", "--git-dir") is None:
        return {"available": False, "reason": "not a git repository"}

    tags = git(repo, "tag")
    tag_count = len([t for t in (tags or "").splitlines() if t])

    first = git(repo, "log", "--reverse", "--format=%H", "--", ".spark")
    first = first.splitlines()[0] if first else None
    if not first:
        return {
            "available": False,
            "tags": tag_count,
            "reason": ".spark/ is not tracked in this repository",
        }

    # A root commit has no parent; then the adoption commit is the history.
    parent = git(repo, "rev-parse", "--verify", "-q", f"{first}^")
    rev_range = f"{parent}..HEAD" if parent else "HEAD"

    numstat = git(repo, "log", "--numstat", "--format=", rev_range)
    added = deleted = 0
    for line in (numstat or "").splitlines():
        cols = line.split("\t")
        if len(cols) == 3 and cols[0].isdigit() and cols[1].isdigit():
            added += int(cols[0])
            deleted += int(cols[1])

    return {
        "available": True,
        "tags": tag_count,
        "added": added,
        "deleted": deleted,
        "adopted_on": git(repo, "log", "-1", "--format=%ad", "--date=short", first),
        "adopted_at_root": parent is None,
    }


# --------------------------------------------------------------------------
# .spark/ artifacts
# --------------------------------------------------------------------------

def scan_project(project: Path) -> dict | None:
    """Count features and reached phases in one project's `.spark/`."""
    spark = project / ".spark"
    if not spark.is_dir():
        return None

    features: list[dict] = []
    for entry in sorted(spark.iterdir()):
        if not entry.is_dir() or entry.name.startswith("."):
            continue
        reached = {
            phase: any((entry / name).is_file() for name in names)
            for phase, names in PHASES.items()
        }
        features.append({"name": entry.name, "reached": reached})

    return {
        "path": str(project),
        "name": project.name,
        "id": project_id(project),
        "features": features,
        "phase_counts": {
            phase: sum(f["reached"][phase] for f in features) for phase in PHASES
        },
        "has_constitution": (spark / "constitution.md").is_file(),
        "git": git_stats(project),
    }


def find_projects(root: Path, depth: int) -> list[Path]:
    """Directories under `root` that contain a `.spark/`, breadth-first."""
    found: list[Path] = []
    frontier = [(root, 0)]
    while frontier:
        current, level = frontier.pop(0)
        try:
            entries = sorted(p for p in current.iterdir() if p.is_dir())
        except (PermissionError, OSError):
            continue
        if (current / ".spark").is_dir():
            found.append(current)
            continue  # a project's own subdirectories are not projects
        if level >= depth:
            continue
        for entry in entries:
            if entry.name in SKIP_DIRS or entry.is_symlink():
                continue
            if entry.name.startswith(".") and entry.name != ".spark":
                continue
            frontier.append((entry, level + 1))
    return found


# --------------------------------------------------------------------------
# Claude Code transcripts
# --------------------------------------------------------------------------

def scan_transcripts(root: Path) -> dict:
    """Role-agent runs, ceremony invocations and human gates in aSPARK sessions.

    A session counts as aSPARK-driven when it either invoked one of the
    ceremonies by name, or loaded a skill from the aspark plugin cache.
    Merely *mentioning* aspark is not enough — a session that lists the
    available skills, or one that reads these transcripts, would otherwise
    detect itself and inflate every number here.
    """
    if not root.is_dir():
        return {"available": False, "reason": f"no transcript directory at {root}"}

    sessions = sorted(root.glob("*/*.jsonl"))
    if not sessions:
        return {"available": False, "reason": f"no transcripts under {root}"}

    ceremonies: Counter[str] = Counter()
    agents: Counter[str] = Counter()
    gates = 0
    aspark_sessions = 0
    days: set[str] = set()

    for path in sessions:
        found_cmds: Counter[str] = Counter()
        found_agents: Counter[str] = Counter()
        found_gates = 0
        found_days: set[str] = set()
        is_aspark = False

        try:
            handle = path.open(errors="ignore")
        except OSError:
            continue
        with handle:
            for line in handle:
                try:
                    rec = json.loads(line)
                except (ValueError, TypeError):
                    continue

                kind = rec.get("type")
                if kind == "user":
                    text = user_text(rec)
                    for name in CMD_RE.findall(text):
                        if name in CEREMONIES:
                            found_cmds[name] += 1
                            is_aspark = True
                    if SKILL_RE.search(text):
                        is_aspark = True
                elif kind == "assistant":
                    blocks = rec.get("message", {}).get("content")
                    if not isinstance(blocks, list):
                        continue
                    for block in blocks:
                        if block.get("type") != "tool_use":
                            continue
                        if block.get("name") == "AskUserQuestion":
                            found_gates += 1
                        elif block.get("name") == "Agent":
                            kind_of = (block.get("input") or {}).get("subagent_type", "")
                            if kind_of.startswith("aspark:"):
                                found_agents[kind_of.split(":", 1)[1]] += 1
                                is_aspark = True

                stamp = rec.get("timestamp")
                if isinstance(stamp, str) and len(stamp) >= 10:
                    found_days.add(stamp[:10])

        if is_aspark:
            aspark_sessions += 1
            ceremonies.update(found_cmds)
            agents.update(found_agents)
            gates += found_gates
            days |= found_days

    return {
        "available": True,
        "root": str(root),
        "sessions_total": len(sessions),
        "sessions_aspark": aspark_sessions,
        "agent_runs": dict(agents.most_common()),
        "agent_runs_total": sum(agents.values()),
        "gates": gates,
        "ceremonies": dict(ceremonies.most_common()),
        "active_days": len(days),
        "days": sorted(days),
        "first_day": min(days) if days else None,
        "last_day": max(days) if days else None,
    }


# --------------------------------------------------------------------------
# rendering
# --------------------------------------------------------------------------

def label_projects(projects: list[dict]) -> None:
    """Give every project a unique label.

    A stale second checkout shares its basename with the live one. Silently
    folding the two together would double-count features that only ever ran
    once, so collisions are disambiguated by path rather than merged.
    """
    seen = Counter(p["name"] for p in projects)
    for project in projects:
        if seen[project["name"]] > 1:
            parent = Path(project["path"]).parent
            try:
                parent = parent.relative_to(Path.home())
            except ValueError:
                pass
            project["label"] = f"{project['name']} (~/{parent})" if str(parent) != "." else project["name"]
        else:
            project["label"] = project["name"]


def feature_count(project: dict) -> int:
    """Features in a project, scanned (a list) or merged (already a count)."""
    features = project["features"]
    return features if isinstance(features, int) else len(features)


def render_totals(report: dict) -> list[str]:
    """The aggregate table: counts only, no project named.

    What a project is called is nobody's business but its owner's, and a
    name adds nothing to a figure about the loop. The per-project view stays
    available locally; this is the shape meant for publishing.
    """
    projects = report["projects"]
    totals = report["totals"]
    t = totals["phase_counts"]
    out = [
        "| Features | Spec | Plan | Review | QA | Release | Git tags |",
        "|---:|---:|---:|---:|---:|---:|---:|",
        f"| **{totals['features']}** | **{t['spec']}** | **{t['plan']}** | "
        f"**{t['review']}** | **{t['qa']}** | **{t['release']}** | **{totals['tags']}** |",
        "",
        f"{totals['projects']} project{'s' if totals['projects'] != 1 else ''}, "
        f"{totals['features']} feature{'s' if totals['features'] != 1 else ''}. "
        "A phase counts as reached when its artifact exists — nothing here is "
        "inferred from a transcript.",
    ]

    if report.get("merged_from"):
        note = (
            f"Merged from {report['merged_from']} machine "
            f"report{'s' if report['merged_from'] != 1 else ''}. Projects are "
            "unioned on a stable identity, never added, so a repository checked "
            "out on more than one machine counts once."
        )
        if report.get("unidentified_projects"):
            n = report["unidentified_projects"]
            note += (
                f" {n} project{'s' if n != 1 else ''} could not be identified "
                "across machines (not a git repository) and "
                f"{'are' if n != 1 else 'is'} counted as found — if the same one "
                "exists on two machines, it is counted twice. `git init` gives "
                "such a project an identity that merges."
            )
        out.append("")
        out.append(note)

    counted = [p for p in projects if p["git"]["available"]]
    skipped = Counter(p["git"]["reason"] for p in projects if not p["git"]["available"])
    line = (
        f"**+{totals['added']:,} / −{totals['deleted']:,} lines** since the loop "
        f"was adopted, across the {len(counted)} of {len(projects)} projects whose "
        "line count is measurable"
    )
    if skipped:
        line += "; " + ", ".join(
            f"{n} report{'s' if n == 1 else ''} n/a ({reason})"
            for reason, n in skipped.most_common()
        )
    out.append(line + ".")
    return out


def render_detail(report: dict) -> list[str]:
    """The per-project table, for reading on the machine that produced it."""
    totals = report["totals"]
    out = [
        "| Project | Features | Spec | Plan | Review | QA | Release | Tags | Lines since adoption |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for p in report["projects"]:
        c = p["phase_counts"]
        g = p["git"]
        if g["available"]:
            lines = f"+{g['added']:,} / −{g['deleted']:,}"
            if not g["adopted_at_root"]:
                lines += f" (since {g['adopted_on']})"
            tags = str(g["tags"])
        else:
            lines = f"n/a — {g['reason']}"
            tags = str(g.get("tags", "n/a"))
        out.append(
            f"| {p['label']} | {feature_count(p)} | {c['spec']} | {c['plan']} | "
            f"{c['review']} | {c['qa']} | {c['release']} | {tags} | {lines} |"
        )
    t = totals["phase_counts"]
    out.append(
        f"| **Total** | **{totals['features']}** | **{t['spec']}** | **{t['plan']}** | "
        f"**{t['review']}** | **{t['qa']}** | **{t['release']}** | "
        f"**{totals['tags']}** | **+{totals['added']:,} / −{totals['deleted']:,}** |"
    )
    out.append("")
    out.append(
        f"{totals['projects']} project{'s' if totals['projects'] != 1 else ''}, "
        f"{totals['features']} feature{'s' if totals['features'] != 1 else ''}. "
        "A phase counts as reached when its artifact exists — nothing here is "
        "inferred from a transcript."
    )
    return out


def render_markdown(report: dict, totals_only: bool = False) -> str:
    out: list[str] = ["## Loop artifacts on disk\n"]
    out += render_totals(report) if totals_only else render_detail(report)

    tr = report["transcripts"]
    out.append("\n## Loop activity in Claude Code transcripts\n")
    if not tr["available"]:
        out.append(f"n/a — {tr['reason']}. The disk table above stands on its own.")
        return "\n".join(out) + "\n"

    out.append(f"- **{tr['sessions_aspark']}** of {tr['sessions_total']} sessions were aSPARK-driven")
    out.append(f"- **{tr['agent_runs_total']}** role-agent runs: " + " · ".join(
        f"{role} {n}" for role, n in tr["agent_runs"].items()) or "- no role-agent runs recorded")
    out.append(f"- **{tr['gates']}** human gate decisions (`AskUserQuestion`)")
    if tr["first_day"]:
        out.append(f"- **{tr['active_days']}** active days, {tr['first_day']} to {tr['last_day']}")
    named = sum(tr["ceremonies"].values())
    out.append(
        f"- {named} ceremonies invoked by name: "
        + " · ".join(f"/{c} {n}" for c, n in tr["ceremonies"].items())
        + " — an undercount, because `/spark` runs the other ceremonies "
          "internally without leaving a command of its own"
    )
    return "\n".join(out) + "\n"


def merge_reports(paths: list[Path]) -> dict:
    """Combine per-machine JSON reports into one honest total.

    Artifacts are unioned, never added. The same repository checked out on
    two machines holds the *same* features, so adding the two reports would
    double-count every one of them; projects are keyed on `project_id` and
    each count takes the highest any machine saw, which is the most complete
    view available when one clone is behind the other.

    Transcript figures are the opposite case and *are* summed: a session on
    another machine is a genuinely different session. Active days union
    rather than add, because the same day can appear on two machines.

    Projects with no stable identity (not a git repository) cannot be
    matched across machines. They are kept and counted, and the merged
    report says how many there are, because a total that hides them would
    be wrong in the other direction.
    """
    reports = []
    for path in paths:
        try:
            data = json.loads(path.read_text())
        except (OSError, ValueError) as exc:
            raise SystemExit(f"{path}: not a readable JSON report ({exc})")
        if not isinstance(data, dict) or "projects" not in data or "totals" not in data:
            raise SystemExit(f"{path}: not a spark-metrics report")
        schema = data.get("schema")
        if schema != REPORT_SCHEMA:
            raise SystemExit(
                f"{path}: report schema {schema!r}, this script writes and reads "
                f"{REPORT_SCHEMA}. Regenerate it with the same version of the script."
            )
        reports.append(data)

    merged: dict[str, dict] = {}
    unidentified: list[dict] = []
    for data in reports:
        for project in data["projects"]:
            key = project.get("id")
            if not key:
                unidentified.append(project)
                continue
            if key not in merged:
                merged[key] = {
                    "id": key,
                    "features": feature_count(project),
                    "phase_counts": dict(project["phase_counts"]),
                    "git": dict(project["git"]),
                }
                continue
            seen = merged[key]
            seen["features"] = max(seen["features"], feature_count(project))
            for phase in PHASES:
                seen["phase_counts"][phase] = max(
                    seen["phase_counts"][phase], project["phase_counts"][phase]
                )
            here, there = seen["git"], project["git"]
            here["available"] = here.get("available") or there.get("available")
            for field in ("tags", "added", "deleted"):
                if field in there:
                    here[field] = max(here.get(field, 0), there[field])
            if there.get("available"):
                here.pop("reason", None)

    projects = [
        dict(p, features=feature_count(p), label=p.get("id", "unidentified"))
        for p in list(merged.values()) + unidentified
    ]
    totals = {
        "projects": len(projects),
        "features": sum(feature_count(p) for p in projects),
        "phase_counts": {
            phase: sum(p["phase_counts"][phase] for p in projects) for phase in PHASES
        },
        "tags": sum(p["git"].get("tags", 0) for p in projects),
        "added": sum(p["git"].get("added", 0) for p in projects),
        "deleted": sum(p["git"].get("deleted", 0) for p in projects),
    }

    return {
        "schema": REPORT_SCHEMA,
        "merged_from": len(reports),
        "unidentified_projects": len(unidentified),
        "projects": projects,
        "totals": totals,
        "transcripts": merge_transcripts([r["transcripts"] for r in reports]),
    }


def merge_transcripts(parts: list[dict]) -> dict:
    """Sum session figures across machines; union the days."""
    usable = [t for t in parts if t.get("available")]
    if not usable:
        reasons = sorted({t.get("reason", "unavailable") for t in parts})
        return {"available": False, "reason": "; ".join(reasons)}

    agents: Counter[str] = Counter()
    ceremonies: Counter[str] = Counter()
    days: set[str] = set()
    sessions_total = sessions_aspark = gates = 0
    for part in usable:
        agents.update(part.get("agent_runs", {}))
        ceremonies.update(part.get("ceremonies", {}))
        days |= set(part.get("days") or [])
        sessions_total += part.get("sessions_total", 0)
        sessions_aspark += part.get("sessions_aspark", 0)
        gates += part.get("gates", 0)

    return {
        "available": True,
        "sessions_total": sessions_total,
        "sessions_aspark": sessions_aspark,
        "agent_runs": dict(agents.most_common()),
        "agent_runs_total": sum(agents.values()),
        "gates": gates,
        "ceremonies": dict(ceremonies.most_common()),
        "active_days": len(days),
        "days": sorted(days),
        "first_day": min(days) if days else None,
        "last_day": max(days) if days else None,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("projects", nargs="*", type=Path, help="project directories (default: search --search-root)")
    parser.add_argument("--search-root", type=Path, default=Path.home())
    parser.add_argument("--depth", type=int, default=3, help="search depth below --search-root (default: 3)")
    parser.add_argument("--exclude", action="append", default=[], metavar="SUBSTRING",
                        help="skip any project whose path contains SUBSTRING (repeatable)")
    parser.add_argument("--transcripts", type=Path, default=Path.home() / ".claude" / "projects")
    parser.add_argument("--no-transcripts", action="store_true", help="count disk artifacts only")
    parser.add_argument("--merge", nargs="+", type=Path, metavar="REPORT.json",
                        help="combine JSON reports from several machines instead of scanning")
    parser.add_argument("--totals-only", action="store_true",
                        help="aggregate counts only — no project named, for publishing")
    parser.add_argument("--format", choices=("md", "json"), default="md")
    args = parser.parse_args()

    if args.merge:
        merged = merge_reports([Path(f).expanduser() for f in args.merge])
        if args.format == "json":
            print(json.dumps(merged, indent=2))
        else:
            # A merged report has no project names to begin with — only
            # opaque ids — so the aggregate shape is the only one it has.
            print(render_markdown(merged, totals_only=True))
        return 0

    candidates = args.projects or find_projects(args.search_root.expanduser(), args.depth)
    candidates = [c for c in candidates if not any(x in str(c) for x in args.exclude)]
    projects = [r for r in (scan_project(Path(p).expanduser().resolve()) for p in candidates) if r]
    if not projects:
        where = " ".join(str(p) for p in args.projects) or f"{args.search_root} (depth {args.depth})"
        print(f"No project with a .spark/ directory found in {where}.", file=sys.stderr)
        return 1
    projects.sort(key=lambda p: (-len(p["features"]), p["name"]))
    label_projects(projects)

    totals = {
        "projects": len(projects),
        "features": sum(len(p["features"]) for p in projects),
        "phase_counts": {
            phase: sum(p["phase_counts"][phase] for p in projects) for phase in PHASES
        },
        "tags": sum(p["git"].get("tags", 0) for p in projects),
        "added": sum(p["git"].get("added", 0) for p in projects),
        "deleted": sum(p["git"].get("deleted", 0) for p in projects),
    }

    transcripts = (
        {"available": False, "reason": "skipped with --no-transcripts"}
        if args.no_transcripts
        else scan_transcripts(args.transcripts.expanduser())
    )

    report = {
        "schema": REPORT_SCHEMA,
        "projects": projects,
        "totals": totals,
        "transcripts": transcripts,
    }
    if args.format == "json":
        payload = dict(report)
        if args.totals_only:
            # A name must not survive in the JSON either, or --totals-only
            # would be a display trick rather than a real one.
            # `id` survives: it is an opaque hash, not a name, and without
            # it a merge across machines cannot tell one project from two.
            payload["projects"] = [
                {"id": p["id"], "features": len(p["features"]),
                 "phase_counts": p["phase_counts"],
                 "git": {k: v for k, v in p["git"].items() if k != "adopted_on"}}
                for p in projects
            ]
        print(json.dumps(payload, indent=2))
    else:
        print(render_markdown(report, totals_only=args.totals_only))
    return 0


if __name__ == "__main__":
    sys.exit(main())

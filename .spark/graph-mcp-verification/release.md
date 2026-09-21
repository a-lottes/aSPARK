# Release: graph-mcp-verification

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 3), `qa.md` (`passed`, round 1) |
| **Status** | `preparing` |
| **Version** | v0.11.0 (**unbumped** — no bump proposed) |
| **Date** | 2026-09-21 |

**Handoff**
- **Status:** `preparing` — pre-flight complete, release commit staged locally,
  nothing pushed. Awaiting the user's explicit go for any outward-facing step.
- **Summary:** Verify-only sweep re-checked GitHub issues #8, #10, #11 (optional
  `aspark-graph`/MCP integration) live; all three confirmed and closeable with
  evidence, zero Core defects found. No capability added, no behavior changed.
- **Open:** `1 outstanding` — the push + PR are prepared but not executed; every
  command below is pending the caller's relayed authorization.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except
  `Status`/`Version`; log the mismatch at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Run fresh, on commit `2ec691c` (branch tip before this pass's own commit), just now.*

- [x] `review.md` status is `passed` — read fresh: Handoff + REVIEW GATE, round 3.
      0 open Blocker, 0 open Major (F1/F3 `fixed r2`; F2/F11 waived by the user,
      both rulings re-verified as accurately recorded), 0 open Minor (F14 `fixed r3`).
- [x] `qa.md` status is `passed` — read fresh: Handoff + QA GATE, round 1. 14/14 ACs
      and 8/10 NFRs (2 N/A) confirmed, 0 open Blocker/Major/Minor. **QA-method row:**
      constitution §8 carries a complete declaration (surface `no`, substitute method
      named) — QA ran by that declared method, against the installed plugin, as this
      project's standing fact (§8, added 2026-08-29), not a per-feature override or a
      waiver for this release; `qa.md` records every `AC-`/`NFR-` ID QA owns, same
      as always.
- [x] Full test suite green on the release commit — none exists, none possible for
      prompt material (constitution §4).
- [x] Build succeeds from a clean checkout — N/A: Markdown + JSON only, no build step.
- [x] No uncommitted changes in the working tree — clean except this feature's own
      untracked deliverable (`.spark/graph-mcp-verification/**`, now staged) and the
      pre-existing, never-committed guard-hook ledger `.spark/.guard/` (unrelated to
      this feature's authorship; review F1 already disclosed and routed this).
- [x] Branch staleness (project `CLAUDE.md` caution) — `git fetch origin main`;
      `git rev-parse HEAD origin/main main` all three return `2ec691c` — identical,
      zero drift. `git log --oneline main..origin/main` and `origin/main..HEAD` both
      empty. Nothing merged into `main` since this branch was cut; not stale.
- [x] `claude plugin validate .` run live — **passed**, one pre-existing `autoUpdate`
      warning unrelated to this diff, present on every prior release.
- [x] Fence re-check — `git diff --name-only origin/main..HEAD` empty pre-commit
      (nothing tracked changed yet); `skills/ agents/ tools/ lenses/ templates/
      .claude-plugin/plugin.json` byte-identical to `origin/main`; `plugin.json`
      still `0.11.0`.

## 2. Changelog

### Added
- Nothing new to use — this release ships no new capability. It is a live
  verification pass over three previously-open claims about the optional
  dependency-graph/MCP integration.

### Changed
- Nothing changed in the shipped plugin — `skills/`, `agents/`, `tools/`,
  `lenses/`, `templates/` and the plugin manifest are byte-identical to before
  this sweep. Only a new evidence record was added.

### Fixed
- Nothing needed fixing. The one-time "build the graph" reminder was confirmed
  to fire exactly once per run and never nag; the optional MCP-first resolution
  path was confirmed to be taken ahead of any file-based fallback, twice in a
  row; and both alternative browser-automation backends (Playwright and Chrome
  DevTools) were confirmed to actually drive a real page, not just be named in
  setup instructions. All three previously-undecided claims now hold up live.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | **Not executed — no bump.** Spec NFR-2 requires this verify-only sweep's fence to leave `.claude-plugin/plugin.json` byte-identical (no shipped capability changed — evidence only, under `.spark/graph-mcp-verification/**`). Version stays `0.11.0`. No tag — none before merge in `pr` mode; the real tag, if any, happens post-merge, outside this role's control. |
| PR / merge | **Prepared, not executed — awaiting the user's explicit go.** Release commit staged locally (unpushed): `.spark/graph-mcp-verification/{spec,plan,review,qa,evidence,release}.md`. Pending commands, none yet run: `git commit -m "docs: verify-only sweep closes #8/#10/#11 live (v0.11.0, unbumped)"`; `git push -u origin feat/graph-mcp-verification`; `gh pr create --base main --head feat/graph-mcp-verification --title "docs: verify-only sweep closes #8/#10/#11 live (v0.11.0, unbumped)" --body <§2 changelog>`. |
| Deploy | N/A — no deploy surface; the plugin is installed by consumers via `/plugin install`, never deployed by this repo (constitution §2). |
| Post-release smoke check | N/A — `pr` mode, nothing deployed (named, not dropped); no PR is open yet for even a pre-merge sanity pass. |

## 4. Learnings (Keep!)

- **What went well:** three review rounds plus one QA round each re-derived the
  same facts from primary source (raw JSONL, live `claude mcp list`, live
  restoration probes) rather than trusting the prior round's label — zero drift
  across the whole cycle, including a disclosed non-defect (F1: the untracked
  `.spark/.guard/` ledger was first mis-described as "unrelated," corrected to
  name it accurately as the guard hook's shared provenance ledger, with NFR-1's
  actual fence untouched by the correction).
- **What we'd do differently:** two Majors (F2, F11) needed the user's explicit
  waiver rather than a clean fix — an execution-mode deviation (T7) surfaced
  only at round 3; catching plan deviations at `/peer-review` round 1 would
  avoid a late-cycle waiver negotiation next time.
- **Patterns worth reusing:** disclosing a machine-state artifact precisely
  (what it is, what this run added to it, why the fence still holds) instead of
  waving it off as "unrelated" — candidate for this repo's `CLAUDE.md` alongside
  the existing refuted-with-finding and branch-staleness habits.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. Checked only where genuinely true today.*

- [x] All pre-flight checks passed at release time — §1, all fresh
- [x] Changelog written in user-facing language — §2
- [ ] Release actions executed and verified — **not yet**: commit staged but not
      created, nothing pushed, no PR open. Prepared-but-not-published, per this
      role's Hard Rules — a normal, reportable state, not a failure.
- [x] Learnings recorded — §4
- [x] Line budget respected: Ist 91 / Soll ~100 (excluding HTML comments)
- [ ] Status set to `released`/`handed-off` — **not yet**: stays `preparing`
      until the user's explicit go authorizes the push/PR steps in §3

---

## Rollback path

- **Anchor:** `origin/main` is at `2ec691c`, unchanged — confirmed live via
  `git fetch origin main` + `git rev-parse origin/main`. Nothing has been pushed;
  `main` is exactly as it was before this pass started.
- **Before commit (now):** `git restore --staged .spark/graph-mcp-verification/`
  fully undoes the staging with zero trace — nothing committed, nothing to revert.
- **After local commit, before push:** `git reset --soft HEAD~1` unwinds the
  release commit while keeping the working tree; the untracked feature files
  return to their current staged/unstaged state.
- **After push, before merge:** `git push origin --delete feat/graph-mcp-verification`
  removes the remote branch; the PR (once opened) closes itself with nothing
  merged into `main`.
- **After merge (future, outside this role's control):** `git revert -m 1
  <merge-commit>` on `main` removes the six `.spark/graph-mcp-verification/**`
  files this release adds. No tag exists to remove (none was cut, per `pr` mode).

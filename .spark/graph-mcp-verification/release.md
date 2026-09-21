# Release: graph-mcp-verification

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 3), `qa.md` (`passed`, round 1) |
| **Status** | `handed-off` |
| **Version** | v0.11.0 (**unbumped** — no bump proposed) |
| **Date** | 2026-09-21 |

**Handoff**
- **Status:** `handed-off` — PR [#55](https://github.com/a-lottes/aSPARK/pull/55)
  is open (`state: OPEN`, `mergeable: MERGEABLE`) against `main`; branch
  `feat/graph-mcp-verification` is pushed and tracking `origin/feat/graph-mcp-verification`.
  `claude plugin validate .` re-run fresh on the pushed commit (`ec3e151`,
  identical to the local pre-flight commit — nothing changed in between):
  passed, one pre-existing `autoUpdate` warning. Real merge and any tag happen
  outside this ceremony's control, on the maintainer's own timeline.
- **Summary:** Verify-only sweep re-checked GitHub issues #8, #10, #11 (optional
  `aspark-graph`/MCP integration) live; all three confirmed and closeable with
  evidence, zero Core defects found. No capability added, no behavior changed.
- **Open:** `1 outstanding` — self-review and merge by the declared approver
  (`a-lottes`), outside this role's control. Issues #8/#10/#11 are referenced
  by number in the PR body but left for the maintainer to close by hand,
  matching this repo's own convention (no merged PR here has ever used a
  `Closes #`/`Fixes #` auto-close keyword with a real number; the one
  analogous verification issue, #9, was closed manually with no linked PR).
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except
  `Status`/`Version`; log the mismatch at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Run fresh, on commit `2ec691c` (branch tip before this pass's own commit); re-confirmed on the pushed commit `ec3e151` at execute time.*

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
- [x] No uncommitted changes in the working tree — clean except the pre-existing,
      never-committed guard-hook ledger `.spark/.guard/` (unrelated to this
      feature's authorship; review F1 already disclosed and routed this).
- [x] Branch staleness (project `CLAUDE.md` caution) — `git fetch origin main`;
      `git rev-parse HEAD origin/main main` all three return `2ec691c` — identical,
      zero drift at pre-flight time. Nothing merged into `main` since this branch
      was cut; not stale.
- [x] `claude plugin validate .` run live — **passed** at pre-flight and re-run
      fresh again on the pushed commit `ec3e151` post-push: same result, one
      pre-existing `autoUpdate` warning unrelated to this diff, present on every
      prior release.
- [x] Fence re-check — `git diff --name-only origin/main..HEAD` touches only
      `.spark/graph-mcp-verification/**`; `skills/ agents/ tools/ lenses/
      templates/ .claude-plugin/plugin.json` byte-identical to `origin/main`;
      `plugin.json` still `0.11.0`.

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
| Version bump & tag | **Not executed — no bump.** Spec NFR-2 requires this verify-only sweep's fence to leave `.claude-plugin/plugin.json` byte-identical. Version stays `0.11.0`. No tag — none before merge in `pr` mode; the real tag, if any, happens post-merge, outside this role's control. |
| PR / merge | **Executed.** `git push -u origin feat/graph-mcp-verification` → branch pushed, tracking `origin/feat/graph-mcp-verification`. `gh pr create --base main --head feat/graph-mcp-verification` → [PR #55](https://github.com/a-lottes/aSPARK/pull/55) opened, body drawn from §2 above. Confirmed via `gh pr view 55`: `state: OPEN`, `mergeable: MERGEABLE`. Self-review and merge by the declared approver (`a-lottes`) remains outstanding, outside this role's control. |
| Deploy | N/A — no deploy surface; the plugin is installed by consumers via `/plugin install`, never deployed by this repo (constitution §2). |
| Post-release smoke check | N/A, named not dropped — `pr` mode, nothing deployed. Per constitution §7 the `handed-off` checkpoint is PR-open + `claude plugin validate .` passing locally on the pushed commit, both now confirmed (PR #55 `OPEN`/`MERGEABLE`; validate passed on `ec3e151`). No CI exists to be green (no `.github/workflows/`). A real merge, any tag, and an install-time smoke check of the merged result are the next owner's (`a-lottes`'s) job, outside this pass. |

## 4. Learnings (Keep!)

- **What went well:** three review rounds plus one QA round each re-derived the
  same facts from primary source (raw JSONL, live `claude mcp list`, live
  restoration probes) rather than trusting the prior round's label — zero drift
  across the whole cycle. A real technical constraint (an `Agent`-tool subagent
  shares its parent session's already-loaded MCP tool set, so it can never see
  a server registered mid-session) was solved for real rather than assumed
  away: genuinely fresh `claude -p ... --permission-mode bypassPermissions`
  processes, which read MCP config at their own start (review T7, `evidence.md:214`).
- **What we'd do differently:** F3's fix pass (re-running a ceremony step as a
  real fresh process instead of a subagent simulation) silently invalidated an
  already-recorded waiver's factual claim — M8 said "never `~/aSPARK`" for
  bypassed runs, but F3's own fix ran a fifth such process with
  `cwd=~/aSPARK`. Round 2 caught this as F11 (Major) only because it re-derived
  M8's claim from the session files rather than trusting the label; a naive
  "F2 is waived, don't revisit it" reading would have let a stale waiver ship.
  Two Majors (F2, F11) needed the user's explicit waiver rather than a clean
  fix — catching plan-deviation execution modes (T7) at `/peer-review` round 1
  would avoid a late-cycle waiver negotiation next time.
- **Patterns worth reusing:** (1) disclosing a machine-state artifact precisely
  instead of waving it off as "unrelated" — already routed to this repo's
  `CLAUDE.md`. (2) A fix to one finding can silently invalidate another
  finding's already-recorded waiver in the same round — re-derive a waiver's
  stated facts after any later fix pass, not only before it. (3) The
  fresh-subagent-can't-see-mid-session-MCP-registrations constraint and its
  `claude -p --permission-mode bypassPermissions` fix is a reusable technique
  for any future MCP-behavior verification in this repo. (2) and (3) are
  flagged as CLAUDE.md candidates for the user's consent, not yet written.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. Checked only where genuinely true today.*

- [x] All pre-flight checks passed at release time — §1, all fresh, re-confirmed
      on the pushed commit
- [x] Changelog written in user-facing language — §2
- [x] Release actions executed and verified — §3: branch pushed and tracking,
      PR #55 open and mergeable, `claude plugin validate .` green on the pushed
      commit. Merge itself is explicitly outside this role's control (`pr` mode).
- [x] Learnings recorded — §4
- [x] Line budget respected: Ist 94 / Soll ~100 (excluding HTML comments)
- [x] Status set to `released`/`handed-off` — `handed-off`, per constitution §7
      (`pr` mode's terminal status), now that PR #55 is open and validate passes
      on the pushed commit

---

## Rollback path

- **Anchor:** `origin/main` is at `2ec691c`, unchanged by this release — the PR
  is open, not merged. `main` is exactly as it was before this pass started.
- **Before commit:** n/a — the release commit (`ec3e151`) already exists from
  the prior pass.
- **After local commit, before push:** n/a — already pushed this pass.
- **After push, before merge (current state):** `git push origin --delete
  feat/graph-mcp-verification` removes the remote branch; PR #55 closes itself
  with nothing merged into `main`. `git branch -D feat/graph-mcp-verification`
  removes the local branch if desired; the release commit remains reachable
  via its hash (`ec3e151`) until garbage-collected.
- **After merge (future, outside this role's control):** `git revert -m 1
  <merge-commit>` on `main` removes the six `.spark/graph-mcp-verification/**`
  files this release adds. No tag exists to remove (none was cut, per `pr` mode).

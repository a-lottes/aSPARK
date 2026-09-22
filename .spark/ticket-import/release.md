# Release: ticket-import

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 2), `qa.md` (`passed`, round 2) |
| **Status** | `handed-off` |
| **Version** | v0.12.0 (proposed, `pr` mode — no tag created before merge; real tag lands at/after merge, outside this ceremony's control) |
| **Date** | 2026-09-22 |

**Handoff**
- **Status:** `handed-off` — PR #57 opened into `main` (https://github.com/a-lottes/aSPARK/pull/57), branch `feat/ticket-import` pushed and tracking `origin/feat/ticket-import`, `claude plugin validate .` re-run green on the pushed commit `84e94f0`. This ceremony's own work is done.
- **Summary:** `/story-time` can now start from a real GitHub issue number instead of retyping it; `/go-live` can post one status comment back to a feature's tracked issue when a project opts in via a new constitution field (default `none`, zero change for everyone else). Both gates `passed` round 2; proposed minor bump `0.11.0` → `0.12.0`; `pr` mode, PR #57 open and awaiting the declared approver's self-review and merge.
- **Open:** `1 outstanding` — self-review and merge by the declared approver (`a-lottes`), and the real tag cut at/after merge, both outside this ceremony's control. This repo's own `Tracker write-back` field is absent from its constitution, so no ticket-comment step applies (unchanged from the prepare pass).
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Re-run fresh, this session, on `feat/ticket-import` — gates checked at `a0b6054` (pre-commit); working-tree/build/validate checks re-confirmed after the release-prep commit below — not copied from `review.md`/`qa.md`. Release-prep commit: `84e94f0`.*

- [x] `review.md` status is `passed` — REVIEW GATE at `review.md:110-121` read fresh: no open Blocker, no open Major (F1–F3 all `fixed r2`, re-verified by the Reviewer against primary source), every Must AC traces to code, all plan deviations documented, line budget 121/150, status `passed`.
- [x] `qa.md` status is `passed` — QA GATE at `qa.md:71-82` read fresh: every Must-story AC verified (AC-1.5 stays an inherited, disclosed partial — a live-firing proof gap, not a behavior failure), every declared-method-observable NFR verified, no open Blocker/Major (B1 `fixed r2`), line budget 82/130, status `passed`. **QA method:** constitution §8 carries a complete declaration (`Browser-observable surface: no`, substitute method named — hands-on QA against the installed plugin) — QA ran by that declared method as this project's standing fact (§8, added 2026-08-29), not a per-feature override or a waiver for this release; `qa.md` records every `AC-`/`NFR-` ID it owns, same as always.
- [x] Full test suite green — N/A, none exists or is possible for prompt material (constitution §4). Substitute bar re-run fresh: `claude plugin validate .` → `✔ Validation passed with warnings` (one pre-existing `autoUpdate` warning, unrelated to this diff, present on every prior release).
- [x] Build succeeds from a clean checkout — N/A, no build step (constitution §3/§4); the validate run above is the equivalent bar and passed.
- [x] No uncommitted changes in the working tree — resolved in the prepare pass (`.spark/ticket-import/qa.md` committed); re-checked again just now, before push: `git status --porcelain` shows only the pre-existing, out-of-scope `.spark/.guard/` — unchanged, no tracked file left uncommitted.

**Branch staleness (project `CLAUDE.md` house rule) — checked twice, not once.** Prepare pass: `origin/main` (`bfa2389`) 6 commits ahead of the branch's merge-base `2ec691c` (`graph-mcp-verification` PR #55, `loop-cost-in-readme` PR #56), zero conflicts. **Execute pass, immediately before push, re-checked fresh rather than trusted from the prepare pass:** `git fetch origin main` → `origin/main` still `bfa2389`, unmoved since the prepare pass. `git merge-tree $(git merge-base HEAD origin/main) HEAD origin/main` → zero `<<<<<<<` conflict markers across the full dry-run output. Safe to push into unchanged ground.

**Diff re-derived fresh, not cited.** `git diff origin/main...feat/ticket-import --stat` (excluding `.spark/`) → 7 files, `+109/−22`: `README.md`, `ROADMAP.md`, `agents/release-manager.md`, `docs/status.md`, `skills/go-live/SKILL.md`, `skills/story-time/SKILL.md`, `templates/constitution.md`. Matches `review.md`'s cited 7-file, no-`.spark` scope.

**Version confirmed pre-bump.** `.claude-plugin/plugin.json` read directly before editing: `"version": "0.11.0"` (the immediately prior release, `graph-mcp-verification`, was a verify-only sweep that shipped **unbumped**).

**Version bump justification (one line).** Minor: `0.11.0` → `0.12.0` — purely additive per spec NFR-1: no protected heading/row/column/ID pattern in constitution §3's table is touched, `templates/spec.md`'s existing `Ticket` row is reused unchanged, and the one new field lives in `templates/constitution.md`, which `aspark-graph` never parses. Confirmed by `/peer-review` (round 2, F1–F3 closed).

**Ticket-reference note (verified, not assumed).** This feature's own `spec.md` header carries `Ticket: #19` — a deliberate, disclosed dogfood exception (clarifications A3/C4). This repo's constitution §7 has **no `Tracker write-back` field at all** (absent, not `none`) — per this feature's own AC-2.4, absent/`none` means zero tracker calls and the report never mentions write-back, independent of the `Ticket` value. No ticket-comment step applies to this release for that reason; this note is the one and only mention, confined to this pre-flight record. (The PR body still names #19 for the maintainer's own hand-close on merge — this is a PR-description convention, not the write-back mechanism, and the two are unrelated per the Hard Rules' changelog exemption.)

## 2. Changelog

### Added
- Starting a new piece of work (`/story-time`) can now begin from a real GitHub issue number instead of retyping its title and description by hand — pass the issue number and the tool fetches it, then still asks all the same clarifying questions it always has.
- Teams that track work in GitHub Issues can opt in, once, to having a finished release post a single status update back to the issue it came from — so the tracker stops sitting silently "open" once the work is actually done, approved, or handed off.

### Changed
- Nothing changes in how existing work is planned, reviewed or released unless a maintainer actively passes an issue number or opts a project into status updates — every other project sees identical behavior to before.

### Fixed
- Nothing — this release adds capability, it does not correct a defect.

**Honestly, what's not proven yet (per spec NFR-9):** the failure-handling path (missing/unreachable `gh` command) and the "no ticket on file" skip path are confirmed only by reading the code, not by triggering them live; and neither the import half nor the status-update half has yet been exercised on a project outside this one. Full detail: `docs/status.md:87`.

## 3. Release Actions

*Outward-facing steps executed this pass, with explicit user go received in-conversation.*

| Action | Result |
|---|---|
| Version bump & tag | Applied and pushed: `.claude-plugin/plugin.json` `0.11.0` → `0.12.0`, on `feat/ticket-import`, now on `origin/feat/ticket-import`. No tag — `pr` mode creates the real tag at/after merge, outside this ceremony's control. |
| PR / merge | **Opened.** PR #57, https://github.com/a-lottes/aSPARK/pull/57. `gh pr view 57 --json state,mergeable` → `state: OPEN`, `mergeable: MERGEABLE`. Body drawn from §2's changelog; issue #19 named, left for the maintainer to close by hand on merge — this repo's own convention (PR #55, no `Closes #` keyword; re-confirmed by reading PR #55's body before drafting this one). Self-review/merge by the declared approver (`a-lottes`) is the only step left, outside this ceremony's control. |
| Deploy | N/A — no deploy surface; consumers pull via `/plugin install` / marketplace update, not a push from here. |
| Post-release smoke check | N/A in the CI/deploy sense — this mode's real checkpoint (PR-open + `claude plugin validate .` green on the pushed commit) is done: re-run on `84e94f0` → `✔ Validation passed with warnings` (same one pre-existing `autoUpdate` warning). No live install-time smoke test performed — that is the next owner's job, after merge (see §5). |

**Release-prep commit** (local, made in the prepare pass, now pushed as part of `feat/ticket-import`):
```
chore: prepare ticket-import release, propose v0.12.0 (pr mode, awaiting go)

Bumps .claude-plugin/plugin.json 0.11.0 -> 0.12.0 (minor: additive only
per NFR-1 -- optional /story-time argument, one new constitution field,
new opt-in logic in release-manager.md; no protected templates/ structure
renamed or removed). review.md (passed, round 2) and qa.md (passed,
round 2) both fresh-verified green at pre-flight; claude plugin
validate . re-run clean (one pre-existing, unrelated warning). Also
commits .spark/ticket-import/qa.md, left untracked by /demo-day (same
gap situational-lenses hit at its own /go-live). Branch is 6 commits
behind origin/main (graph-mcp-verification PR #55, loop-cost-in-readme
PR #56) but a dry-run git merge-tree shows zero conflicts against the
current diff -- both shared README.md edits land on non-overlapping
line ranges. No tag, no push, no PR yet -- pr mode, prepared and
awaiting the user's explicit go. See .spark/ticket-import/release.md.

Co-Authored-By: Claude Sonnet 5 <noreply@anthropic.com>
```

**Publish commands, executed this pass:**
```
$ git push -u origin feat/ticket-import
 * [new branch]      feat/ticket-import -> feat/ticket-import
branch 'feat/ticket-import' set up to track 'origin/feat/ticket-import'.
```
```
$ gh pr create --base main --head feat/ticket-import \
  --title "feat: ticket import into /story-time, status write-back on /go-live" \
  --body-file <drafted from §2's changelog + PR/merge row above>
https://github.com/a-lottes/aSPARK/pull/57
```
```
$ gh pr view 57 --json state,mergeable,url,number
{"mergeable":"MERGEABLE","number":57,"state":"OPEN","url":"https://github.com/a-lottes/aSPARK/pull/57"}
```

**Rollback path.** Purely additive (NFR-1): no protected template heading, row, column, ID pattern, or slash command is renamed or removed; the one new constitution field defaults to `none` and the new `/story-time` argument is optional. **Before merge (current state):** PR #57 is open, not yet merged — don't merge / close the PR; `origin/main` stays unaffected, and the pushed branch can be deleted without consequence. **After merge:** `git revert -m 1 <merge-commit-sha>` on `main` restores all 7 non-`.spark` files and the version bump in one commit; no tag exists yet to delete (`pr` mode cuts the real tag at/after merge). Safe because every project that has not opted into the new `Tracker write-back` field, and has not passed an issue number to `/story-time`, sees zero behavioral difference whether this release is reverted or not.

## 4. Learnings (Keep!)

- **What went well:** the read/write split from clarification A2 (a per-run CLI argument needs no constitution declaration; an outward-facing side effect on a third party's tracker does) held up cleanly through Review and QA with no rework, and let the feature prove its read half live on this repo's own real issue while proving its write half safely in a disposable scratch repo rather than risking a spurious comment on this repo's own tracker. Three genuine gate rounds each caught something real, not a rubber stamp: `/peer-review` round 1 found actual logic gaps (F1 missing `--repo` pinning on the write path, an irreversible-comment risk; F2 an idempotence key that a skip-write itself destroyed; F3 the negative case's own subagent invocation never having run); round 2's re-verification, checking primary source (session transcripts) rather than the self-report, found F12 — the fix landed and the logic is sound, but the shipped guard's URL-keyed behavior had never actually been exercised live, only walked through, and two docs still cited the old evidence as current proof; `/demo-day` then independently caught B1 — the `review.md` this gate was told to trust as `passed`/round 2 was still uncommitted, `HEAD` carried round 1's `changes-requested`, and a lost working tree would have silently reverted the record.
- **What we'd do differently:** `qa.md` reached `/go-live` uncommitted for the second time this project's history (`situational-lenses` hit the identical gap) — worth adding a close-out check to `/demo-day`'s own SKILL that commits or explicitly flags its own deliverable before handing off, rather than relying on the next `/go-live` to catch it.
- **Patterns worth reusing (candidates for `CLAUDE.md`):** this feature's own clarification A2 — "could the constitution know this?" as the placement test for whether a capability needs a standing declaration vs. a per-run argument — is a reusable shape for any future feature that has to choose between the two. Also a sharper, more general form of an existing entry: this loop's B1/F12 both show a *report's own gate verdict* can drift from its committed record between the moment it's written and the moment a later gate reads it — the same class `CLAUDE.md`'s "re-verify at every gate" and "check branch staleness" entries already name for evidence and branch position, but not yet for a gate report's own `Status` field specifically.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time (§1 — 5/5; branch-staleness re-checked twice — prepare pass and immediately before push — both clean, `origin/main` unmoved between the two)
- [x] Changelog written in user-facing language (§2 — no commit hashes, ticket IDs or internal jargon)
- [x] Release actions executed and verified — push done (`feat/ticket-import` tracking `origin/feat/ticket-import`), PR #57 open and confirmed `OPEN`/`MERGEABLE`, `claude plugin validate .` re-run green on the pushed commit. Rollback path written (§3).
- [x] Learnings recorded (§4)
- [x] Line budget respected: Ist 121 / Soll ~100 (excluding HTML comments; none used) — over Soll for the same reason as the prepare pass: the branch-staleness re-derivation and the full publish-command record are kept so this report's own claims stay independently checkable rather than asserted.
- [x] Status set to `released`/`handed-off` — `handed-off` (this repo's `pr`-mode terminal status, constitution §7). What remains outstanding: self-review and merge by the declared approver (`a-lottes`); the real tag is cut at/after merge, outside this ceremony's control. This report describes a PR open and awaiting merge — not a shipped release.

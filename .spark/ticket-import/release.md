# Release: ticket-import

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 2), `qa.md` (`passed`, round 2) |
| **Status** | `preparing` |
| **Version** | v0.12.0 (proposed, `pr` mode — no tag created before merge) |
| **Date** | 2026-09-22 |

**Handoff**
- **Status:** `preparing` — prepare-only pass. Local prep done (version bump, release commit staged, this report); no push, no PR, no tag. Awaiting the user's explicit go for the outward-facing steps listed in §3.
- **Summary:** `/story-time` can now start from a real GitHub issue number instead of retyping it; `/go-live` can post one status comment back to a feature's tracked issue when a project opts in via a new constitution field (default `none`, zero change for everyone else). Both gates `passed` round 2; proposed minor bump `0.11.0` → `0.12.0`; `pr` mode, prepared and awaiting go.
- **Open:** `2 outstanding` — the outward-facing publish steps (push, PR open) are pending the user's go (§3); after the go, self-review/merge by the declared approver (`a-lottes`) remains outside this ceremony's control. This repo's own `Tracker write-back` field is absent from its constitution, so no ticket-comment step applies to this release regardless of the go (see §1 note).
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed.

## 1. Pre-Flight Checks

*Re-run fresh, this session, on `feat/ticket-import` — gates checked at `a0b6054` (pre-commit); working-tree/build/validate checks re-confirmed after the release-prep commit below — not copied from `review.md`/`qa.md`. (This report is written into that same commit, so it cannot cite its own final hash without going stale on the next edit; verify with `git log -1 --format=%H` on `feat/ticket-import`.)*

- [x] `review.md` status is `passed` — REVIEW GATE at `review.md:110-121` read fresh: no open Blocker, no open Major (F1–F3 all `fixed r2`, re-verified by the Reviewer against primary source), every Must AC traces to code, all plan deviations documented, line budget 121/150, status `passed`.
- [x] `qa.md` status is `passed` — QA GATE at `qa.md:71-82` read fresh: every Must-story AC verified (AC-1.5 stays an inherited, disclosed partial — a live-firing proof gap, not a behavior failure), every declared-method-observable NFR verified, no open Blocker/Major (B1 `fixed r2`), line budget 82/130, status `passed`. **QA method:** constitution §8 carries a complete declaration (`Browser-observable surface: no`, substitute method named — hands-on QA against the installed plugin) — QA ran by that declared method as this project's standing fact (§8, added 2026-08-29), not a per-feature override or a waiver for this release; `qa.md` records every `AC-`/`NFR-` ID it owns, same as always.
- [x] Full test suite green — N/A, none exists or is possible for prompt material (constitution §4). Substitute bar re-run fresh: `claude plugin validate .` → `✔ Validation passed with warnings` (one pre-existing `autoUpdate` warning, unrelated to this diff, present on every prior release).
- [x] Build succeeds from a clean checkout — N/A, no build step (constitution §3/§4); the validate run above is the equivalent bar and passed.
- [x] No uncommitted changes in the working tree — **not clean at pre-flight**: `.spark/ticket-import/qa.md` (this feature's own round-2 QA deliverable) was untracked, never committed by `/demo-day` (its own Handoff block flags this: "this round's own `qa.md` rewrite, not yet committed"). Same gap `situational-lenses` hit at its own `/go-live` — resolved the same way, included in this pass's release-prep commit (below) rather than deferred. Re-checked after committing: `git status --porcelain` now shows only the pre-existing, out-of-scope `.spark/.guard/` (the optional `aspark-guard` companion plugin's own session ledger) — no tracked file left uncommitted.

**Branch staleness (project `CLAUDE.md` house rule, re-checked live, not taken on trust).** `git fetch origin main` → local `main` (`2ec691c`) is **6 commits behind** `origin/main` (`bfa2389`): `graph-mcp-verification` (PR #55, merged) and `loop-cost-in-readme` (PR #56, merged) landed since this branch was cut. Both touch `README.md`; `graph-mcp-verification` also touches `CLAUDE.md` and its own `.spark/graph-mcp-verification/*`. `git merge-base feat/ticket-import origin/main` = `2ec691c`, confirming the branch was cut from exactly that point (no drift within the branch itself). `git merge-tree 2ec691c feat/ticket-import origin/main` → **zero conflict markers**, exit `0`. Direct diff check on the one shared file: `origin/main`'s new paragraph lands at `README.md:127-129` ("What one loop costs"); this branch's edits land at `README.md:104-112` (the ceremony table rows) — non-overlapping ranges. No rebase required for a clean PR merge; will be re-checked immediately before push, per the same house rule.

**Diff re-derived fresh, not cited.** `git diff origin/main...feat/ticket-import --stat` (excluding `.spark/`) → 7 files, `+109/−22`: `README.md`, `ROADMAP.md`, `agents/release-manager.md`, `docs/status.md`, `skills/go-live/SKILL.md`, `skills/story-time/SKILL.md`, `templates/constitution.md`. Matches `review.md`'s cited 7-file, no-`.spark` scope (its own count was `+87/−17`, a minor recount variance that changes no verdict).

**Version confirmed pre-bump.** `.claude-plugin/plugin.json` read directly before editing: `"version": "0.11.0"` (the immediately prior release, `graph-mcp-verification`, was a verify-only sweep that shipped **unbumped**).

**Version bump justification (one line).** Minor: `0.11.0` → `0.12.0` — purely additive per spec NFR-1: no protected heading/row/column/ID pattern in constitution §3's table is touched, `templates/spec.md`'s existing `Ticket` row is reused unchanged, and the one new field lives in `templates/constitution.md`, which `aspark-graph` never parses. Confirmed by `/peer-review` (round 2, F1–F3 closed).

**Ticket-reference note (verified, not assumed).** This feature's own `spec.md` header carries `Ticket: #19` — a deliberate, disclosed dogfood exception (clarifications A3/C4): the read half's positive case was proven against this repo's own real, already-public issue, while this repo's constitution §7 `Ticket-reference format: none` is otherwise left unamended. This repo's constitution §7 has **no `Tracker write-back` field at all** (absent, not `none`) — per this feature's own AC-2.4, absent/`none` means zero tracker calls and the report never mentions write-back, independent of the `Ticket` value. No ticket-comment step applies to this release for that reason; this note is the one and only mention, confined to this pre-flight record.

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

*Local, reversible prep only, this pass — no outward-facing action taken. Publish commands below are drafted and pending, not executed.*

| Action | Result |
|---|---|
| Version bump & tag | **Applied, locally, not yet on `main`.** `.claude-plugin/plugin.json` `0.11.0` → `0.12.0`, committed on `feat/ticket-import` in this pass's release-prep commit (justification above). Not pushed. No tag — `pr` mode creates the real tag at/after merge, outside this ceremony's control. |
| PR / merge | **Not opened.** Pending the user's go. Exact commands below. |
| Deploy | N/A — no deploy surface; consumers pull via `/plugin install` / marketplace update, not a push from here. |
| Post-release smoke check | N/A this pass — nothing published yet. This mode's actual equivalent (`claude plugin validate .`) already re-run clean at pre-flight above; will be re-run again immediately after push, per house rule. |

**Release-prep commit, made this pass (local only, not pushed — outward-facing steps still require a separate, explicit go):**
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
Files: `.claude-plugin/plugin.json`, `.spark/ticket-import/qa.md`, `.spark/ticket-import/release.md`. Committed on `feat/ticket-import` (`git log -1 --format=%H` on that branch is authoritative; not cited here by hash to avoid this report going stale on its own amend).

**Publish commands, pending the user's explicit go — none of these have been run:**
```
git push -u origin feat/ticket-import
```
```
gh pr create --title "feat: ticket import into /story-time, status write-back on /go-live" \
  --base main --head feat/ticket-import --body "$(cat <<'EOF'
## Summary
- /story-time <issue-number> fetches a real GitHub issue (gh issue view,
  pinned to the resolved repo) and hands its title/body to the Product
  Owner as the seed idea -- the full interrogation still runs unchanged.
- /go-live can post exactly one gh issue comment to a feature's tracked
  issue, stating the terminal status, version/PR reference and a link to
  the release artifact -- only when a project opts in via the new
  constitution field `Tracker write-back` (default none, zero change for
  every existing project). Guarded against re-posting on a later release
  pass for the same feature.
- Proposes a minor bump, 0.11.0 -> 0.12.0 (purely additive, NFR-1).

## Test plan
- [x] review.md passed, round 2 (F1-F3 Majors fixed and independently
      re-verified against source)
- [x] qa.md passed, round 2 (B1 fixed and confirmed via committed blob)
- [x] claude plugin validate . passes locally (re-run at /go-live
      pre-flight; one pre-existing, out-of-scope warning)
- [x] Dry-run git merge-tree against current origin/main: zero conflicts
- [ ] Self-review and merge by the declared approver (a-lottes)
EOF
)"
```

**Rollback path.** Purely additive (NFR-1): no protected template heading, row, column, ID pattern, or slash command is renamed or removed; the one new constitution field defaults to `none` and the new `/story-time` argument is optional. Before merge: don't merge / close the PR — `origin/main` stays unaffected, nothing has been pushed yet at the time of writing. After merge: `git revert -m 1 <merge-commit-sha>` on `main` restores all 7 non-`.spark` files and the version bump in one commit; no tag exists yet to delete (`pr` mode cuts the real tag at/after merge). Safe because every project that has not opted into the new `Tracker write-back` field, and has not passed an issue number to `/story-time`, sees zero behavioral difference whether this release is reverted or not — reverting returns every consumer to exactly its prior behavior, never a broken one.

## 4. Learnings (Keep!)

- **What went well:** the read/write split from clarification A2 (a per-run CLI argument needs no constitution declaration; an outward-facing side effect on a third party's tracker does) held up cleanly through Review and QA with no rework, and let the feature prove its read half live on this repo's own real issue while proving its write half safely in a disposable scratch repo rather than risking a spurious comment on this repo's own tracker.
- **What we'd do differently:** `qa.md` reached `/go-live` uncommitted for the second time this project's history (`situational-lenses` hit the identical gap) — worth adding a close-out check to `/demo-day`'s own SKILL that commits or explicitly flags its own deliverable before handing off, rather than relying on the next `/go-live` to catch it.
- **Patterns worth reusing (candidates for `CLAUDE.md`):** this feature's own clarification A2 — "could the constitution know this?" as the placement test for whether a capability needs a standing declaration vs. a per-run argument — is a reusable shape for any future feature that has to choose between the two.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time (§1 — 5/5, with the one finding, uncommitted `qa.md`, resolved within this prepare pass rather than deferred; branch-staleness re-check run this pass and will re-run immediately before push, per house rule)
- [x] Changelog written in user-facing language (§2 — no commit hashes, ticket IDs or internal jargon)
- [ ] Release actions executed and verified — **not yet**: this is a prepare-only pass. Local prep (version bump, release-prep commit content, drafted PR body) is ready above; push and PR-open are pending the user's explicit go (§3). Rollback path is written (§3, above).
- [x] Learnings recorded (§4)
- [x] Line budget respected: Ist 136 / Soll ~100 (excluding HTML comments; none used) — over Soll; the branch-staleness re-derivation, the ticket-reference verification note, and the full drafted PR body/commit text needed to make the pending publish commands exact and copy-pasteable (§1/§3) account for the overrun, each kept to make this report's own claims independently checkable rather than asserted.
- [ ] Status set to `released`/`handed-off` — **not yet**: `Status: preparing`. This report is presented to the user as "prepared, awaiting go" per `skills/go-live/SKILL.md` step 2; on receiving explicit authorization, a follow-up pass runs the push/PR-open commands above, re-verifies the pre-push checks, and updates this report's Status to `handed-off` (this repo's `pr`-mode terminal status, constitution §7) — never `released`.

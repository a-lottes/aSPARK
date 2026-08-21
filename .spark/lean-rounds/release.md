# Release: lean-rounds

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 3); `qa.md` — **does not exist**, user-directed skip (see below) |
| **Status** | `preparing` |
| **Version** | v0.7.0 (**proposed only** — `pr` mode, no tag before merge) |
| **Date** | 2026-08-21 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`/`Version`).
- **Summary:** Review gate green (r3, 0 Blockers/Majors). QA gate was **not run** — the user explicitly chose to skip `/demo-day` entirely for this feature (recorded below as a gate override, not a silent bypass). Fresh pre-flight passed; local release commit + branch prepared; nothing pushed.
- **Open:** `1 outstanding` — push branch, open PR, request self-review; all outside this role's authority without the user's explicit go. Owner: the user (`a-lottes`).
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`.

**⚠ Recorded gate override (QA), per the Hard Rule that every override is the user's call, recorded with reason.** `.spark/lean-rounds/qa.md` does not exist. The user explicitly chose to skip `/demo-day` outright for this feature — not to fake-run it — after being told: aSPARK ships zero UI (constitution §2: `seo`/`ux` lenses off), so `/demo-day`'s browser-click gate cannot be meaningfully satisfied here. Two prior features (`lean-artifacts`, `graph-gates`) instead used a documented ceremony-override QA method; that same option was offered for `lean-rounds` and the user declined it, citing how much verification `/peer-review` already did: 3 full rounds, with the Reviewer independently re-executing the live `~/aSPARK-graph` consumer at every round (not trusting claims), plus `/increment`'s own T8 negative-case-first dry run and positive-case fixture simulation. This is not treated as blocking; the release proceeds on the strength of the review gate alone, with this override on the record.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — read fresh: header `Status: passed`, Round 3, Handoff Verdict "Gate `passed` r3", REVIEW GATE fully checked (0 open Blockers/Majors; F7 open by design — commit hygiene, not a code defect).
- [ ] `qa.md` status is `passed` — **N/A / user override**, see above. Not silently skipped, not blocking.
- [x] Full test suite green on the release commit — N/A, no automated suite exists or is possible for prompt material (constitution §4). Ran fresh, now: `claude plugin validate .claude-plugin/plugin.json` → passed; `claude plugin validate .` (marketplace manifest) → passed with 1 warning (`autoUpdate` unknown field) — pre-existing since commit `789e33f` (2026-08-06), `marketplace.json` untouched by this diff, confirmed via `git log --follow`.
- [x] Build succeeds from a clean checkout — N/A, no build step: Markdown + JSON only (constitution §3).
- [x] No uncommitted changes in the working tree — verified fresh via `git status` immediately before staging. Two categories present: this feature's 12 tracked files + untracked `.spark/lean-rounds/` (in scope, staged by path below), and one pre-existing, unrelated untracked file, `docs/aSPARK_Enterprise_Architecture_Handbook_v1.0.docx` (review finding F7) — deliberately **excluded**, staged nothing by wildcard.

## 2. Changelog

### Added
- Review and QA reports now show a round counter, so you can tell at a glance which pass of review or testing produced what's on the page.
- All five report templates (spec, plan, review, QA, release) now check their own length against a stated target as part of finishing their checklist — previously true for only three of them.
- The QA tester now has a documented way to re-test and update a QA report after a fix is applied, matching what the reviewer could already do for review reports.

### Changed
- Re-reviewing or re-testing a feature no longer makes its review/QA report grow with every pass. Findings, test results, the summary and the pass/fail verdict are each updated in place instead of piling a new "Round 2" section on top of the last one.
- A finding that gets fixed, turns out not to be a real problem, or comes back after being fixed now always uses one of three exact words — so tooling that counts open issues reads the report's true current state.

### Fixed
- Findings raised in a second or third round of review used to end up outside the part of the report automated tooling actually reads, making them invisible to it even though a human could see them. They now always live in the place the tooling looks, every round.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | **Proposed only, no tag.** `.claude-plugin/plugin.json` bumped `0.6.0` → `0.7.0` in local release commit `b0d0761` on branch `feat/lean-rounds` (not pushed). Bump: **minor** — purely additive, no protected template heading/column/ID (constitution §3) renamed or removed, independently verified by the Reviewer against the live `aspark_graph` parser across all 3 review rounds (spec NFR-1). Per constitution §7 (`pr` mode): no tag before merge — the real tag happens at/after merge, outside this role's control. |
| PR / merge | **Prepared, not opened.** Local commit `b0d0761` made on `feat/lean-rounds` (18 files: 12 feature files + `.claude-plugin/plugin.json` + 5 new `.spark/lean-rounds/*.md` files; handbook `.docx` excluded). Push and `gh pr create` are pending the user's explicit go — see Pending commands below. |
| Deploy | N/A — handed-off mode, no deploy. |
| Post-release smoke check | N/A — handed-off mode, no deploy. |

**Pending commands (none executed — awaiting the user's explicit go):**
1. `git push -u origin feat/lean-rounds`
2. `gh pr create --base main --head feat/lean-rounds --title "feat: overwrite-in-place review/QA reports + all-five-template line-budget gate (v0.7.0, proposed)" --body "<drafted summary: §2 Changelog + gate status + version note, same shape as PR #22>"`
3. After merge: the real tag — outside this role's control regardless of authorization.

## 4. Learnings (Keep!)

- **What went well:** Risk-first sequencing (T1's walking skeleton proved the new overwrite-in-place shape against the live parser on one template before rippling to four more files). The Reviewer re-executed the real `aspark-graph` consumer live at all 3 rounds rather than trusting prior claims, catching a real gap (F5). The review process caught a misuse of its own new round-numbering rule mid-review — a self-referential, strong signal the mechanics hold.
- **What we'd do differently:** Plan's blast-radius scoping (T4) missed the one file needed to actually *trigger* the new QA re-test mode, caught only in fix-mode (F1) — future scoping for "new mode on an existing ceremony" should trace the invoking skill, not just the owning agent. F10: a spec wording amendment was made unilaterally during fix-mode on an already-`approved` spec — content was right (verified twice) but the authority wasn't fix-mode's; the user ratified it after the fact rather than a revert. Future non-UI features should default to the ceremony-override QA method before accepting an outright `/demo-day` skip, so a QA record still exists.
- **Patterns worth reusing** (candidates for `.spark/constitution.md` / project memory): walking-skeleton-first for any change touching the cross-repo template contract; uniform gate items across *all* owning agents (5-of-5, not 3-of-5) to close the "advisory-looking rule" gap named by F17; offer the ceremony-override QA method as the default before an outright skip on non-UI features.

---

## ✅ KEEP GATE

- [x] All pre-flight checks passed at release time — see §1 (QA box is a recorded user override, not a failure).
- [x] Changelog written in user-facing language — see §2; no commit hashes, ticket IDs or jargon.
- [ ] Release actions executed and verified — **not yet**: prepared only (local commit + branch), push/PR pending the user's explicit go (§3). Rollback path below.
- [x] Learnings recorded — see §4.
- [x] Line budget respected: Ist **80** / Soll ~100 (excluding HTML comments; there are none in this file) — counted via `wc -l`, same method `review.md`'s own self-report used.
- [ ] Status set to `released`/`handed-off` — **neither yet**: no outward-facing action has been authorized. Remains `preparing`. Outstanding: push, PR, self-review-request — owner: the user (`a-lottes`); the real tag/merge happens outside this role's control once a PR exists.

---

## Rollback path

- **What would need undoing:** the single local release commit on `feat/lean-rounds` (12 feature files, `.claude-plugin/plugin.json`, 5 new `.spark/lean-rounds/*.md` files). Nothing is pushed — `git branch -D feat/lean-rounds` (or simply not pushing/merging it) fully undoes this pass with zero outward trace.
- **If later pushed/merged:** a single `git revert b0d0761` on `main` restores every protected template structure, all five agents and the plugin manifest to their pre-feature state in one operation, including un-bumping `plugin.json` back to `0.6.0` — no separate version-rollback step needed.
- **No tag exists** (per `pr` mode) — nothing published to consumers/marketplace to roll back yet.

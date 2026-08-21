# Release: lean-rounds

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 3); `qa.md` — **does not exist**, user-directed skip (see below) |
| **Status** | `handed-off` |
| **Version** | v0.7.0 (**proposed only** — `pr` mode, no tag before merge) |
| **Date** | 2026-08-21 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`/`Version`).
- **Summary:** Review gate green (r3, 0 Blockers/Majors). QA gate was **not run** — the user explicitly chose to skip `/demo-day` entirely for this feature (recorded below as a gate override, not a silent bypass). Fresh pre-flight passed. User's explicit go for outward-facing action received ("committ push and release"). Push done and confirmed live. `gh pr create` was denied twice at the release-manager subagent's own permission level (a delegated-tool-permission wall, same spot `lean-artifacts` hit for PR #22) — run instead from the orchestrating session, which held the permission, and succeeded: **[PR #23](https://github.com/a-lottes/aSPARK/pull/23)** is open against `main`.
- **Open:** `1 outstanding` — self-review and merge the PR. Owner: the user (`a-lottes`), the declared approver (constitution §7). The real tag happens at/after that merge, outside this role's control either way.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`.

**⚠ Recorded gate override (QA), per the Hard Rule that every override is the user's call, recorded with reason.** `.spark/lean-rounds/qa.md` does not exist. The user explicitly chose to skip `/demo-day` outright for this feature — not to fake-run it — after being told: aSPARK ships zero UI (constitution §2: `seo`/`ux` lenses off), so `/demo-day`'s browser-click gate cannot be meaningfully satisfied here. Two prior features (`lean-artifacts`, `graph-gates`) instead used a documented ceremony-override QA method; that same option was offered for `lean-rounds` and the user declined it, citing how much verification `/peer-review` already did: 3 full rounds, with the Reviewer independently re-executing the live `~/aSPARK-graph` consumer at every round (not trusting claims), plus `/increment`'s own T8 negative-case-first dry run and positive-case fixture simulation. Not treated as blocking; the release proceeds on the strength of the review gate alone, with this override on the record.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — read fresh: header `Status: passed`, Round 3, Handoff Verdict "Gate `passed` r3", REVIEW GATE fully checked (0 open Blockers/Majors; F7 open by design — commit hygiene, not a code defect).
- [ ] `qa.md` status is `passed` — **N/A / user override**, see above. Not silently skipped, not blocking.
- [x] Full test suite green on the release commit — N/A, no automated suite exists or is possible for prompt material (constitution §4). Ran fresh: `claude plugin validate .claude-plugin/plugin.json` → passed; `claude plugin validate .` (marketplace manifest) → passed with 1 pre-existing, unrelated warning (`autoUpdate` field, since commit `789e33f`, `marketplace.json` untouched by this diff).
- [x] Build succeeds from a clean checkout — N/A, no build step: Markdown + JSON only (constitution §3).
- [x] No uncommitted changes in the working tree — verified fresh via `git status`. The only untracked file remaining is the pre-existing, unrelated `docs/aSPARK_Enterprise_Architecture_Handbook_v1.0.docx` (review finding F7) — deliberately excluded, never staged.

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
| Version bump & tag | **Proposed only, no tag.** `.claude-plugin/plugin.json` bumped `0.6.0` → `0.7.0` in local commits `b0d0761`/`254da89` on `feat/lean-rounds`, now **pushed**. Bump: **minor** — purely additive, no protected template heading/column/ID (constitution §3) renamed or removed, independently verified by the Reviewer against the live `aspark_graph` parser across all 3 review rounds (spec NFR-1). Per constitution §7 (`pr` mode): no tag before merge, none created — the real tag happens at/after merge, outside this role's control. |
| PR / merge | **Push and PR both done.** User's explicit go received ("committ push and release"), authorizing push and PR creation. `git push -u origin feat/lean-rounds` — done, confirmed live. `gh pr create` — denied twice at the release-manager subagent's delegated permission level (not a GitHub-side error); run instead from the orchestrating session, which held the permission — succeeded on the first attempt there. **[PR #23](https://github.com/a-lottes/aSPARK/pull/23)** open against `main`, title and body as drafted below. Self-review and merge remain the user's (constitution §7). |
| Deploy | N/A — no deploy surface exists for this project (Markdown/JSON Claude Code plugin, no runtime, no server); in `pr` mode "deploy" is the PR merging to `main`, which hasn't happened yet. |
| Post-release smoke check | N/A — nothing to smoke: no merge has happened yet. `.github/workflows/` does not exist, so "CI green" is N/A by absence, not an unchecked box. |

**PR opened — [#23](https://github.com/a-lottes/aSPARK/pull/23):**

> **Title:** `feat: overwrite-in-place review/QA reports + all-five-template line-budget gate (v0.7.0, proposed)`
>
> **Body:** the §2 Changelog above (Added/Changed/Fixed, user-facing), a **Gates** section — Review `passed` r3, 0 open Blockers/Majors; QA **not run**, user-directed skip, reason as recorded in the Handoff block above; Version `0.7.0` proposed only, no tag — an **Approval** section naming self-review-via-PR (`a-lottes`, constitution §7), and a **Test plan** checklist: `claude plugin validate` (plugin + marketplace) passed; dogfood evidence in `evidence.md`; merge-and-revalidate left as the one item outside this PR's control.

**Commands — final status:**
1. `git push -u origin feat/lean-rounds` — done, confirmed live.
2. `gh pr create` — done, from the orchestrating session after the subagent-level denial. [PR #23](https://github.com/a-lottes/aSPARK/pull/23) open.
3. After merge: the real tag — outside this role's direct control per `pr` mode, unchanged, owned by the user.

## 4. Learnings (Keep!)

- **What went well:** Risk-first sequencing (T1's walking skeleton proved the new overwrite-in-place shape against the live parser on one template before rippling to four more files). The Reviewer re-executed the real `aspark-graph` consumer live at all 3 rounds rather than trusting prior claims, catching a real gap (F5). The review process caught a misuse of its own new round-numbering rule mid-review — a self-referential, strong signal the mechanics hold.
- **What we'd do differently:** Plan's blast-radius scoping (T4) missed the one file needed to actually *trigger* the new QA re-test mode, caught only in fix-mode (F1) — future scoping for "new mode on an existing ceremony" should trace the invoking skill, not just the owning agent. F10: a spec wording amendment was made unilaterally during fix-mode on an already-`approved` spec — content was right (verified twice) but the authority wasn't fix-mode's; the user ratified it after the fact rather than a revert. Future non-UI features should default to the ceremony-override QA method before accepting an outright `/demo-day` skip, so a QA record still exists. The `gh pr create` permission denial recurred in the exact same spot as the `lean-artifacts` release — worth a standing permission grant for this specific, narrow command rather than re-discovering the wall every release.
- **Patterns worth reusing** (candidates for `.spark/constitution.md` / project memory): walking-skeleton-first for any change touching the cross-repo template contract; uniform gate items across *all* owning agents (5-of-5, not 3-of-5) to close the "advisory-looking rule" gap named by F17; offer the ceremony-override QA method as the default before an outright skip on non-UI features.

---

## ✅ KEEP GATE

- [x] All pre-flight checks passed at release time — see §1 (QA box is a recorded user override, not a failure).
- [x] Changelog written in user-facing language — see §2; no commit hashes, ticket IDs or jargon.
- [x] Release actions executed and verified — push done and confirmed live; [PR #23](https://github.com/a-lottes/aSPARK/pull/23) open against `main`, verified via `gh pr list` before and after creation. Rollback path below, now PR-aware.
- [x] Learnings recorded — see §4.
- [x] Line budget respected: Ist **87** / Soll ~100 (excluding HTML comments; there are none in this file) — counted via `wc -l`, same method `review.md`'s own self-report used.
- [x] Status set to `handed-off` — the PR is genuinely open (constitution §7's condition for this status). **Outstanding: self-review and merge** — **owner: the user (`a-lottes`)**, the declared approver; the real tag happens at/after that merge, outside this role's control either way.

---

## Rollback path

- **What would need undoing:** three commits (`b0d0761`, `254da89`, `7fe334d`) pushed to `origin/feat/lean-rounds`, and [PR #23](https://github.com/a-lottes/aSPARK/pull/23), now open against `main`. Nothing has merged, so `main` itself is untouched.
- **Before merge:** close PR #23 (`gh pr close 23`) and delete the branch — `git push origin --delete feat/lean-rounds` (and locally, `git branch -D feat/lean-rounds`). No tag exists yet, so nothing else to unwind.
- **After merge:** a single `git revert b0d0761` (and `254da89`/`7fe334d` if also merged) on `main` restores every protected template structure, all five agents and the plugin manifest to their pre-feature state in one operation, including un-bumping `plugin.json` back to `0.6.0` — no separate version-rollback step needed.
- **No tag exists** (per `pr` mode) — nothing published to the marketplace/consumers to roll back yet.

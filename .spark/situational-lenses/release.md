# Release: situational-lenses

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 5), `qa.md` (`passed`, round 1) |
| **Status** | `handed-off` |
| **Version** | v0.8.1 (**proposed only** — `pr` mode; patch bump; not tagged, not pushed) |
| **Date** | 2026-09-12 |

**Handoff**
- **Status:** `handed-off` — PR #43 is open (`main` ← `feat/situational-lenses`), mergeable, CI N/A (no `.github/workflows` in this repo), declared approver (`a-lottes`, self-review-via-PR, constitution §7) is the PR opener and has the PR to review/merge. The merge itself and the post-merge tag (`v0.8.1`) are outside this role's control and have not happened.
- **Summary:** A verify-only evidence sweep of the `lenses/` mechanism — real refutations found and routed, two privacy leaks found and fixed (one required a history squash), and a documentation restatement. No new capability ships; `lenses/`, `agents/`, `skills/`, `templates/` are untouched.
- **Open:** `2 outstanding` — (1) the merge/tag decision itself, owned by `a-lottes` as self-review-via-PR approver, on their own timeline, outside this ceremony; (2) an optional local `git gc` (review F24, Nit, not gating) the user may run or skip.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch at the next `/go-live`.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — read fresh: Handoff + REVIEW GATE, round 5. 0 open Blocker (F12 `fixed r5`, re-derived independently), 0 open Major (F20 `fixed r5`); 1 open Nit (F24, optional `git gc`), none waived because none needed waiving.
- [x] `qa.md` status is `passed` — read fresh: Handoff + QA GATE, round 1. 0 open Blocker/Major; 5 `fail` rows mirror the ledger's own routed `refuted-with-finding` verdicts exactly, 1 open Minor (B1, exploratory, non-blocking). **QA-method row:** constitution §8 carries a complete declaration (surface `no`, substitute method named) — QA ran by that declared method, against the installed plugin, as this project's standing fact (§8, added 2026-08-29), not a per-feature override or a waiver for this release; `qa.md` records every `AC-`/`NFR-` ID QA owns, same as always.
- [x] Full test suite green on the release commit — none exists, none possible for prompt material (constitution §4). Bar: `claude plugin validate .`, re-run fresh — **passed**, one pre-existing `autoUpdate` warning unrelated to this diff, present on every prior release.
- [x] Build succeeds from a clean checkout — N/A: Markdown + JSON only, no build step (constitution §3).
- [x] No uncommitted changes in the working tree — **not clean at pre-flight**: `.spark/situational-lenses/qa.md` (this feature's own QA deliverable) was untracked, never committed by `/demo-day`. Included in this pass's release commit (`d05fe22`) — completing the gate's own artifact, not a code fix.
- [x] Branch staleness (project `CLAUDE.md` caution) — checked twice: at prepare time, and again fresh before push this turn (`git fetch origin main`; `git merge-base HEAD origin/main` == `origin/main` tip `a6a086c`, both times). No commit landed on `main` between prepare and publish; not stale.
- [x] Fence re-check — `git diff --name-only origin/main -- lenses/ agents/ skills/ templates/ .claude-plugin/plugin.json` empty before this pass's own version bump; the bump itself is this release's only touch to that list, and renames/removes nothing (constitution §3 protected structures untouched).

## 2. Changelog

### Added
- Nothing new to use — this release ships no new capability. It is a verification pass over the existing situational-lenses mechanism.

### Changed
- The README's project-status table now describes what was actually checked for situational lenses — verified against this project itself and three real external projects' completed work — instead of an unverified claim.

### Fixed
- Two places where a real external project's private, non-public name briefly appeared in this repository's history were found and removed before anything was shared outside this machine; nothing leaked reached GitHub.
- A counting method that could report "zero problems found" when the real state was "nothing was actually checked" was replaced with one that checks properly in every case — it still finds the same problems it always should have.

**Found, routed, not fixed here (verify-only, by design — see `CLAUDE.md`'s standing convention):** a gap where one feature's quality checks get applied under the wrong checklist in roughly 3 of 4 projects surveyed; a place where adding a future checklist would require editing more than the one file it's supposed to be limited to; and two kinds of project (public websites, API services) that nobody has yet run this tool on, so those checks remain genuinely unproven rather than confirmed. None of these is fixed in this release; each is queued as follow-up work.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | **Executed (local only, proposed).** `.claude-plugin/plugin.json` `0.8.0` → `0.8.1` — patch: no new capability, no protected structure (constitution §3) touched; the shipped artifact is an evidence ledger plus a restated `README.md` section, the same shape as the `0.7.0`→`0.7.1` precedent (`handbook-maturity`, docs-only). No tag created — none before merge in `pr` mode; the real tag happens post-merge, outside this role's control. |
| PR / merge | **Executed — PR #43 open.** `https://github.com/a-lottes/aSPARK/pull/43`, `main` ← `feat/situational-lenses`, state `OPEN`, `mergeable: MERGEABLE`. Approver = self-review-via-PR (`a-lottes`), per constitution §7 — established by a read-only `gh pr view` check, since I opened the PR myself (the access this role's Hard Rules grant). Not merged; merge/tag remain the approver's own call, outside this ceremony. |
| Deploy | N/A — no deploy surface; the plugin is installed by consumers via `/plugin install`, never deployed by this repo (constitution §2). |
| Post-release smoke check | N/A — `pr` mode, nothing deployed (named, not dropped). Ran anyway on the open PR's branch as a pre-merge sanity check: `claude plugin validate .` — **passed**, same pre-existing unrelated `autoUpdate` warning as every prior run. Proposed again post-merge, on `main`, per the command ledger below. |

**Command ledger (this pass):**

1. ✅ Bumped `.claude-plugin/plugin.json` `"version": "0.8.0"` → `"0.8.1"`
2. ✅ Release commit `d05fe22` — version bump, `qa.md`, `release.md` (prepare pass)
3. ✅ `git push -u origin feat/situational-lenses` — pushed, tracking set
4. ✅ `gh pr create …` into `main` — PR #43 opened: `https://github.com/a-lottes/aSPARK/pull/43`
5. ✅ This update — `.spark/situational-lenses/release.md` §3/Status, committed and pushed to the same branch
6. ☐ Post-merge (maintainer, outside this role): `git fetch origin && git tag -a v0.8.1 origin/main -m "aSPARK Core v0.8.1 — situational-lenses verify-only sweep" && git push origin v0.8.1`

## 4. Learnings (Keep!)

- **What went well:** five rounds of adversarial `/peer-review` caught a Blocker-class privacy leak on its third attempted fix (F1 → F12 → truly closed at r5) by re-deriving from primary sources every round rather than trusting the ledger's own word — exactly the discipline `CLAUDE.md`'s refuted-with-finding convention exists to protect.
- **What we'd do differently:** the QA deliverable (`qa.md`) reached `/go-live` uncommitted — a gap between ceremony completion and artifact commit that this pass had to close itself; catching it at `/demo-day`'s own close-out would avoid a pre-flight surprise next time.
- **Patterns worth reusing:** "refuted-with-finding is a valid ceremony outcome" (already in this repo's `CLAUDE.md`) held up under five rounds of the hardest adversarial pressure this project has seen — worth keeping verbatim. The branch-staleness check this project's `CLAUDE.md` already names paid off twice here: confirmed not-stale at prepare time and again fresh before publish, no surprise at either gate.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. Checked only where genuinely true today.*

- [x] All pre-flight checks passed at release time — §1, all fresh (re-verified this turn: staleness and test-suite bar both re-run); the one finding (uncommitted `qa.md`) was resolved within the prepare pass, not deferred
- [x] Changelog written in user-facing language — §2, the verify-only shape and its routed findings stated plainly, no verdict oversold
- [x] Release actions executed and verified — §3: push done, PR #43 open and confirmed (`OPEN`, `MERGEABLE`) via `gh pr view`; rollback path written below
- [x] Learnings recorded — §4
- [x] Line budget respected: Ist 86 / Soll ~100 (excluding HTML comments)
- [x] Status set to `released`/`handed-off` — set to `handed-off`: PR open, CI N/A (no workflows in this repo), declared approver (`a-lottes`) is the PR's own opener and owns the merge/tag decision next, per constitution §7

---

## Rollback path

- **Anchor:** `origin/main` is still at `a6a086c`, unchanged throughout this pass — confirmed via `gh pr view 43` (`baseRefName: main`, PR not merged) and by never running any merge command here. `main` remains exactly as it was before this release started; nothing merges automatically.
- **Before merge (now):** `git push origin --delete feat/situational-lenses` removes the remote branch and the PR closes itself with nothing merged into `main`. Locally, `git reset --soft HEAD~1` (or `~2` to also undo this report's own update commit) unwinds the release commit(s) while keeping the working tree.
- **After merge (future, outside this role's control):** `git revert -m 1 <merge-commit>` on `main` restores `plugin.json` to `0.8.0` and reverts the four touched files; then `git push origin :refs/tags/v0.8.1 && git tag -d v0.8.1` removes the tag before any re-tag.

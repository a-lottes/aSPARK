# Release: situational-lenses

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 5), `qa.md` (`passed`, round 1) |
| **Status** | `preparing` |
| **Version** | v0.8.1 (**proposed only** — `pr` mode; patch bump; not tagged, not pushed) |
| **Date** | 2026-09-12 |

**Handoff**
- **Status:** `preparing` — prepared, **awaiting the user's go** to publish. Nothing outward-facing has happened: no push, no PR, no tag.
- **Summary:** A verify-only evidence sweep of the `lenses/` mechanism — real refutations found and routed, two privacy leaks found and fixed (one required a history squash), and a documentation restatement. No new capability ships; `lenses/`, `agents/`, `skills/`, `templates/` are untouched.
- **Open:** `2 outstanding` before publish — the user's go to push/open the PR, and an optional local `git gc` (review F24, Nit, not gating) the user may run or skip. Not blocking this prepare pass.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch at the next `/go-live`.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — read fresh: Handoff + REVIEW GATE, round 5. 0 open Blocker (F12 `fixed r5`, re-derived independently), 0 open Major (F20 `fixed r5`); 1 open Nit (F24, optional `git gc`), none waived because none needed waiving.
- [x] `qa.md` status is `passed` — read fresh: Handoff + QA GATE, round 1. 0 open Blocker/Major; 5 `fail` rows mirror the ledger's own routed `refuted-with-finding` verdicts exactly, 1 open Minor (B1, exploratory, non-blocking). **QA-method row:** constitution §8 carries a complete declaration (surface `no`, substitute method named) — QA ran by that declared method, against the installed plugin, as this project's standing fact (§8, added 2026-08-29), not a per-feature override or a waiver for this release; `qa.md` records every `AC-`/`NFR-` ID QA owns, same as always.
- [x] Full test suite green on the release commit — none exists, none possible for prompt material (constitution §4). Bar: `claude plugin validate .`, re-run fresh — **passed**, one pre-existing `autoUpdate` warning unrelated to this diff, present on every prior release.
- [x] Build succeeds from a clean checkout — N/A: Markdown + JSON only, no build step (constitution §3).
- [x] No uncommitted changes in the working tree — **not clean at pre-flight**: `.spark/situational-lenses/qa.md` (this feature's own QA deliverable) was untracked, never committed by `/demo-day`. Included in this pass's release commit below — completing the gate's own artifact, not a code fix.
- [x] Branch staleness (project `CLAUDE.md` caution) — `git merge-base HEAD origin/main` equals `origin/main`'s own tip (`a6a086c`) after a fresh `git fetch`; no commit has landed on `main` since this branch diverged. Not stale; release-mode calculus (§7 `pr`) unchanged.
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
| PR / merge | **Prepared, not opened — awaiting the user's go.** Pending commands: `git push -u origin feat/situational-lenses`, then `gh pr create --base main --head feat/situational-lenses --title "docs: situational-lenses verify-only evidence sweep (v0.8.1, proposed)" --body <drafted from §2, plus review/QA gate summary>`. Approver = self-review-via-PR (`a-lottes`), per constitution §7. |
| Deploy | N/A — no deploy surface; the plugin is installed by consumers via `/plugin install`, never deployed by this repo (constitution §2). |
| Post-release smoke check | N/A — `pr` mode, nothing deployed (named, not dropped). Proposed for after merge: `claude plugin validate .` on `main`; re-confirm the protected-surface diff stays empty. |

**Command ledger (this pass):**

1. ✅ Bumped `.claude-plugin/plugin.json` `"version": "0.8.0"` → `"0.8.1"`
2. ☐ `git add .claude-plugin/plugin.json .spark/situational-lenses/qa.md .spark/situational-lenses/release.md; git commit` — release commit, **not yet executed**, pending this report's review
3. ☐ `git push -u origin feat/situational-lenses` — **pending user go**
4. ☐ `gh pr create …` into `main` — **pending user go**
5. ☐ Post-merge (maintainer): `git fetch origin && git tag -a v0.8.1 origin/main -m "aSPARK Core v0.8.1 — situational-lenses verify-only sweep" && git push origin v0.8.1`

## 4. Learnings (Keep!)

- **What went well:** five rounds of adversarial `/peer-review` caught a Blocker-class privacy leak on its third attempted fix (F1 → F12 → truly closed at r5) by re-deriving from primary sources every round rather than trusting the ledger's own word — exactly the discipline `CLAUDE.md`'s refuted-with-finding convention exists to protect.
- **What we'd do differently:** the QA deliverable (`qa.md`) reached `/go-live` uncommitted — a gap between ceremony completion and artifact commit that this pass had to close itself; catching it at `/demo-day`'s own close-out would avoid a pre-flight surprise next time.
- **Patterns worth reusing:** "refuted-with-finding is a valid ceremony outcome" (already in this repo's `CLAUDE.md`) held up under five rounds of the hardest adversarial pressure this project has seen — worth keeping verbatim. The branch-staleness check this project's `CLAUDE.md` already names paid off here: confirmed not-stale in one command, no surprise at this gate.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. Checked only where genuinely true today.*

- [x] All pre-flight checks passed at release time — §1, all fresh; the one finding (uncommitted `qa.md`) is resolved within this same pass, not deferred
- [x] Changelog written in user-facing language — §2, the verify-only shape and its routed findings stated plainly, no verdict oversold
- [ ] Release actions executed and verified — **not yet**: version bump done locally; release commit, push, and PR are prepared but not executed, pending the user's explicit go (listed in §3's command ledger); rollback path written below
- [x] Learnings recorded — §4
- [x] Line budget respected: Ist 86 / Soll ~100 (excluding HTML comments)
- [ ] Status set to `released`/`handed-off` — **not yet**: stays `preparing` until the user authorizes the push and PR; `handed-off` is the earliest this can move to, once PR is open, CI (absent, reads N/A by this repo's own lack of `.github/` workflows) and the declared approver are confirmed per constitution §7

---

## Rollback path

- **Anchor:** `origin/main` is at `a6a086c`, confirmed current (no new merges since this branch diverged). Nothing has been pushed; the entire branch, including this pass's release commit, is local-only.
- **If this prepare pass needs undoing before push:** `git reset --soft HEAD~1` drops the release commit (version bump, `qa.md`, `release.md`) while keeping the working tree; `git checkout -- .claude-plugin/plugin.json` alone reverts just the version bump if the commit is kept.
- **After the user's go (push + PR opened, before merge):** `git push origin --delete feat/situational-lenses` removes the remote branch; the PR closes itself with nothing merged into `main` — `main` is untouched throughout `pr` mode until the declared approver merges it.
- **After merge (future, outside this role's control):** `git revert -m 1 <merge-commit>` on `main` restores `plugin.json` to `0.8.0` and reverts the four touched files; then `git push origin :refs/tags/v0.8.1 && git tag -d v0.8.1` removes the tag before any re-tag.

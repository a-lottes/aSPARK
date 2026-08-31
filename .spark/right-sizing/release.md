# Release: right-sizing

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`, round 5), `qa.md` (`passed`, round 8) |
| **Status** | `handed-off` |
| **Version** | v0.8.0 (**proposed** — `pr` mode; minor bump; committed `c9dce8f` on `feat/right-sizing`; tag happens post-merge, outside this role's control) |
| **Date** | 2026-08-31 |

**Handoff**
- **Status:** mirrors the header table above. PR #31 opened into `main`, awaiting merge by the declared approver (`a-lottes`, self-review-via-PR). Nothing else remains in this session's control.
- **Summary:** A project with no browser-observable surface can now declare its QA method once in the constitution instead of renegotiating the same override every feature; a later phase can cite a predecessor's already-established fact instead of re-deriving it. Proposed **v0.8.0** (minor, additive, no breaking change).
- **Open:** `3 outstanding`, none blocking handoff: (1) the declared approver (`a-lottes`) still needs to merge PR #31 — real tag/merge happen then, outside this session; (2) `handbook-maturity/release.md` still self-reports `preparing` though its PR #27 is visibly merged into `origin/main` — a stale artifact belonging to a different feature, flagged for the caller, not fixed here; (3) `README.md`'s QA-method-declaration status row currently reads "first exercised by this feature's own `/demo-day` and `/go-live`" — true as of this report closing that citation (§1 below); no edit needed, not stale.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch at the next `/go-live`.

## 1. Pre-Flight Checks

- [x] `review.md` status is `passed` — read fresh: Handoff + REVIEW GATE complete, round 5. 0 open Blocker, 0 open Major (`F17` `fixed r5`); 5 open Minor/Nit (`F10`, `F20`–`F22` carried, `F23` new), none gate-blocking, none waived because none needed waiving.
- [x] `qa.md` status is `passed` — read fresh: Handoff + QA GATE complete, round 8. 0 open Blocker/Major; `F23` closed this round; one Minor accepted (verbatim field-quoting, capped by `AC-2.4`/`C19`). **QA-method row (`AC-1.4`):** constitution §8 carries a complete declaration (surface `no`, substitute method named) — QA ran by that declared method, against the installed plugin, as this project's standing fact (§8, added 2026-08-29 by this feature's own `/charter`), not as a per-feature override or a waiver for this release; `qa.md` records every `AC-`/`NFR-` ID QA owns, same as always.
- [x] Full test suite green on the release commit — none exists, none possible for prompt material (constitution §4). Bar: `claude plugin validate`, re-run fresh at `f4e3d11` — **passed**, one pre-existing `autoUpdate` warning, unrelated to this diff, present on every prior release.
- [x] Build succeeds from a clean checkout — N/A: Markdown + JSON only, no build step (constitution §3).
- [x] No uncommitted changes in the working tree — verified fresh: `git status --porcelain` empty on `feat/right-sizing` after the push; the only change since `f4e3d11` is this release's own commits (`c9dce8f`, `f152976`).
- [x] Added-surface check (`NFR-2`, enumerated here per its own text): one optional constitution field (§8, QA method only) plus conditional reading/writing rules in six ceremony locations — `/demo-day`, `/go-live`, `/charter`, `qa-tester.md`, `reviewer.md`, `/spark` (agent-file mirrors: `agents/facilitator.md`, `agents/release-manager.md`). Zero new slash commands, agents, lenses or template files; diff read fresh (`085db99..HEAD`) confirms every removed line is a wording tweak, never a removed protected structure (constitution §3).

## 2. Changelog

### Added
- A project with no browser-observable surface can declare its QA method once, so the QA step proceeds by that method automatically instead of asking the same override question on every feature.
- A release for such a project now describes QA as having run by that declared method — a settled project fact — rather than reporting a one-off exception granted for that release.

### Changed
- A later review or QA pass can now cite a fact an earlier pass in the same feature already established, instead of re-deriving it from scratch — except when verifying a fix to that exact fact, verifying a required acceptance criterion, when the earlier pass flagged the fact as unverified, or when there's a concrete reason to doubt it; those cases still get a fresh check.
- On a project with no such declaration (every project's default today, unchanged), or where the declaration is missing a piece or names a method the session genuinely can't perform, the QA step behaves exactly as before — same question, nothing silently skipped.

### Fixed
- The QA-method override that had to be renegotiated by hand on four consecutive features no longer needs repeating once declared.

**Stated plainly, not hidden:** four of the files carrying this release's QA-declaration wording — `skills/demo-day/SKILL.md`, `skills/spark/SKILL.md`, `skills/go-live/SKILL.md`, `agents/release-manager.md` (this file) — remain `not-verified-live` in this loop's own testing; the nested session needed to exercise them could not authenticate in this environment, reproduced in all 8 QA rounds. Recorded as an accepted, environment-caused gap (`evidence.md` §15.3, `review.md` r5), not a defect, and still true as of this release. This change makes no claim about line, token or cost savings, and no claim that the result generalizes beyond this project (`NFR-5`).

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | **Executed (local only, proposed).** `.claude-plugin/plugin.json` `0.7.1` → `0.8.0` — confirmed minor: additive only, no protected structure (constitution §3) renamed or removed, confirmed `0.7.1` already spent (handbook-maturity's release, unbumped by graph-gates-verification per its own spec NFR-2) and `0.8.0` unclaimed by any local/remote branch or tag. No tag created — none before merge in `pr` mode; the real tag happens post-merge, outside this role's control. |
| PR / merge | **Opened, with the user's explicit go.** PR #31 (https://github.com/a-lottes/aSPARK/pull/31), `feat/right-sizing` → `main`. The expected `README.md` conflict against PR #29's edit (both touch the Project-Status table) did **not** materialize — `gh pr view 31` (read-only, self-opened) reports `mergeable: MERGEABLE`, `mergeStateStatus: CLEAN`; the two edits landed on non-overlapping lines within the same table, so GitHub's 3-way merge resolved it cleanly. Reported plainly, not treated as a failure — nothing needed resolving at PR-open, contrary to the expectation logged in the prior pass. No CI exists (`.github/` holds templates only) — CI green reads N/A by absence, confirmed via the same read-only `gh pr view`. Approver = self-review-via-PR (`a-lottes`), same identity as the PR author — "requested" is satisfied by the PR's existence, no separate step required. Merge and tag remain outside this session's authorization. |
| Deploy | N/A — no deploy surface; the plugin is installed by consumers via `/plugin install`, never deployed by this repo (constitution §2). |
| Post-release smoke check | N/A until merge (`pr` mode; named as such, not silently dropped). Proposed for after merge: `claude plugin validate` on `main`, plus a `/charter` or `/go-live` dry run on a repo without the declaration, confirming the negative case (`AC-1.3`/`NFR-4`) still holds unchanged. |

**Command ledger:**

1. ✅ Bumped `.claude-plugin/plugin.json` `"version": "0.7.1"` → `"0.8.0"`
2. ✅ `git add .claude-plugin/plugin.json .spark/right-sizing/release.md`; committed as `c9dce8fb3192300931c946783fc5ea89731b93f3` on `feat/right-sizing`
3. ✅ `git push -u origin feat/right-sizing` — new branch pushed, tracking set
4. ✅ `gh pr create` into `main` — PR #31 opened, title/body drafted from §2
5. ✅ Checked at PR-open: no conflict materialized (`mergeStateStatus: CLEAN`) — nothing to resolve, contrary to the prior pass's expectation (same shape as PR #22 was expected to need, this one didn't)
6. ☐ Post-merge (maintainer): `git fetch origin && git tag -a v0.8.0 origin/main -m "aSPARK Core v0.8.0 — QA-method declaration + predecessor-citation rule" && git push origin v0.8.0`

## 4. Learnings (Keep!)

- **What went well:** `AC-1.4`'s citation rule got its first real use in this very report (§1's QA row cites constitution §8 as a standing fact, not a per-feature ask) — the loop closing on itself, not just designing for it. Artifact chain stayed intact through 5 review rounds, 8 QA rounds, and four spec amendments without any ID being renumbered or reused.
- **What we'd do differently:** four straight `/increment` fix attempts (`C15`–`C18`) chased narrower wordings of the same "never mention the declaration" clause against a live contradicting instruction — the real problem was the requirement, not the wording: it conflicted structurally with `qa-tester.md`'s pervasive exhaustive-disclosure mandate, so no wording could win. What broke the loop: re-reading US-1's own "so that" clause (`spec.md:112-114`, "so that I stop **re-negotiating** the same override") showed the actual need was avoiding a live ask, not lifelong silence — `C19` re-scoped to that achievable, action-based guarantee and passed on its first try. Next time: after two failed fix attempts on the same AC, stop revising wording and re-read the story's "so that" before drafting a third.
- **Patterns worth reusing:** citing a standing constitution fact instead of re-litigating it per release (this feature's own `US-2`, now dogfooded by this report); the environment-caused `not-verified-live` gap (nested `claude -p` auth) has now recurred across features — a CLAUDE.md or project-memory note would stop it being rediscovered fresh each time.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. Checked only where genuinely true today.*

- [x] All pre-flight checks passed at release time — §1, all fresh
- [x] Changelog written in user-facing language — §2, limitation and honesty constraint stated plainly
- [x] Release actions executed and verified — push + PR done (§3); PR-open, CI-green (N/A by absence), and approver-requested all established by a read-only `gh pr view` on a PR this session opened itself; rollback path written below
- [x] Learnings recorded — §4
- [x] Line budget respected: Ist 88 / Soll ~100 (excluding HTML comments — none in this file)
- [x] Status set to `handed-off` (declared `pr` mode) — outstanding: PR #31's merge and the v0.8.0 tag, owned by the declared approver (`a-lottes`, self-review-via-PR), happening post-merge outside this session's control

---

## Rollback path

- **Anchor:** `origin/main` was at `1671f2b` before this push; that commit is untouched. The release commits (`c9dce8f`, `f152976`) live on the pushed branch `feat/right-sizing` and in open PR #31, nothing merged into `main` yet.
- **Abandon now (current state):** `gh pr close 31 && git push origin --delete feat/right-sizing` — closes the PR and removes the pushed branch; `main` is never touched.
- **Pushed / PR open, pre-merge:** same as above — this is the state as of this report.
- **After merge:** one `git revert -m 1 <merge-sha>` on `main` restores `plugin.json` to `0.7.1` and reverts the eight touched files' declaration-reading clauses. Only if tag `v0.8.0` was already pushed: `git push origin :refs/tags/v0.8.0 && git tag -d v0.8.0`, re-tagging only after the revert lands.
</content>

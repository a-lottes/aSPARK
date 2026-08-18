# Release: lean-artifacts

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`, with recorded user waiver on AC-1.7/AC-1.8) |
| **Status** | `preparing` |
| **Version** | v0.6.0 (**proposed only** — `pr` mode, no tag before merge) |
| **Date** | 2026-08-17 |

<!-- Handoff: read this block first, the numbered sections below by exception. Whoever
     writes to this report updates it in the same edit that changes status or actions:
     overwrite in place, never append. The block holds one current state, never a
     per-round log; a stale block is a defect, not a cosmetic issue. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status` and `Version`).
- **Summary:** Both gates green (review `passed`, QA `passed` with a recorded, user-accepted waiver on AC-1.7/AC-1.8). Branch pushed and confirmed live; PR [#22](https://github.com/a-lottes/aSPARK/pull/22) opened directly from the main conversation after the release-manager subagent's `gh pr create` was denied by that context's own permission classifier. **`main` has diverged since the branch was cut** — `gh pr view` reports `mergeable: CONFLICTING`. Two files conflict: `README.md` (this branch's §Project Status bullet vs. `main`'s PR #21 moving status content to `docs/status.md`) and `.spark/constitution.md` (this branch's `acfa3ac` amendment vs. `main`'s `20e99bf` replacing the internal backlog with a public roadmap). Neither conflict has been resolved — this role has not attempted to, since resolving requires a content judgment call belonging to the user. v0.6.0 remains proposed only — no tag.
- **Open:** `2 outstanding` — (1) resolve the merge conflicts in `README.md` and `.spark/constitution.md` (rebase or merge `main` into this branch, then re-push) before this PR can actually merge; (2) after that, self-review-approve and merge, and after merge, the real tag — outside this role's control either way. Owner: the user (`a-lottes`). See §3/§4.
- **Binding ruling:** §3 Release Actions and the KEEP GATE below carry the final ruling.
- **On conflict:** the numbered body below wins for everything except `Status`/`Version`; log the mismatch as a finding at the next `/go-live` and proceed — don't stop on it.

## 1. Pre-Flight Checks

<!-- Verified immediately before releasing — not copied from earlier reports. -->

- [x] `review.md` status is `passed` — confirmed by reading `.spark/lean-artifacts/review.md` header + Handoff block just now: `passed`, 0 Blockers/Majors, 2 open Nits (F1, F2), REVIEW GATE fully checked.
- [x] `qa.md` status is `passed` — confirmed by reading `.spark/lean-artifacts/qa.md` header + Handoff block just now: `passed`, 0 Blockers/Majors, 3 open Minors (QA-F1/F2/F3). **Not a rubber stamp:** 2 of 12 Must ACs (AC-1.7, AC-1.8) are recorded `partial`, not `pass` — the QA Tester declined to self-mark them passing (no agent passes its own gate, constitution §6) because neither has a naturally-occurring specimen in this repo yet (no real report here has ever closed to zero open items, and no real block/body value-contradiction exists to test against). The user reviewed both gaps and **explicitly accepted the risk on 2026-08-17**, setting `qa.md` to `passed` themself rather than sending the feature back to `/increment`. This is a real, recorded waiver, not a silent pass — I am relying on it, not re-litigating it, and am not overriding anything myself.
- [x] Full test suite green on the release commit — **N/A as "full test suite," substituted per constitution §4** (no automated suite is possible for prompt-only material). Ran the actual bar fresh, right now, on the exact release commit `3d2939d`: `claude plugin validate .claude-plugin/plugin.json` → **Validation passed**; `claude plugin validate .` (resolves to the marketplace manifest) → **Validation passed with 1 warning** (`autoUpdate` unknown field — pre-existing since commit `789e33f`, `chore/opus-models-autoupdate-gitignore`, unrelated to this feature, not introduced by `3d2939d`). Confirmed `.claude-plugin/marketplace.json` carries no second `version` field (single-version rule, NFR-1 assumption, holds).
- [x] Build succeeds from a clean checkout — **stated explicitly rather than silently skipped: there is no build step.** Constitution §3: "Markdown + JSON only. No build step, no runtime, no dependencies." Nothing to run; nothing failed.
- [x] No uncommitted changes in the working tree — verified fresh with `git status` on the release commit. Two categories present, handled differently:
  - **Two pre-existing, unrelated untracked files** — `docs/aSPARK_Enterprise_Architecture_Handbook.docx.bak`, `docs/aSPARK_Enterprise_Architecture_Handbook_v1.0.docx`. Predate this feature, not touched by any commit on this branch, consciously **excluded** from this release — seen, not missed.
  - **Two feature-related untracked files found at pre-flight time** — `.spark/lean-artifacts/review.md` and `.spark/lean-artifacts/qa.md` (the reviewer's and QA tester's actual gate reports) had never been committed; commit `3d2939d` only carries `plan.md`/`evidence.md` because it landed before those reports existed. Since `.spark/` is tracked and public in this repo (constitution §5), and these two files are the evidentiary basis for this very release, I committed them **unmodified, as written by their authors** — together with this report — as the local release-prep commit (§3). This is release-commit housekeeping, not a fix to the increment: no content in either file was altered. After that commit, `git status` is clean for every tracked path this feature touches; only the two unrelated docx files remain untracked.

## 2. Changelog

<!-- User-facing language. What can they do now that they couldn't before? -->

### Added
- Every review, QA, spec, plan and release report now opens with a short **Handoff** block right at the top — status, a one-line verdict, what (if anything) is still open, which section has the final ruling, and what wins if the block and the rest of the report ever disagree. You can tell whether a report is done and what's left without reading the whole thing.

### Changed
- The team members and ceremonies that act on a previous report — the Reviewer doing a re-review, `/increment` closing out findings, `/go-live` checking its two release gates, `/next-steps` scanning for open items across features — now read that new block first, and only read further when they specifically need to (for example, verifying a fix was actually made, or working out a genuine disagreement between the block and the report). Reports written before this change keep working exactly as they did before; nothing about reading them changes.

### Fixed
- Nothing — this release adds a new capability rather than fixing a defect. (No token or byte saving is claimed anywhere in this release: the new block adds lines, it does not shrink anything.)

## 3. Release Actions

<!-- What was actually executed, with results. -->

<!-- Direct mode: fill all four. Declared `pr` mode (handed-off): Version bump is
     *proposed only*, no tag before merge; Deploy and Post-release smoke check
     are N/A — write "N/A — handed-off, no deploy" rather than leaving them blank. -->

| Action | Result |
|---|---|
| Version bump & tag | **Proposed only, no tag.** `.claude-plugin/plugin.json` already reads `0.6.0` (was `0.5.0`), bumped as part of task T10 and committed in `3d2939d`. Bump level: **minor** — purely additive (new Handoff block + reading/writing rules across 5 templates and 5 consumers), no protected heading/column/ID pattern in constitution §3 renamed, removed or reordered, confirmed independently by both the reviewer (AC-1.4, NFR-1) and QA (§2 NFR-1) against the actual `aspark-graph` parser source. Per constitution §7 (`pr` mode): **no tag is created before merge** — the real tag happens at/after merge, outside this role's control. No local tag was created — correct in this mode regardless of PR state. |
| PR / merge | **Push done, PR open, not yet mergeable.** `git push -u origin feat/lean-artifacts` confirmed live. `gh pr create` was denied by the release-manager subagent's own permission classifier; the caller ran it directly in the main conversation instead, using the drafted title/body below — **[PR #22](https://github.com/a-lottes/aSPARK/pull/22), state `OPEN`**, confirmed via `gh pr view 22 --json state,mergeable`. That same check reports **`mergeable: CONFLICTING`** — `main` gained 8 commits (`d97e57d`..`a7165b8`, three merged PRs: #17, #20, #21) since this branch was cut, two of which touch files this branch also touches: `README.md` (PR #21, `docs/readme-status`, moved §Project Status content to `docs/status.md`) and `.spark/constitution.md` (`20e99bf`, replaced the internal backlog with a public roadmap). Confirmed via `git merge-tree` — exactly those two files, no others, are "changed in both." **Not resolved this pass** — conflict resolution is a content decision (which change wins in each overlapping hunk) that belongs to the user, not something this role should silently pick a side on. |
| Deploy | N/A — no deploy surface exists for this project (Markdown/JSON Claude Code plugin, no runtime, no server). "Deploy" in this repo means the PR merging to `main` and installers subsequently picking up `0.6.0` from the marketplace listing — that only happens after merge. |
| Post-release smoke check | **N/A — nothing to smoke yet, correctly.** No deploy has happened (no merge, no new install) — a real smoke check only exists after merge, outside this role's control, exactly as flagged in the previous pass. What *is* checkable right now, and was checked: the branch is genuinely pushed (`git log`/`git status` against `origin/feat/lean-artifacts`, both confirmed live above) and there is no CI configured in this repo (`.github/workflows/` does not exist) — so "CI green" is **N/A by absence**, not an unchecked box. PR-open and approver-requested are **not yet true** (PR isn't open), so those are left honestly unconfirmed below rather than asserted. |

**Local commits this pass (all now pushed):** `31d1add`, `0ee24cd`, `eb33b96` on `feat/lean-artifacts` — adding `.spark/lean-artifacts/review.md`, `.spark/lean-artifacts/qa.md` (both previously untracked, unmodified), and this report with two small self-referential corrections. `git push -u origin feat/lean-artifacts` — **executed**, confirmed live.

**User's explicit go, as relayed by the caller, 2026-08-17 (this conversation):** authorized exactly steps 1 (`git push`) and 2 (`gh pr create`) below; explicitly excluded tag and merge as outside this role's remit. Recorded here per constitution §6 ("every override is recorded in the artifact with its reason") even though this is an authorization, not a gate override.

**Commands — status after this pass:**
1. `git push -u origin feat/lean-artifacts` — **done**, confirmed live.
2. `gh pr create --base main --head feat/lean-artifacts --title "..." --body "..."` — **attempted, denied by the local permission classifier** (not a `gh`/GitHub-side error — the tool call itself was refused before reaching GitHub). Needs either a `gh`/`Bash` permission grant from the user for this role to retry, or the user runs it manually. Draft below.
3. After merge: the real tag/release — still outside this role's direct control per `pr` mode, unchanged from the previous pass.

**Drafted PR — title and body, ready to submit:**

> **Title:** `feat: add Handoff blocks to spec/plan/review/qa/release templates (v0.6.0, proposed)`
>
> **Body:**
>
> ## Summary
>
> - **Added:** every review, QA, spec, plan and release report now opens with a short **Handoff** block right at the top — status, a one-line verdict, what (if anything) is still open, which section has the final ruling, and what wins if the block and the rest of the report ever disagree. You can tell whether a report is done and what's left without reading the whole thing.
> - **Changed:** the team members and ceremonies that act on a previous report — the Reviewer doing a re-review, `/increment` closing out findings, `/go-live` checking its two release gates, `/next-steps` scanning for open items across features — now read that new block first, and only read further when they specifically need to (for example, verifying a fix was actually made, or working out a genuine disagreement between the block and the report). Reports written before this change keep working exactly as they did before; nothing about reading them changes.
> - **Fixed:** nothing — this adds a new capability rather than fixing a defect. No token or byte saving is claimed anywhere: the new block adds lines, it does not shrink anything.
>
> Three commits ride together on this branch:
> - `2f48497` — the feature's spec (`.spark/lean-artifacts/spec.md`)
> - `acfa3ac` — a constitution amendment recording `review-report.md`'s parser-required findings-table columns (`severity`/`location`/`status`), surfaced during this feature's own spec pass
> - `3d2939d` — the increment itself: the Handoff block added to all five templates plus the reading/writing rules in every consumer, and the proposed minor version bump (`0.5.0` → `0.6.0`)
>
> Full gate trail, evidence and this release's own report: `.spark/lean-artifacts/{spec,plan,review,qa,release}.md`.
>
> ## Gates
>
> - Review: `passed` (`.spark/lean-artifacts/review.md`) — 0 Blockers/Majors, 2 open Nits.
> - QA: `passed` (`.spark/lean-artifacts/qa.md`) — 0 Blockers/Majors, 3 open Minors; 2 of 12 Must ACs (AC-1.7, AC-1.8) recorded `partial` with a **user-accepted waiver** (no naturally-occurring specimen in this repo yet to verify the exact rendering/contradiction branch against — mechanism itself exercised live and held).
> - Version: `0.6.0` is **proposed only** in this PR — per this repo's declared `pr` release mode (constitution §7), no tag is created before merge; the real tag happens at/after merge.
>
> ## Approval
>
> This repo is solo-maintained (constitution §7): **self-review-via-PR** is the declared approver mode — the same maintainer (`a-lottes`) opens, reviews and merges this PR rather than pushing straight to `main`. There is no GitHub branch protection on `main` (process commitment, not enforced infrastructure, per the same section) and no CI configured for this Markdown/JSON-only plugin.
>
> ## Test plan
>
> - [x] `claude plugin validate .claude-plugin/plugin.json` — passed
> - [x] `claude plugin validate .` (marketplace manifest) — passed, 1 pre-existing unrelated warning
> - [x] Dogfood evidence, negative-case-first, in `.spark/lean-artifacts/evidence.md` (constitution §4 — no automated test suite is possible for prompt material)
> - [ ] Merge and confirm the plugin still updates/validates cleanly post-merge (post-release smoke check, outside this PR's control)

**`gh pr create` retried once more, isolated, after the push succeeded — denied again by the same classifier, consistently, not a one-off.** Confirmed across two separate attempts with different invocation shapes (`--body` inline, then `--body-file`) that this is a firm tool-permission wall in this environment, not a transient fluke or a formatting issue on this role's side. Not retried a third time, per the standing instruction not to keep pushing on a denial — this is now handed back to the user.

## 4. Learnings (Keep!)

<!-- The K in SPARK: what does the team keep from this cycle? -->

- **What went well:**
  - The walking-skeleton checkpoint (plan tasks T2–T4) gated the feature's real design risk — parser safety for a change touching a cross-repo, unversioned contract — on a single template pair (`review-report.md` + `reviewer.md`) *before* rolling the same shape out to four more templates and four more consumers. The evidence record shows an explicit go/no-go gate at T4 ("if the design fails here, fix T2 before rollout"), not a rollout that just happened to work.
  - Both the reviewer and the QA tester independently re-read the actual `aspark_graph/artifacts.py` parser source themselves — not each other's citations of it, not the evidence file's summary — before signing off on the load-bearing safety claim (no `##` heading, no pipe `Status`/`Version` row inside the block). Neither found a discrepancy, but the practice caught real, if minor, imprecision elsewhere (review finding F1: evidence's own line-cites ran a few lines short of the parser's actual function boundaries).
  - Negative-case-first was actually exercised, not just claimed: both the review and QA runs checked real, untouched old-shape artifacts (`.spark/graph-gates/review.md`, `.spark/tracker-handoff/*`) before checking the new-shape positive case, at every checkpoint that touched compatibility (AC-1.5, AC-2.4).

- **What we'd do differently:**
  - The QA tester's own delegation instructions pointed it at the *installed plugin cache* (`~/.claude/plugins/cache/aspark/aspark/0.5.0/templates/qa-report.md`) as "the" report template — which is genuinely stale (no Handoff block at all) for any feature that edits `templates/` directly in the working tree. The tester caught this itself (QA-F3) and used the working-tree copy instead, but a future QA run that doesn't notice would silently grade the feature against the wrong artifact and could produce a false negative. Worth fixing the delegation boilerplate so template-touching features point QA at the working tree by default, not a cached install.
  - Two Nits (review F1, F2) and three Minors (QA-F1, F2, F3) were all left `open` rather than fixed inline, by design — both agents judged that editing already-approved `.spark/` prose without the author's intent was the wrong move mid-gate. That's a defensible call, but it means five small, cheap items are now this feature's own housekeeping debt; worth closing them in the same pass that eventually produces this repo's first zero-open-items review/QA round (which would also naturally satisfy AC-1.7's untested zero-open branch, see below).
  - I found the same shape of gap myself at pre-flight: two real feature artifacts (`review.md`, `qa.md`) sat untracked in the working tree despite `.spark/` being tracked and public in this repo. Not a defect in the increment — `3d2939d` simply landed before those reports existed — but a reminder that "prepare the release commit" should explicitly include a fresh `git status` sweep for *this feature's own* untracked `.spark/` artifacts, not just the code diff, at every future `/go-live`.

- **Patterns worth reusing** (candidates for `.spark/constitution.md` or project memory):
  - **Walking-skeleton-then-rollout** for any change touching a protected, cross-repo, unversioned contract (constitution §3's template contract): verify the riskiest slice first, record an explicit go/no-go gate, then generalise. This feature is now a second precedent alongside whatever motivated the pattern originally.
  - **Independent re-verification of load-bearing external source**, not citation-trusting, as a standing expectation for reviewer + QA whenever a claim depends on a sibling repo's actual code (here, `aspark-graph/artifacts.py`) rather than its docs or another agent's summary.
  - **"Untestable-by-nature, not by neglect" as a named, distinct waiver category.** AC-1.7 (zero-open rendering) and AC-1.8 (a real block/body value-contradiction) are Must ACs with no naturally-occurring specimen anywhere in this repo yet — the mechanism was exercised live via adjacent/constructed cases, and the user accepted the specific, narrow gap rather than manufacturing an artificial specimen just to check a box. That's a cleaner shape of accepted risk than a generic "we're out of time" waiver, and worth naming explicitly as an option in future QA rounds facing the same shape of gap.

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time — see §1; two substitutions (test suite → `claude plugin validate`, build → explicitly N/A) both stated, not silently skipped, per constitution §4.
- [x] Changelog written in user-facing language — see §2; no commit hashes, ticket IDs or internal jargon; no token/byte-saving claim (NFR-4).
- [ ] Release actions executed and verified — **partially, and accurately reflected as such.** Push: done, confirmed live (§3). PR: **open** ([#22](https://github.com/a-lottes/aSPARK/pull/22)), but **not mergeable** — `main` diverged while this branch was in flight, producing real conflicts in `README.md` and `.spark/constitution.md` (§3). CI: N/A by absence (no `.github/workflows/`). No deploy, no tag — correct in this mode/state regardless. This box stays unchecked: a PR that cannot currently merge is not a completed release action, even though it is genuinely open.
- [x] Learnings recorded — see §4, pulled from this cycle's actual review/QA trail, not boilerplate.
- [ ] Status set to `released`, or `handed-off` in declared `pr` mode — **left `preparing`.** The PR is now open and CI is N/A-by-absence, two of constitution §7's three `handed-off` conditions. The third — a mergeable PR the declared approver can actually act on — isn't true yet: `README.md` and `.spark/constitution.md` conflict against `main`'s current tip (§3). Calling this `handed-off` while the PR can't be merged would overstate readiness; the outstanding owner (`a-lottes`, also the approver) needs to resolve the conflict (rebase or merge `main` in, re-push) before this is a genuine handoff.

---

## Rollback path

- **What would need undoing, and how.** The only functional change in this release is commit `3d2939d` (`feat: add handoff blocks to spec/plan/review/qa/release templates`) — 12 modified files (5 templates, 5 consumer agents/skills, `README.md`, `.claude-plugin/plugin.json`) plus 2 new project-local files (`evidence.md`, `plan.md`, non-shipped). A single `git revert 3d2939d` on whatever branch carries it (this branch now, or `main` after merge) restores every protected template structure and every consumer's reading rules to their pre-feature state in one operation, and reverts `plugin.json` back to `0.5.0` in the same commit — **no separate version-rollback step is needed**, since reverting the commit that bumped it un-bumps it.
- **No tag to roll back.** Per constitution §7 (`pr` mode), no tag exists yet — the version bump is proposed only. If this PR is never opened or never merged, the only outward-facing fact so far is the **push** (`origin/feat/lean-artifacts` now exists on GitHub, publicly visible on this public repo) — reverting that requires nothing beyond not opening/merging a PR against it, or deleting the remote branch (`git push origin --delete feat/lean-artifacts`) if even the branch's existence should be undone. No tag, no merge, no marketplace listing change has happened; there is nothing published to consumers to roll back.
- **This pass's own local commit** (`31d1add`, review.md/qa.md/release.md housekeeping) is additive-only (new `.spark/` files, no shipped-surface change) and can be reverted independently with `git revert 31d1add`, or simply left as an accurate historical record even if `3d2939d` itself is later reverted — the gate reports remain true statements about what was reviewed and tested, regardless of whether the feature ships.
- **Prior commits on this branch not in scope for rollback:** `2f48497` (spec) and `acfa3ac` (constitution amendment) are separately accepted ceremonies, already public, and do not touch the shipped/consumed contract — reverting the feature commit does not require touching either.

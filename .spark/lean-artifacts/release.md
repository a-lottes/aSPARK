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
- **Summary:** Both gates green (review `passed`, QA `passed` with a recorded, user-accepted waiver on AC-1.7/AC-1.8); pre-flight re-run clean on commit `3d2939d`; a local prep commit now also carries `review.md`/`qa.md`/this report; v0.6.0 is proposed only — no tag, no push, no PR yet. Awaiting the user's explicit go for the outward-facing steps.
- **Open:** `1 outstanding` — opening the PR into `main`, requesting the declared self-review approver, and (after merge, outside this role's control) the real tag. Owner: the user (`a-lottes`), on explicit go. See §3/§4.
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
| Version bump & tag | **Proposed only, no tag.** `.claude-plugin/plugin.json` already reads `0.6.0` (was `0.5.0`), bumped as part of task T10 and committed in `3d2939d` before this release pass began. Bump level: **minor** — purely additive (new Handoff block + reading/writing rules across 5 templates and 5 consumers), no protected heading/column/ID pattern in constitution §3 renamed, removed or reordered, confirmed independently by both the reviewer (AC-1.4, NFR-1) and QA (§2 NFR-1) against the actual `aspark-graph` parser source. Per constitution §7 (`pr` mode): **no tag is created before merge** — the real tag happens at/after merge, outside this role's control. This pass created **no** local tag. |
| PR / merge | **Not opened.** Prepared-but-not-published, per this pass's explicit constraint (prepare only). Local release-prep commit created (below) so the branch is ready to push and open as a PR the moment the user gives the go. |
| Deploy | N/A — no deploy surface exists for this project (Markdown/JSON Claude Code plugin, no runtime, no server). "Deploy" in this repo means the PR merging to `main` and installers subsequently picking up `0.6.0` from the marketplace listing — that only happens after merge, outside this pass. |
| Post-release smoke check | N/A this pass — nothing was deployed yet (no PR opened, no merge). Named explicitly rather than dropped: once the PR is opened and merged (second pass, after the user's go), the smoke check for this feature is a real, cheap one — reinstall/update the plugin from the marketplace and confirm `claude plugin validate` still passes and one instantiated template (e.g. `templates/review-report.md`) renders its Handoff block correctly in a fresh `.spark/<feature>/review.md`. |

**Local release-prep commit created this pass** (not pushed): commit `31d1add` on `feat/lean-artifacts`, adding `.spark/lean-artifacts/review.md`, `.spark/lean-artifacts/qa.md` (both previously untracked, unmodified) and this file, `.spark/lean-artifacts/release.md`. Message: `docs: prepare lean-artifacts release (v0.6.0, proposed)`. This is local, reversible, and not outward-facing — no `git push`, no PR, no publish of any kind was performed. Branch is now `feat/lean-artifacts`, several commits ahead of `origin/main` @ `cc89c30` (the feature commit `3d2939d` plus this pass's `.spark/`-only prep commits); exact count will shift again once the PR is opened and squashed/merged, so it isn't pinned here.

**Commands pending explicit go — none run this pass:**
1. `git push -u origin feat/lean-artifacts`
2. `gh pr create --base main --head feat/lean-artifacts --title "..." --body "..."` (self-review-via-PR per constitution §7 — the same maintainer opens, reviews and merges)
3. After merge: the real tag/release, outside this role's direct control per `pr` mode.

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
- [ ] Release actions executed and verified — **not yet, by design this pass.** Local release-prep commit made (reversible); PR not opened, not pushed, no deploy, no tag. Awaiting the user's explicit go, listed in §3, before any outward-facing action runs. Rollback path: see below.
- [x] Learnings recorded — see §4, pulled from this cycle's actual review/QA trail, not boilerplate.
- [ ] Status set to `released`, or `handed-off` in declared `pr` mode — **left `preparing`.** This is the first (prepare) pass; the terminal `handed-off` status (constitution §7 — this repo does not merge to `main` directly) is set on the second pass, after the user's explicit go and the outward-facing steps in §3 actually run. Outstanding owner: the user (`a-lottes`), who is also the declared self-review approver.

---

## Rollback path (required before any outward-facing action)

- **What would need undoing, and how.** The only functional change in this release is commit `3d2939d` (`feat: add handoff blocks to spec/plan/review/qa/release templates`) — 12 modified files (5 templates, 5 consumer agents/skills, `README.md`, `.claude-plugin/plugin.json`) plus 2 new project-local files (`evidence.md`, `plan.md`, non-shipped). A single `git revert 3d2939d` on whatever branch carries it (this branch now, or `main` after merge) restores every protected template structure and every consumer's reading rules to their pre-feature state in one operation, and reverts `plugin.json` back to `0.5.0` in the same commit — **no separate version-rollback step is needed**, since reverting the commit that bumped it un-bumps it.
- **No tag to roll back.** Per constitution §7 (`pr` mode), no tag exists yet — the version bump is proposed only. If this PR is never merged, nothing outward-facing ever happened and there is nothing to revert; simply not merging (or closing the PR) is the entire rollback.
- **This pass's own local commit** (`31d1add`, review.md/qa.md/release.md housekeeping) is additive-only (new `.spark/` files, no shipped-surface change) and can be reverted independently with `git revert 31d1add`, or simply left as an accurate historical record even if `3d2939d` itself is later reverted — the gate reports remain true statements about what was reviewed and tested, regardless of whether the feature ships.
- **Prior commits on this branch not in scope for rollback:** `2f48497` (spec) and `acfa3ac` (constitution amendment) are separately accepted ceremonies, already public, and do not touch the shipped/consumed contract — reverting the feature commit does not require touching either.

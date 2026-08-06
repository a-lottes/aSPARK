# Release: tracker-handoff

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `handed-off` |
| **Version** | v0.5.0 (**still proposed** — merged to `main`, but no git tag exists yet; the real, non-proposed tag happens at/after merge, outside this pass's control, C9/A9) |
| **Date** | 2026-08-06 |

> **Pass 1** of this feature's own Keep phase was prepare-only, per
> `skills/go-live/SKILL.md` step 2 — no push, no `gh pr create`, no tag.
>
> **Pass 2 (this revision), same date.** The caller relayed the user's
> explicit authorization for the three outward-facing steps pass 1 listed as
> pending. Between the two passes, the user also asked for
> `.spark/constitution.md`'s §7 amendment to be committed on this same
> branch (`cc58fec`, "docs: declare PR-first delivery in the constitution")
> — closing the one real gap pass 1 flagged: without that commit, the PR
> would not have carried the declaration its own `handed-off` mechanism
> depends on. All three authorized steps ran and are recorded below with
> real, freshly-established facts — nothing here is copied from pass 1 or
> asserted without a live check performed in this pass.
>
> **This release is, itself, the deferred positive-case evidence named in
> `.spark/tracker-handoff/evidence.md` Entry 2 (R8/C8/NFR-6).** Entry 2 is
> now **discharged** (dated note appended to `evidence.md` this pass) — the
> Q1/C10 fact-establishing mechanism has fired for real, R9 is no longer
> open, and AC-2.2/AC-2.3/AC-2.4 are verified live rather than only read.

## 1. Pre-Flight Checks

<!-- Verified immediately before releasing — not copied from earlier reports. -->

- [x] `review.md` status is `passed` — unchanged since pass 1; no open
      Blocker or Major; two Minors (F1/F2) discharged per `qa.md`.
- [x] `qa.md` status is `passed` — unchanged since pass 1; QA GATE closed
      with a recorded user override on AC-3.4 (named follow-up B2) and
      NFR-6's positive case (this release) explicitly left open by design
      at QA time.
- [x] Full "test suite" green, this project's own bar (constitution §4: no
      automated suite exists or is possible for prompt material) —
      `claude plugin validate .` re-run fresh this pass, on the merged
      commit's line: **`✔ Validation passed with warnings`**, identical
      single pre-existing warning (`marketplace.json`'s `autoUpdate` field,
      unrelated to this feature). Third consecutive identical result across
      both passes.
- [x] Build succeeds from a clean state — N/A in the literal sense (no
      build step; constitution §0/§3, Markdown + JSON only), satisfied by
      the validate check above.
- [x] Working tree, `feat/tracker-handoff` branch itself, clean at the
      moment of push/PR/merge — `git status` immediately before `git push`
      showed the branch exactly 2 commits ahead of `origin` (`f7d13e6`,
      `cc58fec`), nothing uncommitted on the branch's own tracked history.
      (The *session's* working directory still carries the same unrelated
      items pass 1 flagged and correctly excluded — `.spark/BACKLOG.md`,
      the three untracked `.docx` files — plus this report and the
      `evidence.md` append being edited live as part of writing this
      report. None of these are part of any commit pushed or merged.)

## 2. Changelog

<!-- User-facing language. What can they do now that they couldn't before? -->

### Added
- If your team ships through a pull request rather than pushing straight to
  the main branch, you can now declare that once for the whole project —
  release mode, who approves, the target branch, your ticket-tracker format
  — and every release from then on ends honestly at "handed over, pending
  approval" instead of either falsely claiming "released" or sitting stuck
  with no way to close.
- A feature's spec can now record a ticket reference (a Jira key, a GitHub
  issue, or an explicit "none") in exactly one place, so your organization's
  reference for the work no longer has to live only in a branch name, a
  commit message, or someone's memory.

### Changed
- When delivering by pull request, the release report now marks the version
  number "proposed" rather than final, and no version tag is created until
  after the pull request actually merges — the exact commit under review can
  still change during review, so tagging it early would be premature.
- The tools that tell you what to work on next and that resume an
  in-progress feature both now recognize "handed over, pending approval" as
  a closed state for your team — they stop treating it as unfinished work
  still to pick up.

### Fixed
- Teams whose merge approval belongs to someone outside the team no longer
  have to choose between falsely claiming a release happened or leaving the
  release process open forever with no way to close it — there is now a
  truthful way to say "our part is done, the rest is out of our hands."

**Unchanged, by design:** projects that declare no delivery mode see zero
difference — same steps, same report sections, same gate boxes, terminal
status still `released` or `aborted`, and the word "handed-off" never
appears anywhere in their output (verified live, `qa.md` AC-1.1/AC-1.2/AC-2.6,
Venues A; re-confirmed structurally by `evidence.md` Entry 1, unaffected by
this pass).

## 3. Release Actions

<!-- What was actually executed, with results. -->

| Action | Result |
|---|---|
| Version bump & tag | `.claude-plugin/plugin.json` bumped `0.4.0` → **`0.5.0`**, committed in `f7d13e6`, now on `main` via the merge. **Minor** bump: an additive optional capability (declared PR-mode delivery + `handed-off` terminal status), no protected `templates/` structure renamed or removed (constitution §5, NFR-1). **Still marked proposed in this table** — no git tag created (`git tag -l` unchanged, still ends at `v0.4.0`, checked fresh this pass). Per C9/A9, the real tag is created at/after merge, outside this pass's control — that is a correct, expected gap for `handed-off`, not a defect. |
| PR / merge | **Done.** Pushed `feat/tracker-handoff` (`f7d13e6`, `cc58fec`) to `origin`. Opened https://github.com/a-lottes/aSPARK/pull/3 ("feat: give the Keep phase an honest end for PR-mode delivery"), body per the draft below (updated to mention the constitution commit). Self-review attempted via `gh pr review --approve`: GitHub rejected it (`GraphQL: Review Can not approve your own pull request`) — a real, structural limit, recorded honestly rather than worked around. `main` carries no branch protection (`gh api repos/a-lottes/aSPARK/branches/main/protection` → 404, re-checked this pass), so no GitHub-native approval was required to merge; "self-review-via-PR" (constitution §7) is exercised here as reading the full diff and merging as the declared approver, not as a literal GitHub approval — that distinction is now established fact, not assumption. Merged via `gh pr merge 3 --merge` (merge commit, no squash/rebase — history of both commits preserved intact). Resulting merge commit: `0eae0f4bf4351d916c2707ca3883e355bd01a7be` on `main`. `gh pr view 3` confirms `state: MERGED`, `mergedBy: a-lottes`. |
| Deploy | N/A — handed-off, no deploy. |
| Post-release smoke check | N/A — handed-off, no deploy. |

### AC-2.2's gate facts, honestly as of this pass (Q1/C10 mechanism)

| Fact | Status | How established |
|---|---|---|
| PR open on `main` | **True, then merged** | `gh pr create` returned https://github.com/a-lottes/aSPARK/pull/3; `gh pr view 3 --json state,mergeable` read `OPEN`/`MERGEABLE` before merge, then `MERGED` after — a real read-only check each time, not self-attestation. |
| CI green | **N/A — no CI configured** | Re-confirmed this pass: `gh pr checks 3` → `no checks reported on the 'feat/tracker-handoff' branch` (exit 1, meaning nothing to check, not a failure); `find .github -type f` still finds no such directory. Same N/A fact as pass 1, now cross-checked against the live PR itself, not just the filesystem. |
| Declared approver requested | **True, self-review-via-PR exercised** | The declared approver (`a-lottes`, constitution §7) is the PR's sole author and the account that merged it (`mergedBy: a-lottes`, `gh pr view 3`). A literal self-*approve* review is structurally impossible on GitHub (confirmed by the rejected attempt above) and no branch protection required one (404, confirmed above) — so "requested" here means the merge itself, performed deliberately by the declared approver after reading the diff, which is what this repo's solo-maintainer §7 declaration means in practice. |
| Ticket linked where declared | **N/A — `none` declared** | Unchanged from pass 1: constitution §7 ticket-reference format is `none`; `spec.md`'s `Ticket` row reads `none` (NFR-10). |
| Rollback path written | **Done** | §5 below, revised this pass to reflect the real merge commit. |

### PR description, as opened (revised from pass 1's draft to note the constitution commit)

> **Title:** feat: give the Keep phase an honest end for PR-mode delivery
>
> **Summary**
> - Adds a standing `Delivery & Handoff` declaration to the constitution
>   (direct vs. PR, approver, target branch, ticket format, terminal
>   status) — declared once, read by every release, never guessed.
> - Adds `handed-off` as a second, honest terminal release status for
>   projects delivering via PR: the loop ends there once a PR is open, CI
>   is green (or N/A, as here) and the declared approver is requested —
>   never on a deploy that didn't happen.
> - Teaches `/spark` and `/next-steps` to treat `handed-off` as
>   closed-for-this-team, distinct from `released`.
> - Adds a `Ticket` row to `spec.md` so a project's ticket reference has
>   exactly one home.
> - Also includes the constitution's own §7 "Delivery & Handoff" amendment
>   as a committed change on this branch — it is what makes this PR's own
>   `handed-off` mechanism reachable in the first place, so it travels with
>   this PR rather than as a separate concern.
> - Purely additive: no protected template row/heading/column renamed or
>   removed (constitution §3); zero difference for any project that
>   declares nothing (verified live, `qa.md`).
>
> **This PR is its own dogfood.** It is opened, self-reviewed and
> self-merged under the very `pr`-mode declaration it introduces
> (constitution §7, confirmed by the user 2026-08-06) — this repo's first
> real exercise of `handed-off`.
>
> **Test plan:** `.spark/tracker-handoff/{spec,plan,review,qa,evidence}.md`
> — review `passed`, QA `passed` (one user-recorded override on AC-3.4,
> named follow-up B2), `claude plugin validate .` green before and after.
>
> Ticket: none (this repo declares no tracker, constitution §7).

## 4. Learnings (Keep!)

<!-- The K in SPARK: what does the team keep from this cycle? -->

- **What went well:** The spec's own sequencing bet (C8/R8 — defer this
  feature's positive-case evidence to its own release, after a separate
  `/charter` amendment lands) paid off across both passes: pass 1 read the
  constitution honestly without inventing content, flagged the one real gap
  precisely (the amendment existing in the working tree but not committed),
  and pass 2 closed exactly that gap before publishing — no fact in this
  report was asserted without a live `gh`/`git` check performed in this
  pass. The Q1/C10 mechanism, designed on paper in `plan.md`, worked exactly
  as specified the first time it touched a real PR.
- **What we'd do differently:** GitHub's structural rejection of
  self-approval (`Can not approve your own pull request`) was not
  anticipated anywhere in `spec.md`, `plan.md` or `review.md` — the
  constitution's "self-review-via-PR" language was written assuming an
  approval action would be literal. It isn't, for a solo maintainer without
  branch protection. The distinction ("self-review-via-PR" = read-and-merge,
  not a GitHub-native approve) had to be discovered and named live in this
  pass rather than being written down in advance — worth adding a line to
  `agents/release-manager.md` or the constitution's §7 template guidance so
  the next solo-maintainer project doesn't rediscover it.
- **Patterns worth reusing:** (1) The three-column "in commit? / why?"
  breakdown of a dirty working tree (pass 1, §1) remains a reusable shape
  for release passes with in-flight unrelated edits — still a candidate for
  `templates/release-notes.md`. (2) Establishing a gate fact as **N/A by a
  read-only check performed now** vs. **"not yet true" pending an action**
  vs. **"true, now cross-checked against the live artifact"** are three
  distinct, nameable states this feature's own release exercised in
  sequence (pass 1 → pass 2) — worth writing explicitly into
  `agents/release-manager.md`'s Q1/C10 guidance as a three-state vocabulary,
  not just two.

---

## 5. Rollback Path

**Current state: merged to `main`, no tag yet.**

1. `git revert 0eae0f4` on `main` (never `reset --hard` — this repo is
   public on the plugin marketplace and other clones may already have
   fetched `main` at `0eae0f4`), then push the revert. This cleanly reverts
   both the feature commit (`f7d13e6`) and the constitution amendment
   (`cc58fec`) together, since they merged as one merge commit.
2. If a real (non-proposed) tag `v0.5.0` is created at/after this point
   (C9/A9, outside this pass's control) before a revert is needed, delete it
   both remotely (`git push origin :refs/tags/v0.5.0`) and locally
   (`git tag -d v0.5.0`); re-tag the prior commit (`e89e0af`, effectively
   `v0.4.0`'s state) if a marker is needed for consumers pinned to a tag.
3. **Consumer-visible effect:** low. The change is purely additive and
   degrades to silence when undeclared (constitution §6) — a consumer
   project with no `Delivery & Handoff` declaration sees zero behavioral
   difference whether this release is reverted or not. The only visible
   effect of a revert is the loss of the `handed-off` status, the `Ticket`
   row, and the constitution's §7 declaration itself for consumers who *had*
   started declaring PR mode in the meantime.
4. **Who may perform this:** the sole maintainer/approver, `a-lottes` — the
   same person who opened, self-reviewed and merged the PR (constitution
   §7).

---

## ✅ KEEP GATE

*All boxes checked → the loop is closed. The feature is done-done.*

- [x] All pre-flight checks passed at release time — 5/5 this pass; the
      branch's own committed history was clean at push time, and every
      unrelated dirty item in the session's working directory remains
      correctly excluded and accounted for (§1).
- [x] Changelog written in user-facing language — §2, sourced from US-1..4,
      zero commit hashes/ticket IDs/jargon.
- [x] Release actions executed and verified — §3: version bump on `main`
      (still correctly proposed, no tag), PR opened and merged
      (https://github.com/a-lottes/aSPARK/pull/3, merge commit `0eae0f4`),
      deploy/smoke correctly N/A. Every fact in the Q1/C10 table above was
      established by a live, read-only check performed in this pass.
- [x] Learnings recorded — §4, extended this pass with the self-approval
      discovery.
- [x] Status set to `released`, or `handed-off` in declared `pr` mode —
      **set to `handed-off`.** PR is open-then-merged, CI is correctly N/A,
      the declared approver (`a-lottes`) both requested and performed the
      merge under constitution §7's self-review-via-PR mechanism. **Not**
      claimed as `released`: no deploy exists for this project, and the
      real (non-proposed) version tag has not been created — by design,
      C9/A9, outside this pass's authority to create.

**What remains genuinely open, honestly, even at `handed-off`:**

1. The real, non-proposed `v0.5.0` git tag does not exist yet
   (`git tag -l` still ends at `v0.4.0`) — this is correct and expected for
   `handed-off`, not a defect (C9/A9: tag creation happens at/after merge,
   outside the Release Manager's control, presumably a separate
   maintainer action or automation this project has not yet built).
2. `evidence.md` Entry 2 is discharged (dated note appended this pass) but
   the broader "no polling, ever" guarantee (AC-2.5) is only as strong as
   this being the last ceremony to touch `release.md` for this feature —
   no future ceremony should re-open or re-check this report looking for
   the tag; that would violate the constitution's no-polling principle
   named in `evidence.md` Entry 1.

# Plan: api-lens-public-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/api-lens-public-run/spec.md` (`approved`) |
| **Status** | `approved` |
| **Date** | 2026-10-26 |

**Handoff**
- **Status:** `approved` (dark mode, recommended gate).
- **Summary:** Review-only lens run on spring-petclinic-rest PR #329 (merge `7690a61`), reviewer agent run blind to the author's own pre-read; evidence compares the two.
- **Open:** `none`
- **Binding ruling:** §3 Task Breakdown.
- **On conflict:** body wins except `Status`.

## 1. Architecture Decision

- **Context:** The lens is Markdown; the only way to test it is to run `/peer-review`. No target `.spark/` trail exists and no JVM is available.
- **Decision:** Pick one bounded public PR with real API surface (new versioned list endpoints, tag renames, repository changes). Clone it into untracked scratch outside the repo. The reviewer agent receives the diff range, the `api` lens path and the review template, and is **not** told the author's pre-read findings. The author's independent read is recorded first (evidence §3) so right/wrong/missed can be judged without hindsight.
- **Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Run the full loop on the target (spec/plan/QA there) | Needs a trail in someone else's repo and a build; out of scope, and the lens fires at Specify/Review only. |
| Pick a tiny dependabot diff | The lens would be silent everywhere; shows nothing. |
| Build and run the target's tests | No JVM in this environment; stated as a limitation, not hidden. |

- **Consequences:** Spec-phase half of the lens (NFRs) is not exercised; one run, one observation.

## 2. Affected Components

Only `.spark/api-lens-public-run/*`, `README.md` (Project Status), `ROADMAP.md`. Target clone at `/tmp/target/spring-petclinic-rest` (scratch, untracked).

## 3. Task Breakdown

| # | Task | Story | Status | Definition of Done | Covers (AC / NFR) | Depends on |
|---|---|---|---|---|---|---|
| T1 | Pick and pin target diff; record author's independent pre-read | US-1 | done | Repo, base, merge commit, date, diff command in evidence.md; pre-read written before the review | AC-1.1, NFR-1 | none |
| T2 | Run `/peer-review` (reviewer agent, api lens) on the diff | US-2 | done | `review.md` written by the reviewer, with lens findings | AC-2.1 | T1 |
| T3 | Compile evidence: per-check fired/silent/not-verified-live, right/wrong/missed, firing count, refutations | US-2, US-3 | done | `evidence.md` complete, citations re-resolved at the pinned commit | AC-2.1, AC-2.2, AC-3.1, AC-3.2, NFR-2 | T2 |
| T4 | Update README Project Status and ROADMAP to the run's actual result | US-4 | done | Wording matches evidence; nothing moved to Shipped beyond what ran | AC-4.1, AC-4.2, NFR-3 | T3 |

## 4. Test Strategy

Verification is re-resolving every citation with `git show 7690a61:<path> | sed -n` and a clean `git status` outside the trail/docs.

## 5. Risks

- The reviewer may ignore the lens (a result, recorded as such).
- Anchoring: the pre-read is written first and the reviewer is blind to it.

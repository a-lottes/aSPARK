# Spec: api-lens-public-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |
| **Date** | 2026-10-26 |
| **Ticket** | #91 |

**Handoff**
- **Status:** `approved` (dark-mode factory line took the recommended gate; the issue's own AC-1…AC-6 are the approved scope).
- **Summary:** Run the `api` lens through `/peer-review` on a real public open-source API diff and commit the full trail, positive and negative results alike.
- **Open:** `none`
- **Binding ruling:** §4 User Stories.
- **On conflict:** the numbered body wins except `Status`.

## 1. Problem & Goal

- **Problem:** ROADMAP "The one gap that matters most": the lens layer's success definition includes a Review lens firing and being Review-verified on a real `api`; no public, checkable run exists. Most real use is closed source.
- **Goal:** One public, re-runnable `api`-lens Review on a named upstream diff, with every checklist item recorded fired / silent / not-verified-live.
- **Success signal:** A stranger can clone the target, check out the named commit, re-run `/peer-review` with `lenses/api.md` and compare against `evidence.md`.
- **Why now:** The gap is the roadmap's stated top item; the constitution says a loop change is validated by running the loop.

## 2. Target Users

Maintainers and prospective adopters deciding whether the `api` lens is worth trusting; the aSPARK author reading the roadmap.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The target repo has no `.spark/` trail; the run is a *Review-only* lens run, so the target's profile (`api` active) is declared in this evidence, not committed to the target. | Accepted; recorded in evidence.md. |
| A2 | No JVM is available in the run environment, so the target is not built or tested. Anything needing the build is `not-verified-live`. | Accepted; honest limitation. |
| A3 | Lens firing is instruction-driven; one run gives one observation, not a rate. | Accepted; AC-3 reports the observed count and what it does not show. |
| A4 | The scanner/greps used stay untracked scratch (constitution §3). | Accepted; AC-6. |

## 4. User Stories

### US-1 (Must): Name the target so it can be re-run

> As a stranger, I want the exact repo, commit and date, so that I can re-run the same diff.

**Acceptance criteria:**

- [ ] AC-1.1: Given the evidence file, when read, then it names target repo URL, merge commit, base commit, diff command and run date.

### US-2 (Must): Per-check lens record with citations

> As a maintainer, I want each api-lens check marked fired / silent / not-verified-live with `file:line` from the target, so that I can see what the lens did.

**Acceptance criteria:**

- [ ] AC-2.1: Given the 13 checklist items in `lenses/api.md`, when `evidence.md` is read, then each has one status and, where fired, a target `file:line` citation.
- [ ] AC-2.2: Given the reviewer's findings, when compared with an independent author check, then each finding is marked right / wrong / partly, and anything the lens missed is listed.

### US-3 (Must): Honest statement of what the run proves

> As a reader, I want the write-up to say firing is instruction-driven and give the observed rate, so that I do not read it as a guarantee.

**Acceptance criteria:**

- [ ] AC-3.1: Given evidence.md, then it states lens firing is instruction-driven, not test-enforced, and gives the observed count (n of 13), flagged as one run.
- [ ] AC-3.2: Given failures or misfires, then each is recorded as refuted-with-finding, not smoothed over.

### US-4 (Must): Docs claim only what was shown

> As a reader of README/ROADMAP, I want status wording that matches the run.

**Acceptance criteria:**

- [ ] AC-4.1: README Project Status and ROADMAP are updated only to what the run showed; "Shipped" only if exercised.
- [ ] AC-4.2: No executable code is committed; no lens text is changed; no `website` run.

## 5. Non-Functional Requirements

| # | Requirement |
|---|---|
| NFR-1 | Reproducibility: every cited line resolves at the named commit. |
| NFR-2 | Negative results are reported as plainly as positive ones. |
| NFR-3 | Scope fence: `.spark/api-lens-public-run/`, `README.md`, `ROADMAP.md` only. |

## 6. Out of Scope

The `website` / QA-verified UI run; any change to `lenses/api.md`.

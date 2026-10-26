# QA Report: api-lens-public-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | `.spark/api-lens-public-run/spec.md`, `plan.md`, `evidence.md`, `review.md` (`passed`) |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-10-26 |

**Handoff**
- **Status:** `passed`.
- **Verdict:** Yes, with the disclosed limits: it is one prompted, partial run (see evidence.md §2, §6 R1–R5). Nothing in the docs claims more.
- **Open:** `none`.
- **Binding ruling:** §5 Verdict and the gate checklist below.
- **On conflict:** the numbered body wins for everything except `Status`.

**QA method (constitution §8):** `Browser-observable surface: no`; the substitute is commands whose output was observed and files read with text quoted. Performed here by the orchestrator in the same session that built the trail (no separate QA agent was available in dark mode), so it is **not an independent tester**; every row below was re-run from primary source, not copied from `evidence.md`.

## 1. Test Environment

- **App URL:** N/A. **Browser:** N/A. **Data:** N/A.
- **Substitute method:** `git show 7690a61:<path> | sed -n '<n>p'`, `git grep`, `git ls-files`, `git diff --name-only`, in `/workspace/repo` and the scratch clone `/tmp/target/spring-petclinic-rest`.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Read evidence.md §1; `git rev-parse 7690a61^1 7690a61^2` | repo, merge, base, diff cmd, date named; base matches | base `03af87f…` matches; merge `7690a61fb2…`; date 2026-06-13/run 2026-10-26 | ✅ pass |
| AC-2.1 | Re-resolved 8 cited lines with `sed -n`: `openapi.yml:872,905`, `ExceptionControllerAdvice.java:80,117`, `PetRestControllerV2.java:32`, `OwnerRestControllerV1.java:124`, `JpaPetRepositoryImpl.java:81`, `pom.xml:374`; counted the 13 rows in evidence §4 | each line holds the quoted text; 13 rows, each one status | all 8 resolve to the described code; 13 rows | ✅ pass |
| AC-2.2 | Read evidence §5 | every finding F1–F9 marked right/wrong/partly; misses listed | F1–F9 each judged; M1–M3 listed; F5 partly, F2 not-lens | ✅ pass |
| AC-3.1 | Read evidence §2.2, §7 | states firing is instruction-driven, not test-enforced; gives count, flagged as one run | present, with the prompted-trace confounder named | ✅ pass |
| AC-3.2 | Read evidence §6 | failures recorded as refuted-with-finding | R1–R5 recorded, including against the author's own process (R2) | ✅ pass |
| AC-4.1 | `git diff README.md ROADMAP.md` | wording claims only what ran; no new Shipped row | README adds one paragraph, ROADMAP amends the gap paragraph with an "Update"; Shipped table untouched; both say partial | ✅ pass |
| AC-4.2 | `git ls-files '*.py' '*.sh' '*.js'`; `git diff --name-only`; `git status --short` | no executable file; `lenses/` untouched; changes only in fence | no executables; changed: `README.md`, `ROADMAP.md`, untracked `.spark/api-lens-public-run/` | ✅ pass |
| NFR-1 | as AC-2.1, plus one extra: re-ran F3's grep word-bounded | citations reproduce | reviewer's `grep -i etag` command was sloppy (false-positive substring hits); conclusion holds at `-iw` (0 hits); corrected in both docs | ✅ pass |
| NFR-2 | Read evidence §5–§7 | negatives as plain as positives | R1–R5, misses, scope misfire, "no control run" all stated | ✅ pass |
| NFR-3 | `git diff --name-only` | fence respected | yes | ✅ pass |

## 3. Exploratory Findings

| # | Severity | Finding |
|---|---|---|
| E1 | Minor | QA was run by the orchestrator, not an independent agent; stated in the method note. A human reading the PR should treat this QA as a consistency check, not a second opinion. |
| E2 | Nit | The scratch clone and `/tmp/preread.md` are not in the repo, so a stranger cannot check the "written before" ordering; disclosed as self-reported (evidence R2). |

## 4. Console & Network

N/A (no running app).

## 5. Verdict

Passed. No Blockers or Majors. The result the repo can honestly claim is narrow, and the README and ROADMAP say so.

---

## ✅ QA GATE

- [x] Every Must AC verified
- [x] No open Blocker or Major bugs
- [x] Exploratory findings triaged (E1, E2 accepted, disclosed)
- [x] Status set to `passed`

# Review Report: api-lens-public-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Target diff `git -C /tmp/target/spring-petclinic-rest diff -M 03af87f 7690a61` (spring-petclinic-rest PR #329), `.spark/api-lens-public-run/plan.md` |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-10-26 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** The `api` lens fired on 11 of 13 items (1 silent, 1 not-verified-live). Two target-side Majors: probable 500-instead-of-400 on bad paging params (not verified live), and no data-layer tests for the new paged pet query. Nothing was built or run.
- **Open:** `F1`–`F8` are target-side lens output (recorded, not fixable here); `F9` fixed. Blockers: none. Majors `F1`, `F2` waived for this evidence-only loop (see gate). Minors/Nits: see §3.
- **Binding ruling:** §6 Verdict and the gate checklist below. This is the only binding location; there is no other round to point to.
- **On conflict:** the numbered body below wins for everything except `Status`. Log the mismatch as a finding at the next `/peer-review` and proceed. Do not stop on it.

## 1. Scope

- **Reviewed:** all 27 files in `git diff -M 03af87f 7690a61` of `https://github.com/spring-petclinic/spring-petclinic-rest` (base `03af87f`, merge `7690a61`, PR #329 merged 2026-06-13). The diff covers `openapi.yml`, `pom.xml` (`useTags`), the new `v2/PetRestControllerV2` and `v2/OwnerRestControllerV2`, the renames of eight v1 controllers, the pet repository/service paging in all three profiles (jdbc, jpa, spring-data-jpa) and the tests. To judge it in context I also read `ExceptionControllerAdvice.java`, both security configs, `application.properties`, `PetRestControllerV1.java`, `AbstractClinicServiceTests.java` and the openapi-generator config in `pom.xml`. Every citation below is `path:line` at `7690a61`, resolved with `git show 7690a61:<path> | nl`. I did not modify the target checkout.
- **Not reviewed / not run:** no JVM is available, so nothing was compiled, generated or tested. The generated `*Api` interfaces (from openapi-generator 7.22.0, `pom.xml:35`) do not exist on disk, so I inferred their annotations rather than read them. Every claim that depends on them is marked not-verified-live. Profile: `api` only (caller's declaration). The target has no `.spark/` trail and no constitution.
- **Pre-existing issues outside the diff (no finding raised):** v1 `listPets` returns 404 for an empty list (`v1/PetRestControllerV1.java:66-68`). `/oops` is in the spec (`openapi.yml:33-37`) but no class implements it, at both base and merge.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ⚠️ | Marked `done`, and its DoD says the author's pre-read is in `evidence.md` *before* the review. No `evidence.md` exists in the trail at review time, so I cannot check that the pre-read came first (F9). |
| T2 | ✅ | This report. The reviewer ran without the author's pre-read and had only the diff range, the lens path and the template. |
| T3 | ⚠️ | Marked `done` before T2's output existed. Not reviewable yet (F9). |
| T4 | ⚠️ | Marked `done`. No README/ROADMAP change is visible in the working tree (`git status` shows only the trail as untracked). Not reviewable yet (F9). |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `rest/controller/v2/PetRestControllerV2.java:33-37`; `openapi.yml:887,897-898,913-918`; `rest/advice/ExceptionControllerAdvice.java:80-86,117-148` | **Not verified live.** The contract promises 400 + ProblemDetail for bad `page`/`size` (min 0, 1..100). The advice maps only `MethodArgumentNotValidException` to 400. A rejected `@Min`/`@Max` on a query parameter raises `ConstraintViolationException` or `HandlerMethodValidationException` instead (inferred from generator 7.22 + Boot 4.0.6, not read). Either one falls into the catch-all `Exception` handler, which returns 500 "unexpected error". If the generated constraints are absent, `PageRequest.of(-1, …)` throws `IllegalArgumentException`, which is also a 500, and `size=100000` would pass with no bound. Either way a client error is reported as a server fault (lens 1.2, 2.3). The same gap exists on `/v2/owners` (`v2/OwnerRestControllerV2.java:54-60`). **Fix:** add a 400 handler for both exception types that fills `schemaValidationErrors`, then test `size=0`, `size=101` and `page=-1`. | recorded (target-side) |
| F2 | Major | `src/test/.../V2RestControllersTests.java:119-134`; `repository/jdbc/JdbcPetRepositoryImpl.java:153-182`; `repository/jpa/JpaPetRepositoryImpl.java:78-87`; `repository/springdatajpa/SpringDataPetRepository.java:44-48` | Three new `findAll(Pageable)` implementations, including hand-written `LIMIT/OFFSET` SQL (`JdbcPetRepositoryImpl.java:159`), have no test. The only new test mocks `ClinicService` (`V2RestControllersTests.java:122`) and covers only the happy path: no empty page, no last page, no bounds, no auth. Owner paging set the precedent with service-level tests (`service/clinicService/AbstractClinicServiceTests.java:350,360`). Pet paging skipped it. **Fix:** add a `findPets` paging case to `AbstractClinicServiceTests`, which runs against every profile, and negative controller tests (F1). | recorded (target-side) |
| F3 | Minor | `openapi.yml:905-908`; `v2/PetRestControllerV2.java:38` | The spec declares an `ETag` response header, but the controller never sets one. `git grep -n -iw etag 7690a61 -- src/main/java` finds no filter or header code. The spec does not match the implementation (lens 2.3). This copies a spec-wide pre-existing pattern. **Fix:** drop the header from `/v2/pets` or register `ShallowEtagHeaderFilter`. | recorded (target-side) |
| F4 | Minor | `openapi.yml:11-30,365,414,476,531`; `openapi.yml:8`; `pom.xml:372` | Every tag was renamed (`pet`→`pets`, `owner`→`owners`, `failing`→`oops`, …). Owner-nested pet/visit operations moved to the `owners` tag. No wire path changed, but anyone who generates SDKs or Swagger UI groups from the published spec by tag gets renamed classes and groups. `info.version` stays `'1.0'` and nothing records the change (lens 3.2). The new `owner-v2`/`pet-v2` tags are also singular while the v1 tags are plural. **Fix:** bump `info.version` or add a changelog note. | recorded (target-side) |
| F5 | Minor | `repository/jdbc/JdbcPetRepositoryImpl.java:167-170` | In the jdbc profile, every page request loads the whole `owners` table to attach owners to at most `size` pets. The "paginated" read is therefore unbounded (lens 1.3). The pattern is copied from the unpaged `findAll` (`:140-143`). **Fix:** use a JOIN, or `WHERE id IN (:ownerIds)` over the page's owner ids. | recorded (target-side) |
| F6 | Minor | `openapi.yml:901-924`; `v2/PetRestControllerV2.java:32`; `V2RestControllersTests.java:64,97,118` | In code the auth requirement holds: `@PreAuthorize OWNER_ADMIN`, the same as v1 `listPets` (`v1/PetRestControllerV1.java:62`). The contract says nothing about auth: no `securitySchemes` and no 401/403 responses. The tests use `standaloneSetup` without the security filter chain, so `@WithMockUser` exercises no authorization at all. Security is off by default (`application.properties:49`), but that is the project's choice and pre-existing (lens 4.1). **Fix:** declare a basic-auth scheme plus 401/403, and add one secured MockMvc test. | recorded (target-side) |
| F7 | Minor | `v2/PetRestControllerV2.java:31-39`; `security/BasicAuthenticationConfig.java:34-43` | There is no rate limit and no recorded N/A. The `size ≤ 100` cap is the only bound, and it may not be enforced (F1) (lens 4.3). Pre-existing, project-wide. **Fix:** record a conscious N/A for this sample app, or add a limit. | recorded (target-side) |
| F8 | Nit | `repository/jpa/JpaPetRepositoryImpl.java:80`; `repository/jdbc/JdbcPetRepositoryImpl.java:159` | The jpa and jdbc implementations hard-code `ORDER BY id` and ignore `pageable.getSort()`. Spring Data applies the sort (`SpringDataPetRepository.java:45-48`). The profiles diverge as soon as a caller passes a different sort. **Fix:** honour the sort, or assert it is `id`. | recorded (target-side) |
| F9 | Minor | `.spark/api-lens-public-run/plan.md` §3 (T1, T3, T4) | Artifact bookkeeping (aSPARK side). T1–T4 are marked `done`, but `evidence.md` does not exist yet. T1's "pre-read before the review" is therefore unverifiable from the trail. **Fix:** set T3/T4 to their real state, and commit the pre-read with a timestamp or commit that predates this review. | fixed |

## 4. Requirements Traceability

These are the aSPARK-side ACs. Target findings are lens output, not ACs of this feature.

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | §1 of this report names the repo, base, merge, diff command and date. `evidence.md` is absent. | ⚠️ partial (T1/T3 pending) |
| AC-2.1 | §7 below: 13 items, each with one status and a target `file:line` | ✅ met for the review side; `evidence.md` copy pending |
| AC-2.2 | Out of the reviewer's remit: comparing against the author's pre-read is T3's job | ❌ not yet (pending T3) |
| AC-3.1 / AC-3.2 | Pending `evidence.md` (T3). The input it needs is in §7: 11 fired, 1 silent, 1 not-verified-live, one run | ⚠️ pending |
| AC-4.1 / AC-4.2 | No README/ROADMAP diff yet. I committed no code and changed no lens text | ⚠️ pending T4 |
| NFR-1 | Every citation was resolved with `git show 7690a61:<path> \| nl` | ✅ |
| NFR-2 | Clean items are recorded as clean in §7, and negatives as findings | ✅ |
| NFR-3 | This pass wrote only `review.md` | ✅ |

## 5. What Was Checked

- [x] Correctness: paging maths (`PetMapper.java:43-51`), offset/limit in all three profiles, count queries, v1 paths unchanged, every tag maps to an implemented interface (`git grep 'implements .*Api'`)
- [x] Non-functional: the `api` lens, all 13 items (§7)
- [x] Error handling: bad-input path goes through the advice catch-all (F1)
- [x] Security: authz annotations, default security posture, no SQL built from input (named parameters, `JdbcPetRepositoryImpl.java:155-161`)
- [ ] Tests: read and judged (F2). **Not run, no JVM.**
- [x] Readability: renames are mechanical, and the v2 controllers mirror each other

## 6. Verdict

As a lens run, the review did its job. The `api` lens fired on 11 of 13 items, with a finding or a cited clean observation for each. It stayed silent on idempotency, which this diff never touches. Input validation (4.2) could only be marked not-verified-live, because it depends on generated code that needs a build. As a review of PR #329 itself, the change is a reasonably clean, additive, path-versioned endpoint. It breaks nothing on the wire, uses the same envelope and naming as `/v2/owners`, and uses the same authz as v1. Two things would block a merge if I were gating the target. First, bad paging input very likely returns 500 instead of the contracted 400 (F1). That is inferred from the advice and generator config, not observed, because nothing could be built here. Second, three new data-access implementations ship with no test (F2). The Minors are honest contract drift: an ETag that is never sent, unversioned tag renames that break codegen, auth missing from the spec, and an unbounded owners load in jdbc. Several of them are pre-existing patterns that the diff copies. None of these findings can be fixed inside this feature's fence (the target is read-only). They are the run's evidence, not work for `/increment`. F9 is the only aSPARK-side item, and T3/T4 must close it.

## 7. API lens checklist trace

FIRED = finding or verified-clean observation · SILENT = not applicable to this diff · NOT-VERIFIED-LIVE = needs a build.

| Item | Check | Status | Evidence at `7690a61` |
|---|---|---|---|
| 1.1 | Nouns/verbs, no RPC | FIRED (clean) | `GET /v2/pets`, `openapi.yml:872-876`: a plural noun read with GET |
| 1.2 | Honest status codes | FIRED + NOT-VERIFIED-LIVE | F1. The happy path returns 200 with a possibly empty page (`v2/PetRestControllerV2.java:38`), which is better than v1's 404 on empty |
| 1.3 | Consistent pagination, no unbounded list | FIRED | Same params and envelope as `/v2/owners` (`openapi.yml:880-900` vs `:146-174`; `PetPage` `:2109-2153` vs `OwnerPage` `:2064-2108`). The DB read is still unbounded in jdbc (F5). v1 `/pets` stays unpaged (`:838-871`), pre-existing |
| 1.4 | Idempotent retries for mutations | SILENT | The diff adds no mutating endpoint. Renamed v1 mutators are unchanged apart from class and package names |
| 2.1 | One error envelope | FIRED (clean) | 400/500 → `ProblemDetail` (`openapi.yml:913-924`), produced by `ExceptionControllerAdvice.java:63-71`. Field details are missing on the F1 path |
| 2.2 | Naming/casing/format consistency | FIRED | camelCase `totalElements`/`totalPages`, int64/int32 types identical to `OwnerPage` (`openapi.yml:2109-2153`). Singular v2 tags vs plural v1 tags (F4) |
| 2.3 | OpenAPI matches implementation | FIRED + NOT-VERIFIED-LIVE | ETag declared but never sent (F3). Declared 400 probably delivered as 500 (F1) |
| 3.1 | API is versioned | FIRED (clean) | Path version `/v2/pets` (`openapi.yml:872`), controllers split into `v1/`/`v2/` packages. v1 itself has no version in its path (`/pets`) |
| 3.2 | No silent breaking change | FIRED | No path, field or status changed. `/v2/owners` moved class but kept its contract (`v2/OwnerRestControllerV2.java:52-61`). Tag renames break codegen silently (F4) |
| 3.3 | New fields additive/optional | FIRED (clean) | New `page`/`size` are `required: false` with defaults (`openapi.yml:883,893`). `PetPage` is a new response-only schema (`:2109`) |
| 4.1 | Auth stated on every endpoint, authz at data | FIRED | Code: `@PreAuthorize` at `v2/PetRestControllerV2.java:32`. The contract does not state it and the tests do not exercise it (F6) |
| 4.2 | Server-side input validation | NOT-VERIFIED-LIVE | Constraints are declared (`openapi.yml:887,897-898`) and `performBeanValidation` is on (`pom.xml:374`). Whether the generated interface enforces them, and with which status, needs a build (F1) |
| 4.3 | Rate/payload limits or recorded N/A | FIRED | None present and none recorded (F7) |

Totals: **11 FIRED** (1.2 and 2.3 also carry a NOT-VERIFIED-LIVE part), **1 SILENT** (1.4), **1 NOT-VERIFIED-LIVE** (4.2), out of 13. This is a single run, so it shows that the lens fired once here, not a rate.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place. Never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived). F1 and F2 are Majors against the read-only public target; they are the run's lens output, not defects of this feature. **Waiver taken by the factory's dark-mode default (no human was available): a human should confirm it when reading the PR.** Reason: the feature's fence forbids touching the target, and its purpose is to record them.
- [x] Every Must AC traces to its artifact; no constitution non-negotiable violated. Re-checked after round 1: `evidence.md` (AC-1.1, 2.1, 2.2, 3.1, 3.2), README/ROADMAP edits (AC-4.1), no code and no lens change (AC-4.2).
- [x] All plan deviations documented and accepted. F9 (tasks marked `done` early) is corrected in `plan.md` and recorded as R2 in `evidence.md`.
- [x] Test suite: N/A for this feature (no code); the target's suite was not run (no JVM, spec A2), disclosed in `evidence.md` §2.
- [x] Line budget respected: Ist 113 / Soll ~150 (excluding HTML comments). This includes §7, an extra section the caller required.
- [x] Status set to `passed`.


**Orchestrator note (post-review):** the reviewer's `git grep -i etag` returned three hits that were substring false positives (`PetAgeValidat…`); the conclusion stands with a word-bounded `git grep -n -iw etag` (0 hits) and the citation in F3 was corrected. Lens-firing count (§7) is prompted by the caller's trace request — see `evidence.md` §2.2.

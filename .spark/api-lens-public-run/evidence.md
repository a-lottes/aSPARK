# Evidence: api-lens-public-run

| | |
|---|---|
| Feature | api-lens-public-run |
| Phase | Act / Review (evidence for `review.md`) |
| Date | 2026-10-26 |
| Ticket | #91 |

## 1. Target (AC-1.1)

| | |
|---|---|
| Repo | `https://github.com/spring-petclinic/spring-petclinic-rest` |
| Change | PR #329 "pets v2 pagination" (branch `San-43/feature/pets-v2-pagination`), merge commit `7690a61fb289fb9b0cc41b6b2fb115e83dec122d`, merged 2026-06-13 |
| Base (first parent) | `03af87f40aafa2d2358630817c0f38bfa7e3c161` |
| Diff | `git diff -M 03af87f 7690a61` — 27 files, +506/−141 (8 of them pure v1 controller/test renames) |
| Re-run | `git clone https://github.com/spring-petclinic/spring-petclinic-rest && cd spring-petclinic-rest && git checkout 7690a61`, then `/peer-review` with `lenses/api.md` as the only active lens. Every `file:line` below resolves with `git show 7690a61:<path> \| sed -n '<line>p'` |
| Run date | 2026-10-26 (aSPARK at the commit this file lands in; model `claude-sonnet-5-5` for both orchestrator and `reviewer` agent) |

Why this diff: new versioned list endpoint (`GET /v2/pets`), a contract file (`openapi.yml`), three persistence profiles, tag renames across the whole contract, and an error handler — every section of the lens has something to bite on. Chosen over dependabot-only commits, where the lens would simply be silent.

## 2. How this run differs from a normal `/peer-review` (read before the numbers)

1. **Review-only, on a foreign repo.** The target has no `.spark/` trail and no constitution. The `api` profile was declared by the caller in the reviewer's prompt. The step "read the constitution's active lenses and pass their paths" was **not exercised**; I passed `/opt/aspark/lenses/api.md` by hand. This repo's own constitution lists `api` as *Off* (it has no routes), which is correct for this repo and irrelevant to the target.
2. **The 13-row trace table was requested by me** (§7 of `review.md`), not produced by the ordinary template. The `reviewer` agent would not necessarily emit a per-item account unprompted. So "11 of 13 fired" measures *the agent can walk the checklist when told to emit a trace*, not *the lens surfaces itself in a default review*. The unprompted firing rate is **not measured** by this run.
3. **Spec-phase half not exercised.** No NFRs exist for the target, so the lens's rule that "findings are tied to the NFR they violate" could not be tested; every finding is untied.
4. **Nothing was built or run.** No JVM in the environment. The generated `*Api` interfaces (from `openapi.yml` via openapi-generator, `pom.xml:372-374`) do not exist on disk, so anything depending on their annotations is `not-verified-live`.
5. **One run, one model, one reviewer session.** n = 1.

## 3. Author's independent pre-read (written before the reviewer ran; scratch copy `/tmp/preread.md`, transcribed here)

The reviewer was given only the diff range, the lens path and the template; it did not see this list.

- P1 `page`/`size` bounds are declared (`openapi.yml:884-900`) but the advice has no handler for query-parameter validation, only `MethodArgumentNotValidException` (`ExceptionControllerAdvice.java:117`), and a catch-all `Exception` → 500 (`:80`). Probable 500 instead of the documented 400. Unverifiable without a build.
- P2 `ETag` is declared on every 200 (`openapi.yml:905` and 60+ more) and no Java code sets one.
- P3 Versioning is path-only and only for v2; v1 has no prefix.
- P4 Tag renames (`pet`→`pets`, `owner`→`owners`, …) change generated client class names; the `V2Api` interface was dropped from the owner controller.
- P5 Pre-existing, but the renamed file appears in the diff: `updateOwner` returns 204 *with a body* (`v1/OwnerRestControllerV1.java:124`); v1 `listPets` returns 404 on empty (`v1/PetRestControllerV1.java:66`) and is unpaged.
- P6 `/v2/pets` mirrors `/v2/owners` (consistent pagination).
- P7 `@PreAuthorize` on both v2 controllers (line 32 of each).
- P8 JDBC page query loads every owner and type (`JdbcPetRepositoryImpl.java:162-170`); JPA narrows `long` offset to `int` (`JpaPetRepositoryImpl.java:81`).
- P9 v2 tests are happy-path only (`V2RestControllersTests.java:98,118`).

## 4. Per-check record (AC-2.1)

Status vocabulary: **fired** = the reviewer wrote a finding or a cited clean observation for the item; **silent** = it recorded the item as not applicable to this diff, with reason; **not-verified-live** = the answer depends on a build that did not run. Verdict column is the author's, from the primary source at `7690a61`.

| Item | Check | Status | Target citation | Author's verdict |
|---|---|---|---|---|
| 1.1 | Nouns, no RPC | fired (clean) | `openapi.yml:872` `/v2/pets` GET | agree |
| 1.2 | Honest status codes | fired + not-verified-live (part) | `PetRestControllerV2.java:33-38`; `ExceptionControllerAdvice.java:80,117` | agree on the inference; unobserved (F1). Missed P5 (below) |
| 1.3 | Pagination, no unbounded list | fired | `openapi.yml:872-924` vs `/v2/owners`; `JdbcPetRepositoryImpl.java:167-168` | clean part right; the JDBC finding is a stretch (see §5 F5) |
| 1.4 | Idempotent retries | silent | — (no new mutating endpoint) | agree |
| 2.1 | One error envelope | fired (clean) | `openapi.yml` 400/500 → `ProblemDetail`; `ExceptionControllerAdvice.java:63-71` | agree |
| 2.2 | Naming/format consistency | fired | `PetPage` vs `OwnerPage` schemas; singular `owner-v2`/`pet-v2` vs plural tags (`openapi.yml:11-20`) | agree |
| 2.3 | OpenAPI matches implementation | fired + not-verified-live (part) | ETag `openapi.yml:905`, no setter in `src/main/java` | ETag part confirmed by `git grep -n -iw etag 7690a61 -- src/main/java`; the 400 part unobserved |
| 3.1 | Versioned | fired (clean) | `openapi.yml:872`; `controller/v1/`, `controller/v2/` | agree; the reviewer noted v1 is unprefixed but raised no finding |
| 3.2 | No silent breaking change | fired | tag renames `openapi.yml:11-30`; `info.version: '1.0'` unchanged (`:8`) | right, narrow (see F4 below); wire paths unchanged, so breaking only for codegen/Swagger groups |
| 3.3 | Additive optional fields | fired (clean) | `page`/`size` `required: false` with defaults, `openapi.yml:880-900` | agree |
| 4.1 | Auth stated per endpoint | fired | code `@PreAuthorize` at `PetRestControllerV2.java:32`; no `securitySchemes`/401/403 anywhere in `openapi.yml` (`git grep` returns nothing) | right |
| 4.2 | Server-side validation | not-verified-live | `openapi.yml:884-900`, `pom.xml:374` `performBeanValidation` | right to refuse to call it; remains unobserved |
| 4.3 | Rate/size limits | fired | none in `PetRestControllerV2.java` or `BasicAuthenticationConfig.java` | right but low value (pre-existing, project-wide) |

**Count:** 13 items → 11 fired (2 of them with an unverified part), 1 silent (1.4), 1 not-verified-live (4.2). Observed once, with the trace prompted (§2.2).

## 5. Findings: right, wrong, missed (AC-2.2)

| Reviewer finding | Verdict | Basis |
|---|---|---|
| F1 Major: out-of-range `page`/`size` probably 500 not 400 | **right in reasoning, unobserved** — keep `not-verified-live` | Matches P1; the advice (`:80`, `:117`) and spec (`openapi.yml:884-900`) citations resolve. The specific exception types are inferred from generator 7.22 + Boot, not read. Whether the generated interface carries `@Min/@Max` at all is unknown. |
| F2 Major: three new `findAll(Pageable)` implementations untested | **right, but not an api-lens item** | Matches P9; only mocked service test at `V2RestControllersTests.java:119-134`. This is the generic review half, not the lens. Do not credit it to the lens. |
| F3 Minor: ETag declared, never set | **right** | Verified by grep. |
| F4 Minor: tags renamed, `info.version` unchanged | **right but weakly argued** | Matches P4. The reviewer correctly says no wire path changed. It did not notice that `OwnerRestController` stopped implementing `V2Api` (P4 second half); harmless here but it is the same class of codegen break. |
| F5 Minor: JDBC page loads all owners | **partly** | Real, matches P8, but it is an efficiency finding. Lens 1.3 is about the *response* being unbounded; the response here is bounded. Counted as a **misfire of scope**, not of fact. |
| F6 Minor: contract states no auth; tests don't run the filter | **right** | Verified no `securitySchemes`. |
| F7 Minor: no rate limit / no recorded N/A | **right, trivial** | Checklist item literal; pre-existing and project-wide. Noise rather than signal for this diff. |
| F8 Nit: JPA/JDBC ignore `pageable.getSort()` | **right** | `JdbcPetRepositoryImpl.java:159`, `JpaPetRepositoryImpl.java:80` hardcode `ORDER BY id`. Not in my pre-read; a real find. |
| F9 Minor (aSPARK side): plan marks T1–T4 `done` before evidence existed | **right — refuted-with-finding against my own process** | See §6 R2. |

**Missed by the reviewer (author found, reviewer did not write):**

- **M1** `updateOwner` returns `204 No Content` *with a body* (`v1/OwnerRestControllerV1.java:124`) — a lens 1.2 smell. The reviewer listed v1's 404-on-empty as pre-existing and out of scope (`PetRestControllerV1.java:66`) but not this one. Caveat: the file shows as new in the diff only because it was renamed; the line itself is old. A narrower-scope reviewer is defensible; recorded as a miss, not a failure.
- **M2** JPA `(int) pageable.getOffset()` silent narrowing (`JpaPetRepositoryImpl.java:81`). Minor; unreachable at `size ≤ 100` and any realistic page.
- **M3** Dropped `V2Api` interface (see F4).

**Missed by both** (author's pre-read and the reviewer): the author did not open the generated client or run the app, so any runtime defect in the new endpoint's behaviour is unseen by this run.

## 6. Failures and misfires (AC-3.2): refuted-with-finding

- **R1 — "reviewer walked the checklist" is prompted, not observed.** Claim in the issue and lens docs: the lens fires in Review. What this run shows: it fires *when the caller asks for a per-item trace and names the profile*. Not shown: that a default `/peer-review` with an active `api` lens emits the same findings. Route: a follow-up run without the trace instruction, and with a real constitution so the dispatch step is exercised. Lens text unchanged (out of scope).
- **R2 — T1–T4 were marked `done` in `plan.md` before `evidence.md` existed** (review F9). The "pre-read written before the review" claim in T1's DoD was therefore not checkable from the trail at review time. The pre-read's priority is shown only by this document's account and the scratch file's timestamp; it is not tamper-evident. I had set all four tasks to `done` when writing the plan, before T2–T4 ran; I corrected `plan.md` afterwards (T4 `in-progress` until the docs edit landed) and wrote this file. The ordering claim remains self-reported.
- **R3 — F5 is a scope misfire**: efficiency finding filed under lens 1.3. Kept in the table because it is a real defect, but not counted as lens signal.
- **R4 — F2 is generic review output**, not lens output. 2 of the 9 findings (F2, F9) are not api-lens findings at all; 1 (F5) is scope-stretched. Of the 9, 6 are lens-attributable and right (F1, F3, F4, F6, F8, F7 as low-value).
- **R5 — Dispatch, NFR-tying and the Specify half of the lens were not run** (§2.1, §2.3). The roadmap's wording "a Review lens firing and being Review-verified on a real `api`" is met only in part: the lens *content* ran on a real API; the *activation chain* did not; nothing was Review-*verified* against the running service (no build).

## 7. What this does and does not show (AC-3.1)

- Lens firing is **instruction-driven**. No test in this repo or anywhere enforces that a lens fires; it fired here because the checklist was passed to an agent and the agent was told to trace it. The 11-of-13 figure is **one observation of one prompted session**, not a rate and not a guarantee. A second session could fire more, fewer or different items.
- It shows: with the lens text in context the reviewer produced on-topic, citable, mostly correct contract findings on a real public diff (3 clearly valuable: F1, F3, F6; 2 clean extra catches: F4, F8), and refused to claim what it could not verify (4.2, F1).
- It does not show: that the lens beats a generic review (no control run without the lens was made), that the activation chain works on a project with a constitution, that Specify-phase NFRs are produced, or that anything is correct at runtime.

## 8. Scratch and fences (AC-4.2)

Target clone at `/tmp/target/spring-petclinic-rest` and the pre-read at `/tmp/preread.md` are untracked scratch; the only commands used were `git show`/`git diff`/`git grep`/`sed`. No script was written or committed. `lenses/api.md` unchanged. No `website` run.

## 9. Small correction found while verifying

The reviewer's grep for ETag code (`git grep -i etag`) returned three false positives (the substring matches `PetAgeValidat…`). It reached the right conclusion, but the command was sloppy. I re-ran it word-bounded: `git grep -n -iw etag 7690a61 -- src/main/java` → 0 hits. Both `review.md` F3 and §4 above carry the corrected command. A reviewer's cited command is not evidence until someone re-runs it.

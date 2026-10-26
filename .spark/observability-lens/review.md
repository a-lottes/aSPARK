# Review Report: observability-lens

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Commits `6c40f26` and `08e1299` on `factory/issue-89`, `.spark/observability-lens/plan.md`, `spec.md` |
| **Status** | `passed` |
| **Round** | 2 |
| **Date** | 2026-10-26 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** The spec now carries AC-1..AC-6. Every round-1 Major and Minor is confirmed fixed from source. Passed. Three Nits remain open.
- **Open:** `3 open` — Blockers: none; Majors: none (Minors/Nits: see §3)
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Round 2 re-derived every round-1 fact from source rather than from the round-1 rows (condition (a): every one is a fix being verified). Read: `git show 08e1299` in full, the current `spec.md`, `lenses/observability.md:1-60`, `lenses/security.md` section headings and `:42,:54`, `lenses/api.md:48-49`, `lenses/library.md:35-39`, `CONTRIBUTING.md:189`, `lenses/README.md:46,102`, `agents/facilitator.md:72`, `templates/constitution.md:27`, `skills/{story-time,peer-review,demo-day}/SKILL.md` dispatch lines, `.spark/constitution.md:56-62`. Ran a fresh repo-wide sweep (excluding `.spark/`) for closed type→lens lists and lens counts. This sweep found F10. `lenses/` holds 10 lens files. `plugin.json` parses and reads `0.15.0`. `origin/main` is an ancestor of `HEAD`, so the branch is current. No tool file was passed. Active lens: `library`. Open question: issue #89 is still unreadable here because `gh` is not installed and there is no network. So the spec's AC text is checked for presence and internal consistency, not for fidelity to the issue. The ACs were added to an `approved` spec during fix-mode, not by `/story-time`. Recorded here, not as a finding: the caller confirmed the ACs.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Lens follows the lens contract. Round-1 citation and conflict fixes (F5, F6) confirmed. |
| T2 | ✅ | Three activation gaps were missed by T2 and fixed at review (F2). The deviation is documented in `evidence.md` E1 and accepted. |
| T3 | ✅ | E2/E3 are labelled dry runs with 0 sessions run, and the public docs now match (F4). |
| T4 | ✅ | Docs updated. The version bump is now required by spec AC-6. The conflict with `CONTRIBUTING.md:189` is a documented exception (E4, F3). |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `.spark/observability-lens/spec.md:1-8`, `plan.md:1-12` | Spec has no AC or NFR rows, only "AC-1..AC-6 are the issue's, verbatim in intent". Plan has no test strategy. Why it matters: Review and QA trace against the spec. Fix: copy the six ACs and the prompt-material caveat into `spec.md`. r2: `spec.md:12-21` now lists AC-1..AC-6, the caveat (`:8`) and a test strategy. | fixed r2 |
| F2 | Minor | `docs/workflow.md:77`, `docs/family.md:16`, `agents/qa-tester.md:192` | AC-2 sweep incomplete: a closed type→lens list, the "9 lenses" count, and the non-`qa` example list all lacked `observability`. Fix applied at review. Re-verified r2: all three sites carry it, and E1 records them. | fixed r2 |
| F3 | Minor | `.claude-plugin/plugin.json:4`, `evidence.md` E4 | Version bump `0.14.3→0.15.0` contradicts `CONTRIBUTING.md:189` ("Don't bump the version"). r2: spec AC-6 (`spec.md:19`) now requires a semver bump per the library lens. An additive change is minor (`library.md:37-39`), so `0.15.0` is correct. The conflict is accepted as a documented exception (E4). | fixed r2 |
| F4 | Minor | `ROADMAP.md:60`, `docs/status.md:110` | Public docs said the lens "fires" on a sample `api`. Evidence says 0 sessions ran. Fix applied. Re-verified r2: both now say "expected to fire … hypothetical sample … 0 agent sessions run". | fixed r2 |
| F5 | Minor | `lenses/observability.md:24` | The boundary cited `security.md` "§1 and §5". Fixed to §2 and §5. Re-verified r2: "no credential logged" is at `security.md:42` (§2) and PII-in-logs at `:54` (§5). | fixed r2 |
| F6 | Minor | `lenses/observability.md:56` | The unauthenticated health endpoint conflicted with `api.md:49`. Fixed to "(stated as deliberately public, per `api` §4)". Re-verified r2: `api.md:48` is §4. | fixed r2 |
| F7 | Minor | `evidence.md` E4 | The semver citation was `library.md:37`; "additions are backward compatible" is `:39`. Fixed to `:37-39`. Re-verified r2. | fixed r2 |
| F8 | Nit | `lenses/observability.md:47` | §1 item 2 ("no swallowed exception, no `catch {}`") restates the Reviewer's baseline error-handling hunt, although the lens says it does not re-run that hunt. Fix: trim it to "each failure path logs once, at the right level, with context". | open |
| F9 | Nit | `lenses/README.md:102` | The README row lists silent types `library`, `cli`, `website`, but the lens (`observability.md:18`) also names `web-app`. Fix: add `web-app` to the row. The "A `api`" typo, fixed in round 1, is confirmed fixed. | open |
| F10 | Nit | `ROADMAP.md:37` | The Shipped table still says "Eight lenses"; `lenses/` holds ten and `README.md:121` says "Ten". This was stale before this feature, but E1 claims the count sweep is complete. Why it matters: it is a public count that disagrees with README. Fix: "Eight"→"Ten", unless that row is meant as a historical snapshot. That ambiguity is why it was not fixed at review. | open |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1 (activation, silent profiles, non-overlap with `security`) | `lenses/observability.md:3,9,16-27,50` | ✅ met r2. `applies-to: [api]`; silent for `library`, `cli`, static `website` and `web-app`; logging hygiene is deferred to `security` §2/§5, with no PII or credential check restated. |
| AC-2 (dispatch + activation for claimed phases) | Dispatch: `skills/story-time/SKILL.md:70-71`, `skills/peer-review/SKILL.md:48-52`, `skills/demo-day/SKILL.md:83`. Activation: `agents/facilitator.md:72`, `templates/constitution.md:27`, `lenses/README.md:46` | ✅ met. Re-derived r2 (condition b). No skill holds a closed name list, and every activation site names `observability`←`api`. Residual: `.spark/constitution.md` has no row, disclosed in E1 as `/charter`'s to amend. |
| AC-3 (silent on `library`) | `evidence.md` E2; `.spark/constitution.md:58-62` | ⚠️ met as a dry run: inferred by a read, not observed, and labelled so. |
| AC-4 (fires in Review on `api`) | `evidence.md` E3 | ⚠️ met as a dry run. Hypothetical sample, 0 sessions run. The hold rate is stated as "none measured", not as a guarantee, which is what AC-4 requires. |
| AC-5 (docs, honest labels, stale #6) | `README.md:121`, `ROADMAP.md:59-63`, `docs/status.md:110`, `docs/workflow.md:77,86`, `docs/family.md:16`, `lenses/README.md:102` | ✅ met r2. Labels say "dry-run only, unproven". The #6 mention now reads "formerly #6, already shipped". F10 is a residual Nit. |
| AC-6 (Markdown only, semver bump) | `lenses/observability.md`, `.claude-plugin/plugin.json:4` | ✅ met r2. There is no executable code. The minor bump is correct for an additive lens. |

## 5. What Was Checked

- [x] Correctness: every round-1 fix re-read at source, and all six ACs traced
- [x] Non-functional: `library` lens (semver/public surface); constitution profile unchanged
- [x] Error handling: N/A, Markdown/JSON only
- [x] Security: no secrets; lens defers logging hygiene to `security`
- [ ] Tests: no test suite exists (constitution §3). `plugin.json` is valid JSON. `claude plugin validate` is not available here.
- [x] Readability: lens reads consistently with `api.md`/`security.md`

## 6. Verdict

Passed. Round 1 blocked on F1, a spec with no acceptance criteria. The spec now carries AC-1..AC-6, a prompt-material caveat and a test strategy. Every AC traces to a concrete location. AC-3 and AC-4 are met only as dry runs, and both the evidence and the public docs label them as reads with 0 sessions run. F3 is resolved because spec AC-6 now requires the bump. Its conflict with `CONTRIBUTING.md:189` is accepted as a documented exception, and the maintainer can revert one line. All six reviewer fixes from round 1 were re-derived at source and hold. Three Nits stay open for the developer: F8, F9 and the new F10. None affects dispatch, activation or any AC verdict. One thing cannot be verified here: whether the spec's ACs match issue #89 word for word.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated
- [x] All plan deviations documented and accepted — T2 (E1), T4 version (AC-6, E4)
- [x] Test suite runs green — N/A (no suite exists); `plugin.json` is valid JSON
- [x] Line budget respected: Ist ~85 / Soll ~150 (excluding HTML comments)
- [x] Status set to `passed`

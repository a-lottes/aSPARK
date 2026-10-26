# Review Report: observability-lens

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Commit `6c40f26` on `factory/issue-89`, `.spark/observability-lens/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 1 |
| **Date** | 2026-10-26 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** Lens content and dispatch are sound; spec carries no acceptance criteria, so the gate cannot be traced. Changes requested.
- **Open:** `3 open` — Blockers: none; Majors: `F1` (Minors/Nits: see §3)
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Reviewed all 12 files of `6c40f26` (`git show 6c40f26`), plus surrounding context: `lenses/security.md`, `lenses/api.md`, `lenses/README.md`, the dispatch sites in `skills/{story-time,peer-review,demo-day}/SKILL.md`, `agents/{facilitator,product-owner,qa-tester}.md`, `templates/constitution.md`, `.spark/constitution.md`, `CONTRIBUTING.md`. Full-repo grep (excluding `.spark/`) for closed lens lists and lens counts. No tool file passed. Not reviewed: issue #89 itself (`gh` not installed, no network) — see F1. Branch is current: `main` is an ancestor of `HEAD`, one commit ahead. Active lens applied: `library` (this repo's only one, `.spark/constitution.md:58`).

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | `lenses/observability.md` follows the lens contract (frontmatter, owner table, phase-tagged checks, phase notes). |
| T2 | ⚠️ | Dispatch side clean; activation audit missed three sites (F2, fixed at review). |
| T3 | ✅ | `evidence.md` E2/E3 written and labelled as dry runs; public-doc wording overclaimed (F4, fixed). |
| T4 | ⚠️ | Docs updated; `docs/family.md` count missed (F2). Version bump contradicts `CONTRIBUTING.md:189`; justified by an AC-6 not in the repo (F3). |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `.spark/observability-lens/spec.md:1-8`, `plan.md:1-12` | Spec has no AC or NFR rows, only "AC-1..AC-6 are the issue's, verbatim in intent". Plan has no test strategy. Why it matters: Review and QA trace against the spec. The issue text is not in the repo, so every AC verdict in §4 is reconstructed from plan/evidence labels and cannot be checked; AC-6's version-bump override (F3) rests on text nobody can read here. Fix: `/story-time` copies the six ACs (and the prompt-material caveat per AC) into `spec.md` using `templates/spec.md`. | open |
| F2 | Minor | `docs/workflow.md:77`, `docs/family.md:16`, `agents/qa-tester.md:192` | AC-2 sweep incomplete. `workflow.md` kept the closed type→lens list without `observability` (the same defect fixed in `facilitator.md`/`constitution.md`). `family.md` still said "9 lenses". `qa-tester.md`'s non-`qa` example list omitted it. Why it matters: E1 claimed completeness. None of these sites gates dispatch, so behaviour is unchanged. Fix applied: all three updated, and an E1 row records them. | fixed |
| F3 | Minor | `.claude-plugin/plugin.json:4`, `evidence.md` E4 | Version bump `0.14.3→0.15.0` contradicts `CONTRIBUTING.md:189` ("Don't bump the version"). The override cites an AC-6 that is not in the spec (F1). Why it matters: a factory PR setting the release version pre-empts the maintainer. Fix: confirm AC-6 from issue #89 and record it in the spec, or revert the line. Minor: E4 already discloses it. | open |
| F4 | Minor | `ROADMAP.md:60`, `docs/status.md:110` | Public docs said the lens "fires in Review on a sample `api`". Evidence E3 says the sample is hypothetical and 0 sessions ran. Why it matters: it overclaims an observation that never happened (CLAUDE.md "Prompt material makes a check likely"). Fix applied: reworded to "expected to fire … 0 agent sessions run, inferred, not observed". | fixed |
| F5 | Minor | `lenses/observability.md:24` | Boundary cited `security.md` "§1 and §5". §1 is Transport & headers. "No credential logged" is §2 (`security.md:42`) and PII-in-logs is §5 (`security.md:54`). Why it matters: the AC-1 non-overlap pointer sent the Reviewer to the wrong section. Fix applied: §2 and §5. | fixed |
| F6 | Minor | `lenses/observability.md:56` | Health check asks for an "unauthenticated" endpoint. `api.md:49` requires every endpoint to state its auth and none to be accidentally public. With both lenses active on every `api`, the two checks read as conflicting. Fix applied: "(stated as deliberately public, per `api` §4)". | fixed |
| F7 | Minor | `evidence.md` E4 | `lenses/library.md:37` covers only breaking→major. "Additions are backward compatible" is `:39`. Fix applied: citation changed to `:37-39`. | fixed |
| F8 | Nit | `lenses/observability.md:47` | §1 item 2 ("no swallowed exception, no `catch {}`") restates the Reviewer's baseline error-handling hunt (`agents/reviewer.md:50`), although the lens says it does not re-run that hunt. Its observability angle (logged with context) is the part to keep. Fix: trim it to "each failure path logs once, at the right level, with context". | open |
| F9 | Nit | `lenses/observability.md:19`, `lenses/README.md:102`; `lenses/observability.md:18` (typo fixed at review) | The README row lists silent types `library`, `cli`, `website`, but the lens also names `web-app`. Fix: add `web-app` to the README row. The typo "A `api`"→"An `api`" was also fixed at review. | open |

## 4. Requirements Traceability

ACs reconstructed from `plan.md` Covers and `evidence.md`. They are not in the spec (F1).

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1 (lens, non-overlap with `security`) | `lenses/observability.md:1-78`, boundary `:23-27` | ✅ met after F5/F6 fixes. Logging hygiene is deferred to `security`, the checklist adds no PII/credential check, and the cross-lens wording is corrected. |
| AC-2 (dispatch + activation for claimed phases) | Dispatch: `skills/story-time/SKILL.md:70-71`, `skills/peer-review/SKILL.md:49-52`, `skills/demo-day/SKILL.md:82-85` (all re-read: condition b). Activation: `agents/facilitator.md:72`, `templates/constitution.md:27`, `lenses/README.md:46` | ✅ met after F2 fix. No skill holds a closed name list. All E1 citations verified. |
| AC-3 (silent on `library`) | `.spark/constitution.md:37,58,61`; `observability.md:3` | ⚠️ inferred by a read, not observed. Honestly labelled in E2. |
| AC-4 (fires on `api`) | `evidence.md` E3 | ⚠️ inferred by a read on a hypothetical sample, 0 sessions. Labelled as a dry run in E3. Public docs corrected (F4). |
| AC-5 (docs) | `README.md:121`, `ROADMAP.md:59-63`, `docs/status.md:110,199`, `docs/workflow.md:77,86`, `docs/family.md:16`, `lenses/README.md:102` | ✅ after F2 fix |
| AC-6 (version) | `.claude-plugin/plugin.json:4` | ⚠️ done, but the AC is unverifiable and conflicts with `CONTRIBUTING.md:189` (F3) |
| NFR (library lens: semver) | `plugin.json:4` | ✅ additive change, so a minor bump is correct if a bump is wanted at all |

## 5. What Was Checked

- [x] Correctness: lens content, frontmatter, dispatch and activation traced site by site
- [x] Non-functional: `library` lens (semver/public surface); constitution profile unchanged
- [x] Error handling: N/A, Markdown/JSON only, no executable code
- [x] Security: no secrets; lens defers logging hygiene to `security` correctly
- [ ] Tests: no test suite exists (constitution §3, Markdown only). `plugin.json` parses as valid JSON. `claude plugin validate` is not available here.
- [x] Readability: lens reads consistently with `api.md`/`security.md`

## 6. Verdict

The lens itself is good work. It owns a real gap ("can someone who was not there find out what happened?") with falsifiable checks. Its `phases: [specify, review]` claim matches the dispatch rules, which read `phases` generically. Its boundary with `security` is explicit. The three activation sites that needed hand edits were found. Review found and fixed six low-risk defects: three missed closed-list or count sites, a wrong `security` section citation, a latent conflict with `api` §4, and a public-doc overclaim that turned a hypothetical sample into an observed firing. The evidence is honest about being a read with 0 sessions run. The change still does not pass, because F1 is open. The spec contains no acceptance criteria, so every AC verdict above is reconstructed from labels in the plan and evidence rather than traced to a contract. The one AC that overrides a written contribution rule (AC-6's version bump) cannot be checked at all. Once the spec carries AC-1..AC-6 from issue #89 and F3 is resolved against them, this should pass on re-review without code changes. The reviewer's fixes are uncommitted in the working tree.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [ ] No open Major findings — F1 open
- [ ] Every Must AC traces to implementing code; no constitution non-negotiable violated — no AC is in the spec (F1); no non-negotiable violated
- [ ] All plan deviations documented and accepted — T2/T4 deviations documented here, not yet accepted
- [x] Test suite runs green — N/A (no suite exists); `plugin.json` is valid JSON
- [x] Line budget respected: Ist ~75 / Soll ~150 (excluding HTML comments)
- [ ] Status set to `passed`

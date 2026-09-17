# Review Report: lens-dispatch-registry

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment` (`3f27eda`), `.spark/lens-dispatch-registry/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 1 |
| **Date** | 2026-09-17 |

**Handoff**
- **Status:** `changes-requested` — all round-1 findings fixed by the developer (F1-F3, F6-F7) or the reviewer (F4-F5); awaiting re-review to confirm and close the gate.
- **Verdict:** The registry-sourced dispatch and activation rules are right, verified against all 9 lens frontmatters with zero omissions and zero false inclusions; the one thing that had to change — `lenses/README.md`'s new step 4 claiming a genericity the `act` phase does not have (F1) — is fixed, along with every Minor/Nit the reviewer raised.
- **Open:** `0 findings, re-review pending` — all of F1-F7 are now `fixed`; the Reviewer, not the developer, confirms each and sets `Status` to `passed`/bumps `Round`
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Reviewed: `git diff main...feat/lens-dispatch-registry` (merge-base form, single commit `3f27eda`) —
9 non-artifact files (+74/−51) plus the three `.spark/lens-dispatch-registry/` artifacts. PR #48's
later landing on `main` was excluded by the three-dot form, as instructed.

Every cited site was re-read in the **current working tree**, not from the ledger's quotes: all eight
edited resolved-instruction sites, the three receiving agents (`designer.md`, `reviewer.md`,
`qa-tester.md`), all 9 `lenses/*.md` frontmatters, `skills/increment/SKILL.md`,
`skills/story-time/SKILL.md`, `skills/charter/SKILL.md`, `docs/status.md`, `docs/workflow.md`. The
phase→lens matrix (design 4, qa 5, review 8, act 1) and the negative case were **re-derived from the
frontmatters**, not cited from `evidence.md` — triggered by condition (b), Must-AC verification
(AC-2.4, NFR-4, NFR-5). The protected-template byte-identity check (NFR-6/C5) was likewise re-run from
scratch against `git show main:templates/spec.md` — condition (b) and (d).

Not reviewed: `.spark/accessibility-lens/` (prior feature, cited only), `docs/…` beyond the two
residual sites, and the positive firing case — no venue exists (spec §3 A2), `not-verified-live` by
design and correctly not asserted anywhere in the diff.

Tool note: `aspark-graph` was **not** re-run. Plan §2 records that all seven (later nine) target paths
return under `unknown_files` with empty `files`/`affected_stories`/`affected_acs` — the tool holds no
data on this repo's plugin material, so a fresh query could not tell me where to look. Scoping was done
by hand: `grep -rn 'lenses/'` over `skills/ agents/ templates/` to enumerate every lens-path reference,
and a regex sweep for multi-lens-name enumerations. That sweep found no ninth resolved-instruction site;
the only remaining enumerations are the type-triggered vocabulary (spec §6 / C2, out of scope) and
non-restrictive "e.g." forms.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Matrix re-derived independently from the 9 frontmatters: design 4, qa 5, review 8, act 1 — matches |
| T2 | ✅ | `skills/look-and-feel/SKILL.md:33-37`; resolves to `{seo, ux, i18n, accessibility}`. Sentence was garbled — F4, fixed |
| T3 | ✅ | `skills/demo-day/SKILL.md:82-85`; resolves to `{ux, seo, security, i18n, accessibility}`; the browser-observable→`phases: qa` widening is recorded as planned (see F6 for the receiving-layer residue) |
| T4 | ✅ | `skills/peer-review/SKILL.md:49-52`; parenthetical gone, resolves to 8 |
| T5 | ✅ | `agents/facilitator.md:51-55`, `:68-72`; no enumerated characteristic or lens list remains; resolves to 6 characteristics and 4 characteristic-triggered lenses |
| T6 | ✅ | `templates/constitution.md:27-28`, `:35`; headings/columns/rows byte-identical (re-verified), only the two HTML comments changed |
| T7 | ⚠️ | `skills/spark/SKILL.md:64-68`; list gone, but the DoD's `${CLAUDE_PLUGIN_ROOT}/…` reference and the plural were lost — F5, fixed |
| T8 | ✅ | `templates/spec.md:69-72`; structure byte-identical (re-verified from `main`), comment-only, three names readable as examples |
| T9 | ✅ | Cross-check reproduced independently; zero omissions, zero false inclusions, both layers |
| T10 | ⚠️ | Negative case and `validate` correct; the diff-level compatibility assertion covers only 7 of 9 files — F2 |
| T11 | ⚠️ | Caveat retired and links kept+repointed as required, but the replacement overclaims and omits the `act` caveat plan §5 R5 explicitly assigned to this task — F1. Also leaves the characteristic→lens fact declared twice in one file — F3 |
| T12 | ✅ | `README.md:321`, `:340-346`; claim bounded to the eight sites, both residuals named with `file:line` |

**Scope widening (plan §1, user-directed).** I judge it legitimate, independently of the plan's own
argument. C1 did settle the framing as a general-mechanism fix, so two more instances of the same
mechanism are not a new decision; the spec's success signal ("none of the **six** sites contains a
hardcoded list") is over-satisfied rather than contradicted; AC-3.2's "states the gap is closed" branch
is the one the widening enables; and I verified the §6/C2 fence held — T7 and T8 edited *lens-name*
lists only, while the type-triggered lists at `agents/facilitator.md:67-68`, `templates/constitution.md:26-27`
and `lenses/README.md:45-46` are all still present and untouched. The one real cost is that T7/T8 carry
no AC, so AC-3.2's "all eight sites" claim rests on work no AC verifies — NFR-4/T9 covers it, and the
plan says so up front. Not a finding.

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `lenses/README.md:127-131` | New step 4 claims "a lens with **any combination of phases** … reaches its agents … with no skill, agent or template edit". False for `phases: act`: `skills/increment/SKILL.md` contains **zero** lens references (grep, whole file), so nothing dispatches lens files at Act — the increment's own ledger says exactly this at `evidence.md:413-418`, and plan §5 R5 predicted the overclaim and assigned the caveat to T11, which never wrote it. Matters because this is the one file a future lens author reads before shipping; an author declaring `act` would expect dispatch and get silence — the same failure mode this feature exists to end — and constitution §1 makes "a doc that presents an intention as delivered" a defect. Fix: append the ledger's own qualifier, e.g. "— the one exception is Act: `/increment` dispatches no lens files, so an `act` check is realized through the spec's §5 NFRs, not by dispatch." | fixed |
| F2 | Minor | `.spark/lens-dispatch-registry/evidence.md:445-451` | T10's NFR-6 assertion states the diff "shows exactly 7 files changed … 39 insertions, 30 deletions … nothing outside it". The shipped increment changes **9** non-artifact files: `README.md` (+12/−5) and `lenses/README.md` (+23/−16) were added by T11/T12 after T10 ran (`git diff --numstat main...feat/lens-dispatch-registry -- ':!.spark'`). Matters because NFR-6 is the library lens's compatibility bar and is supposed to cover the whole diff; a present-tense claim that silently excludes two files is not the coverage it advertises, and this repo's `CLAUDE.md` warns precisely against carrying a gate's word forward. Compatibility itself **does** hold — I re-derived it over all 9 files. Fix: date-stamp the snapshot ("as of T10, before T11/T12") and add one line covering the two doc files, or re-run the stat and restate 9. | fixed |
| F3 | Minor | `lenses/README.md:47-49` vs. `:86-92` | The characteristic→lens fact is now declared **twice** in the registry — the *Two ways a lens activates* bullets and the Characteristics table's `Activates` column — and the two consumers read different copies: `agents/facilitator.md:70` and `templates/constitution.md:27` point at the bullets, `agents/facilitator.md:52` and `templates/constitution.md:35` at the table. That is a partial deviation from plan §1's own decision ("read each fact at its single declaration site, never at a copy"): an author updating one copy silently breaks the other consumer. Mitigated but not closed by step 3's hand-update instruction. Fix: make the *Two ways* section refer to the Characteristics table's `Activates` column instead of restating the mapping, and point both `/charter` consumers at that one table. | fixed |
| F4 | Nit | `skills/look-and-feel/SKILL.md:34-37` | The new instruction's object was stranded: "pass the path of every active lens whose … includes `design` — read each active lens's file (…); do not work from a list of lens names given here — **in step 4**", with the trailing clause two lines from its verb. Matters because this is prompt text an agent parses under load. Fixed by reordering to "… includes `design` in step 4. To decide, read each active lens's file …" — no semantic change. | fixed |
| F5 | Nit | `skills/spark/SKILL.md:66-67` | Two regressions against T7's own DoD: "the matching **lens** … **activates**" where several may activate (the replaced text was plural), and "the registry's *Available lenses* table" with no resolvable path, where the DoD asked for `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s table and constitution §3 requires that form. Fixed: restored the plural and the explicit `${CLAUDE_PLUGIN_ROOT}` path. | fixed |
| F6 | Nit | `agents/qa-tester.md:174-176` vs. `skills/demo-day/SKILL.md:82-85` | Dispatch now selects by `phases: qa` (T3's deliberate widening away from "browser-observable"), but the receiving instruction still says to verify each lens's "**browser-observable** checks" and adds "(Lenses like `api`, `cli`, `library`, `data` have no browser surface…)". No live defect — every qa-phase lens's checks happen to be browser-observable today — but the two layers now define the same set by different criteria, and under constitution §8 substitute-method projects the receiving filter is the narrower one. Plan §2's "verified generic, no edit needed" is true for *membership* only, not for this qualifier. Fix (when next touched): align the receiving clause to "the checks it marks for the `qa` phase". | fixed |
| F7 | Minor | `templates/spec.md:69`, `templates/constitution.md:27`, `:35` | The three new registry pointers are written as relative prose — "the plugin's lenses/README.md" — while the five non-template sites in the same diff correctly use `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`; constitution §3 Patterns: "Plugin-internal paths are always referenced as `${CLAUDE_PLUGIN_ROOT}/…`, never relative." Matters more after this change than before: these comments are instantiated *into a consumer project*, and they no longer carry the list inline, so a reference that doesn't resolve now yields no vocabulary at all rather than a stale one. Left open rather than fixed because `templates/constitution.md:25` used this phrasing pre-diff, so there is a plausible deliberate template convention to rule on. Fix: use `${CLAUDE_PLUGIN_ROOT}/lenses/README.md` in all three (and optionally `:25`). | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `agents/facilitator.md:51-55` → `lenses/README.md:82-92` (6 rows, `must-be-accessible` present) | ✅ met |
| AC-1.2 | `agents/facilitator.md:68-72` → `lenses/README.md:45-49`; resolves to `security`, `i18n`, `data`, `accessibility` — all four, per plan §1's recorded reading | ✅ met |
| AC-1.3 | `templates/constitution.md:27-28`, `:35` | ✅ met |
| AC-1.4 | `lenses/README.md:112-126` steps 1-3 + the two sites above; a 10th lens needs no edit to `facilitator.md` or `templates/constitution.md` | ✅ met |
| AC-2.1 | `skills/look-and-feel/SKILL.md:33-37` → `{seo, ux, i18n, accessibility}` | ✅ met |
| AC-2.2 | `skills/demo-day/SKILL.md:82-85` → `{ux, seo, security, i18n, accessibility}` | ✅ met |
| AC-2.3 | `skills/peer-review/SKILL.md:49-52`; parenthetical removed entirely → 8 lenses | ✅ met |
| AC-2.4 | The three sites above + generic receiving clauses re-read at `agents/designer.md:62-64,76-77`, `agents/reviewer.md:62-64,80`, `agents/qa-tester.md:174-176,193-194` | ✅ met |
| AC-3.1 | `lenses/README.md:127-136` — caveat retired, both links present (kept + repointed), but the replacement claim overreaches into `act` | ⚠️ partial (F1) |
| AC-3.2 | `README.md:321`, `:340-346`; claim scoped to the eight sites, both prose residuals named | ✅ met |
| NFR-4 | Re-derived from all 9 frontmatters: design `{accessibility,i18n,seo,ux}`, qa `{+security}`, review `{all but ux}`, act `{accessibility}` — every one named by the matching rewritten instruction, none falsely included | ✅ met |
| NFR-5 | Negative case re-derived live: `library` = `[specify, review]` → design ∅, qa ∅, review `{library}`, identical to T1. Independently corroborated by this very run — `/peer-review` passed me `library.md` and nothing else | ✅ met |
| NFR-6 | Re-verified over all 9 changed files: no slash command renamed; `templates/spec.md` and `templates/constitution.md` headings/columns/`NFR-n` patterns byte-identical to `main` (diff of extracted heading+table lines is empty); both plugin manifests untouched; every dispatch set is a strict **superset** of the list it replaced, so no consumer loses a lens — additive, minor-bump | ✅ met |

## 5. What Was Checked

- [x] Correctness: every Must AC traced to its resolved instruction text, re-read in the working tree
- [x] Non-functional: NFR-4/5/6 re-derived from primary source; constitution §1, §3, §4, §6 checked against the diff
- [x] Error handling: N/A — prompt material, no runtime. The one failure mode (malformed `phases`) is documented at `lenses/README.md:114-117` per R4
- [x] Security: N/A — no user input, no secrets, no network surface touched (spec NFR-2)
- [x] Tests: `claude plugin validate .` re-run after my fixes — passes with the one pre-existing, unrelated `autoUpdate` warning. No suite exists and none is possible (constitution §4); the read-based dry run is the bar and it was performed
- [x] Readability: two garbled/regressed instruction sentences found and fixed (F4, F5)
- [x] Library lens (§1 public surface, §2 compatibility, §4 contract clarity; §3 N/A per constitution §2): no surface added, no contract structure renamed, docs shipped in the same change

## 6. Verdict

The mechanism this feature set out to build is correct and I could not break it: all eight closed
enumerations are gone, each replaced by a rule that reads the fact at its declaring site, and when I
re-derived the phase sets from the nine lens frontmatters myself — rather than trusting the ledger — every
rewritten instruction resolved to exactly the right set, with `accessibility` now included at design, qa
and review where it previously reached none of them, and with no lens falsely included anywhere. The
protected-template edit is genuinely comment-only: extracting every heading and table line from
`templates/spec.md` and diffing it against `main` returns empty, so C5's "no major bump" holds, as does
NFR-6 more broadly — every new dispatch set is a strict superset of the list it replaced, so no installed
consumer loses anything. The two deliberately-left-open residuals are honestly disclosed, not glossed:
`docs/status.md:34` and `docs/workflow.md:40-42` really do still list eight lenses, and both are named
with `file:line` in the ledger, in `README.md`'s row and in `lenses/README.md`'s step 3, framed as
documentation accuracy rather than as a dispatch gap — which is what they are. What stops this passing is
F1: in retiring a caveat that was true, step 4 replaced it with a claim that is not — "any combination of
phases … reaches its agents" is false for `act`, where no skill dispatches anything, and the plan's own
R5 flagged that this task had to say so. A feature whose thesis is that a stale closed list silently
misleads the next lens author should not ship a stale open claim in the same paragraph. Fix F1, decide
F7 (a one-line convention call), and this is ready for QA; F2, F3 and F6 are real but can ride to the
fix pass or the next feature at the developer's discretion.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [ ] No open Major findings (or explicitly waived by the user, with reason recorded here) — `F1` open; only the user may waive a Major
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated (§6's five non-negotiables checked; F1 and F7 touch §1 and §3, neither of which is a §6 non-negotiable)
- [x] All plan deviations documented and accepted — T7, T10, T11 deviate; each is recorded in §2 and carries a finding
- [x] Test suite runs green — no suite exists (constitution §4); `claude plugin validate .` passes with the one pre-existing warning, re-run after the reviewer's fixes
- [x] Line budget respected: Ist 147 / Soll ~150 (excluding HTML comments)
- [ ] Status set to `passed` — `changes-requested` while F1 is open

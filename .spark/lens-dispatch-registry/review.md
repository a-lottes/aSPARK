# Review Report: lens-dispatch-registry

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The diff of `/increment` (`3f27eda`) plus the fix-mode commit (`f32be5c`), `.spark/lens-dispatch-registry/plan.md` |
| **Status** | `passed` |
| **Round** | 2 |
| **Date** | 2026-09-17 |

**Handoff**
- **Status:** `passed` — F1 (the only gate-blocking Major) is genuinely closed, verified against the current files rather than the fix-mode ledger; two new Nits (F8, F9) are open and block nothing.
- **Verdict:** Every round-1 finding is resolved. The `act` exception is now stated honestly and the four phases the new step-4 text *does* claim (`specify`, `design`, `review`, `qa`) each really are reached without a skill edit — I re-derived all five phase sets from the nine frontmatters and traced each to its dispatching skill. F2 had regressed inside the very commit that fixed it (its restated file count omitted its own `agents/qa-tester.md` edit); the Reviewer corrected the numbers this round.
- **Open:** `2 findings` — F8, F9, both Nit, both documentation-accuracy residue of the fix pass; route to the next touch of `lenses/README.md` / the ledger, not back to `/increment`
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Re-review of `f32be5c` ("close round-1 review findings F1-F7") layered on the already-reviewed
`3f27eda`. Judged against the **combined** diff `git diff main...feat/lens-dispatch-registry` —
10 non-artifact files (+88/−59; round 1 saw 9, `agents/qa-tester.md` is new via F6) plus the
`.spark/lens-dispatch-registry/` artifacts.

Every one of F1-F7 was verified by re-reading the **current file**, never the fix-mode ledger entry or
the developer's claim — condition (a), verifying a fix, on all seven. The phase→lens matrix was
re-derived from scratch from the nine `lenses/*.md` frontmatters (condition (b), Must-AC verification):
specify 9, design 4, qa 5, review 8, act 1 — unchanged from round 1. The protected-template check was
re-run against `git show main:…` over the **combined** diff, not the fix commit alone (conditions (b)
and (d)): every changed line in `templates/spec.md` and `templates/constitution.md` sits inside an HTML
comment, and the extracted heading/table/`NFR-n` streams diff empty against `main`.

New this round because the fix touched them: `skills/story-time/SKILL.md:26-42` and
`agents/product-owner.md:74-80` (the Specify-phase path, which step 4's new wording now names
explicitly), a repo-wide sweep for the retired "browser-observable"/"no browser surface" phrasing, and a
sweep for any surviving relative `the plugin's lenses/README.md` reference (none remain).

Not reviewed: `.spark/accessibility-lens/` (prior feature, cited only), `docs/…` beyond the two
residuals, and the positive firing case — no venue exists (spec §3 A2), `not-verified-live` by design.

Tool note: `aspark-graph` was not re-run, for the reason recorded in round 1 — it holds no data on this
repo's plugin material (plan §2), so it could not tell me where to look. Scoping was by hand:
`grep -rn 'lenses/'` and `grep -rln lens` over `skills/ agents/ templates/`, which enumerates 13 files
and found no dispatch site the fix pass missed or broke.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Matrix re-derived independently from the 9 frontmatters: design 4, qa 5, review 8, act 1 — matches |
| T2 | ✅ | `skills/look-and-feel/SKILL.md:33-38`; resolves to `{seo, ux, i18n, accessibility}`; F4's reordering landed |
| T3 | ✅ | `skills/demo-day/SKILL.md:82-85`; resolves to `{ux, seo, security, i18n, accessibility}`; the receiving layer now matches (F6) |
| T4 | ✅ | `skills/peer-review/SKILL.md:49-52`; parenthetical gone, resolves to 8 |
| T5 | ✅ | `agents/facilitator.md:51-55`, `:69-72`; both now cite the one Characteristics table (F3); resolves to 7 characteristics and 4 characteristic-triggered lenses |
| T6 | ✅ | `templates/constitution.md:26-28`, `:36`; headings/columns/rows byte-identical to `main` across both commits, only HTML comments changed |
| T7 | ✅ | `skills/spark/SKILL.md:64-68`; F5's plural and `${CLAUDE_PLUGIN_ROOT}` path restored |
| T8 | ✅ | `templates/spec.md:69`; comment-only against `main`, now in `${CLAUDE_PLUGIN_ROOT}` form (F7) |
| T9 | ✅ | Cross-check reproduced independently; zero omissions, zero false inclusions, both layers |
| T10 | ⚠️ | Negative case and `validate` correct; the diff-level compatibility assertion was restated in fix mode and still undercounted — F2, now corrected |
| T11 | ✅ | Caveat retired, `act` exception written, mapping now declared once — F1/F3 closed; one stale author instruction remains (F8) |
| T12 | ✅ | `README.md:321`, `:340-346`; unchanged by the fix pass, claim still bounded to the eight sites |

**Fix-pass deviation.** `agents/qa-tester.md` is a file plan §2 classified as "verified generic, no edit
needed"; F6's fix edited it. I judge that legitimate and in-scope: the edit changes only the receiving
clause's *description* of the set it is handed (`:174-176`, `:191-193`), not which lenses it receives,
so the genericity plan §2 asserted is intact. It is disclosed in the ledger at `evidence.md:595-602`.
**Scope widening (plan §1, user-directed)** is unchanged from round 1 and remains legitimate: the
§6/C2 fence still holds — the type-triggered lists at `agents/facilitator.md:67-68`,
`templates/constitution.md:27`, `:35` and `lenses/README.md:45-46` are all still present and untouched.

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `lenses/README.md:128-140` | New step 4 claimed "a lens with **any combination of phases** … reaches its agents … with no skill, agent or template edit". False for `phases: act`: `skills/increment/SKILL.md` contains **zero** lens references (grep, whole file), so nothing dispatches lens files at Act. Matters because this is the one file a future lens author reads before shipping; an author declaring `act` would expect dispatch and get silence — the same failure mode this feature exists to end — and constitution §1 makes "a doc that presents an intention as delivered" a defect. **Fixed r2, verified independently:** the claim is now enumerated (`specify`, `design`, `review`, `qa`) with `act` excepted in the developer's own words. All five re-derived: `act` still has zero dispatchers (`grep -c -i lens skills/increment/SKILL.md` = 0); `design`/`qa`/`review` are phase-filtered at `skills/look-and-feel/SKILL.md:34`, `skills/demo-day/SKILL.md:83`, `skills/peer-review/SKILL.md:49`; `specify` reaches the PO via `skills/story-time/SKILL.md:41`, which passes *every* active lens unfiltered — over-dispatch, not under-dispatch, and `agents/product-owner.md:80` handles "a lens with nothing relevant" explicitly, so the claim holds for it too. No new inaccuracy. | fixed r2 |
| F2 | Minor | `.spark/lens-dispatch-registry/evidence.md:454-460` | T10's NFR-6 assertion stated the diff "shows exactly 7 files changed", excluding the two files T11/T12 added after T10 ran. Matters because NFR-6 is the library lens's compatibility bar and is supposed to cover the whole diff. **Regressed within its own fix and corrected r2:** the fix-mode restatement replaced "7" with a present-tense "**9** files changed … 74 insertions, 30→51 deletions" — which omits the *same commit's* F6 edit to `agents/qa-tester.md` and understates `lenses/README.md` (+29/−18, not +23/−16). Re-derived: `git diff --numstat main...feat/lens-dispatch-registry -- ':!.spark'` = **10 files, +88/−59**. Compatibility itself does hold over all 10 — `agents/qa-tester.md` is an agent prompt, clarifying, no set narrowed. Reviewer corrected the passage to 10 files with the numbers pinned to commit `f32be5c` so it cannot silently go stale a third time. | fixed r2 |
| F3 | Minor | `lenses/README.md:47-50` vs. `:85-93` | The characteristic→lens fact was declared **twice** in the registry and the two consumers read different copies, contradicting plan §1's "read each fact at its single declaration site, never at a copy". **Fixed r2, verified independently:** the *Two ways* bullet now defers ("it is the single declaration of this fact, not restated here") and all four consumer pointers — `agents/facilitator.md:52`, `:70`, `templates/constitution.md:28`, `:36` — resolve to the one Characteristics table at `:85-93`. Grep confirms no second copy of the mapping survives outside that table. AC-1.1/AC-1.2 still resolve correctly through the new pointers (7 characteristics; `security`, `data`, `i18n`, `accessibility`). | fixed r2 |
| F4 | Nit | `skills/look-and-feel/SKILL.md:33-38` | The new instruction's object was stranded two lines from its verb ("… includes `design` … — **in step 4**"), hard for an agent to parse under load. **Fixed r2:** reordered to "… includes `design` in step 4. To decide, read each active lens's file …"; re-read in the working tree, semantics unchanged, dispatch set still `{seo, ux, i18n, accessibility}`. | fixed r2 |
| F5 | Nit | `skills/spark/SKILL.md:66-68` | Two regressions against T7's own DoD: a singular "the matching **lens** … activates" where several may, and "the registry's *Available lenses* table" with no resolvable path where constitution §3 requires `${CLAUDE_PLUGIN_ROOT}/…`. **Fixed r2:** current text reads "the matching lenses — see `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s *Available lenses* table … — activate for every phase"; both plural and path confirmed in the file. | fixed r2 |
| F6 | Nit | `agents/qa-tester.md:174-176`, `:191-193` | Dispatch selects by `phases: qa` but the receiving instruction still said "**browser-observable** checks" and "(Lenses like `api`, `cli`, `library`, `data` have no browser surface…)" — two layers defining one set by different criteria, the receiving one narrower under constitution §8. **Fixed r2, verified independently:** now "verify the checks it marks for the **qa** phase" and "don't declare a `qa` phase". The replacement claim is true — `api`, `cli`, `library`, `data` all declare `phases: [specify, review]`, re-read from frontmatter. Repo-wide grep: no skill, agent or template outside `.spark/` still keys off the retired phrasing; `templates/qa-report.md:44`, `:97` use "browser-observable **NFR**", a different concept, untouched and unaffected. | fixed r2 |
| F7 | Minor | `templates/spec.md:69`, `templates/constitution.md:26`, `:28`, `:36` | Three new registry pointers used relative prose ("the plugin's lenses/README.md") against constitution §3 Patterns ("Plugin-internal paths are always referenced as `${CLAUDE_PLUGIN_ROOT}/…`, never relative"). Matters more after this change because these comments are instantiated into a consumer project and no longer carry the list inline. **Fixed r2, verified independently:** all three now use the explicit form, as does the pre-existing `:26` reference that round 1 left optional; `grep -rn "plugin's lenses/README"` over `skills/ agents/ templates/ lenses/ docs/ README.md` returns nothing. Byte-identity re-checked over the **combined** diff from `main`: every `+`/`−` line in both templates lies inside an HTML comment, and the heading/table/`NFR-n` streams diff empty — C5 and NFR-6 hold. | fixed r2 |
| F8 | Nit | `lenses/README.md:119-122` | Step 3 still tells a lens author that a new characteristic must be hand-added "to the detection-signals tables above **and the *Two ways a lens activates* section**". F3's fix made that section stop restating the characteristic mapping, so for a characteristic-triggered lens there is now nothing to update there — and an author who follows the instruction literally would re-introduce the duplicate declaration F3 just removed. Matters because step 3 is the author-facing contract and F3's whole point was one declaration site. Fix: scope that clause to type-triggered lenses, e.g. "… and, for a new **type**, the *Two ways a lens activates* bullets". | open |
| F9 | Nit | `.spark/lens-dispatch-registry/evidence.md:198-201` | T3's write-up still asserts the `api`/`cli`/`library`/`data` parenthetical in `agents/qa-tester.md` "is accurate and **untouched**" — F6's fix in the same ledger (`:595-602`) rewrote exactly that parenthetical, so the two sections now contradict each other on a point of fact. Artifact-wording only: it changes no verdict, no gate answer and no Must AC (capped at Minor by rule; Nit here). Matters because `lenses/README.md:136-140` links this ledger as "the worked proof". Fix: add a forward pointer at `:199` — "(superseded by the F6 fix below; the parenthetical now reads 'don't declare a `qa` phase')". | open |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `agents/facilitator.md:51-55` → `lenses/README.md:85-93` (7 rows, `must-be-accessible` present) | ✅ met |
| AC-1.2 | `agents/facilitator.md:69-72` → `lenses/README.md:85-93` `Activates` column; resolves to `security`, `data`, `i18n`, `accessibility` — all four | ✅ met |
| AC-1.3 | `templates/constitution.md:26-28`, `:36` | ✅ met |
| AC-1.4 | `lenses/README.md:113-127` steps 1-3 + the two sites above; a 10th lens needs no edit to `facilitator.md` or `templates/constitution.md` | ✅ met |
| AC-2.1 | `skills/look-and-feel/SKILL.md:33-38` → `{seo, ux, i18n, accessibility}` | ✅ met |
| AC-2.2 | `skills/demo-day/SKILL.md:82-85` → `{ux, seo, security, i18n, accessibility}` | ✅ met |
| AC-2.3 | `skills/peer-review/SKILL.md:49-52`; parenthetical removed entirely → 8 lenses | ✅ met |
| AC-2.4 | The three sites above + generic receiving clauses re-read at `agents/designer.md:62-64,76-77`, `agents/reviewer.md:62-64,80`, `agents/qa-tester.md:174-176,191-193` | ✅ met |
| AC-3.1 | `lenses/README.md:128-140` — caveat retired, both links present, and the replacement claim is now bounded to the four phases that really are generic, with `act` excepted (F1) | ✅ met r2 |
| AC-3.2 | `README.md:321`, `:340-346`; claim scoped to the eight sites, both prose residuals named; untouched by the fix pass | ✅ met |
| NFR-4 | Re-derived from all 9 frontmatters: design `{accessibility,i18n,seo,ux}`, qa `{+security}`, review `{all but ux}`, act `{accessibility}`, specify `{all 9}` — every one named by the matching rewritten instruction, none falsely included | ✅ met |
| NFR-5 | Negative case re-derived live: `library` = `[specify, review]` → design ∅, qa ∅, review `{library}`. Corroborated by this run — `/peer-review` passed me `library.md` and nothing else | ✅ met |
| NFR-6 | Re-verified over all **10** changed files: no slash command renamed; both protected templates comment-only against `main` across the combined diff; both plugin manifests untouched; every dispatch set still a strict superset of the list it replaced, and F6's edit narrows nothing — additive, minor-bump | ✅ met |

## 5. What Was Checked

- [x] Correctness: every Must AC re-traced to its resolved instruction text in the working tree; all seven round-1 fixes verified from the file, not the ledger
- [x] Non-functional: NFR-4/5/6 re-derived from primary source; constitution §1, §3, §4, §6 re-checked against the fix-mode diff
- [x] Error handling: N/A — prompt material, no runtime. The one failure mode (malformed `phases`) is documented at `lenses/README.md:115-118` per R4
- [x] Security: N/A — no user input, no secrets, no network surface touched (spec NFR-2)
- [x] Tests: `claude plugin validate .` re-run on `f32be5c` — "Validation passed with warnings", the same single pre-existing, unrelated `autoUpdate` warning. No suite exists and none is possible (constitution §4); the read-based dry run is the bar and was performed
- [x] Cross-reference integrity (new this round): swept for anything still keyed to the phrasing the fix pass retired — "browser-observable"/"no browser surface" and relative `the plugin's lenses/README.md`; found one stale author instruction (F8) and one self-contradiction inside the ledger (F9), both Nit
- [x] Library lens (§1 public surface, §2 compatibility, §4 contract clarity; §3 N/A per constitution §2): no surface added, no contract structure renamed, docs shipped in the same change

## 6. Verdict

This passes. The one thing that blocked round 1 is genuinely fixed and fixed in the right way: step 4 no
longer claims a genericity the mechanism does not have, and — more to the point — the four phases it
*does* now claim each survived an independent check rather than a re-read of the developer's sentence.
`act` still has zero dispatchers in `/increment`, and the new exception says exactly that; `design`, `qa`
and `review` resolve through their phase-filtering skills; and `specify`, the phase the new wording adds,
holds for a reason the fix text doesn't state but that I confirmed — `/story-time` passes every active
lens unfiltered, so a `specify` lens cannot fail to arrive, and the PO's "a lens with nothing relevant"
rule absorbs the over-dispatch. F3 collapsed the duplicate mapping to one table that all four consumers
now cite, F6 aligned the receiving clause with a replacement claim I verified against the four
frontmatters it names, and F7's `${CLAUDE_PLUGIN_ROOT}` conversion left both protected templates
comment-only against `main` across the *combined* diff, not just the fix commit — headings, columns and
`NFR-n` patterns all byte-identical, so C5 holds. The blemish worth naming is that the fix pass repeated
its own mistake in miniature: F2's correction restated the file count in the present tense and left out
the very edit that commit was making (`agents/qa-tester.md`), so the ledger claimed 9 files where the
diff has 10 — I re-derived the numbers and corrected the passage, pinning it to a commit so it cannot
drift again. What remains is two Nits that block nothing and should ride to the next touch: step 3 still
tells a lens author to update a section F3 just emptied (F8), and the ledger's T3 section still calls a
parenthetical "untouched" that its own fix-mode section rewrote (F9). Neither changes a dispatch set, a
gate answer or a Must AC. Ready for QA.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here) — `F1` confirmed fixed at round 2; nothing waived
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated (§6's five non-negotiables re-checked against the fix-mode diff; F8/F9 touch neither)
- [x] All plan deviations documented and accepted — T10 still deviates (F2, corrected); the fix pass's edit to `agents/qa-tester.md` is recorded in §2 and in the ledger
- [x] Test suite runs green — no suite exists (constitution §4); `claude plugin validate .` passes on `f32be5c` with the one pre-existing warning
- [x] Line budget respected: Ist 149 / Soll ~150 (excluding HTML comments)
- [x] Status set to `passed` — two open Nits (F8, F9), no Blocker or Major

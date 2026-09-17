# QA Report: lens-dispatch-registry

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | `.spark/constitution.md` §8 (QA method), `.spark/lens-dispatch-registry/spec.md` |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-09-17 |

**Handoff**
- **Status:** `passed`
- **Verdict:** Ship it. All 10 Must ACs and all 3 QA-owned NFRs independently re-derived from the current working tree (branch `feat/lens-dispatch-registry`, HEAD `5008adb`) — not cited from `review.md` or `evidence.md`. Zero discrepancies found against either artifact.
- **Open:** `none`
- **Binding ruling:** §5 Verdict and the gate checklist below
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch at the next `/demo-day` and proceed.

## 1. Test Environment

- **App URL:** N/A — `.spark/constitution.md` §8 declares `Browser-observable surface: no` for aSPARK Core (a Claude Code plugin of Markdown, zero executable files) and names the substitute method: hands-on QA against the installed plugin, where a performed step is a real command whose output was observed or a real file read with its text quoted.
- **Method used:** real `grep`/`git diff`/`git show`/`sed` commands against the working tree at `feat/lens-dispatch-registry` (HEAD `5008adb`), plus `claude plugin validate .` — no browser opened, no reasoning about what a file "would" resolve to.
- **Browser / viewport(s):** N/A per §8.
- **Test data / accounts used:** N/A.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Read `agents/facilitator.md:51-55` | Vocabulary sourced from registry table, not a capped 6-name list | Reads "the current characteristic list from `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s *Characteristics* detection-signals table rather than working from a list here" — table at `lenses/README.md:85-93` has 7 rows incl. `must-be-accessible` | ✅ pass |
| AC-1.2 | Read `agents/facilitator.md:69-72`; cross-derive `Activates` column | Mapping resolves to all 4 characteristic-triggered lenses (`security`,`i18n`,`data`,`accessibility`) | Text points to `Activates` column, no name list; column values re-read: `handles-auth/is-public/handles-payments/handles-pii`→`security`, `has-database`→`data`, `is-multilingual`→`i18n`, `must-be-accessible`→`accessibility` — all 4 present | ✅ pass |
| AC-1.3 | Read `templates/constitution.md:22-36`; `git diff main...HEAD -- templates/constitution.md` | Comment points to registry, no embedded 6-item copy | Both the profile comment and characteristics comment now read "see `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s ... detection-signals table"; diff shows every changed line sits inside an HTML comment, headings/table/columns unchanged | ✅ pass |
| AC-1.4 | Re-read `lenses/README.md` "Adding a lens" steps 1-3 + `facilitator.md`/`templates/constitution.md` pointers | A 10th (hypothetical) lens needs no edit to either file | Both files defer to the registry table by rule, not enumeration — a new row added at step 3 is picked up with zero further edit | ✅ pass |
| AC-2.1 | Read `skills/look-and-feel/SKILL.md:32-38` | Names every active lens whose `phases` includes `design`, not a 3-name subset | "pass the path of every active lens whose own frontmatter `phases` field includes `design`... do not work from a list of lens names given here" — no lens name appears | ✅ pass |
| AC-2.2 | Read `skills/demo-day/SKILL.md:78-85` | Names every active lens whose `phases` includes `qa`, not a 4-filename subset | Same computed-set phrasing, "field includes `qa`... do not work from a list of lens names given here" | ✅ pass |
| AC-2.3 | Read `skills/peer-review/SKILL.md:45-52` | 7-name parenthetical removed/non-restrictive | Same computed-set phrasing for `review`; grep for a name list in this block returns nothing | ✅ pass |
| AC-2.4 | `grep phases lenses/*.md`; read `agents/designer.md:62-77`, `agents/reviewer.md:62-80`, `agents/qa-tester.md:174-193` | Resolved sets (design 4, qa 5, review 8) actually reach each agent via a generic ("apply only lenses you were given") head clause | Frontmatter re-derived: design={accessibility,i18n,seo,ux}, qa={accessibility,i18n,security,seo,ux}, review=all 9 minus `ux` (ux has no `review` phase)=8. All 3 receiving agents' head clauses are generic, per-lens bullets illustrative only | ✅ pass |
| AC-3.1 | Read `lenses/README.md:128-140` | "Adding a lens" step 4 rewritten, `act` exception stated honestly | Step 4 now enumerates `specify`,`design`,`review`,`qa` as generic and explicitly excepts `act`: "`/increment` dispatches no lens files at all"; independently confirmed `grep -in lens skills/increment/SKILL.md` = 0 matches | ✅ pass |
| AC-3.2 | Read `README.md:321` | States gap closed across 8 sites, names the 2 residual stale docs | Line 321: "the add-a-file guarantee... has since been closed across all eight resolved-instruction sites... Two prose lens-count copies (`docs/status.md`, `docs/workflow.md`) remain stale... a separate, named documentation-accuracy finding, not a reopened dispatch gap" | ✅ pass |
| NFR-4 | Cross-checked all 9 `lenses/*.md` frontmatter `phases` against the 3 dispatch skills' resolved instruction text | Zero omissions/false inclusions across design/qa/review | design 4, qa 5, review 8 all independently re-derived above match; instructions are rule-based (no enumeration), so no omission is structurally possible | ✅ pass |
| NFR-5 | Read `.spark/constitution.md:43,55` (this repo's own profile); `lenses/library.md:3-4` | Negative case: `library`-only, 0 characteristics → design ∅, qa ∅, review `{library}` | Profile confirmed `library` type, "Characteristics: none of the six"; `library.md phases: [specify, review]` — no `design`/`qa` → design ∅, qa ∅, review={library} exactly as expected | ✅ pass |
| NFR-6 | `git diff main...HEAD --numstat -- ':!.spark'`; `git diff main...HEAD -- templates/spec.md templates/constitution.md`; `claude plugin validate .` | Additive-only, no protected structure renamed, compat holds | 10 files changed (matches review's corrected count); both protected templates' every changed line is inside an HTML comment (headings/columns/`NFR-n` pattern untouched); `claude plugin validate .` → "Validation passed with warnings" (1 pre-existing, unrelated `autoUpdate` warning) | ✅ pass |

## 3. Exploratory Findings

Beyond the ACs: grepped for stray hardcoded lens-name enumerations across `skills/`, `agents/`, `templates/` not already named in `review.md` (`grep -rn` for adjacent-lens-name patterns) — none found. Confirmed `skills/story-time/SKILL.md:41` and `agents/product-owner.md:74-80` (the `specify`-phase leg review's F1 fix depends on) independently: both pass/apply "any active lens"/"each active lens the caller passed", generic, no name list. Confirmed both disclosed residuals are real and as claimed: `docs/status.md:34` lists exactly 8 checklists (`seo,ux,api,cli,library,security,i18n,data`), omitting `accessibility`; `docs/workflow.md:40-42` likewise omits it — both pre-existing, unrelated to this feature's dispatch mechanism, and correctly routed rather than fixed (spec §6, out of scope).

No bugs found. No findings table rows.

## 4. Console & Network

N/A — no browser session per constitution §8. `claude plugin validate .` is the closest analogue to a "console"; output clean apart from the pre-existing, unrelated `autoUpdate` warning (confirmed present before this feature via `plan.md`'s own T-series notes, not introduced by this diff).

## 5. Verdict

Ship it. Every Must AC (US-1: AC-1.1–1.4, US-2: AC-2.1–2.4, US-3: AC-3.1–3.2) and every QA-owned NFR (NFR-4, NFR-5, NFR-6) was independently re-derived from the current file contents and real command output on `feat/lens-dispatch-registry` — never cited forward from `evidence.md` or `review.md`'s word alone, per this project's re-derivation rule for Must ACs. All eight resolved-instruction sites read as generic, computed-set rules with zero hardcoded lens-name lists remaining; the two folded-in sites (`skills/spark/SKILL.md`, `templates/spec.md`) read the same way. The one honestly-disclosed non-generic case (`act`, zero dispatchers) re-confirmed by direct grep at 0 matches. The two disclosed stale prose residuals (`docs/status.md:34`, `docs/workflow.md:40-42`) are real, out of scope by spec §6, and correctly not treated as failing ACs. Both protected templates (`templates/spec.md`, `templates/constitution.md`) diff comment-only against `main`. `claude plugin validate .` passes. Positive-firing case remains `not-verified-live` by design (spec A2) — no venue in this repo, not a gap I could force closed. I would demo this without hesitation.

---

## ✅ QA GATE

- [x] Every Must-story acceptance criterion verified by the declared substitute method and passed
- [x] Every QA-owned NFR verified and passed
- [x] No open Blocker or Major bugs (none found)
- [x] N/A: browser console — no browser-observable surface (constitution §8); `claude plugin validate .` clean apart from 1 pre-existing, unrelated warning
- [x] N/A: viewports — no browser-observable surface (constitution §8)
- [x] Line budget respected: Ist 78 / Soll ~130 (excluding HTML comments)
- [x] Status set to `passed`

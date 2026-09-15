# QA Report: accessibility-lens

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | `.spark/accessibility-lens/spec.md`, `plan.md`, `evidence.md`, `review.md` (round 2, `passed`) |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-09-15 |

**Handoff**
- **Status:** `passed`.
- **Verdict:** Yes — the deliverable is a correctly-structured, correctly-suppressed lens file, and its one known limitation (dispatch/activation gap, NFR-6) is disclosed honestly in the README and ledger rather than hidden. Demo-able as-is.
- **Open:** `none` — no Blocker, no Major. NFR-6 is a by-design `refuted-with-finding` (this project's own house rule names that a valid outcome), already routed to a follow-up increment; not a QA-opened bug.
- **Binding ruling:** §5 Verdict and the gate checklist below.
- **On conflict:** the numbered body below wins for everything except `Status`.

**QA method for this project (constitution §8):** aSPARK Core declares `Browser-observable surface: no` and names a substitute — hands-on QA against the installed plugin, where a performed step is a real command whose output was observed or a real file read with its text quoted, never reasoning about what a file "would" do. No browser or app URL was needed or requested. Every row below was independently re-performed by me this round — commands re-run, files re-read, quotes re-pulled from current source — not copied from `evidence.md`/`review.md`.

## 1. Test Environment

- **App URL:** N/A — no browser-observable surface (constitution §8).
- **Browser / viewport(s):** N/A.
- **Test data / accounts used:** N/A.
- **Substitute method used:** commands run in `/Users/andreaslottes/aSPARK` on branch `docs/accessibility-lens` (`git status --porcelain`, `git diff --name-only main [-- <paths>]`, `grep`, `claude plugin validate .`) plus direct reads of `lenses/accessibility.md`, `lenses/README.md`, `lenses/seo.md`, `lenses/ux.md`, `README.md`, `.spark/constitution.md`, `agents/facilitator.md`, `templates/constitution.md`, `skills/look-and-feel/SKILL.md`, `skills/demo-day/SKILL.md`, `skills/peer-review/SKILL.md`.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Read `lenses/accessibility.md:1-5` | `name: accessibility`, `triggers: [must-be-accessible]`, `applies-to` absent, `phases: [specify, design, act, review, qa]` | Exactly that; matches `lenses/security.md`'s key shape | ✅ pass |
| AC-1.2 | `grep -ni "must-be-accessible" .spark/constitution.md`; read §2 *Active lenses* table | Zero match; lens absent from active-lens table | Exit 1 (no match); active-lens table shows only `library` — Active; §2 states "Characteristics: none of the six" | ✅ pass |
| AC-1.3 | Read `lenses/README.md:47-49` (bullet), `:92` (characteristics table), `:106` (available-lenses table) | `accessibility`/`must-be-accessible` present in all three, same format as `security`/`i18n`/`data` rows | Confirmed at all three locations verbatim | ✅ pass |
| AC-1.4 | `git diff --name-only main` (full) and `git diff --name-only main -- skills/ agents/ templates/ .claude-plugin/` | "No agent/skill file edited" clause holds; "touches only 4 files" superseded per Q1 ruling (README added) | Full diff = `README.md`, `lenses/README.md`, `lenses/seo.md`, `lenses/ux.md` (+ untracked `lenses/accessibility.md`, `.spark/accessibility-lens/`); protected-path diff = empty | ✅ pass (ruled — Q1 honored, README's 5th-file edit is deliberate per constitution §4) |
| AC-2.1 | Read `lenses/accessibility.md:43-49` (§1) | Specify section beats the template's generic "WCAG 2.1 AA" with a named flow requirement + numeric contrast target, plus a conscious-N/A escape | "names the actual flow(s)... and a numeric contrast target (4.5:1 body text, 3:1 large text)... not the spec template's generic 'WCAG 2.1 AA' example restated verbatim"; N/A escape bullet present | ✅ pass |
| AC-2.2 | Read `lenses/accessibility.md:51-60` (§2) side by side with `agents/designer.md` §3 | Contrast/focus/target-size cited once, not restated; `prefers-reduced-motion` cited to `ux` once or owned outright | "cited to `agents/designer.md` §3's baseline once — not restated as new findings"; motion bullet cites `lenses/ux.md`'s check once, owns it when `ux` inactive | ✅ pass |
| AC-2.3 | Read `lenses/accessibility.md:62-75` (§3); `skills/increment/SKILL.md:26-27` | Semantic HTML, labelled controls, ARIA-as-fallback, live-region announcements; realized via NFR/plan traceability, no lens-specific `/increment` step | All four present; §3's last bullet states "no lens-specific step exists in `/increment` itself"; `increment/SKILL.md:26-27` reads spec §4/§5 unconditionally, confirmed unchanged | ✅ pass |
| AC-2.4 | Read `lenses/accessibility.md:77-86` (§4) | Keyboard traps + focus management on route/modal changes; explicit statement that semantic/ARIA correctness is not re-checked here | Both bullets present; third bullet: "Semantic markup and ARIA correctness (Act, above) are **not** re-checked here... a deliberately narrower Review remit" | ✅ pass |
| AC-2.5 | Read `lenses/accessibility.md:87-94` (§5) | Exactly 3 bullets: keyboard-only pass-per-AC, measured contrast for ≥1 borderline pair, live-region confirmation | Exactly 3 bullets present, 1:1 with the AC's three clauses (no 4th zoom/reflow bullet — F5's fix confirmed) | ✅ pass |
| AC-3.1 | `grep -n accessibility lenses/seo.md lenses/ux.md` | Both pointer phrases replaced with a named path to `lenses/accessibility.md` | `seo.md:54`: "...doubles as `lenses/accessibility.md`'s check..."; `ux.md:59`: same pattern | ✅ pass |
| AC-3.2 | `git diff --stat main -- lenses/seo.md lenses/ux.md` and full diff text | Exactly 1 changed line per file, no other checklist item touched | Diff shows exactly 1 line changed in each file; `seo.md:76` and `ux.md:71-72` unchanged, confirmed by reading the diff in full | ✅ pass |
| NFR-1 | Read `lenses/accessibility.md` whole file | Valid frontmatter, per-phase owner map, only falsifiable checks | Frontmatter valid; *Who owns what* table has 5 rows; every checklist item is a checkable claim | ✅ pass |
| NFR-2 | Cross-check frontmatter `phases` list against the file's 5 `###` headings | 5/5 mapping both directions | `phases: [specify, design, act, review, qa]` ↔ sections 1–5 headings tagged `(Specify — Product Owner)` … `(QA — QA Tester)`, one each, no gaps, no extras | ✅ pass |
| NFR-3 | `evidence.md` T9's claim re-derived: `grep must-be-accessible .spark/constitution.md` after registration (T5) landed | Registration in `lenses/README.md` alone does not activate the lens | No match (same result as AC-1.2) — registration confirmed to not equal activation | ✅ pass |
| NFR-4 | Same negative-case commands as AC-1.2, on this repo's own `library` profile | Zero accessibility checks/findings/NFRs contributed | Zero — confirmed by the same grep and the active-lens table read | ✅ pass |
| NFR-5 | `git diff main -- lenses/seo.md lenses/ux.md README.md lenses/README.md`; `git diff --name-only main -- .claude-plugin/` | Purely additive; no command/heading/column/ID renamed or removed; `plugin.json` untouched | Full diffs read: every changed hunk is either a 1-line pointer swap or a pure addition (new table rows, one qualifying clause appended, never rewritten); `.claude-plugin/` diff empty | ✅ pass |
| NFR-6 | Re-read all 5 dispatch/activation sites at their cited `file:line`s (below) | Consequence honestly stated: two of five phase rows ship undispatched, the characteristic itself not offered by `/charter`'s closed vocabulary | Confirmed live, unchanged since round 2 — see §3 below | ❌ `refuted-with-finding` (by design, per `CLAUDE.md`'s routing ceremony — not a QA-opened defect; correctly routed and disclosed, see §3) |
| NFR-Provability | Read `README.md:302`, `evidence.md` | Positive-firing half honestly recorded `not-verified-live`, no venue on this repo | Confirmed — this repo declares no `must-be-accessible` characteristic and has no browser surface; nothing here could exercise the positive case | `not-verified-live` (as declared — not a failure) |
| NFR-Accessibility | Spec §5 | N/A — feature ships no UI of its own | Confirmed — `lenses/accessibility.md` is prompt material, no rendered surface | N/A |
| NFR-Performance | Spec §5 | N/A — lenses are prompt-time context | Confirmed | N/A |

## 3. Exploratory Findings

No new defects found. Independent re-verification of this feature's own central claim — the five dispatch/activation sites — confirms **no drift since review round 2 closed**; all five read exactly as `evidence.md`/`review.md` quote them:

| Site | Confirmed at | Quote still accurate? |
|---|---|---|
| `skills/look-and-feel/SKILL.md:34-35` | read live | Yes — closed list `ux`, `seo`, `i18n`; `accessibility` absent |
| `skills/demo-day/SKILL.md:84` | read live | Yes — closed list `ux.md`, `seo.md`, `security.md`, `i18n.md`; `accessibility.md` absent |
| `skills/peer-review/SKILL.md:50-51` | read live | Yes — generic `<name>.md` head clause, but the parenthetical membership list (7 names) is closed and doesn't include `accessibility` |
| `agents/facilitator.md:51-52,67-69` | read live | Yes — six-characteristic closed list at 51-52 (matches `evidence.md`'s corrected F9 range exactly); three-lens mapping stops at `security`/`i18n`/`data` at 67-69 |
| `templates/constitution.md:27-28,35` | read live | Yes — shipped template still enumerates the same six characteristics, `must-be-accessible` absent |

Also confirmed, not new: `.spark/.guard/ledger.jsonl`/`trail.jsonl` are still present and untracked (already recorded as review's Open Question 1, unrelated to this feature — out of scope here too); `.spark/constitution.md:16`'s "8 lenses" count is still stale (already known, routed to `/charter` per plan Q3, untouched by this diff as expected). Both Markdown anchors checked resolve: `lenses/README.md`'s `../.spark/accessibility-lens/evidence.md` and both `README.md:302` ledger links (`.spark/situational-lenses/evidence.md`, `.spark/accessibility-lens/evidence.md`) all point at files that exist.

Fresh read of `lenses/accessibility.md` end to end, unprimed: reads as a coherent, usable lens — the *Who owns what* table maps 1:1 to the five `###` sections, the "flags, never invents scope" discipline is applied consistently, and the Review section's explicit "ARIA correctness is not re-checked here" line is a genuinely useful piece of honesty rather than a hedge. `README.md:302` and `lenses/README.md`'s "Adding a lens" §4 qualifying clause both read as "complete but not yet fully wired," not oversold ("shipped, fully working") and not so hedged the lens looks broken — both name exactly which two skills and which two `/charter` sites need a hand-edit today.

`claude plugin validate .`: `✔ Validation passed with warnings` (one pre-existing `autoUpdate` warning on `marketplace.json`, unrelated to this diff).

## 4. Console & Network

N/A — no browser instrument exists under the declared substitute method (constitution §8); there is no runtime console or network traffic to observe for Markdown/prompt material. The analogous check performed instead was `claude plugin validate .` (§3), which is clean apart from the pre-existing, unrelated warning.

## 5. Verdict

Yes, I'd demo this. The lens file is well-formed, correctly cross-referenced, cited nowhere it shouldn't be, and stays silent on this repo's own profile exactly as promised — I re-ran the negative case myself rather than trusting the ledger. Its one real limitation, NFR-6's dispatch-and-activation gap at five sites, is not a surprise I'm uncovering — it's this feature's own declared, by-design `refuted-with-finding` outcome (this project's `CLAUDE.md` names that a legitimate result, not a failure to grind past), and what I verified independently is that the disclosure is accurate and current: the same five `file:line`s quoted in `evidence.md` and `review.md` still read exactly that way today, and a reader hitting `README.md:302` or `lenses/README.md`'s "Adding a lens" section gets an honest, correctly-scoped account rather than an oversold or over-hedged one. Nothing I checked — frontmatter, phase mapping, pointer edits, fence, `plugin validate`, or the five dispatch quotes — disagreed with what two rounds of review already established; my job here was independent confirmation, not rediscovery, and it holds up.

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run
`/demo-day`. On re-test, edit this same checklist in place — never duplicate it as a second gate.*

- [x] Every Must-story acceptance criterion verified (by the declared substitute method) and passed — AC-1.1–AC-1.4, AC-2.1–AC-2.5 all ✅; AC-1.4's file-list clause is a recorded, ruled supersession (Q1), not a fail
- [x] Every declared-method-observable NFR verified and passed, or honestly recorded otherwise — NFR-1–5 ✅; NFR-6 `refuted-with-finding` by design (accepted outcome, routed); NFR-Provability `not-verified-live` as declared; NFR-Accessibility/Performance N/A per spec
- [x] No open Blocker or Major bugs (Minor bugs listed and accepted by the user) — none found this round
- [x] Browser console free of errors on the tested flows — N/A, no browser surface (§8); substitute check (`plugin validate`) clean
- [x] Tested on all agreed viewports — N/A, no browser surface (§8)
- [x] Line budget respected: Ist 100 / Soll ~130 (excluding HTML comments)
- [x] Status set to `passed`

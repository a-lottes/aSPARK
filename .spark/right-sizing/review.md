# Review Report: right-sizing

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | `git diff c03e643..04f6cab` (8 files) over the full feature diff `085db99..04f6cab` (16 files), `.spark/right-sizing/plan.md` |
| **Status** | `passed` |
| **Round** | 5 |
| **Date** | 2026-08-31 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** round 5's §6 supersedes round 4's. **`F17` is genuinely closed, not closed in form**
  — all four propagated files carry the action-based guarantee, each scoped to its own ceremony,
  with zero remnants of "say nothing / no mention" anywhere in the shipped surface. `F18`/`F19`
  are fixed and the diff is scoped as `evidence.md` Entry 15 §15.4 claims. The plan's own revision
  (`R1`) is internally consistent.
- **Open:** `5 open` — Blockers: `none`; Majors: `none`. Minors/Nits: F10 (user-accepted as open
  since r3), F20, F21, F22 (all unchanged from r4), **F23** (new, Minor — `/demo-day` r8 owes a
  re-test of the STOP branch). 18 findings closed; **`F17`/`F18`/`F19` confirmed `fixed r5`.**
- **What round 8 of `/demo-day` owes:** re-run the B5 scenario against `agents/qa-tester.md:45-55`'s
  *new* wording — `qa.md` r7's Run 1 evidence was gathered against text this round replaced (F23).
  The four propagated files stay `not-verified-live` and that limit must survive into `/go-live`'s
  release notes and the README maturity row.
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Re-review, round 5, at `04f6cab` (working tree clean). Reviewed: the eight-file delta since r4,
plus — read fresh, not cited from r4 — all four propagated files in full surrounding context,
`agents/qa-tester.md:36-130` end to end, `plan.md` end to end, `evidence.md` Entry 15,
`templates/constitution.md:103-125`. **Not reviewed:** live agent behaviour — I do not re-run
`/demo-day`; I check whether the shipped text supports what the evidence reports.

**Re-derivation (AC-2.2, per AC-2.3).** **(a)** F17/F18/F19 — confirming claimed fixes; each of
the five files read at source, not grepped for the phrase's absence. **(b)** AC-1.3/NFR-4 —
Must-AC verification, re-read against `spec.md:119`/`:149`'s `C19` text, traced into all five
readers. **(d)** Entry 15 §15.4's diff-scope claim and §15.5's gate table — a self-report about
the file r4 warned must not move, so checked against `git diff` and a fresh gate-item grep.
**(d)** NFR-6 — re-derived. Everything else (F1–F16, F20–F22, AC-1.1/1.2/1.4–1.10, AC-2.x,
NFR-1/2/5) is **cited from r2/r3/r4**; `qa.md` and `spec.md` are byte-unchanged since r4, so no
condition fires on them. Facts re-derived without a named condition: **0**.

**Tool (`aspark-graph`, runner=yes / graph=yes), review slice.** Resolved once after the gate
check: CLI on `PATH` + `graph.json` present. `staleness` → `files_checked: 0` (nothing indexed,
not "fresh"). `impact --diff c03e643..04f6cab` → `files: []`, **all eight paths in
`unknown_files`** = *"I do not index these"*, **not** an all-clear. `story_trace US-1` →
`{"found": false, "reason": "not_found"}`. All three are structural empties per the tool file's
own `unknown_files` rule, so **no tool result scoped any reading**: every location below was
found by hand (`grep -rn` over `agents/ skills/ templates/ lenses/ tools/ README.md`) and read.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | `templates/constitution.md:105-125`; unchanged since r4 and carries no content-suppression claim of its own — checked, since it is the file that ships into every consumer |
| T2 | ✅ **r5** | DoD re-worded to `C19`'s action bar (`plan.md:57`); `skills/demo-day/SKILL.md:31-40` now matches the corrected criterion. r4's ⚠️ discharged |
| T10 | ✅ **r5** | `skills/spark/SKILL.md:73-84`, both branches; the absent/`yes` branch now carries the block |
| T3 | ✅ **r5** | `agents/qa-tester.md:42-122`; F18/F19 fixed inside it without moving the live-proven block |
| T4 | ✅ **r5** | `go-live:33-43` + `release-manager.md:63-80`; citation form and the `qa.md`-`passed` requirement intact, absent-case clauses re-scoped |
| T5, T6, T7 | ✅ | Unchanged since r4 |
| T8 | ✅ **r5** | DoD re-worded to the action bar (`plan.md:64`); T14 re-judged its recorded observations against it (Entry 15 §15.1) |
| T9 | ✅ | Unchanged since r4 |
| T11 | ✅ | `demo-day:31-40`, `spark:77-84`. DoD's grep (`say nothing\|no mention`) → zero hits, re-run by me across the whole shipped surface. Both carry all three parts, scoped to a live conversational branch. `demo-day`'s four outcomes, browser STOP and `/charter`-only clause are byte-identical (`git diff` shows no other changed line) |
| T12 | ✅ | `go-live:37-42`, `release-manager.md:72-80`; both re-scoped to *row wording*, not to a conversational ask — the scoping distinction T11 vs T12 is real and correct. Gate-item grep over both → empty |
| T13 | ⚠️ **r5** | Both corrections land and are right (F18/F19 `fixed r5`), but **not where the DoD says**: T13 specified F18's fix as a reword *at `:50-52`*; the shipped fix deletes the false sentence and states the true routing at `:62-65` instead. Better placement, undocumented deviation. The DoD's "touches those two clauses only" is also slightly over-tight — a third, clarifying sentence (`:50-53`) was added. Fences held: fraud rule, B5 do-not-suggest rule, three-part block and incomplete/unperformable branches all byte-unchanged (verified against `git diff`, not against the claim) |
| T14 | ✅ | `evidence.md` Entry 15. Every DoD element present and, where checkable, true: §15.1 re-judgement, §15.2 dry run, §15.3 the venue limit stated once, §15.5 gate table re-run. I re-derived the gate half independently (§4, NFR-6) and it holds |
| D1, D2 | ✅ accepted | Unchanged from r3/r4 |
| R1 | ✅ | Plan revision is internally consistent: Handoff (`:12`, `:14`) agrees with §3's status column (all 14 `done`), with §1's "four more (T11–T14) were appended" and with the PLAN GATE's approval line (`:111`). Two rejected alternatives were added for the revision itself. One stale clause — **F23**'s sibling, filed as **F24** |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `templates/constitution.md:111` | Contract comment said `/go-live` "behaves exactly as today" while the same diff changed it. Fixed at `:112-118` | fixed r2 |
| F2 | Major | `skills/demo-day/SKILL.md:98` | `## Rules` rejected the report its own step 1 authorises. Fixed at `:99-104` | fixed r2 |
| F3 | Major | `plan.md:72`, `evidence.md` §4.5 | Round 1 ran the installed `0.7.0`, so nothing in the diff had executed. Fixed: `0.7.1` installed at `47f6040` | fixed r2 |
| F4 | Minor | `agents/qa-tester.md` (r2 `:46-50`/`:61-65`) | Declared branch entered only on a complete §8 yet held an incomplete-case sub-bullet. Fixed: entry condition widened | fixed r2 |
| F5 | Minor | `skills/demo-day/SKILL.md:42`/`:81-83` | Step 1 promised to pass the method; step 2 enumerated URL/viewports only. Fixed | fixed r2 |
| F6 | Minor | `agents/release-manager.md:73-75` | Only §8 reader that never stated AC-1.10. Fixed: read-only clause added | fixed r2 |
| F7 | Minor | `README.md:251` | Status row claimed dogfooding the declared path had not run. Fixed | fixed r2 |
| F8 | Minor | `agents/qa-tester.md` (r2 `:26`, `:111-112`, `:140-148`) | Agent unconditionally browser-bound outside step 1. Fixed in all three places | fixed r2 |
| F9 | Nit | `spec.md:149` vs `skills/charter/SKILL.md:45-53` | NFR-4 did not exempt `/charter`, which asks one more question on every project. Resolved by spec amendment C17 | fixed r4 |
| F10 | Nit | `demo-day:28`, `qa-tester:55`, `go-live:33`, `spark:74`, `release-manager:65` | §8 addressed by number in five shipped files; a consumer numbering differently makes the reference wrong. All five also name `QA Method`. Fix: lead with the name, number parenthetical. **Open by the user's explicit decision, not oversight** | open |
| F11 | Nit | `agents/facilitator.md:76-83` | Paragraph mis-indented inside a list item. Reviewer re-indented | fixed r1 |
| F12 | Major | `agents/facilitator.md`, `agents/qa-tester.md` | Both claimed `/go-live` was the declaration's only other reader; `/spark` reads it too. Fixed in both | fixed r3 |
| F13 | Nit | `skills/demo-day/SKILL.md:55` | "both gates above" predated the §8 read becoming a third sub-step. Reviewer fixed | fixed r2 |
| F14 | Nit | `evidence.md:518` | Entry 6 recorded `47f6040` as 12 files; actual 15. Reviewer corrected | fixed r2 |
| F15 | Minor | `templates/constitution.md:110-118` | Contract comment gave `/go-live` its difference and never `/spark`'s. Fixed at `:115-118` | fixed r4 |
| F16 | Minor | `evidence.md` §7.1 | Concluded "AC-1.1 performed" when only its `/spark` half had run. Fixed at `:578-583` | fixed r4 |
| F17 | Major | `demo-day:31-40`, `spark:77-84`, `release-manager:72-80`, `go-live:37-42` | `C19` re-scoped AC-1.3/NFR-4 to an action rule; only `qa-tester.md` had been changed, leaving four files shipping the retired "say nothing / no mention" guarantee and contradicting `qa-tester.md:74-79`. **r5, re-derived under AC-2.2(a)+(b), read not grepped:** all four now carry the three-part block (Never ask/error/warn/re-negotiate — Fine to state in own words — Discouraged verbatim quoting, capped Minor), each correctly scoped: a live conversational branch in `demo-day`/`spark`, an artifact-row-wording rule in `go-live`/`release-manager` ("in the row or in the reply"). `grep -rn "say nothing\|no mention\|nothing more"` over `agents/ skills/ templates/ lenses/ tools/ README.md` returns **no hit about the declaration** (the nine remaining hits are the `aspark-graph` tool rule, `/go-live`'s pre-existing release-mode clause and unrelated README prose — each checked). Plan root cause fixed too (T2/T8 DoD, `R1`) | **fixed r5** |
| F18 | Minor | `agents/qa-tester.md` (r4 `:50-52`) | "If a declaration already exists and is complete, you would not have reached this branch at all" was false for a complete `surface: yes` declaration. **r5, re-derived under AC-2.2(a):** false sentence deleted; `:62-65` now states the true routing ("A complete `Browser-observable surface: yes` declaration routes here too… the STOP branch above applies to it exactly as it would to an undeclared project"), which matches `:56-61`'s own routing and `qa.md:73`'s live Runs 4–5. Placement differs from T13's DoD — see §2 | **fixed r5** |
| F19 | Minor | `agents/qa-tester.md:45-53` | STOP branch said "nothing more" (content suppression) while `:74-79` says stating the fact is "fine, not a violation". **r5, re-derived under AC-2.2(a):** now "name the missing tool or URL, and add no other options for unblocking yourself", plus an explicit reconciliation at `:50-53` ("a rule about what you may not *offer*, not about staying silent"). The B5 do-not-suggest rule survives verbatim in substance at `:46-49` | **fixed r5** |
| F20 | Nit | `evidence.md:994-997` | Entry 14 calls the STOP-branch fix "a third distinct location… carrying a C19-shaped constraint" and its parenthetical names only two. Unchanged this round. Capped Minor by AC-2.4. Fix: say "second", or name the third (`qa-tester.md:84-87`) | open |
| F21 | Nit | `spec.md:227` vs `:12` and `:255` | C18's resolution cell still reads "not yet re-approved" while the Handoff and SPEC GATE both record it re-approved 2026-08-31. `spec.md` is byte-unchanged since `c03e643`; **still stands exactly as filed.** Capped Minor by AC-2.4. Fix: "re-approved at the `/story-time` gate of 2026-08-31, later superseded by C19" | open |
| F22 | Nit | `spec.md:254` | SPEC GATE reports "Ist 253 / Soll ~250"; file is 255 lines with 4 HTML-comment lines (`:105-107`, `:232`) → Ist **251**. Re-counted this round: unchanged, still over-reports its own overage (so the "recorded not waived" branch is unaffected). Capped Minor by AC-2.4. Fix: 251 | open |
| F23 | Minor | `agents/qa-tester.md:45-55` vs `.spark/right-sizing/qa.md:71` (Run 1) | T13 edited the STOP branch **after** `qa.md` r7 certified it; r7's Run 1 (the B5 reproduction) is evidence about text this round replaced, and its cited fix string at `:46-47` no longer reads as quoted. Entry 15 §15.3 discloses this honestly but does not close it, and unlike the four skill files **this one is closable here** — `qa-tester.md` is invocable directly as a sub-agent, which is exactly how all seven rounds ran. Why it matters: it is the only live venue this feature has, and the change relaxes a content constraint in the branch B1/B4/B5 all came from. Mitigating (my own reading of `qa.md:71`, not Entry 15's): Runs 2–3 already *stated the fact in their own words* under the stricter text and were passed under `C19`, and the forbidden act stays forbidden verbatim — so the untested delta's worst case is a behaviour `C19` explicitly permits. Fix: `/demo-day` round 8 re-runs Run 1's scenario (Venue A, ordinary + narration-demanding) against the new wording; no new matrix needed | open |
| F24 | Nit | `plan.md:121` (R1), and `:9` | R1's closing sentence still reads "the new tasks stay `todo` for `/increment`" while §3 shows T11–T14 `done`; the header `Date` row still reads `2026-08-29` for a file revised 2026-08-31 (the Handoff carries the revision date, so nothing is lost). True when `/sprint-plan` wrote it, stale now — the Handoff-vs-body class Entry 11 keeps finding. Capped Minor by AC-2.4: no verdict, gate answer or Must AC turns on it. Fix: "…stayed `todo` for `/increment`, which completed them the same day" | open |
| F25 | Nit | `evidence.md:1115` | §15.5 says `before` was "measured against `22673c8` (the commit round 4's review was written against)". Round 4 was written against **`c03e643`**; `22673c8` was the *base* of its diff. The baseline chosen is fine (wider); only the label is wrong. Capped Minor by AC-2.4. Fix: name `22673c8` as the base of round 4's diff range | open |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `demo-day:47-49`, `spark:73-77`, `qa-tester:99-101` | ✅ met — cited locations re-anchored r5 (the propagation shifted `qa-tester` by +5) |
| AC-1.2 | `demo-day:50-52`, `qa-tester:106-108`, `templates/constitution.md:106-108` | ✅ met |
| AC-1.3 | `qa-tester:45-55` + `:62-87`; `demo-day:31-40`, `spark:77-84`, `go-live:37-42`, `release-manager:72-80` | ✅ **met r5** — re-derived under AC-2.2(a)+(b). All five readers now state the same action-based bar; the agent half is live-evidenced 5/5 (`qa.md:71`), the other four are `not-verified-live` and say so (Entry 15 §15.3, F23) |
| AC-1.4 | `go-live:33-36`, `release-manager.md:63-71` | ✅ met |
| AC-1.5 | `qa-tester:56-65`, `demo-day:31-40`, `templates/constitution.md:121-122` | ✅ met — strengthened this round: `qa-tester:62-65` now states the `yes`-surface routing explicitly instead of denying it (F18) |
| AC-1.6 | `demo-day:44-46`, `qa-tester:96-98` | ✅ met |
| AC-1.7 | `templates/constitution.md:109-118`, `facilitator.md:117-122`, `qa-tester:117-122` | ✅ met |
| AC-1.8 | `charter:45-53`, `facilitator:112-118`; `.spark/constitution.md` Amendments row | ✅ met |
| AC-1.9 | `demo-day:41-43`, `spark:77`, `qa-tester:91-95`, `go-live:37` | ✅ met |
| AC-1.10 | `qa-tester:120-122`, `demo-day:52-54`, `go-live:42-43`, `spark:83-84`, `facilitator:112-114`, `charter:52-53`, `release-manager:78-80` | ✅ met — all seven survived the propagation, re-checked |
| AC-2.1–2.3 | `reviewer.md:171-181`, `qa-tester.md:231-241` | ✅ met |
| AC-2.4 | `reviewer.md:182-186`, `qa-tester.md:242-246` | ✅ met |
| AC-2.5 | no age/shape instruction anywhere in `085db99..04f6cab` | ✅ met |
| NFR-1 | `templates/constitution.md` +28/−0; `git diff --stat 22673c8..04f6cab -- templates/` → **empty** | ✅ met |
| NFR-2 | `git diff --stat 085db99..04f6cab`: 16 files, and `--diff-filter=A` adds **only `.spark/` artifacts** — no new skill, agent, lens, template or dependency | ✅ met — line-by-line release-note enumeration is still `/go-live`'s to deliver |
| NFR-3 | `templates/constitution.md:105-125` + the per-file blocks | ✅ **met r5** — the contract now answers "what may this phase say?" the *same* way in all five readers (F17), and `qa-tester:62-65` no longer states a false precondition (F18) |
| NFR-4 | The absent/incomplete branch in all five readers | ✅ **met r5** — re-derived under AC-2.2(b). Same action bar everywhere; held 5/5 live where a venue exists |
| NFR-5 | `README.md:96`, `:251`; no line/token/dollar or generalization claim in `085db99..04f6cab` | ✅ met — `README.md` byte-unchanged since `47f6040`; release-notes half falls to `/go-live` |
| NFR-6 | `git diff 085db99..04f6cab -- templates/ skills/ agents/ README.md \| grep -E "^[+-]\s*- \[[ x]\]"` → **empty** | ✅ met — re-derived, not cited: not one gate-item line added, removed or reworded across the whole feature |

## 5. What Was Checked

- [x] Correctness: all four propagated blocks read in full context at source (not grepped for a
  phrase's absence) and judged against `spec.md:119`/`:149`'s `C19` text, per ceremony
- [x] Predecessor claim, verified not cited: Entry 15 §15.4's "exactly two locations, nothing else
  in that file" checked against `git diff c03e643..04f6cab -- agents/qa-tester.md` — **true** (one
  hunk; block, fraud rule, B5 rule, three sub-branches byte-unchanged). §15.5's gate table
  re-derived independently — holds
- [x] Plan self-consistency (Entry 11's class): `plan.md` Handoff vs §3 status column vs `R1` vs
  the PLAN GATE — agree, with one stale clause (F24)
- [x] Non-functional: NFR-1…6 re-checked; library lens **§1** (no new export/file — `--diff-filter=A`
  adds only `.spark/` artifacts), **§2** (additive only, no removed/renamed/tightened surface, no
  gate item moved, `plugin.json` still `0.7.1` for `/go-live` to bump), **§4** (contract clarity —
  where F17/F18 landed, now closed). §3 N/A per constitution §2
- [x] Edge cases: the `yes`-surface + complete-declaration venue (now stated, F18); the STOP branch
  (F19); incomplete/unperformable branches (byte-unchanged); `/spark:69-72`'s ordinary
  QA-prerequisite ask vs `:78`'s "never ask" — **not** a contradiction, `C19` question 3
  explicitly excludes today's default ask
- [x] Error handling / security: all four fall-backs still resolve toward more verification.
  Security N/A per constitution §2/§5; nothing private added
- [x] Tests: `claude plugin validate` → passed (1 pre-existing `autoUpdate` warning, outside the
  diff). No suite exists or is possible (constitution §4)
- [x] Venue: `diff -rq` over `agents/ skills/ templates/ lenses/ tools/` vs the `0.7.1` cache →
  **zero differences** — this review ran under the propagated text, not a stale copy

## 6. Verdict

**`passed`.** `F17` is closed on substance, not on form. I read all four files fresh rather than
grepping for the retired phrase, and the replacement is the right shape in each: the same
Never / Fine / Discouraged triple, but scoped honestly — `demo-day` and `spark` govern a live
conversational branch ("stating in your own words… in your reply"), `go-live` and
`release-manager` govern a row in an artifact ("naming, in the row or in the reply"). That
distinction is the thing a careless propagation would have flattened, and it wasn't. The one
contradiction that made `F17` Major — `demo-day:33` ordering silence while `qa-tester` said
"you are not required to suppress this" — is gone, and the plan's own root cause went with it:
T2/T8's Definition of Done now names the action bar, so the retired wording can't be
re-certified next round. `F18` and `F19` are fixed, and Entry 15 §15.4's diff-scope claim
survives being checked against the diff instead of being taken on trust: the three-part block,
the fraud rule, the B5 do-not-suggest rule and the three sub-branches are byte-unchanged.

**On the honesty limit — my own call, not Entry 15's.** Shipping the four propagated files with
the limit stated is right, and I would not route this back to `/increment` for it. Not because
the disclosure is well written, but because the change *relaxes* a constraint in the safe
direction: the old text said "say nothing", silence already satisfied an action rule, so nothing
compliant becomes non-compliant. The only new permission is "state the fact in your own words",
which `C19` declares explicitly not a violation — the untested delta's worst case is a permitted
behaviour, and the forbidden act stays forbidden verbatim in all five files. The obstacle is also
environmental (`claude -p` OAuth, reproduced in all seven rounds), not a defect of this change: a
gate waiting for a venue that cannot exist never opens. **But I split the judgment where Entry 15
leaves it whole.** T13's two clauses are not in that category — they sit in the one file that
*does* have a live venue, in the exact branch B1/B4/B5 came from, and `qa.md` r7's Run 1 now
cites replaced text. That is closable cheaply with the matrix that already exists, and the review
gate hands off to `/demo-day` anyway, so it costs a round already scheduled. Hence **F23, Minor,
aimed at QA rather than back at the developer.** I checked before deciding it doesn't hold the
gate: r7's Runs 2 and 3 already show the agent stating the fact in its own words under the
*stricter* text and being passed for it — exactly the behaviour the new wording legalises.

**What is left is small.** One Minor and four Nits, none changing a verdict, a gate answer or a
Must AC; three (`F20`–`F22`) are unchanged from round 4 and outside this increment's scope. **I
applied no fixes this round** — every open row is either the user's standing decision (`F10`) or
an AC-2.4-capped artifact-wording item belonging to that artifact's owner. No Blocker, no Major,
no constitution non-negotiable violated, gates byte-identical, `validate` green.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] **No open Major findings — `F17` confirmed `fixed r5`**, re-derived at source under AC-2.2(a).
  Nothing was waived; none was needed
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — §6's
  five re-checked: no protected §3 structure renamed, all four fall-backs intact in every reader,
  nothing executed unasked, no gate self-passed, nothing private added. AC-1.3/NFR-4 now trace to
  all five readers (§4)
- [x] **All plan deviations documented and accepted** — `R1` is recorded in `plan.md:121` and
  user-approved at a second plan-gate walk (`plan.md:111`); D1/D2 unchanged and accepted since r3.
  r4's open item (T2/T8's superseded criteria) is discharged. One undocumented micro-deviation in
  T13's fix *placement* is recorded in §2 rather than filed — it changed no task, AC or gate item
- [x] Test suite runs green — none exists (constitution §4); the bar, `claude plugin validate`,
  re-run this round: passed with the 1 pre-existing `autoUpdate` warning
- [x] Line budget respected **on the template's second branch, not the first**: **Ist 216 / Soll
  ~150** (excluding HTML comments — none in this file) — **66 over, recorded not waived.** Cause:
  25 finding rows in a non-appending file. F1–F16 were compressed again to one line each and §1,
  §5 and §6 were trimmed, but three new rows landed, so the file grew by 8. The budget is **not**
  met and I am not claiming it is; the honest fix is a convention for retiring closed rows, which
  is not mine to invent here
- [x] Status set to `passed`

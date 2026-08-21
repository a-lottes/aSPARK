# Review Report: lean-rounds

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The working-tree diff of `/increment`, `.spark/lean-rounds/plan.md` |
| **Status** | `passed` |
| **Round** | 3 |
| **Date** | 2026-08-20 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** Gate `passed` r3. F1–F6 and F8 fixed and each re-verified live against the real consumer; F9 accepted and F10 waived by explicit user ruling, reasons in §3. F7 stays open by design — commit hygiene, no file to fix.
- **Open:** `1 open` — Blockers: `none`; Majors: `none`; Minors/Nits: `F7` (commit-hygiene note, not a code defect; confirmed live as the only `open` row the consumer sees)
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Reviewed: the working-tree diff, **12** modified files (+174/−25) — round 1's 11 plus
`skills/demo-day/SKILL.md` (F1's fix, a recorded plan deviation); round 3 adds only F8's
three lines in `templates/review-report.md`. Nothing committed, added or deleted. Re-read
in full: both agents, both report templates, `skills/{demo-day,peer-review}/SKILL.md`, plus
the untracked trail (`spec.md`, `plan.md`, `evidence.md`) — in scope because F5, F9 and F10
were filed there.

**Verification actually run** (no build, no test suite — constitution §4), re-executed
in full each round rather than carried forward: `claude plugin validate .` → pass, same
single pre-existing `autoUpdate` warning. All parser claims re-run with
`~/aSPARK-graph/.venv/bin/python` against `~/aSPARK-graph/src/aspark_graph/`: (a)
`extract_features` + `queries.gate_health` on fresh fixtures built from the *current*
templates, exercising `accepted`, `fixed r<n>`, `not reproducible r<n>`, bare `fixed`
and `open`; (b) `_parse_qa`/`_parse_review` on the literal current vs. `HEAD` templates;
(c) `_parse_review` on the old accreted `.spark/graph-gates/review.md`; (d) the same on
this report itself. Results in §4. The fixtures use template-style filenames because
`_parse_feature` probes only those — constitution §3 consumer defect 1, re-confirmed
live, unchanged by this feature and not Core's to fix.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Unchanged since round 1; parser walkthrough re-run live and still passes |
| T2 | ✅ | Unchanged; `Spec ID`/`Result`/`^B\d+$` still untouched, re-verified against `HEAD` |
| T3 | ✅ r2 | DoD's "suffix only on change" rule is now stated verbatim at `agents/reviewer.md:118-120` |
| T4 | ✅ r2 | Re-test mode is now reachable: `skills/demo-day/SKILL.md:57-58` mirrors `skills/peer-review/SKILL.md:55-56` word-for-word modulo "re-test"/"re-review" |
| T5 | ✅ | Re-confirmed on live evidence: fix-mode wrote 5 bare `fixed` cells and left `Round` at 1 (§4, AC-1.5) |
| T6 | ✅ | Five checkbox lines still byte-identical modulo Soll (md5 re-run) |
| T7 | ✅ | Five agent sentences still byte-identical modulo gate name (md5 re-run) |
| T8 | ✅ | Evidence Entry 9 records the fix round honestly, including that F7 has no file to fix |
| — | ✅ r3 | Both deviations documented (`plan.md:73-88`) and now accepted: the 12th-file addition on its own merits, the AC-2.5 amendment by the user's explicit ratification of C19 (F10) |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `skills/demo-day/SKILL.md:57-58` | `/demo-day` never pointed the QA Tester at the previous `qa.md`, so `agents/qa-tester.md:45`'s whole re-test mode was unreachable and US-1/US-2/US-3 silently did not apply to `qa.md`. **Fix confirmed r2:** read both skills in full — the new sentence sits inside step 2 (Delegate), after the tool-file paragraph, in the same position and wording as `peer-review:55-56`. A `/demo-day` re-run now passes the pointer, so the trigger fires. | fixed r2 |
| F2 | Minor | `agents/reviewer.md:118-120` | T3's DoD required the "suffix `r<n>` only when the value changed" rule verbatim in `reviewer.md`; only `qa-tester.md` carried it. **Fix confirmed r2:** the rule is now in the overwrite-in-place paragraph and symmetric with `qa-tester.md:63-65`. Dogfooded in §4 below — six unchanged verdicts were left untouched, six changed ones carry `r2`. | fixed r2 |
| F3 | Minor | `templates/qa-report.md:70-71` | The placeholder row offered `accepted` while the vocabulary block above it did not list it. **Fix confirmed r2:** `accepted` is now in the block, within spec §6's permitted "user's own waiver". Verified live, not assumed — a fixture row with `accepted` parses to a Finding node and is correctly excluded from `gate_health`'s `open_findings`. | fixed r2 |
| F4 | Minor | `agents/reviewer.md:102-106`, `agents/qa-tester.md:52-57` | The missing-`Round`-row fallback said "set to the round you're about to write", contradicting AC-1.7/§6's no-migration rule. **Fix confirmed r2:** both agents now say set to exactly `1`, framed as the first write under the convention; the two passages are verbatim identical. Residual, accepted per AC-3.4: on the one legacy accreted artifact the header will read `1` while its body still shows `## Round 3`. | fixed r2 |
| F5 | Minor | `.spark/lean-rounds/spec.md:165-174` | AC-2.5 claimed absolutely "raises no `TemplateDriftError`", which `_parse_qa` disproves. **Fix confirmed r2 on substance:** now "no *new* `TemplateDriftError`", naming the pre-existing `Spec ID` defect. Re-verified live this round: current and `HEAD` `qa-report.md` raise the *identical* error, so "no new drift" is exactly true. Who was allowed to make that edit is a separate finding — F10. | fixed r2 |
| F6 | Nit | `agents/qa-tester.md:55` | A 106-character line in a paragraph wrapped at ~72. **Fix confirmed:** re-checked this round with an `awk length>85` scan over both agent files — no long lines remain. | fixed r1 |
| F7 | Nit | `docs/aSPARK_Enterprise_Architecture_Handbook_v1.0.docx` (untracked) | An unrelated binary sits untracked beside this feature's diff; `git add -A` would sweep it in, against constitution §5's "keep it deliberate". Not a code defect and correctly left open. **Fix:** stage the 12 changed files by path at commit time; handle the handbook separately. | open |
| F8 | Nit | `templates/review-report.md:55-70` | F3 was fixed in `qa-report.md` only, so the two otherwise-parallel vocabulary blocks diverged. **Fix confirmed r3:** the `accepted` entry is present, correctly widened to cover a waived Major, at the block's own 98-column width. Re-verified live through the full `extract_features` → `gate_health` path (a `_parse_review`-only harness returns a false empty because it builds no Feature node): `accepted` ×2 and `fixed r3` drop out, `open` alone is reported. Noted and dismissed: the entry points at §6 Verdict for a waiver's reason while the gate line says "recorded here" — both are in-report, no action. The status cell read `fixed r2` when handed to me; corrected to `r3`, since only the owner names the confirming round (AC-1.5/1.6 — the very rule this feature adds). | fixed r3 |
| F9 | Minor | `.spark/lean-rounds/spec.md:326-335`, `.spark/lean-rounds/plan.md:96-104` | This feature's own SPEC GATE and PLAN GATE carry no line-budget checkbox, and `spec.md` is **335** lines against the ~250 Soll this feature makes binding elsewhere. **User ruling 2026-08-20:** accepted as an explained exception — both gates closed before the budget-checkbox mechanism (T6) existed, so nothing is retrofitted onto an already-closed gate. Not waived as an overage; recorded as not applicable to gates that predate the rule. | accepted |
| F10 | Major | `.spark/lean-rounds/spec.md:165-174` + `:309` (C19) | Fix-mode amended AC-2.5 in a spec whose `Status` is `approved`, and appended its own C19 ruling, where every comparable ruling is the PO's or the user's. **User ruling 2026-08-20:** explicitly ratified — C19's resolution updated to record the user's direct confirmation (not the developer's unilateral note); content stands as amended, re-verified live twice (round 2 and this round) against the real `_parse_qa`. Waived at the gate with reason recorded here and in `spec.md` §7. | accepted |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `templates/review-report.md:60-62`, `qa-report.md:64-66`, `reviewer.md:106-107`, `qa-tester.md:56-57` | ✅ met |
| AC-1.2 | `review-report.md:63-65`, `qa-report.md:67-69`, `reviewer.md:107-109`, `qa-tester.md:57-59` | ✅ met |
| AC-1.3 | `review-report.md:56-59`, `qa-report.md:60-63`; **live r2**: `gate_health` on a fresh fixture returned `open_findings = ['F4','F5']` only — `fixed r2`, `not reproducible r2`, bare `fixed` **and the new `accepted`** all fall out of `queries.py:302`'s exact `== "open"` | ✅ met |
| AC-1.4 | `review-report.md:66-67`, `qa-report.md:70-71`, `reviewer.md:114-115`, `qa-tester.md:65-67` | ✅ met |
| AC-1.5 | `skills/increment/SKILL.md:54-62`; **live r2**: parsing this report's own round-1 state yielded `F1–F6 = 'fixed'` (bare, no suffix) with `Round` still `1` — fix-mode obeyed the rule in a real run, not just in a fixture | ✅ met |
| AC-1.6 | `review-report.md:60-62`, `reviewer.md:112-113`, `qa-tester.md:62-63`; this round's own `fixed` → `fixed r2` transitions are the working proof | ✅ met |
| AC-1.7 | Still no migration code; **live**: `_parse_review` on the old accreted `.spark/graph-gates/review.md` again yields exactly F1–F9. F4's fix removes the "write to an old-shape artifact" tension | ✅ met r2 |
| AC-2.1 | `review-report.md:77-78`, `qa-report.md:47-48`, `reviewer.md:118-120`, `qa-tester.md:63-65` — both owners now carry the rule; this table dogfoods it across three rounds — a suffix only where the verdict moved, every unchanged cell left exactly as it was | ✅ met r2 |
| AC-2.2 | `reviewer.md:119-122`, `qa-tester.md:71-74` | ✅ met |
| AC-2.3 | `review-report.md:38-39,43-44,96-97`, `qa-report.md:36,80,84-85`, `reviewer.md:115-119`, `qa-tester.md:67-71` | ✅ met |
| AC-2.4 | `review-report.md:9`, `qa-report.md:9` + single-Scope/Verdict/gate statements in both | ✅ met |
| AC-2.5 | **Live r2**: current and `HEAD` `qa-report.md` raise the *same* `TemplateDriftError` (`missing an 'AC' column (found [… 'spec id' …])`); current and `HEAD` `review-report.md` both parse to identical Finding nodes; the round-2 fixture parses clean with all five status words. The amended wording now matches the evidence exactly | ✅ met r2 |
| AC-3.1 | `review-report.md:9`, `qa-report.md:9`, `reviewer.md:100-101`, `qa-tester.md:50-52`; the re-test half is now reachable via `demo-day/SKILL.md:57-58` (F1) | ✅ met r2 |
| AC-3.2 | `review-report.md:103-104`, `qa-report.md:91-92` | ✅ met |
| AC-3.3 | `review-report.md:28`, `qa-report.md:27`; no "latest round" wording anywhere | ✅ met |
| AC-3.4 | `reviewer.md:102-106`, `qa-tester.md:52-57` — both now default to exactly `1`, matching this AC's wording rather than exceeding it | ✅ met |
| AC-3.5 | `git diff` for `templates/spec.md`/`plan.md` = exactly 1 added line each | ✅ met |
| AC-4.1 | md5 of the five checkbox lines with Soll masked: identical (`4c228c…`), re-run this round | ✅ met |
| AC-4.2 | Checkbox wording unchanged; F9 is the one exception and is recorded with a reason, which is what this AC requires | ✅ met |
| AC-4.3 | `qa-report.md:30-32,99` (~130), `release-notes.md:24-26,87` (~100) | ✅ met |
| AC-4.4 | md5 of the five agent sentences with the gate name masked: identical (`5e0834…`), re-run this round | ✅ met |
| AC-4.5 | `templates/spec.md:119`, `plan.md:101` | ✅ met |
| NFR-1 | No protected heading, column or ID pattern renamed or removed; live old-vs-new parse agrees on both templates | ✅ met |
| NFR-2 | `review-report.md:56-70`, `qa-report.md:60-76`; both templates now state the exact-`open` rule **and** the full five-word vocabulary — F3 closed the gap in `qa-report.md`, F8 in `review-report.md`; live-verified on both | ✅ met r3 |
| NFR-3 | No new command, agent, lens or template file; F1's fix adds one sentence, not surface | ✅ met |
| NFR-4 | Evidence Entries 8/9 claim no token/byte saving and record the fix round honestly; the Ist/Soll half is met for every gate opened after T6 existed, and the two that predate it are an accepted, reasoned exception (F9), not a silent miss. This report is itself the bounded-growth transcript: 151→150→150 lines across three rounds | ✅ met r3 |
| NFR-5 | No gate blocks on `Round`; old-shape parse unchanged | ✅ met |

**Library lens** (active, §1/§2/§4): §1 surface — still minimal; F1's fix adds a sentence to
an existing skill, no new entry point. §2 compatibility — purely additive, re-verified against
the real consumer: current and `HEAD` templates parse identically and the one drift is
pre-existing and equal on both; the version bump belongs to `/go-live`. §3 packaging — N/A
(constitution §2). §4 clarity — both templates now carry the same vocabulary (F3 + F8).

## 5. What Was Checked

- [x] Correctness: logic does what the acceptance criteria demand
- [x] Non-functional: applicable NFRs and constitution quality bars hold
- [x] Error handling: failures are handled, not swallowed
- [x] Security: no injected input trusted, no secrets in code — N/A, Markdown only
- [x] Tests: exist, are meaningful, and pass — no suite exists (constitution §4); `claude plugin validate` + four live parser runs substituted
- [x] Readability: the next developer will understand this

## 6. Verdict

This passes. Every code finding I raised over three rounds is fixed, and I confirmed each
by reading the file and re-running the real consumer, never by grepping for the fix text:
F1's sentence sits in the right step in `/peer-review`'s exact wording, so `/demo-day`
genuinely reaches the re-test mode; F2's and F4's wording is verbatim symmetric across
both agents; F3's and F8's `accepted` entries parse and are correctly excluded from
`open_findings` on both templates; and current vs. pre-change `qa-report.md` raise the
*identical* pre-existing drift, which is what makes the amended AC-2.5 true. The two
findings that were not about code are closed the only way they could be — by the user, on
the record. F10 was real: the implementer rewrote an acceptance criterion in an approved
spec and logged its own ruling beside rulings that are the PO's or the user's. It is now
explicitly ratified in C19 rather than quietly kept — the overstep is documented, not
erased. F9 is accepted with a stated reason (both gates closed before the checkbox
existed), which AC-4.2 allows and which beats a retrofit that would fake a self-report.
F7 stays open on purpose: an untracked handbook has no file to fix and must not be swept
in by `git add -A`. The best evidence for the feature remains the feature — fix-mode left
bare `fixed` cells and never touched `Round`, §4 carries a suffix only where a verdict
moved, and this report held at 151→150→150 lines across three rounds while absorbing five
new findings and two user rulings. The accretion it exists to prevent did not happen.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings — none was ever raised
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here) — F1 fixed r2; **F10 waived by the user 2026-08-20**, reason: the AC-2.5 amendment's content was independently verified correct twice, so the user ratified it directly (recorded in `spec.md` §7 C19) rather than reverting and re-running `/story-time`; the authority overstep is accepted as a one-off and stays on the record in C19 and in §3 here
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — all 22 ACs ✅, all 5 NFRs ✅ after F8's fix and F9's reasoned exception. No §6 non-negotiable touched; F10 was a §1 authority breach, now ratified by the only party who could
- [x] All plan deviations documented and accepted — both recorded in `plan.md:73-88`; the 12th-file addition accepted on its merits, the AC-2.5 amendment by the user's C19 ratification
- [x] Test suite runs green — N/A, no suite exists (constitution §4); `claude plugin validate .` passes and every live parser run this round is green, including the full `extract_features` → `gate_health` path
- [x] Line budget respected: Ist _150_ / Soll ~150 (excluding HTML comments) — self-reported, no linter checks this; an overage is recorded here with a reason or explicitly waived by the user
- [x] Status set to `passed`

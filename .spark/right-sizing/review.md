# Review Report: right-sizing

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | `git diff 22673c8..c03e643` (4 files) over the full feature diff `085db99..c03e643` (16 files), `.spark/right-sizing/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 4 |
| **Date** | 2026-08-31 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** round 4's §6 supersedes round 3's. **C19's action-based mechanism holds where it was
  built** — `agents/qa-tester.md` is correct against the current AC-1.3/NFR-4, and `qa.md` r7's 5/5
  claim survives spot-checking. **But C19 was landed in one of four declaration-reading files.**
  `skills/demo-day/SKILL.md:33`, `skills/spark/SKILL.md:78`, `agents/release-manager.md:73` and
  `skills/go-live/SKILL.md:37` still ship the *superseded* "say nothing / no mention" guarantee.
- **Open:** `7 open` — Blockers: `none`; Majors: **`F17`**. Minors/Nits: F10 (user-accepted as open
  since r3), F18, F19, F20, F21, F22. 16 findings closed; `F9`/`F15`/`F16` were left `fixed` by r3
  and are **confirmed `fixed r4`**. **r3's venue caveat is cleared:** `diff -rq` over `agents/
  skills/ templates/ lenses/ tools/` vs the `0.7.1` cache → zero differences.
- **What round 5 owes:** F17 is not a hand-patch of four files. `plan.md` T2/T8 still state "no
  error, no warning, no mention" as their *verification criteria*, so the code matches a plan that
  no longer matches the spec — r3's C17 root cause, one layer down. Route T2/T8 through
  `/sprint-plan`, then `/increment`, then a `/demo-day` round that can only cover the `qa-tester`
  half (the three skill files stay `not-verified-live`; `claude -p` auth is still broken,
  `qa.md:59-61`).
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Re-review, round 4, at `c03e643` (working tree clean). Reviewed: the four-file delta since r3
(`evidence.md` +375, `qa.md` +176 new, `spec.md` ±21, `agents/qa-tester.md` +61/−16), plus — read
fresh, not cited from r3 — `spec.md` end to end, `agents/qa-tester.md` end to end, `qa.md` end to
end, `evidence.md` Entries 13–14, and every shipped `§8` reader (`demo-day`, `spark`, `go-live`,
`release-manager.md`, `facilitator.md`, `templates/constitution.md`, `reviewer.md`). **Not
reviewed:** live agent behaviour — I do not re-run `/demo-day`'s invocations; I check whether the
shipped text supports what `qa.md` r7 reports it did.

**Re-derivation (AC-2.2, per AC-2.3).** **(b)** AC-1.3/NFR-4 — Must-AC verification, read fresh
from `spec.md:119`/`:149` under C19, never from r3's rows or C18's. **(a)** F9, F15, F16 —
confirming claimed fixes, each re-read at source. **(c)** AC-1.7 — r3 marked its row explicitly
unconfirmed. **(d)** `qa.md` r7's "5/5 clean" — seven rounds of prior failure on this exact claim
is a concrete reason. **(d)** the propagation state of the other four readers — r3 checked them
against pre-C19 wording. Everything else (F1–F8, F11–F14, NFR-1/2, the unchanged §4 rows) is
**cited from r2/r3, not re-derived**. Facts re-derived without a named condition: **0**.

**Spot-check of `qa.md` r7 (task-directed).** Every location it cites is accurate at source:
`qa-tester.md:46-47` (B5 fix string), `:86-93` (AC-1.6/1.9 pair), `:116` (`/charter`-only),
`:230-233` (all four AC-2.2 conditions), `release-manager.md:65-67`, `facilitator.md:114-115`. Its
Run 4/5 account is what the text prescribes: `qa-tester.md:56-59` does route a `surface: yes`
project straight to the unchanged equipment check, which is why AC-1.5 held 2/2. **The verdict is
trustworthy for what it tested and honest about what it did not** — §1, §3 and §5 all state the
three skill files remain `not-verified-live`, and §5 recommends the propagation F17 now files. One
imprecision, not filed: the `✅ pass r7` cells (`qa.md:71`, `:87`) carry no `not-verified-live`
qualifier though three other sections do; the disclosure exists and the substance is F17.

**Tool (`aspark-graph`, runner=yes / graph=yes), review slice.** `staleness` → `files_checked: 0`
(nothing indexed, not "fresh"). `impact --diff 22673c8..c03e643` → `files: []`, all four paths in
`unknown_files` = *"I do not index these"*, **not** an all-clear. `story_trace US-1` →
`{"found": false, "reason": "not_found"}`. All three are structural empties per the tool file's
Markdown-only rule, so **no tool result scoped any reading**: every location below was found by
hand (`grep -rn` over `agents/ skills/ templates/`) and read at the cited lines.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ r4 | `templates/constitution.md:105-125`. F15's `/spark` clause is present at `:115-118`; the four contract facts and both stated differences are true as shipped |
| T2 | ⚠️ r4 | `skills/demo-day/SKILL.md:27-47` matches the plan — but the plan's own Verification cell demands "no error, no warning, no mention" and "exactly as today, say nothing", which spec `C19` retired. Code conforms; the plan does not. **F17** |
| T10 | ⚠️ r4 | `skills/spark/SKILL.md:73-79`, both branches, unchanged since r1. The absent/`yes` branch still ends "and say nothing about the declaration" — **F17** |
| T3 | ⚠️ r4 | `agents/qa-tester.md:42-117`, rewritten twice since r3 for C19 and B5. Correct against the current AC-1.3/NFR-4 (§4), but carries **F18** and **F19** |
| T4 | ⚠️ r4 | `go-live:33-38` + `release-manager.md:63-75`; the citation form and the `qa.md`-`passed` requirement are intact. Both absent-case clauses still say "no mention of it" / "say nothing about the declaration" — **F17** |
| T5 | ✅ | `charter:45-53` + `facilitator:112-122` unchanged; the Hard Rule names all three readers with each one's real effect |
| T6 | ✅ | Identical block in `reviewer.md:171-186` and `qa-tester.md:226-241`; live-proven — this round runs under it (§1) |
| T7 | ✅ | `README.md:96` and `:251`; the status row still claims no saving and no generalization |
| T8 | ⚠️ r4 | Negative case documented; its Verification cell also fixes "no mention" as the criterion — **F17**, same root cause as T2 |
| T9 | ✅ r4 | The declared path is no longer "not run": `/demo-day` executed seven rounds against §8, `qa.md` r7 `passed`. r3's `⚠️` is discharged |
| D1 | ✅ | Unchanged: recorded, small, no scope effect |
| D2 | ✅ accepted | Unchanged from r3, including the open ratification note for the EM |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `templates/constitution.md:111` | The contract comment said `/go-live` "behaves exactly as today" while the same diff changed it. Fixed: `:112-118` now states its one difference | fixed r2 |
| F2 | Major | `skills/demo-day/SKILL.md:98` | `## Rules` rejected the report its own step 1 authorises. Fixed: `:99-104` qualifies "performed steps" for a declared method without weakening the fraud rule | fixed r2 |
| F3 | Major | `plan.md:72`, `evidence.md` §4.5 | Round 1 ran the installed `0.7.0`, so nothing in the diff had executed. Fixed: `0.7.1` installed at `47f6040`, cache byte-identical, review runs under it | fixed r2 |
| F4 | Minor | `agents/qa-tester.md` (r2 lines `:46-50`/`:61-65`) | Declared branch entered only on a complete §8 yet held an incomplete-case sub-bullet. Fixed: entry condition widened, four outcomes mirrored | fixed r2 |
| F5 | Minor | `skills/demo-day/SKILL.md:42`/`:81-83` | Step 1 promised to pass the method; step 2 enumerated URL/viewports only. Fixed: step 2 passes the method with URL/viewports `N/A` | fixed r2 |
| F6 | Minor | `agents/release-manager.md:73-75` | The only §8 reader that never stated AC-1.10. Fixed: read-only clause + point-to-`/charter` added | fixed r2 |
| F7 | Minor | `README.md:251` | Status row claimed dogfooding the declared path had not run. Fixed: row now states exactly that, and names the fixtures | fixed r2 |
| F8 | Minor | `agents/qa-tester.md` (r2 `:26`, `:111-112`, `:140-148`) | Agent was unconditionally browser-bound outside step 1. Fixed in all three places; steps 5–6 `N/A`-able with reason, without shrinking step 3 | fixed r2 |
| F9 | Nit | `spec.md:149` (NFR-4) vs `skills/charter/SKILL.md:45-53` | NFR-4's "every ceremony behaves exactly as today" did not exempt `/charter`, which asks one more question on every project. Resolved by spec amendment C17, no file change. **r4, re-derived under AC-2.2(a):** `spec.md:149` now reads "every ceremony that **reads** the declaration" with "**One exemption:** `/charter`, the ceremony that *writes* it" | fixed r4 |
| F10 | Nit | `skills/demo-day/SKILL.md:28`, `agents/qa-tester.md:55`, `skills/go-live/SKILL.md:33`, `skills/spark/SKILL.md:74`, `agents/release-manager.md:65` | §8 is addressed by number in five shipped files; a consumer numbering its sections differently makes the reference wrong. All five also name `QA Method`, so failure is unlikely — hence Nit. Fix: lead with the name, keep the number parenthetical. Open by the user's explicit decision, not by oversight | open |
| F11 | Nit | `agents/facilitator.md:76-83` | Paragraph indented 2 spaces inside a 3-space list item. Reviewer re-indented; `claude plugin validate` green | fixed r1 |
| F12 | Major | `agents/facilitator.md`, `agents/qa-tester.md` | Both claimed `/go-live` was the declaration's only other reader; `skills/spark/SKILL.md:73-79` reads it too and changes what the orchestrator asks. Fixed: `facilitator.md:117-122` and `qa-tester.md:112-115` name all three readers; re-enumeration found no third false variant | fixed r3 |
| F13 | Nit | `skills/demo-day/SKILL.md:55` | "Only once **both** gates above have passed" predated the §8 read becoming a third sub-step. Reviewer changed to "the gates" | fixed r2 |
| F14 | Nit | `evidence.md:518` | Entry 6 recorded `47f6040` as 12 files; `git show --name-only` → 15. Reviewer corrected in place. Capped Minor by AC-2.4 | fixed r2 |
| F15 | Minor | `templates/constitution.md:110-118` | The shipped contract comment gave `/go-live` its one difference and never mentioned `/spark`'s — the third instance of one stale-spec class, in the file that ships into every consumer's constitution. **r4, re-derived under AC-2.2(a):** `:115-118` now carries "/spark still runs every step it runs today - the one difference is that it stops asking for a start command, URL and browser tooling", satisfying amended AC-1.7 | fixed r4 |
| F16 | Minor | `evidence.md` §7.1 | §7.1 concluded "AC-1.1 performed" when only its `/spark` half had run and `/demo-day` had not. **r4, re-derived under AC-2.2(a):** `evidence.md:578-583` now reads "This is the orchestrator half only, and it is not AC-1.1 … AC-1.1 is **not yet met** and belongs in §7.4's not-run list" | fixed r4 |
| F17 | **Major** | `skills/demo-day/SKILL.md:31-33`, `skills/spark/SKILL.md:77-78`, `agents/release-manager.md:72-73`, `skills/go-live/SKILL.md:37` | C19 re-scoped AC-1.3/NFR-4 from content-suppression to an action-based rule and `spec.md:12` named the work as "`agents/qa-tester.md` **and the other declaration-reading files**". Only `qa-tester.md` was changed. These four still ship the retired guarantee — `demo-day:33` "say nothing about the declaration. No error, no warning, no mention."; `spark:78` "and say nothing about the declaration."; `release-manager:73` "word the row **exactly as today** and say nothing about the declaration."; `go-live:37` "worded exactly as today, with no mention of it." Why it matters: (i) `demo-day:33` and `qa-tester.md:69-74` ("You are not required to suppress this") are two shipped instructions for the **same phase** giving opposite answers — the NFR-3 / library-lens §4 contract defect F12 was Major for; (ii) all four restate a promise this feature's own `evidence.md` Entries 10–13 prove unachievable across four failed attempts, so the next `/demo-day` tests the skill half against a disproven claim and re-files B1/B4. Not a Blocker: over-suppression cannot produce the forbidden *action*, so AC-1.3's behavioural guarantee is not violated by it. Fix: propagate `qa-tester.md:60-82`'s three-part block (Never / Fine, not a violation / Discouraged) into all four, each scoped to its own ceremony — and first correct `plan.md` T2/T8's Verification cells, which still name "no mention" as the criterion | open |
| F18 | Minor | `agents/qa-tester.md:50-52` | "If a declaration already exists and is complete, you would not have reached this branch at all" is false for a complete `Browser-observable surface: yes` declaration, which `:56-59` routes straight to this equipment check. Disproved by `qa.md:73`'s own r7 Runs 4–5 (Venue B: `yes` + a named method, reached the equipment check and stopped). Why it matters: it is the reassurance a reader uses to decide the "never suggest a declaration" rule is unreachable in their case, and it is wrong on exactly the AC-1.5 shape. Fix: "If a **`no`-surface** declaration already exists and names a performable method, you would not have reached this branch." | open |
| F19 | Minor | `agents/qa-tester.md:45` vs `:69-74` | The STOP branch says "name the missing tool or URL, **nothing more**" — a content-suppression framing — while `:69-74` says stating in your own words that no declaration applies is "fine, not a violation" and "you are not required to suppress this". Both govern the same run (no declaration + no browser tooling). Why it matters: it reintroduces the "say nothing" shape C19 retired, in the very branch B5 came from, leaving the agent to arbitrate between two of its own rules — the failure mode Entries 10–13 attribute the four failed attempts to. Fix: scope it to the act, not the content — "name the missing tool or URL; add no options for unblocking yourself" | open |
| F20 | Nit | `evidence.md:995-998` | Entry 14 calls the STOP-branch fix "a third distinct location in the same file now carrying a C19-shaped constraint" and its own parenthetical names only two. Capped Minor by AC-2.4. Fix: say "second", or name the third (`qa-tester.md:79-82`, the invocation-independence sentence) | open |
| F21 | Nit | `spec.md:227` vs `:12` and `:255` | C18's resolution cell still reads "not yet re-approved" while the Handoff and SPEC GATE both record it re-approved 2026-08-31 — the same Handoff-vs-body class `/increment` already fixed once for C19 (`evidence.md:1000-1006`). Capped Minor by AC-2.4: C18 is superseded, no verdict or gate answer turns on it. Fix: "re-approved at the `/story-time` gate of 2026-08-31, later superseded by C19" | open |
| F22 | Nit | `spec.md:254` | SPEC GATE reports "Ist 253 / Soll ~250"; the file is 255 lines with 4 HTML-comment lines (`:105-107`, `:232`) → Ist **251**. Over-reports its own overage, so the box's "recorded not waived" branch is unaffected. Capped Minor by AC-2.4. Fix: 251 | open |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `demo-day:40-42`, `spark:73-77`, `qa-tester:94-96` | ✅ met |
| AC-1.2 | `demo-day:43-45`, `qa-tester:101-103`, `templates/constitution.md:106-108` | ✅ met |
| AC-1.3 | `qa-tester:60-82` (Never / Fine / Discouraged) + `:45-52` (STOP branch, B5); `demo-day:31-33`, `spark:75-78`, `go-live:37` | ⚠️ **partial r4** — re-derived under AC-2.2(b) against C19's current text. The agent half is correct and live-evidenced 5/5 (`qa.md:71`). The `/demo-day`, `/spark`, `/go-live` and `release-manager` halves still state the superseded content-suppression claim: **F17** |
| AC-1.4 | `go-live:33-37`, `release-manager.md:63-71` | ✅ met |
| AC-1.5 | `qa-tester:56-59`, `demo-day:31-33`, `templates/constitution.md:123-124` | ✅ **met r4** — no longer fixture-only: `qa.md:73` records 2/2 live runs on a `yes`-surface venue routing to the unchanged equipment check |
| AC-1.6 | `demo-day:37-39`, `qa-tester:91-93` | ✅ met r4 — fixture (c) discharged by `qa.md:74`'s five live stops |
| AC-1.7 | `templates/constitution.md:109-118`, `facilitator.md:117-122`, `qa-tester:112-115`; `agents/reviewer.md` → 0 declaration references | ✅ **met r4** — re-derived under AC-2.2(c), r3's row was explicitly unconfirmed. Both stated differences present in all three mirrors; the generic-mechanism fence holds |
| AC-1.8 | `charter:45-53`, `facilitator:112-118`; `.spark/constitution.md` Amendments row | ✅ met |
| AC-1.9 | `demo-day:34-36`, `spark:75`, `qa-tester:86-90`, `go-live:37` | ✅ met r2 |
| AC-1.10 | `qa-tester:115-117`, `demo-day:45-47`, `go-live:38`, `spark:78-79`, `facilitator:112-114`, `charter:52-53`, `release-manager:73-75` | ✅ met r2 |
| AC-2.1–2.3 | `reviewer.md:171-181`, `qa-tester.md:226-236` — conditions (a)–(d) verbatim, "name which condition triggered it" | ✅ met |
| AC-2.4 | `reviewer.md:182-186`, `qa-tester.md:237-241` | ✅ met |
| AC-2.5 | no age/shape instruction anywhere in `085db99..c03e643` | ✅ met |
| NFR-1 | `templates/constitution.md` +28/−0; no template touched since `22673c8` | ✅ met |
| NFR-2 | `git diff --stat 085db99..c03e643`: 16 files, all pre-existing; 10 skills / 7 agents / 9 lenses / 6 templates unchanged | ✅ met — the line-by-line release-note enumeration is still `/go-live`'s to deliver |
| NFR-3 | `templates/constitution.md:105-125` + the per-file blocks | ⚠️ **partial r4** — F15 confirmed fixed, but the contract now answers "what may the QA phase say?" two opposite ways across `demo-day:33` and `qa-tester:69-74` (**F17**), and `qa-tester:50-52` states a false precondition (**F18**) |
| NFR-4 | the absent/incomplete branch in all five readers; `qa-tester:60-82` carries C19's action-based form | ⚠️ **partial r4** — re-derived under AC-2.2(b). Held 5/5 live where implemented; the other four readers state a superseded guarantee (**F17**) |
| NFR-5 | `README.md:96`, `:251`; no line/token/dollar or generalization claim in `085db99..c03e643` | ✅ met — release-notes half falls to `/go-live` |
| NFR-6 | `git diff 085db99..c03e643 -- templates/ skills/ agents/ README.md \| grep -E "^[+-]\s*- \[[ x]\]"` → **empty**: not one gate-item line added, removed or reworded across the whole feature | ✅ met — re-derived, not cited |

## 5. What Was Checked

- [x] Correctness: AC-1.3/NFR-4 re-read under C19 and traced to `qa-tester.md:45-82` line by line;
  all six `§8` readers re-enumerated by grep and read
- [x] Non-functional: NFR-1…6 re-checked; library lens §1 (no new public surface), §2 (additive, no
  protected §3 structure touched, `plugin.json` still `0.7.1` for `/go-live` to bump), §4 (contract
  clarity — where F17/F18 land). §3 N/A per constitution §2
- [x] Predecessor claim: `qa.md` r7's cited locations spot-checked at source (§1) — accurate; its
  `passed` verdict is trustworthy for the half it tested, honest about the half it did not
- [x] Edge cases: the `yes`-surface + complete-method venue (F18), the STOP branch with no
  declaration (F19), the incomplete and unperformable branches (intact, `qa-tester:86-93`)
- [x] Error handling / security: all four fall-backs still resolve toward more verification.
  Security N/A per constitution §2/§5; nothing private added
- [x] Tests: `claude plugin validate` → passed (1 pre-existing `autoUpdate` warning, outside the
  diff). No suite exists or is possible (constitution §4)
- [x] Venue: `diff -rq` over `agents/ skills/ templates/ lenses/ tools/` vs the `0.7.1` cache →
  zero differences. r3's carried caveat is cleared

## 6. Verdict

**`changes-requested`.** The mechanism itself is sound, and I want to say that before the finding:
`agents/qa-tester.md` is now genuinely correct against the *current* AC-1.3/NFR-4. The re-scoping
to an action rule is the right repair — it traces back to US-1's own "so that I stop
re-negotiating" clause instead of a stronger claim the loop invented — and `qa.md` r7's 5/5
survives spot-checking: every location it cites is accurate, its Run 4/5 account is exactly what
`qa-tester.md:56-59` prescribes, and it discloses its own limits rather than papering over them.
Seven rounds of QA did not miss something inside the file they tested.

**They missed something outside it, and said so.** C19 changed a requirement that four shipped
files make a promise about; one was updated. `skills/demo-day/SKILL.md:33` still orders "say
nothing about the declaration. No error, no warning, no mention" — the QA phase's own skill
contradicting the QA phase's own agent, which now says "you are not required to suppress this".
`/spark`, `/go-live` and `release-manager.md` carry the same retired wording. Nothing here breaks
the behavioural guarantee — silence still satisfies an action rule — which is why F17 is Major and
not a Blocker. What it breaks is the contract: a consumer reading the two files gets two answers,
and three of them still promise something `evidence.md` Entries 10–13 spent four failed attempts
proving cannot be kept. `qa.md:140-152` recommended exactly this propagation and named the honest
caveat; the recommendation was not actioned, which is the same shape as the `lean-rounds` learning
§1 cites as this feature's own "why now".

**The routing matters more than the patch.** `plan.md` T2/T8 still name "no error, no warning, no
mention" as their *verification criteria* — the four files are faithful to a plan that is no longer
faithful to the spec. That is C17's root cause one layer down, and hand-patching alone would leave
the plan able to re-certify the retired wording next round. Fix T2/T8 at `/sprint-plan`, land the
propagation, then re-test what can be re-tested — the three skill files stay `not-verified-live`
whatever their wording says, and that limit belongs in the change, stated plainly. F18 and F19 are
left `open` deliberately: both are one-line edits, but they sit inside the exact text seven QA
rounds just certified, and a reviewer editing it would invalidate `qa.md` r7's venue claim. **I
applied no fixes this round.** No Blocker, one Major, no non-negotiable violated, `validate` green.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [ ] **No open Major findings — `F17` is open and not waived.** Only the user may waive a Major
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — §6's
  five re-checked: no protected §3 structure renamed, all four fall-backs intact in every reader,
  nothing executed unasked, no gate self-passed, nothing private added. AC-1.3/NFR-4 trace to
  `qa-tester.md:45-82` but only partially across the other readers (F17)
- [ ] **All plan deviations documented and accepted — `plan.md` T2/T8's verification criteria
  contradict spec C19 and need `/sprint-plan` to ratify the change** (§2, §6)
- [x] Test suite runs green — none exists (constitution §4); the bar, `claude plugin validate`,
  re-run this round: passed with the 1 pre-existing `autoUpdate` warning
- [x] Line budget respected **on the template's second branch, not the first**: **Ist 208 / Soll
  ~150** (excluding HTML comments — none in this file) — **58 over, recorded not waived.** Cause:
  22 finding rows in a non-appending file, six of them new. Mitigated, not solved — every closed
  row was compressed to location/problem/fix/status with its round-by-round narrative left to git,
  and §1/§5/§6 were trimmed twice. The budget itself is **not** met and I am not claiming it is;
  the honest fix is a convention for retiring closed rows, which is not mine to invent here
- [ ] Status set to `passed` — set to `changes-requested`

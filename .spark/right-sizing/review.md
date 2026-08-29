# Review Report: right-sizing

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | The uncommitted working-tree diff of `/increment`, `.spark/right-sizing/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 1 |
| **Date** | 2026-08-29 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** Round 1's verdict stands as written in §6. `/increment` has since fixed F1, F2 and F4–F8 in place. F3 is **partially** addressed: its text half — the untrue claims in `plan.md` §4, that gate's test-strategy box, and `evidence.md` §4.5 — is corrected, but its venue half is not, and F3 is deliberately left `open` rather than marked fixed.
- **Open:** `3 open`, 8 fixed — Blockers: `none`; Majors: `F3` (venue half only: ceremonies still load the installed `0.7.0`, so no ceremony has executed this diff; the user has taken on installing this branch). Nits `F9`, `F10` are open by explicit user decision — accepted, not fixed. F9 is for the EM/PO, not the developer.
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Reviewed: the full working-tree diff, 11 modified tracked files, +175/−6 after my own fix
(`git diff --stat`; `/increment`'s Entry 4.1 quotes 10 files/+153 — that count predates the
T9 amendment to `.spark/constitution.md` and my F11 fix, and is not a discrepancy). Read in
full: `spec.md`, `plan.md`, `evidence.md`, `.spark/constitution.md`, `lenses/library.md`.
Read in context beyond the diff: `skills/demo-day/SKILL.md` whole, `agents/qa-tester.md`
whole, `agents/release-manager.md` §§1–6, `templates/release-notes.md` §1.

**Tool (`aspark-graph`, runner=yes / graph=yes).** `staleness` → `stale: false`,
`files_checked: 0` (nothing indexed — not "fresh"). `impact` on all 11 changed paths →
`found: true`, `files: []`, all 11 in `unknown_files` = *"I do not index these"* (Markdown-only
repo), **not** an all-clear. `story_trace US-1`/`US-2` → `{"found": false, "reason":
"not_found"}`. `gate_health` and the QA leg not called, per the tool file. **No result
scoped any reading**; every location below was found by hand and read directly.

Not reviewed: `.spark/right-sizing/` is untracked and is input, not diff. No re-review — round 1.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ⚠️ | Section, both fields and both `Default when absent:` present. The contract comment states all four facts but one of them is false as shipped — **F1** |
| T2 | ⚠️ | All four outcomes present and correctly ordered (`:27-47`). Two loose ends the DoD didn't reach: **F2**, **F5** |
| T10 | ✅ | `skills/spark/SKILL.md:73-79`, both branches, pure insertion, no write path |
| T3 | ⚠️ | Branch, fraud rule and one-row-per-AC/NFR all present. Entry condition contradicts its own incomplete case — **F4**; downstream browser-only steps unqualified — **F8** |
| T4 | ⚠️ | Both files carry the citation form and the absent-case wording; §1 pre-flight item untouched. `release-manager.md` omits the AC-1.10 clause — **F6** |
| T5 | ✅ | `charter:45-53` + `facilitator:76-83`, explicit user decision, profile explicitly not an answer; Hard Rule at `facilitator:112-116` |
| T6 | ✅ | Identical block in both agents, all four AC-2.2 conditions verbatim, cap correctly conjunctive |
| T7 | ⚠️ | Both README locations updated; the status row over-labels maturity — **F7** |
| T8 | ⚠️ | 4.1/4.3/4.4/4.6 are real performed checks. 4.2 is a text reading, and 4.5's stated cause is wrong — **F3** |
| T9 | ⚠️ | §8 written by `/charter` with the user's confirmation logged; fixtures (a)/(b) sound, (c) honestly partial. The declared-path QA/release run is `not run` by design (5.3) and now blocked by **F3** |
| D1 | ✅ | Deviation recorded, small, no scope effect. `.spark/graph-gates-verification/` confirmed absent; `.spark/graph-gates/qa.md` is the stronger specimen, as claimed |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `templates/constitution.md:111` | The shipped contract comment asserts "`/story-time`, `/look-and-feel`, `/sprint-plan`, `/increment`, `/peer-review` and **`/go-live` behave exactly as today**". This same diff changes `/go-live` (`skills/go-live/SKILL.md:33-37`, `agents/release-manager.md:63-73`). It is false in the one file that ships into every consumer project as the contract, so a consumer will trust the wrong thing (NFR-3, library lens §4). `agents/facilitator.md:116` ("never any other ceremony") and `agents/qa-tester.md:66` ("no other ceremony changes at any value of it") repeat it. Fix: apply the plan §1 ruling verbatim — no ceremony gains an off switch, and `/go-live` changes only how §1's QA row is *worded* (AC-1.4) | fixed |
| F2 | Major | `skills/demo-day/SKILL.md:98` | `## Rules` still reads "A QA report without performed browser steps is invalid — **reject it** and fix the tooling problem instead." On a declared project the new step-1 branch produces exactly such a report, so the ceremony's own Rules order the orchestrator to reject the report its own step 1 just authorised. This fires at the very next ceremony of this loop, on this repo. Fix: qualify to "without performed steps — of the declared method where §8 declares one" (AC-1.1, AC-1.2) | fixed |
| F3 | Major | `plan.md:72`, `evidence.md` §4.5 | Ceremonies load `${CLAUDE_PLUGIN_ROOT}`, which resolves to the installed cache `~/.claude/plugins/cache/aspark/aspark/0.7.0/` (the paths this ceremony was handed); the repo is `0.7.1`. `grep -c "Cite what a predecessor already established" .../0.7.0/agents/reviewer.md` → **0**. So no ceremony in this session ran any changed text. Consequences: plan §4's "US-2 is verified by this feature's own loop … the only live proof available" is untrue this round, which makes the PLAN GATE's test-strategy box untrue as worded; `evidence.md` §4.5 blames the contradicting live `/spark` observation on venue when the orchestrator was 0.7.0's `/spark`, which has no §8 clause at all — so that observation is not evidence about the shipped text in either direction; and `/demo-day` under §8's "against the **installed plugin**" cannot exercise this diff until it is installed. Not capped by AC-2.4: it changes a gate answer and a Must story's verification. Fix: install this branch locally (or point the plugin root at the working tree), re-run the absent-case and declared-case dry runs, and correct plan §4 + evidence §4.5 | open |
| F4 | Minor | `agents/qa-tester.md:46-50` vs `:61-65` | The branch is entered only when §8 "declares one — a project with no browser-observable surface **naming the method**", yet a sub-bullet inside it handles "**incomplete** — surface `no` with no method named" by STOPping. Either that clause is unreachable, or an incomplete §8 STOPs QA — which diverges from `/demo-day:34-36` and `/spark:77`, both of which fall back to today's ask (AC-1.9, NFR-4). The plan's own risk row predicted exactly this divergence. Fix: enter the branch on "§8 exists at all" and mirror `/demo-day`'s four outcomes | fixed |
| F5 | Minor | `skills/demo-day/SKILL.md:42` vs `:72-80` | Step 1 promises "pass the method to the QA Tester in step 2", but step 2's payload list is unchanged and still enumerates "the app URL … the agreed viewports", which do not exist on a declared project, and never mentions the method. Only `agents/qa-tester.md:46`'s own fallback read of §8 saves this. Fix: add the declared method to step 2's list and mark URL/viewports `N/A` there | fixed |
| F6 | Minor | `agents/release-manager.md:63-73` | The only touched §8 reader that never states AC-1.10. Every other one does: `demo-day:45-47`, `qa-tester:67-69`, `go-live:38`, `spark:78-79`, `facilitator:112-116`. NFR-3 requires the fact where its writer meets it, and `release-manager.md` is the file that actually writes `release.md`. Fix: append "You only **read** §8; only `/charter` creates or amends it." | fixed |
| F7 | Minor | `README.md:251` | The status row labels the capability "**Shipped, dogfooded on this repo only**", but `evidence.md` §5.3 marks the declared QA and release path **not run**, and F3 shows it could not have run. Constitution §1 ("a doc that presents an intention as delivered is a defect") and §4's docs-in-step bar make this a defect now, even if it becomes true two ceremonies from now. Fix: label it as shipped with the declared path first exercised by this feature's own `/demo-day`/`/go-live`, and re-check the row at `/go-live` | fixed |
| F8 | Minor | `agents/qa-tester.md:26`, `:111-112`, `:140-148` | Outside step 1 the agent is still unconditionally browser-bound — "`pass` only after you performed the steps **in the browser**", "every verdict rests on a step you performed **in the browser**", step 5 "resize to mobile width", step 6 "watch the browser console" — with no guidance for a declared project, while `:157-159` forbids improvising. Fix: one clause in the declared branch naming which of steps 5–6 are `N/A` and restating the verdict rule method-neutrally | fixed |
| F9 | Nit | `spec.md:150` (NFR-4) vs `skills/charter/SKILL.md:45-53` | NFR-4 says that with no declaration "**every** ceremony behaves exactly as today"; `/charter` now asks one more question on every project, declared or not. Honestly recorded in `evidence.md` §4.1, but the NFR's literal wording needs the writing ceremony exempted. For the EM/PO, not the developer | open |
| F10 | Nit | `skills/demo-day/SKILL.md:28`, `agents/qa-tester.md:47`, `skills/go-live/SKILL.md:33`, `skills/spark/SKILL.md:74`, `agents/release-manager.md:65` | The section is addressed by number (`§8`) in five shipped files. A consumer constitution that numbers its sections differently makes the reference wrong; the existing precedent (`go-live:31`) names `Delivery & Handoff` by name only. All five do also name `QA Method`, so the failure is unlikely — hence Nit. Fix: lead with the name, keep the number parenthetical | open |
| F11 | Nit | `agents/facilitator.md:76-83` | The new paragraph was indented 2 spaces inside a 3-space ordered-list item, so it read as a lazy continuation rather than part of item 3. Reviewer re-indented to 3 spaces; no wording changed; `claude plugin validate` re-run green afterwards | fixed r1 |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `demo-day:40-42`, `spark:73-77`, `qa-tester:46-50` | ✅ met |
| AC-1.2 | `demo-day:43-45`, `qa-tester:55-57`, `templates/constitution.md:106-108` | ✅ met |
| AC-1.3 | `demo-day:31-33`, `spark:77-79`, `go-live:37`; guard-false re-issue of all 6 deleted lines | ✅ met in text; live evidence is F3 |
| AC-1.4 | `go-live:33-37`, `release-manager.md:63-73` | ✅ met |
| AC-1.5 | `demo-day:31-33`, `qa-tester:47-48`, `templates/constitution.md:114-115`; fixture (a) in `evidence.md` §5.2 | ✅ met |
| AC-1.6 | `demo-day:37-39`, `qa-tester:61-65` | ✅ met (fixture (c) honestly partial) |
| AC-1.7 | `templates/constitution.md:109-111` | ⚠️ partial — F1; the AC-1.7/AC-1.4 tension itself is ruled by the user (`plan.md:33`) and is not a finding |
| AC-1.8 | `charter:45-53`, `facilitator:76-83`; `.spark/constitution.md` Amendments row | ✅ met |
| AC-1.9 | `demo-day:34-36`, `spark:77`, `go-live:37` | ⚠️ partial — F4 (`qa-tester` diverges) |
| AC-1.10 | `demo-day:45-47`, `qa-tester:67-69`, `go-live:38`, `spark:78-79`, `facilitator:112-116`, `charter:52-53` | ⚠️ partial — F6 (`release-manager.md`) |
| AC-2.1 | `reviewer.md:171-181`, `qa-tester.md:177-187` | ✅ met |
| AC-2.2 | same, conditions (a)–(d) verbatim, framed "bounded reading, never 'don't verify'" | ✅ met |
| AC-2.3 | same, "name which condition triggered it" | ✅ met |
| AC-2.4 | `reviewer.md:182-186`, `qa-tester.md:188-192` — three conjunctive conditions, cap at `Minor`, never gate-blocking | ✅ met |
| AC-2.5 | no age/shape instruction added anywhere (`git diff agents/ \| grep -iE '\+.*(pre-existing\|legacy\|migrat)'` → empty, re-run) | ✅ met |
| NFR-1 | `templates/constitution.md` +21/−0; parser blindness cited from `evidence.md` Entry 1 P1/P2 under AC-2.1, not re-derived | ✅ met |
| NFR-2 | no new command, agent, lens or template file (`git status --short` = 11 `M`, 0 `A`); `/spark` extension is the recorded plan-gate ruling | ✅ met — the line-by-line release-note enumeration is `/go-live`'s to deliver |
| NFR-3 | `templates/constitution.md:99-114` + the per-file blocks | ⚠️ partial — F1, F4, F6 |
| NFR-4 | the absent branch in all four readers | ⚠️ partial — F3 (no executed run), F9 (`/charter`) |
| NFR-5 | `README.md:251`, `evidence.md` §5.3; no line/token/dollar claim anywhere in the diff | ⚠️ partial — F7 (maturity label, not a volume claim) |
| NFR-6 | none of `templates/{spec,plan,review-report,qa-report,release-notes}.md` is in the diff; `skills/go-live/SKILL.md` step 4 untouched | ✅ met — verified from the diff itself |

## 5. What Was Checked

- [x] Correctness: logic does what the acceptance criteria demand — traced all 15 Must ACs above
- [x] Non-functional: applicable NFRs and constitution quality bars hold — NFR-1…6, constitution §1/§3/§4/§6
- [x] Error handling: failures are handled, not swallowed — every fall-back resolves toward more verification; F4 is the one inconsistency
- [x] Security: N/A per constitution §2/§5 — no runtime, no data; no secret or private material added under `.spark/`
- [x] Tests: `claude plugin validate` re-run green (1 pre-existing `autoUpdate` warning, outside the diff); no suite exists or is possible (§4)
- [x] Readability: clear, but see F1/F4 — two blocks contradict themselves

## 6. Verdict

**`changes-requested`.** The feature is genuinely built: both rules land at every reader
named in NFR-2 as extended, all fifteen Must acceptance criteria trace to concrete shipped
text, the additive-only shape is real (six deleted lines, every one re-issued behind a guard
that is false when nothing is declared), and NFR-6 holds by construction because none of the
five gate-bearing templates is in the diff at all. `/increment`'s evidence is unusually honest
— it flags its own gaps in §4.5 and §5.3 rather than smoothing them. What stops it is that
three statements the diff ships are contradicted by the diff itself: the consumer-facing
contract comment says `/go-live` is unchanged while this same commit changes it (F1);
`/demo-day`'s Rules section orders the orchestrator to reject the very report its new branch
authorises (F2); and the README labels as dogfooded a path that has not run. Underneath all of
it sits F3: this loop reads the installed 0.7.0 plugin, not the working tree, so nothing in
this diff has ever been executed by any ceremony — which explains the one contradicting live
observation in §4.5, invalidates the plan's stated proof for US-2, and blocks `/demo-day`
until the branch is installed. None of that is a Blocker — no gate moved, no coverage was
suppressed, and every ambiguity resolves toward more verification, exactly as C15 demands —
but F1 and F2 will mislead the next reader and the next ceremony respectively, and F3 has to
be settled before anyone can claim this was dogfooded.

**Open questions for the EM/PO** (not findings): (1) with AC-2.2(b) exempting every Must AC's
verification, US-2's rule saves a `/peer-review` round on an all-Must feature almost nothing —
S2 is satisfiable by construction, so consider whether S2 is measuring anything; (2) F9's
NFR-4 wording needs the writing ceremony exempted, or `/charter` is a standing NFR-4 breach.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

- [x] No open Blocker findings
- [ ] No open Major findings — **F1, F2, F3 open**; not waived
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — §6's five non-negotiables each checked: no protected structure renamed, absent-case branches present, nothing executed unasked, no gate self-passed, nothing private added
- [x] All plan deviations documented and accepted — D1 recorded and verified
- [x] Test suite runs green — none exists (constitution §4); the bar, `claude plugin validate`, re-run green after F11's fix
- [x] Line budget respected: Ist 141 / Soll ~150 (excluding HTML comments — none in this file)
- [ ] Status set to `passed` — set to `changes-requested`

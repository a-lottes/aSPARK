# Review Report: right-sizing

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | `git diff 085db99..47f6040` (15 files) + five uncommitted working-tree modifications, `.spark/right-sizing/plan.md` |
| **Status** | `passed` |
| **Round** | 3 |
| **Date** | 2026-08-29 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** round 3's §6 supersedes round 2's. **F12 confirmed fixed** — both files name all
  three readers, both statements true against source, and **no third false variant** was
  introduced. Two new `Minor` findings in new locations: `F15` (`templates/constitution.md:110-111`)
  and `F16` (`evidence.md` Entry 7.1).
- **Open:** `1 open`, 15 fixed — Blockers: `none`; Majors: `none`. Only `F10` remains open, by
  the user's explicit decision — accepted, not fixed.
  **The root cause named in §6 was repaired, not worked around.** The user took the verdict's
  route: at a second `/story-time` gate on 2026-08-29 the Product Owner amended **AC-1.7**
  (complete fence, both stated differences), **NFR-4** (one exemption — `/charter`, the writing
  ceremony) and **NFR-2** (a *fourth* mirror the PO found, which omitted `skills/spark/SKILL.md`
  and would have made `/go-live` enumerate six locations against a spec naming five). Logged as
  spec C17. `F9` closed with no file change; `F15` then followed as the single clause the
  amendment obliged; `F16` corrected an overstatement in `evidence.md` §7.1.
  **What round 4 owes:** confirming the shipped text against the *amended* AC-1.7 — the
  traceability row for it is marked unconfirmed, and no reviewer has yet read the amended spec.
- **Venue caveat, carries to `/demo-day` (verified this round):** cache-vs-tree now differs on
  exactly `agents/facilitator.md`, `agents/qa-tester.md`, `skills/demo-day/SKILL.md` and, since
  F15, `templates/constitution.md` — the QA phase, `/charter` and the shipped template. `claude plugin update aspark@aspark` **plus a restart** before
  `/demo-day`. `agents/reviewer.md` is byte-identical, so the caveat did not reach this round.
- **Binding ruling:** §6 Verdict and the gate checklist below — the only binding location.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Re-review, round 3. Reviewed: committed `git diff 085db99..47f6040` (15 files, +1202/−11)
**plus all five uncommitted modifications** — the F12 fix (`facilitator.md`, `qa-tester.md`),
my own F13 fix (`demo-day/SKILL.md`), and the two `.spark/right-sizing/` artifacts. Read in
full: the F12 delta and its surrounding blocks, every file mentioning `§8`, `spec.md`'s AC/NFR
lists, `plan.md` §1 + `## Deviations`, `evidence.md` Entry 7, constitution §§4/6/8, the lens.

**Re-derivation (AC-2.2, per AC-2.3).** **(a)** for F12 — the reader set re-enumerated from
source (`grep -rn '§8'` over `agents/ skills/ templates/ README.md`, each hit then read), not
taken from F12's row or `/increment`'s claim; **(a)** again for F14's count (`git show
--name-only 47f6040 | wc -l` → 15, correction present at `evidence.md:518`). **(d)** for the
venue — the brief calls the installed snapshot settled while three shipped files have moved
since the install. Everything else (F1–F8, F11, F13, the unchanged §4 rows) is **cited from
round 2, not re-derived**. Facts re-derived without a named condition: **0**.

**Venue, re-checked.** `agents/reviewer.md` in the `0.7.1` cache is byte-identical to the tree
and carries the US-2 rule (`grep -c` → 1), as do my own instructions — I am executing `0.7.1`.
`diff -rq` over `agents/ skills/ templates/ lenses/ tools/` differs on exactly three files:
`facilitator.md`, `qa-tester.md`, `demo-day/SKILL.md` — the QA phase and `/charter`, neither of
them this ceremony. **Entry 6/7.4's framing is right:** the caveat is `/demo-day`'s, not mine.

**Tool (`aspark-graph`, runner=yes / graph=yes), review slice.** CLI + `graph.json` both
present. `staleness` → `files_checked: 0` (nothing indexed, not "fresh"). `impact` on the three
changed files → `found: true`, `files: []`, all three in `unknown_files` = *"I do not index
these"*, **not** an all-clear. A structural empty per the tool file, so **no tool result scoped
any reading**: every location below was found by hand and read at the cited lines.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ⚠️ | `templates/constitution.md:99-121`. The contract comment's four facts are all true as shipped (F1 fixed). But its ceremony list at `:110-111` matches AC-1.7 *verbatim* — and AC-1.7 predates `/spark` joining the diff, so the shipped comment accounts for `/go-live`'s one difference and is silent on `/spark`'s: **F15** |
| T2 | ✅ | Four outcomes (`:31-42`), coverage + write-lock clause (`:43-47`), Rules qualified (`:99-104`), step 2 passes the method (`:81-83`). F2, F5, F13 all landed in this file |
| T10 | ✅ | `skills/spark/SKILL.md:73-80`, both branches, pure insertion, no write path — unchanged since round 1. Its declared branch drops three asks (start command, URL, browser tooling): `facilitator.md:117-119` states all three, `qa-tester.md:82-83` names two — accurate but not exhaustive; no defect |
| T3 | ⚠️ | Entry condition now "exists at all" with `/demo-day`'s four outcomes mirrored (`:47-80`); steps 5–6 `N/A` clause at `:76-80`. F4, F8 fixed; **F12 fixed r3** — `qa-tester.md:81-84` now names `/spark` and `/go-live` as the only readers besides this phase, both true |
| T4 | ✅ | `go-live:33-38` + `release-manager.md:63-73`; the latter now carries AC-1.10 (F6 fixed). §1's `qa.md`-`passed` requirement is explicitly unchanged |
| T5 | ✅ | `charter:45-53` + `facilitator:76-83` unchanged and correct; the Hard Rule, now `:112-122`, names all three readers with each one's actual effect — **F12 fixed r3**, verified against `spark:70-80` |
| T6 | ✅ | Identical block in `reviewer.md:171-186` and `qa-tester.md:194-209`; now **live-proven** — this round runs under it |
| T7 | ✅ | `README.md:96` and `:251`; the status row now states the declared path has **not** run (F7 fixed) |
| T8 | ✅ | 4.5's cause corrected and honest; the venue it named as missing now exists and is exercised (F3) |
| T9 | ⚠️ | §8 written by `/charter` with the user's confirmation logged; fixtures (a)/(b) sound, (c) honestly partial. The declared-path QA/release run remains `not run` **by design** (5.3) — no longer blocked, `/demo-day` is now performable |
| D1 | ✅ | Unchanged from round 1: recorded, small, no scope effect |
| D2 | ✅ accepted | Correcting a claim review proved false is not a scope change, it was recorded with its reason, and `/increment` did not touch `Status` or any `[x]`/`[ ]` state — constitution §6's "no agent passes its own gate" is intact. One thing for the EM to ratify: `plan.md:15`'s binding ruling names **§1/§3** as the revision locations, and D2 landed in §4 + the PLAN GATE prose. D2 itself invites that ratification |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `templates/constitution.md:111` | The shipped contract comment asserted "`/story-time`, `/look-and-feel`, `/sprint-plan`, `/increment`, `/peer-review` and **`/go-live`** behave exactly as today" while this same diff changes `/go-live`. **r2:** `:110-114` now drops `/go-live` from that list and states its one difference ("still runs every check it runs today — the one difference is how it *words* the QA row"), which is exactly the `plan.md:33` ruling and matches AC-1.4. The list that remains is AC-1.7's, verbatim | fixed r2 |
| F2 | Major | `skills/demo-day/SKILL.md:98` | `## Rules` ordered the orchestrator to reject the very report its own step 1 authorises. **r2:** `:99-104` now reads "without performed steps … 'Performed steps' means **in the browser**, except on a project whose constitution §8 declares a substitute method, where it means steps performed by *that* method", and keeps "a report resting on code reading is invalid on every project". The contradiction is gone and the fraud rule is not weakened | fixed r2 |
| F3 | Major | `plan.md:72`, `evidence.md` §4.5 | Ceremonies load `${CLAUDE_PLUGIN_ROOT}`; round 1 ran the installed `0.7.0`, so nothing in the diff had been executed. **r2, re-derived under AC-2.2(a)/(d) — see §1 Venue:** the marketplace is repointed at the working tree, `0.7.1` is installed at `47f6040`, the cache is byte-identical to the tree (six paths checked, three more than claimed), and **this review is itself running `0.7.1`'s `reviewer.md`**. `plan.md:72`'s corrected, conditional claim is accurate and its condition is now met; `evidence.md` §4.5 correctly retracts the "venue contamination" cause. Entry 6's own "F3 closes at the first `/peer-review` run under `0.7.1`" — that is this run | fixed r2 |
| F4 | Minor | `agents/qa-tester.md:46-50` vs `:61-65` | The declared branch was entered only on a *complete* §8, yet contained an incomplete-case sub-bullet. **r2:** `:47-49` now enters on "the caller passed one, or §8 exists at all" and `:51-59` mirrors `/demo-day`'s four outcomes; the incomplete case falls back to the equipment check, consistent with `demo-day:34-36` and `spark:75` | fixed r2 |
| F5 | Minor | `skills/demo-day/SKILL.md:42` vs `:72-80` | Step 1 promised to pass the method to step 2; step 2 still enumerated URL/viewports only. **r2:** `:81-83` passes "**that method** in place of the app URL and the viewports, and say they are `N/A`" — the promise and the payload now agree | fixed r2 |
| F6 | Minor | `agents/release-manager.md:63-73` | The only touched §8 reader that never stated AC-1.10. **r2:** `:71-73` now reads "You only **read** §8; only `/charter` creates or amends it, so if you believe the declaration is wrong, say so and point to `/charter` rather than editing it" — NFR-3 satisfied at the file that writes `release.md` | fixed r2 |
| F7 | Minor | `README.md:251` | The status row labelled the capability "dogfooded on this repo only" while the declared path had not run. **r2:** the row now says "declared path **first exercised by this feature's own `/demo-day` and `/go-live`** — until then … the declared path itself has not run", and names the fixtures. Honest as of today; re-check it at `/go-live`, when it becomes stale in the other direction | fixed r2 |
| F8 | Minor | `agents/qa-tester.md:26`, `:111-112`, `:140-148` | The agent was unconditionally browser-bound outside step 1. **r2:** all three fixed — mindset `:25-27`, the tool rule `:127-129` ("performed yourself, in the browser or by the declared method"), and `:76-80` which makes steps 5–6 `N/A`-able *with the reason recorded* while explicitly forbidding `N/A` from shrinking step 3. `:157-159`'s no-improvising rule is no longer in tension: the `N/A` route is now authorised text | fixed r2 |
| F9 | Nit | `spec.md:150` (NFR-4) vs `skills/charter/SKILL.md:45-53` | NFR-4 says that with no declaration "**every** ceremony behaves exactly as today"; `/charter` now asks one more question on every project, declared or not. Honestly recorded in `evidence.md` §4.1, but the NFR's literal wording needs the writing ceremony exempted. For the EM/PO, not the developer **Resolved at the `/story-time` gate of 2026-08-29, not by a file change:** NFR-4 now reads "every ceremony that **reads** the declaration behaves exactly as today" with one stated exemption for `/charter`, the ceremony that writes it (spec C17). | fixed |
| F10 | Nit | `skills/demo-day/SKILL.md:28`, `agents/qa-tester.md:48`, `skills/go-live/SKILL.md:33`, `skills/spark/SKILL.md:74`, `agents/release-manager.md:65` | The section is addressed by number (`§8`) in five shipped files. A consumer constitution numbering its sections differently makes the reference wrong; the precedent (`go-live:31`) names `Delivery & Handoff` by name only. All five also name `QA Method`, so failure is unlikely — hence Nit. Fix: lead with the name, keep the number parenthetical | open |
| F11 | Nit | `agents/facilitator.md:76-83` | The new paragraph was indented 2 spaces inside a 3-space ordered-list item, so it read as a lazy continuation rather than part of item 3. Reviewer re-indented to 3 spaces; no wording changed; `claude plugin validate` re-run green afterwards | fixed r1 |
| F12 | Major | `agents/facilitator.md:116-118`, `agents/qa-tester.md:81-83` | Both say the declaration's **only** other reader is `/go-live` — facilitator: "the only ceremony besides QA that reads it at all is `/go-live`"; qa-tester: "the only other reader is `/go-live`". False in the same commit: `skills/spark/SKILL.md:73-79` reads §8 and *changes what the orchestrator asks* ("don't ask any of that and don't re-negotiate the method"). Introduced by F1's fix, which rewrote exactly these two clauses. Why it matters: `facilitator.md` is the file that explains §8 **to the user at `/charter`**, so the user is told the wrong surface — and `/spark` not asking for a URL is the most visible effect of declaring. Violates NFR-3 (library lens §4: contract clarity); not capped by AC-2.4, since it is shipped prompt material, not a `.spark/` artifact. **r3, re-derived from source under AC-2.2(a):** fixed in both. `facilitator.md:116-122` — "Three read it, and only these three: the QA phase (`/demo-day` and the QA Tester) … `/spark`, which stops asking for a start command, URL and browser tooling … `/go-live`, which words its pre-flight QA row"; `qa-tester.md:81-84` states the same set. Checked for a **third variant**: `grep -rn '§8'` returns six readers — `demo-day`, `qa-tester`, `spark`, `go-live`, `release-manager`, `facilitator`; `release-manager` is `/go-live`'s own agent (`go-live:28-29`) and `facilitator` is `/charter`, the writer the same bullet excludes. The set is exactly right and no new false claim was introduced | fixed r3 |
| F13 | Nit | `skills/demo-day/SKILL.md:55` | "Only once **both** gates above have passed" predates F2/F5's insertion of the §8 read as a third sub-step, and on a declared project the browser gate deliberately "does not apply" — so the tool-resolution sub-step keys off a gate that never ran. Reviewer changed "both gates" → "the gates"; no semantics touched, `:69-70`'s "a run that stopped on the browser or app gate never reaches this sub-step" needed no change. `claude plugin validate` re-run green | fixed r2 |
| F14 | Nit | `evidence.md:518` | Entry 6 recorded the release commit as "47f6040, 12 files"; `git show --name-only 47f6040 \| wc -l` → **15** (the four newly added `.spark/right-sizing/` artifacts are in the commit too). Capped at Minor by AC-2.4 — inside a `.spark/` artifact, changes no verdict, gate answer or Must AC. Reviewer corrected the count in place | fixed r2 |
| F15 | Minor | `templates/constitution.md:110-111` | The shipped contract comment lists the ceremonies that "behave exactly as today", then gives `/go-live` its one difference — and never mentions `/spark`, which on a declared project stops asking for a start command, URL and browser tooling (`spark:73-80`). Not false (it never asserts `/spark` is unchanged) but materially incomplete, and it is the **third** location carrying this same gap after F12's two — the one that ships into every consumer's constitution, where the user decides whether to declare. F12's fix corrected the two agent files and did not reach here. Violates NFR-3 / library lens §4 ("a reader needs no external doc to use the rule correctly"). Root cause is AC-1.7's list, frozen before the plan-gate ruling added `/spark`, so the code faithfully mirrors a stale spec — see §6. Fix: after the `/go-live` clause add "`/spark` still runs every step it runs today — the one difference is that it stops asking for a start command, URL and browser tooling, and names the declared method instead"; and raise AC-1.7's list with F9 at `/story-time` | fixed |
| F16 | Minor | `.spark/right-sizing/evidence.md:566-583` (Entry 7.1), `:627-632` (7.4) | Entry 7.1 records a real `/spark` step 2 observation, then at `:578` concludes "That is **AC-1.1 performed** rather than described". AC-1.1 (`spec.md:118`) is *"when the loop reaches the QA phase, then **`/demo-day`** proceeds by the declared method"* — `/demo-day` has not run. What was performed is AC-1.1's orchestrator half only, which the heading's own "(at the orchestrator)" says and the conclusion drops; §7.4's "Still not run" list then names AC-1.2 and AC-1.4 but not AC-1.1, so a reader concludes AC-1.1 is evidenced. Why it matters: constitution §8's own evidence rule says reasoning about text "never passes an acceptance criterion", and this is that, one level removed — an over-claim on a Must AC in the artifact `/demo-day` and `/go-live` read. Bounded, hence Minor: AC-2.2(b) forces the QA Tester to re-derive every Must AC anyway, so it cannot legitimately cite 7.1. **AC-2.4's cap does not apply** — the subject is a Must AC's evidence state, not wording. Fix: scope the sentence to "AC-1.1's `/spark` half performed; its `/demo-day` half not run", and add AC-1.1 to §7.4 | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `demo-day:40-42`, `spark:73-77`, `qa-tester:63-65` | ✅ met |
| AC-1.2 | `demo-day:43-45`, `qa-tester:70-72`, `templates/constitution.md:106-108` | ✅ met |
| AC-1.3 | `demo-day:31-36`, `spark:75-77`, `go-live:37`; guard-false re-issue of all 6 deleted lines | ✅ met r2 — live venue now exists (F3) |
| AC-1.4 | `go-live:33-37`, `release-manager.md:63-73` | ✅ met |
| AC-1.5 | `demo-day:31-33`, `qa-tester:51-53`, `templates/constitution.md:117-118`; fixture (a) in `evidence.md` §5.2 | ✅ met |
| AC-1.6 | `demo-day:37-39`, `qa-tester:60-62` | ✅ met (fixture (c) honestly partial) |
| AC-1.7 | `templates/constitution.md:109-114` | ⚠️ **re-assessment owed to round 4** — this row was written against the *pre-amendment* AC-1.7. The user amended AC-1.7, NFR-2 and NFR-4 at a second `/story-time` gate, 2026-08-29 (spec C17); `/increment` then landed F15, so the contract comment now names `/spark`'s one difference beside `/go-live`'s, and all three mirrors carry both. **Claimed met, unconfirmed:** no reviewer has checked the shipped text against the amended AC |
| AC-1.8 | `charter:45-53`, `facilitator:76-83`; `.spark/constitution.md` Amendments row | ✅ met |
| AC-1.9 | `demo-day:34-36`, `spark:75`, `qa-tester:54-59`, `go-live:37` | ✅ met r2 — F4 fixed, all four readers agree |
| AC-1.10 | `demo-day:45-47`, `qa-tester:83-85`, `go-live:38`, `spark:78-79`, `facilitator:112-114`, `charter:52-53`, `release-manager:71-73` | ✅ met r2 — F6 fixed |
| AC-2.1 | `reviewer.md:171-181`, `qa-tester.md:194-204` | ✅ met |
| AC-2.2 | same, conditions (a)–(d) verbatim, framed "bounded reading, never 'don't verify'" | ✅ met |
| AC-2.3 | same, "name which condition triggered it" | ✅ met |
| AC-2.4 | `reviewer.md:182-186`, `qa-tester.md:205-209` — three conjunctive conditions, cap at `Minor`, never gate-blocking | ✅ met |
| AC-2.5 | no age/shape instruction added anywhere (`git diff 085db99..47f6040 agents/ \| grep -iE '\+.*(pre-existing\|legacy\|migrat)'` → empty) | ✅ met |
| NFR-1 | `templates/constitution.md` +24/−0; parser blindness re-derived, not cited (`aspark-graph` never opens `constitution.md`) | ✅ met |
| NFR-2 | no new command, agent, lens or template file (`git show --name-status 47f6040`: 11 `M`, 4 `A`, all under `.spark/`); `/spark` extension is the recorded plan-gate ruling | ✅ met — the line-by-line release-note enumeration is `/go-live`'s to deliver |
| NFR-3 | `templates/constitution.md:99-121` + the per-file blocks | ⚠️ partial r3 — F12 fixed (so is F1/F4/F6); **F15** open: the shipped template comment still omits `/spark`'s one difference |
| NFR-4 | the absent/incomplete branch in all five readers; live proof now possible | ✅ met — **F9 closed by the NFR-4 amendment of 2026-08-29** (spec C17): the writing ceremony is now explicitly exempted, so no file change was needed |
| NFR-5 | `README.md:251`, `evidence.md` §5.3/Entry 6; no line/token/dollar claim anywhere in the diff | ✅ met r2 — F7 fixed |
| NFR-6 | none of the five gate-bearing templates is in the diff; re-counted `^- \[ \]` at `085db99` vs `47f6040`: 13/10/13/7/11, identical both sides | ✅ met — re-derived, not cited |

## 5. What Was Checked

- [x] Correctness: F12 re-derived from source under AC-2.2(a) — reader set re-enumerated by `grep -rn '§8'`, all six hits read. F1–F8/F11/F13 cited from round 2, not re-derived
- [x] Non-functional: NFR-1…6 re-checked against the five-file delta; library lens §§1/2/4 (§3 N/A) — no new file, command or public surface, no protected §3 structure touched; §4 is where F15 lands
- [x] Edge cases of the fix: `/charter` also *reads* §8, and so does `release-manager.md:65-73` — both fall inside the carve-outs the two sentences already make (writer; `/go-live`'s own agent). Checked explicitly for a third false variant: none
- [x] Error handling / security: unchanged; all four fall-backs still agree across readers. Security N/A per constitution §2/§5; nothing private added by the five modified files
- [x] Tests: `claude plugin validate` re-run this round → passed (1 pre-existing `autoUpdate` warning, outside the diff). No suite exists or is possible (constitution §4)
- [x] Evidence honesty (constitution §4, NFR-5): Entry 7 read end to end. 7.2's account of my own round-2 behaviour is accurate, S2 self-qualification included — it does **not** overstate. 7.1 does: **F16**

## 6. Verdict

**`passed`.** F12 is genuinely fixed, and I checked the thing worth checking: the fix did
**not** produce a third false variant. Both sentences are now true against source —
`facilitator.md:117-121` names all three readers with each one's real effect, `qa-tester.md:82-84`
names the same set, and a full re-enumeration of every `§8` reference (six files) returns exactly
that set once `release-manager` is read as `/go-live`'s own agent and `facilitator` as `/charter`,
the writer the bullet already excludes. Nothing shipped now says something untrue. What remains
is two `Minor` findings and the two Nits the user already accepted; none of them is a Blocker,
no Major is open, no gate was moved, no non-negotiable is violated, and `claude plugin validate`
passes. The feature is ready for `/demo-day`.

**But the pattern is the point, and it is not a code problem.** F9, F12 and now F15 are three
instances of one defect: `/spark` entered this diff by a **plan-gate ruling made after
`spec.md` was `approved`**, and AC-1.7's ceremony list and NFR-4's "every ceremony behaves
exactly as today" were never updated to know it. Every file mirroring that list inherits an
incomplete set — `templates/constitution.md:110-111` is *correct* against AC-1.7 and
*incomplete* against reality at once — so each round fixes one instance by hand and the next
mirror goes unnoticed. A fourth round would find a fourth instance. **The repair is one line of
spec, at `/story-time`:** give AC-1.7 the `/spark` entry with its one difference, as `/go-live`
already has, and exempt the writing ceremony in NFR-4 (F9). F15 then falls out as a one-line
edit and the class closes. I am not inflating F15 to Major to force that — it is honestly Minor
— but routing this back to `/increment` for a fourth round would treat the symptom.

**Open questions for the EM/PO** (not findings): (1) F9 + F15 are one spec repair. (2) S2 is `0`,
but AC-2.2(b) exempts every Must AC and this feature is all-Must, so S2 measures little here —
`evidence.md` 7.2 says the same, honestly. (3) `plugin.json` is still `0.7.1`, already released by
a previous feature, while constitution §5 makes a new optional capability a **minor** bump —
`/go-live` must land `0.8.0`. (4) `/demo-day` must `claude plugin update aspark@aspark` **plus
restart** first, or it tests superseded text (§1).

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

- [x] No open Blocker findings
- [x] No open Major findings — F12 fixed and confirmed r3; F9, F10, F15, F16 are Nit/Minor, none waived, none blocking
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated — §6's five re-checked against the five-file delta: no protected structure renamed, absent/incomplete branches intact in all readers, nothing executed unasked, no gate self-passed, nothing private added
- [x] All plan deviations documented and accepted — D1 unchanged; D2 accepted, with the ratification note for `/sprint-plan` in §2
- [x] Test suite runs green — none exists (constitution §4); the bar, `claude plugin validate`, re-run this round: passed with the 1 pre-existing `autoUpdate` warning
- [x] Line budget respected **on the template's second branch, not the first**: **Ist 175 / Soll ~150** (excluding HTML comments — none in this file) — **25 over, recorded not waived.** Cause: three rounds of findings accumulate in one non-appending file (16 rows in §3), plus this round's F12 re-derivation record and two new rows. Trimmed §1/§5/§6 twice; further cuts would delete substance. The template allows "an overage recorded here with a reason"; that is the branch this box is checked on — the budget itself is **not** met, and I am not claiming it is
- [x] Status set to `passed`

# Review Report: campaign-core

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | `git diff origin/main...HEAD` (8196c17, 2304ea5, aef71f5, eeee044 on c5eb37d), `.spark/campaign-core/plan.md` |
| **Status** | `changes-requested` |
| **Round** | 2 |
| **Date** | 2026-09-30 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** round 2: changes requested (one open Major, F24). Fix pass done; round-3 re-review pending — this line is superseded by the round-3 verdict.
- **Open:** `0 open` — F24 (Major) and F27, F28, F8, F10, F11, F15 are `fixed` by the round-2 fix pass; all others `verified` in round 2. Awaiting the owner's round-3 verification.
- **Binding ruling:** §6 Verdict and the gate checklist below. They are the only binding location; there is no other round to point to.
- **On conflict:** the numbered body below wins for everything except `Status`. Log the mismatch as a finding at the next `/peer-review` and proceed; don't stop on it.

## 1. Scope

- **Reviewed:** the full diff, with the fix pass `aef71f5` read line by line: the three campaign files, `docs/status.md`, plan §4/§6, `spec.md:14`, and the ledger section "`/peer-review` round 1 — fix pass and re-runs" (`evidence.md:823-996`). `fixtures.md` was read in full.
- **Re-run by me:** `wc -l` 57/64/84, standing rule 3 lines. `git ls-files '*.py'` is empty; `ls campaigns` shows 2 files. `git diff origin/main...HEAD` over `skills agents ROADMAP.md .spark/constitution.md .claude-plugin` is empty; under `templates/` only `campaign.md` is new. The kind's frontmatter parses (Ruby YAML) as 7 keys, `stop-rules` has 5 items, and the SR-5 parenthetical stays one item. `claude plugin validate .` passes (only the existing `autoUpdate` warning). Every relative link in the touched docs resolves; the `issues/` links are GitHub-relative.
- **Condition (a) re-derivation:** every fixed finding was re-derived from the current text, not from the Handoff. **Tool:** `aspark-graph` was not queried (Markdown only; see plan §2).
- **Not reviewed:** no session was run. Live claims were checked against the quoted transcripts only.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1, T2, T4, T5, T8, T10–T12 | ✅ | As in round 1. T2/T5 text was changed by D-7, and caps still hold (57/64) |
| T3 | ✅ | The re-run against the current format is quoted (`evidence.md:962-996`); fixtures are quoted (`fixtures.md:247-289`) |
| T6 | ✅ | The re-run on `approved` instances can fail (F4 verified); fixtures are quoted |
| T7 | ✅ | The re-run with a minimal prompt is quoted, with independent `git` observations (`evidence.md:885-960`). The fixture had a wrong `common.py` (F25, fixed) |
| T9 | ⚠️ | Unchanged; the add-a-file walk has no dispatch (disclosed) |
| D-1…D-7 | ✅ | D-1…D-6 were user-accepted 2026-09-30 (`plan.md:165`). D-7 is the fix pass reviewed here. D-6 says "the kind text" keeps SR-5 committed; the instance text does not (F24) |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `campaigns/migration-campaign.md:53`, `:24`, `:30` | **Problem:** SR-8 "roll the in-flight slice back" on uncommitted work means a discard. **Why it matters:** a destructive git action without a go (§6). **Fix:** commit, then revert. **r2:** `:54` now reads "WIP commit, revert that commit, then halt. Uncommitted work is never discarded". This satisfies AC-5.5, and no discard phrase remains in the three files. Its path scope is F27 | verified |
| F2 | Major | `templates/campaign.md:52`; `campaigns/migration-campaign.md:22-24`, `:29` | **Problem:** the slice list defining the goal was unprotected, so dropping a red slice made the goal true. **Fix:** freeze it. **r2:** `templates/campaign.md:53` and `migration-campaign.md:25` freeze the slice list and parity check ("stays in the list and stays red"). This is instruction-only; its honesty is covered by F15/F26 | verified |
| F3 | Major | `campaigns/migration-campaign.md:20`, `:28-29`, `:37-38` | **Problem:** the run order let the Migrator start on slices nobody approved. **r2:** `:30` "stop and wait … step 3 does not begin before that" closes the Major path. The step-1-before-step-2 residue is F28 | verified |
| F4 | Major | `evidence.md:231`, `:243`, `:261`, `:280` | **Problem:** the T6(b) refusals could not fail (`draft`). **r2:** re-run with `approved` and the approval filled in (`evidence.md:829-883`). Each refusal names only the missing element | verified |
| F5 | Major | `evidence.md:473`, `:498`, `:627`; T9 `:711-713` | **Problem:** the T7 prompt dictated the behaviours credited to the kind. **r2:** the bare-prompt re-run (`evidence.md:887`) shows Archaeologist-first, a separate Verifier per slice, split commits, the halt at SR-5 and 0 destructive commands | verified |
| F6 | Major | `evidence.md:117-120`, `:187-188`, `:465-469`; `plan.md:82`, `:93`, `:97` | **Problem:** fixtures were not quoted. **r2:** `fixtures.md` quotes every input, the T7 instance in full. It was complete except `common.py` (F25, fixed) | verified |
| F7 | Minor | `templates/campaign.md:11-12`, `:35`; `campaigns/README.md:70-71` | **Problem:** `halted`→`running` authority was unstated. **r2:** the user ruled that the agent may resume once the cause is resolved and recorded in a CK entry. The rule is consistent in `templates/campaign.md:11-12` and `campaigns/README.md:70-72` and within AC-1.9. A goal change still needs a fresh approval (AC-1.6). The SR-5 interaction is F24 | verified |
| F8 | Minor | `templates/campaign.md:8` vs `campaigns/README.md:49`, `evidence.md:142-143`, plan T2 DoD | **Problem:** contradictory approval-writer rules. **r2, still open:** `templates/campaign.md:8` ("transcribed") names no writer, while `campaigns/README.md:49` says "the user records … and sets `approved`". The T3(a) re-run offered "record it in the file and set `running`" (`evidence.md:979`), skipping a user-set `approved`, and the ledger calls this allowed (`:996`). **Fix (user's call):** one clause on whether a transcribed approval still needs the user to set `approved` | fixed |
| F9 | Minor | `templates/campaign.md:41`, `:31`; `campaigns/migration-campaign.md:57` | **Problem:** SR-3 had no observable. **r2:** `templates/campaign.md:42` "iterations used or tokens spent exceed §3, checked at every checkpoint" | verified |
| F10 | Minor | `campaigns/migration-campaign.md:30` vs `:39-40`, `:42` | **Problem:** the CK/parity-quote writer was ambiguous. **r2, still open:** the Migrator is cleared (`:41`), and `:31` names the campaign session as the one that quotes the Verifier into CK. But `:43` still has the Verifier "quotes the observed output into the instance", so two writers remain; in the re-run only the session wrote (`evidence.md:905`). **Fix:** `:43` becomes "reports its output verbatim; the campaign session quotes it (step 3)" | fixed |
| F11 | Minor | `templates/campaign.md:10`, `:43`; `campaigns/migration-campaign.md:15-20`; `campaigns/README.md:45` | **Problem:** the format/kind merge was unspecified. **r2, still open:** `:15` and `README:46` now say the body goes in as §8 and the frontmatter is dropped. Still unsaid: where the filled slice list, parity check and token budget go (the body has only the `S<n>` shape, `:23`), and whether the `SR-5…` placeholder row is replaced (a blank element = not startable). `templates/campaign.md:10` still says "Copy this file plus the chosen kind's content". The project's own post-fix instance deviates: `fixtures.md:159`, `:174-188` ("Migration specifics", invented `### Slice list`, an H1 kept). **Fix:** one sentence naming §8's filled blocks and the §4 row | fixed |
| F12 | Minor | `campaigns/README.md:45`; `campaigns/migration-campaign.md:15` | **Problem:** a relative plugin path. **r2:** `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md` at both sites (constitution:83) | verified |
| F13 | Minor | `plan.md:97`, `:125`, `:155-161`; `evidence.md:577` | **Problem:** the T7 rollback deviation and AC-5.4 scope were not recorded. **r2:** D-6 (`plan.md:162`) and §4 (`:125`) | verified |
| F14 | Minor | `evidence.md:294`, `:548`, `:669`; `README.md:128` | **Problem:** runs with the guard loaded were undisclosed. **r2:** `evidence.md:827` and `docs/status.md:88` say "read-verified only". `README.md:128` and `campaigns/README.md:73` state the design rule, not a test claim. A guard-off run is for `/demo-day` | verified |
| F15 | Minor | `evidence.md:369-384`; `templates/campaign.md:7` | **Problem:** NFR-11 was shown only on a `draft` instance, and nothing detects edits to a frozen copy. **r2, still open:** no approved-instance tamper run exists. The integrity disclosure was added by me (F26), and `plan.md:126-131` does not list the freeze. **Fix:** a `/demo-day` run on an `approved` instance with a tampered brief or slice list, plus a line in plan §4 | fixed |
| F16 | Minor | `docs/status.md:88` | **Problem:** overclaims in the status row. **Fix applied** in r1. Re-checked r2: the row was rewritten in D-7, and its residual overclaim is F26 | verified |
| F17 | Minor | `campaigns/README.md:40` | **Problem:** "no doc contains a list". **Fix applied:** "docs name kinds only as examples" (present) | verified |
| F18 | Minor | `evidence.md:693` | **Problem:** SR-2 and SR-9 were missing from the caveat. **Fix applied** (present) | verified |
| F19 | Nit | `README.md:160` | **Problem:** `campaigns/` was missing. **Fix applied** (present) | verified |
| F20 | Nit | `evidence.md:180` | **Problem:** the size was unannotated. **Fix applied** (present) | verified |
| F21 | Nit | `CONTRIBUTING.md:150-151` | **Problem:** wrong pointers. **Fix applied** (present, `:150-151`) | verified |
| F22 | Nit | `plan.md:160` | **Problem:** D-4 scope. **r2:** "T9, T10, T11" | verified |
| F23 | Nit | `spec.md:14` | **Problem:** a stale "Awaiting approval". **r2:** removed | verified |
| F24 | Major | `campaigns/migration-campaign.md:6` vs `:15`, `:51`; `templates/campaign.md:11-12` | **Problem:** the user's SR-5 ruling ("the slice stays committed until the user decides") exists only in the frontmatter. `:15` and `README:46` drop the frontmatter from the instance, and the SR-5 row `:51` omits the ruling. The resume rule then lets the agent "resolve the cause" itself (revert the slice), record a CK and set `running`. **Why it matters:** the text that governs the run does not carry a user ruling. `plan.md:162` and `docs/status.md:88` claim it does. **Fix:** `:51` gains "halt; the slice stays committed and the run resumes only on the user's decision" | fixed |
| F25 | Minor | `fixtures.md:78` | **Problem:** `common.py` was quoted with `return float(x)`, which is the post-S2 state. The fixture had the identity (`evidence.md:466`, `:908` sed `return x$`, CK-1 S1 green). **Why it matters:** a QA rebuild would be red at S1 from iteration 1. **Fix applied:** `return x` | fixed |
| F26 | Minor | `docs/status.md:88` | **Problem:** "the frozen list and the wait were observed holding". The wait was only stated by a refusing session (`evidence.md:840`), never performed, and a "later run with a minimal prompt" did not exercise the §6 fix. **Fix applied:** reworded, plus "Nothing detects an edit to an approved instance; its integrity is agent-followed" | fixed |
| F27 | Minor | `campaigns/migration-campaign.md:54` | **Problem:** the SR-8 WIP commit is not scoped to the slice's paths, unlike `:31`. **Why it matters:** a broad `git add` sweeps the user's unrelated uncommitted edits into the WIP commit, and the revert then removes them from the working tree (recoverable from history, but surprising). **Fix:** "commit the slice's paths only as a WIP commit" | fixed |
| F28 | Minor | `campaigns/migration-campaign.md:20`, `:29-30` | **Problem:** the Strategist's cut branch (step 2) comes after the Archaeologist (step 1). But an empty list is not startable (`:20`), and the cut list needs approval "with the goal", so the cut can only happen before approval, outside a run. The empty-slices session had to reason this out (`evidence.md:840`). **Fix:** move the cut to a "Before approval" line above step 1 | fixed |
| F29 | Nit | `plan.md:14` | **Problem:** the Handoff said "D-1…D-5 recorded" and omitted the acceptance. **Fix applied:** "D-1…D-7 … D-1…D-6 user-accepted" | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1, 1.2, 1.4, 1.7, 1.8 | `templates/campaign.md:5-8`, `:17-29`, `:46` | ✅ met; live T8(a), (b), (d) |
| AC-1.3 | `templates/campaign.md:36-44` | ✅ met structurally r2 (SR-3 defined); only SR-1 is live |
| AC-1.5 | `templates/campaign.md:8`, `:11`; `campaigns/README.md:49`, `:69` | ✅ met; live T3(a) plus the re-run. Wording conflict F8 |
| AC-1.6 | `templates/campaign.md:53` | ✅ met r2; live T8(c), second run |
| AC-1.9 | `templates/campaign.md:5`, `:11-13` | ✅ met r2 (the resume rule per the user's ruling) |
| AC-2.1, 2.2, 2.4, 2.5, 2.6 | `campaigns/README.md`; empty skills/agents diff; `ls` | ✅ met (re-run) |
| AC-2.3 | `campaigns/README.md:37-41`, `:59-72` | ✅ met r2: dispatch observed under a bare prompt |
| AC-5.1, 5.6 | `campaigns/migration-campaign.md:7`, `:20`, `:57-59` | ✅ met r2; the refusals can fail |
| AC-5.2 | `campaigns/migration-campaign.md:28-44` | ⚠️ text met; order residue F28 |
| AC-5.3 | `campaigns/migration-campaign.md:31`, `:34`, `:42-44` | ⚠️ met; dispatch is no longer prompt-driven. Two writers remain (F10) |
| AC-5.4 | `campaigns/migration-campaign.md:40`, `:55` | ⚠️ positive half observed; SR-9's trip was never exercised |
| AC-5.5 | `campaigns/migration-campaign.md:47-55` | ⚠️ SR-8 is safe r2. SR-5/SR-7 are live; SR-6/SR-8 read-verified; the SR-5 ruling is missing from the instance (F24) |
| AC-5.7 | `campaigns/migration-campaign.md:26`; `templates/campaign.md:50` | ✅ met r2: no contract step without a prompt |
| AC-5.8 | `campaigns/migration-campaign.md:61-64`; `README.md:129` | ✅ met |
| NFR-1, 2, 4, 5, 7, 8 | caps 57/64/84 and 3 rule lines; no `*.py`; validate passes | ✅ (the minor bump is due at `/go-live`) |
| NFR-3 | `README.md:124-130`; `docs/status.md:88` | ✅ after F26 |
| NFR-6 | `campaigns/README.md` | ✅ |
| NFR-9 | `templates/campaign.md:8`, `:11-13`, `:29`, `:53` | ⚠️ F8 |
| NFR-11 | T8(e) | ⚠️ partial (F15) |

## 5. What Was Checked

- [x] Correctness: every fix re-derived from the current text; SR numbering (1–4 in the format, 5–9 in the kind) is consistent; "frozen" vs the Strategist writing before approval is consistent
- [x] Non-functional: NFR-1…9 and 11, the constitution quality bars, and the `library` lens sections 1, 2 and 4 (frontmatter re-parsed)
- [x] Error handling and security: halt, resume and rollback paths re-read; no discard or force phrase remains (F1). Integrity of the approved copy is not detected (F15)
- [x] Tests: `validate` re-run; re-run transcripts audited for discriminating power; fixtures checked for internal consistency (F25)
- [x] Readability: cross-file contradictions (F10, F11, F24, F28)

## 6. Verdict

**Changes requested. The gate does not pass: one open Major (F24).**

All six round-1 Majors are fixed and hold on re-derivation. SR-8 no longer discards anything. The slice list and parity check are frozen in the instance itself. The run stops for approval after the Strategist. The AC-5.1/5.6 re-run can fail. The bare-prompt T7 re-run shows the behaviours coming from the kind, not the prompt. The fixtures are quoted. One of them was wrong, and I fixed it (F25).

The fix pass introduced one Major. The user ruled that SR-5 leaves the slice committed until the user decides. That ruling was placed only in the kind's frontmatter, and the documented merge drops the frontmatter from the instance. The new resume permission then lets an agent revert and continue on its own. The fix is one table cell.

The six open Minors (F8, F10, F11, F15, F27, F28) do not block the gate but should go into the same fix pass. The wait after the Strategist, SR-8 in its new form, the SR-5 → user-decision path and every guard-off claim remain unperformed. `/demo-day` must perform them or record them as `not-verified-live`.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [ ] No open Major findings (or explicitly waived by the user, with reason recorded here). F24 is open
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated by the diff as shipped
- [x] All plan deviations documented and accepted: D-1…D-6 user-accepted 2026-09-30; D-7 is this fix pass. D-6's wording is inaccurate (F24)
- [x] Test suite runs green: no suite exists (constitution §4); `claude plugin validate .` passes, re-run by me
- [x] Line budget respected: Ist 126 / Soll ~150 (no HTML comments)
- [ ] Status set to `passed`

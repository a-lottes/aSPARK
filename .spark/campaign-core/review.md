# Review Report: campaign-core

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | `git diff origin/main...HEAD` (8196c17 … 3a9fbc9 on c5eb37d); r5: `git diff 7d28a5e..398f202` (QA fix passes a57ea0d, a3d2a47, 398f202), `.spark/campaign-core/plan.md` |
| **Status** | `passed` |
| **Round** | 5 |
| **Date** | 2026-09-30 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** round 5: passed. The QA-driven text (plan D-8…D-10) has no Blocker or Major; the changed rules do not contradict each other on role play, baseline run, status-setting or refusal. Two stale counts in `docs/status.md:88` fixed by me (F35).
- **Open:** F34, F36 (Minor), F37, F38 (Nit), F39 (Minor, qa.md), F40 (Nit, ledger). None blocks the gate. F1–F33 stay `verified`.
- **Binding ruling:** §6 Verdict and the gate checklist below. They are the only binding location; there is no other round to point to.
- **On conflict:** the numbered body below wins for everything except `Status`. Log the mismatch as a finding at the next `/peer-review` and proceed; don't stop on it.

## 1. Scope

- **Reviewed (r5, narrow):** only `git diff 7d28a5e..398f202`: `templates/campaign.md:10-17`, `:22`, `:32`; `campaigns/migration-campaign.md:23`, `:26`, `:34`, `:44`, `:53`; `campaigns/README.md:22`, `:46`, `:67-68`, `:75`; `README.md:129`; `docs/status.md:88`; `plan.md:165-169`; `evidence.md:1142-1149`; `qa.md` read in full as the source for every doc claim (condition (b): AC-2.1/AC-5.4 wording re-derived). Earlier QA rounds read at `a57ea0d`/`a3d2a47` for the guard-less runs.
- **Re-run by me (r5):** `wc -l` 60/87/64 (format exactly at cap 60; README 87, ledger says 86 — README gained `:22` in 398f202), standing rule 3. `git ls-files '*.py'` empty; `ls campaigns` 2 files; after `git fetch`, `git diff origin/main...HEAD` over `skills agents ROADMAP.md .spark/constitution.md .claude-plugin` empty; under `templates/` only `A templates/campaign.md`. `claude plugin validate .` passes (only `autoUpdate`). **Tool:** `aspark-graph` not queried (Markdown only). Status row `docs/status.md:88`: 3 pipes, one row. New relative links resolve (`qa.md`, `evidence.md`).
- **Not reviewed:** I ran no session. Live claims were checked against the quoted transcripts only.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1, T2, T4, T5, T8, T10–T12 | ✅ | As in round 1. T2/T5 text was changed by D-7 (rounds 1–3); caps still hold (58/64/85) |
| T3 | ✅ | The re-run against the current format is quoted (`evidence.md:962-996`); fixtures are quoted (`fixtures.md:247-289`) |
| T6 | ✅ | The re-run on `approved` instances can fail (F4 verified); fixtures are quoted |
| T7 | ✅ | The re-run with a minimal prompt is quoted, with independent `git` observations (`evidence.md:885-960`). The fixture had a wrong `common.py` (F25, fixed) |
| T9 | ⚠️ | Unchanged; the add-a-file walk has no dispatch (disclosed) |
| D-8…D-10 | ✅ | r5: the QA fix passes and the user's rulings (B4, B9, B14, B15, B16, AC-2.1/AC-5.4 partials) are recorded (`plan.md:165-169`). D-9 still says B14 "stays open"; D-10 supersedes it |
| D-1…D-7 | ✅ | D-1…D-6 were user-accepted 2026-09-30 (`plan.md:166`). D-7 (`plan.md:164`, now covering rounds 1–3) is the fix pass reviewed here. D-6's SR-5 wording is now true of the instance text (`migration-campaign.md:51`) |

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
| F8 | Minor | `templates/campaign.md:8` vs `campaigns/README.md:49`, `evidence.md:142-143`, plan T2 DoD | **Problem:** contradictory approval-writer rules. **r2, still open:** `templates/campaign.md:8` ("transcribed") names no writer, while `campaigns/README.md:49` says "the user records … and sets `approved`". The T3(a) re-run offered "record it in the file and set `running`" (`evidence.md:979`), skipping a user-set `approved`, and the ledger calls this allowed (`:996`). **r3:** `templates/campaign.md:8` and `campaigns/README.md:49` now agree: the agent may transcribe on the user's instruction, "only the user sets `approved`". Consistent with AC-1.5 and NFR-9 | verified |
| F9 | Minor | `templates/campaign.md:41`, `:31`; `campaigns/migration-campaign.md:57` | **Problem:** SR-3 had no observable. **r2:** `templates/campaign.md:42` "iterations used or tokens spent exceed §3, checked at every checkpoint" | verified |
| F10 | Minor | `campaigns/migration-campaign.md:30` vs `:39-40`, `:42` | **Problem:** the CK/parity-quote writer was ambiguous. **r2, still open:** the Migrator is cleared (`:41`), and `:31` names the campaign session as the one that quotes the Verifier into CK. But `:43` still has the Verifier "quotes the observed output into the instance", so two writers remain; in the re-run only the session wrote (`evidence.md:905`). **r3:** `:43` "reports the observed output verbatim (the campaign session copies it into the instance)"; one writer left, matching `:31` | verified |
| F11 | Minor | `templates/campaign.md:10`, `:43`; `campaigns/migration-campaign.md:15-20`; `campaigns/README.md:45` | **Problem:** the format/kind merge was unspecified. **r2, still open:** `:15` and `README:46` now say the body goes in as §8 and the frontmatter is dropped. Still unsaid: where the filled slice list, parity check and token budget go (the body has only the `S<n>` shape, `:23`), and whether the `SR-5…` placeholder row is replaced (a blank element = not startable). `templates/campaign.md:10` still says "Copy this file plus the chosen kind's content". The project's own post-fix instance deviates: `fixtures.md:159`, `:174-188` ("Migration specifics", invented `### Slice list`, an H1 kept). **r3:** `templates/campaign.md:10` and `migration-campaign.md:15` now name §8's filled blocks and the replacement of the `SR-5…` row (`templates/campaign.md:44`, same ID). `README.md:46` lags (F32); the token-budget copy is F30 | verified |
| F12 | Minor | `campaigns/README.md:45`; `campaigns/migration-campaign.md:15` | **Problem:** a relative plugin path. **r2:** `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md` at both sites (constitution:83) | verified |
| F13 | Minor | `plan.md:97`, `:125`, `:155-161`; `evidence.md:577` | **Problem:** the T7 rollback deviation and AC-5.4 scope were not recorded. **r2:** D-6 (`plan.md:162`) and §4 (`:125`) | verified |
| F14 | Minor | `evidence.md:294`, `:548`, `:669`; `README.md:128` | **Problem:** runs with the guard loaded were undisclosed. **r2:** `evidence.md:827` and `docs/status.md:88` say "read-verified only". `README.md:128` and `campaigns/README.md:73` state the design rule, not a test claim. A guard-off run is for `/demo-day` | verified |
| F15 | Minor | `evidence.md:369-384`; `templates/campaign.md:7` | **Problem:** NFR-11 was shown only on a `draft` instance, and nothing detects edits to a frozen copy. **r2, still open:** no approved-instance tamper run exists. The integrity disclosure was added by me (F26), and `plan.md:126-131` does not list the freeze. **r3:** an `approved` instance with a planted §9 was not followed and was reported (`evidence.md:1087-1135`, one run). `plan.md:131` lists the freeze as instruction-only, and the ledger's Limit says detection does not exist. An edit to the approved slice list itself was not run (for `/demo-day`) | verified |
| F16 | Minor | `docs/status.md:88` | **Problem:** overclaims in the status row. **Fix applied** in r1. Re-checked r2: the row was rewritten in D-7, and its residual overclaim is F26 | verified |
| F17 | Minor | `campaigns/README.md:40` | **Problem:** "no doc contains a list". **Fix applied:** "docs name kinds only as examples" (present) | verified |
| F18 | Minor | `evidence.md:693` | **Problem:** SR-2 and SR-9 were missing from the caveat. **Fix applied** (present) | verified |
| F19 | Nit | `README.md:160` | **Problem:** `campaigns/` was missing. **Fix applied** (present) | verified |
| F20 | Nit | `evidence.md:180` | **Problem:** the size was unannotated. **Fix applied** (present) | verified |
| F21 | Nit | `CONTRIBUTING.md:150-151` | **Problem:** wrong pointers. **Fix applied** (present, `:150-151`) | verified |
| F22 | Nit | `plan.md:160` | **Problem:** D-4 scope. **r2:** "T9, T10, T11" | verified |
| F23 | Nit | `spec.md:14` | **Problem:** a stale "Awaiting approval". **r2:** removed | verified |
| F24 | Major | `campaigns/migration-campaign.md:6` vs `:15`, `:51`; `templates/campaign.md:11-12` | **Problem:** the user's SR-5 ruling ("the slice stays committed until the user decides") exists only in the frontmatter. `:15` and `README:46` drop the frontmatter from the instance, and the SR-5 row `:51` omits the ruling. The resume rule then lets the agent "resolve the cause" itself (revert the slice), record a CK and set `running`. **Why it matters:** the text that governs the run does not carry a user ruling. `plan.md:162` and `docs/status.md:88` claim it does. **r3:** `:51` carries the ruling ("stays committed … does not resume after `SR-5` until they have"). The frontmatter still parses as 7 keys and 5 items. T7d (`evidence.md:1056-1085`) refused "please continue", `HEAD` unchanged (one run). The general resume rule has no carve-out (F31, Minor) | verified |
| F25 | Minor | `fixtures.md:78` | **Problem:** `common.py` was quoted with `return float(x)`, which is the post-S2 state. The fixture had the identity (`evidence.md:466`, `:908` sed `return x$`, CK-1 S1 green). **Why it matters:** a QA rebuild would be red at S1 from iteration 1. **Fix applied:** `return x`. **r3:** present (`fixtures.md:78`); run 4 went green at S1 (`evidence.md:1041`) | verified |
| F26 | Minor | `docs/status.md:88` | **Problem:** "the frozen list and the wait were observed holding". The wait was only stated by a refusing session (`evidence.md:840`), never performed, and a "later run with a minimal prompt" did not exercise the §6 fix. **Fix applied:** reworded, plus "Nothing detects an edit to an approved instance; its integrity is agent-followed". **r3:** present; the new approved-instance and "continue" claims each match one ledger run | verified |
| F27 | Minor | `campaigns/migration-campaign.md:54` | **Problem:** the SR-8 WIP commit is not scoped to the slice's paths, unlike `:31`. **Why it matters:** a broad `git add` sweeps the user's unrelated uncommitted edits into the WIP commit, and the revert then removes them from the working tree (recoverable from history, but surprising). **r3:** `:54` "commit **the in-flight slice's own paths only** … Other uncommitted files are left alone and nothing is discarded". Text only; not run | verified |
| F28 | Minor | `campaigns/migration-campaign.md:20`, `:29-30` | **Problem:** the Strategist's cut branch (step 2) comes after the Archaeologist (step 1). But an empty list is not startable (`:20`), and the cut list needs approval "with the goal", so the cut can only happen before approval, outside a run. The empty-slices session had to reason this out (`evidence.md:840`). **r3:** `:30` "before approval, in a planning session, since an instance with an empty list is not startable". It kept the step-2 numbering rather than moving above step 1, but the timing is stated unambiguously | verified |
| F29 | Nit | `plan.md:14` | **Problem:** the Handoff said "D-1…D-5 recorded" and omitted the acceptance. **Fix applied:** "D-1…D-7 … D-1…D-6 user-accepted". **r3:** present (`plan.md:14`) | verified |
| F30 | Minor | `campaigns/migration-campaign.md:15`; `templates/campaign.md:10` vs `:32` | **Problem (new r3):** the merge rule puts the token budget under §8, while §3 already holds `Tokens`. The fixture carries both (`fixtures.md:147`, `:184-185`). **Why it matters:** two copies of one budget can diverge, and §6's freeze names §1–§3, the slice list and the parity check, not a §8 copy. **Fix:** drop "token budget" from the §8 list (it lives in §3). **r4:** `templates/campaign.md:10` and `migration-campaign.md:15` say it "stays in §3"; `README.md:46` lists only slice list and parity check. No §8 token-budget pointer remains: the kind's "Not startable" (`:20`) and Budget (`:58-59`, "as in the format's §3") name no section; §6 freezes §1–§3. The ledger (`evidence.md:1141`) and `fixtures.md:675` disclose that the runs carried a §8 copy and were not repeated; true of the round-2 runs and also of the T6 re-run (`evidence.md:872` cites both copies), which the ledger's "runs recorded above" covers | verified |
| F31 | Minor | `templates/campaign.md:11-12`; `campaigns/README.md:70-72` vs `migration-campaign.md:51` | **Problem (new r3):** the general resume rule ("after `halted` once the cause is resolved and recorded in a `CK-` entry") has no carve-out for a rule that reserves the decision to the user. SR-5 wins only by specific-over-general. **Why it matters:** this is the self-resume path F24 closed. The only evidence it holds is one run (T7d). **Fix:** add "unless the tripped rule reserves the decision to the user" at both sites (format 57 → ≤58). **r4:** present at `templates/campaign.md:12-13` and `README.md:71-72` ("as `SR-5` does"); with `:51` ("does not resume after `SR-5` until they have") no agent-resolved resume path remains. Goal/list changes still route through fresh approval (§6, AC-1.6); AC-1.9's status set is unchanged. No unqualified "resume once resolved" remains in the three files or `docs/status.md`. Residue, fail-closed: the format's clause alone does not say resume is allowed once the user *has* decided; the `SR-5` row does. Text only; not run | verified |
| F32 | Nit | `campaigns/README.md:46` | **Problem (new r3):** the contract still says "the kind's added stop rules extend §4". It names neither §8's filled blocks nor the `SR-5…` row replacement, and 0478363 did not touch this line, although the fix summary claims three sites. **Fix:** mirror `templates/campaign.md:10`. **r4:** `README.md:46` now names the slice list and parity check under §8 and the `SR-5…` row replacement; it agrees with `templates/campaign.md:10` and `migration-campaign.md:15`, no contradiction among the three | verified |
| F33 | Nit | `fixtures.md:675`, `:677` | **Problem (new r3):** the round-2 fixtures are described as deltas, not quoted. The §8 heading name and the new top comment are unstated, and the F15 fixture omits that `parity.py` is the three-slice one (`evidence.md:1122` prints S3). **Fix:** name the heading and the `parity.py` source. **r4:** `fixtures.md:675-679` names the §8 heading (`Migration specifics …`, not the rule's `"Kind-specific"`; nothing keys on it), the three-slice `parity.py` (matches `evidence.md:1122`), caps 5/3 (matches `:469`, `:1108`) and T7d's `HEAD` `99cb57d` (matches `:1058`). Sufficient for a rebuild | verified |
| F34 | Minor | `templates/campaign.md:32` vs `:13-14`, `campaigns/README.md:72-74`, `campaigns/migration-campaign.md:51` | **Problem (new r5):** "a stop rule … [is] not waivable and need[s] a changed, re-approved spec" read literally also covers continuing after *any* trip, while the resume rule lets the agent set `running` once the cause is resolved and recorded, and SR-5's revert option needs no fresh approval (QA `dec` resumed that way, `qa.md:55`). **Why it matters:** two rules for one situation; fail-closed (more restrictive), so no destructive path. **Fix:** "disabling a stop rule is not waivable; resuming after a trip follows the Status rule above" | open |
| F35 | Minor | `docs/status.md:88` | **Problem (new r5):** "every run had it loaded except one negative-case check, so … barely verified" contradicted the same row's "One full three-slice migration ran without `aspark-guard`" (guard-less: `negC` r1, `mign` r2 — `qa.md@a57ea0d:24`, `@a3d2a47:25`); "QA (two rounds, 33 rows)" while the row reports round 3. **Fix applied:** "except two sessions, one negative-case check and one full migration (below) … rests on those two runs"; "three rounds" | fixed r5 |
| F36 | Minor | `docs/status.md:88` ("Known limits") | **Problem (new r5):** "ran a check or committed a log entry out of order when a subagent could not run (observed twice in round 3)". Per `qa.md:100` (B16) only `dn3` had a denied subagent; the `mig` CK ordering slip was in a normal run. **Why it matters:** the disclosure narrows the condition, so a reader thinks normal runs keep order. **Fix:** "once ran the Archaeologist's tests itself when that subagent could not (`dn3`), and once committed a CK entry late in a normal run (`mig`)" | open |
| F37 | Nit | `templates/campaign.md:11-12` vs `campaigns/README.md:26` | **Problem (new r5):** "`name` (= the file name)" omits "without `.md`", and "if any is missing" does not cover a wrong `name`. QA read it as intended (`FPv`, `FPr`, `D`, `D2`, `qa.md:102`). **Fix:** "(= the file name without `.md`)", "missing or wrong". Not applied: this is the exact text QA measured at 13/19 | open |
| F38 | Nit | `campaigns/README.md:67-68` | **Problem (new r5):** "Observed meanwhile" states `/spark`, `/next-steps` and `/spark campaigns` behaviour without "one run, non-deterministic" (`qa.md:94`); `/spark campaigns` rests on round 1 only, and round 2's `/next-steps` pointed to `/charter` and named the directory rather than listing the campaign. **Fix:** add "(one run each, not guaranteed)" | open |
| F39 | Minor | `.spark/campaign-core/qa.md:110`, `:106` | **Problem (new r5):** §5 Verdict still reads "**Fail (not yet).**" while the header (`:8`), Handoff (`:14`) and gate (`:122`) say `passed` on the user's ruling, and the Handoff (`:18`) names §5 as binding. §4 quotes `wc -l` 58/86/64 against NFR-1's 60/86/64 (`:59`). Artifact wording; the gate answer is recorded correctly elsewhere. **Fix:** QA rewrites §5 to the user-accepted pass | open |
| F40 | Nit | `.spark/campaign-core/evidence.md:1149` | **Problem (new r5):** the ledger has no `/demo-day` round-3 entry, though D-10 (`plan.md:167`) records doc changes (`campaigns/README.md:22`, `docs/status.md:88`); its last line count (86) is now 87. **Fix:** a two-line round-3 entry | open |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1, 1.2, 1.4, 1.7, 1.8 | `templates/campaign.md:5-8`, `:17-29`, `:46` | ✅ met; live T8(a), (b), (d) |
| AC-1.3 | `templates/campaign.md:36-44` | ✅ met structurally r2 (SR-3 defined); only SR-1 is live |
| AC-1.5 | `templates/campaign.md:8`, `:11`; `campaigns/README.md:49`, `:69` | ✅ met; live T3(a) plus the re-run. F8 resolved r3 |
| AC-1.6 | `templates/campaign.md:53` | ✅ met r2; live T8(c), second run |
| AC-1.9 | `templates/campaign.md:5`, `:11-13` | ✅ met r4: the resume rule per the user's ruling, with the SR-5 carve-out explicit (F31) |
| AC-2.1 | `templates/campaign.md:11-12`; `campaigns/README.md:20-22` | ◐ partial r5: best effort, 13 of 19 (`qa.md:45`); user-accepted partial, B15 waived (`plan.md:167`) |
| AC-2.2, 2.4, 2.5, 2.6 | `campaigns/README.md`; empty skills/agents diff; `ls` | ✅ met (re-run) |
| AC-2.3 | `campaigns/README.md:37-41`, `:59-72` | ✅ met r2: dispatch observed under a bare prompt |
| AC-5.1, 5.6 | `campaigns/migration-campaign.md:7`, `:20`, `:57-59` | ✅ met r2; the refusals can fail |
| AC-5.2 | `campaigns/migration-campaign.md:28-44` | ✅ met r3 (F28) |
| AC-5.3 | `campaigns/migration-campaign.md:31`, `:34`, `:42-44` | ✅ met r3: one writer (F10); live in run 4 |
| AC-5.4 | `campaigns/migration-campaign.md:40`, `:55` | ⚠️ positive half observed; SR-9's trip not verified live, user-accepted partial r5 (`plan.md:166`) |
| AC-5.5 | `campaigns/migration-campaign.md:47-55` | ⚠️ text met r3 (the SR-5 ruling is in the row; SR-8 is path-scoped). SR-5/SR-7 are live; SR-6/SR-8 read-verified |
| AC-5.7 | `campaigns/migration-campaign.md:26`; `templates/campaign.md:50` | ✅ met r2: no contract step without a prompt |
| AC-5.8 | `campaigns/migration-campaign.md:61-64`; `README.md:129` | ✅ met |
| NFR-1, 2, 4, 5, 7, 8 | caps 58/64/85 and 3 rule lines; no `*.py`; validate passes | ✅ (the minor bump is due at `/go-live`) |
| NFR-3 | `README.md:124-130`; `docs/status.md:88` | ✅ after F26 |
| NFR-6 | `campaigns/README.md` | ✅ |
| NFR-9 | `templates/campaign.md:8`, `:11-13`, `:29`, `:53` | ✅ r3 (F8) |
| NFR-11 | T8(e) | ✅ r3: a planted brief in an `approved` instance was not followed (one run). Edit detection is disclosed as absent |

## 5. What Was Checked

- [x] Correctness: every fix re-derived from the current text. r3: the SR-5 row, the resume rule, §6 and AC-1.5/1.6/1.9 read together (F31); the merge rule was checked against the fixture as built (F30, F33). r4: F30–F33 re-derived; the resume rule read against AC-1.6/1.9 and the SR-5 row
- [x] Non-functional: NFR-1…9 and 11, the constitution quality bars, and the `library` lens sections 1, 2 and 4 (frontmatter re-parsed)
- [x] Error handling and security: halt, resume and rollback paths re-read. r3: no destructive git phrase, self-approval or self-resume path in the three files beyond F31's implicit precedence
- [x] Tests: `validate` re-run. r3: the ledger's round-2 section is audited against its claims, including the discarded F15 attempt (`evidence.md:1002`), and against `docs/status.md:88`
- [x] Readability: cross-file contradictions (F10, F11, F24, F28; r3: F30, F32; r5: F34, F37)
- [x] r5: role play vs CK writer (`migration-campaign.md:31`, `:34`), baseline vs Verifier (`:44`), status-by-statement vs AC-1.9/NFR-9 (`templates/campaign.md:8`, `:15-16`), one-goal refusal (`:22`), contract gate (`:26`), SR-7 (`:53`), plugin-folder rule (`campaigns/README.md:46`); no destructive git, self-approval, self-resume after SR-5 or invented-structure path. Doc claims checked against `qa.md` (F35, F36, F38)

## 6. Verdict

**Passed. No Blocker or Major is open.**

Round 5 read only the QA-driven text (D-8…D-10). The changed rules hold together: the session "never plays a role" yet writes the CK entry as "(not a role)" (`migration-campaign.md:31`, `:34`); the baseline run is allowed only because it "verifies nothing", and every green still needs a fresh Verifier (`:44`); `approved`/`complete`/`abandoned` are set by the user's own statement, which the agent transcribes as it already does for approval (`templates/campaign.md:8`, `:15-16`), so AC-1.9 and NFR-9 hold; `complete` never implies the contract (`:26`). The format is exactly 60 lines. The docs match `qa.md`'s 13-of-19 figure, the SR-2/SR-6 planted and SR-4 real distinction, and both accepted partials. Two stale counts in `docs/status.md:88` contradicted the row itself; I fixed them (F35). Still open: the waiver sentence can be read as barring every resume (F34, fail-closed), one disclosure that names too narrow a condition (F36), `qa.md`'s §5, which still says "Fail" (F39), and three Nits. The behaviour text was re-run by QA rounds 2–3; 398f202 changed only doc lines, which need no run.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here). F24 verified r3; QA's B15 (Major) waived by the user 2026-09-30 (`plan.md:167`)
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated by the diff as shipped
- [x] All plan deviations documented and accepted: D-1…D-6 user-accepted 2026-09-30; D-7…D-9 are fix passes, reviewed here; D-10 records the user's rulings
- [x] Test suite runs green: no suite exists (constitution §4); `claude plugin validate .` passes (only the `autoUpdate` warning), re-run by me r5
- [x] Line budget respected: Ist 135 / Soll ~150 (no HTML comments)
- [x] Status set to `passed`

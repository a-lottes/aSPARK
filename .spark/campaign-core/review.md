# Review Report: campaign-core

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | `git diff origin/main...HEAD` (8196c17, 2304ea5 on c5eb37d), `.spark/campaign-core/plan.md` |
| **Status** | `draft` |
| **Round** | 1 |
| **Date** | 2026-09-30 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** round 1: changes requested (6 Majors, no Blocker). Fix pass done; re-review pending — this line is superseded by the round-2 verdict.
- **Open:** `0 open` — F1–F15, F22 and F23 are `fixed` (fix pass `aef71f5`, awaiting re-review); F16–F21 were fixed by the Reviewer in round 1. Not yet re-verified by the owner of this report.
- **Binding ruling:** §6 Verdict and the gate checklist below. They are the only binding location; there is no other round to point to.
- **On conflict:** the numbered body below wins for everything except `Status`. Log the mismatch as a finding at the next `/peer-review` and proceed; don't stop on it.

## 1. Scope

- **Reviewed:** `templates/campaign.md`, `campaigns/README.md`, `campaigns/migration-campaign.md`, and the README, CONTRIBUTING, `docs/repo-layout.md` and `docs/status.md` hunks. Also the ledger `evidence.md` (all 822 lines), `plan.md` and `spec.md`, against constitution §1–§8 and the `library` lens (review sections 1, 2 and 4; section 3 N/A).
- **Re-run by me:**
  - `wc -l`: 56/83/63; the standing-rule section is 4 lines.
  - `git ls-files '*.py'`: empty. `ls campaigns`: 2 files.
  - `git diff origin/main --stat` over `skills`, `agents`, `ROADMAP.md`, `.spark/constitution.md`, `.claude-plugin` and `templates` (except the new file): empty. `plugin.json` is unchanged.
  - `grep -rn migration-campaign skills agents templates`: exit 1. `grep -rniE campaign skills agents`: 0.
  - `claude plugin validate .`: "passed with warnings". The only warning is the existing `autoUpdate` one.
  - `.github/ISSUE_TEMPLATE/enhancement.yml` exists. Every relative link in the diff resolves.
- **Tool:** `aspark-graph` was not queried. It does not index Markdown, and every changed path is Markdown (plan §2 already records `unknown_files`). Scoping was done by hand.
- **Not reviewed:** no dry run was re-performed, because the review phase has no session budget for it. The live claims in the ledger were checked against the transcripts the ledger quotes, not re-run. **Condition (b) re-derivation:** Must-AC evidence was re-read from the primary transcripts, not from the ledger's summaries.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ | Fixture, both transcripts, sizes and `*.py` recorded before T2 |
| T2 | ✅ | All DoD elements are present, 56 lines. The approval-line wording conflicts with the plan's "transcription" (F8) |
| T3 | ⚠️ | Both refusals are observed (spot-checked: T3(b) diff shows `halted` plus CK-3 only). The DoD asks for the "full text quoted"; the fixture is only summarised (F6) |
| T4 | ✅ | 83 lines; all DoD points present |
| T5 | ✅ | 63 lines, seven keys, SR-5…9, ⌈1.5×⌉, inert heading. Protocol defects are in F1–F3 |
| T6 | ⚠️ | Refusals are observed, but every instance was `draft`, so the test cannot fail (F4). Fixture text not quoted (F6) |
| T7 | ⚠️ | The run-1 "not counted" treatment is honest. Run 2: the prompt carries rules that the evidence attributes to the kind (F5). The DoD's rollback-at-halt did not happen and is missing from §6 (F13). Fixture not quoted (F6) |
| T8 | ✅ | (c) second run spot-checked: the diff is `Status` only. (e) covers an unapproved instance only (F15) |
| T9 | ⚠️ | Diff/grep checks re-run and clean. The add-a-file walk instantiated the second kind but dispatched none of its roles (docs overclaim, F16 fixed) |
| T10 | ✅ | README section is 9 lines; ROADMAP untouched; all five honesty points present |
| T11 | ✅ | Re-run and audit match what I re-ran |
| T12 | ✅ | Run on the user's go, in a scratch copy; one `campaigns` node, all artifacts skipped |
| D-1…D-5 | ⚠️ | D-5 is disclosed as not re-run in plan §6, `evidence.md:623` and `docs/status.md`. D-4 is cited by T9/T11 too (F22). A deviation for the T7 rollback is missing (F13). None are user-accepted yet |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `campaigns/migration-campaign.md:53`, `:24`, `:30` | **Problem:** SR-8 says "roll the in-flight slice back", but the only rollback defined is a revert commit or a committed restore (`:24`), and the Migrator commits only when the slice is done (`:30`). A mid-slice slice is uncommitted work, so "roll it back" in practice means a discard such as `git checkout -- .` or `git restore`. That destroys work and can take unrelated uncommitted user changes with it. **Why it matters:** a destructive git action without a go (constitution §6). SR-8 is read-verified only. **Fix (user's call):** SR-8 either commits the in-flight work and then reverts it, or halts without rollback and reports. Add "never discard uncommitted changes" | fixed |
| F2 | Major | `templates/campaign.md:52`; `campaigns/migration-campaign.md:22-24`, `:29` | **Problem:** the goal is "every slice in the slice list is parity-green", but the slice list and the parity check live in the kind's sections, outside the §1–§3 that §6 protects. Nothing in the instance forbids the agent from re-cutting or dropping a slice mid-run. "Frozen at approval" appears only in `campaigns/README.md:46`, which the instance does not carry. **Why it matters:** dropping the red slice makes the goal true. This is the Goodhart path A5 names. T7 run 2 declined it (`evidence.md:544`) by the session's own judgment, not by the text. **Fix:** §6 covers "§1–§3 and the kind's slice list and verifier" | fixed |
| F3 | Major | `campaigns/migration-campaign.md:20`, `:28-29`, `:37-38` | **Problem:** "Order of a run" puts the Archaeologist first and the Strategist second, both inside a run. But a run cannot start with an empty slice list (`:20`), and the Strategist's list is meant to be approved with the goal (`:38`), so the Strategist can only run *before* approval. Step 2 ("cuts the slice list, unless … user-approved") then flows into step 3 with no wait for approval. **Why it matters:** read literally, the agent migrates slices nobody approved, or can never start. In T6 `empty-slices` (`evidence.md:246-251`) and T7a the session had to invent the order. **Fix:** Strategist → user approves slices + goal + budget → Archaeologist → iterations; a slice list not user-approved = not startable | fixed |
| F4 | Major | `evidence.md:231`, `:243`, `:261`, `:280` | **Problem:** all three T6(b) instances were `Status` = `draft`, and each session refused *also* because of `draft`. Every refusal would have happened with the not-startable rule deleted. **Why it matters:** the only live evidence for Must AC-5.1/AC-5.6 cannot fail, and the ledger does not say so. **Fix:** re-run with `Status` `approved` and approval recorded, one element missing each; or label AC-5.1/5.6 read-verified | fixed |
| F5 | Major | `evidence.md:473`, `:498`, `:627`; T9 table `:711-713` | **Problem:** the T7 prompt adds, beyond naming the instance, "Run each role brief as a fresh general-purpose subagent… Commit each iteration as one commit. Never remove the old code." The ledger credits the kind with the fresh-subagent dispatch (AC-5.3, AC-2.3) and "no contract step" (AC-5.7). "One commit" is also the likely cause of the D-5 symptom, and it now contradicts the kind's `:30`. **Why it matters:** Inc 1 activation is naming the instance (`campaigns/README.md:61`); these Must-AC observations may be prompt-driven. QA would re-run a prompt that conflicts with the kind. **Fix:** re-run T7 with the bare T3 prompt, or disclose in the ledger and T9 that these behaviours were prompted | fixed |
| F6 | Major | `evidence.md:117-120`, `:187-188`, `:465-469`; `plan.md:82`, `:93`, `:97` | **Problem:** the T3 DoD asks for "full text quoted" and the T7 DoD for "fixture text is quoted"; plan §2 says fixtures' "full text is quoted in the ledger". The ledger summarises the fixtures instead: `parity.py`, `old/calc.py` and the composed instances are not quoted, and instances came from an unrecorded, untracked helper. **Why it matters:** QA must re-perform T7 (plan §4) and cannot rebuild the fixture; a DoD is claimed `done` while unmet. **Fix:** quote the fixture files and one composed instance verbatim, or re-scope the DoD with the user | fixed |
| F7 | Minor | `templates/campaign.md:11-12`, `:35`; `campaigns/README.md:70-71` | **Problem:** the agent may set `running`, and nothing says who may move `halted` → `running`. After a stop-rule halt, a later session could set `running` and continue. **Why it matters:** "escalate to the user" loses force. The spec (AC-1.3, AC-1.9) is silent too. **Fix (user's call):** one line: "from `halted`, only the user's explicit go resumes" | fixed |
| F8 | Minor | `templates/campaign.md:8` vs `campaigns/README.md:49`, `evidence.md:142-143`, plan T2 DoD | **Problem:** the template says the approval line is "never filled in by the agent". The plan and ledger treat the agent transcribing the user's statement as allowed (T3(a) offered to), and the waiver (`:28`) says "transcribed" with no writer named. **Why it matters:** contradictory approval rules invite either self-approval or a stuck campaign. **Fix:** "written only by the user, or by the agent transcribing the user's in-conversation statement verbatim; `approved` is always set by the user" (user's call) | fixed |
| F9 | Minor | `templates/campaign.md:41`, `:31`; `campaigns/migration-campaign.md:57` | **Problem:** SR-3 trips on "the budget window in §3", but §3 defines no window. Running out of iterations at a slice boundary is no stop rule (SR-8 covers mid-slice only). **Why it matters:** the observable AC-1.3 requires is not actually named. **Fix:** SR-3 reads "iterations used ≥ cap, or tokens (as observed in §3) ≥ budget" | fixed |
| F10 | Minor | `campaigns/migration-campaign.md:30` vs `:39-40`, `:42` | **Problem:** the Migrator's output includes "the `CK-` entry", but `:30` logs the CK after the Verifier. The Verifier "quotes into the instance", yet in T7 the main session wrote it (`evidence.md:514`, `:521`). **Why it matters:** the context that produced the slice may write the parity record (AC-5.3). **Fix:** name one writer; the Migrator does not write the CK | fixed |
| F11 | Minor | `templates/campaign.md:10`, `:43`; `campaigns/migration-campaign.md:15-20`; `campaigns/README.md:45` | **Problem:** "copy the format plus the kind's content" leaves the merge unspecified: two Goal sections, a literal `SR-5… <kind-specific additions>` row (a blank element = not startable?), frontmatter copied or not. **Why it matters:** instances differ by author; the fixtures used an undocumented helper. **Fix:** state the merge (kind body appended as §8+; the SR-5 row replaced by the kind's table; frontmatter dropped) | fixed |
| F12 | Minor | `campaigns/README.md:45`; `campaigns/migration-campaign.md:15` | **Problem:** agent-facing steps say "Copy `templates/campaign.md`". In a consumer repo that path resolves against the consumer's tree, not the plugin (constitution §3 `${CLAUDE_PLUGIN_ROOT}` rule). **Why it matters:** a hand-run reads a missing or wrong file; T6 and T9 prompts had to supply absolute paths. **Fix:** "from the aSPARK plugin (`${CLAUDE_PLUGIN_ROOT}/templates/campaign.md`)" | fixed |
| F13 | Minor | `plan.md:97`, `:125`, `:155-161`; `evidence.md:577` | **Problem:** T7's DoD expected a rollback of S2 at the halt; it happened only in T7b, by user choice. The ledger says so, but plan §6 has no deviation row for it. §4 still says AC-5.4 is live in T6/T7, though only its positive half ran (SR-9 never tripped). **Why it matters:** silent plan drift. **Fix:** `/increment` adds D-6 and corrects the §4 line; I did not edit `plan.md` | fixed |
| F14 | Minor | `evidence.md:294`, `:548`, `:669`; `README.md:128` | **Problem:** `aspark-guard@aspark` is enabled in the user's settings (verified). Its `.spark/.guard/` and hook appear in the T6, T7 and T7a sessions, but the ledger never states that every dry run ran with the guard loaded. **Why it matters:** "without `aspark-guard` nothing changes" is read-verified only, and the run conditions are undisclosed. **Fix:** one line in the ledger header; QA runs one session with the guard disabled | fixed |
| F15 | Minor | `evidence.md:369-384`; `templates/campaign.md:7` | **Problem:** the planted-instruction run (NFR-11) used an unapproved `draft` instance, so every injected instruction was moot. No run edits the role briefs or stop rules of an *approved* instance, and nothing detects post-approval edits to the "frozen" copy. **Why it matters:** NFR-11 is only partly shown. **Fix:** a QA run on an approved instance with a tampered brief; record integrity as agent-followed | fixed |
| F16 | Minor | `docs/status.md:88` | **Problem:** the row said "Proven live" for single runs; said a second kind was "reaching the phases" when none of its roles was dispatched; said "two gaps… except one sentence" when there were three; and omitted SR-2/SR-9 from *Not proven*. **Fix applied:** reworded to "Observed live, one … run per case"; add-a-file described as instantiated, no dispatch; three gaps; SR-2/SR-9 added | fixed |
| F17 | Minor | `campaigns/README.md:40` | **Problem:** "No skill, agent or doc contains a closed list of kind names", while README and `docs/repo-layout.md` name the kind. **Fix applied:** "No skill or agent contains a list of kind names; docs name kinds only as examples." | fixed |
| F18 | Minor | `evidence.md:693` | **Problem:** the T7 caveat listed the unexercised rules without SR-2 or SR-9, AC-5.4's trip half. **Fix applied:** added both | fixed |
| F19 | Nit | `README.md:160` | **Problem:** the "Going deeper" line omitted `campaigns/`, which `docs/repo-layout.md` now lists. **Fix applied:** added | fixed |
| F20 | Nit | `evidence.md:180` | **Problem:** the kind's size read `58` with no note that D-2 made it 63. **Fix applied:** annotated | fixed |
| F21 | Nit | `CONTRIBUTING.md:150-151` | **Problem:** the text pointed to "the kind list in `README.md`" (there is none) and to "the size cap in the spec" (a feature spec contributors never see). **Fix applied:** reworded | fixed |
| F22 | Nit | `plan.md:160` | **Problem:** D-4 names T10 only; T9 and T11 also diff against `origin/main`. **Fix:** add "T9, T11" | fixed |
| F23 | Nit | `spec.md:14` | **Problem:** the Handoff says "Awaiting the user's approval" while `Status` is `approved` (the On-conflict rule says log it). **Fix:** PO rewords the line | fixed |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `templates/campaign.md:5-8`, `:11`, `:15-49` | ✅ met (structural) |
| AC-1.2 | `templates/campaign.md:16`, `:18` | ✅ met; live T8(a) |
| AC-1.3 | `templates/campaign.md:35-43` | ⚠️ partial: SR-3 has no defined observable (F9); only SR-1 is live; SR-2/3/4 read-verified |
| AC-1.4 | `templates/campaign.md:45`; `README.md:128` | ✅ met |
| AC-1.5 | `templates/campaign.md:8`, `:11`; `campaigns/README.md:69` | ✅ met; live T3(a), T8(e). Wording conflict F8 |
| AC-1.6 | `templates/campaign.md:51-52` | ⚠️ met for §1–§3; the slice list is unprotected (F2). Live T8(c), second run |
| AC-1.7 | `templates/campaign.md:20-28` | ✅ met; live T8(d) |
| AC-1.8 | `templates/campaign.md:18` | ✅ met; live T8(b) |
| AC-1.9 | `templates/campaign.md:5`, `:11-12` | ⚠️ met as written; `halted`→`running` authority is unstated (F7) |
| AC-2.1 | `campaigns/README.md:20-31`; `campaigns/migration-campaign.md:1-9` | ✅ met; live T6(a) |
| AC-2.2 | skills/agents diff empty (re-run) | ✅ met |
| AC-2.3 | `campaigns/README.md:37-41`, `:59-71`; ledger T9 | ⚠️ partial: dispatch observed only under a prompt that dictated it (F5) |
| AC-2.4 | `ls campaigns` (re-run) | ✅ met |
| AC-2.5 | `campaigns/README.md:76-83`; `CONTRIBUTING.md:23`, `:136-151` | ✅ met |
| AC-2.6 | `campaigns/README.md:73-74`; no skill changed | ✅ met |
| AC-5.1 | `campaigns/migration-campaign.md:17-20` | ⚠️ text met; live evidence cannot fail (F4) |
| AC-5.2 | `campaigns/migration-campaign.md:32-43` | ⚠️ text met; run order contradicts approval (F3) |
| AC-5.3 | `campaigns/migration-campaign.md:41-43` | ⚠️ text met; CK/quote writer ambiguous (F10); dispatch prompt-driven (F5) |
| AC-5.4 | `campaigns/migration-campaign.md:39`, `:54` | ⚠️ positive half observed; SR-9 trip never exercised |
| AC-5.5 | `campaigns/migration-campaign.md:50-53` | ⚠️ SR-5/SR-7 live; SR-6/SR-8 read-verified; SR-8 is unsafe as worded (F1) |
| AC-5.6 | `campaigns/migration-campaign.md:7`, `:56-58` | ⚠️ text met; live evidence cannot fail (F4) |
| AC-5.7 | `campaigns/migration-campaign.md:25`; `templates/campaign.md:49` | ⚠️ text met; "no contract step" was also dictated by the prompt (F5) |
| AC-5.8 | `campaigns/migration-campaign.md:60-63`; `README.md:129` | ✅ met: 3 bullets, C10 content, inert, README says so |
| NFR-1 | 56/63 lines, 3 rule lines, 0 SKILL.md lines | ✅ |
| NFR-2 | `campaigns/README.md:59-74`; T1/T11 | ✅ |
| NFR-3 | `README.md:124-130`; `docs/status.md:88` | ✅ after F16 |
| NFR-4 | no command or `name` change | ✅ |
| NFR-5 | protected templates untouched; T12 graph build | ✅ (the minor bump is due at `/go-live`) |
| NFR-6 | `campaigns/README.md`; `README.md:122-130` | ✅; plugin-path clarity F12 |
| NFR-7 | `*.py` empty; validate passes (re-run) | ✅ |
| NFR-8 | only `S`/`SR-`/`CK-` in the format | ✅ |
| NFR-9 | `templates/campaign.md:8`, `:11-12`, `:28`, `:52` | ⚠️ F7, F8 |
| NFR-11 | T8(e) | ⚠️ partial (F15) |

## 5. What Was Checked

- [x] Correctness: every Must AC traced to text; protocol contradictions in F1–F3, F7–F11
- [x] Non-functional: NFR-1…9 and 11 plus the constitution quality bars; `library` lens sections 1, 2 and 4
- [x] Error handling: malformed / not-startable / halt paths read and their live evidence checked
- [x] Security: injection surface (F15); no secrets in the diff; destructive-git path (F1)
- [x] Tests: `validate` re-run green; dry-run evidence audited for discriminating power (F4–F6)
- [x] Readability: contradictions between the three campaign files recorded

## 6. Verdict

**Changes requested. The gate does not pass.**

The docs are honest after F16–F21: "experimental", "anticipated, not observed", "not enforced by Core" and "inert until routing ships" are all present and accurate. No protected structure, skill, agent, ROADMAP or version changed, and nothing executable is tracked.

Three open Majors are in the product text itself:
- **F1:** SR-8's rollback of uncommitted work is a plausible destructive action taken without a go.
- **F2:** the slice list that defines the goal sits outside the sections the agent may not edit.
- **F3:** the run order contradicts the rule that slices must be approved before a start.

Three open Majors are in the evidence:
- **F4:** the AC-5.1 and AC-5.6 refusals could not have failed.
- **F5:** the T7 prompt dictated the dispatch and the no-contract behaviour that the evidence credits to the kind.
- **F6:** the fixtures the DoD requires to be quoted are not quoted.

The Must ACs are all implemented in text, but several are only read-verified. The docs now say so, and QA must keep them `not-verified-live` unless it performs them.

**Open design questions for the user (not decided here):**
1. Should SR-5 roll the in-flight slice back on its own? Today only SR-8 does. T7's DoD expected a rollback at the halt, and the session offered it as an option instead.
2. Who resumes a campaign from `halted` (F7)?

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [ ] No open Major findings (or explicitly waived by the user, with reason recorded here). F1–F6 are open
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated by the diff as shipped. F1 is a §6 risk in an untested rule, not a performed violation
- [ ] All plan deviations documented and accepted. F13 is missing; D-1…D-5 are not yet user-accepted
- [x] Test suite runs green: no suite exists (constitution §4); `claude plugin validate .` passes, re-run by me
- [ ] Line budget respected: Ist 160 / Soll ~150 (no HTML comments). 10 lines over, because 23 findings plus 34 traceability rows are each one row. This overage needs the user's waiver or a trim in round 2
- [ ] Status set to `passed`

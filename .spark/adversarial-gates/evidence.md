# adversarial-gates — Evidence

Increment 1 (US-1 + US-4). Quoted outputs are verbatim; scratch fixtures live outside the repo.

## T1 — Walking skeleton and baselines

- **Branch:** `feat/adversarial-gates`, cut from `origin/main` (not from `docs/campaign-core-released`); spec + plan are the first commit (`fe2025a`).
- **Base SHA:** `fa33f2ccc91f640f8efd623b9e29391c86f22e28` (`origin/main`). "Base" below is a git worktree of this SHA.
- **`claude plugin validate .`** (Claude Code 2.1.289):

```
⚠ Found 1 warning:

  ❯ root: CLAUDE.md at the plugin root is not loaded as project context. To ship context with your plugin, use a skill (skills/<name>/SKILL.md) instead.

✔ Validation passed with warnings
```

- **`git ls-files '*.py'`:** empty.
- **`wc -l skills/*/SKILL.md`** (pre-change):

```
      97 skills/charter/SKILL.md
     120 skills/demo-day/SKILL.md
      94 skills/go-live/SKILL.md
      79 skills/increment/SKILL.md
      67 skills/look-and-feel/SKILL.md
     107 skills/next-steps/SKILL.md
      80 skills/peer-review/SKILL.md
     136 skills/spark/SKILL.md
      78 skills/sprint-plan/SKILL.md
     116 skills/story-time/SKILL.md
     974 total
```

- **Dry-run harness proof.** Scratch repo: one commit `init`, `README.md` = `# Notes app` / `A tiny CLI that stores notes.`, no `.spark/`. Command: `claude -p "/aspark:next-steps" --plugin-dir <base worktree> --max-turns 8`. Exit 0. Output, verbatim:

```
There's nothing to propose from yet. The repo has one commit ("init"), a 42-byte README, and no `.spark/` directory. That means no shipped features, no in-flight or stalled work, and no open findings.

There's also no `.spark/constitution.md`. I recommend running **`/charter`** first. It sets the project's standing principles and constraints, which is what a good proposal would be measured against. I won't invoke it for you. If you'd rather skip it, say so and I'll continue. With a brief this thin, though, I'd only be asking you for the first idea.

Which way do you want to go?
1. Run `/charter` now.
2. Skip it and tell me the first idea or theme you have in mind. I'll pass that to the Product Owner, or you can go straight to `/story-time <idea>` or `/spark <idea>`.
```

## Method (T2) — written and committed before any scan

**A search, not a census.** The corpus is what the terms below find in the scope below, read by the session's Grep and Read tools. No script. A gate evasion the terms miss is not in it; no completeness is claimed.

**Scope.** `ls .spark/*/{review,qa,evidence}.md`, minus this file (`.spark/adversarial-gates/evidence.md`, which is the output, not a source): **51 files** across 17 feature folders. Only text already committed on `origin/main` counts. Quotes come from `.spark/` only (NFR-9).

**Search terms** (case-insensitive, each run over the whole scope): `skipp`, `bypass`, `evad`, `rationali`, `waiv`, `rounded up`, `generous`, `lenient`, `without (asking|the user|approval)`, `self-approv`, `set .*approved`, `proceeded`, `silently`, `unlogged`, `simulat`, `trust(ed)? (the|its) (prior|earlier)`, `did not (re-?)?(run|verify|read)`, `claimed .* (pass|done|verified)`. Every hit is read in context (±5 lines) before it is classed or dropped. Dropped hits are not listed.

**Gate unit (D2).** A *gate* is one ceremony's gate step: the gate check or gate close in a named `skills/<s>/SKILL.md`. An entry is attached to the one gate whose rule was evaded; if no gate rule was evaded, it has no gate and cannot be `agent-evaded-gate`.

**Entry schema (D1).** Each entry has: `E<n>` · verbatim quote · `file:line` (the quote must match that line) · gate (skill + step) · class · acting context (`ceremony session` or `<role> agent`) · US-2 flag (`yes` for every `verdict-rounded-up`, else `no`).

**Classes — decision rules.** Decide in this order; the first rule that fits wins. When two classes fit, the entry takes the one that does *not* count toward the threshold.

1. `agent-evaded-gate` — an agent (the ceremony session or a role agent) **skipped, bypassed, or satisfied by assertion** a rule a `SKILL.md` gate step states, *and the trail records that it did*. Both halves are needed: a stated gate rule, and a recorded act that did not meet it.
   - *Boundary example (in):* a session set a status to `approved` without the user's explicit approval that the gate-close step requires.
   - *Boundary example (out):* a reviewer found that a gate was evaded by something other than an agent's own act (a human instruction, a tool fault). That is `other`.
2. `verdict-rounded-up` — a review or QA **verdict, severity, or pass mark was more generous than the evidence** (a partial check marked pass, a finding downgraded without a cited reason), with no gate step evaded.
   - *Boundary example (in):* "partial pass" counted as pass in a QA Result cell.
   - *Boundary example (out):* a finding the reviewer *later corrected itself* in the same round because new evidence appeared. That is ordinary review, not an entry.
3. `other` — everything else that is a real over-claim but fits neither: a doc claim stronger than its evidence, a waiver the user granted knowingly, a fix that invalidated an earlier waiver.
   - *Boundary example (in):* a README sentence that asserted an enforced guarantee for a prompt-level check.
   - *Boundary example (out):* anything the trail shows the user knowingly accepted with the facts in front of them is not an evasion at all; drop it.

**What does not count.** A finding that a reviewer *caught* and the fix pass *repaired* is still an entry if the original act matches a class (the evasion happened); but a hit that is only a reviewer's hypothetical ("would have skipped") is dropped. A rule restated in many files is **one** entry per distinct act, not one per mention.

**Threshold (AC-1.2).** A gate needs **≥ 2** `agent-evaded-gate` entries from **two distinct acts** (different features or different rounds). `verdict-rounded-up` and `other` never count (C10). Entries are never merged or split after the scan to move a gate across the threshold.

**Ruling order.** T3 scans and counts; T4 rules which gates qualify; both read this section, which is not edited after its commit. A needed change is a deviation recorded in the plan, not an edit here.

## Corpus (T3)

Scan of the 51 in-scope files with the Method's terms. Raw hit counts per term (term → lines): `skipp` 35 · `bypass` 16 · `evad` 0 · `rationali` 0 · `waiv` 84 · `rounded up` 2 · `generous` 1 · `lenient` 0 · `without (asking|the user|approval)` 5 · `self-approv` 2 · `set .*approved` 15 · `proceeded` 7 · `silently` 58 · `unlogged` 0 · `simulat` 18 · `trust(ed)? (the|its) (prior|earlier)` 0 · `did not (re-?)?(run|verify|read)` 7 · `claimed .* (pass|done|verified)` 16. Terms returning 0 or only fixture/test text (e.g. the planted-instruction fixtures in `campaign-core/evidence.md:375,382`, which are tests the agent *passed*) produced no entry. Hits for `waiv` and `silently` were read through their per-file counts and the lines that name an agent act; they are dominated by ratified waivers (the user knew) and "silently" used as a *requirement* of the feature under test. One hit, `right-sizing/evidence.md:321` ("the orchestrator skipped the ask"), is **dropped**: the same file retracts it at round 1 (finding F3). A `Blocker` sweep (`| Blocker |` rows, 11 lines) was added to catch acts the terms miss; it found E2 and E7.

Entries (every quote was matched to its `file:line` by `grep -F` on that exact line):

- **E1** · `agent-evaded-gate` · `.spark/right-sizing/evidence.md:807` · gate: `/demo-day` step 6 (close the gate: "set the report status to `passed`" only when the QA GATE checklist is "genuinely satisfied") · acting context: `qa-tester` agent (the file calls it "a *different* agent") · US-2 flag: no
  > claimed `Status: passed` while its own QA
  (continues at `:808-810`: "GATE checklist had **three open boxes** and one **checked** box asserting something false … B4 sat `open, unaccepted`")
- **E2** · `other` (borderline, see note) · `.spark/right-sizing/evidence.md:983` · gate: `/demo-day` step 1 (gear check; its rule: "**Never** ask the user to choose, confirm or supply a substitute method") · acting context: `qa-tester` agent · US-2 flag: no
  > volunteered *"a `.spark/constitution.md` §8 declaring an alternate QA
- **E3** · `verdict-rounded-up` · `.spark/project-kickoff/review.md:57` · gate: none (no gate step evaded) · acting context: `reviewer` agent's own earlier round · US-2 flag: **yes — input for US-2 (Inc 2)**
  > AC-3.4 carried a ✅ while the same sentence said it was inspection-only
- **E4** · `verdict-rounded-up` · `.spark/graph-mcp-verification/review.md:80` · gate: none · acting context: ceremony session via a subagent · US-2 flag: **yes — input for US-2 (Inc 2)**
  > AC-1.1 is given `confirmed (performed)`, but its emission half is a subagent's section literally headed **"SIMULATED USER-FACING CEREMONY OUTPUT"**
- **E5** · `other` · `.spark/graph-mcp-verification/review.md:79` · gate: none (constitution §6, not a `SKILL.md` gate) · acting context: ceremony session · US-2 flag: no
  > That execution mode is authorized nowhere
- **E6** · `other` · `.spark/lens-dispatch-registry/review.md:76` · gate: none (a doc claim) · acting context: `/increment` session · US-2 flag: no
  > New step 4 claimed "a lens with **any combination of phases** … reaches its agents … with no skill, agent or template edit". False for `phases: act`
- **E7** · `other` · `.spark/situational-lenses/review.md:55` · gate: none (constitution §6, not a `SKILL.md` gate) · acting context: `/increment` session · US-2 flag: no
  > All three surveyed projects' **real names appeared in plain text**, on a public repo
- **E8** · `other` · `.spark/lean-rounds/review.md:58` · gate: none (a skill omission, not an agent's act) · acting context: n/a (the skill text) · US-2 flag: no
  > `/demo-day` never pointed the QA Tester at the previous `qa.md`
- **E9** · `other` · `.spark/graph-gates/review.md:694` · gate: none · acting context: `/increment` fix pass · US-2 flag: no
  > F4's leg claimed a checklist entry that did not exist
- **E10** · `other` · `.spark/campaign-core/evidence.md:494` · gate: none (a campaign kind's rule, not a `SKILL.md` gate) · acting context: ceremony session · US-2 flag: no
  > The session **skipped the Archaeologist**

**Note on E2 (borderline — a reader should decide, not this file).** The same forbidden act (offering a substitute-method declaration at `/demo-day` step 1) is recorded as recurring: B1 and B4 earlier, B5 here (`right-sizing/qa.md:103-105`, `evidence.md:981-995`). Rule 1 of the Method needs the agent to have *skipped, bypassed or satisfied by assertion* the gate's rule; offering the user a way around the browser requirement is a rule breach at the gate, but the agent still stopped, so it fits `other` under "when two classes fit, take the one that does not count". It is kept as `other`. If a reviewer reclassifies E2 and counts B1/B4 as distinct acts, `/demo-day` step 1 would reach 3. That ruling would change T4's outcome and is exactly the call this feature must not make in its own favour.

### Counts

| Class | Entries | Count |
|---|---|---|
| `agent-evaded-gate` | E1 | **1** |
| `verdict-rounded-up` | E3, E4 | 2 |
| `other` | E2, E5, E6, E7, E8, E9, E10 | 7 |
| **Total** | | 10 |

| Gate | `agent-evaded-gate` | Other classes attached |
|---|---|---|
| `/demo-day` step 6 (close) | 1 (E1) | – |
| `/demo-day` step 1 (gate and gear check) | 0 | E2 (`other`) |
| every other `SKILL.md` gate | 0 | – |

`verdict-rounded-up` entries E3, E4 are kept here, flagged "input for US-2 (Inc 2)", and produce no row in any `SKILL.md` (AC-1.8).

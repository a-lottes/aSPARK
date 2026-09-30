---
name: migration-campaign
trigger: replacing a legacy component, module or system in verified, reversible slices
goal-kind: every slice in the slice list is parity-green
roles: [archaeologist, strategist, migrator, parity-verifier]
stop-rules: [SR-5 a parity-green slice turns red (halt; the slice stays committed until the user decides), SR-6 rollback used twice on one slice, SR-7 characterization tests not green on the old code, SR-8 budget runs out mid-slice, SR-9 one iteration's diff spans two slices]
budget-defaults: iterations = ceil(1.5 x slice count), unmeasured; tokens = no default (unset = not startable)
phases: [specify, plan, act, review]
---

# Migration campaign

Replace old code with new code **one reversible slice at a time**. Old and new coexist
(expand-contract) until a slice is parity-green; the old code goes only on the user's go.
Instantiate from `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md`: sections 1–7 come from the format; append this file's body (below the frontmatter) as its §8 "Kind-specific", with the slice list and parity check filled in under it (the token budget stays in the format's §3); replace §4's `SR-5…` placeholder row with the rows below.

## Goal, for the instance
- **Condition:** every slice in the slice list is parity-green.
- **Observable:** the per-slice parity result, quoted in the instance. **Verifier:** the parity check the user names.
- **Not startable** while the slice list is empty, the parity check is unset, or the token budget is unset.

## Slices
- `S<n>`: an ordered list; slices should own **disjoint** paths (SR-9 can only trip on a diff touching paths of two slices, so a path owned by two slices is a blind spot). Each slice names the paths it owns and a **rollback step** that preserves history
  (a revert commit, or a restore committed on top — never `reset --hard` or a force operation).
- **Frozen at approval:** the slice list and the parity check cannot be dropped, shortened or edited by the agent (format §6). A slice that will not go green stays in the list and stays red.
- **Contract** (removing the old code of a slice) is a separate step per slice, taken only after that slice is parity-green. It waits for the user's explicit go in the conversation; setting `complete` never implies it.

## Order of a run
1. **Archaeologist first.** No Migrator starts until the characterization tests are quoted **green on the old code**, even when the slice list is already approved.
2. **Strategist** cuts the slice list — before approval, in a planning session, since an instance with an empty list is not startable. After cutting one, **stop and wait** for the user to approve it with the goal; step 3 does not begin before that.
3. **Each iteration:** the Migrator does one slice and commits **its paths only**; then a fresh Parity Verifier runs; then the campaign session (not a role) logs the `CK-` entry, quoting the Verifier's output verbatim, in a **separate commit** — so rolling a slice back never reverts the log.

## Roles
Each role brief — the Strategist included — runs as a **fresh general-purpose subagent** through the host's normal dispatch; none has an `agents/*.md`. The campaign session never plays a role itself.

- **Archaeologist** (plan). Pins the existing behaviour as characterization tests that pass against the **old** code,
  before any migration. Output: the tests and their observed green output, quoted.
- **Strategist** (plan). Cuts the ordered slice list, each slice with owned paths, a rollback step and an expand-contract
  approach. Output: `S1…Sn` in the instance for the user to approve with the goal.
- **Migrator** (act). Migrates **one slice per iteration**. Output: a diff that touches only that slice's paths.
  It never marks a slice parity-green and does not write the `CK-` entry.
- **Parity Verifier** (review). Runs as a **separate invocation, in a context separate from the one that produced the slice**.
  It runs the parity check against old and new and reports the observed output verbatim (the campaign session copies it into the instance). It **edits neither the
  migrated code nor the parity check**. Only its quoted output can mark a slice parity-green; when unsure it reports, it does not mark. **If a fresh Verifier cannot be dispatched or cannot run the check, halt and escalate:** the campaign session never runs the parity check itself, never stands in for the Verifier and never marks a slice green.

## Stop rules added to the four in the format
All halt the run and escalate to the user (agent-followed, not enforced by Core).

| ID | Trips when (observable) |
|---|---|
| SR-5 | a previously parity-green slice turns red in the Verifier's output. Halt; the breaking slice **stays committed**. Only the user decides between a revert, a changed slice list (fresh approval) or another approach. The agent does not resume after `SR-5` until they have |
| SR-6 | rollback is used twice on the same slice |
| SR-7 | the Archaeologist's tests are not green on the old code. The agent does not install or download anything to fix it; the user decides |
| SR-8 | the budget runs out mid-slice: commit **the in-flight slice's own paths only** as a work-in-progress commit, revert that commit, then halt. Other uncommitted files are left alone and nothing is discarded |
| SR-9 | one iteration's diff spans two slices (`git diff --stat` names paths of two slices) |

## Budget
- **Iterations:** the cap is ⌈1.5 × slice count⌉. **Tokens:** no default; the user states them at approval.
- Both are unmeasured and the user may override them at approval. Observed as in the format's §3.

## Standing rule for feature loops — inert until routing ships
- A feature that touches an in-flight slice must name this campaign in its spec and re-run that slice's parity check green before merge.
- A feature that touches no in-flight slice is unaffected and sees no new step.
- Until a later increment ships routing, no ceremony reads this text; the README says so.

---
name: migration-campaign
trigger: replacing a legacy component, module or system in verified, reversible slices
goal-kind: every slice in the slice list is parity-green
roles: [archaeologist, strategist, migrator, parity-verifier]
stop-rules: [SR-5 a parity-green slice turns red, SR-6 rollback used twice on one slice, SR-7 characterization tests not green on the old code, SR-8 budget runs out mid-slice, SR-9 one iteration's diff spans two slices]
budget-defaults: iterations = ceil(1.5 x slice count), unmeasured; tokens = no default (unset = not startable)
phases: [specify, plan, act, review]
---

# Migration campaign

Replace old code with new code **one reversible slice at a time**. Old and new coexist
(expand-contract) until a slice is parity-green; the old code goes only on the user's go.
Copy this file's content into the instance after [`templates/campaign.md`](../templates/campaign.md).

## Goal, for the instance
- **Condition:** every slice in the slice list is parity-green.
- **Observable:** the per-slice parity result, quoted in the instance. **Verifier:** the parity check the user names.
- **Not startable** while the slice list is empty, the parity check is unset, or the token budget is unset.

## Slices
- `S<n>`: an ordered list. Each slice names the paths it owns and a **rollback step** that preserves history
  (a revert commit, or a restore committed on top — never `reset --hard` or a force operation).
- **Contract** (removing the old code of a slice) is a separate step per slice. It waits for the user's explicit go in the conversation.

## Order of a run
1. **Archaeologist first.** No Migrator starts until the characterization tests are quoted **green on the old code**, even when the slice list is already approved.
2. **Strategist** cuts the slice list, unless the instance already carries a user-approved one.
3. **Each iteration:** the Migrator does one slice and commits it; then a fresh Parity Verifier runs; then a `CK-` entry is logged. Commit the slice's paths and the campaign log **separately**, so rolling a slice back never reverts the log.

## Roles
Each role brief runs as a **fresh general-purpose subagent** through the host's normal dispatch; none has an `agents/*.md`.

- **Archaeologist** (plan). Pins the existing behaviour as characterization tests that pass against the **old** code,
  before any migration. Output: the tests and their observed green output, quoted.
- **Strategist** (plan). Cuts the ordered slice list, each slice with owned paths, a rollback step and an expand-contract
  approach. Output: `S1…Sn` in the instance for the user to approve with the goal.
- **Migrator** (act). Migrates **one slice per iteration**. Output: a diff that touches only that slice's paths, and the
  `CK-` entry for the iteration. It never marks a slice parity-green.
- **Parity Verifier** (review). Runs as a **separate invocation, in a context separate from the one that produced the slice**.
  It runs the parity check against old and new, and quotes the observed output into the instance. It **edits neither the
  migrated code nor the parity check**. Only its quoted output can mark a slice parity-green; when unsure it reports, it does not mark.

## Stop rules added to the four in the format
All halt the run and escalate to the user (agent-followed, not enforced by Core).

| ID | Trips when (observable) |
|---|---|
| SR-5 | a previously parity-green slice turns red in the Verifier's output |
| SR-6 | rollback is used twice on the same slice |
| SR-7 | the Archaeologist's tests are not green on the old code |
| SR-8 | the budget runs out mid-slice: roll the in-flight slice back, then halt |
| SR-9 | one iteration's diff spans two slices (`git diff --stat` names paths of two slices) |

## Budget
- **Iterations:** the cap is ⌈1.5 × slice count⌉. **Tokens:** no default; the user states them at approval.
- Both are unmeasured and the user may override them at approval. Observed as in the format's §3.

## Standing rule for feature loops — inert until routing ships
- A feature that touches an in-flight slice must name this campaign in its spec and re-run that slice's parity check green before merge.
- A feature that touches no in-flight slice is unaffected and sees no new step.
- Until a later increment ships routing, no ceremony reads this text; the README says so.

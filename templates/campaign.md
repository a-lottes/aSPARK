# Campaign: <campaign-name>

| | |
|---|---|
| **Status** | `draft` \| `approved` \| `running` \| `halted` \| `complete` \| `abandoned` |
| **Kind** | <kind name> |
| **Kind source** | upstream `campaigns/<kind>.md`, copied below and frozen at approval |
| **Goal approved by / date** | <user> / YYYY-MM-DD — the user's own statement, transcribed; the agent never invents it |

<!-- Copy this file plus the chosen kind's content to `.spark/campaigns/<campaign-name>/campaign.md`.
     Any element left blank = not startable. The agent may set Status only to `running` (at the start after
     approval, and after `halted` once the cause is resolved and recorded in a `CK-` entry) or `halted`;
     `approved`, `complete` and `abandoned` are the user's. IDs: `S<n>` slices, `SR-<n>` stop rules,
     `CK-<n>` checkpoints. Keep the file name `campaign.md`. -->

## 1. Goal
- **Condition:** <one end state that a command or file state can confirm> · **Observable:** <command and expected output, or file state> · **Verifier:** <who or what runs it>
- **Thresholds:** <numbers or states that separate done from not done>
- "It looks good" is not decidable and is rejected. One undertaking, one goal, one budget: several independent goals or a set of stories go to the feature loop, not here.

## 2. Veto record
| Condition | Met / missed | Note |
|---|---|---|
| **Mandatory:** the check is automatically verifiable — the agent can run it and see the result | | |
| Advisory: the work recurs | | |
| Advisory: the budget is affordable | | |
| Advisory: the agent has tools that run the check | | |

A missed mandatory condition is a stop unless the user records a **waiver**: their statement transcribed, reason, date. Advisory misses are recorded, not stops.

## 3. Budget
- **Iterations:** <n> · **Tokens:** <n>, observed by the user pasting `/cost` at a checkpoint, or by the agent's estimate labelled as an estimate.
- Defaults are unmeasured and may be overridden by the user at approval.

## 4. Stop rules
Every rule halts the run and escalates to the user; the agent then sets `halted`.

| ID | Trips when (observable) |
|---|---|
| SR-1 | two consecutive checkpoints show no change in the goal observable |
| SR-2 | the identical error appears twice |
| SR-3 | iterations used or tokens spent exceed §3, checked at every checkpoint |
| SR-4 | a merge conflict blocks the work |
| SR-5… | <kind-specific additions> |

Budget and stop rules are **followed by the agent, not enforced by Core**. Optional enforcement is `aspark-guard`'s concern.

## 5. Rollback
- <how a step is undone without destroying history: a revert commit, or a restore committed on top — never `reset --hard` or a force operation>
- Removing old code is not a rollback step and waits for the user's explicit go.

## 6. Changing the goal
§1–§3 and, where the kind has them, the slice list and the parity check are **frozen at approval**; any difference from the approved text is a stop: halt and report. To change the goal, thresholds or budget, iteration pauses and the agent sets `halted`. The agent does **not** edit §1–§3 — not even as a proposal — and reports what it found and what it proposes. Only the user changes them, recorded here with reason and date. The whole spec is approved afresh before iteration resumes.

## 7. Checkpoints
| CK | Date | Iteration | Goal observable (quoted) | Status set |
|---|---|---|---|---|

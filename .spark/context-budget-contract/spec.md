# Spec: context-budget-contract

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |

## User Story

**US-1** As an agent running a large feature, I need a defined per-ceremony
context budget, so that growing artifacts never silently overflow the prompt.

**US-2** As a team resuming mid-loop in a fresh session, I need a load order
(statuses first, full text only for the resumed phase), so that resume stays
token-economical regardless of feature size.

## Acceptance Criteria

- **AC-1** `docs/workflow.md` defines, per ceremony, what must be read in full
  vs. header-only (table), plus the `/increment` full-plan prohibition and the
  overflow rule (record a finding, re-cut the plan).
- **AC-2** `skills/spark/SKILL.md` resume path instructs statuses-first loading
  and links the budget table.

## Out of Scope

- Any mechanical enforcement (no executable code per Constitution §3).
- Artifact summarization as new artifacts (rejected: unverified summaries
  become silent state drift).

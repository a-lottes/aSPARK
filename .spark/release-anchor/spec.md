# Spec: release-anchor

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |

## User Story

**US-1** As a maintainer of an aSPARK-driven project, I want every `release.md`
to carry the git state it shipped (commit SHA, tag, PR), so that any release
can be traced back to the exact code after the fact — across sessions and
machines.

**US-2** As a team member joining mid-project, I want one append-only
`.spark/releases.md` per project, so that "what shipped when, in which order"
is answerable without walking feature directories.

## Acceptance Criteria

- **AC-1** `templates/release-notes.md` header contains `Commit` and `PR` rows
  (in addition to Version/Date), placed with the other header rows.
- **AC-2** `skills/go-live/SKILL.md` step 4 instructs writing the *executed*
  results (resolved SHA, PR URL) back into the artifact in the same edit that
  flips Status to `released`.
- **AC-3** `agents/release-manager.md` names the anchor discipline: evidence,
  not intention; placeholders after `released` are a defect.
- **AC-4** A project-level release index template exists and is append-only.

## Out of Scope

- Backfilling anchors for past releases (impossible by definition).
- Any executable code (Constitution §3: zero executable files).

# Plan: ux-volume-findability

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Status** | `approved` |
| **Date** | 2026-11-18 |

## Where each rule lives (CLAUDE.md: put a rule in the file the agent reads)

| Rule | File the agent has open at that step | Task |
|---|---|---|
| §7 checks, cut rule, phase notes, QA volume run | `lenses/ux.md` (passed to PO, Designer and QA Tester by every dispatching skill) | T1 |
| Volume table | `templates/constitution.md` §2 (read by every agent) | T2 |
| Draft the table | `agents/facilitator.md` step 3 (writes §2) | T3 |
| Surface the table for confirmation | `skills/charter/SKILL.md` step 3 | T3 |
| Cut needs follow-up or waiver | `agents/product-owner.md` Clarify item 8 | T4 |
| Designer names §7 | `agents/designer.md` §4 `ux` bullet | T4 |
| QA volume run | `agents/qa-tester.md` step 4 `ux` bullet | T4 |
| NFR example | `templates/spec.md` NFR-4 | T4 |
| Lens description | `lenses/README.md`, README, `docs/status.md` | T5 |

## Dispatch and activation check (every claimed phase)

`ux.md` keeps `phases: [specify, design, qa]`. `/story-time`, `/look-and-feel` and `/demo-day` dispatch lens files by their `phases` frontmatter (`lenses/README.md` § Adding a lens, step 4), so §7 reaches the same three agents the lens reached before. Activation is unchanged (`applies-to: [web-app, website]`). The new constitution table is written only by `/charter` (Facilitator), the sole writer of §2.

## Tasks
- T1 `lenses/ux.md`: §7, pointer from §2 large-data, phase notes for PO/Designer/QA.
- T2 `templates/constitution.md`: §2 bullet + table, delete-when-off comment.
- T3 Facilitator + `/charter`.
- T4 PO, Designer, QA Tester, spec template.
- T5 Docs: lenses README row, README section, `docs/status.md` row.
- T6 Evidence: negative case by reading, then a Designer dry run, old lens vs new lens, on a copy of the field project.

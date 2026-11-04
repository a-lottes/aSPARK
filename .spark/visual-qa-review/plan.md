# Plan: visual-qa-review

| | |
|---|---|
| **Phase** | Plan |
| **Status** | `approved` |
| **Date** | 2026-10-30 |

**Architecture.** Edit the files the agents read at the moment they act: `agents/qa-tester.md` (visual review, binding deviations), `lenses/ux.md` §6, `agents/designer.md`, `templates/qa-report.md` (new §6 table placed after the protected tables, two gate items), `templates/spec.md` §8 comment (binding/advisory labels), `skills/demo-day/SKILL.md`. Rejected: a new lens or agent (out of scope); editing protected columns.

## Task Breakdown

| # | Task | Story | Status | Definition of Done |
|---|---|---|---|---|
| T1 | QA Tester: visual review and deviation rules | US-1, US-2 | done | text in agents/qa-tester.md |
| T2 | ux lens §6 | US-3 | done | lenses/ux.md |
| T3 | Designer scale and space use | US-4 | done | agents/designer.md |
| T4 | Templates and demo-day skill | US-1, US-2 | done | templates/qa-report.md, spec.md, skills/demo-day |
| T5 | Docs with maturity label | NFR-2 | done | README, ROADMAP, docs/status.md |
| T6 | Dry runs, negative case first | all | done | evidence.md |

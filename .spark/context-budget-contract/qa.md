# QA: context-budget-contract

| | |
|---|---|
| **Phase** | Review (QA) |
| **Owner** | QA-Tester (`/demo-day`) |
| **Status** | `passed` |

## Checks

- Section renders as valid Markdown (table + list, no broken pipes).
- **Negative case**: small features keep today's behavior - the table permits
  full reads everywhere; it only limits when artifacts grow. No error, no
  warning for small features.
- **not-verified-live**: a real /spark resume on an oversized feature was not
  executed here (needs a live Claude Code session) - reviewer's live test.

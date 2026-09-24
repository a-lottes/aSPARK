# Release: context-budget-contract

| | |
|---|---|
| **Phase** | Keep |
| **Owner** | Release Manager (`/go-live`) |
| **Input** | `review.md` (`passed`), `qa.md` (`passed`) |
| **Status** | `handed-off` |
| **Version** | vX.Y.Z |
| **Date** | 2026-09-24 |

## 2. Changelog

### Added

- Per-ceremony context budget: docs/workflow.md now defines what each ceremony
  must read in full vs. header-only; /spark resume loads statuses first.
  Large features no longer silently overflow the prompt.

## 3. Release Actions

| Action | Result |
|---|---|
| Version bump & tag | proposed only (pr mode) |
| PR / merge | this PR |
| Deploy | N/A - prompt material |

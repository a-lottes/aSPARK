# QA: release-anchor

| | |
|---|---|
| **Phase** | Review (QA) |
| **Owner** | QA-Tester (`/demo-day`) |
| **Status** | `passed` |

## Checks

- AC-3: `agents/release-manager.md` contains the anchor-discipline paragraph
  directly above "Releasing is publishing". Verified by file read.
- AC-4: `templates/releases-index.md` exists, is append-only by instruction
  comment, Markdown-only.
- **Negative case** (Constitution/CONTRIBUTING requirement): in a project
  *without* prior releases, nothing changes — no error, no warning; the index
  is created only on first `/go-live`, by instruction. No template references
  it before that.
- **Negative case 2**: templates that predate this change (no Commit/PR rows
  in an existing project's old artifacts) are untouched — the new rows are
  additive; old artifacts simply lack them.

## not-verified-live

- An actual `/go-live` run against a live git remote was NOT executed here
  (requires a real target project + user go). The instruction path is
  verified by reading; live execution is the reviewer's/Andreas's test.

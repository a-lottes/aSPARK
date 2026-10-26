# Review: template-version-marker

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Status** | `passed` |

## AC Trace

- **AC-1** → all 8 files in `templates/` contain the marker once, on line 3
  (grep count 1 each; `sed -n 1,4p` shows title, blank, marker, blank). Traced.
- **AC-2** → `git diff origin/main -- templates/` shows only added lines. Traced.
- **AC-3** → `.spark/constitution.md` template-contract note. Traced.
- **AC-4** → `ROADMAP.md` Blocked entry. Traced.

## Findings

- Release coordination for the unshipped consumer items (graph asserting,
  guard reading) was missing; now recorded in `spec.md` ("Release coordination").
  Resolved.

No other findings.

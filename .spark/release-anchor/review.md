# Review: release-anchor

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Status** | `passed` |

## AC Trace

- **AC-1** → `templates/release-notes.md`: two new header rows, verifiable by
  reading the template. Traced.
- **AC-2** → `skills/go-live/SKILL.md`: step 4 now ends with the write-back
  instruction and the exact index-row shape. Traced.

**Note on AC-3/AC-4:** verified below in QA; both are single-file additions.

## Findings

None blocking. One observation recorded for the record: the write-back is
instruction (this repo has no runtime by design); the backstop is the
Release Manager's own KEEP GATE, which now lists the anchor explicitly.

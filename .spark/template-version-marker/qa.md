# QA: template-version-marker

| | |
|---|---|
| **Phase** | Review (QA) |
| **Owner** | QA-Tester (`/demo-day`) |
| **Status** | `passed` |

## Checks

- AC-1: marker present once at line 3 in all 8 templates (grep).
- AC-2: diff of `templates/` is additions only; no protected heading or row touched.
- AC-3, AC-4: read the constitution note and ROADMAP entry; both match the spec.
- **Negative case:** artifacts that predate the marker simply lack it; nothing in
  this repo reads it, so nothing breaks.

## not-verified-live

- `aspark-graph` and `aspark-guard` reading the marker is out of this repo and
  was not tested; see the spec's "Release coordination".

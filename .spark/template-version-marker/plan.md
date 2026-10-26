# Plan: template-version-marker

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Status** | `approved` |

## Architecture decision

Add the marker as an HTML comment on line 3 of each template: invisible when
rendered, no change to any protected structure. Rejected: YAML frontmatter (would
change the first line every consumer parses); marker equal to the plugin version
(would force a contract bump on every release).

## Tasks

| # | Task | Covers |
|---|---|---|
| 1 | Add `<!-- aspark-template: aspark/0.1.0 -->` after the title in all 8 templates | AC-1, AC-2 |
| 2 | Update the constitution's template-contract note | AC-3 |
| 3 | Update the ROADMAP entry (core shipped, reading side open) | AC-4 |
| 4 | Record the cross-repo release coordination in the spec | scope |

## Test strategy

Grep that every template has the marker at line 3 exactly once; diff shows only
added lines in templates.

## Risks

- Marker shipped alone and read by nobody: mitigated by the hold in the spec's
  "Release coordination" section.

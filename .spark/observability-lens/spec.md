# Spec: observability-lens

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |
| **Date** | 2026-10-26 |
| **Ticket** | #89 (tracks #15) |

**Handoff**
- **Status:** `approved` (mirrors the header table). The issue's acceptance criteria were adopted as the approved spec in dark mode; Design Review N/A (no UI).
- **Summary:** add `lenses/observability.md` for deployed `api` services, silent elsewhere.
- **Open:** `none`
- **Binding ruling:** the AC list below.
- **On conflict:** the numbered body wins for everything except `Status`.

Source: issue #89, "Add an observability lens (lenses/observability.md)". Prompt-material caveat, stated up front: AC-3/AC-4 are dry runs and the lens firing is likely, never certain.

## Acceptance criteria

- **AC-1:** The lens declares which project types/characteristics activate it (e.g. `api`, deployed services) and explicitly names profiles where it stays silent (`library`, `cli`, static `website`); it does not overlap `security` logging-hygiene checks, and cross-references them instead of duplicating.
- **AC-2:** Per CLAUDE.md "An add-a-file scope check must examine every phase the artifact claims": dispatch AND activation are checked for every phase the lens frontmatter claims (Specify, Plan, Review, QA as applicable) across skills, `agents/facilitator.md` and `templates/constitution.md`; any gap is fixed or disclosed.
- **AC-3:** Negative case first: a dry run in a repo with no service profile (e.g. this repo, `library`) shows the lens does not fire and nothing changes. Evidence in `.spark/observability-lens/evidence.md`.
- **AC-4:** Positive case: a dry run on a sample `api` project shows the lens fires in Review; labelled a dry run, not a public run. Any prompt-material check states its measured hold rate, not a guarantee.
- **AC-5:** README/ROADMAP/docs/status.md maturity labels updated honestly (shipped vs. unproven); the stale #6 mention in the ROADMAP #15 entry is corrected.
- **AC-6:** Markdown only, no executable code (constitution §3); semver bump per the library lens.

## Test strategy

Markdown-only repo: verification is the dry runs in `evidence.md` plus `/peer-review`. No automated tests exist or are added.

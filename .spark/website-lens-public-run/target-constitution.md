# Constitution: startbootstrap-agency (as profiled for this run)

| | |
|---|---|
| **Scope** | Project-wide for the run target only |
| **Owner** | The aSPARK Factory line (dark mode, recommended gate). **Not** the target's maintainers: they never declared this profile |
| **Status** | `active` |
| **Date** | 2026-10-27 |

<!-- Written for the run (issue #96), copied verbatim to the scratch clone at
     `/tmp/target/startbootstrap-agency/.spark/constitution.md` (untracked, never pushed upstream).
     The skills read it from there. -->

## 1. Product Principles

- A one-page agency theme must be usable by keyboard and screen-reader users, not only by mouse users.

## 2. Project Profile & Active Lenses

- **Project type(s):** `website`.
  Evidence: multi-section static HTML page, `dist/index.html`, built from Pug/SCSS (`package.json`).
- **Characteristics:** `must-be-accessible`.
  Evidence: none in the target. This is a **declared assumption for the run**: the theme is reused
  as the starting point of public agency sites, many under an accessibility mandate (EAA/ADA). The
  characteristic is what activates the lens (`lenses/accessibility.md` frontmatter `triggers`).
- **Active lenses:**

| Lens | Why it's active (or off) | Enforced in |
|---|---|---|
| `accessibility` | **Active** — trigger `must-be-accessible` | `/story-time`, `/look-and-feel`, `/increment`, `/peer-review`, `/demo-day` |
| `seo` | Off — the page is a demo theme with placeholder copy; indexing is not a goal of this run. (Type `website` would otherwise activate it; left off on purpose to keep the run to one lens) | — |
| `ux` | Off — same reason; keeps the run to one lens | — |
| `security`, `api`, `cli`, `library`, `i18n`, `data`, `observability` | Off — static page, no auth, no PII, no backend | — |

- **Active-lens load:** 1 lens active.

## 3. Technical Constraints

- **Stack / runtime:** static HTML/CSS/JS in `dist/`; Bootstrap 5.2.3 bundle.

## 4. Quality Bars

- **Accessibility:** WCAG 2.1 AA is the floor (assumed).

## 8. QA Method

- **Browser-observable surface:** yes

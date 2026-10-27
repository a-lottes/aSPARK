# Constitution: eleventy-base-blog

| | |
|---|---|
| **Scope** | Project-wide — binds every SPARK phase and every feature |
| **Owner** | The user (amended via `/charter`) |
| **Status** | `active` |
| **Date** | 2026-10-27 |

<!-- Drafted in dark mode (no user available): every entry is grounded in a file or marked `not stated` / `not found`.
     Read: README.md, package.json, eleventy.config.js, _data/metadata.js, _includes/layouts/base.njk,
     content/sitemap.xml.njk, netlify.toml, .nvmrc, .editorconfig, .github/dependabot.yml, caller's git summary.
     Absent: CLAUDE.md, CONTRIBUTING.md, robots.txt, any test files or test script, CODEOWNERS, accessibility statement. -->

## 1. Product Principles

- Zero-JavaScript, pre-rendered output is the default; content is exclusively static. — inferred from README.md:48-49 (note: `base.njk:40,72` ships a small module script for heading anchors, so "zero-JS" is a goal with one exception).
- Performance out of the box: the starter ships "four-hundos" Lighthouse with 0 CLS and 0ms TBT. — inferred from README.md:53-55.
- The product is a starter that adopters clone and edit, so defaults stay minimal and readable over feature-rich. — inferred from README.md:1-3, 22. Priority order among these three: not stated.
- Primary user: someone starting a personal blog on Eleventy. — inferred from README.md:3; edge users (non-blog sites, multi-author, CMS-driven) not stated.

## 2. Project Profile & Active Lenses

- **Project type(s):** `website`. Evidence: Eleventy SSG with page routes (`eleventy.config.js:131-154`, input `content`, output `_site`); `content/sitemap.xml.njk:1-5` emits `/sitemap.xml`; Atom feed (`eleventy.config.js:63-86`); content meant to be found (`_includes/layouts/base.njk:7` meta description). Not `web-app`: no SPA, no auth-gated routes (README.md:48-49). Not `api`/`cli`/`library`: no `bin`, no `main`/`exports` (`package.json:1-47`).
- **Characteristics:** `is-public` (judgment call, inferred): live demos on the open internet (README.md:83-86), Netlify/Vercel deploy configs (`netlify.toml:1-3`, `vercel.json`), README treats it as "public-facing" (README.md:113). Not detected: `handles-auth`, `handles-pii`, `handles-payments` (no such code; author email in `_data/metadata.js:8` is a placeholder), `has-database` (no DB), `is-multilingual` (single `language: "en"`, `_data/metadata.js:4`), `must-be-accessible` (no statement/VPAT/mandate found; `not found`).
- **Active lenses:**

| Lens | Why it's active (or off) | Enforced in |
|---|---|---|
| `seo` | active — type `website`: sitemap, feed, meta description, per-page `<title>` (`base.njk:6-7`) | `/story-time`, `/look-and-feel`, `/peer-review`, `/demo-day` |
| `ux` | active — type `website`: navigation, layouts, responsive CSS, dark-mode styles (`css/index.css:23`) | `/story-time`, `/look-and-feel`, `/demo-day` |
| `security` | active (needs user confirmation) — `is-public`; README already documents a CSP trade-off (README.md:111-116); supply chain via monthly Dependabot (`.github/dependabot.yml:8-18`) | `/story-time`, `/peer-review`, `/demo-day` |
| `accessibility` | off — `must-be-accessible` not found; no statement, VPAT or legal mandate in repo. Baseline a11y (skip link, `aria-current`, `base.njk:43,53`) is covered by the Designer baseline | — |
| `i18n` | off — single locale (`_data/metadata.js:4`) | — |
| `data` | off — no database, only files and front matter | — |
| `api` | off — no route handlers, no OpenAPI | — |
| `cli` | off — no `bin` entry (`package.json`) | — |
| `library` | off — no `main`/`exports`; consumed by cloning, not as a dependency (README.md:16-19) | — |

- **Active-lens load:** 3 lenses active (`seo`, `ux`, `security`). Below the elevated-load threshold.

## 3. Technical Constraints

- **Stack / runtime:** Eleventy `^3.1.7` static site generator, ES modules (`package.json:4,34`), Nunjucks for Markdown and HTML templates (`eleventy.config.js:142-146`), Node `>=18` (`package.json:22-24`; `.nvmrc:1` pins 22). Language: JavaScript only; no TypeScript found.
- **Patterns to follow:** content lives under `content/`, layouts and includes under `_includes/`, global data under `_data/`, filters under `_config/` (`eleventy.config.js:149-154`, `:7`); static assets in `public/` are passthrough-copied (`eleventy.config.js:24-28`); blog posts need the `posts` tag (README.md:101); front matter `draft` must be boolean, validated by Zod (`_data/eleventyDataSchema.js:8-10`); drafts are excluded from full builds (`eleventy.config.js:12-20`).
- **Off-limits:** server-side runtime (output is static `_site`; `netlify.toml:1-3`); not stated beyond that. Inline `<style>` is the current default and conflicts with a strict CSP; switching is a documented choice (README.md:113-116), not a violation.

## 4. Quality Bars (Definition of Done defaults)

- **Testing:** `not found` — no test script (`package.json:6-15`), no test files, no CI workflow (only `.github/workflows/gh-pages.yml.sample`). The only automated gate is that `npm run build` exits cleanly (`package.json:7`). Bar adopted here: every increment must build without error. Coverage targets are deliberately omitted because the code does not follow any.
- **Accessibility:** baseline only — keep the skip link, landmarks and `aria-current` (`base.njk:43,53,59`) and accessible heading deep links (README.md:72). No WCAG level declared (`not stated`).
- **Performance:** keep the README claims true: 0 CLS (images carry `width`/`height`) and lazy, async-decoded images (README.md:64-66; `eleventy.config.js:89-107`). Lighthouse 100s are claimed (README.md:53) but not enforced by any script (`not found`).
- **Security:** no secrets in the repo or the built output (not stated, proposed default for a public static site); third-party dependency additions need justification (`not stated`).

## 5. Conventions

- **Naming / structure:** tabs, 2-wide, LF, final newline, UTF-8 (`.editorconfig:3-9`); lowercase single-word file names under `content/` (e.g. `firstpost.md`, `tag-pages.njk`).
- **Commits / branches:** short imperative subjects, sometimes with issue refs ("Fixes #249", "Upgrade core to v3.1.6", "Fix npm audit"); no Conventional Commits; dependency bumps via monthly Dependabot with a 7-day cooldown (`.github/dependabot.yml:10-13`); work arrives by merged PRs (caller's git summary: 551 commits, latest `cf0cc1f` "v3.1.7" 2026-10-15). One feature branch per `.spark/<feature>` is proposed, not observed.
- **Language:** all artifacts, code and reports in English regardless of chat language (site language `en`, `_data/metadata.js:4`).

## 6. Non-Negotiables

- Output stays fully static and deployable to a subfolder without content changes (HtmlBasePlugin, `eleventy.config.js:60`; README.md:50; `build-ghpages` script `package.json:9`). Falsifiable: `npm run build-ghpages` succeeds and links resolve under the prefix.
- Drafts never appear in a production build (`eleventy.config.js:17-19`; README.md:70).
- `npm run build` succeeds on a fresh clone with the pinned Node (`.nvmrc:1`) before anything is released.
- Not stated by the user: further non-negotiables. None are invented here.

## 7. Delivery & Handoff

<!-- Nothing here is stated by the user; no CODEOWNERS or PR-approval rule found. Defaults apply. -->

- **Release mode:** not stated — default `direct` applies.
- **Approver:** n/a (default).
- **Target branch:** n/a (default); git history shows `main` with merged PRs, but no declared approval rule.
- **Ticket-reference format:** `#123` observed in commit subjects ("Fixes #249"); not declared — default `none` applies until the user confirms.
- **Tracker write-back:** not stated — default `none`.
- **Terminal status:** not stated — default `released`.

## 8. QA Method

<!-- Proposed, needs the user's confirmation. This is the "yes" case, so no ceremony changes behavior. -->

- **Browser-observable surface:** `yes` — proposed, needs user confirmation. After `npm run build` the site is browsable, and `npm start` serves it at `http://localhost:8080` (`package.json:7,10`; Eleventy dev-server default port, not stated in the repo). Live-browser QA stays the method.
- **Substitute verification method:** n/a — surface is `yes`, so no substitute is read.

## 9. Project Context

- **Shape:** `brownfield` — has source files and a manifest (`package.json:1`).

**Product brief:**

- **Primary user:** `inferred from README.md:3` — someone starting a blog with Eleventy.
- **Problem today:** `inferred from README.md:1-3` — a working, opinionated blog skeleton so they don't assemble one from docs.
- **Smallest version:** `not stated`
- **Success signal:** `inferred from README.md:53-55` — Lighthouse 100s, zero layout shift, clean clone-and-run. Adoption metrics: `not stated`.
- **Stack:** `inferred from package.json:22-46, eleventy.config.js:1-5`.
- **Non-negotiables:** `not stated` by user; §6 entries are inferred from the repo.

**System picture:**

- **Stack & entry points:** `inferred from package.json:6-15, eleventy.config.js:10` — Eleventy 3 config exported as the entry; `content/index.njk` is the home page.
- **Module structure:** `inferred from eleventy.config.js:149-154` — `content/` (pages, `blog/` posts), `_includes/layouts/` (base, home, post), `_data/` (metadata, schema), `_config/filters.js`, `css/`, `public/`, output `_site/`.
- **Data model:** `not found` — no persistence; site metadata at `_data/metadata.js:1-11`, posts are Markdown with front matter and the `posts` tag.
- **Test practice:** `not found` — `package.json:6-15` has no `test` script; no test files.
- **Conventions:** `inferred from .editorconfig:1-9`; no CONTRIBUTING.md (`not found`).
- **How to run:** `inferred from package.json:7,10, README.md:30-42` — `npm install`, `npm run build`, `npm start`.
- **Known pain points:** `not stated`; visible from the repo: placeholder values (`metadata.js:2-9`, `eleventy.config.js:79-83` duplicates title, base URL and author instead of reading `_data/metadata.js`); README.md:98 points to `content/about/index.md` but the file is `content/about.md`.

---

## Amendments

| Date | Change | Why |
|---|---|---|
| 2026-10-27 | Initial constitution (dark mode, no user input; defaults inferred from the repo) | Project kickoff |

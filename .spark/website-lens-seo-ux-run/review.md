# Review Report: website-lens-seo-ux-run

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Whole-file diff of 11ty/eleventy-base-blog @ `cf0cc1f` against the empty tree; `spec.md` (approved) as the plan |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-10-27 |

<!-- Handoff: overwrite in place, never append. See templates/review-report.md. -->

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** The run conforms to the spec. Every observed-behavior AC traces to code with no contradiction. Every `[GAP]` AC is confirmed as a gap. Two spec inaccuracies (F14, F15) are Minor. The target findings stay open by design. Evaluation mode is degraded (static read plus HTTP fetch, no browser).
- **Open:** `17 open` (target findings, open by design): Blockers: none; Majors: `F1`, `F2`, `F3` (Minors/Nits: see §3)
- **Binding ruling:** §6 Verdict and the gate checklist below.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed.

## 1. Scope

- **Reviewed:** `git diff 4b825dc…HEAD` on `eleventy.config.js`, `_data/`, `_includes/`, `content/` (all `.md`/`.njk`/`.js`, `.xsl` skimmed), `css/` (skimmed for responsive rules only), `package.json`, `netlify.toml`, `vercel.json`, `public/img/.gitkeep`. I added `_config/filters.js` to the scope even though the caller's pathspec left it out. `eleventy.config.js:7` imports it, and AC-1.1, AC-3.3 and AC-2.2 depend on it.
- **Not reviewed:** `package-lock.json` (it was only read by `npm audit`), binary images, `README.md`, `.github/`, and `css/` beyond what is listed above. The `ux` lens is not a review-phase lens here.
- **Evaluation mode (degraded):** static source read, plus a grep of the existing **dev-mode** `_site/` build, plus read-only HTTP `fetch` against the dev server on `:8080` (dev mode: drafts are included and images use `/.11ty/image` URLs). No browser, and no production build: the target is read-only and I was told to write nowhere else. `npm audit` was run read-only, and `git status` confirmed the tree was unchanged afterwards.
- **Template note:** the caller named `/opt/aspark/templates/review.md`, which does not exist. I used `/opt/aspark/templates/review-report.md`.
- **Lenses applied:** `seo` (§1-§5 review items), `security` (§1, §4, §5; §2/§3 are n/a because there is no auth and no data access). Standard `anti-generosity` applied.

## 2. Plan Conformance

There is no plan.md. The spec's stories stand in as tasks. "Conforms" means each AC matches the code as the spec describes it.

| Task | Implemented as planned? | Note |
|---|---|---|
| US-1 | ⚠️ | Code matches AC-1.1..1.4 and AC-1.7. For AC-1.5 the `[GAP]` is confirmed, but the spec's "observed today" list leaves out `/about/` and `/blog/` (F14) |
| US-2 | ✅ | AC-2.1..2.7 trace to `post.njk`, `eleventy.config.js:12-20,57,89-107` |
| US-3 | ✅ | AC-3.1..3.4 trace. AC-3.5's precondition does not exist in the content: no tag carries only a draft (`fifthpost.md:1-5` has no tags) |
| US-4 | ✅ | AC-4.1..4.3 trace. `[GAP]` AC-4.4 confirmed (F1) |
| US-5 | ✅ | `[GAP]` AC-5.4..5.7 confirmed (F2, F4, F5, F6). AC-5.1..5.3 and AC-5.8 trace |
| NFR-5 / A6 | ⚠️ | A6's premise that "headers are set by the host, not the repo" is wrong: both deploy configs can set headers (F15) |

## 3. Findings

All F1-F13 rows are about the target. They stay `open` by design: the run is retrospective and fixes belong to a later feature (spec A1). F14-F15 are about the spec.

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `eleventy.config.js:77-85` | Rule: seo §3 / AC-4.4. The feed hardcodes `title: "Blog Title"`, `base: "https://example.com/"` and author `"Your Name"` instead of reading `_data/metadata.js`. The on-page setup instructions (`home.njk:8`) tell adopters to edit only `metadata.js`, so feed entry links will keep pointing at example.com. Fix: `import metadata from "./_data/metadata.js"` and pass `metadata.title/description/url/author`. | open |
| F2 | Major | `_includes/layouts/base.njk:6-7` | Rule: seo §3 "unique title/description, not one global default" / AC-5.4. `/`, `/blog/`, `/about/`, `/tags/` and `404` all fall back to `metadata.title`, and every non-post page also falls back to `metadata.description` (HTTP: `/` and `/nope/` both return `<title>Eleventy Base Blog v9</title>`). Fix: give `index.njk`, `blog.njk`, `about.md`, `tags.njk` and `404.md` their own `title`/`description` front matter, and compute a description in `tag-pages.njk:13-19`. | open |
| F3 | Major | `package.json:34,42` (lockfile) | Rule: NFR-5 "no high/critical advisories" / security §4. `npm audit` reports 2 high: `zod@4.4.3` (direct, GHSA-mrhx-c7xc-m3w5, <4.6.6) and `markdown-it@14.3.2` via `@11ty/eleventy` (GHSA-gfr2-rv44-r23c). Both are build-time only and their input is the author's own content, so real exploitability is low, but NFR-5 is stated as a hard bar. Fix: bump `zod` to `^4.6.6` and update the lockfile so `markdown-it` resolves to >=14.3.3 (`fixAvailable: true` for both). | open |
| F4 | Minor | repo root / `public/` (absent) | Rule: seo §1 / AC-5.5. There is no `robots.txt` (HTTP 404 on the dev server), so `sitemap.xml` is not discoverable through it. Fix: add `public/robots.txt` with `Sitemap: <metadata.url>sitemap.xml`, or add a `robots.txt.njk` template that builds the URL from `metadata.url`. | open |
| F5 | Minor | `_includes/layouts/base.njk:3-41` | Rule: seo §2-§3 / AC-5.6. No `<link rel="canonical">` and no `og:*`/Twitter tags (HTTP: absent on `/` and `/tags/second-tag/`). Fix: emit `canonical` and `og:url` from `page.url \| htmlBaseUrl(metadata.url)`, and `og:title`/`og:description` from the same values as `<title>`/description. | open |
| F6 | Minor | `content/sitemap.xml.njk:8-9` | Rule: seo §1 / AC-5.7. The sitemap iterates `collections.all`, so it includes `/feed/feed.xml`, and in dev mode also the draft. Fix: filter on `page.outputPath` ending in `.html` (or exclude the feed with `eleventyExcludeFromCollections` through `templateData`). | open |
| F7 | Minor | `content/tag-pages.njk:11` | Rule: seo §1 "sitemap lists the public routes". `eleventyExcludeFromCollections: true` keeps the 4 indexable tag pages out of `sitemap.xml` (10 `<url>` entries, none under `/tags/<slug>/`). Fix: drop the exclusion, or add a second loop over the tag keys in `sitemap.xml.njk`. | open |
| F8 | Minor | `content/sitemap.xml.njk:13` | Rule: seo §1. `lastmod` uses `page.date`. For non-post pages that is the file's mtime, which resets on every clone or checkout, so it carries no information. Fix: use the newest post date for list pages, or omit `lastmod` where there is no content date. | open |
| F9 | Minor | `content/content.11tydata.js:2`, `_includes/layouts/home.njk:4-14` | Rule: AC-1.5 `[GAP]`. The directory-wide `home` layout puts the template-author instructions on 9 built pages (`/`, `/about/`, `/blog/`, `/tags/`, 4 tag pages, `404.html`). Fix: set `layout: layouts/base.njk` in `content.11tydata.js` and set `layout: layouts/home.njk` only in `index.njk`. | open |
| F10 | Minor | `netlify.toml:1-3`, `vercel.json:1` | Rule: security §1. No security headers are configured (no CSP, `X-Content-Type-Options`, or `frame-ancestors`), and the dev server sends none. Both configs support repo-level headers (`[[headers]]`, `"headers"`). Spec §6 puts hosting headers out of scope, so the severity stays Minor. Fix: add a baseline header block that allows `style-src 'unsafe-inline'` (the documented trade-off). | open |
| F11 | Minor | `eleventy.config.js:95` | Rule: error handling / constitution §4 "0 CLS". `failOnError: false` lets a broken image pass the build unoptimized and without `width`/`height`, which breaks the CLS bar without failing the build. Fix: set `failOnError: true` for production (`ELEVENTY_RUN_MODE === "build"`). | open |
| F12 | Minor | `_includes/postslist.njk:3` | Dead logic: `url` is never defined in this scope, so `postlist-item-active` is never applied and `css/index.css:270` is dead. Fix: compare against `page.url`, or remove the class and its CSS. | open |
| F13 | Nit | `_config/filters.js:41`, `eleventy.config.js:13-14`, `base.njk:50,71` | (a) `(b, a) => b.localeCompare(a)` sorts ascending but swaps the parameter names; rename to `(a, b)`. (b) A draft with no `title` renders as `"undefined (draft)"`; guard on `data.title`. (c) A visually hidden `<h2>` comes before the page `<h1>` (NFR-3 records this as observed). (d) The build timestamp comment makes every page differ on every build; drop it. | open |
| F14 | Minor | `spec.md` AC-1.5, A8 | Artifact accuracy: the "observed today" list (`/`, `/404.html`, `/tags/`, tag pages) leaves out `/about/` and `/blog/`, which also render the message box (`grep message-box _site`). The AC's verdict does not change. Fix: add both routes to AC-1.5 and A8. | open |
| F15 | Minor | `spec.md` A6, NFR-5 | Artifact accuracy: A6 says response headers "are set by the host, not the repo (`netlify.toml:1-3`)". Both deploy files can set headers (see F10), so the stated reason for scoping headers out is false. The scoping decision itself is the user's to keep. Fix: restate A6 as "headers are configurable in the repo but out of scope for this run". | open |
| F16 | Nit | `content/sitemap.xml.njk:7-8` | The `xmlns:xhtml` namespace is declared but never used, and the loop variable `page` shadows Eleventy's global `page`. Fix: drop the namespace and rename the loop variable to `entry`. | open |
| F17 | Nit | `_includes/layouts/base.njk:67` | The footer prints `eleventy.generator` (the exact version) on every page. The information disclosure is trivial. Fix: print it without the version, or keep it as a conscious starter choice. | open |

## 4. Requirements Traceability

Verdict key: PASS/FAIL comes with the observable that decides it. `⚠ not-verified-live` means the code was traced statically but the AC needs a browser or a production build that I could not run.

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `index.njk:9-15`, `filters.js:15-29`, `postslist.njk:1-8` | ⚠ not-verified-live (prod build: dev includes the draft) |
| AC-1.2 | `index.njk:17-20` | ⚠ not-verified-live |
| AC-1.3 | `base.njk:43-56` | ⚠ not-verified-live ("visible") |
| AC-1.4 | `blog.njk:9-10` | ⚠ not-verified-live (prod build) |
| AC-1.5 `[GAP]` | `content.11tydata.js:2`, `home.njk:4-14` | FAIL as expected: message box on 9 pages (F9, F14) |
| AC-1.6 | `css/index.css:60,76,188` | ⚠ not-verified-live (no 375px viewport) |
| AC-1.7 | `404.md:5-7` | PASS: HTTP `/nope/` returns 404 with "Content not found." and `<a href="/">home</a>` |
| AC-2.1 | `post.njk:7,10` | ⚠ not-verified-live |
| AC-2.2 | `post.njk:11-14`, `filters.js:36-38` | ⚠ not-verified-live |
| AC-2.3 | `post.njk:19-28` | ⚠ not-verified-live |
| AC-2.4 | `fourthpost.md:11`, `eleventy.config.js:89-107` | ⚠ not-verified-live (markup has avif/webp, alt, 350x685, lazy; CLS not measured) |
| AC-2.5 | `base.njk:40,60`, `eleventy.config.js:112` | ⚠ not-verified-live (JS behavior) |
| AC-2.6 | `eleventy.config.js:57` | ⚠ not-verified-live |
| AC-2.7 | `eleventy.config.js:17-19` | ⚠ not-verified-live (prod build) |
| AC-3.1 | `tag-pages.njk:14,22` | ⚠ not-verified-live (HTTP tab title `Tagged &#39;second tag&#39;` is correct; the click step was not performed) |
| AC-3.2 | `tag-pages.njk:24-25` | ⚠ not-verified-live |
| AC-3.3 | `tags.njk:4`, `filters.js:36-42` | ⚠ not-verified-live |
| AC-3.4 | `tags.njk:1-8` (no `eleventyNavigation`) | ⚠ not-verified-live |
| AC-3.5 | `eleventy.config.js:17-19` | ⚠ not-verified-live (precondition absent in the content) |
| AC-4.1 | `base.njk:8`, `eleventy.config.js:67-72` | ⚠ not-verified-live |
| AC-4.2 | `eleventy.config.js:63-76` | ⚠ not-verified-live (dev feed: 5 entries incl. the draft) |
| AC-4.3 | `eleventy.config.js:28,66` | ⚠ not-verified-live (XSL returns HTTP 200; the rendering was not observed) |
| AC-4.4 `[GAP]` | `eleventy.config.js:79,83` | FAIL as expected: feed "Blog Title" vs site "Eleventy Base Blog v9" (F1) |
| AC-4.5 | `eleventy.config.js:89-107` | ⚠ not-verified-live (dev feed holds `/.11ty/image` URLs) |
| AC-5.1 | `sitemap.xml.njk:1-17` | ⚠ not-verified-live (prod build) |
| AC-5.2 | `base.njk:6-7` | ⚠ not-verified-live |
| AC-5.3 | `base.njk:2,5` | PASS: all 13 built `.html` files carry the viewport tag; `lang="en"` |
| AC-5.4 `[GAP]` | `base.njk:6-7` | FAIL as expected (F2) |
| AC-5.5 `[GAP]` | absent | FAIL as expected: HTTP 404 (F4) |
| AC-5.6 `[GAP]` | absent | FAIL as expected (F5) |
| AC-5.7 `[GAP]` | `sitemap.xml.njk:8` | FAIL as expected: lists `feed.xml` (F6) |
| AC-5.8 | templates | PASS: `grep noindex _site` returns 0 files |
| NFR-1 | `eleventy.config.js:89-107` | ⚠ not-verified-live (Lighthouse is QA's) |
| NFR-2 | templates server-render all journey content; only `base.njk:40` is JS | ⚠ not-verified-live |
| NFR-3 | `base.njk:6-7,50` | ⚠ not-verified-live (lengths look within limits statically; h2 before h1, see F13) |
| NFR-4, NFR-6 | `base.njk:43,53,59` | ⚠ not-verified-live (ux/a11y, not this phase) |
| NFR-5 | `metadata.js:8` | FAIL: `npm audit` reports 2 high (F3). The email appears in no template or built page (grep) |
| NFR-7 | `package.json:7,9` | ⚠ not-verified-live (no build run; the target is read-only) |
| NFR-8 | — | n/a (spec) |

## 5. What Was Checked

- [x] Correctness: each AC traced to code (static); 3 ACs decided by HTTP or grep observables
- [x] Non-functional: NFR-5 checked by `npm audit` and grep; the others are traced but not live
- [x] Error handling: `failOnError` (F11), Zod schema `eleventyDataSchema.js:12-14` throws on a non-boolean `draft`
- [x] Security: Nunjucks autoescape is on (HTTP output `&#39;`); `\| safe` only on author content; no secrets; headers (F10); audit (F3)
- [ ] Tests: none exist (constitution §4 `not found`); the build was not run because the target is read-only
- [x] Readability: F12, F13, F16

## 6. Verdict

As the caller ruled, this review gates the retrospective run's conformance to its spec, not the target's quality, and on that question it passes. The spec cites code locations for its ACs, and every one I checked holds at `cf0cc1f`. The draft preprocessor, feed config, sitemap loop, layouts and tag pagination do what US-1..US-5 claim. All six `[GAP]` ACs (1.5, 4.4, 5.4-5.7) are real, confirmed by HTTP fetch or by grep of the built output. Two spec inaccuracies need a wording fix. AC-1.5/A8 undercount the affected pages (F14). A6 gives a false reason for scoping headers out (F15). Neither changes a verdict.

The target itself has three open Majors. The feed's hardcoded metadata will send adopters' feed links to example.com (F1). One title and description repeat across all non-post pages (F2). `npm audit` reports 2 high advisories, which fails NFR-5 as written (F3). There are also 9 Minors and 4 Nits. All of these stay open by design for a later feature.

What I could not check: every browser-observable behavior (the 375px layout, CLS, the heading-anchor JS, XSL rendering, focus and keyboard behavior), and every production-build claim (draft exclusion, prod feed image URLs, prod sitemap, `build-ghpages` prefix), because I could neither build nor drive a browser. Those 28 rows are marked `⚠ not-verified-live` and remain for `/demo-day`. Standard applied: `anti-generosity`. Evaluation mode: static plus HTTP, degraded.

---

## ✅ REVIEW GATE

*Gate scope for this run (caller ruling): the run's conformance to the spec. Target findings are open by design and are not a gate input.*

- [x] No open Blocker findings
- [ ] No open Major findings: F1, F2, F3 are open target findings, not waived. Per the caller's ruling they are excluded from this run's gate.
- [x] Every Must AC traces to implementing code; no constitution non-negotiable is violated by the source as read (§6 build checks not run: target read-only)
- [x] All plan deviations documented: no plan.md; the spec deviations are F14 and F15, recorded as Minor
- [ ] Test suite runs green: no test suite exists (constitution §4); the build was not run (read-only target)
- [x] Line budget respected: Ist ~140 / Soll ~150 (excluding HTML comments), self-reported
- [x] Status set to `passed` (run-conformance gate only)

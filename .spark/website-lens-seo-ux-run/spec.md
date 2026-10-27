# Spec: reader-journey

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), Designer (`/look-and-feel`) |
| **Status** | `approved` |
| **Date** | 2026-10-27 |
| **Ticket** | none |

**Handoff**
- **Status:** `approved` (dark-mode factory line took the recommended gate for issue #105; A5-A8 accepted as risk; mirrors the header table; authoritative for `Status`).
- **Summary:** Retrospective spec of what a blog reader can do today (home, find post, read, follow tag, subscribe via Atom) and what search engines can discover; records observed behavior as ACs and the gaps as explicit `[GAP]` ACs.
- **Open:** `none` blocking; A5-A8 accepted as risk in dark mode (no user to answer), kept open in §3
- **Binding ruling:** §4 User Stories for the current stories; §7 Clarifications for what changed since the last round and why
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed.

## 1. Problem & Goal

- **Problem:** Nothing is wrong to build; the problem is that the starter's reader journey is undocumented and untested (`constitution.md §4`: no test script, no CI). An adopter who edits the layouts cannot tell which behaviors are intended and which are accidents. The visitor who hurts when it silently breaks is the reader of an adopter's blog (constitution §1: primary user is someone starting a personal blog on Eleventy).
- **Goal:** One checkable description of the journey home -> post -> tag -> feed, plus the search-engine discoverability surface, so later changes can be verified against it. Where the shipped site falls short of the active `seo`/`ux`/`security` lenses, the shortfall is recorded, not fixed (nothing may change in this run).
- **Success signal:** A QA tester can walk every AC below in a browser at `http://localhost:8080/` (or by viewing `_site/` output) and mark each pass, fail, or `[GAP]`-confirmed with no interpretation needed.
- **Why now:** The lenses are newly active (`constitution.md §2`); this spec is their baseline. Without it, the next layout edit has nothing to regress against.

## 2. Target Users

- **Reader (primary):** a person who lands on the home page of an adopter's blog, on desktop or phone, wants to find and read a post and optionally follow a topic or subscribe.
- **Feed subscriber:** a reader using a feed reader app who pastes or auto-discovers the Atom URL.
- **Search crawler:** an automated indexer that does not run JavaScript.
- **Adopter (secondary, indirect):** the blog author who clones the starter; they benefit from correct defaults but are not the actor in any story.

Grounding: `constitution.md §9` (entry point `content/index.njk`, layouts under `_includes/layouts/`, run via `npm run build` / `npm start`). Layout, feed and sitemap facts were re-read from source because this feature touches exactly those areas (§9 rule (a)).

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | **This is a retrospective spec.** The site already exists and nothing may be changed. ACs describe observed behavior at `cf0cc1f`; they are not new requirements. `[GAP]` ACs describe lens-driven expectations the site does not meet today and are expected to fail until a future feature fixes them. | Accepted |
| A2 | The current `_site/` was produced by a dev-mode build (it contains the draft `fifthpost` at `/blog/fifthpost/`, in the sitemap, feed and home list). Production (`npm run build`) must exclude drafts (`eleventy.config.js:17-19`, constitution §6). Draft-related ACs are verified against a production build, not the current `_site/`. | Accepted; QA runs `npm run build` first |
| A3 | Content is placeholder (`metadata.js:2-9`: `example.com`, "Your Name"). ACs test structure, not copy. | Accepted |
| A4 | Original phrasing of the request: "Reader journey ... plus discoverability for search engines (sitemap, metadata)". Translated to the reader outcomes in §4. | Recorded |
| A5 | Is the `[GAP]` set (no `robots.txt`, no canonical, no Open Graph, one repeated title/description on non-post pages) intended starter minimalism (constitution §1: "defaults stay minimal") or a defect? | **Open** - user decides; US-5 is Should until then |
| A6 | The `security` lens is "active, needs user confirmation" (constitution §2). Response headers are set by the host, not the repo (`netlify.toml:1-3`); is a headers requirement meaningful? | **Open** - NFR-5 scoped to repo-controlled facts until answered |
| A7 | Feed hardcodes `https://example.com/`, title "Blog Title" and "Your Name" (`eleventy.config.js:77-85`), while the site uses `_data/metadata.js` (title "Eleventy Base Blog v9"). Two sources of truth: placeholder duplication or defect? (constitution §9 lists it as a pain point.) | **Open** - AC-4.4 documents the mismatch as `[GAP]` |
| A8 | The `home.njk` onboarding "message-box" renders on every page using the home layout, including `/404.html`, `/tags/` and tag pages (`content.11tydata.js:1-3`, `home.njk:4-13`). Intended for first run only. | **Open** - recorded as `[GAP]` AC-1.5 |

## 4. User Stories

### US-1 (Must): Land on the home page and find a post

> As a reader, I want the home page to show the latest posts and a way to reach the rest, so that I can find something to read within a click or two.

**Acceptance criteria:**

- [ ] AC-1.1: Given a production build (4 non-draft posts), when I load `/`, then one `<h1>` reads "Latest 3 Posts" and exactly 3 posts are listed newest first, each a link with its title and a month-year date (`index.njk:11-15`, `postslist.njk`).
- [ ] AC-1.2: Given the home page with more than 3 posts, when I read below the list, then "N more post(s) can be found in the archive" appears, N equals total posts minus 3, and "the archive" links to `/blog/`.
- [ ] AC-1.3: Given any page, when I look at the header, then a site-title link to `/` and a navigation list with Home, Archive, About and Feed links is visible, and the entry for the current page carries `aria-current="page"` (`base.njk:43-56`).
- [ ] AC-1.4: Given `/blog/`, when it loads, then every non-draft post is listed newest first and each link opens that post.
- [ ] AC-1.5: `[GAP]` Given a first-time reader on `/`, when the page loads, then no template-author instructions ("Edit `_data/metadata.js`...") are visible. **Observed today:** the message box renders on `/`, `/404.html`, `/tags/` and every tag page (`home.njk:5-13`).
- [ ] AC-1.6: Given the home page at 375px viewport width, when it loads, then no horizontal scroll appears and post links are readable and not clipped or overlapping.
- [ ] AC-1.7: Given an unknown URL such as `/nope/` on the dev server, when requested, then the 404 page shows "Content not found." with a "home" link to `/` (`404.md:5-7`).

### US-2 (Must): Read a post and move between posts

> As a reader, I want a post to be readable and to link to related reading, so that I can keep going after the first article.

**Acceptance criteria:**

- [ ] AC-2.1: Given `/blog/firstpost/`, when it loads, then the page has exactly one `<h1>` equal to the post title, a `<time>` element with a machine-readable `datetime` and readable text, and the body content (`post.njk:7-17`).
- [ ] AC-2.2: Given a post with tags, when I view the metadata line, then each tag is a link to `/tags/<slug>/` (`post.njk:11-14`) and the internal `posts` tag is not shown.
- [ ] AC-2.3: Given a post with neighbors in date order, when I scroll to the end, then "Previous" and/or "Next" links point to the adjacent posts; the oldest post has no "Previous" and the newest no "Next" (`post.njk:19-28`).
- [ ] AC-2.4: Given `/blog/fourthpost/`, when it loads, then the possum image is served in responsive formats with non-empty `alt`, explicit `width`/`height` and `loading="lazy"`, and the page shows no layout shift.
- [ ] AC-2.5: Given a post with a `##` heading, when I hover or focus it, then a heading anchor link appears and activating it updates the URL hash; with JavaScript disabled the heading and its `id` still exist and the page is fully readable.
- [ ] AC-2.6: Given a code block in a post, when I press Tab through the page, then the block is keyboard-focusable (`eleventy.config.js:57`).
- [ ] AC-2.7: Given a production build, when I request `/blog/fifthpost/` (draft), then the page does not exist and the post is absent from the home page, archive and tag pages.

### US-3 (Must): Follow a tag to related posts

> As a reader, I want to click a tag and see all posts with that tag, so that I can read more on a topic I liked.

**Acceptance criteria:**

- [ ] AC-3.1: Given a post tagged "second tag", when I click that tag, then I land on `/tags/second-tag/` with the heading "Tagged “second tag”" and the browser tab title "Tagged 'second tag'".
- [ ] AC-3.2: Given a tag page, when it loads, then it lists every non-draft post carrying that tag, newest first, each linking to the post.
- [ ] AC-3.3: Given a tag page, when I click "all tags", then `/tags/` opens and lists every tag alphabetically as links, with no `posts` entry.
- [ ] AC-3.4: Given `/tags/`, when I look at the header navigation, then there is no "Tags" item; `/tags/` is reachable only from a tag page's "all tags" link. Observed behavior, recorded so a change is deliberate (`tags.njk` has no `eleventyNavigation`).
- [ ] AC-3.5: Given a tag whose only post is a draft, when the production build runs, then either no page for that tag is emitted or it shows an empty list without error. **Unverified** - QA records which (C3).

### US-4 (Must): Subscribe via the Atom feed

> As a feed subscriber, I want a working Atom feed that my reader app can discover and parse, so that I get new posts without visiting the site.

**Acceptance criteria:**

- [ ] AC-4.1: Given any HTML page, when I view the source, then `<head>` contains `<link rel="alternate" type="application/atom+xml" href="/feed/feed.xml">` (`base.njk:8`), and the header "Feed" link opens `/feed/feed.xml`.
- [ ] AC-4.2: Given `/feed/feed.xml`, when fetched, then it is well-formed Atom with a `<feed>` root, a self link, an `<updated>`, and at most 10 `<entry>` items, each with title, absolute link, id, updated and HTML content (`eleventy.config.js:73-76`).
- [ ] AC-4.3: Given `/feed/feed.xml` opened in a browser, when it loads, then `pretty-atom-feed.xsl` renders a human-readable page and the stylesheet URL returns 200 (`eleventy.config.js:28,66`).
- [ ] AC-4.4: `[GAP]` Given the feed and the site, when I compare the feed title with the `<title>` of `/`, then they are identical. **Observed today:** feed "Blog Title" vs site "Eleventy Base Blog v9"; feed author "Your Name" vs "Your Name Here" (A7).
- [ ] AC-4.5: Given a production build, when I inspect feed entries, then no draft appears and image URLs in entry content resolve to real files, not `/.11ty/image/?src=...` dev-server URLs. **Unverified** - the dev-mode feed contains both; QA confirms on a production build.

### US-5 (Should): Be discoverable by search engines

> As a search crawler, I want a sitemap and per-page metadata in the server-rendered HTML, so that every public page is indexed with a meaningful title and description.

**Acceptance criteria:**

- [ ] AC-5.1: Given `/sitemap.xml`, when fetched, then it is valid sitemap XML with one absolute URL (built from `metadata.url`) and a `lastmod` for each public page: home, archive, about, tags index, each non-draft post.
- [ ] AC-5.2: Given a post page, when I view the source with JS disabled, then `<title>` and `<meta name="description">` are the post's own front-matter values and the body text is in the raw HTML.
- [ ] AC-5.3: Given any page, when I view the source, then `<html lang="en">` and a viewport meta tag are present.
- [ ] AC-5.4: `[GAP]` Given home, archive, about, tags-index, 404 and tag pages, when I read `<title>` and description, then each is unique. **Observed today:** home, archive, about, tags and 404 share the title "Eleventy Base Blog v9"; all of those and every tag page share one description (`base.njk:6-7`). Only posts with front-matter values are unique.
- [ ] AC-5.5: `[GAP]` Given `/robots.txt`, when requested, then it returns 200, does not `Disallow: /`, and references the sitemap. **Observed today:** the file does not exist.
- [ ] AC-5.6: `[GAP]` Given any indexable page, when I view the source, then it carries `<link rel="canonical">` and Open Graph tags (`og:title`, `og:description`, `og:url`). **Observed today:** none in any built page.
- [ ] AC-5.7: `[GAP]` Given `/sitemap.xml`, when I read the URLs, then it lists only HTML pages. **Observed today:** it includes `https://example.com/feed/feed.xml` and, in a dev build, the draft post.
- [ ] AC-5.8: Given any page, when I view the source, then no `<meta name="robots" content="noindex">` exists (confirmed absent today).

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Performance (`seo`) | On a production build served locally, Lighthouse performance on `/` and a post page is >= 95 (README claims 100); CLS = 0 on `/blog/fourthpost/`; LCP < 2.5s on a mid-range laptop. | /demo-day |
| NFR-2 | SEO: rendering | All journey content (post list, post body, tag lists, feed entries) is present in the unrendered server HTML; the site works with JS disabled except heading anchors. | /demo-day (view-source) + /peer-review |
| NFR-3 | SEO: metadata (`seo`) | Titles <= 60 chars and descriptions <= 160 chars on every page; uniqueness is `[GAP]` (AC-5.4); one `<h1>` per page and no skipped heading levels. Observed, not required: an `<h2>` "Top level navigation menu" precedes the `<h1>` on every page (`base.njk:50`). | /demo-day |
| NFR-4 | UX (`ux`) | Home -> post -> tag page -> feed link completes in <= 4 clicks and is completable at 375px width. Skip link is the first Tab stop and moves focus to `#main`; links show a visible focus state. A tag or archive with 0 posts shows a heading, not a blank page. | /look-and-feel + /demo-day |
| NFR-5 | Security (`security`) | No secrets in `_site/`; the placeholder author email (`metadata.js:8`) appears in no built page (verify by search); external links use https. Response headers are not set by the repo (A6). The README-documented inline-`<style>` CSP trade-off (`README.md:111-116`) is accepted, not a finding. `npm audit` shows no high or critical advisories at release. | /peer-review + /demo-day |
| NFR-6 | Accessibility | Baseline only (constitution §4): skip link, landmarks, `aria-current`, image `alt`. No WCAG level declared. | /look-and-feel |
| NFR-7 | Reliability | `npm run build` exits 0 on a clean clone with Node 22; `npm run build-ghpages` produces links that resolve under the prefix (constitution §6). | /demo-day |
| NFR-8 | Observability | N/A - static output, no runtime to log. | - |

## 6. Out of Scope

- Any code, template or config change (retrospective run; fixes for every `[GAP]` belong to a later feature).
- Site search, archive pagination, comments, newsletters, social sharing buttons.
- Structured data (JSON-LD), RSS/JSON feed variants, per-tag feeds.
- Multilingual support and `hreflang` (single locale, i18n lens off).
- Analytics, cookie banners, privacy pages (no PII or cookies found).
- A formal accessibility conformance level (accessibility lens off).
- Hosting-level concerns: HTTPS, HSTS, real response headers (host-owned, A6).
- Adding a "Tags" item to the navigation (AC-3.4 records current behavior only).

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-10-27 | Does "retrospective" allow ACs that fail today? | Yes: marked `[GAP]`, expected to fail; a failing `[GAP]` is a documented finding, not a QA defect against this run (A1). |
| C2 | 2026-10-27 | Which build do ACs run against? | A production build; the checked-in `_site/` is a dev build and would fail AC-2.7, AC-4.5 and AC-5.7 for the wrong reason (A2). |
| C3 | 2026-10-27 | Draft handling on tag pages (AC-3.5) and feed image URLs (AC-4.5) | Cannot be settled from source; stays Unverified for QA. |
| C4 | 2026-10-27 | Is the `[GAP]` set intentional minimalism? | Unresolved - moved to A5. |

## 8. Design Review

<!-- Filled by /look-and-feel. Empty design review = gate stays red for UI-facing features. -->

- **Overall impression:**
- **Heuristics findings:** (visibility of status, consistency, error prevention, recognition over recall, …)
- **Accessibility notes:** (contrast, keyboard navigation, focus order, labels)
- **Design risks & required changes:**

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked (done; A5-A8 parked as open)
- [x] Open questions are resolved or explicitly accepted as risk (A5-A8 accepted as risk, dark mode)
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions
- [x] Design review: N/A for this run, not performed (retrospective spec, nothing is built; the Design phase of the lenses is not exercised, see evidence.md)
- [x] Line budget respected: Ist ~140 / Soll ~250 (excluding HTML comments) - self-reported, no linter checks this
- [x] Status `approved` set by the dark-mode line's recommended gate, not by a person

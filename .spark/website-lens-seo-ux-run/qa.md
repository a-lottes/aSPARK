# QA Report: website-lens-seo-ux-run

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Running app (URL), `.spark/website-lens-seo-ux-run/spec.md` (the acceptance criteria) |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-10-27 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). **Orchestrator ruling (dark mode, not the QA Tester's):** the tester wrote `failed` against the target. Following the precedent of `.spark/website-lens-public-run/qa.md`, `passed` here certifies the QA *run* (every browser-observable row performed live or marked `not-verified-live`), not the target. Target findings B1-B5 and the 6 `[GAP]` ACs are open by design (spec A1, C1, §6: nothing in the target may change). The tester's verdict below stands unedited: I would not demo the target as a release candidate. The QA GATE checkboxes below are the tester's own and are left as written; they describe the target, not the run.
- **Verdict:** No, I would not demo this as a release candidate. As a retrospective baseline it holds: 6 `[GAP]` ACs are confirmed, 1 non-`[GAP]` AC fails (AC-2.6), NFR-5 fails on `npm audit`, and 8 rows are `⚠ not-verified-live`.
- **Open:** `5 open` - Blockers: none; Majors: `B4` (npm audit, 2 high); Minors: `B1`, `B2`, `B3`, `B5` (see §3). Target `[GAP]` findings stay open by design (spec A1, C1).
- **Binding ruling:** §5 Verdict and the gate checklist below.
- **On conflict:** the numbered body below wins for everything except `Status`.

## 1. Test Environment

- **App URL:** `http://127.0.0.1:8081/` (production build, `npm run build`, static `python SimpleHTTP/0.6`). `:8080` not used.
- **Evaluation mode:** live browser (Playwright MCP, Chromium). 33 browser tool calls (1 errored: a screenshot with an out-of-bounds path; its file was not kept). Read-only Bash: `grep`/`npm audit` in the target (target tree unchanged).
- **Browser / viewport(s):** 1280x800 desktop and 375x800 mobile. Real clicks for the Home -> post -> tag -> all tags -> Feed path at 375px; the draft, metadata and sitemap checks used `fetch()` inside the browser page (same-origin, raw server HTML), not view-source tabs.
- **Test data:** shipped placeholder content: 4 posts (`firstpost`..`fourthpost`), draft `fifthpost`, 4 tags. No accounts.
- **Constitution:** `/tmp/scratch/eleventy-base-blog/.spark/constitution.md` §8 says `Browser-observable surface: yes`, so no substitute method applies; the standard browser check ran.
- **Lighthouse:** not available (no binary; `npx --no-install lighthouse` failed with "missing packages"). No score is estimated.
- **Lenses applied (qa phase):** `seo` (title/meta/canonical/OG/lang/h1 per route, server-rendered content, CLS/LCP), `ux` (flow, mobile width, skip link and focus, touch targets, states), `security` (headers, cookies, secrets/PII in output and console, http links, audit). **Not applicable:** security auth/session, authz, IDOR/URL tampering, PII deletion (no auth, no data, no accounts); ux forms/validation (no form on the site); ux motion/`prefers-reduced-motion` (no animation observed, not tested). `accessibility`, `i18n` are off in the constitution and were not tested.
- **Standard:** `anti-generosity` applied.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Loaded `/`, read snapshot | h1 "Latest 3 Posts", 3 posts newest first, month-year | 1 h1 "Latest 3 Posts"; fourth (Sep 2018), third (Aug 2018), second (Jul 2018), each a link with `<time>` | ✅ pass |
| AC-1.2 | Read below the list | "N more post(s)" with N = 4-3, link to `/blog/` | "1 more post can be found in the archive", link `/blog/` | ✅ pass |
| AC-1.3 | Loaded `/`, `/blog/`, `/about/`; read nav and `aria-current` | Title link `/`, Home/Archive/About/Feed, current page marked | All 4 links present; `aria-current="page"` on Home, Archive, About respectively | ✅ pass |
| AC-1.4 | `/blog/` list parsed | All non-draft posts, newest first, links open posts | 4 posts: fourth, third, second, first; hrefs `/blog/<slug>/`; draft absent | ✅ pass |
| AC-1.5 `[GAP]` | Loaded `/` (browser), fetched other routes | No template-author message | Message ("Edit `_data/metadata.js`...") visible on `/`; `message-box` present on `/blog/`, `/about/`, `/tags/`, `/tags/second-tag/`, `/404.html` | ❌ fail - `[GAP]`-confirmed (also confirms review F14: `/about/` and `/blog/` are affected) |
| AC-1.6 | Resized to 375px, loaded `/`; measured 9 pages | No horizontal scroll; links not clipped/overlapping | `scrollWidth` = `clientWidth` = 375 on `/` and 8 other pages; post links 295px wide. Clipping/overlap was not measured and the screenshot was not inspected | ⚠ not-verified-live |
| AC-1.7 | Opened `/nope/` and `/404.html` | 404 page "Content not found." with home link | `/nope/` on this static server shows the Python server's "Error response / File not found", not the site page (the AC is scoped to the dev server). `/404.html` shows h1 "Content not found." and "Go home" link to `/` | ⚠ not-verified-live (unknown-URL routing is host-owned; the 404.html content is correct) |
| AC-2.1 | Opened `/blog/fourthpost/` (browser); parsed all 4 posts | One h1 = title, `<time datetime>`, body | Each post: exactly 1 h1 equal to the title; `<time datetime="2018-09-30">30 September 2018</time>`; body paragraphs | ✅ pass |
| AC-2.2 | Read tag links on all posts; clicked "second tag" | Tag links to `/tags/<slug>/`, no `posts` | e.g. third post: `second tag`, `posts with two tags`; no bare `posts` link | ✅ pass |
| AC-2.3 | Read Previous/Next on 4 posts | Oldest no Previous, newest no Next | first: Next only; second/third: both; fourth: Previous only | ✅ pass |
| AC-2.4 | Opened `/blog/fourthpost/`; measured CLS | Responsive formats, alt, width/height, lazy, no shift | `<picture>` with 2 `<source>`; `currentSrc` `.avif`; `alt` non-empty; `width=350 height=685`; `loading="lazy"`; layout-shift total = 0 | ✅ pass |
| AC-2.5 | Clicked "Jump to section titled: Section Header" | Hash updates; headings and ids exist without JS | Hash became `#section-header`. Raw server HTML (fetch) contains `<h2 id="section-header">`, ids on all h2/h3, and `<p>` body. Hover/focus reveal and a real JS-disabled load were not observed | ⚠ not-verified-live |
| AC-2.6 | Read `tabIndex` of both `<pre>` on `/blog/thirdpost/` | Each code block keyboard-focusable | First `<pre class="language-js">` `tabIndex` 0; second plain `<pre>` `tabIndex` -1 and overflows horizontally at 375px (scrollWidth 403 > 343) | ❌ fail (B1) |
| AC-2.7 | Requested `/blog/fifthpost/`; searched home, archive, tags, feed, sitemap | 404; absent everywhere | HTTP 404; "fifthpost" appears in none of 9 HTML pages, the feed (4 entries) or the sitemap | ✅ pass |
| AC-3.1 | Clicked "second tag" from third post at 375px | `/tags/second-tag/`, h1 `Tagged “second tag”`, tab title `Tagged 'second tag'` | URL `/tags/second-tag/`, tab title `Tagged 'second tag'`, h1 `Tagged “second tag”` | ✅ pass |
| AC-3.2 | Read all 4 tag pages | Every non-draft post with the tag, newest first | second-tag: fourth, third; another-tag: first; number-2: second; posts-with-two-tags: third | ✅ pass |
| AC-3.3 | Clicked "all tags" | `/tags/` alphabetical, no `posts` | another tag, number 2, posts with two tags, second tag; no `posts` | ✅ pass |
| AC-3.4 | Read nav on `/tags/` | No "Tags" nav item | Nav: Home, Archive, About, Feed | ✅ pass |
| AC-3.5 | Compared tag list to the draft | Empty or absent page for a draft-only tag | No tag is draft-only (the draft has no tags), so the precondition does not exist; no page emitted for any extra tag | ⚠ not-verified-live (not testable with this content) |
| AC-4.1 | Read `<head>` of 9 pages; clicked header Feed | `link rel=alternate type=atom` -> `/feed/feed.xml`; Feed opens it | `<link rel="alternate" href="/feed/feed.xml" type="application/atom+xml" ...>` on all 9; click opened `/feed/feed.xml` | ✅ pass |
| AC-4.2 | Parsed `/feed/feed.xml` | Atom `<feed>`, self link, updated, <=10 entries with title/link/id/updated/HTML content | No parser error; root `feed`; self `https://example.com/feed/feed.xml`; updated 2018-09-30; 4 entries, each with all fields, `content type="html"` | ✅ pass |
| AC-4.3 | Opened the feed in the browser; fetched XSL | Human-readable page; XSL 200 | Rendered "Web Feed Preview" with 4 linked items; `pretty-atom-feed.xsl` 200 | ✅ pass |
| AC-4.4 `[GAP]` | Compared feed title with `<title>` of `/` | Identical | Feed "Blog Title" vs site "Eleventy Base Blog v9"; feed author "Your Name" | ❌ fail - `[GAP]`-confirmed |
| AC-4.5 | Searched feed text; fetched an image URL | No draft; real image URLs, no `/.11ty/image/` | No "fifthpost", no `.11ty/image`; entry image `https://example.com/blog/fourthpost/xbVnp_hAou-350.png`; same path on this server returns 200 `image/png` | ✅ pass |
| AC-5.1 | Parsed `/sitemap.xml` | Valid; absolute URL + lastmod per public page | Valid XML; 9 `<url>`, all `https://example.com/...` with `lastmod`; home, archive, about, tags, 4 posts present | ✅ pass |
| AC-5.2 | Read raw HTML of the 4 posts | Own title and description; body in HTML | e.g. first post title "This is my first post.", description "This is a post on My Blog about agile frameworks."; `<p>` present | ✅ pass |
| AC-5.3 | Read 9 pages | `lang="en"`, viewport | `lang="en"` and viewport meta on all 9 | ✅ pass |
| AC-5.4 `[GAP]` | Read title/description on 9 routes | Each unique | `/`, `/blog/`, `/about/`, `/tags/`, `/404.html` all "Eleventy Base Blog v9"; one description "I am writing about my experiences as a naval navel-gazer." on all non-post pages including tag pages; posts unique | ❌ fail - `[GAP]`-confirmed |
| AC-5.5 `[GAP]` | Requested `/robots.txt` | 200, references sitemap | HTTP 404 | ❌ fail - `[GAP]`-confirmed |
| AC-5.6 `[GAP]` | Read `<head>` of 9 pages | canonical + og:title/description/url | `link[rel=canonical]` absent and 0 `og:` tags on all 9 | ❌ fail - `[GAP]`-confirmed |
| AC-5.7 `[GAP]` | Read sitemap URLs | HTML pages only | Includes `https://example.com/feed/feed.xml` (draft correctly absent). Tag pages also missing (review F7) | ❌ fail - `[GAP]`-confirmed |
| AC-5.8 | Searched 9 pages | No noindex | `noindex` found on none | ✅ pass |
| NFR-1 | Lighthouse attempted; CLS/LCP via PerformanceObserver on `/blog/fourthpost/` | Perf >= 95 on `/` and a post; CLS 0; LCP < 2.5s | Lighthouse unavailable, no score. Observed (unthrottled, local): CLS 0, LCP 108 ms (IMG), FCP 108 ms. CLS/LCP not measured on `/` | ⚠ not-verified-live (score not measured; CLS/LCP observed within the target on the post only) |
| NFR-2 | Parsed raw server HTML of list, post, tag and feed pages | Content in server HTML; JS only for anchors | Post list, bodies, tag lists and feed entries all present in fetched HTML; 1 script per page (`/dist/*.js`, anchors) | ✅ pass |
| NFR-3 | Measured 9 pages | Title <= 60, description <= 160, one h1, no skipped levels | Longest title 48, longest description 64; exactly 1 h1 each; sequences e.g. H2(nav) H1 H2 H3 H3 H2 - no skipped level after the h1; hidden nav `<h2>` precedes the h1 on every page (spec-noted). Uniqueness: see AC-5.4 | ✅ pass |
| NFR-4a | Real clicks at 375px: `/` -> third post -> "second tag" -> "all tags" -> header Feed | <= 4 clicks, completable at 375px | Feed reached on click 4 (3 clicks from `/` to the tag page plus 1 to Feed); all steps worked at 375 | ✅ pass |
| NFR-4b | At 1280px: Tab, Enter on skip link, Tab again; read focus style | Skip link first stop, moves to `#main`, visible focus | First Tab stop = "Skip to main content"; Enter -> URL `#main`; next Tab landed on first link inside main. `document.activeElement` stayed `BODY` (main has no tabindex), so focus moves by sequential start point only. Focused link: `:focus-visible` true, outline auto 1px | ✅ pass |
| NFR-4c | Looked for a 0-post tag/archive | Heading, not blank | No such page exists in this content | ⚠ not-verified-live |
| NFR-5a | `grep -rF youremailaddress@example.com _site`; email regex over 8 fetched pages; `http:` link search | No secrets, no email, https links | No hits in `_site` or fetched pages; no `http://` links/images | ✅ pass |
| NFR-5b | `npm audit` in the target (read-only) | No high/critical | 2 high: `zod <4.6.6` (GHSA-mrhx-c7xc-m3w5), `markdown-it` (GHSA-gfr2-rv44-r23c) - matches review F3, re-derived because it is a stated NFR bar | ❌ fail (B4) |
| NFR-5c | Read response headers, `document.cookie`, console | Repo-controlled facts only (A6) | No CSP/HSTS/`X-Content-Type-Options` on this Python harness (host-owned, so not evidence about the deploy); no `Set-Cookie`, `document.cookie` empty; console free of app errors. JS bundle contents not inspected | ⚠ not-verified-live |
| NFR-6 | Read snapshot landmarks, alt, skip link | Skip link, landmarks, `aria-current`, alt | `banner`, `navigation`, `main`, `contentinfo`; skip link; `aria-current`; possum image alt non-empty | ✅ pass |
| NFR-7 | `npm run build` / `build-ghpages` | Exit 0; prefix links resolve | Target read-only; no build run by me. `build-ghpages` out of reach | ⚠ not-verified-live |
| NFR-8 | - | - | N/A per spec | N/A |

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B1 | Minor | Open `/blog/thirdpost/`; check the 2 `<pre>` blocks (or Tab through) | Every code block reachable by keyboard. Observed: the unhighlighted `<pre>` has `tabindex` -1 and scrolls horizontally at 375px (403 > 343), so a keyboard user cannot scroll it (AC-2.6; `eleventy.config.js:57` only covers highlighted blocks) | open |
| B2 | Minor | At 375px on `/`, measure header links | Touch targets ~44px (ux lens §4). Observed: Home 41x20, Archive 50x20, About 40x20, Feed 34x20, site title 343x21 | open |
| B3 | Minor | Load any page; request `/favicon.ico` | No console errors on a normal load. Observed: `/favicon.ico` 404 and no `<link rel=icon>` in the page. The first load of `/` logged one truncated 404 console error, which I could not tie to a URL (a second load logged nothing) | open |
| B4 | Major | `cd` to the target; `npm audit` | No high advisories (NFR-5). Observed: 2 high (`zod`, `markdown-it`). Same as review F3 | open |
| B5 | Minor | Open `/sitemap.xml` | `lastmod` meaningful. Observed: non-post pages carry the build date 2026-10-27 (review F8) and tag pages are missing (F7) | open |

`[GAP]` ACs (1.5, 4.4, 5.4-5.7) are recorded in §2 as confirmed gaps; per spec C1 they are not filed again as QA defects.

## 4. Console & Network

- Console errors seen: 1 truncated 404 on the first load of `/` (B3); `/nope/` and fetch probes of 404 routes (`/blog/fifthpost/`, `/robots.txt`, `/favicon.ico`) logged expected 404s. No JavaScript errors. Post page `/blog/fourthpost/` and a later load of `/`: no console messages.
- Network on `/blog/fourthpost/`: document 200, `/dist/cC8wS6ZjFU.js` 304, `fourthpost/xbVnp_hAou-350.avif` 304. No failed requests on the flow pages.
- Response headers (Python harness): `content-type`, `last-modified`, `server` only; no security headers; not evidence about the deploy host.

## 5. Verdict

Would I demo this to a stakeholder right now? No, not as a release candidate. Measured against the retrospective spec: 6 `[GAP]` ACs are confirmed as gaps; AC-2.6 fails; NFR-5 fails (`npm audit`, 2 high); 8 rows are `⚠ not-verified-live` (AC-1.6, AC-1.7, AC-2.5, AC-3.5, NFR-1, NFR-4c, NFR-5c, NFR-7). Everything else listed `✅ pass` was performed in the browser or on raw server HTML fetched from it. The reader journey Home -> post -> tag -> Feed works at 1280px and 375px with CLS 0. The review's predictions held: draft excluded on the production build, feed image URLs are real, message box also on `/about/` and `/blog/`. Standard `anti-generosity` applied. Lighthouse was not run, so NFR-1's score is unmeasured.

---

## QA GATE

- [ ] Every Must-story acceptance criterion verified in the real browser and passed (AC-2.6 fails; AC-1.5 `[GAP]`; AC-1.6, AC-1.7, AC-2.5, AC-3.5 not-verified-live)
- [ ] Every browser-observable NFR verified and passed (NFR-1, NFR-4c, NFR-5b/c, NFR-7 open)
- [ ] No open Blocker or Major bugs (B4 open)
- [ ] Browser console free of errors on the tested flows (B3: one 404 on first load)
- [x] Tested on all agreed viewports (1280x800 and 375px)
- [x] Line budget respected: Ist ~115 lines / Soll ~130 (excluding HTML comments); the AC table rows are long; self-reported, no linter
- [ ] Status set to `passed` (status is `failed`)

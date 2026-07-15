---
name: seo
applies-to: [website]
phases: [specify, design, review, qa]
---

# SEO Lens

Active when the project profile includes **`website`** — content meant to be
found by search engines, not a login-walled app. A page nobody can find is a
feature nobody uses; SEO is the discoverability half of "does the product
actually work". This lens does **not** turn aSPARK into a marketing tool (no
keyword strategy, no link building) — it keeps the *technical* foundations of
findability from silently rotting as the site is built.

Like every lens, this flags concerns; it never invents scope. A missing SEO
concern becomes a proposed **NFR** for the PO or a **finding** for the phase
that owns it — the same bar as any other finding: location, the rule it
violates, a concrete fix.

## Who owns what

Each area is verified by exactly one phase, so a concern raised in Specify is
actually checked downstream — never just asserted.

| Area | Owner phase | Agent |
|---|---|---|
| SEO makes it into the spec as measurable NFRs | Specify | Product Owner |
| Content structure & semantics (headings, landmarks, link text) | Specify (design-check) | Designer |
| Rendering, indexability, metadata, structured data in the diff | Review | Reviewer |
| What's actually rendered & measured in a real browser | QA | QA Tester |

## The checklist

### 1. Discoverability & crawlability *(Review)*
- [ ] `robots.txt` exists and doesn't accidentally `Disallow: /` the site (or block indexable routes).
- [ ] A `sitemap.xml` (or framework equivalent) lists the public routes and is referenced from `robots.txt`.
- [ ] No indexable page ships `<meta name="robots" content="noindex">` unintentionally; staging/no-index rules don't leak to production.
- [ ] Internal links use real, crawlable `<a href>` — not click handlers on `<div>`s — and link text is descriptive, not "click here".

### 2. Rendering & indexability *(Review, verified in QA)*
- [ ] Content that must be indexed is present in the **server-rendered HTML** (SSR/SSG/prerender), not injected only after client-side JS — a crawler that doesn't run JS must still see it.
- [ ] Each indexable route has a **unique, stable URL**; no important content lives only behind hash routes or query-only states.
- [ ] Canonical URLs are set (`<link rel="canonical">`) so duplicate/parametrized URLs don't split ranking.
- [ ] Pagination, filters and infinite scroll expose crawlable URLs for their content, or are consciously marked out of scope.

### 3. Per-page metadata *(Review, verified in QA)*
- [ ] Every indexable page has a **unique** `<title>` (~50–60 chars) and `<meta name="description">` (~150–160 chars) — not one global default repeated everywhere.
- [ ] Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) and Twitter Card tags are present so shared links render a preview.
- [ ] `<html lang>` is set; `hreflang` is present if the site is multilingual.
- [ ] One `<h1>` per page that names the page's subject; heading levels don't skip.

### 4. Media & assets *(Design for intent, Review for implementation)*
- [ ] Content images have descriptive `alt` text (this doubles as the accessibility check — cite it once, not twice).
- [ ] Images are sized/compressed and lazy-loaded below the fold; no layout shift from unsized media.

### 5. Structured data *(Review)*
- [ ] Where the content type warrants it (articles, products, events, breadcrumbs, org), JSON-LD structured data is present and valid for the schema used.
- [ ] Structured data matches the visible content — no marking up data the user can't see.

### 6. Performance / Core Web Vitals *(QA, browser-observed)*
- [ ] **LCP** (largest contentful paint) is within a stated budget on a mid-range device — a slow site is demoted and abandoned.
- [ ] **CLS** (cumulative layout shift) is negligible: reserved space for images/ads/embeds, no content jumping.
- [ ] **INP / interaction latency** stays responsive; the main thread isn't blocked by heavy JS on load.
- [ ] These have a measurable NFR (e.g. "LCP < 2.5s on a mid-range laptop, throttled Fast 3G") so QA can verify, not vibe-check.

## Phase notes

- **Specify (PO):** if the profile has `website`, ensure at least one **NFR**
  captures the discoverability and Core-Web-Vitals bars as measurable statements
  (`NFR-n`), so Review and QA have something traceable to verify. Don't restate
  the whole checklist as stories — the lens is the standard; the NFRs are the
  falsifiable slice this feature must meet.
- **Design (Designer):** judge content *structure and semantics* — heading
  hierarchy, landmark regions, descriptive link text, `alt` intent. This overlaps
  your accessibility checks by design; cite each finding once.
- **Review (Reviewer):** the technical bulk. Trace the metadata, rendering
  strategy, canonical/sitemap/robots and structured data in the **diff**. A
  client-only render of content that the spec says must be indexable is a finding,
  not a preference.
- **QA (QA Tester):** in the real browser, confirm rendered `<title>`/meta per
  route (view source *and* rendered DOM), that indexable content appears with JS
  disabled or in the server response, and measure the Core Web Vitals NFRs
  (Lighthouse/DevTools). Report what you measured, under the same `NFR-n` IDs.

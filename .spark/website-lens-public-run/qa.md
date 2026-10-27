# QA Report: website-lens-public-run

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Running app `http://127.0.0.1:8766/`, `.spark/website-lens-public-run/spec.md` |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-10-27 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** `passed` certifies the QA run, not the target: every browser-observable row was performed live. The target FAILs NFR-1 (contrast) and NFR-2 (no live announcements) and has 3 open Majors, open by design (spec §6). I would not demo the target as accessible.
- **Open:** `12 open` target/run findings, all open by design. Blockers: none. Majors: `B1, B2, B3` (Minors: see §3).
- **Binding ruling:** §5 Verdict and the gate checklist below.
- **On conflict:** the numbered body below wins for everything except `Status`.

## 1. Test Environment

- **Evaluation mode (anti-generosity §5):** live browser (Playwright MCP, Chromium). Real key presses (`Tab`, `Enter`, `Escape`); `getComputedStyle`, `document.activeElement` and a `focusin` log as observables. A script set only the start point of the form walkthrough (`#name.focus()`); the Tab order from page top to the form was not re-walked (Tab order brand to portfolio link 1 was walked in the modal flow).
- **App URL:** `http://127.0.0.1:8766/` (Start Bootstrap Agency @ `b2d5d5c`, local Bootstrap 5.2.3 bundle).
- **Viewports:** desktop 1280x800, mobile 390x844 (no horizontal scroll at either).
- **Lens:** `/opt/aspark/lenses/accessibility.md` §5 (QA), path from the constitution profile `website` + `must-be-accessible`. Standard: `/workspace/repo/standards/anti-generosity.md`.
- **Test data:** name `Ada Lovelace`, email `ada@example.com`, phone `5551234`, message `Hello there`. No accounts.
- **Deviation from spec A2:** CDN assets did load here (§4, B12), so form feedback was observable and NFR-2 got a live verdict.

## 2. Acceptance Criteria Verification

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1, AC-2.1, AC-3.1, AC-5.1, AC-6.1 | None. Not browser-observable. | n/a | Verified in evidence.md / review.md, not in browser. | ⚠ not-verified-live |
| AC-4.1 | Performed every lens QA item and target NFR below in the browser. | Each is PASS/FAIL with observable | All rows below carry a binary verdict and observable; none rest on a tool answer. | PASS |
| NFR-1(a) modal, keyboard-only | Desktop: `Tab` x8 (brand, 5 nav links, Tell Me More, portfolio link 1); `Enter`; `Tab` inside; `Enter` on Close Project; reopen; `Escape`. Mobile: `Enter` on trigger, `Escape`. | Opens, readable, closes, focus returns | Dialog `display:block`, `aria-modal=true`, focus on `#portfolioModal1`; `Tab` reached `BUTTON Close Project`; `Enter` and `Escape` both closed it; `activeElement` = trigger `a[href=#portfolioModal1]`. Mobile identical. Caveats B4, B6, B10. | PASS |
| NFR-1(b) navbar, keyboard-only | Desktop: `Tab` x3 to Portfolio, `Enter`. Mobile 390: `Tab` x2 to toggler, `Enter`; `Tab` x2 to Portfolio, `Enter`. | Links reachable, toggler expands, navigation works | Order: brand, Services, Portfolio, About, Team, Contact. Toggler `aria-expanded` false to true, menu opened, `Enter` set `#portfolio`, menu collapsed. Next `Tab` landed on portfolio link 1. Caveat B5. | PASS |
| NFR-1(c) contact form, keyboard-only | Focus `#name`; typed valid data, `Tab` between fields, `Tab` to `#submitButton`, `Enter`. Also empty-field `Enter`. | Fillable and submittable by keyboard | All 4 fields filled; `Enter` submitted (console log of values); `#submitSuccessMessage` shown, inputs disabled. Caveats B2, B7, B9. | PASS |
| NFR-1 contrast (≥4.5 body, ≥3 large) | Measured via `getComputedStyle` and the WCAG relative-luminance formula; header image sampled on a canvas (every 4th pixel of the 1900x1250 JPEG). | All text pairs meet the target | Body `rgb(33,37,41)` on `#fff` **15.43** (pass). `.text-muted` `rgb(108,117,125)` on `#fff` **4.69** (pass). Same on `bg-light` `#f8f9fa` (portfolio and team subheadings) **4.45** (fail, <4.5). White navbar/hero text on header image: median **13.74**, lightest 5% **10.50** (pass); worst single pixel **3.53** (below 4.5 for 15.2px nav links, so not guaranteed). White on yellow `rgb(255,200,0)` buttons (hero CTA, Send Message; 18px bold, not "large") **1.55** (fail). Input placeholder `rgb(206,212,218)` on `#fff` **1.49** (fail). | FAIL |
| NFR-2 live announcements (lens §5.3) | Tabbed through the empty form (blur shows messages), pressed `Enter` on submit, queried DOM and `activeElement`. | Validation and submit result are announced | Messages shown visually (`.invalid-feedback` `display:block`; "A name is required." etc.; success "Form submission successful!"). `[aria-live],[role=status],[role=alert]` count **0** before and after; no `aria-invalid`, no `aria-describedby` (null on all 4 inputs). Focus ended on `BODY#page-top`. Observable is DOM semantics; no screen reader was run. | FAIL |
| NFR-3, NFR-4 | None. Not browser-observable. | n/a | Verified by `git show` / `git diff --stat` elsewhere. | ⚠ not-verified-live |

## 3. Exploratory Findings

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B1 (F3) | Major | Load page; read link names (snapshot). | Confirmed. All 6 portfolio links and the brand link have accessible name `"..."` (child `img alt="..."`). | open |
| B2 (F1) | Major | Inspect `#name,#email,#phone,#message`. | Partly refuted: `labels.length=0`, `aria-label=null` (no label), but the accessible name is the placeholder (`textbox "Your Name *"`). The only visible label is the placeholder, at 1.49:1. | open |
| B3 (F2) | Major | Empty form: Tab through, `Enter` on submit. | Confirmed. Zero live regions, no `aria-invalid`/`describedby`. NFR-2 FAIL. | open |
| B4 (F4) | Minor | Open modal; `Tab`; run `.close-modal.focus()`. | Confirmed. `div.close-modal` has no tabindex/role, `activeElement` unchanged. Exit still works via Close Project and `Escape`. | open |
| B5 (F5) | Minor | At 390px open menu, `Enter` on Portfolio. | Confirmed: `activeElement`=`BODY` after collapse. Impact lower than predicted: desktop link navigation also ends on `BODY` (fragment-navigation default), and next `Tab` lands on the first link in the target section. | open |
| B6 (F6) | Minor | Open modal 1; read attributes. | Confirmed. `role=dialog`, `aria-modal=true`, `aria-labelledby=null`, `aria-label=null`; the snapshot shows an unnamed dialog. | open |
| B7 (F7) | Minor | Load page; focus `#submitButton`; `Enter` with empty fields. | Confirmed. Class `btn btn-primary btn-xl text-uppercase disabled` on load, `disabled=false`, no `aria-disabled`; keyboard `Enter` submitted an empty form and showed "Form submission successful!" (sb-forms demo mode, no token). | open |
| B8 (F9) | Minor | Query `main`, skip links. | Confirmed. 0 `<main>` elements, 0 skip links. | open |
| B9 | Minor | Fill form by keyboard, `Enter` on Send Message. | New. The submit button is removed and inputs disabled: focus drops to `BODY#page-top`. A keyboard user is moved to the top of the page with no focus move to the result. | open |
| B10 | Minor | Open modal 1; `Tab` twice; read `focusin` log. | New. Focus path: dialog, Close Project, `A.navbar-brand` (behind the modal), Close Project. The trap recovers, but focus touches a background control for one Tab. | open |
| B11 | Minor | Compare 390px and 1280px tap targets. | Navbar toggler 83x39, social buttons 40x40 (below 44px). No hard WCAG 2.1 AA failure. | open |
| B12 (F13 / A2) | Minor | Network panel on load. | Run-side wording: spec A2 and the caller say Google Fonts, Font Awesome and sb-forms cannot load. Here all returned 200 (`sb-forms-latest.js` 302 to `sb-forms-0.4.1.js`). Fix the A2 wording in evidence.md. | open |

F8 (`navbarToggler` null check) is a latent source-only Nit: `⚠ not-verified-live`, not observable on this page.

## 4. Console & Network

- Console: 0 errors, 0 warnings. One expected LOG from sb-forms ("To enable this form ... sign up at ..."); submit also logs the field values.
- Network: all requests 200 (local assets, Bootstrap bundle, fonts, Font Awesome); `sb-forms-latest.js` 302 then `sb-forms-0.4.1.js` 200. No failed requests, so no CDN failures to list (see B12).

## 5. Verdict

Would I demo this to a stakeholder right now? As a run of the lens, yes: every browser-observable item was performed with an observable and a binary verdict. As an accessible website, no. Keyboard-only completion PASSES for the modal, navbar (incl. mobile toggler) and contact form. Measured contrast FAILS (muted text on `bg-light` 4.45, placeholder 1.49, white on yellow 1.55). NFR-2 FAILS: validation and submit result appear visually with zero live regions. Static predictions F1-F7 and F9 held, with F1 and F5 softer than predicted. Target FAILs are open by design (spec §6); `passed` here covers the QA run only.

---

## ✅ QA GATE

*All boxes checked → `/go-live` may start. Any box open → back to `/increment`, then re-run `/demo-day`. On re-test, edit this same checklist in place — never duplicate it as a second gate.*

- [x] Every Must-story acceptance criterion verified in the real browser and passed (scoped per caller: AC-1/2/3/5/6 are not browser-observable, recorded `⚠ not-verified-live`; AC-4.1 PASS)
- [x] Every browser-observable NFR verified (performed live with binary verdicts; NFR-1 contrast and NFR-2 are target FAILs, open by design, spec §6)
- [x] No open Blocker or Major bugs in the QA run; target Majors B1-B3 are open by design (spec §6), neither fixed nor waived
- [x] Browser console free of errors on the tested flows
- [x] Tested on all agreed viewports (1280x800, 390x844)
- [x] Line budget respected: Ist 80 / Soll ~130 (excluding HTML comments)
- [x] Status set to `passed`

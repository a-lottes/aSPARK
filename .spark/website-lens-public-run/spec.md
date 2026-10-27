# Spec: website-lens-public-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`), drafted by the line orchestrator in dark mode |
| **Status** | `approved` |
| **Date** | 2026-10-27 |
| **Ticket** | #96 |

**Handoff**
- **Status:** `approved` (dark-mode factory line took the recommended gate; the issue's AC-1…AC-6 are the approved scope).
- **Summary:** Run the `accessibility` lens, activated from a declared constitution profile, through `/peer-review` and a live-browser `/demo-day` on a real public open-source `website`, and commit the trail.
- **Open:** `none`
- **Binding ruling:** §4 User Stories.
- **On conflict:** the numbered body wins except `Status`.

## 1. Problem & Goal

- **Problem:** ROADMAP "The one gap that matters most": the lens success definition needs a UI lens firing and QA-verified on a real `website`. The `api` half got a partial run (`.spark/api-lens-public-run/`); the `website` half is open.
- **Goal:** One public, re-runnable, browser-verified `accessibility`-lens run on a pinned open-source website, activated from a constitution, with every lens check recorded PASS / FAIL / `not-verified-live`.
- **Success signal:** A stranger can clone the target at the pinned commit, serve it as described, and repeat the same checks.

## 2. Target Users

Adopters deciding whether to trust the UI lens; the aSPARK author reading the roadmap.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The target has no `.spark/` trail. Its profile (`website` + `must-be-accessible`) is declared by the line in `target-constitution.md`, a scratch copy of which sits in the clone so the skills read it from there. | Accepted. Disclosed: the target's maintainers declared nothing. |
| A2 | The container browser reaches localhost only. The page's CDN scripts and fonts cannot load. Bootstrap's bundle is replaced by the same npm version (`bootstrap@5.2.3`, served locally); Google Fonts, Font Awesome and `https://cdn.startbootstrap.com/sb-forms-latest.js` (the contact form's submit/feedback script, `dist/index.html:608`) stay missing, so fonts, icons and the form's submit and validation feedback cannot be observed. | Accepted; evidence lists the deviation. Anything depending on them is `not-verified-live`. |
| A3 | Lens firing is instruction-driven. One run gives one observation. | Accepted; AC-3 states n=1 and no rate. |
| A4 | The target is not changed. Review reviews the existing files as a whole-file diff against the empty tree (no real increment exists). | Accepted; disclosed. |

## 4. User Stories

### US-1 (Must): Name the target so it can be re-run

> As a stranger, I want the exact repo, commit, serve command and URL so I can reproduce the run.

- [ ] AC-1.1: Given `evidence.md`, when read, then it names repo URL, pinned commit, license, serve instructions, every deviation from upstream, and run date.

### US-2 (Must): Lens activated from a constitution

> As a maintainer, I want the lens to come from a declared profile so the activation chain is exercised.

- [ ] AC-2.1: Given `target-constitution.md`, when the skills' dispatch step runs, then `accessibility` is selected because the profile declares `must-be-accessible`, and its path is passed to the reviewer and the QA tester by the dispatch rule (frontmatter `phases`), not typed by hand as a lens choice.

### US-3 (Must): Review without a per-item trace

> As a reader, I want to know whether the lens fired unprompted.

- [ ] AC-3.1: Given the reviewer's prompt, then it contains no per-item trace request; `evidence.md` records which lens items surfaced in `review.md` anyway, as n=1 with no rate claim.

### US-4 (Must): Live QA with binary verdicts

> As a reader, I want each lens-derived check run in a real browser.

- [ ] AC-4.1: Given `qa.md`, then every lens QA item (keyboard-only pass, measured contrast, live-region confirmation) and the target NFRs below are PASS/FAIL with the observable, or `⚠ not-verified-live` with a reason, per `standards/anti-generosity.md`.

### US-5 (Must): Docs claim only what was shown

- [ ] AC-5.1: `evidence.md` lists what is not shown (single run, single model, prompt-enforced only). `ROADMAP.md`, `docs/status.md` and `README.md` match it; nothing is marked Shipped beyond what ran.
- [ ] AC-6.1: No executable code is committed; no lens, skill or agent text is changed.

## 5. Non-Functional Requirements (target-side, the lens's Specify grounding)

| # | Requirement | How it's verified |
|---|---|---|
| NFR-1 | Accessibility of the target's flows: (a) open a portfolio modal, read it, close it; (b) use the navbar (incl. the mobile toggler at ≤ 991 px); (c) fill and submit the contact form — all keyboard-only. Text contrast ≥ 4.5:1 body, ≥ 3:1 large text. | QA, keyboard-only walkthrough and measured contrast in the browser |
| NFR-2 | Async/state changes a sighted user sees (contact-form validation, submit result) are exposed to assistive tech. | QA, live check in the browser |
| NFR-3 | Reproducibility: every cited `file:line` resolves at the pinned commit. | Re-resolution with `git show` |
| NFR-4 | Scope fence: `.spark/website-lens-public-run/`, `README.md`, `ROADMAP.md`, `docs/status.md` only. | `git diff --stat` |

## 6. Out of Scope

Fixing the target; the `seo` / `ux` lenses; changing any lens; a rate of lens firing.

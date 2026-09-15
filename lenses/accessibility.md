---
name: accessibility
triggers: [must-be-accessible]
phases: [specify, design, act, review, qa]
---

# Accessibility Lens

Active when the project declares the characteristic `must-be-accessible` — an
existing accessibility statement/VPAT/WCAG target, a public-facing product
under a legal accessibility mandate (EAA, ADA Title II/III, Section 508, EN 301
549), or a direct confirmation at `/charter`. Accessibility isn't a shape of
software, it's a property of who must be able to use it — a `library` that
ships a generated docs site, an `api` with an admin console, or a `cli` with a
companion web dashboard can carry the same obligation a `website` does, and a
`web-app` behind a VPN with no public users may not. That is why this lens is
triggered by a characteristic, not a type.

The Designer's baseline Critique Lens already checks contrast, keyboard
reachability, labels/alt text and touch targets on every UI, lens or no lens
(`agents/designer.md` §3) — but only once, as freeform Design Review prose,
before any code exists. This lens does not repeat that baseline; it grounds it
into a traceable `NFR-n` and adds the depth nothing today provides: whether the
*implemented* code is actually accessible (Act, Review) and whether the
*running* UI is accessible under real assistive-tech conditions (QA). It also
overlaps `ux`'s feedback/motion check and `seo`'s media/alt-text check — each
cited once, never duplicated (see `lenses/ux.md`, `lenses/seo.md`).

Like every lens, it flags concerns and proposes NFRs; it never invents scope.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| Accessibility expectations as a measurable, flow-specific NFR | Specify | Product Owner |
| Contrast, focus order, target size, reduced-motion (grounding the baseline) | Design | Designer |
| Semantic markup, labels, ARIA only where semantics fall short | Act | Developer |
| Keyboard traps and focus management on route/modal changes, in the diff | Review | Reviewer |
| Keyboard-only walkthrough, measured contrast, live-region behavior | QA | QA Tester |

## The checklist

### 1. Grounding the NFR *(Specify — Product Owner)*
- [ ] The accessibility NFR names the actual flow(s) to keyboard- and
  screen-reader-test and a numeric contrast target (4.5:1 body text, 3:1 large
  text) — not the spec template's generic "WCAG 2.1 AA" example restated
  verbatim.
- [ ] If the feature adds no new UI, the NFR records a one-line conscious N/A
  rather than being silently omitted — the lens flags, it never invents scope.

### 2. Grounding the design baseline *(Design — Designer)*
- [ ] Contrast, focus order/keyboard reachability, and touch target size are
  cited to `agents/designer.md` §3's baseline once — not restated as new
  findings — and grounded into the spec's accessibility `NFR-n` so they become
  traceable through Review and QA instead of staying one-time Design Review
  prose.
- [ ] `prefers-reduced-motion` support is checked: cited to `lenses/ux.md`'s
  motion check once when `ux` is also active, owned outright here when it
  isn't (e.g. a `library` project with a docs site that declares no
  `web-app`/`website` type).

### 3. Implementing accessible markup *(Act — Developer)*
- [ ] Interactive elements and structure use semantic HTML (`button`, `nav`,
  `main`, headings in order) and every form control has a programmatic label —
  not a raw `<div>` with a click handler standing in for a native element.
- [ ] ARIA is added only where semantics fall short (a custom widget with no
  native equivalent), never as a substitute for the native element that would
  have worked.
- [ ] Async state changes (loading, error, success) that a sighted user sees
  are also announced to assistive tech — e.g. an `aria-live` region — so the
  same state `ux`'s feedback check already requires is not silently
  sighted-only.
- [ ] Realized through the spec's accessibility `NFR-n` and the plan's
  `Covers (AC / NFR)` column, the same generic mechanism every other NFR
  category already uses — no lens-specific step exists in `/increment` itself.

### 4. Keyboard traps & focus in the diff *(Review — Reviewer)*
- [ ] No keyboard trap is introduced by a custom widget (modal, dropdown,
  date picker) — focus can always move in and back out via keyboard alone.
- [ ] Focus moves logically on route changes and modal open/close (to the new
  content or back to the trigger, not lost to `<body>`).
- [ ] Semantic markup and ARIA correctness (Act, above) are **not** re-checked
  here — this section is scoped to keyboard traps and focus management only,
  a deliberately narrower Review remit. A wrong ARIA pattern that Act got
  wrong ships unless QA's keyboard walkthrough surfaces it.

### 5. Live, keyboard and measured verification *(QA — QA Tester)*
- [ ] Every acceptance criterion of the feature is completed keyboard-only (no
  mouse), reported pass/fail per AC.
- [ ] A **measured** (not eyeballed) contrast ratio is reported for at least
  one text/background pair flagged as borderline, under the matching `NFR-n`.
- [ ] Whether Act's live-region announcements (§3) actually fire is confirmed
  live — cited once against `ux`'s existing state-coverage check, never a
  duplicate NFR for the same state.

## Phase notes

- **Specify (PO):** turn the flow(s) that need keyboard/screen-reader testing
  and the contrast target into a measurable `NFR-n` — or record the conscious
  N/A. This is the only carrier the Act check (§3) has: if the NFR lands as
  N/A, the Act row has nothing to attach to for that feature.
- **Design (Designer):** cite the existing baseline once, don't re-derive it;
  the value added here is turning it into something Review and QA can trace,
  not new findings.
- **Act (Developer):** semantic-first, ARIA as the fallback, live regions for
  state changes a sighted user already gets for free. Verified through the
  plan's own AC/NFR traceability — no separate lens-resolution step exists in
  `/increment`.
- **Review (Reviewer):** keyboard traps and focus management in the diff, and
  nothing beyond — a missing focus return after closing a modal is a real
  finding, filed at the `file:line` that introduced it.
- **QA (QA Tester):** the browser is the only place a keyboard-only pass and a
  measured contrast ratio can actually be performed — report what you did and
  observed, under the matching `NFR-n`, never what the source code implies.

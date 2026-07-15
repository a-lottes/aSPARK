---
name: ux
applies-to: [web-app, website]
phases: [specify, design, qa]
---

# UX Lens

Active when the project profile includes **`web-app`** (and optionally
`website`) — a frontend the user *operates*, not just reads. The Designer
already applies base usability heuristics to every UI; this lens goes **deeper**
where the interaction is the product: the efficiency of a flow, the design of a
form, the behavior under real conditions (mobile, slow network, empty and error
states). It exists so app-like frontends get scrutiny proportional to how much
the user lives inside them.

This lens does **not** re-run the Designer's base heuristics — those always
apply. It adds the interaction depth that only matters when the UI is app-like.
Like every lens, it flags concerns and proposes NFRs; it never invents features.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| UX quality bars make it into the spec as NFRs / ACs | Specify | Product Owner |
| Flow, forms, states, responsive design in the spec/mockup | Specify (design-check) | Designer |
| The same, exercised in a real browser | QA | QA Tester |

*(No Review row: UX is judged from the running product and the spec, not from
reading the diff. The Reviewer's remit stays code correctness.)*

## The checklist

### 1. Flow efficiency *(Design, verified in QA)*
- [ ] The core task is reachable in as few steps/clicks as its value warrants — no incidental detours, no dead-end screens.
- [ ] The primary action on every screen is obvious and singular; secondary actions don't compete with it visually.
- [ ] The user can always see where they are and how to get back — no navigation that strands them.
- [ ] Progressive disclosure: complexity is revealed when needed, not dumped on first load.

### 2. State coverage *(Design, verified in QA)*
- [ ] **Empty state** is designed (first use, no data yet) — it orients and offers the next action, not a blank void.
- [ ] **Loading state** gives feedback within ~100ms of an action; long waits show progress, not a frozen UI.
- [ ] **Error state** says what happened and what to do next, in the user's words — recoverable, not a dead end.
- [ ] **Success/confirmation** is visible for consequential actions; the user is never left guessing whether it worked.
- [ ] **Partial/large-data** states hold up: long lists, long strings, many items don't break layout or scroll.

### 3. Forms & input *(Design, verified in QA)*
- [ ] Inputs are labelled, grouped logically, and ordered the way the user thinks — not the way the data model is shaped.
- [ ] Validation is inline and timely (on blur / on submit, not keystroke-nagging), and says how to fix, not just "invalid".
- [ ] Destructive or irreversible actions are guarded (confirm, or undo); the user can cancel and back out without losing work.
- [ ] Sensible defaults, autofocus on the first field, correct input types/keyboards on mobile.

### 4. Responsive & touch *(Design, verified in QA on mobile width)*
- [ ] The layout works from mobile width up — no horizontal scroll, no content clipped or overlapping.
- [ ] Touch targets are ~44px+ and not crowded; hover-only affordances have a touch/focus equivalent.
- [ ] The core flow is completable on a phone, not just technically rendered on one.

### 5. Feedback & motion *(Design, verified in QA)*
- [ ] Interactive elements have visible hover, focus and active states (this doubles as the keyboard-accessibility check — cite once).
- [ ] Motion is functional (orients, connects cause and effect), brief, and respects `prefers-reduced-motion`.
- [ ] Nothing moves, autoplays or steals focus without the user initiating it.

## Phase notes

- **Specify (PO):** capture the load-bearing UX bars as measurable **NFRs** or
  concrete **ACs** — e.g. "the create flow completes in ≤ 3 steps", "every async
  action shows feedback within 100ms", "core flow completable at 375px width".
  This gives QA something falsifiable to verify rather than a taste debate.
- **Design (Designer):** walk this checklist on top of your base Critique Lens.
  These are `Major`/`Minor` findings with location, rule and fix — the same
  format as everything else. Accessibility items in here are never Minor by
  default.
- **QA (QA Tester):** you already explore off the happy path — this lens tells
  you *what* to hammer: every state above, forms with junk input, the flow on
  mobile width, feedback timing. Verify against the UX NFRs by their `NFR-n` IDs
  and report what you observed.

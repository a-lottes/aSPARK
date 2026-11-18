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
states, and the amount of data the user will actually have after a year of use). It exists so app-like frontends get scrutiny proportional to how much
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
- [ ] **Partial/large-data** states hold up: long lists, long strings, many items don't break layout or scroll. (Whether the user can still *find* things at that size is §7.)

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
- [ ] Interactive elements have visible hover, focus and active states (this doubles as `lenses/accessibility.md`'s check — cite once).
- [ ] Motion is functional (orients, connects cause and effect), brief, and respects `prefers-reduced-motion`.
- [ ] Nothing moves, autoplays or steals focus without the user initiating it.

### 6. Start-up robustness *(verified in QA)*
- [ ] The app starts and works when browser storage throws on access (`localStorage`/`sessionStorage` raising `SecurityError`, e.g. blocked site data): the access itself, not only the read, sits inside error handling, and the app falls back to defaults.
- [ ] A reload in the middle of use leaves the app usable, with no stuck or half-restored state.
- [ ] A window resize while the app runs keeps it working and laid out (no frozen canvas, no stale size).
- A failed start (blank page, uncaught error, nothing interactive) under any of these is a `Blocker`.

### 7. Volume & findability *(Specify, Design, verified in QA)*

§2 asks whether a long list *breaks*. This section asks whether it is still
*usable*: a page that renders 50 customers with 10 entries each without a
layout fault can still be one nobody can work with. The checks are measured
against the **expected usage volume** in the constitution's §2 (today, after
one year, upper bound). Where that entry is missing, the Specify row below
asks for it; no check here is judged against fixture size.

- [ ] **Volume is stated.** The spec names, for every list, table, grouped page and choice control the feature adds or changes, the number of items it holds at the constitution's *after one year* volume (e.g. "customers: 50; people in the participant picker: 250"). A missing number is a Clarify question, not a silent omission.
- [ ] **Reachable in ≤ 3 actions.** At the after-one-year volume, the user reaches a given item in at most three actions (type in a search, pick a filter, open a group, follow a jump link). Scrolling past more than about two screen heights to find it counts as failing. A miss is `Major`.
- [ ] **Bounded lists.** No list grows without limit on one page: it has pagination, "show more", a time window (e.g. the last 30 days, older ones in an archive view) or grouping with collapsed groups. A list whose after-one-year size fits on about two screen heights may stay unbounded; say so in the spec.
- [ ] **No dead-end cap.** A cap line such as "n more not shown" links to where those items are. Content that exists but cannot be reached in the UI is `Major`.
- [ ] **Choice controls scale.** A select, radio group or checkbox list with more than about 15 options at the after-one-year volume has a search/type-ahead, or is pre-filtered by the context the user already chose (e.g. participants limited to the chosen customer, the rest reachable via search). A checkbox list of everything is `Major`.
- [ ] **Many groups are navigable.** A page grouped by entity (per customer, per project) with more than about 7 groups at the after-one-year volume has a jump list, collapsible groups or a filter, and orders groups by what matters now (recency, urgency), not only alphabetically.
- [ ] **Four sizes are designed:** empty, one item, typical, and after-one-year volume, not only empty.

**Cutting it is a decision, not a default.** Search, filter, sort or
pagination for a list that fails a check above may still go to *Out of
Scope*, but only with one of: a named follow-up (issue or backlog item) in
the spec, or the user's explicit waiver recorded in the spec's
Clarifications. The lens still invents no feature; it makes the gap visible
and makes the cut someone's decision. A cut with neither is a `Major` the
Designer raises in the Design Review.

## Phase notes

- **Specify (PO):** capture the load-bearing UX bars as measurable **NFRs** or
  concrete **ACs** — e.g. "the create flow completes in ≤ 3 steps", "every async
  action shows feedback within 100ms", "core flow completable at 375px width".
  This gives QA something falsifiable to verify rather than a taste debate.
  For every list or choice control the feature touches, state the volume and
  the findability bar from §7 as an NFR, e.g. "at 50 customers / 250 people,
  any customer is reachable in ≤ 3 actions; the participant picker shows only
  the chosen customer's people plus a search". If the constitution has no
  expected usage volume, ask for it in the Clarify pass.
- **Design (Designer):** walk this checklist on top of your base Critique Lens.
  These are `Major`/`Minor` findings with location, rule and fix — the same
  format as everything else. Accessibility items in here are never Minor by
  default. Walk §7 against the stated volume, not against the fixtures, and
  raise an un-decided cut of search/filter/pagination as `Major`.
- **QA (QA Tester):** you already explore off the happy path — this lens tells
  you *what* to hammer: every state above, forms with junk input, the flow on
  mobile width, feedback timing, and the start-up robustness item (§6: storage that throws, reload mid-use, resize while running). Verify against the UX NFRs by their `NFR-n` IDs
  and report what you observed.
  **Volume run (§7).** Every screen with a list, grouped page or choice
  control is also walked in the browser with a dataset of the constitution's
  *after one year* volume, at desktop and phone width. Use the project's
  generator if it has one; otherwise build the dataset outside the repo and
  say how. Pick a target item first, then count the actions it takes to reach
  it, and record the count and a screenshot. A list screen checked only
  against fixtures smaller than that volume is `⚠ not verified`, never a pass.

# Constitution: <project-name>

| | |
|---|---|
| **Scope** | Project-wide — binds every SPARK phase and every feature |
| **Owner** | The user (amended via `/charter`) |
| **Status** | `active` |
| **Date** | YYYY-MM-DD |

<!-- The constitution is the project's standing context: the principles and constraints that would
     otherwise be re-explained at the start of every feature. Every agent (Product Owner, Designer,
     Engineering Manager, Reviewer) reads this file before doing phase work. Keep it short and true —
     a constitution nobody follows is worse than none. Amend it with /charter when reality changes. -->

## 1. Product Principles

<!-- What this product optimizes for, in priority order. The tie-breakers the PO uses when scoping. -->

- e.g. Speed of the core flow beats breadth of features.
- e.g. We serve <primary user>; edge users are explicitly out of scope until stated otherwise.

## 2. Technical Constraints

<!-- The stack, the patterns to follow, and the things that are off-limits. The EM plans within these. -->

- **Stack / runtime:** e.g. TypeScript + React + Postgres; no new languages without an amendment.
- **Patterns to follow:** e.g. server components by default; data access only through the repository layer.
- **Off-limits:** e.g. no ORM lock-in, no client-side secrets, no new top-level dependency > 50kB gzip without justification.

## 3. Quality Bars (Definition of Done defaults)

<!-- The baseline every increment inherits, so specs don't restate it each time. Reviewer & QA enforce it. -->

- **Testing:** e.g. every Must story has an automated test; no PR drops coverage on touched files.
- **Accessibility:** e.g. WCAG 2.1 AA is the floor for all UI.
- **Performance:** e.g. no user-facing action slower than 2s on a mid-range laptop.
- **Security:** e.g. all user input validated server-side; no secrets in code or logs.

## 4. Conventions

<!-- The team culture new code must match, so it looks like one author on a good day. -->

- **Naming / structure:** e.g. kebab-case files, feature-first folders.
- **Commits / branches:** e.g. Conventional Commits; one feature branch per `.spark/<feature>`.
- **Language:** all artifacts, code and reports in English regardless of chat language.

## 5. Non-Negotiables

<!-- The short list of things that are never traded away, whatever the deadline. Blockers by definition. -->

- e.g. User data is never logged in plaintext.
- e.g. We never ship a Must story with a failing acceptance criterion.

---

## Amendments

<!-- The change log. The constitution is stable but not frozen; every change is dated and reasoned. -->

| Date | Change | Why |
|---|---|---|
| YYYY-MM-DD | Initial constitution | Project kickoff |

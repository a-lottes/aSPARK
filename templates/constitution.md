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

## 2. Project Profile & Active Lenses

<!-- What kind of software this is, and which situational concern-checklists ("lenses") therefore apply.
     The Facilitator grounds this in the repo (see the detection signals in
     `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`); the user confirms. Lenses activate two ways: from the
     project TYPE (seo←website, ux←web-app, api←api, cli←cli, library←library) and from CHARACTERISTICS —
     see the `Activates` column of `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s "Characteristics"
     detection-signals table for the current mapping. A project can be several
     types and carry several characteristics. Lenses are applied by the existing agents in the phases they own —
     no new roles. Leave a lens off when it doesn't genuinely apply. -->

- **Project type(s):** e.g. `website` + `web-app` (public marketing site plus an authed dashboard).
  <!-- one or more of: website (public, indexable) · web-app (app-like frontend) · api · cli · library -->
- **Characteristics:** e.g. `handles-auth`, `handles-pii`, `has-database`.
  <!-- see `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s "Characteristics" detection-signals table for the current list -->
- **Active lenses:**

| Lens | Why it's active (or off) | Enforced in |
|---|---|---|
| `seo` | e.g. active — the marketing pages must be found by search engines | `/story-time`, `/look-and-feel`, `/peer-review`, `/demo-day` |
| `ux` | e.g. active — the dashboard is app-like; interaction is the product | `/story-time`, `/look-and-feel`, `/demo-day` |
| `security` | e.g. active — handles auth and PII on the public internet | `/story-time`, `/peer-review`, `/demo-day` |
| `data` | e.g. active — Postgres-backed; migrations and retention matter | `/story-time`, `/peer-review` |
| *(others)* | e.g. `api`/`cli`/`library`/`i18n` off — no API, single-locale | — |

- **Active-lens load:** _N_ lenses active.
  <!-- State the count. There is no cap — a project legitimately carries several. But when 4 OR MORE are
       active, flag it: "⚠ elevated load — each phase applies several lenses; keep specs tight and NFRs few
       so agents scrutinize rather than skim." This visibility is the throttle, not a limit. -->
- **⚠ elevated load** (only when 4+ lenses are active): several lenses apply in
  each phase — keep specs tight and NFRs few so the agents don't skim.
  <!-- Delete this line when fewer than 4 lenses are active. -->


## 3. Technical Constraints

<!-- The stack, the patterns to follow, and the things that are off-limits. The EM plans within these. -->

- **Stack / runtime:** e.g. TypeScript + React + Postgres; no new languages without an amendment.
- **Patterns to follow:** e.g. server components by default; data access only through the repository layer.
- **Off-limits:** e.g. no ORM lock-in, no client-side secrets, no new top-level dependency > 50kB gzip without justification.

## 4. Quality Bars (Definition of Done defaults)

<!-- The baseline every increment inherits, so specs don't restate it each time. Reviewer & QA enforce it. -->

- **Testing:** e.g. every Must story has an automated test; no PR drops coverage on touched files.
- **Accessibility:** e.g. WCAG 2.1 AA is the floor for all UI.
- **Performance:** e.g. no user-facing action slower than 2s on a mid-range laptop.
- **Security:** e.g. all user input validated server-side; no secrets in code or logs.

## 5. Conventions

<!-- The team culture new code must match, so it looks like one author on a good day. -->

- **Naming / structure:** e.g. kebab-case files, feature-first folders.
- **Commits / branches:** e.g. Conventional Commits; one feature branch per `.spark/<feature>`.
- **Language:** all artifacts, code and reports in English regardless of chat language.

## 6. Non-Negotiables

<!-- The short list of things that are never traded away, whatever the deadline. Blockers by definition. -->

- e.g. User data is never logged in plaintext.
- e.g. We never ship a Must story with a failing acceptance criterion.

## 7. Delivery & Handoff

<!-- How this project's Keep phase ends. Every field defaults to today's behavior when absent — an
     undeclared project sees no new prompt, no new terminology, anywhere in /go-live. Declare this
     only if release actually depends on someone outside the team approving a PR. -->

- **Release mode:** `direct` \| `pr`. Default when absent: `direct`.
- **Approver:** e.g. `CODEOWNERS`, a named reviewer, or a role — who merges when mode is `pr`. Default when absent: n/a (mode is `direct`).
- **Target branch:** e.g. `main` — the branch a `pr`-mode release targets. Default when absent: n/a (mode is `direct`).
- **Ticket-reference format:** e.g. `PROJ-123`, `#123`, a URL, or `none`. Default when absent: `none`.
- **Terminal status:** the status a `pr`-mode release ends in once handed over — `handed-off`, unless amended. Default when absent: `released` (direct mode's only terminal status).

## 8. QA Method

<!-- How this project's QA phase verifies. Every field defaults to today's behavior when absent — an
     undeclared project sees no new prompt, no new terminology, anywhere in /spark or /demo-day.
     Declare this only if the project genuinely has no browser-observable surface.

     Four things this declaration does NOT do:
     - It changes the *method*, never the coverage. `qa.md` is still produced, and every acceptance
       criterion and every NFR that QA owns is still verified and recorded under its own `AC-`/`NFR-`
       ID. A declared method is performed and written down — never a licence to read the source.
     - It is browser/QA-specific. It is not a generic "declare a ceremony inapplicable" switch:
       **no ceremony gains an off switch at any value.** /story-time, /look-and-feel,
       /sprint-plan, /increment and /peer-review behave exactly as today. Exactly two
       ceremonies have exactly one stated difference each. /go-live still runs every check it
       runs today - the one difference is how it *words* the QA row of the release report's
       pre-flight section, which cites this declaration as a standing project fact instead of
       a per-feature override. /spark still runs every step it runs today - the one difference
       is that it stops asking for a start command, URL and browser tooling, and names the
       declared method instead. Apart from /demo-day, whose method is the point of this
       section, and /charter, its sole writer, no ceremony behaves differently at any value.
     - It is not self-service. Only /charter may create or amend it; a phase that believes the
       declaration is wrong stops and points to /charter rather than editing it.
     - It cannot suppress live-browser QA on a project that has a browser-observable surface. There,
       no value here changes anything. -->

- **Browser-observable surface:** `yes` \| `no` — whether this project has a UI a browser can drive. Default when absent: `yes`.
- **Substitute verification method:** the named method the QA phase performs instead, e.g. `documented dry run against the installed plugin, one performed step per AC`. Read only when the surface is `no`. Default when absent: none — the QA phase asks the user, exactly as today.

## 9. Project Context

<!-- What this project actually is, so the Product Owner and Engineering Manager can cite one
     confirmed picture instead of each re-deriving their own. Written once by /charter's kickoff
     interview (a project with no source files or manifest to picture) or discovery pass (a project
     with code), and confirmed by the user in the same round as §2's profile and §8's QA method —
     never a separate round, never a separate ceremony.

     Default when absent: every phase behaves exactly as it does today — no prompt, no warning, no
     migration. Sole writer: /charter. A phase that finds an entry wrong records the contradiction
     where it works (a spec assumption, a plan risk, a review finding) and points back to /charter;
     it never edits this section itself.

     Size caps, enforced at write time: the whole section ≤ 35 lines, the product brief ≤ 12, the
     system picture ≤ 25. What doesn't fit is pointed at (README, CLAUDE.md, a doc) rather than
     duplicated here. This is not a design doc and not a place for per-feature requirements — those
     stay in spec.md. It is not kept fresh automatically; a stale entry is corrected at the next
     /charter, not silently trusted or silently ignored.

     Every entry is marked with where it came from: `inferred from <file:line>` (read, not asked),
     `asked` (a kickoff question, answered), `confirmed by user` (offered, the user agreed as-is),
     or `not stated` / `not found` (asked and skipped, or looked for and absent) — never a guess
     dressed as a fact. -->

- **Shape:** `greenfield` \| `brownfield` — a label, not a gate; no ceremony branches on it.

**Product brief** (always present — ≤ 12 lines):

- **Primary user:** e.g. `asked` — solo developers picking their first CLI framework.
- **Problem today:** e.g. `asked` — no tool compares three or more options side by side.
- **Smallest version:** e.g. `asked` — a two-framework comparison, hardcoded list.
- **Success signal:** e.g. `asked` — a user picks a framework without opening five tabs.
- **Stack:** e.g. `inferred from package.json:1-12`, or `undecided — the EM proposes at the first /sprint-plan`.
- **Non-negotiables:** e.g. `asked` — never recommends an unmaintained package.

**System picture** (only where the repo has source files or a manifest — ≤ 25 lines; omit this block entirely on a repo with neither):

- **Stack & entry points:** e.g. `inferred from package.json:1-12, src/index.ts:1`.
- **Module structure:** e.g. `inferred from src/:1` — feature-first folders under `src/`.
- **Data model:** e.g. `inferred from prisma/schema.prisma:1-40`, or `not found` — no persistence.
- **Test practice:** e.g. `inferred from package.json:8` — Vitest, run via `npm test`.
- **Conventions:** e.g. `inferred from CONTRIBUTING.md:1-20`, or `not found`.
- **How to run:** e.g. `inferred from README.md:12-18` — `npm run dev`.
- **Known pain points:** e.g. `asked` — the auth module has no tests.

---

## Amendments

<!-- The change log. The constitution is stable but not frozen; every change is dated and reasoned. -->

| Date | Change | Why |
|---|---|---|
| YYYY-MM-DD | Initial constitution | Project kickoff |

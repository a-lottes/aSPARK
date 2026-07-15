# The SPARK Workflow — Deep Dive

This document describes the mechanics behind the loop: how artifacts hand
over between phases, what the gates check, who is allowed to decide what,
and how the feedback loops work. Read the [README](../README.md) first for
the big picture.

## Project-Wide Context: the Constitution

Before any single feature, a project may set a **constitution** at
`.spark/constitution.md` (via `/charter`). It is the one artifact that is *not*
per-feature: it holds the standing principles, technical constraints, quality
bars and non-negotiables that bind every phase of every feature. Every agent
reads it before phase work — so a decision that holds across the whole project
(the stack, the accessibility floor, "user data is never logged in plaintext")
is made once and inherited, instead of re-argued in each `/story-time`.

The constitution is optional but recommended: a project runs without one, but
each feature then carries context the constitution would have supplied for free.
It is stable, not frozen — `/charter` amends it, and every amendment is dated
and reasoned. A spec, plan or diff that conflicts with the constitution doesn't
silently win; the conflict surfaces as an open question or a Blocker.

## Situational Concerns: the Project Profile & Lenses

Not every quality concern applies to every project. SEO matters for a public
website and is meaningless for a CLI; deep interaction UX matters for an app-like
frontend and not for a backend service. aSPARK adapts to this without adding
roles or ceremonies, through two pieces:

- **The project profile.** The constitution's *Project Profile & Active Lenses*
  section records two things, grounded by the Facilitator in the repo's real
  signals and confirmed by the user: the **type(s)** — `website`, `web-app`,
  `api`, `cli`, `library`, or a combination — and the **characteristics**, the
  data/behavior facts a type doesn't capture (`handles-auth`, `is-public`,
  `handles-payments`, `handles-pii`, `has-database`, `is-multilingual`). A
  project can be several types and carry several characteristics.
- **Lenses.** A lens (`lenses/<name>.md` in the plugin) is a situational
  checklist for one concern. It activates two ways: from the **type**
  (`seo`←`website`, `ux`←`web-app`/`website`, `api`←`api`, `cli`←`cli`,
  `library`←`library`) or from a **characteristic** (`security`←auth/public/
  payments/PII, `i18n`←multilingual, `data`←database) — because a concern like
  security is a property of what the software does with data, not its shape. A
  lens is **knowledge, not a role**: it gives the *existing* agents extra checks
  to run in the phases they own, so the concern flows through the whole loop
  exactly like accessibility does — written as a measurable NFR in Specify,
  design-checked, verified in Review and (where it has a browser surface) QA
  under the same `NFR-n` ID. Nothing is asserted in one phase and never verified.
  Non-UI lenses (`api`, `cli`, `library`, `data`) have no `/demo-day` surface;
  their verification is carried by Specify, Review and the increment's own tests.

How a concern travels the loop, using `seo` on a `website` as the example:

```
 /story-time      /look-and-feel     /peer-review        /demo-day
 PO writes an  ─▶ Designer checks ─▶ Reviewer checks  ─▶ QA measures LCP/CLS,
 SEO NFR          heading/semantic   metadata, SSR vs    rendered titles &
 (NFR-n)          structure          client-only render  meta, in the browser
```

**Detection vs. decision.** The constitution is the **single source of truth**:
its *Project Profile* is the only place a lens is switched on, and every phase
reads the active lenses from there. Without a constitution, the phase skills do
**not** apply lenses off a guess — they give a one-line **nudge** ("this looks
like a `website` — an `seo` lens would apply; run `/charter` to record it") and
nothing more. So a lens is only ever applied from a profile entry the user
confirmed, never from a fallback and never silently; the nudge just surfaces the
choice early. This keeps the phases from drifting: there is one profile, not one
guess per phase. When **4 or more** lenses are active, the profile flags the
elevated load — there is no cap, but the count is made visible so agents in each
phase scrutinize the stack rather than skim it. Adding a new concern is a new
`lenses/<name>.md` file plus a profile entry — no agent or skill is rewritten,
because the skills pass active lens paths to their agents generically. The full
contract and the detection signals live in
[`lenses/README.md`](../lenses/README.md).

## The Artifact Chain

Every feature lives in `.spark/<feature-name>/` inside the target project.
Each phase produces exactly one artifact, and each artifact declares which
input it requires — including the status that input must have:

```
 spec.md ──▶ plan.md ──▶ (code) ──▶ review.md ──▶ qa.md ──▶ release.md
 approved    approved    tasks done   passed       passed     released
```

| Artifact | Written by | Requires | Terminal status |
|---|---|---|---|
| `spec.md` | `/story-time` + `/look-and-feel` | the idea | `approved` (or `rejected`) |
| `plan.md` | `/sprint-plan` | spec `approved` | `approved` |
| the code | `/increment` | plan `approved` | all tasks `done` |
| `review.md` | `/peer-review` | tasks `done`, build green | `passed` |
| `qa.md` | `/demo-day` | review `passed`, running app | `passed` |
| `release.md` | `/go-live` | review + qa `passed` | `released` (or `aborted`) |

Because the artifacts carry the state, the loop is **resumable**: any later
session (or `/spark`) reads the statuses and continues at the first gate
that isn't closed. There is no hidden state outside `.spark/`.

## Gates

Every template ends in a gate checklist. A gate is closed when every box is
genuinely true — and gates enforce three invariants:

1. **No phase starts on an open gate.** `/sprint-plan` refuses a draft spec;
   `/go-live` refuses open QA blockers. There is no "just this once".
2. **Only the human approves.** Agents draft, check and recommend — but
   `approved`, waivers and the publish go are always the user's, given
   explicitly in the conversation. An earlier approval never carries over
   to a later gate.
3. **Overrides are recorded, not silent.** The user *may* overrule a gate
   (e.g. waive a Major finding). The override, its reason, and who gave it
   go into the artifact — the trail stays honest.

## The Feedback Loops

Findings never get "fixed in place" by the role that found them — they route
back through the developer, and the finding phase re-runs:

```
                    ┌────────────── findings ──────────────┐
                    ▼                                       │
 /sprint-plan ──▶ /increment ──▶ /peer-review ──▶ /demo-day ──▶ /go-live
       ▲                │  ▲                          │
       │                │  └───────── bugs ───────────┘
       └── plan wrong ──┘
```

- **Reviewer** fixes only obvious, low-risk issues itself (recorded as
  `fixed`); everything else goes to `/increment` fix-mode, then re-review.
- **QA** fixes nothing, ever. Bugs go to `/increment`, then `/demo-day`
  re-tests the fix *and* the flows around it.
- **Plan wrong?** `/increment` never improvises architecture. It stops, and
  the loop returns to `/sprint-plan` (revision) or `/story-time`.
- **Escalation:** `/spark` counts rounds — after three failed rounds of the
  same phase it stops and puts the situation to the user, because at that
  point the plan or the spec is the problem, not the code.

## Who Does What — and What They May Not

| Role | Owns | Explicitly may not |
|---|---|---|
| Facilitator | drafting the constitution; grounding it in reality | approve it; write per-feature requirements into it |
| Product Owner | the *why* and *what*; scope; stories | write solutions; approve their own spec |
| Designer | design quality of the spec/UI | invent scope; touch non-design spec sections |
| Engineering Manager | the *how*; architecture; task cut | change the spec; approve their own plan |
| Developer (`/increment`) | the code | deviate from the plan; scope-creep |
| Reviewer | the review verdict; obvious fixes | waive own findings; refactor at will |
| QA Tester | the QA verdict, in a real browser | fix code; pass anything unobserved |
| Release Manager | the release; the learnings | release over a red gate; publish without the user's go |

The separations are the point: the QA tester who patched the app would test
their own work; the reviewer who waives their own finding reviews nothing.

## Traceability

The spec assigns stable IDs — `US-n` (stories), `AC-n.m` (acceptance criteria)
and `NFR-n` (non-functional requirements) — and every downstream phase cites
them, so any requirement can be traced forward to the work that satisfies it
and any line of work traced back to the requirement that justifies it:

```
 spec: AC-1.1 ──▶ plan: task "Covers AC-1.1" ──▶ review: AC-1.1 → file.ts:42 ──▶ qa: AC-1.1 ✅
```

The rules that keep the chain honest: IDs are never renumbered (new ones append
at the end); the plan gate refuses a Must AC that no task covers; the review
traces each Must AC to implementing code; and QA verifies each AC and each
browser-observable NFR under the same ID. A requirement that falls out of the
chain at any hop is a gate failure, not an oversight to catch later.

Ambiguity is removed *before* the chain starts: the Specify phase runs a
**Clarify pass** — a structured sweep across functional boundaries, data,
permissions, error cases, NFRs, integrations and UX states — and records each
resolution in the spec's *Clarifications* table. An unresolved clarification is
an open question and keeps the spec gate closed.

## Conventions

- **Feature names** are short kebab-case (`weekly-stats-dashboard`), used as
  the directory name under `.spark/`.
- **Statuses** are lowercase, in the artifact's header table. Skills keep
  them accurate at all times — they are the loop's state machine.
- **Severities** everywhere: `Blocker` > `Major` > `Minor` (> `Nit` in code
  review). Blockers always block their gate; Majors need an explicit,
  recorded user waiver; Minors are accepted or fixed at the user's choice.
- **Templates** live in the plugin (`templates/`); artifacts are always
  instantiated into the target project, never edited in the plugin.
- **English** for all artifacts, code and reports — regardless of the
  conversation language.

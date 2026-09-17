# Lenses — situational concern checklists

A **lens** is a focused checklist for a concern that only matters for *some*
kinds of software: SEO matters for a public website, not for a CLI; deep UX
craft matters for an app-like frontend, not for a backend service. Lenses are
**knowledge, not roles** — they don't add team members or ceremonies. They give
the existing agents an extra checklist to run when, and only when, the project's
profile says the concern applies.

This is the same idea the Designer already uses internally with its *Critique
Lens*, generalized so any phase can pick up any concern the project actually has.

## How a lens gets activated

1. **The profile decides.** `.spark/constitution.md` holds a *Project Profile &
   Active Lenses* section (written by `/charter`, grounded in the repo by the
   Facilitator). It lists the project's type(s) — `website`, `web-app`, `api`,
   `cli`, `library` — and its **characteristics** (`handles-auth`, `handles-pii`,
   `is-public`, `has-database`, `is-multilingual`, …). The **active lenses** are
   derived from both (see *Two ways a lens activates* below).
2. **The skill resolves and passes it.** Each ceremony skill reads the active
   lenses from the constitution and passes the relevant lens file paths (from
   `${CLAUDE_PLUGIN_ROOT}/lenses/`) to its agent, alongside the template.
3. **The agent applies its slice.** Every lens tags each check with the phase
   that owns it. An agent applies only the rows for its phase, with the same
   rigor as its core checklist, and reports findings/verifications under the
   same severity and traceability rules as everything else.

**No constitution?** The loop still works, but the constitution is the **single
source of truth** — it's the only place a lens is switched on. Without one, the
phase skills do **not** apply lenses off a guess; they give a one-line **nudge**
(name the likely type from the signals below and point to `/charter`) and nothing
more. A lens is applied only from a confirmed profile entry, never from a fallback
and never silently — the nudge just surfaces the choice early so the user can make
it permanent via `/charter`.

## Two ways a lens activates

A concern isn't always a shape of software. Some lenses bind to the project
**type** (SEO only makes sense for a website); others bind to a **characteristic**
— what the software *does with data* — independent of type (security applies to a
website, a web-app or an api alike, as soon as it handles auth or PII). The
profile records both, so:

- **Type-triggered lenses** declare `applies-to: [<type>]` — `seo`←`website`,
  `ux`←`web-app`/`website`, `api`←`api`, `cli`←`cli`, `library`←`library`.
- **Characteristic-triggered lenses** declare `triggers: [<characteristic>]` —
  see the *Characteristics* detection-signals table's `Activates` column below
  for the current mapping; it is the single declaration of this fact, not
  restated here.

## The lens contract (what every lens file guarantees)

- **Frontmatter** declares `name`, either `applies-to` (project types) or
  `triggers` (characteristics), and `phases` (which SPARK phases have checks).
- **A per-phase map** says which agent owns which area, mirroring the spec's
  `NFR` "How it's verified" column — so a concern raised in Specify is actually
  verified downstream, never just asserted.
- **Falsifiable checks only.** Every item is observable/checkable, tied to a
  concrete signal — the same bar the Designer's findings meet ("names its
  location, the rule it violates, and a concrete fix"). No "make it SEO-friendly".
- **The lens flags; it never invents scope.** Like the Designer, a lens surfaces
  a concern as a finding or a proposed NFR — turning it into a built feature is
  the PO's call, not the lens's.

## Detection signals

The Facilitator (in `/charter`) and the phase skills' fallback detection use
these signals. A project can be **several types at once** — e.g. a Next.js app
with a public marketing site *and* an authed dashboard is `website` + `web-app` —
and carries any number of characteristics.

### Project types (activate type-triggered lenses)

| Type | Signals |
|---|---|
| `website` (public, indexable) | SSR/SSG framework with page routes (Next.js, Astro, Nuxt, SvelteKit, Gatsby, Hugo/Jekyll/Eleventy) or multi-page HTML; `robots.txt`, `sitemap.xml`, `public/` marketing routes; content meant to be found by search engines |
| `web-app` (app-like frontend) | SPA (Vite/CRA React·Vue·Svelte without SSR), routes behind auth, dashboard/tool UI; indexability is not a goal |
| `api` / backend service | Express·Fastify·Nest·FastAPI·Flask·Spring route handlers, OpenAPI spec, no UI |
| `cli` | `bin` entry in `package.json`, `commander`/`click`/`argparse`, terminal entrypoint |
| `library` | `main`/`exports` published package, no `bin`, no server, consumed as a dependency |

### Characteristics (activate characteristic-triggered lenses)

| Characteristic | Signals | Activates |
|---|---|---|
| `handles-auth` | login/session/JWT/OAuth code, auth middleware, a users/credentials table | `security` |
| `is-public` | deployed to the open internet, no VPN/allowlist gate, unauthenticated routes | `security` |
| `handles-payments` | Stripe/PayPal/billing integration, checkout, card data flow | `security` |
| `handles-pii` | stores names, emails, addresses, health/financial data; a privacy policy exists | `security` |
| `has-database` | Postgres/MySQL/Mongo/SQLite, an ORM, migration files | `data` |
| `is-multilingual` | i18n library (i18next, `react-intl`, `vue-i18n`, gettext), locale files, a language switcher | `i18n` |
| `must-be-accessible` | an existing accessibility statement/VPAT/WCAG target in the repo, a public-facing product under a legal accessibility mandate (EAA, ADA Title II/III, Section 508, EN 301 549), or a direct user confirmation at `/charter` absent a file-based signal — same judgment-call latitude `is-public` already has | `accessibility` |

## Available lenses

| Lens | Activated by | Adds |
|---|---|---|
| [`seo.md`](seo.md) | type `website` | Discoverability, rendering/indexability, metadata, Core Web Vitals, structured data |
| [`ux.md`](ux.md) | type `web-app`, `website` | Interaction depth beyond base heuristics: flows, forms, responsive/mobile, feedback & motion |
| [`api.md`](api.md) | type `api` | Resource/method design, error-envelope consistency, versioning & breaking-change detection, auth surface |
| [`cli.md`](cli.md) | type `cli` | Help/discoverability, stdout/stderr & scriptability, exit codes, safety flags |
| [`library.md`](library.md) | type `library` | Public API surface, semver/deprecation discipline, packaging & footprint, contract clarity |
| [`security.md`](security.md) | char. `handles-auth`, `is-public`, `handles-payments`, `handles-pii` | Depth beyond the Reviewer baseline: header/transport hardening, auth lifecycle, authz matrix, supply chain, PII/privacy |
| [`i18n.md`](i18n.md) | char. `is-multilingual` | Externalized strings, locale-aware formatting, text-expansion & RTL layout |
| [`data.md`](data.md) | char. `has-database` | Migration safety, integrity/transactions, indexing at scale, retention & recovery |
| [`accessibility.md`](accessibility.md) | char. `must-be-accessible` | Specify-through-QA a11y depth beyond the Designer's baseline: grounded NFR, semantic HTML/ARIA in Act, keyboard-trap/focus checks in Review, keyboard-only + measured-contrast in QA |

## Adding a lens

A new concern is a new file, nothing else — no new agent, no skill rewrite:

1. Create `lenses/<name>.md` following the contract above (copy an existing one).
   Declare `applies-to` (a project type) or `triggers` (a characteristic).
2. Give each check a phase owner in the lens's own `phases:` frontmatter field —
   that field is what every dispatching skill reads to decide who receives the
   lens file. A missing or misspelled `phases` entry silently drops the lens
   from every phase it should reach, with no error to surface the mistake.
3. Add it to the *Available lenses* table here and, if it binds to a new type
   or a new characteristic, to the detection-signals tables above and the
   *Two ways a lens activates* section — these are the lists an author must
   still update by hand for this file to stay the accurate single source of
   truth. Three prose copies *outside* this file also name lenses for a human
   reader and are not sourced from here, so they need the same hand update if
   you want them to stay accurate: [`README.md`](../README.md)'s own lens
   table, [`docs/status.md`](../docs/status.md), and
   [`docs/workflow.md`](../docs/workflow.md).
4. Its checks flow automatically: every dispatching skill and the `/charter`
   activation path now read this file's tables and each lens's own `phases`
   frontmatter, rather than a closed, named list — a lens declaring
   `specify`, `design`, `review` or `qa`, and any new characteristic, reaches
   its agents and becomes declarable at `/charter` with no skill, agent or
   template edit. The one exception is `act`: `/increment` dispatches no
   lens files at all, so an `act` check is realized through the checks a
   spec author writes into §5 Non-Functional Requirements, not by dispatch —
   unchanged by this fix. See
   [`.spark/lens-dispatch-registry/evidence.md`](../.spark/lens-dispatch-registry/evidence.md)
   for the worked proof (all 9 shipped lenses, both dispatch and activation)
   and [`.spark/accessibility-lens/evidence.md`](../.spark/accessibility-lens/evidence.md)
   for the original finding that prompted the fix.

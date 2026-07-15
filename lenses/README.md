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
  `security`←`handles-auth`/`is-public`/`handles-payments`/`handles-pii`,
  `i18n`←`is-multilingual`, `data`←`has-database`.

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

## Adding a lens

A new concern is a new file, nothing else — no new agent, no skill rewrite:

1. Create `lenses/<name>.md` following the contract above (copy an existing one).
   Declare `applies-to` (a project type) or `triggers` (a characteristic).
2. Give each check a phase owner so a real agent verifies it.
3. Add it to the *Available lenses* table here, and to the detection signals if
   it binds to a new type or a new characteristic.
4. Its checks flow automatically: the skills pass active lens paths to their
   agents by name, so any activated lens is picked up without further wiring.

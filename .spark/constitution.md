# Constitution: aSPARK Core

| | |
|---|---|
| **Scope** | Project-wide — binds every SPARK phase and every feature |
| **Owner** | The user (amended via `/charter`) |
| **Status** | `active` |
| **Date** | 2026-08-06 |

<!-- The constitution is the project's standing context: the principles and constraints that would
     otherwise be re-explained at the start of every feature. Every agent (Product Owner, Designer,
     Engineering Manager, Reviewer) reads this file before doing phase work. Keep it short and true —
     a constitution nobody follows is worse than none. Amend it with /charter when reality changes. -->

**What this project is.** This repo *is* aSPARK Core: the Claude Code plugin that
provides the SPARK loop. It ships 10 skills, 7 agents, 8 lenses and 6 templates as
Markdown prompt material plus two JSON manifests, and is installed from a plugin
marketplace into *other people's* projects. It has no runtime, no build, no
dependencies and no executable code of its own.

## 1. Product Principles

- **Suppression is a feature.** Relevance beats coverage: a check that fires where
  it doesn't apply trains users and agents to skim, which erodes trust in every
  other check. A new concern must name the profile that activates it *and* the
  profiles where it stays silent.
- **The user is the only approver.** Agents draft, check and recommend; `approved`,
  every waiver and every publish is the user's, given explicitly and recorded in
  the artifact. No phase passes its own gate.
- **A change to the loop is validated by running the loop.** Prompt material has
  no test suite, so the evidence is a dogfood or dry run of the affected phases,
  written down. For a change that adds an optional capability, the **negative case
  runs first** — in a repo where the capability is absent, nothing may change.
- **Honesty about maturity over ambition.** Shipped, unproven and planned are
  labelled as such; a doc that presents an intention as delivered is a defect.
  *Known open exception:* `docs/aSPARK_Enterprise_Architecture_Handbook.docx`
  describes a target platform without per-chapter maturity labels — tracked as
  `handbook-maturity` in `.spark/BACKLOG.md`.

## 2. Project Profile & Active Lenses

- **Project type(s):** `library`.
  Evidence: `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` publish
  a versioned artifact (`0.3.1`, four releases) that other projects install as a
  dependency (`/plugin install aspark@aspark`). No `bin`, no server, no page routes,
  no UI. The "public API" is not code but the **consumed contract**: the ten slash
  commands, the `${CLAUDE_PLUGIN_ROOT}/…` paths skills resolve, and the protected
  structures in `templates/` (§3).
  <!-- Judgement call, not a literal signal match: there is no `main`/`exports` field
       because there is no package manifest. The library lens is proposed because its
       load-bearing sections — public surface and semver/breaking-change discipline —
       are exactly this repo's dominant risk. Its §3 "Packaging & footprint" is N/A
       (no bundle, no runtime deps, no engines to declare). -->
- **Characteristics:** none of the six.
  Nearest miss: `is-public` — the repo and the plugin are publicly distributed, but
  the detection signal for `is-public` is a *deployed* surface ("open internet, no
  allowlist gate, unauthenticated routes"), and there is none. Public *distribution*
  is handled as a constraint (§5, §6), not as a lens trigger.
- **Active lenses:**

| Lens | Why it's active (or off) | Enforced in |
|---|---|---|
| `library` | **Active** — consumers install a versioned artifact; every command name, template heading and ID pattern is a promise. Sections 1 (public surface), 2 (compatibility/versioning) and 4 (contract clarity) apply; section 3 (packaging/footprint) is N/A — no bundle, no dependencies | `/story-time`, `/peer-review` |
| `security` | **Off** — no runtime, no auth, no PII, no network surface, no dependencies to audit; 14 of the lens's 15 checks are inapplicable. The one live concern (instructing agents to execute an external command) is carried as a constraint in §3/§6 instead | — |
| `seo`, `ux` | Off — no website, no web-app, no UI of any kind | — |
| `api` | Off — no route handlers, no OpenAPI spec, no service | — |
| `cli` | Off — no `bin`, no process, no stdout/stderr or exit codes of our own; slash commands are prompts, not a terminal entrypoint | — |
| `i18n`, `data` | Off — single-locale (English), no database, no persistence | — |

- **Active-lens load:** 1 lens active. Elevated load does not apply.

## 3. Technical Constraints

- **Stack / runtime:** Markdown + JSON only. No build step, no runtime, no
  dependencies, no lockfile, no executable code. Introducing a language or
  toolchain requires an amendment.
- **Patterns to follow:**
  - **A new concern is a new file, not an edit to the roles.** A lens goes in
    `lenses/<name>.md`; skills pass lens paths to agents generically, so no agent
    or skill is rewritten. The same shape applies to any future optional-capability
    directory.
  - Plugin-internal paths are always referenced as `${CLAUDE_PLUGIN_ROOT}/…`, never
    relative.
  - One ceremony per `skills/<command>/SKILL.md`, frontmatter `name` identical to
    the folder and to the slash command; one role per `agents/<role>.md`.
  - Templates live in the plugin and are **instantiated** into the target project —
    never edited in place, never read from the target project.
- **The template contract (cross-repo, hard).** The sibling repo `aspark-graph`
  parses artifacts shaped by `templates/` and raises `TemplateDriftError` on a
  mismatch. There is **no version handshake** — no template carries a version
  marker, while the consumer pins `SUPPORTED_TEMPLATE = "aspark/0.1.0"`. Renaming
  or removing any of these is a silent breaking change in another repo:

  | Template | Protected — do not rename, do not remove |
  |---|---|
  | `spec.md` | story heading form `### US-<n> (<MoSCoW>): <title>`; AC line form `- [ ] AC-<n>.<m>: <text>` |
  | `plan.md` | the heading words `Task Breakdown`; the columns `#`, `Task`, `Story`, `Status`, `Definition of Done`; task IDs matching `^T\d+$` |
  | `review-report.md` | the heading word `Findings`; the findings table's columns `Severity`, `Location`, `Status`; finding IDs matching `^F\d+$` |
  | `qa-report.md` | the verification table's columns `Spec ID` and `Result` (`Spec ID` carries `AC-<n>.<m>` and `NFR-<n>` values) |
  | `release-notes.md` | the header-table rows `Status` and `Version` |

  **Appending a column is allowed** — the consumer matches headings by substring and
  tolerates extra columns. `plan.md` already carries `Covers (AC / NFR)` and
  `Depends on` beyond the protected five.
  ⚠ **Two known consumer defects, neither Core's to fix.** Both verified against
  `~/aSPARK-graph/src/aspark_graph/artifacts.py` on 2026-07-25.

  1. **Filename mismatch — the load-bearing one.** `_parse_feature` (lines 76–80)
     probes hardcoded paths `spec.md`, `plan.md`, `review-report.md`, `qa-report.md`,
     `release-notes.md`. Core instantiates its templates as `spec.md`, `plan.md`,
     **`review.md`**, **`qa.md`**, **`release.md`** (§5). Each probe is a bare
     `if x.exists():` with no `else` and no alias — so in *any* Core-managed project
     three of the five artifact types are **silently invisible**. `gate_health`
     reports `open_findings: 0` because it never opened a findings file, and
     `story_trace` ends at Code with no QA leg. Both look like clean answers.
  2. **`qa-report.md` column.** The contract docs name the column `AC`; the template
     ships `Spec ID`, because the table carries `NFR-<n>` rows as well as
     `AC-<n>.<m>` ones. `_parse_qa` (line 234) would raise `TemplateDriftError`, and
     `_cmd_build` treats that as fatal (`return 1`). This defect is **latent for Core
     projects and masked by defect 1** — the file is never found, so the guard is
     never reached. It fires only where trails happen to use template-style names.

  `Spec ID` is the protected name because it is what ships. Core renames nothing to
  accommodate the consumer; the fix belongs to the consuming repo. **Until defect 1
  is fixed, any `gate_health` or `story_trace` answer about review or QA state is
  unsound for a Core-managed project** — which constrains what an optional
  graph integration may claim (§6, degrade-to-silence).
- **Off-limits:**
  - **No hard dependency on a sibling repo** (`aspark-graph`, `aspark-policy`, or
    any external tool). Core is installed into arbitrary projects that have none of
    them.
  - No vendoring another repo's code, no installer, no auto-build, no auto-execute
    on the user's behalf.
  - No claim that an unpublished package is on a registry (`aspark-graph` is
    install-from-source, not on PyPI).
  - No secrets, credentials or customer material anywhere in the repo — including
    under `.spark/`, which is tracked and therefore published (§5).

## 4. Quality Bars (Definition of Done defaults)

- **Testing:** there is no automated test suite and none is possible for prompt
  material — do not write an NFR that assumes one. The bar is: `claude plugin
  validate` passes, **and** the change is exercised by a documented dogfood or dry
  run of every phase it touches, negative case first, with the result written down.
- **Traceability:** the `US-` / `AC-` / `NFR-` / `T` / `F` ID chain stays intact
  end to end. A change that breaks a downstream citation of an ID is a defect, not
  a cosmetic issue. IDs are never renumbered; new ones append.
- **Docs in step:** a capability ships in the same change as its README entry, and
  `README.md` §Project Status states what is proven and what is not (it asserts
  "This README always reflects the current state" — that assertion is the bar).
- **Backward compatibility:** every change is assessed against an already-installed
  consumer project before it ships. Breaking someone's running loop is this repo's
  worst failure mode.
- **Accessibility / performance:** N/A — this project ships no UI and no runtime.
  The real cost is *agent attention*; keep specs tight and NFRs few.

## 5. Conventions

- **Naming / structure:** kebab-case files and directories; feature directories are
  `.spark/<kebab-case-feature>/`. Templates are named `spec.md`, `plan.md`,
  `review-report.md`, `qa-report.md`, `release-notes.md`, but instantiate in target
  projects as `spec.md`, `plan.md`, `review.md`, `qa.md`, `release.md`.
- **Commits / branches:** Conventional Commits (`feat:`, `docs:`, `chore:`); one
  branch per feature, prefixed with its type (`feat/situational-lenses`).
- **Versioning:** one version, in `.claude-plugin/plugin.json`. A new optional
  capability is a minor bump; a change to a protected structure in §3 is breaking
  and released only in coordination with the consuming repo.
- **`.spark/` is tracked in this repo, so everything committed under it is public**
  on the marketplace repo. Precedent is deliberate (`.spark/situational-lenses/`) —
  keep it deliberate, never accidental.
- **Language:** English for everything committed, without exception — code, docs,
  templates, skills, agents and `.spark/` artifacts — regardless of the
  conversation language. Untracked working notes are scratch, not artifacts, and
  are out of scope for this rule; committing one puts it in scope.

## 6. Non-Negotiables

- **No silent breaking change to the consumed contract.** Renaming or removing a
  slash command, a protected template heading, column or ID pattern (§3) is
  breaking by definition — it needs a version bump and, for the template contract,
  a coordinated release with the consuming repo.
- **An optional integration degrades to silence, never to an error.** When the
  external tool is absent, every gate behaves *exactly* as it does today: no error,
  no warning, no mention. No gate ever blocks on the availability, freshness or
  emptiness of an optional tool's answer.
- **Nothing is executed or installed on the user's behalf unasked** — no
  auto-install, no auto-build, no destructive git or deploy action without the
  user's explicit go in the conversation.
- **No agent passes its own gate.** `approved`, waivers and the release go are the
  user's, and every override is recorded in the artifact with its reason.
- **Nothing that must stay private is committed** — this repo is public, `.spark/`
  included.

## 7. Delivery & Handoff

- **Release mode:** `pr` — this repo delivers via a GitHub pull request into `main`,
  not a direct push. Declared 2026-08-06 so that `tracker-handoff`'s own
  `handed-off` terminal status has a real venue to prove its positive case at its
  own `/go-live` (`.spark/tracker-handoff/spec.md`, clarification C8).
  ⚠ **This is a process commitment, not an enforced one.** `gh api
  repos/a-lottes/aSPARK/branches/main/protection` returned `404` ("Branch not
  protected") as of 2026-08-06 — there is no GitHub branch protection on `main`,
  and nothing in GitHub itself currently stops a direct push. This declaration
  governs how *aSPARK's own ceremonies* behave (which gate boxes, which terminal
  status); it does not, by itself, make a direct push impossible. Whether to also
  configure real branch protection is a separate, later decision — not made here
  (see amendment note below). Default when absent: `direct`.
- **Approver:** self-review via PR — the sole maintainer (`a-lottes`) opens a PR,
  reviews it themself, and approves/merges it, rather than pushing straight to
  `main`. Grounding: this repo has no `.github/` directory, no `CODEOWNERS` file,
  and no evidence of a second collaborator (`gh auth status` → authenticated as
  `a-lottes` only) — it is solo-maintained. Self-review-via-PR is a real but
  unusual pattern for a solo project; it still gives `handed-off` an honest,
  non-`released` terminal status by forcing the PR-open/CI-green checkpoint the
  mechanism exists to name, even without a second human. **Confirmed by the user,
  2026-08-06.** Default when absent: n/a (mode is `direct`).
- **Target branch:** `main`. Verified via `git remote -v`
  (`origin` → `git@github.com:a-lottes/aSPARK.git`) and `.git/config`
  (`branch "main"` tracks `origin/main`). Default when absent: n/a (mode is
  `direct`).
- **Ticket-reference format:** `none` — no ticket tracker is used for this
  project. `.spark/` is tracked and therefore public on this repo's marketplace
  listing (§5), so a real ticket ID or PR URL recorded there would be exposed;
  per `.spark/tracker-handoff/spec.md` NFR-10 this repo's own `spec.md` `Ticket`
  rows stay `none`. Default when absent: `none`.
- **Terminal status:** `handed-off` — the loop ends there once a release's PR is
  open, CI is green and the declared approver is requested; the real merge and
  tag happen outside aSPARK's control. Default when absent: `released` (direct
  mode's only terminal status).

---

## Amendments

| Date | Change | Why |
|---|---|---|
| 2026-07-25 | Initial constitution | First `/charter` on aSPARK Core itself — closes the dogfooding gap named as R6 in `.spark/situational-lenses/spec.md`, and records the project profile and the cross-repo template contract once instead of per feature |
| 2026-07-25 | Profile confirmed (`library` only, load 1; `security` off) and status set `active` | The user's decision on the drafted profile: `security`'s checks are 14/15 inapplicable to a repo with no runtime, auth, PII or dependencies; the one live concern is carried as a constraint in §3/§6 instead |
| 2026-07-25 | `qa-report.md`'s protected columns recorded as `Spec ID` + `Result`, with the consumer defect named | Verified against `aspark-graph`'s `_parse_qa` (`artifacts.py:234`): it demands a header equal to or starting with `ac` and raises `TemplateDriftError` on the shipped template. `Spec ID` is protected because it is what ships and it carries `NFR-<n>` as well as `AC-<n>.<m>`; renaming it back would break that semantics, so the fix is the consuming repo's |
| 2026-08-06 | Added `## 7. Delivery & Handoff`, declaring `pr` release mode into `main`, terminal status `handed-off`, `none` ticket format, and approver = self-review-via-PR (confirmed by the user) | Deliberate, already-decided switch to PR-first delivery per `.spark/tracker-handoff/spec.md` clarification C8 — this repo needs a real venue to prove `handed-off`'s positive case at its own `/go-live`, ahead of that feature's Keep phase. Mechanics (branch protection, exact approver identity) were explicitly scoped as this amendment's decision, not the spec's (spec §6 Out of Scope). The user confirmed self-review-via-PR as the approver and explicitly chose **not** to set up real GitHub branch protection now (`gh api .../branches/main/protection` → 404 at decision time) — the declaration is a process commitment the team is choosing to adopt, not a description of enforced infrastructure, flagged inline in §7 rather than papered over |
| 2026-08-15 | `review-report.md`'s protected structures extended with the findings table's columns `Severity`, `Location`, `Status` | The §3 row named only the `Findings` heading and the `^F\d+$` ID pattern, but `aspark-graph`'s `_parse_review` (`artifacts.py:202-205`, verified independently) hard-requires a findings-table header containing `severity`, `location` and `status` (substring match, case-insensitive, same tolerance as the rest of the contract) and raises `TemplateDriftError` if any is absent — so the constitution's own account of the contract was incomplete. Surfaced during `/story-time` on `lean-artifacts` (clarification C2 / tracked dependency A5), which scoped the fix out of its own diff because it renames nothing and doesn't touch this table. `qa-report.md`'s parser (`_parse_qa`) was checked in the same pass and requires only the `ac`/`result` columns already documented in the 2026-07-25 entry above — no scope expansion there |

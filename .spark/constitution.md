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
  This now holds for every tracked document without exception, the architecture
  handbook included (per-chapter Delivery stage labels, the ambition/delivery
  overview table and the inline `Status.` markers shipped with
  `handbook-maturity`, PR #27 / `085db99`).

## 2. Project Profile & Active Lenses

- **Project type(s):** `library`.
  Evidence: `.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` publish
  a versioned artifact (`0.8.0` today, released iteratively since `v0.1.0`) that
  other projects install as a dependency (`/plugin install aspark@aspark`). No `bin`, no server, no page routes,
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
  toolchain requires an amendment. Metrics and audit tooling lives outside this
  repo; published figures are reproducible from the committed reports under
  `docs/reports/`, not from a script shipped here.
  **No new tracked executable code is added.** A one-off scanner (for example
  the `situational-lenses` proof audit) runs as *untracked* scratch under §5,
  with its output committed as the evidence artifact; the script itself is never
  committed.
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
  - No registry or install claim about an external tool that isn't true at the time
    of writing, verified against the registry itself. `aspark-graph` **is** published
    on PyPI (verified 2026-09-11, HTTP 200), so `README.md`'s `pip install
    aspark-graph` is correct and must not be "corrected" back to install-from-source.
  - No secrets, credentials or customer material anywhere in the repo — including
    under `.spark/`, which is tracked and therefore published (§5).
  - **The published surface is the whole working tree, not the tracked files.**
    `.claude-plugin/marketplace.json` declares `"source": "./"` with no
    include/exclude mechanism, and an install copies *ignored* files too: the
    untracked, `.gitignore`-matched `docs/…Handbook.docx.bak` (≈2 MB) is present in
    `~/.claude/plugins/cache/aspark/aspark/0.8.0/docs/` — verifiable by listing that
    directory. So `.gitignore` is not a shield. Anything in the working tree at
    release time ships to every consumer.

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
- **Nothing that must stay private is in the working tree at release** — this repo
  is public, `.spark/` included, and `.gitignore` is no shield: a `source: "./"`
  install copies ignored files too (§3). The test is presence, not tracking.

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
  `main`. Grounding: this repo has **no `CODEOWNERS` file** and no evidence of a
  second collaborator (`gh auth status` → authenticated as `a-lottes` only) — it is
  solo-maintained. (`.github/` does exist, re-verified 2026-09-11: six files, five
  issue templates and a PR template, no `CODEOWNERS` and no workflows.)
  Self-review-via-PR is a real but unusual pattern for a solo project; it still
  gives `handed-off` an honest, non-`released` terminal status by forcing the
  PR-open/validate-green checkpoint the mechanism exists to name, even without a
  second human. **Confirmed by the user,
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
  open, `claude plugin validate` passes locally (§4's real bar) and the declared
  approver is requested; the real merge and tag happen outside aSPARK's control.
  There is **no CI to be green**: this repo has no `.github/workflows/` directory
  (verified 2026-09-11), so the quality checkpoint is the local validate run plus
  §4's documented dogfood, never a GitHub check. Default when absent: `released` (direct
  mode's only terminal status).

## 8. QA Method

- **Browser-observable surface:** `no` — aSPARK Core is a Claude Code plugin made
  of Markdown. **Zero executable files** — `git ls-files '*.py'` returns nothing,
  and that clause is the one here that stays true as the repo grows, so verify it
  live rather than against the count below. The rest is an inventory taken at
  `db4ab15`, the commit that removed the last script: 106 tracked files — 90
  `.md`, 5 `.yml` (GitHub issue templates and their `config.yml` — there is **no**
  CI workflow in this repo), 4 asset `.png`, 4 `.json` (2 plugin manifests + 2
  metrics reports under `docs/reports/`), 1 `.docx` handbook, plus `LICENSE` and
  `.gitignore`. A total is pinned to its commit on purpose: a feature's own
  artifacts change it while that feature is still in flight, so a live total
  would be false more often than true. No package manifest, no `bin`, no server,
  no route handler, no page — `/demo-day`'s browser gate cannot be satisfied here.
  Default when absent: `yes`.
- **Substitute verification method:** hands-on QA against the **installed
  plugin**, where a performed step is a real ceremony invocation or a real
  command whose output was observed. Reading a Markdown file and reasoning about
  what it *would* do is never a performed step and never passes an acceptance
  criterion — such rows are marked `not-verified-live`. Method and its evidence
  rule established in `.spark/graph-gates/qa.md` §1. Default when absent: none —
  the QA phase asks the user, exactly as today.

This changes the QA phase's **method**, never its coverage: `qa.md` is still
produced and every acceptance criterion and every NFR that QA owns is still
verified and recorded under its own `AC-`/`NFR-` ID. It is browser/QA-specific
and grants no other ceremony an off switch. Only `/charter` may create or amend
it.

---

## Amendments

| Date | Change | Why |
|---|---|---|
| 2026-07-25 | Initial constitution | First `/charter` on aSPARK Core itself — closes the dogfooding gap named as R6 in `.spark/situational-lenses/spec.md`, and records the project profile and the cross-repo template contract once instead of per feature |
| 2026-07-25 | Profile confirmed (`library` only, load 1; `security` off) and status set `active` | The user's decision on the drafted profile: `security`'s checks are 14/15 inapplicable to a repo with no runtime, auth, PII or dependencies; the one live concern is carried as a constraint in §3/§6 instead |
| 2026-07-25 | `qa-report.md`'s protected columns recorded as `Spec ID` + `Result`, with the consumer defect named | Verified against `aspark-graph`'s `_parse_qa` (`artifacts.py:234`): it demands a header equal to or starting with `ac` and raises `TemplateDriftError` on the shipped template. `Spec ID` is protected because it is what ships and it carries `NFR-<n>` as well as `AC-<n>.<m>`; renaming it back would break that semantics, so the fix is the consuming repo's |
| 2026-08-06 | Added `## 7. Delivery & Handoff`, declaring `pr` release mode into `main`, terminal status `handed-off`, `none` ticket format, and approver = self-review-via-PR (confirmed by the user) | Deliberate, already-decided switch to PR-first delivery per `.spark/tracker-handoff/spec.md` clarification C8 — this repo needs a real venue to prove `handed-off`'s positive case at its own `/go-live`, ahead of that feature's Keep phase. Mechanics (branch protection, exact approver identity) were explicitly scoped as this amendment's decision, not the spec's (spec §6 Out of Scope). The user confirmed self-review-via-PR as the approver and explicitly chose **not** to set up real GitHub branch protection now (`gh api .../branches/main/protection` → 404 at decision time) — the declaration is a process commitment the team is choosing to adopt, not a description of enforced infrastructure, flagged inline in §7 rather than papered over |
| 2026-08-29 | Added `## 8. QA Method`, declaring `Browser-observable surface: no` and naming the substitute method (hands-on QA against the installed plugin, with a performed step defined as a real ceremony invocation or an observed command output) | Confirmed explicitly by the user at `/charter`, drafted from named evidence only — 72 tracked `.md` files and no package manifest, `bin`, server or route handler — never inferred from the profile or from `ux`/`seo` being off, per `.spark/right-sizing/spec.md` AC-1.8. Retires a negotiation that had recurred on four consecutive features (`graph-gates`, `handbook-maturity`, `lean-rounds`, and this one), each time re-deciding the same override by hand. The method and its "performed step" rule are not new: they were established and used at `.spark/graph-gates/qa.md` §1; this records them once as a standing project fact instead of per feature. Coverage is unchanged — `qa.md` is still produced with every `AC-`/`NFR-` ID verified |
| 2026-08-15 | `review-report.md`'s protected structures extended with the findings table's columns `Severity`, `Location`, `Status` | The §3 row named only the `Findings` heading and the `^F\d+$` ID pattern, but `aspark-graph`'s `_parse_review` (`artifacts.py:202-205`, verified independently) hard-requires a findings-table header containing `severity`, `location` and `status` (substring match, case-insensitive, same tolerance as the rest of the contract) and raises `TemplateDriftError` if any is absent — so the constitution's own account of the contract was incomplete. Surfaced during `/story-time` on `lean-artifacts` (clarification C2 / tracked dependency A5), which scoped the fix out of its own diff because it renames nothing and doesn't touch this table. `qa-report.md`'s parser (`_parse_qa`) was checked in the same pass and requires only the `ac`/`result` columns already documented in the 2026-07-25 entry above — no scope expansion there |
| 2026-09-11 | §1: the handbook honesty exception **closed** — the principle now holds for every tracked document without exception | The exception was stale. `handbook-maturity` completed and merged as PR #27 (`085db99`): every chapter carries a Delivery stage label, an overview table up front splits ambition from delivery, 18 inline `Status.` markers qualify target-state claims, and the title page separates the handbook revision from the shipped baseline. `ROADMAP.md` lists "Maturity labels in the handbook" under **Shipped** and names closing this exception as its own *Next* item (follow-up to issue #18, explicitly scoped there as post-release constitutional bookkeeping). The loop's residuals were checked before closing and none reopens the exception: review F2 (Nit — pre-existing prose citing v0.4.x versions, verified to contradict nothing v0.7.0 ships) and QA E1–E3 were user-accepted and routed to the still-unpicked-up website-sync / handbook-revision follow-up. They are version-currency nits, not ambition presented as delivered, so they stay in `ROADMAP.md`/issues rather than here — as does carrying handbook corrections over to the separate website repo, which is another project's obligation and is not practice here today |
| 2026-09-11 | §3 off-limits: the registry-claim rule **corrected** — the parenthetical calling `aspark-graph` install-from-source and not on PyPI is removed; the general no-false-registry-claim principle stays and now says to verify against the registry | The constitution was the stale document, not the README. `https://pypi.org/pypi/aspark-graph/json` returns HTTP 200 with author "Andreas Lottes" — the package is published. `README.md:226-227` (`published on PyPI as aspark-graph`, `pip install aspark-graph`) and `tools/README.md:125` are therefore accurate and were left untouched. The old wording actively invited a future agent to "fix" a correct README back into a false statement, which is the opposite of what the rule is for |
| 2026-09-11 | §3 stack/runtime: **no exception — Markdown + JSON only stands**, with metrics and audit tooling placed outside this repo, `scripts/spark-metrics.py` named as a known open exception **ruled for removal**, and a standing rule that no new tracked executable code is added (one-off scanners run as untracked scratch under §5, their output committed as the evidence artifact). §8's inventory, §2's version evidence and `cli` justification, and the preamble's "no executable code" claim refreshed to the real tracked file set | The script shipped 2026-09-09 (`f446ca5`, plus `df1005f`/`678f04d` for the cross-machine merge and `b6b7aab` for `docs/reports/*.json`) with no amendment, so the repo's most recent feature had falsified §3's first line. The Facilitator drafted both bounds — a narrow stdlib-only `scripts/` exception (its recommendation) and no exception at all — and the user ruled for **no exception**, knowingly: with `marketplace.json` declaring `"source": "./"` and no include/exclude mechanism, "keep it but don't ship it" does not exist, so keeping the script would have meant knowingly installing a 32 KB executable into every consumer's plugin cache at the next release. The script is recorded in §1's established *known open exception* form rather than deleted from the text, because it still exists on disk today and a flat "no executable code" would have recreated the very defect this amendment fixes; it is marked a scheduled deletion under a ruling already made, not grandfathered, and closing it when the deletion lands is a one-line edit. The deletion itself is follow-up product work, not this ceremony's: `README.md` §Project Status and `docs/metrics.md` instruct readers to run the script and ground the published 54-feature figure on `--merge docs/reports/*.json` being checkable, so removing it rewrites both. Bookkeeping corrected in the same pass against `git ls-files` (104 tracked: 87 `.md` — was 72; 4 `.json` — was 2; the `.py` and `.docx` previously unlisted) and against `.github/`, which holds **no** workflow at all — §8's "5 workflow `.yml`" were issue templates. §2's evidence cited version `0.3.1`/four releases against a live `0.8.0` |
| 2026-09-11 | §7: two stale grounding facts **corrected** — the Approver bullet no longer claims this repo has no `.github/` directory, and the `handed-off` checkpoint no longer names a CI. The terminal status now reads PR open + `claude plugin validate` passing locally (§4's real bar) + approver requested | `.github/` exists (re-verified 2026-09-11: five issue templates plus a PR template, six files) — but there is **no `CODEOWNERS`** and no second collaborator, so the conclusion the evidence supported is unchanged: solo-maintained, self-review-via-PR, confirmed by the user 2026-08-06 and untouched here. The bigger falsity was "CI is green": there is no `.github/workflows/` directory at all, so the checkpoint named a gate that cannot be performed and that no past release performed. Reworded to the checkpoint that is real and that releases actually ran, rather than dropping the quality bar or inventing a CI requirement. **The branch-protection decision and its inline ⚠ are deliberately untouched** — that decision stands exactly as made |
| 2026-09-11 | §3 off-limits gains **"the published surface is the whole working tree, not the tracked files"**, and §6's privacy non-negotiable retuned from *committed* to *present in the working tree at release* | Discovered while auditing the tracked-file inventory: `docs/…Handbook.docx.bak` is untracked **and** `.gitignore`-matched (`.gitignore:22:*.bak`, confirmed by `git check-ignore -v`), yet it is present in the installed plugin cache at `~/.claude/plugins/cache/aspark/aspark/0.8.0/docs/`. A `source: "./"` install copies ignored files, so `.gitignore` does not protect the shipped surface and ≈2 MB of untracked backup reaches every consumer. Stated here rather than left as release bookkeeping because §6's privacy rule was *wrong about its own test*: it bounded exposure by what is committed, when the real bound is what is present. Falsifiable by listing that cache directory. Removing the `.bak` and adding a `/go-live` pre-flight that asserts what the install actually ships are follow-ups, not constitutional |
| 2026-09-11 | §3's *known open exception* **closed**: the last tracked executable file is deleted, so "Markdown + JSON only … no executable code" now holds without qualification. The preamble drops its script sentence, §2's `cli` row drops its parenthetical, §8's inventory is restated with zero executables, and the no-new-tracked-executable-code rule loses its "while the exception is open" framing and stands unconditionally | The removal ruled on earlier today was executed as the `metrics-script-removal` feature (`.spark/metrics-script-removal/`), so the exception has nothing left to describe. Closing it is recorded as its own row rather than by editing the row that opened it: amendment history is the audit trail of what was decided and when, and rewriting it to make a later grep come out clean would cost more than the grep is worth — the feature's `AC-4.1` asks for exactly that grep over this file and is recorded as **refuted-with-finding** instead (`.spark/metrics-script-removal/evidence.md`), a valid ceremony outcome under the project's `CLAUDE.md`. What replaced the tool is published in `docs/metrics.md`: three `python3` stdlib commands over the committed reports under `docs/reports/`, each with its observed output, plus the four combination rules read off the script before it was deleted — so every figure the README publishes stays checkable by a stranger who has only this repository. §8's total is now pinned to the commit it was taken at (`db4ab15`), because a feature's own artifacts change a live count while that feature is still in flight; the clause that stays live-verifiable is the one that matters, `git ls-files '*.py'` returning nothing. Authority for amending this file outside `/charter`: the user's ruling of 2026-09-11, recorded as `A2`/`A8` in that feature's spec |

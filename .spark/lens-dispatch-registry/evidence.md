# Evidence: lens-dispatch-registry

| | |
|---|---|
| Feature | lens-dispatch-registry |
| Phase | Act |
| Date | 2026-09-17 |

## T1 — Pre-fix baseline: all eight sites quoted, phase matrix, negative case, 2026-09-17

**Site count reconciliation.** Plan §1 frames this as "eight sites across seven files." Quoted at
clause level below there are nine distinct regions, because `agents/facilitator.md` and
`templates/constitution.md` each carry two separate clauses that both need the fix (vocabulary +
mapping; intro-comment mapping + standalone characteristics list) — consistent with the plan's
file-level count of eight, not a discrepancy. Every clause is quoted verbatim here so later tasks
and review don't have to reconstruct today's text from memory or from stale line numbers.

### Dispatch sites (US-2)

**`skills/look-and-feel/SKILL.md:32-35`:**
> 3. **Resolve active lenses.** The constitution is the single source of truth.
>    Read the active lenses from `.spark/constitution.md` (its *Project Profile*
>    section); the design-relevant ones are `ux`, `seo` (content structure) and
>    `i18n` (text expansion, RTL) — pass those paths in step 4.

**`skills/demo-day/SKILL.md:82-84`:**
> the paths of any active
> lenses with browser-observable checks (from the constitution's profile —
> `${CLAUDE_PLUGIN_ROOT}/lenses/` — `ux.md`, `seo.md`, `security.md`, `i18n.md`).

**`skills/peer-review/SKILL.md:49-51`:**
> the
> paths of any active lenses with review-phase checks (from the
> constitution's profile — `${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md` for any of
> `seo`, `api`, `cli`, `library`, `security`, `data`, `i18n` that are active).

### Activation sites (US-1)

**`agents/facilitator.md:50-53` (vocabulary):**
> auth walls) — and its **characteristics**, the data/behavior facts that
> activate concern lenses: `handles-auth`, `is-public`, `handles-payments`,
> `handles-pii`, `has-database`, `is-multilingual`. A project can be several
> types and carry several characteristics.

**`agents/facilitator.md:65-69` (mapping):**
> then derive the **active lenses** from both — types activate `seo`←`website`,
> `ux`←`web-app`/`website`, `api`←`api`, `cli`←`cli`, `library`←`library`;
> characteristics activate `security`←`handles-auth`/`is-public`/
> `handles-payments`/`handles-pii`, `i18n`←`is-multilingual`, `data`←
> `has-database`. Recommend a lens only when it genuinely warrants it; ...

**`templates/constitution.md:26-28` (intro-comment mapping):**
> the user confirms. Lenses activate two ways: from the project TYPE (seo←website, ux←web-app, api←api,
> cli←cli, library←library) and from CHARACTERISTICS — what the software does with data (security←handles-auth/
> is-public/handles-payments/handles-pii, i18n←is-multilingual, data←has-database). A project can be several

**`templates/constitution.md:35` (characteristics list comment):**
> <!-- any of: handles-auth · is-public · handles-payments · handles-pii · has-database · is-multilingual -->

### Folded-in sites (US-1 widening, user direction 2026-09-17 — no AC of their own, per plan §1/§2)

**`skills/spark/SKILL.md:66`:**
> lenses (`seo`, `ux`, `api`, `cli`, `library`, `security`, `i18n`, `data`)
> activate for every phase.

**`templates/spec.md:69`:**
> lenses (seo, ux, api, cli, library, security, i18n, data), their concerns for this feature land here

All nine quotes read today, 2026-09-17, on branch `feat/lens-dispatch-registry` before any edit in this
increment. None contains `accessibility` or `must-be-accessible`.

### Phase → lens resolution matrix, derived from all 9 `lenses/*.md` frontmatters

| Lens | `phases` (frontmatter) |
|---|---|
| `accessibility` | specify, design, act, review, qa |
| `api` | specify, review |
| `cli` | specify, review |
| `data` | specify, review |
| `i18n` | specify, design, review, qa |
| `library` | specify, review |
| `security` | specify, review, qa |
| `seo` | specify, design, review, qa |
| `ux` | specify, design, qa |

Resolved set per phase, across all 9 lenses (the target every post-fix instruction must reproduce when
all 9 are active):

| Phase | Resolved lenses | Count |
|---|---|---|
| specify | accessibility, api, cli, data, i18n, library, security, seo, ux | 9 |
| design | accessibility, i18n, seo, ux | 4 |
| act | accessibility | 1 |
| review | accessibility, api, cli, data, i18n, library, security, seo | 8 |
| qa | accessibility, i18n, security, seo, ux | 5 |

Matches plan §1/T1's stated figures (design 4, qa 5, review 8, act 1) exactly.

### This repo's own negative case (constitution §2: type `library`, zero characteristics)

Active-lens set = `{library}` only. `library`'s own `phases: [specify, review]`.

- **design** → `library` not in any design-phase lens's scope → **∅**
- **qa** → `library`'s phases don't include `qa` → **∅**
- **review** → `library`'s phases include `review` → **`{library}`**

This is the pre-fix state and, because nothing about *this repo's own* active-lens set changes in this
feature (no characteristic is being turned on for aSPARK Core itself), it is also the expected **post-fix**
state — T10 re-runs this exact derivation against the reworded text and expects an identical result. A
difference at T10 would mean the fix accidentally changed what a `library`-only project resolves to, which
would itself be a defect.

## T2 — Walking skeleton: `/look-and-feel` computed-set dispatch, proven end to end, 2026-09-17

**New text, `skills/look-and-feel/SKILL.md` step 3:**
> 3. **Resolve active lenses.** The constitution is the single source of truth.
>    Read the active lenses from `.spark/constitution.md` (its *Project Profile*
>    section); pass the path of every active lens whose own frontmatter `phases`
>    field includes `design` — read each active lens's file
>    (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`) to decide; do not work from a list
>    of lens names given here — in step 4. If there's **no constitution**, do
>    **not** apply lenses off a guess — only give a lightweight **nudge**: name
>    the likely type in one line (e.g. "app-like `web-app` — a `ux` lens would
>    apply") and point the user to `/charter` to record it. No lens is switched
>    on without a confirmed constitution entry.

No lens name appears as a dispatch list — `ux` appears once, inside the unrelated no-constitution
nudge, as an illustrative example ("a `ux` lens would apply"), not as a membership test; this mirrors
the "e.g." forms plan §2 already confirmed generic elsewhere (`skills/story-time/SKILL.md:41`,
`skills/charter/SKILL.md:39`).

**Full chain, walked for a hypothetical project that has declared `must-be-accessible`:**

1. **Constitution's active-lens set** (hypothetical): `{ux, seo, i18n, accessibility}` — a `web-app`
   type project (`ux`, `seo` per type-triggered activation) that also declared `must-be-accessible`
   (`accessibility` per characteristic-triggered activation) and `is-multilingual` (`i18n`).
2. **Each active lens's own frontmatter `phases`** (from T1's matrix): `ux` → design ✓, `seo` → design
   ✓, `i18n` → design ✓, `accessibility` → design ✓. All four include `design`.
3. **Resolved design set:** `{ux, seo, i18n, accessibility}` — matches T1's phase matrix design row
   restricted to this project's active-lens set; nothing dropped, nothing invented.
4. **Receiving agent's generic head clause** (`agents/designer.md:61-63`, unedited — verified generic
   at plan time, plan §2):
   > The base lens above applies to every UI. When the caller passes **active lenses**
   > for this project (from the constitution's profile — e.g. `ux`, `seo`), read each
   > lens file and also apply the checks it marks for the **design** phase
   >
   > Apply only lenses you were actually given; never invent a concern the profile
   > didn't activate.

   The Designer's own rule is "apply only what you were given" — it does not filter by name, so a
   passed `accessibility.md` path is applied exactly like a passed `ux.md` or `seo.md` path. The
   per-lens bullets under this clause (`ux`, `seo`, `i18n`) are worked examples of what those three
   lenses check, not an enumeration the Designer checks incoming paths against — confirmed by reading
   the clause immediately preceding them, which names no lens and imposes no such filter.

**Result:** the chain is unbroken — a hypothetical `accessibility`-active project's lens reaches the
Designer at the design phase with zero edits to `agents/designer.md`, satisfying AC-2.1 (no enumerated
subset in the skill's dispatch instruction) and contributing to AC-2.4 (the lens path is among what the
skill passes, verified by re-reading resolved text against frontmatter, not by execution — this repo
has no runtime to execute).

## T3 — `/demo-day` computed-set dispatch, 2026-09-17

**New text, `skills/demo-day/SKILL.md` step 2 (lens clause):**
> and the path of every active
> lens whose own frontmatter `phases` field includes `qa` — read each active
> lens's file (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`) to decide; do not work
> from a list of lens names given here.

The four-filename list (`ux.md`, `seo.md`, `security.md`, `i18n.md`) is gone; no lens name appears
anywhere in this clause.

**Resolved set** (same reasoning as T2, applied to `phases: qa` instead of `design`), against T1's
matrix: `{ux, seo, security, i18n, accessibility}` — five lenses, matching the plan's expected DoD set
exactly.

**"Browser-observable" qualifier, replaced by `phases: qa` — recorded, not silently dropped (plan §1
consequence).** The old text scoped dispatch to lenses "with browser-observable checks"; the new text
scopes it to lenses whose frontmatter declares the `qa` phase. These are the same set today (every lens
that declares `qa` — `ux`, `seo`, `security`, `i18n`, `accessibility` — does so because it has
browser-observable checks; `api`/`cli`/`library`/`data` correctly omit `qa` because they have none). The
replacement is a deliberate widening in *kind*, not in today's *membership*: it is also correct under
constitution §8's declared-substitute-method projects (like aSPARK Core itself), where "browser-observable"
is literally false (no browser exists) but a lens's `qa`-phase checks are still meant to run by the
declared substitute method — `phases: qa` resolves correctly in both cases, the old wording only in one.

**Receiving agent's generic head clause** (`agents/qa-tester.md:174-179`, unedited — verified generic at
plan time):
> 4. **Apply active lenses.** For each active lens the caller passed (from the
>    constitution's profile), verify its **browser-observable** checks and report
>    them under the matching `NFR-n`:
>    ...
>    Apply only lenses you were given; don't test a concern the profile didn't
>    activate.

Same shape as T2: the per-lens bullets (`ux`, `seo`, `security`, `i18n`) are worked examples of what
those four check, not a membership filter on what the skill may pass — a passed `accessibility.md` is
applied under the same "apply only lenses you were given" rule. The parenthetical noting `api`/`cli`/
`library`/`data` "have no browser surface" is accurate and untouched — those four correctly have no `qa`
in their own frontmatter, so they were never in this dispatch's resolved set either before or after the
fix.

**Result:** AC-2.2 (no enumerated filename subset) and AC-2.4 (resolved set includes `accessibility`,
re-derived from frontmatter) both satisfied.

## T4 — `/peer-review` parenthetical made non-restrictive, 2026-09-17

**New text, `skills/peer-review/SKILL.md` step 2 (lens clause):**
> the diff (commit range or changed files since the increment started), and
> the path of every active lens whose own frontmatter `phases` field includes
> `review` — read each active lens's file
> (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`) to decide; do not work from a
> list of lens names given here.

The seven-name parenthetical (`seo`, `api`, `cli`, `library`, `security`, `data`, `i18n`) is removed
entirely — not narrowed, not hedged. The head clause already read as generic ("the paths of any active
lenses with review-phase checks") before this edit; it was the parenthetical alone that restricted it,
per `evidence.md`'s own accessibility-lens finding (F6, downgraded from a clean pass once the
parenthetical was scrutinized). No parenthetical remains to repeat that mistake.

**Resolved set**, against T1's matrix, `phases` including `review`: `{accessibility, api, cli, data,
i18n, library, security, seo}` — eight lenses (`ux` correctly excluded, its frontmatter has no `review`
phase).

**Receiving agent's generic head clause** (`agents/reviewer.md:62-64`, unedited — verified generic at
plan time):
> 8. **Active-lens conformance** — when the caller passes active lenses (from the
>    constitution's profile), read each and verify the checks it marks for the
>    **review** phase against the diff. You own the review slice of most lenses:
>    ...
>    Apply only the lenses you were given.

Same shape as T2/T3: the eight per-lens bullets beneath this clause are worked checklists for what each
lens's review slice covers, not a membership test on what the skill may pass — there is no `accessibility`
bullet among them yet, but the clause doesn't require one to apply a lens it's given; a reviewer without
a worked bullet still applies the lens file's own review-phase content directly, per "read each and
verify the checks it marks."

**Result:** AC-2.3 (parenthetical removed / made non-restrictive) and AC-2.4 (resolved set includes
`accessibility`) both satisfied.

## T5 — Facilitator: registry-sourced characteristic vocabulary and lens mapping, 2026-09-17

**New text, `agents/facilitator.md:46-55` (vocabulary):**
> While you're here, **detect the project's profile** from the repo's signals
> (the detection tables in `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`): its
> **type(s)** — `website`, `web-app`, `api`, `cli`, `library`, or a combination
> (framework, routing, `bin`/`exports`, public/indexable pages, SSR/SSG config,
> auth walls) — and its **characteristics**, the data/behavior facts that
> activate concern lenses. Read the current characteristic list from
> `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s *Characteristics* detection-signals
> table rather than working from a list here — it names each characteristic
> and the signal that evidences it. A project can be several types and carry
> several characteristics.

**New text, `agents/facilitator.md:67-72` (mapping):**
> then derive the **active lenses** from both — types activate `seo`←`website`,
> `ux`←`web-app`/`website`, `api`←`api`, `cli`←`cli`, `library`←`library`; for
> characteristics, look up the current mapping in
> `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`'s *Two ways a lens activates*
> section rather than working from a list here. Recommend a lens only when it
> genuinely warrants it; ...

Neither clause contains an enumerated characteristic or lens list any more. The type-triggered half of
the mapping (`seo`←`website`, etc.) is deliberately **unchanged** — out of scope per spec C2 (types are
a stable, small enumeration, not evidenced as broken); only the characteristic-triggered half, the half
that actually grew once already (this exact feature), now defers to the registry.

**Resolution check.** Reading `lenses/README.md`'s *Characteristics* table (lines 82-92) today yields
6 rows: `handles-auth`, `is-public`, `handles-payments`, `handles-pii`, `has-database`,
`is-multilingual`, and `must-be-accessible` — **7 rows**, not 6 (the registry already includes
`accessibility`'s row, added when that feature shipped; only the facilitator's copy was stale). Reading
the *Two ways a lens activates* section (lines 37-49) resolves the characteristic→lens mapping to all
**four** characteristic-triggered lenses: `security`←`handles-auth`/`is-public`/`handles-payments`/
`handles-pii`, `i18n`←`is-multilingual`, `data`←`has-database`, `accessibility`←`must-be-accessible`
(`lenses/README.md:48-49`).

**AC-1.2 reading, applied (plan §1):** AC-1.2 asks that the mapping "name all characteristic-triggered
lenses the registry currently lists... not a subset." The *resolved* instruction — a Facilitator who
follows "look up the current mapping in `lenses/README.md`'s *Two ways a lens activates* section" —
lands on all four names, because that section names all four. The facilitator's own file names zero;
the resolution names four. This is the reading plan §1 pre-registered so a re-embedding "fix" (naming
the four here again) is recognized as recreating the defect, not as satisfying the AC more literally.

**Result:** AC-1.1 (vocabulary sourced from the registry, not a six-item cap) and AC-1.2 (mapping
resolves to all four characteristic-triggered lenses) both satisfied.

## T6 — Constitution template: point at the registry instead of copying it, 2026-09-17

**New text, `templates/constitution.md:26-27` (intro-comment mapping):**
> the user confirms. Lenses activate two ways: from the project TYPE (seo←website, ux←web-app, api←api,
> cli←cli, library←library) and from CHARACTERISTICS — see the plugin's lenses/README.md "Two ways a
> lens activates" section for the current characteristic→lens mapping. A project can be several

**New text, `templates/constitution.md:35` (characteristics list comment):**
> <!-- see the plugin's lenses/README.md "Characteristics" detection-signals table for the current list -->

**Byte-identity check.** `git diff templates/constitution.md` shows exactly two changed lines, both
inside HTML comments — the TYPE-mapping half of the intro comment (`seo←website`, etc., out of scope per
C2), the `- **Project type(s):**`/`- **Characteristics:**` field labels, the *Active lenses* table's
header row and every column, and every other line in the file are untouched. This satisfies plan §1's
byte-identity requirement and NFR-6 (`templates/spec.md` is the protected-contract file that needs this
same care at T8; `templates/constitution.md` itself is not in that protected set per spec C5, but the
same discipline was applied anyway since it ships to every new project).

**Consumer impact (NFR-6).** This file is read once, at `/charter` time, to seed a new project's
constitution. An already-instantiated consumer's `.spark/constitution.md` is a copy taken at that past
`/charter` run — it does not re-read this template later, so no existing consumer constitution is
touched by this edit; the improved guidance applies starting at that consumer's own next `/charter`
amendment, exactly as plan §1/R7 states.

**Result:** AC-1.3 (template points at the registry rather than embedding a copy) and AC-1.4 (a future
lens needs no template edit) both satisfied.

## T7 — `/spark`'s no-constitution nudge: name the registry, not eight lenses, 2026-09-17

**Old text, `skills/spark/SKILL.md:66`:**
> lenses (`seo`, `ux`, `api`, `cli`, `library`, `security`, `i18n`, `data`)
> activate for every phase.

**New text, `skills/spark/SKILL.md:64-68`:**
> `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`), name the likely type(s)/
> characteristics you see, and note that `/charter` records them so the
> matching lens — see the registry's *Available lenses* table for the current
> set — activates for every phase. Without a constitution no lens is applied —
> the nudge only surfaces the choice; the constitution is the single source of
> truth.

Old text lists 8 names, missing `accessibility`; new text points at the registry's *Available lenses*
table, which lists all 9 today and would list 10 for a hypothetical next lens with no further edit here.
The surrounding "without a constitution no lens is applied" sentence and the constitution-is-truth
framing are unchanged, as plan §1's T7 DoD requires.

**Resolved reading:** `lenses/README.md`'s *Available lenses* table (lines 94-106) lists all 9 shipped
lenses today, `accessibility` included — same table T5 already cited for the characteristic→lens
mapping.

**Result:** satisfies the widened US-1 intent (plan §1's scope-widening paragraph); no AC of its own, as
recorded there — T9's cross-check and T12's "gap is closed" claim both depend on this task landing.

## T8 — Spec template: NFR guidance sources its lens list from the registry, 2026-09-17

**Old text, `templates/spec.md:69`:**
> lenses (seo, ux, api, cli, library, security, i18n, data), their concerns for this feature land here

**New text, `templates/spec.md:66-72`:**
> <!-- Cross-cutting qualities the feature must meet, separate from functional behavior. Each NFR is
>      falsifiable and downstream-traceable (NFR-n). Delete a row only if it genuinely does not apply —
>      "N/A" with a one-line reason is better than a silent gap. If the constitution's profile has active
>      lenses (see the plugin's lenses/README.md "Available lenses" table for the current set), their
>      concerns for this feature land here as measurable NFRs — e.g. "LCP < 2.5s, unique title/description
>      per route" (seo), "every record access is authorized server-side; PII never logged" (security),
>      "migrations are reversible" (data). -->

The three worked examples (`seo`, `security`, `data`) are kept verbatim, still readable as worked
examples of *how* a lens's concern becomes an NFR — not as the membership list of which lenses exist,
which is now the registry's job.

**Byte-identity check (NFR-6, `templates/spec.md` is in constitution §3's protected contract set).**
`git diff templates/spec.md` shows exactly one changed region, entirely inside the `<!-- ... -->` HTML
comment. The `## 5. Non-Functional Requirements` heading, the `| # | Category | Requirement (measurable)
| How it's verified |` table header and its column count, and the `NFR-n` ID pattern used in the row
below it are byte-identical before and after. This is a comment-only change — spec C5's "additive/minor,
no major bump" verdict holds because no protected structure was touched, not because the touched file
happens to be low-risk.

**Result:** satisfies the widened US-1 intent, same as T7; no AC of its own, and T10 re-asserts this
byte-identity check at diff level across the whole increment (plan §1/R10).

## T9 — NFR-4 zero-omission cross-check, all 9 lenses, both layers, 2026-09-17

**Dispatch layer.** For a hypothetical project with all 9 lenses active, each reworked skill's resolved
instruction ("every active lens whose own frontmatter `phases` includes `<phase>`") against T1's matrix:

| Lens | `phases` | `/look-and-feel` (design) | `/demo-day` (qa) | `/peer-review` (review) |
|---|---|---|---|---|
| `accessibility` | specify, design, act, review, qa | ✅ included | ✅ included | ✅ included |
| `api` | specify, review | — correctly excluded | — correctly excluded | ✅ included |
| `cli` | specify, review | — correctly excluded | — correctly excluded | ✅ included |
| `data` | specify, review | — correctly excluded | — correctly excluded | ✅ included |
| `i18n` | specify, design, review, qa | ✅ included | ✅ included | ✅ included |
| `library` | specify, review | — correctly excluded | — correctly excluded | ✅ included |
| `security` | specify, review, qa | — correctly excluded | ✅ included | ✅ included |
| `seo` | specify, design, review, qa | ✅ included | ✅ included | ✅ included |
| `ux` | specify, design, qa | ✅ included | ✅ included | — correctly excluded |

**Column totals:** design 4/4, qa 5/5, review 8/8 — matching T1's phase matrix exactly, zero omissions,
zero false inclusions. Each cell is derived by applying the *resolved instruction's own rule* (read the
lens's frontmatter, check for the phase name) — not asserted from the table above, which is `lenses/
README.md`'s and each lens file's own declared data restated for legibility, the same source every
resolved instruction now reads.

**Receiving layer — re-confirms plan §2's "verified generic" finding still holds after the edits:**
- `agents/designer.md:61-63` — "when the caller passes **active lenses** for this project... Apply only
  lenses you were actually given; never invent a concern the profile didn't activate." (quoted in full
  at T2)
- `agents/qa-tester.md:174,192-193` — "For each active lens the caller passed... Apply only lenses you
  were given; don't test a concern the profile didn't activate." (quoted in full at T3)
- `agents/reviewer.md:62-64,79` — "when the caller passes active lenses... Apply only the lenses you were
  given." (quoted in full at T4)

None of these three files was edited in this increment (plan §2's "verified generic, no edit needed"),
and none needed to be: each already applies whatever set it receives, so widening what the dispatching
skill computes (T2-T4) is sufficient without a corresponding edit here.

**Folded-in sites (T7, T8) — confirmed to contain no lens-name list:**
- `skills/spark/SKILL.md:64-68` — zero lens names; points at the registry's *Available lenses* table.
- `templates/spec.md:66-72` — zero lens names in the membership sense; the three names present (`seo`,
  `security`, `data`) are inside worked examples of *how* a lens concern becomes an NFR, not a list of
  which lenses exist — confirmed by the immediately preceding clause naming the registry as the current
  set.

**Act phase.** Only `accessibility` declares `act` in its `phases`. No skill in this repo dispatches
lens files at the Act phase — `/increment` (`skills/increment/SKILL.md` step 2) reads `spec.md` §4/§5
unconditionally, with no lens-specific resolution step, per `accessibility-lens`'s own plan (C6) and this
feature's spec (NFR-6: "`/increment` already reads `spec.md` §4/§5 unconditionally... needs no
lens-specific resolution step"). `accessibility`'s Act-phase concern is therefore realized through the
NFR chain — a spec author who follows US-1's revised NFR guidance (T8) writes accessibility NFRs
directly into §5, and `/increment` picks them up the same way it picks up every other NFR, with no
dispatch mechanism to fix here. This is unchanged by this feature and is recorded, not newly discovered.

**Result:** NFR-4 satisfied — zero omissions, zero false inclusions, across both the dispatch layer (T2-
T4, T7, T8) and the receiving layer (unedited, re-confirmed generic).

## T10 — Post-fix negative-case re-run and compatibility statement, 2026-09-17

**Negative case re-run (comparison against T1).** This repo's own `.spark/constitution.md` was not
touched by this increment (only `templates/constitution.md`, the template a *future* `/charter` run
seeds from, was edited) — its active-lens set is still `{library}` exactly as at T1. Applying the
post-fix resolved instructions:

- **design** → `library`'s frontmatter `phases` = `[specify, review]`, no `design` → **∅** (unchanged)
- **qa** → `library`'s `phases` has no `qa` → **∅** (unchanged)
- **review** → `library`'s `phases` includes `review` → **`{library}`** (unchanged)

Identical to T1's pre-fix result in every phase. This confirms the fix changed *how* the set is computed
(rule vs. list) without changing *what* it computes for this repo's own profile — a difference here
would have meant the fix accidentally altered a `library`-only project's dispatch, which would itself
have been a defect (plan §1 T10 DoD).

**`claude plugin validate .` output, run on the working tree post-fix:**
```
Validating marketplace manifest: /Users/andreaslottes/aSPARK/.claude-plugin/marketplace.json

⚠ Found 1 warning:

  ❯ autoUpdate: Unknown field 'autoUpdate'. Claude Code ignores it at load time.

✔ Validation passed with warnings
```
Same single pre-existing, unrelated warning present on every prior release since commit `789e33f`
(`.claude-plugin/marketplace.json` is untouched by this diff — confirmed below).

**Diff-level compatibility assertion (NFR-6).** `git diff --stat` on `feat/lens-dispatch-registry`
against its merge-base with `main` shows exactly 7 files changed: `agents/facilitator.md`,
`skills/demo-day/SKILL.md`, `skills/look-and-feel/SKILL.md`, `skills/peer-review/SKILL.md`,
`skills/spark/SKILL.md`, `templates/constitution.md`, `templates/spec.md` — 39 insertions, 30 deletions,
matching plan §2's Affected Components list exactly, nothing outside it.

- **No slash command name changed** — every file above is either an agent prompt or an existing skill's
  internal step text; no `name:` frontmatter field, no new or removed `/`-command was touched.
- **No protected template heading, column or `NFR-n` ID pattern renamed or removed** — `templates/spec.md`
  is in constitution §3's protected contract set (spec C5); T8's byte-identity check (above) already
  confirmed only its HTML comment changed. `templates/constitution.md` is not in that protected set
  (spec C5) but received the same scrutiny at T6: only its two HTML comments changed.
- **`.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json` are both untouched** by this diff
  (absent from the file list above) — the version bump is `/go-live`'s action, not this increment's;
  `plugin.json` still reads `0.9.0` on this branch.
- **No instantiated consumer's own `.spark/constitution.md` is touched** — this feature edits the
  *template* consumers are seeded from (`templates/constitution.md`) and this plugin's own skills/agents,
  never a downstream project's already-written constitution file. A consumer already carrying the old,
  six-characteristic template comment keeps it until that consumer's own next `/charter` amendment
  (plan §1/R7) — this repo's own `.spark/constitution.md`, checked above, is one such case and is
  correctly unaffected.

**Result:** NFR-5 (negative case holds, disclosure honesty groundwork laid for T11/T12) and NFR-6
(additive-only, no protected structure touched, no consumer file touched) both satisfied.

## T11 — Registry: retire the known-exceptions caveat, close its own drift gap, 2026-09-17

**New text, `lenses/README.md`'s "Adding a lens" §2-4:**
> 2. Give each check a phase owner in the lens's own `phases:` frontmatter field —
>    that field is what every dispatching skill reads to decide who receives the
>    lens file. A missing or misspelled `phases` entry silently drops the lens
>    from every phase it should reach, with no error to surface the mistake.
> 3. Add it to the *Available lenses* table here and, if it binds to a new type
>    or a new characteristic, to the detection-signals tables above and the
>    *Two ways a lens activates* section — these are the lists an author must
>    still update by hand for this file to stay the accurate single source of
>    truth. Three prose copies *outside* this file also name lenses for a human
>    reader and are not sourced from here, so they need the same hand update if
>    you want them to stay accurate: `README.md`'s own lens table,
>    `docs/status.md`, and `docs/workflow.md`.
> 4. Its checks flow automatically: every dispatching skill and the `/charter`
>    activation path now read this file's tables and each lens's own `phases`
>    frontmatter, rather than a closed, named list — a lens with any
>    combination of phases and any new characteristic reaches its agents and
>    becomes declarable at `/charter` with no skill, agent or template edit.
>    See `.spark/lens-dispatch-registry/evidence.md` for the worked proof (all
>    9 shipped lenses, both dispatch and activation) and
>    `.spark/accessibility-lens/evidence.md` for the original finding that
>    prompted the fix.

**"Known exceptions" retired.** Step 4 no longer names `/look-and-feel`, `/demo-day` or the `/charter`
path as needing hand-edits — it states the opposite, that all of them now read this file's tables and
frontmatter generically. This is true as of T2-T9 above, not aspirational: T9's cross-check is the
evidence step 4 now points to.

**Evidence link — kept, not dropped, plus repointed (AC-3.1's either/or, both taken).** The original
`.spark/accessibility-lens/evidence.md` link is kept, retitled as "the original finding that prompted the
fix" rather than "the current account of what is and isn't yet generic" (which would now be false — the
account has changed). A new link to this feature's own `.spark/lens-dispatch-registry/evidence.md` is
added as "the worked proof," so a reader lands on the ledger that is actually current.

**R4 addressed (missing/misspelled `phases`).** Step 2 now states the failure mode explicitly, at the
one place a lens author actually reads before shipping a new lens — this is the mitigation plan §5/R4
specified, not a promise that the failure mode is prevented (it isn't; this repo has no runtime to
validate frontmatter, stated honestly rather than claimed away, consistent with R6).

**R9 addressed (prose copies).** Step 3 now names all three prose copies (`README.md`'s lens table,
`docs/status.md`, `docs/workflow.md`) as lists an author must update by hand — not because they drive any
agent's behavior (they don't; §1's "what still is not generic, by design" already established that), but
because a future lens author following these instructions literally would otherwise miss them and leave
the same kind of staleness T12 finds today.

**Result:** AC-3.1 satisfied.

## T12 — README proof-state row states the closed gap honestly, 2026-09-17

**New text, `README.md:321` (Situational-lenses proof-state row, trailing clause):**
> ... the add-a-file guarantee, refuted for one skill file at the time of this sweep, has since been
> closed across all eight resolved-instruction sites by `lens-dispatch-registry` — see
> `.spark/lens-dispatch-registry/evidence.md`. Two prose lens-count copies (`docs/status.md`,
> `docs/workflow.md`) remain stale as of that feature's own sweep — a separate, named
> documentation-accuracy finding, not a reopened dispatch gap.

**New text, `README.md:340-345` (the situational-lenses sweep's own narrative paragraph):**
> The add-a-file guarantee was refuted for one skill file at the time of this sweep — findings routed
> onward, not fixed here, verify-only by design. That routed finding has since been closed:
> `lens-dispatch-registry` replaced every closed lens-name enumeration this sweep found (and two more of
> the same shape it didn't) with a rule read from `lenses/README.md`'s own registry and each lens's own
> frontmatter, across all eight resolved-instruction sites — see `.spark/lens-dispatch-registry/
> evidence.md` for the worked proof against all 9 shipped lenses. Two prose lens-count copies outside any
> dispatch or activation path (`docs/status.md`, `docs/workflow.md`) remain stale as a separate, named
> documentation-accuracy finding — full ledger in `.spark/situational-lenses/evidence.md`.

Neither passage claims prose accuracy it doesn't have — both explicitly scope the "closed" claim to the
eight resolved-instruction sites (dispatch and activation, US-1/US-2) and separately, honestly, name the
two prose copies still stale, rather than letting the dispatch-gap-closed claim imply prose is covered
too.

**Residual named with `file:line`, routed onward, explicitly not an open dispatch gap:**
- `docs/status.md:34` — the *Scope* row's parenthetical still lists 8 lenses (`seo`, `ux`, `api`, `cli`,
  `library`, `security`, `i18n`, `data`), omitting `accessibility`.
- `docs/workflow.md:40-42` — the "Lenses" bullet's type/characteristic examples still name only the
  original 6 characteristic/type mappings, omitting `accessibility`←`must-be-accessible`.

Both are descriptive prose read by a human, not by any agent deciding what to dispatch (§1's "what still
is not generic, by design" — confirmed unchanged by this increment: neither file is in plan §2's
Affected Components, and neither was edited). `lenses/README.md`'s own "Adding a lens" step 3 (T11) now
tells a future lens author to update both by hand; this ledger records that today's count (8, not 9) is
itself already stale, independent of any future lens — a pre-existing documentation defect this feature
found but does not fix, per its own out-of-scope boundary (spec §6: "this feature touches only how any
lens gets discovered, activated and dispatched," not every prose count of lenses in the repo).

**Result:** AC-3.2 satisfied — the gap is stated closed where it is closed, and the one honest residual
is named with `file:line` and routed, not glossed over or silently folded into the "closed" claim.

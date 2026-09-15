# Evidence: accessibility-lens

| | |
|---|---|
| Feature | accessibility-lens |
| Phase | Act |
| Date | 2026-09-15 |

## T2 — Negative case first (constitution §1), 2026-09-15

**Counting domain.** Ceremony-emitted output and produced artifacts (spec NFRs, review findings, QA
checks). Loaded file contents are excluded from the count — the lens file itself existing and being read
is not a "check"; a check is something a ceremony writes down or acts on.

**This repo's own profile.** `.spark/constitution.md` §2: **Project type(s):** `library`. **Characteristics:**
none of the six (`handles-auth`, `is-public`, `handles-payments`, `handles-pii`, `has-database`,
`is-multilingual`). `must-be-accessible` is not among the six characteristics the constitution's *Project
Profile & Active Lenses* section declares, and it is not declared anywhere else in the file.

**Active-lens table.** §2's *Active lenses* table lists exactly one row: `library` — Active. `accessibility`
does not appear as a row, active or off, because it is not yet registered in `lenses/README.md`'s
Characteristics detection-signals table at this point in the build (that registration is T5, after this
negative-case check) — so at T2 the lens cannot be activated by any mechanism, mechanically as well as by
declaration.

**Result.** Zero: this repo's own `.spark/` (spec.md/plan.md/evidence.md/review.md/qa.md across every
shipped feature) contains no accessibility `NFR-n`, no accessibility finding, and no accessibility QA row
attributable to this lens — because the characteristic that would activate it is absent, not because
nobody looked. The zero is recorded *because* `must-be-accessible` is absent from the profile, which is
the reason constitution §1's "nothing may change" holds here, not bare silence.

**Re-run planned at T9** after the registry rows (T5) exist, to confirm registration alone does not
activate the lens absent a constitution declaration (NFR-3: no silent activation).

## T7 — Dispatch refutation, recorded and routed, 2026-09-15

**Verdict: `refuted-with-finding` against NFR-6** ("every concern raised in Specify has a downstream
owner"). The lens's own text is complete and correctly scoped (US-2, verified T3/T4), but two of its five
phase rows will never be *dispatched* to the agent that owns them, because the ceremony skills that select
which lens files to pass carry closed enumerations rather than reading the constitution's active-lens list
generically.

**Design (AC-2.2) — undispatched.** `skills/look-and-feel/SKILL.md:34-35`:

> "the design-relevant ones are `ux`, `seo` (content structure) and `i18n` (text expansion, RTL) — pass
> those paths in step 4"

This is a closed, named list. `accessibility` is not in it and never will be without an edit here — even on
a project that correctly declares `must-be-accessible` in its constitution, `/look-and-feel` will not pass
`lenses/accessibility.md` to the Designer, so AC-2.2's Design-phase check never reaches the agent that owns
it.

**QA (AC-2.5) — undispatched.** `skills/demo-day/SKILL.md:84`:

> "`${CLAUDE_PLUGIN_ROOT}/lenses/` — `ux.md`, `seo.md`, `security.md`, `i18n.md`"

Same defect, same shape. This one is **not new** — `.spark/situational-lenses/evidence.md` Entry 3 already
found and refuted it, predicting verbatim: "adding a 9th lens with new QA-phase coverage would require
editing it." `accessibility` is that 9th lens, and the prediction is now confirmed live rather than
hypothetical.

**Dispatch verified by reading — Specify and Act clean, Review downgraded (F6):**
- **Specify** — `skills/story-time/SKILL.md:41` passes lens paths generically (`{active-lens-name}.md`),
  no closed list. `accessibility` reaches the Product Owner correctly.
- **Act** — `skills/increment/SKILL.md:27-29` reads `spec.md` §4/§5 (ACs/NFRs) unconditionally; it never
  resolves lens files at all, so there is no enumeration to be stale (plan §1, C6/R5). AC-2.3 is realized
  through the NFR chain, not a dispatch step.
- **Review — lower-confidence ✅, revised at `/peer-review` round 1 (F6).** `skills/peer-review/SKILL.md:50-51`
  reads verbatim: "`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md` for any of `seo`, `api`, `cli`, `library`,
  `security`, `data`, `i18n` that are active." The head clause (`<name>.md`, generic) and the parenthetical
  (seven literal names, closed) are grammatically near-identical in shape to `demo-day:84`'s confirmed
  defect — only the object form differs (a placeholder with a restrictive list, vs. four bare filenames).
  Originally recorded here as a clean dispatch pass with the closed list dismissed as a cosmetic staleness
  Nit; round-1 review judged that too confident — the same reword proposed for `look-and-feel`/`demo-day`
  (the computed-set form) applies here too, since a literal reading of the parenthetical could exclude
  `accessibility` the same way the other two do. Downgraded from "no finding" to **grouped with F1's four
  sites** for the routed fix, not left as a standalone clean pass.

**Consequence, stated plainly.** A project that correctly declares `must-be-accessible` gets a lens that
grounds an NFR at Specify and is reachable at Review's generic placeholder — but the Designer never sees
`lenses/accessibility.md` at `/look-and-feel`, and the QA Tester never sees it at `/demo-day`, unless a
human manually passes the file. The lens looks complete; two of its five rows silently do not fire. This is
worse than an absent lens, because nothing signals the gap to the user in the moment.

**Fix, written out, not applied here (per the plan-gate ruling, Q2 — routed, not fixed in this diff):**
reword both closed lists to the computed-set form `skills/peer-review/SKILL.md:50-51` already uses — "for
any active lens whose `phases` frontmatter includes `design`" / "…includes `qa`" — which would make this
and every future lens dispatch correctly without another skill edit. Rejected as this feature's own scope
because it repairs the loop's dispatch layer for every lens, not just this one, and folding it in here would
turn a 5-file diff into a 7-file one for a concern with its own venue. **Routed to a follow-up increment.**

**Prior art.** `.spark/situational-lenses/evidence.md` Entry 3 (the `demo-day:84` half of this finding, and
its own `CLAUDE.md`-cited routing precedent for `refuted-with-finding`).

**Extended at `/peer-review` round 1 (F1): the same defect exists one layer up, at *activation*, not
just dispatch.** T7 above audited only which lens files get passed to agents once a lens is active — never
how `must-be-accessible` gets **into** a constitution in the first place. Two more sites carry the same
closed-enumeration shape:

- `agents/facilitator.md:51-52` — "activate concern lenses: `handles-auth`, `is-public`, `handles-payments`,
  `handles-pii`, `has-database`, `is-multilingual`" — six characteristics, closed, `must-be-accessible` not
  among them.
- `agents/facilitator.md:67-69` — "characteristics activate `security`←`handles-auth`/`is-public`/
  `handles-payments`/`handles-pii`, `i18n`←`is-multilingual`, `data`←`has-database`" — the mapping itself
  stops at three lenses.
- `templates/constitution.md:34-35` — the constitution template every new aSPARK project instantiates ships
  `<!-- any of: handles-auth · is-public · handles-payments · handles-pii · has-database · is-multilingual
  -->` — the same six, closed, shipped to every consumer.

**Consequence.** The constitution is the only place a lens is switched on (`lenses/README.md` "How a lens
gets activated" step 1) and `/charter` is its only writer. As shipped, `must-be-accessible` is not a
characteristic any `/charter` run proposes, and not one the constitution template even hints exists — so
the lens is not merely undispatched at two phases (T7), it is **unreachable by the ordinary path** a user
would take to declare it. Not a Blocker: `agents/facilitator.md:46-47` does point the Facilitator at
`lenses/README.md`'s own detection tables, which (after T5) do carry the `must-be-accessible` row — so a
Facilitator who reads the lens README directly still finds it. But the closed lists at `:51-52`, `:67-69` and
the template are the literal instruction, and they are wrong.

**Verdict revised: `refuted-with-finding` against NFR-6, now at five sites, not two** —
`skills/look-and-feel/SKILL.md:34-35`, `skills/demo-day/SKILL.md:84` (T7, original), `agents/facilitator.md:51-52,67-69`
and `templates/constitution.md:34-35` (this extension, F1), plus `skills/peer-review/SKILL.md:50-51`
(downgraded from clean pass to the same group, F6). **Routed to the same follow-up increment** — the fix
shape is the same in kind (closed enumeration → generic/registry-driven form), even though the mechanism
differs (skill dispatch vs. agent-authored constitution content vs. a shipped template comment), so one
increment can reasonably address all five together.

## T9 — Fence audit, negative-case re-run, AC-1.4 verdict, 2026-09-15

**Diff-scope sweep** (`git status --porcelain` on branch `docs/accessibility-lens`, cut from `main` at
`2846739`):

```
 M README.md
 M lenses/README.md
 M lenses/seo.md
 M lenses/ux.md
?? .spark/accessibility-lens/
?? lenses/accessibility.md
```

Plus the pre-existing, out-of-scope `.spark/.guard/` (the `aspark-guard` plugin's own ledger, unrelated to
this feature — same untracked artifact noted in `companion-offer`'s own evidence trail). Protected-path
check: `git diff --name-only main -- skills/ agents/ templates/ .claude-plugin/` → **empty**. No agent, no
skill, no template, no manifest touched.

**Lens count.** `ls lenses/*.md | wc -l` → **10** (9 lenses + `README.md`), up from 9 before this feature.

**Negative case, re-run after registration (T5) landed.** `grep -n "must-be-accessible"
.spark/constitution.md` → no match. The characteristic is registered as a *detectable signal* in
`lenses/README.md` now, but the constitution — the single source of truth for activation (constitution §2,
`lenses/README.md` "How a lens gets activated" step 1) — still does not declare it. Registration alone does
not activate the lens; NFR-3 (no silent activation) holds after T5 exactly as it held before it.

**AC-1.4 verdict — two clauses, ruled separately per Q1:**
- *"no agent or skill file is edited"* — **confirmed.** Verified above; zero hits under `skills/`,
  `agents/`.
- *"touches only [4 named files]"* — **refuted-with-finding, ruled at the plan gate (Q1).** The actual diff
  touches 5 tracked files plus 2 new paths: `README.md` was added deliberately, because constitution §4's
  docs-in-step bar outranks this AC's literal file list once a user-facing lens table and an "add-a-file
  refuted for one file" claim both existed in `README.md` already. Not a defect — a recorded, ruled
  supersession, not a silent scope-creep.

**Constitution's own "8 lenses" count** (`.spark/constitution.md:16`, unverified exact line by this feature
— routed, not read in full here) is now stale with the 9th lens shipping. **Not corrected in this diff**
(Q3) — routed to `/charter`, alongside the minor version bump this feature triggers at `/go-live`
(constitution §5).

**`claude plugin validate .`** (repo root): `✔ Validation passed with warnings` — one pre-existing
`autoUpdate` warning on `marketplace.json`, untouched by this diff, out of scope.

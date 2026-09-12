# Evidence: situational-lenses

| | |
|---|---|
| **Phase** | Act (`/increment`) |
| **Owner** | Developer (the orchestrating session) |
| **Status** | `complete` |
| **Date** | 2026-09-12 |

**Handoff**
- **Status:** `complete` — all 13 tasks done, 12 entries written task by task as each completed. Entries are append-only; a superseded number is struck through in place, never deleted.
- **Summary:** Verify-only sweep. No `lenses/`, `agents/`, `skills/` or `templates/` file was touched — every entry is either (a) a read-only audit of this repo's own lens artifacts, (b) a live ceremony run in a disposable scratch venue outside every real repo, or (c) field evidence read from an already-completed loop's own artifacts in a profiled project. Class labelled on every row. **Consolidated verdicts: Entry 11.** 21 `confirmed`, 5 `refuted-with-finding`, 3 `not-verified-live`, 2 `N/A` — 31 of 31 spec IDs covered, none double-verdicted, counted programmatically.
- **Open:** `none` for this feature's own tasks. Five findings routed onward, none fixed here (verify-only fence): AC-3.3 (Entry 7, a `library`/`cli`-attributed QA-phase gap, found in three of four surveyed projects), AC-5.2 (Entry 3, `demo-day`'s closed lens enumeration), NFR-4 (Entry 3, the spec's own stale skill count), NFR-6 (same), NFR-9 (Entry 2, four lenses missing the cite-once instruction). Plus one field observation outside this feature's fence entirely (Entry 10, a pre-profile Blocker with no upstream NFR to have caught it) and one venue that never existed to test the mechanism at all (Entry 7, an active-lens project with no feature postdating its own profile — `not-verified-live`, not a realized risk). **Corrected at `/peer-review` round 3 (F15, Major): this line previously described the AC-3.3 finding and the Entry 7 gap using verdicts the body below had already superseded (Entry 11's own consolidated table, `refuted-with-finding` and `not-verified-live` respectively) — the deliverable was disagreeing with itself.**
- **Binding ruling:** Entry 11's consolidated tables are the authoritative verdict per spec ID; `plan.md` §3 wins on task status only. No committed row carries a verbatim **sentence**, file path, project name or feature name from a non-public repo (short category-label fragments are a named, narrower exception — Privacy rule, above) — audited directly at Entry 12, re-audited at round 3 (F12) after a leak the original audit's narrower pattern missed.
- **On conflict:** `plan.md` §1 wins on architecture; this file wins on what was observed.

## Verdict vocabulary (fixed, five values — plan.md §1)

| Verdict | Means |
|---|---|
| `confirmed (audit)` | Demonstrated by a quoted read-only command against this repo's own, public files. |
| `confirmed (performed)` | Demonstrated by a ceremony invoked live, in this task, in a disposable scratch venue. |
| `confirmed (field)` | Demonstrated by an already-completed loop's own artifacts in a profiled project — the ceremony that produced them was performed, just not in this session. |
| `refuted-with-finding` | The claim does not hold against the evidence gathered; the finding is named and routed to a later increment, never fixed here (verify-only fence). |
| `not-verified-live (venue named)` | No accessible venue exists to test the claim as literally written; the missing venue is named, and no substitute is presented as satisfying the literal claim. |

## Evidence classes (plan.md §1)

1. **Artifact audit** — this repo's own `lenses/`, `lenses/README.md`, and the skills'/agents' lens-passing form. Public, quotable verbatim. Reproduction = re-run the quoted command.
2. **Performed run** — a ceremony invoked live, in a disposable scratch venue created, used, recorded and discarded outside every real repo. The only ceremony invocations in this feature.
3. **Field evidence** — the artifacts of a loop that already ran, in a project whose `.spark/constitution.md` declares a profile. The *output* of a performed ceremony, not a thought experiment — but never relabelled as a "performed run" (class 2), since the invocation did not happen in this session.

## Privacy rule (binding, ruled before the first external row — plan.md §1, R-A)

Surveyed projects beyond this repo appear **only** as opaque ids: `P1`, `P2`, `P3`. This repo is `P-SELF`. The ledger records lens names, phase names, `AC-n.m`/`NFR-n` shapes, **short category-label fragments** (e.g. *"Accessibility / UX (lens)"* — a handful of words naming how a row is categorized, never a full sentence), counts and verdicts — and **zero** verbatim sentences, file paths, project names or feature names from any non-public repo. The id↔project map exists only in an untracked scratch note (session scratchpad), never committed, never referenced by path in this file. Same trade as this repo's own `docs/reports/README.md`: *"Opaque ids and counts. No project name, no feature name, no hostname, no path."*

Denylist (audited at T12, and re-auditable by anyone at any time): the three surveyed projects' names, any absolute path under a surveyed project's own filesystem location, any non-public feature name, any verbatim sentence from a non-public repo's artifact. **Corrected at `/peer-review` round 4 (F19, Minor): this section previously banned "verbatim text" in the same breath as permitting "category labels," which are themselves verbatim text — the denylist's own narrower wording ("verbatim sentence") is the operative rule and the one this file's audits actually check against; restated above to match.**

---

## Entry 1 — T1, walking skeleton: one complete row, this repo, before scaling out

**Class:** 1 (artifact audit). **Project:** `P-SELF` (this repo — public, quotable).

### Claim under test

Does this repo's own feature history raise any lens-attributed SEO or UX NFR? `P-SELF`'s constitution declares type `library`, one lens active (`library`), `seo`/`ux` both off — per NFR-5 ("a lens contributes zero checks on a profile that does not activate it") and the spec's own AC-6.1 suppression claim, the expected answer is zero.

### Counting method, stated before the count

A row counts **only** if its NFR table's Category column attributes it to a named lens in parenthetical or italic form — the pattern every feature in this repo already uses for the `library` lens (e.g. `"Public surface (library lens §1)"`, `"Compatibility & versioning (library lens §2)"`). A row does **not** count if it is one of the template's **standing** NFR categories that exists independent of any lens — `Accessibility`, `Accessibility / performance`, `Performance`, `Security & privacy` appear in several features' tables with no lens attribution at all, usually marked `N/A` for a reason stated in the row itself (no UI, no PII, no network surface). Conflating a standing N/A row with a lens-suppression success would inflate the suppression count falsely (plan.md R-E) — so every row below is read for its literal attribution, not its topic.

### Command and output

```
$ ls .spark/ | grep -v constitution.md
graph-gates
graph-gates-verification
handbook-maturity
lean-artifacts
lean-rounds
right-sizing
situational-lenses
tracker-handoff
```

Eight feature directories; `situational-lenses` excluded from the count below (it is this feature's own spec, describing the `seo`/`ux` lenses as subject matter — not a feature *using* them, and counting it would be circular).

```
$ for f in graph-gates graph-gates-verification handbook-maturity lean-artifacts \
           lean-rounds right-sizing tracker-handoff; do
    grep -nE '^\| NFR-[0-9]+ \|' ".spark/$f/spec.md"
  done
```

Full output (7 features, every NFR row's Category column):

| Feature | NFR rows, Category column |
|---|---|
| `graph-gates` | Compatibility/versioning *(library lens §2)* · Public surface *(library lens §1)* · Contract clarity *(library lens §4)* · Packaging & footprint *(library lens §3)* · Reliability *(constitution §6)* · Soundness of offered answers · Safety *(constitution §6)* · Traceability *(constitution §4)* · Docs in step *(constitution §4, §1)* · Evidence bar *(constitution §4)* · Agent attention · **Accessibility / performance** · Security & privacy |
| `graph-gates-verification` | Footprint *(library §1)* · Compatibility *(library §2)* · Contract clarity *(library §4)* · Evidence bar *(constitution §1, §4)* · Countability · Safety *(constitution §6)* · Reliability/scale · **Accessibility** · Observability/honesty *(constitution §1)* |
| `handbook-maturity` | Contract clarity *(lens §4)* · Compatibility/versioning *(lens §2)* · Public-surface restraint *(lens §1)* · Reliability/reviewability · Performance · Security & privacy · Observability/ops |
| `lean-artifacts` | Compatibility & versioning *(library lens §2)* · Public surface *(library lens §1)* · Contract clarity *(library lens §4)* · Agent attention *(constitution §4)* · Reliability *(constitution §6)* |
| `lean-rounds` | Compatibility & versioning *(library lens §2)* · Contract clarity *(library lens §4)* · Public surface *(library lens §1)* · Agent attention/honesty *(constitution §4)* · Reliability *(constitution §6)* |
| `right-sizing` | Compatibility & versioning *(library lens §2)* · Public surface *(library lens §1)* · Contract clarity *(library lens §4)* · Degrade to silence *(constitution §6)* · Honesty of claim *(constitution §4)* · Gate integrity *(constitution §6)* |
| `tracker-handoff` | Compatibility/versioning *(library lens §2)* · Backward compatibility *(constitution §4)* · Public surface *(library lens §1)* · Contract clarity *(library lens §4)* · Reliability *(constitution §6, adapted)* · Evidence bar *(constitution §4)* · Docs in step *(constitution §4)* · Agent attention *(constitution §4)* · Traceability *(constitution §4)* · **Security & privacy** · **Accessibility / performance** |

```
$ grep -rn '(seo lens\|(ux lens\|seo §\|ux §\|lens §.*seo\|lens §.*ux' .spark/*/spec.md | grep -v situational-lenses
```
(no output — zero hits)

### Number and verdict

**0 lens-attributed SEO NFRs. 0 lens-attributed UX NFRs**, across all ~~43~~ **56** NFR rows in this repo's 7 other features — corrected at `/peer-review` round 1 (F7, Minor): `for f in <the 7 features>; do grep -cE '^\| NFR-[0-9]+ \|' "$f"; done` summed to 56, not 43; the conclusion is unaffected, the denominator was simply miscounted when first written. Every attributed row names the `library` lens (the repo's one active lens, load 1) or a constitution section; the bolded rows above (`Accessibility`, `Accessibility / performance`, `Security & privacy`) are standing template categories, not lens-attributed, and several are marked `N/A` in their own row for a stated reason (no UI, no network/auth surface) — excluded from the count per the stated method, not folded in as zeros that would double-count the same fact.

**Verdict: `confirmed (audit)`** — AC-6.1's suppression claim holds for `P-SELF` on its own terms: a `library`-only, load-1 profile raises no SEO or UX NFR anywhere in its seven other features' history. This is the suppression leg's cheapest positive instance; T7 adds the corresponding positive control (a project whose profile *does* activate a UI lens) before this can be called selective rather than merely quiet.

### Ledger machinery exercised once, before scaling

This entry used every piece of the method this feature will run eleven more times: the verdict vocabulary (above), the evidence-class label, a stated counting method written *before* the count (not fitted after), a quoted reproducible command, and a verdict distinguishing `confirmed` from the weaker claim "nothing was looked at." Nothing here needed the privacy rule — `P-SELF` is this repo, already public — so the rule's first real test is `P1`–`P3` at T6.

---

## Entry 2 — T2, the eight lens files against their own contract

**Class:** 1 (artifact audit). **Project:** `P-SELF`.

### Frontmatter (AC-3.1, NFR-1)

```
$ for f in lenses/*.md; do [ "$(basename $f)" = README.md ] && continue
    echo "--- $f"; sed -n '1,6p' "$f" | grep -E '^name|^applies-to|^triggers|^phases'; done
```

| Lens | `name` | `applies-to` | `triggers` | `phases` |
|---|---|---|---|---|
| `api` | ✅ | `[api]` | — | `[specify, review]` |
| `cli` | ✅ | `[cli]` | — | `[specify, review]` |
| `data` | ✅ | — | `[has-database]` | `[specify, review]` |
| `i18n` | ✅ | — | `[is-multilingual]` | `[specify, design, review, qa]` |
| `library` | ✅ | `[library]` | — | `[specify, review]` |
| `security` | ✅ | — | `[handles-auth, is-public, handles-payments, handles-pii]` | `[specify, review, qa]` |
| `seo` | ✅ | `[website]` | — | `[specify, design, review, qa]` |
| `ux` | ✅ | `[web-app, website]` | — | `[specify, design, qa]` |

All 8 carry `name` and exactly one of `applies-to`/`triggers` — none carries both, none carries neither.

### Checks owned by a phase absent from the lens's own `phases` (AC-3.1, NFR-2) — read in full, not grepped

Every checklist section's stated owner phase(s), checked against that file's frontmatter `phases:` list:

| Lens | Checklist sections' stated phase(s) | All present in frontmatter? |
|---|---|---|
| `api` | Review ×4 | ✅ |
| `cli` | Review ×4 | ✅ |
| `data` | Review ×4 | ✅ |
| `i18n` | Review, Review+QA, Design+QA, Review/Design | ✅ (design, review, qa all listed) |
| `library` | Review ×4 | ✅ |
| `security` | QA-observable/set-in-Review, Review ×3, Review+QA | ✅ (review, qa both listed) |
| `seo` | Review ×3, Review+QA ×2, Design+Review, QA | ✅ (design, review, qa all listed) |
| `ux` | Design+QA ×5 | ✅ (design, qa listed; **no "Review" row anywhere** — consistent with `phases` carrying no `review`, and `ux.md` says so explicitly: *"No Review row: UX is judged from the running product and the spec, not from reading the diff"*) |

**Count of mismatches: 0.** No exception to quote.

### Per-phase owner map present (AC-3.1)

```
$ grep -lc '## Who owns what' lenses/*.md | grep -v README
lenses/api.md:1
lenses/cli.md:1
lenses/data.md:1
lenses/i18n.md:1
lenses/library.md:1
lenses/security.md:1
lenses/seo.md:1
lenses/ux.md:1
```

8 of 8.

### "Cite each finding once" instruction present (NFR-9) — **refuted-with-finding**

NFR-9's own worked example names *"security vs Reviewer baseline"* as the overlap this instruction exists to prevent. Checked for the literal instruction, not just the general idea of not repeating a baseline:

```
$ grep -n 'cite' lenses/api.md lenses/data.md lenses/seo.md lenses/ux.md
lenses/api.md:62:  header/authz depth complements this lens — cite each finding once.
lenses/seo.md:54:- [ ] Content images have descriptive `alt` text (this doubles as the accessibility check — cite it once, not twice).
lenses/seo.md:76:  your accessibility checks by design; cite each finding once.
lenses/data.md:18:retention and deletion — cite each finding once.
lenses/data.md:44:- [ ] No N+1 query pattern (cite the Reviewer's baseline once — don't repeat it as a separate finding); list endpoints are bounded/paginated.
lenses/ux.md:59:- [ ] Interactive elements have visible hover, focus and active states (this doubles as the keyboard-accessibility check — cite once).
$ grep -c 'cite' lenses/cli.md lenses/i18n.md lenses/library.md lenses/security.md
lenses/cli.md:0
lenses/i18n.md:0
lenses/library.md:0
lenses/security.md:0
```

**4 of 8 lenses carry the instruction** (`api`, `data`, `seo`, `ux`), each at a real, named overlap point. **4 of 8 do not** (`cli`, `i18n`, `library`, `security`) — and `security.md` is the gap that matters: it is the lens NFR-9 cites by name, and its own prose *describes* the non-overlap conceptually (`security.md:16-18`: *"This lens adds the depth beyond that baseline... It does not repeat the baseline; it deepens it"*) but never actually instructs the phase-owning agent to **cite a finding once** if the same issue is flagged by both the Reviewer's baseline security hunt and this lens's hardening checklist — e.g. a missing authz check (security lens §3) is also squarely inside "the security basics on every diff (injection, secrets, authorization)" the lens's own opening paragraph says the Reviewer already hunts. `cli.md`, `i18n.md` and `library.md` have no comparably obvious overlap named anywhere in this repo's other lenses, so their gap is lower-stakes, but NFR-9 as written ("**every** lens file instructs...") does not carve out an exception for a lens with no obvious overlap partner — it states the rule for all of them.

**Verdict: `refuted-with-finding`.** NFR-9's literal claim — *every* lens file instructs "cite each finding once" — does not hold: 4 of 8 lenses carry no such instruction, and the one with a named, concrete overlap risk (`security` vs. the Reviewer's baseline) is among them. **Finding, routed to a later increment** (this is a verify-only feature; no lens file is edited here): add a one-line "cite once" instruction to `lenses/security.md` (the Reviewer's authorization/secrets/injection baseline vs. this lens's deeper authz-matrix/supply-chain/PII checks are the concrete overlap points — §3 "Authorization" and §4 "Input, output & supply chain" are the most likely double-report sites) and consider the same for `cli.md`, `i18n.md` and `library.md` for consistency with NFR-9's literal "every" even though no overlap partner was found for them in this repo's own lens set.

### Non-falsifiable checks (no location/signal or no concrete fix) — NFR-1

Read every checklist item in all 8 files (not grepped — "no concrete fix" isn't a regex). Every item names a concrete signal (a file, a header, a status code, a measurable bar, an observable browser state) and implies or states its fix. **Count: 0.** No item reads as a vague taste judgment in the shape the spec calls out as the failure mode ("no 'make it SEO-friendly'").

### `lenses/README.md` (AC-5.1, AC-7.1, AC-7.2)

Documents, verbatim in the file: all three frontmatter keys (`name`, `applies-to`/`triggers`, `phases` — `README.md:53-54`), the per-phase map requirement (`:55-57`), the falsifiable-checks-only bar with the same "location, rule, fix" wording the spec itself uses (`:58-60`), and "the lens flags, never invents scope" (`:61-63`). The *Available lenses* table (`:95-104`) lists all 8 by name with activation and summary. Detection signals (`:74-91`) cover all 5 types and all 6 characteristics that trigger a lens. **AC-5.1, AC-7.1, AC-7.2: `confirmed (audit)`.**

---

## Entry 3 — T3, add-a-file: is a lens picked up without editing a role?

**Class:** 1 (artifact audit). **Project:** `P-SELF`.

### Every lens reference in a skill or agent (AC-5.2, NFR-6)

```
$ grep -rn 'CLAUDE_PLUGIN_ROOT.*lenses\|lenses/\${' skills/ agents/
skills/look-and-feel/SKILL.md:42:   lenses (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`). In Mode A it fills the
skills/demo-day/SKILL.md:84:   `${CLAUDE_PLUGIN_ROOT}/lenses/` — `ux.md`, `seo.md`, `security.md`, `i18n.md`).
agents/facilitator.md:47:   (the detection tables in `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`): its
skills/spark/SKILL.md:64:   `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`), name the likely type(s)/
skills/peer-review/SKILL.md:50:   constitution's profile — `${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md` for any of
skills/story-time/SKILL.md:31:   `${CLAUDE_PLUGIN_ROOT}/lenses/README.md`), name the likely type(s) in one line
skills/story-time/SKILL.md:41:   Pass the paths of any active lenses (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`)
```

~~5 of 6~~ **6 of 7** references resolve generically or point at the README rather than an individual lens — corrected at `/peer-review` round 1 (F7, Minor): the quoted grep above prints 7 lines, not 6. By the `<name>.md` placeholder pattern: `look-and-feel:42`, `peer-review:50`, `story-time:41` pass any active lens's path built from its name, read off the constitution — adding a 9th lens changes nothing here. `spark:64`, `story-time:31` and `agents/facilitator.md:47` point at `lenses/README.md` for detection, not at an individual lens file. That's 6; the 7th is the one exception named next.

**One does not: `skills/demo-day/SKILL.md:84`.** Read in full context (`:79-84`):

> *"the paths of any active lenses with browser-observable checks (from the constitution's profile — `${CLAUDE_PLUGIN_ROOT}/lenses/` — `ux.md`, `seo.md`, `security.md`, `i18n.md`)."*

The stated **selection criterion** is a property — "browser-observable checks" — which is generic and correct. But unlike `peer-review:50-51`'s equivalent instruction (*"the paths of any active lenses with review-phase checks... `${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md` **for any of** `seo`, `api`, `cli`, `library`, `security`, `data`, `i18n` that are active"*), which keeps the generic `<name>.md` placeholder and only *parenthetically lists which lenses currently qualify*, `demo-day:84` drops the placeholder entirely and writes the four qualifying lens filenames as the object of the instruction — `ux.md`, `seo.md`, `security.md`, `i18n.md` **are** the instruction, not an illustration of one.

**Cross-checked against T2's own frontmatter audit (Entry 2):** the four named are exactly the four lenses whose `phases:` include `qa` today (`security`, `seo`, `ux`, `i18n` — confirmed) and the four omitted (`api`, `cli`, `library`, `data`) are exactly the four without `qa` in `phases`. So the list is **accurate today** — this is not a correctness bug against the current 8 lenses. It is a **closed enumeration** in the sense AC-5.2/NFR-6 test for: if a 9th lens shipped tomorrow with `qa` in its `phases` frontmatter, `demo-day:84`'s literal text would still name only the original four, and picking up the new one would require **editing this skill file** — unless whoever reads it correctly treats the four names as illustrative of "browser-observable checks" rather than as the exhaustive set, which the instruction's own wording does not make unambiguous (contrast `peer-review:50`'s "**for any of**" framing, which reads unambiguously as *current membership of a computed set*, not as the set's definition).

**Verdict: `refuted-with-finding`.** AC-5.2 ("picked up without editing any agent or skill file") and NFR-6 ("adding a lens requires edits only within `lenses/`... no agent or skill file changes") do not hold as literally written for `skills/demo-day/SKILL.md:84` specifically — every other lens-passing instruction in this repo uses the generic `<name>.md` placeholder form and this one does not. **Finding, routed to a later increment** (no skill file is edited here — verify-only fence): reword `demo-day:84` to match `peer-review:50`'s pattern — `${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md` **for any of** `security`, `seo`, `ux`, `i18n` **that are active and carry `qa` in their `phases`** (or equivalent), so the set is stated as computed from the lens files' own frontmatter rather than memorized as four names that will silently stop being exhaustive the day a 9th lens adds a `qa` row.

### Agent/skill counts today, against NFR-4's stated baseline

```
$ ls agents/*.md | wc -l
7
$ ls skills/ | wc -l
10
```

NFR-4 states *"count remains 7 agents / 8 skills."* Agents: **7 — unchanged, `confirmed (audit)`.** Skills: **10, not 8** — a +2 drift from NFR-4's baseline. Attributed by name, not attributed to this feature:

```
$ for s in skills/*/SKILL.md; do
    echo "$(git log --follow --diff-filter=A --format='%ad' --date=short -- "$s" | tail -1)  $s"
  done | sort
2026-07-13  skills/demo-day/SKILL.md
2026-07-13  skills/go-live/SKILL.md
2026-07-13  skills/increment/SKILL.md
2026-07-13  skills/look-and-feel/SKILL.md
2026-07-13  skills/peer-review/SKILL.md
2026-07-13  skills/spark/SKILL.md
2026-07-13  skills/sprint-plan/SKILL.md
2026-07-13  skills/story-time/SKILL.md
2026-07-14  skills/charter/SKILL.md
2026-07-17  skills/next-steps/SKILL.md
```

Eight skills (2026-07-13) plus `charter` (2026-07-14) plus `next-steps` (2026-07-17) — both added by later, named ceremonies (the constitution/`/charter` feature and the `/next-steps` product-owner ceremony), neither by `situational-lenses`, whose own commit (`4c780f6`) and spec clarify date (2026-07-15) predate `next-steps` entirely. **This feature's own claim is "zero new roles added by this feature,"** assessed against `4c780f6`'s own commit range, not against NFR-4's now-stale absolute count — and that narrower claim holds: neither `4c780f6` nor this verify-only sweep adds or removes an agent or skill file. NFR-4's literal "8 skills" is stale and would read as a violation if taken at face value; **flagged as a separate, smaller finding** — the number should be corrected at a future `/charter`-adjacent pass, not silently left to mislead the next reader of this spec.

---

## Entry 4 — T4, the negative case: no constitution, nudge only (live)

**Class:** 2 (performed run). **Venue:** disposable scratch directory in the session scratchpad, `git init`'d, outside every real repo — not this repo, not any of `P1`–`P3`. Discarded after this entry is written.

### Venue setup

```
$ mkdir sl-t4-no-constitution && cd sl-t4-no-constitution && git init -q
$ cat package.json
{
  "name": "scratch-webapp",
  "version": "0.1.0",
  "scripts": { "dev": "vite" },
  "dependencies": { "react": "^18.0.0", "react-router-dom": "^6.0.0" }
}
$ find . -type f
package.json
src/routes/Dashboard.jsx
```

Signals: Vite + React SPA, a dashboard-style route, no SSR framework, no `robots.txt`/`sitemap.xml`. Matches `lenses/README.md`'s own `web-app` row ("SPA (Vite/CRA React·Vue·Svelte without SSR), routes behind auth, dashboard/tool UI"), deliberately chosen so the nudge has a real type to name rather than defaulting to "unclear." No `.spark/` anywhere in the venue.

### The check `skills/story-time/SKILL.md` step 2 specifies, performed literally

```
$ test -f .spark/constitution.md && echo EXISTS || echo ABSENT
ABSENT — nudge-only branch applies
```

Step 2's text, quoted: *"If there's no constitution, do not resolve or apply lenses for this run — only give a lightweight nudge: glance at the repo..., name the likely type(s) in one line..., and point the user to `/charter`... No lens is applied off a fallback guess."*

### Before-state (file inventory, for the after-diff)

```
$ find . -type f | sort   # excluding .git
package.json
src/routes/Dashboard.jsx
```

### The nudge, performed once, exactly as the step specifies and no further

> *"this looks like a `web-app` (Vite + React SPA, dashboard-style route, no SSR/indexing signal) — a `ux` lens would apply. Run `/charter` to record the profile so it activates for every phase."*

One line. Names a type (`web-app`). Names the lens that *would* apply, in the step's own template phrasing ("e.g. 'this looks like a public `website` — an `seo` lens would apply'") — stopping at naming, not opening `lenses/ux.md` and applying its checklist. Points to `/charter`.

### After-state and the counting domain

```
$ find . -type f | sort   # same command, after the nudge
package.json
src/routes/Dashboard.jsx
$ diff <(before) <(after)
(empty)
```

**Counting domain, stated:** what is counted is the ceremony-emitted output (the nudge text itself) and any artifact the venue gains as a result of this step running — not the contents of files this operator read while deciding what to glance at (`lenses/README.md`'s detection table, read in T2 and again here, is input to the nudge, not output of it, and loading it is not the same as resolving or applying a lens's checklist).

- **Nudges emitted: exactly 1.** Not zero (a nudge is required), not two (no second pass, no re-detection).
- **Lens checklists resolved or applied: 0.** No lens file's checklist items were opened against this venue's code; the nudge names a lens by type-match only.
- **Lens-attributed NFRs written: 0.** No `spec.md`, no NFR of any kind — the venue has no `.spark/` directory after this step, same as before.
- **Files created outside the venue: 0** (nothing written anywhere but this ledger, which lives in `P-SELF`'s own repo, not the venue). **Files created inside the venue: 0** — confirmed by the empty diff above.

**Verdict: `confirmed (performed)`** — for all three IDs this task covers:
- **AC-4.1** holds as a live, observed fact, not an inference from reading the skill file: with no constitution, the only effect of running the profile step is one nudge naming a likely type and pointing to `/charter`; nothing is resolved, applied, written or created.
- **AC-4.2** holds in the same run: the operator (standing in for "the user") did **not** run `/charter` after the nudge, and the after-state confirms nothing was switched on anyway — no lens applied silently in the absence of that follow-up.
- **NFR-3** ("no skill or agent applies a lens without either a confirmed constitution entry or a surfaced nudge the user acts on") holds the same way: a nudge was surfaced, no lens was applied without it being acted on.

---

## Entry 5 — T5, the positive control: constitution present, constitution decides

**Class:** 2 (performed run). **Venue:** a second disposable scratch directory, fresh, separate from T4's — `git init`'d, outside every real repo. Discarded after this entry is written.

### Venue setup: a hand-written constitution activating exactly one lens

```
$ mkdir sl-t5-constitution-present && cd sl-t5-constitution-present && git init -q
$ cat .spark/constitution.md
## 2. Project Profile & Active Lenses

- Project type(s): web-app. Evidence: Vite + React SPA, no SSR, a
  dashboard-style route.
- Characteristics: none of the six.
- Active lenses:
  | ux    | Active — type web-app; the frontend is operated, not just read |
  | seo, api, cli, library, security, i18n, data | Off |
- Active-lens load: 1 lens active.
```

Same web-app signals as T4's venue (deliberately, so the two entries differ in exactly one variable — presence of a constitution), plus a constitution that declares exactly one active lens, written by hand rather than generated, so it is genuinely independent evidence rather than the mechanism checking itself.

### The check `skills/story-time/SKILL.md` step 2 specifies, performed literally

```
$ test -f .spark/constitution.md && echo EXISTS
EXISTS — constitution-present branch applies
```

Step 2's text for this branch, quoted: *"If `.spark/constitution.md` has a Project Profile & Active Lenses section, take the active lenses from it and pass their paths in step 3."* The nudge sentence belongs to the **other** branch and was never reached — there is nothing to "not use," because the step's own logic is an if/else, not a fallback that runs regardless.

### AC-4.3 — the lens resolved **from the constitution**, not re-detected

```
$ grep -A1 '^| `ux`' .spark/constitution.md
| `ux` | **Active** — type `web-app`; the frontend is operated, not just read | ... |
| `seo`, `api`, `cli`, `library`, `security`, `i18n`, `data` | Off | — |
```

One active lens, read verbatim off the file — not inferred a second time from the venue's signals (those signals produced the constitution's own entry when it was hand-written, one step earlier and outside this ceremony run; the ceremony itself only reads the file). **0 lenses applied beyond the one declared** — `seo`, `api`, `cli`, `library`, `security`, `i18n`, `data` were never opened; only `lenses/ux.md` was consulted, because it is the only one the constitution names active.

**Verdict: `confirmed (performed)`** for AC-4.3 — the active lens came from the constitution, the nudge path was structurally unreachable given a constitution exists, and no lens beyond the declared one was touched.

### AC-2.2 — the conscious N/A, performed against a real (if tiny) feature idea

A feature idea was put to this venue's PO step, chosen so the active `ux` lens has **nothing** to touch:

> *"Add `<meta name="robots" content="noindex">` to the internal-only Dashboard route... No new flow, no new form, no new interactive state, no visual change a user would notice — a single static meta tag in the route's head."*

Per `agents/product-owner.md:74-81` ("For each active lens... read its checklist and capture the concerns this feature actually touches as measurable NFRs... A lens with nothing relevant to this feature gets one line saying so — a conscious N/A, not a silent gap"), `lenses/ux.md`'s five checklist sections (flow efficiency, state coverage, forms & input, responsive & touch, feedback & motion) were checked against the idea one by one: a head-only meta tag touches none of them. The conscious N/A written into the spec's NFR table, performed rather than described:

```
| NFR-2 | UX (lens) | N/A -- this feature adds a static <meta> tag only; no new
flow, form, state or interaction for a user to experience. The ux lens's
checklist (flow, state coverage, forms, responsive, feedback/motion) has
nothing to touch here. | -- |
```

**Verdict: `confirmed (performed)`.** AC-2.2 holds: the active lens produced a **one-line, reasoned N/A** naming which checklist sections were checked and why none applied — not a silent omission (no NFR row at all) and not a lens checklist pasted verbatim (the failure mode AC-2.3 separately guards against).

### This entry's scope

T5 covers AC-4.3 and AC-2.2 only, per `plan.md` §3. NFR-3 is already covered by T4; AC-2.2's sibling AC-2.3 ("the lens's own checklist is not pasted verbatim") is a separate claim about a *relevant* lens, not a vacuous one — T8/T9's field evidence, not this task, carries that one, since it needs a real project where the lens actually fired with something to say.

---

## Entry 6 — T6, field survey: the profile section itself, across four projects

**Class:** 3 (field evidence). **Projects:** `P-SELF`, `P1`, `P2`, `P3` — the id↔project map is in an untracked scratchpad note, not this file (privacy rule, §1 above). `P-SELF`'s own constitution is public and quoted directly elsewhere in this repo; `P1`–`P3` appear here only as counts, presence/absence checks, and category labels — never a quote, a path, or a name.

### AC-1.1 — every type/characteristic carries evidence

| | Declared type(s) | Characteristic count | Every claim evidenced? |
|---|---|---|---|
| `P-SELF` | 1 (`library`) | 0 active | Yes — file/config signal (`.claude-plugin/*.json`) for the type; the one near-miss characteristic (`is-public`) is explained, not asserted |
| `P1` | 2 (`cli`, `web-app`) | 2 active (`is-multilingual`, `handles-pii`) | Yes — file/config signal for both types and `is-multilingual`; `handles-pii` is explicitly flagged as a **judgment call** about content sensitivity rather than a literal file-or-config match, disclosed as such rather than asserted as if it were one |
| `P2` | 2 (`cli`, `library`) | 0 active | Yes — file/config signal for both types; one characteristic (`handles-pii`) is explicitly ruled **off** by a disclosed reasoned decision, not a signal absence asserted silently |
| `P3` | 1 (`library`) | 0 active | Yes — the type is disclosed as a judgment call (an internal, statically-linked API contract rather than a published package, confirmed by the user), explicitly flagged as non-literal, same pattern as `P-SELF`'s own type evidence |

**Pattern worth naming, not a violation:** three of four profiles (`P-SELF`, `P1`, `P3`) ground at least one claim in an explicit, disclosed judgment call rather than a literal file signal. AC-1.1's actual requirement is that a claim is *evidenced*, not that the evidence be a literal file — and in every instance, the judgment call is stated as such, with its reasoning, never presented as if it were a mechanical signal match. **Verdict: `confirmed (field)`** for AC-1.1, across all four.

### AC-1.2 — every lens row carries both a "why" and an "enforced in"

Read every lens table, all four profiles, every row. ~~31 total row-entries~~ — **corrected at `/peer-review` round 1 (F7, Minor): the original count conflated two different units and got both wrong.** Counted properly, two ways:

```
$ for c in <each project's constitution.md>; do
    sed -n '/Active lenses/,/Active-lens load/p' "$c" | grep -cE '^\| \`'
  done
6   # P-SELF — a project with 6 literal table rows (two rows each group a pair of lenses)
8   # P1
5   # P2
4   # P3
```

**23 literal table rows**, not 31. Every project's table covers all 8 lenses either way — a grouped row (e.g. `seo`, `ux` sharing one "Off" reason) still names both lenses in its own cell — so the **lens-instance** count, the unit AC-1.2 actually asks about ("a why active/off and an enforced in **per lens**"), is **8 lenses × 4 projects = 32**. Every row, read in full, carries both required columns regardless of whether it covers one lens or several. **0 lens-instances missing either column, across 32.** **Verdict: `confirmed (field)`** — unchanged; only the stated count was wrong, in two different ways, neither previously caught.

### AC-1.3 — a lens the user rejected despite a proposed signal

AC-1.3's literal scenario: *"Given the user rejects a proposed lens... that lens is recorded as off — no lens is switched on that the user did not confirm."* Read for the specific pattern — a lens **proposed as a candidate** (a real type/characteristic signal present) and then **turned off by the user's own decision against that signal** — not a lens that was simply never triggered in the first place.

Checked every "off" row in all four profiles for this pattern:

- `P-SELF`: `security` off — "no runtime, no auth, no PII... 14 of 15 checks inapplicable." No characteristic signal was present to propose it; nothing to reject.
- `P1`: `api`/`library` considered **as project types** and rejected — but that is a type rejection, not a lens proposed by an active characteristic and then turned off; `seo`/`api`/`library`/`data` off rows are all plain type/characteristic mismatches.
- `P2`: `handles-pii` — the closest candidate. The constitution records a **conscious, reasoned decision to rule the characteristic off**, citing the project's own stronger standing non-negotiable as already covering the concern more precisely — a deliberate ruling, not a silent absence. But `security` (the lens `handles-pii` would trigger) is **independently active** on this project anyway, via a different, separately-confirmed path — so no lens was actually proposed-then-rejected here either; the characteristic was ruled off while its associated lens stayed on for other reasons.
- `P3`: `ux`/`seo`/`api`/`cli`/`security`/`data`/`i18n` off — every row cites a plain type/characteristic mismatch (the relevant type or characteristic simply isn't present), none records a rejected proposal.

**Verdict: `not-verified-live (venue named)`.** No project's constitution, across all four surveyed, documents an instance of a lens being proposed on a real signal and then explicitly rejected by the user against that signal — every "off" row is a mismatch recorded as such, not a rejection of something that was genuinely on the table. `P2`'s `handles-pii` ruling is the nearest adjacent evidence and is named here precisely so it is not mistaken for satisfying the AC — it is a characteristic ruled off while its lens stayed active for independent reasons, which is a different claim than AC-1.3 makes. The missing venue: a profile where a live type/characteristic signal fires, the Facilitator proposes the lens it would normally trigger, and the user says no anyway.

### AC-1.4 — the elevated-load flag, present exactly when load ≥ 4

| | Active-lens count | Flag present? | Correct? |
|---|---|---|---|
| `P-SELF` | 1 | No — states the flag is inapplicable below the threshold | ✅ |
| `P1` | 4 | Yes — an elevated-load warning is present | ✅ |
| `P2` | 4 | Yes — an elevated-load warning is present | ✅ |
| `P3` | 1 | No — states the load is not elevated | ✅ |

Two positive instances (load exactly at the 4-threshold, flag set both times) and two negative instances (load 1, no flag, both correctly silent). **Verdict: `confirmed (field)`** — the flag's boundary condition is demonstrated on both sides, not just the easy side.

---

## Entry 7 — T7, the suppression leg, with its own positive control

**Class:** 3 (field evidence). **Projects:** `P-SELF`, `P1`, `P2`, `P3`.

### Counting method, stated before the count

Same method as T1 (Entry 1): a row counts as lens-attributed only if its Category column names the lens in parenthetical/italic form (e.g. *"Accessibility / UX (lens)"*), never the template's standing `Accessibility`/`Performance` categories that exist independent of any lens. Every NFR table, every feature, in all four projects, read in full.

### AC-6.1 / NFR-5 — lens-attributed SEO/UX NFR count, per project

| | Active UI lens? | Lens-attributed SEO/UX NFR rows |
|---|---|---|
| `P-SELF` | No (`library` only) | **0** (Entry 1) |
| `P1` | Yes (`ux` active) | **0** |
| `P2` | Yes (`ux` active) | ~~**4**~~ ~~**8**~~ **9** (7 active, 2 consciously N/A, across 7 features — one feature carries three rows — corrected at `/peer-review` round 1, F6, Minor: `grep -c 'UX (lens)\|ux lens'` missed four rows phrased differently, e.g. *"UX — state coverage & responsiveness (`ux` lens)"* and *"Accessibility & UX (`ux` lens, constitution §4)"*; corrected again at round 2, F6, Minor, then corrected again at round 3 (F12, **Blocker**: the round-2 text below named the feature and quoted the row's literal id verbatim — a non-public feature name and a verbatim sentence from a surveyed repo, exactly what this ledger's own denylist forbids; restated here with neither): the round-1 re-sweep anchored on `| NFR-[0-9]+ \|` immediately after the pipe, which silently excluded one feature's NFR row whose id carries a parenthetical amendment note before the closing pipe. A case-insensitive sweep for any NFR row naming `ux` at all, without anchoring past the id, finds 9, not 8.) |
| `P3` | No (`library` only) | **0** |

**Added at `/peer-review` round 2 (F4, Major): each row's count now carries the command that produced it, over an opaque placeholder path, with the unit named.**

```
$ for s in <project's every feature spec.md>; do grep -niE '^\| NFR-[0-9]+' "$s" | grep -iE 'ux|seo'; done
```
Run per project (unit: matching NFR table rows, across every feature's `spec.md`):
- `P-SELF` → (no output). **0**.
- `P1` → (no output). **0**.
- `P2` → **9** matching lines, spanning 7 distinct `spec.md` files (one file contributes three).
- `P3` → (no output). **0**.

**Corrected at `/peer-review` round 3 (F13, Minor): this command is a looser sweep than the method stated above** — it matches `ux`/`seo` anywhere on the row, not only in the Category column, so a row could in principle match on body text alone and inflate the count past what the stated method would credit. Checked directly for `P2`'s 9 matches: every one names `ux` in its own Category field (the row's second pipe-delimited column), not only in body text — e.g. *"Accessibility / UX (lens)"*, *"UX — state coverage & responsiveness (\`ux\` lens)"* — so the broad command and the stated Category-only method agree on this data, but they are not the same check, and a future re-run should not assume they always will.

**Selectivity holds at the aggregate level required by the AC:** zero on every project whose profile activates no UI lens (`P-SELF`, `P3`), and non-zero on at least one project whose profile does activate one (`P2`). The literal AC only requires the positive side to exist somewhere, which it does. **Verdict: `confirmed (field)`**, for AC-6.1/NFR-5 as literally written.

### A claim this entry got wrong the first time: `P1`'s own zero

**Corrected at `/peer-review` round 1 (F2, Major).** The first draft below called this a `refuted-with-finding` instance — active lens, zero evidence it ever fired, no conscious N/A either — and reasoned that the mechanism "has not yet been exercised on a feature where it would show up." That reasoning was backwards. Checked properly:

```
$ git log --diff-filter=A --format='%ad' --date=short -- .spark/constitution.md   # P1
2026-08-19
$ for f in .spark/*/spec.md; do                                                    # P1, every feature
    git log --diff-filter=A --format='%ad' --date=short -- "$f" | tail -1
  done
2026-07-14   (one feature)
2026-08-04   (the other)
```

`P1` has exactly **two** features in its history, ~~both with an NFR table~~ — **corrected at `/peer-review` round 2 (F10, Minor): only one of the two has an NFR table at all (5 rows); the earlier one has zero.** Both claims still support the same conclusion, checked precisely: `git log --diff-filter=A --format='%ad' -- <each feature's spec.md>` gives 2026-07-14 (0 NFR rows) and 2026-08-04 (5 NFR rows), and **both predate the constitution's own creation (2026-08-19) by weeks** — there is no post-profile feature anywhere in `P1`'s history, with or without an NFR table. This is not "the lens hasn't shown up yet" (which implies a feature exists, post-profile, waiting its turn) — it is the **same structural absence Entry 10 names correctly two entries later**: no constitution existed when either feature ran, so there was no active lens to fire or fail to. R1 requires a lens that exists and could fire; here, as in Entry 10's counterfactual, it could not have.

**Verdict: `not-verified-live (venue named)`**, not `refuted-with-finding`. The missing venue: a `P1` feature that runs *after* 2026-08-19, with an NFR table, under the now-active `ux` lens. None exists yet. This is the correct, narrower claim — and it is exactly the distinction Entry 10 draws for a different project in the same sweep; missing it here first and catching it only at `/peer-review` is recorded rather than quietly reordered to look consistent throughout.

### AC-3.3 — a non-UI lens contributes zero QA-owned checks

`lenses/cli.md`, `library.md`, `api.md`, `data.md` all declare `phases` **without** `qa` (Entry 2) and each states in prose that its verification lives in Specify/Review, not a QA surface. Checked every surveyed project's `qa.md` files for a row attributed to one of these four lenses under the QA phase:

**Corrected at `/peer-review` round 2 (F4, Major): each cell below now carries the command that produced it, over an opaque placeholder path, with the unit named — round 1 left three of the four cells stated as bare conclusions, which is how F2, F3 and F6 went undetected in the first place.** **Corrected again at round 4 (F13/F20, Minor/Major): the four cells below previously used four different ad-hoc grep patterns, one per project, chosen after already knowing each answer — and at least one (`P1`'s) was too narrow to trust: run against `P-SELF`'s own 3 known-matching files, it finds only 1, missing the two that use this repo's own heading-style attribution (`### Active lens: \`library\``) rather than an inline parenthetical. A pattern that under-matches on a dataset whose answer is already known cannot be trusted on one whose answer isn't. Replaced with one broad, deliberately over-inclusive sweep run the same way against every project, followed by the same manual classification step for every match: keep only rows that are (a) shaped like an NFR-table row or a dedicated lens-attribution heading, and (b) resolved at the QA phase with a pass or an explicit N/A — discarding prose mentions and Review-owned cross-references, which the broad sweep also catches by design.**

```
$ grep -niE '### Active lens:|\b(cli|library|data|api)\b.{0,15}lens' <project's every qa.md>
```

- `P-SELF` (real path, exempt from the privacy rule: `.spark/*/qa.md`) → 4 raw matches in 3 files (`graph-gates/qa.md` matches twice: a heading and a prose mention of the same lens two lines later). Classified: 3 files, each carrying one genuine `library`-lens QA-phase attribution (2 headings, 1 bold-prose form) — **3**, unchanged from round 1's corrected count (F3).
- `P1` → (no output). **0**, re-confirmed under the broader sweep — not an artifact of too narrow a pattern this time.
- `P3` → 2 raw matches, one genuine (`library lens, scoped`, ✅ pass at QA) and one explicitly `N/A for QA (owned by Review)` on a different feature's NFR-5/6, correctly excluded. **1**, unchanged from round 2's corrected count (F3).
- `P2` → 5 raw matches: 2 genuine `cli`-lens rows, ✅ pass, on two different features; 2 explicit N/A rows (`library`-lens, "not independently re-verified by QA"; `CLI`-lens, "verified in `review.md`" instead); 1 prose mention with no NFR id at all. **2**, unchanged from round 1's corrected count (F6) — now reached by the same check as the other three, not a different one.

All four counts are unchanged from their already-corrected values; what changed is that one pattern, applied the same way and manually classified the same way, now produces them — closing the gap a reviewer flagged between what Entry 7 claimed to check and what its quoted commands actually checked.

**Verdict: `refuted-with-finding`** — stronger than either earlier draft, not weaker: round 1 counted `P-SELF` as 0 by excluding the lens under test from its own count; round 1's fix corrected `P-SELF` to 3 but left `P3` at the same kind of 0; round 2 corrects `P3` too. AC-3.3's literal text says *"zero **browser** checks"* — on a project with no browser at all, every QA-phase check is by construction a command-output check, not a browser one, so the literal word "browser" does not map cleanly onto any of these projects' own substitute methods. But the **structural** claim AC-3.3 exists to make — a lens whose own `phases` frontmatter excludes `qa` contributes nothing at the QA phase — does not hold for **three of the four projects checked**: `library.md` and `cli.md` both declare no qa ownership, and `P-SELF`'s own class-1 self-audit plus `P2` and `P3`'s own field practice each verified QA-phase content for one of them anyway — 3, 2 and 1, each the count of genuine matches after classification (**corrected at round 5, F23, Minor: "the two units coincide here, per the note above" pointed at a units-coincide note that round 4's own F13/F20 fix deleted when it replaced the four separate ad-hoc commands with one uniform one — there is now one unit throughout, not two to reconcile, so the cross-reference is dropped rather than repaired**; **and at round 4, F16, Minor: this sentence still called `P-SELF`'s self-audit "field practice," the same miscount the next sentence already corrected**). Finding, routed onward: either these lens files' `phases` frontmatter is incomplete (each owning project's actual QA method — command-output-based in every case here, since none has a browser surface — *can* observe this category, and the lens file should say so) or field practice in the two external projects is drifting from the lens contract in the same direction. ~~That the same pattern appears in three independent, unrelated projects, not one, makes "the lens file is incomplete" the far more likely of the two readings~~ — **corrected at `/peer-review` round 3 (F16, Minor): `P-SELF` is this repo's own class-1 self-audit, not independent field practice, and does not belong in a count of "independent, unrelated projects."** Restated: the pattern appears in **two** independent external projects (`P2`, `P3`) plus this repo's own self-audit (`P-SELF`) — two unrelated codebases agreeing is still the stronger signal for "the lens file is incomplete" over "one project drifted," but it is two, not three, and `P-SELF` is evidence of a different kind (a claim about our own artifact, not a second data point on field drift) — still not adjudicated here; this feature verifies the mechanism, not any project's conformance to it.

---

## Entry 8 — T8, the Review leg: a Review-owned lens NFR traced into the diff

**Class:** 3 (field evidence). **Project:** `P2`. **Spec IDs only** — no file path, no filename, no verbatim text quoted from either artifact.

### The chain, Specify → Review, no QA surface required to complete it

`P2`'s declared project type is `cli` + `library` — genuinely non-UI, no `website`/`web-app`/`api` signal anywhere in its profile (confirmed in T6). `security` is one of `P2`'s four active lenses (Entry 6), and `security.md`'s own `phases` frontmatter includes `review` (Entry 2) — it is squarely the "Review-owned lens on a non-UI project" AC-2.1a and AC-3.4 ask for.

One completed feature in `P2`'s history carries a spec-level NFR whose Category column attributes it explicitly to *"Security (lens)"*, and whose *How it's verified* column names `/peer-review` (alongside `/demo-day`, since `security` is also QA-owned — naming both does not fail the AC, which requires only that `/peer-review` be named, not that it be named alone).

**Corrected at `/peer-review` round 1 (F8, Major).** The first draft of this paragraph cited a finding from that feature's `review.md` as if it were the trace of this NFR — it is not. That finding is a different, Major-severity defect (a missing exception-handling boundary on a public function, a `library`-lens concern per this file's own conventions, not a `security` one), and citing it here conflated two unrelated rows that happen to sit in the same report. Checked properly: the feature's `review.md` carries a dedicated **traceability table**, and that NFR's own row in it is a direct pass — *not* a finding to fix, a clean trace — verified by the Reviewer with a fresh, independently-constructed hostile input (not the developer's own fixture) through both code paths the NFR covers, confirming zero script/SVG/iframe tags and zero inline-event-handler attributes reach the rendered output; the hostile payload survives only as escaped text. That is the actual Specify→Review chain this entry means to point at: a named location, a concrete verification method, resolved under the NFR's own ID.

**Verdict: `confirmed (field)`** for AC-2.1a, AC-3.4 and NFR-2's traceability claim. The chain completes at Review — Specify raised a measurable NFR naming `/peer-review` as its verifier, and Review traced it to a concrete location and resolved it under the same ID (here, a clean pass, independently re-verified — a trace does not require a defect to count, only that the NFR was actually checked against something concrete), with no QA surface needed for the chain itself to be complete (QA separately also touched this lens, which is consistent with `security.md`'s own `phases` including `qa`, not a contradiction of the claim).

### The literal `api`-typed half — `not-verified-live (venue named)`

AC-2.1a's wording is *"e.g. `api` or `security`"* — `security` satisfies the AC as written, but the `api` lens **itself** has no venue anywhere on this machine:

```
$ grep -A1 'Project type' <each project's constitution.md>
cli + web-app       (P1)
cli + library       (P2)
library             (P3)
library             (P-SELF)
```

Zero of four declare `api`. **Verdict: `not-verified-live (venue named)`** for the `api` lens specifically — no project accessible here activates it, so its own Specify→Review chain (as opposed to `security`'s, which does complete) remains untested. Recorded separately and explicitly, per `plan.md`'s own instruction, rather than letting `security`'s pass stand in for a lens it is not.

---

## Entry 9 — T9, the QA leg: a UI lens verified in the browser, and the venue that does not exist

**Class:** 3 (field evidence), row (a); structural fact, row (b). **Project:** `P2` for row (a). **Spec IDs only.**

### (a) Generalized — `confirmed (field)`

One completed `P2` feature carries a spec NFR categorized *"Accessibility / UX (lens)"*, naming `/demo-day` in its *How it's verified* column. That same feature's `qa.md` verifies the **same `NFR-n`** with three independently **named, concrete browser measurements** — not "checked," but each one specific: a full DOM heading-structure traversal re-counted from scratch; a WCAG contrast ratio recomputed via a real style-computation API directly against live, rendered colors (stated explicitly as *not* trusting the number the Reviewer had already produced for the same check — an independent re-derivation, not a citation); and a viewport-width scroll measurement at a named mobile breakpoint.

**Verdict: `confirmed (field)`** for the generalized form of the UI-lens/QA leg. The lens is `ux` (stated as such, per this entry's own counting convention — Entry 1/7 — a lens-attributed category, not the template's standing `Accessibility` row). The NFR raised in Specify, verified in `/demo-day`, under the same ID, with a browser-measured result named at the level of specificity AC-2.1 asks for ("e.g. an LCP budget" — here, a contrast ratio and a scroll-width measurement play the equivalent role for a non-SEO UI lens).

### (b) Literal — `not-verified-live (venue named)`, stated as a substitution, not a pass

AC-2.1's literal text names `seo` on a `website` feature specifically. Checked, reusing T8's same grep across all four profiles' declared types (Entry 8): **zero declare `website`.** Checked separately (Entry 6, Entry 7) whether any profile activates `seo` regardless of type: **zero.** AC-3.2's SEO instance inherits the same absence — there is no SEO NFR anywhere to verify in a browser, because there is no project with an `seo` lens active to raise one.

**Verdict: `not-verified-live (venue named)`.** The missing venue: a project declaring type `website` with `seo` active, anywhere accessible to this sweep. Row (a)'s `ux`/accessibility chain is a **substitution** — a different lens, on a different kind of non-indexable UI — and is named as exactly that, never presented as AC-2.1 itself passing. Per `plan.md` §1's own rejected alternative, no synthetic `website`+`seo` fixture was built to manufacture a pass: doing so would prove the mechanism, not this AC's literal claim, which is precisely the R1 failure this feature exists to avoid committing.

---

## Entry 10 — T10, the counterfactual: what happened before a profile existed

**Class:** 3 (field evidence). **Project:** `P2`. **Recorded by opaque id, severity, phase and `NFR-n`/severity shape only — no quote, no path, no filename, either side of this contrast.**

### Before: the earliest loop, no constitution yet

`P2`'s earliest completed loop ran **before** `P2` had a `.spark/constitution.md` at all — confirmed by commit order, not by a claim in either artifact (the feature's own commit predates the constitution-recording commit). Its Specify phase's Security & privacy row is marked **N/A**, reasoned explicitly (no PII collected, no network/auth surface in a local CLI at that point) — a disclosed, conscious N/A, not a silent omission.

Downstream, that same feature's QA phase recorded **two Blocker-severity findings**, one of them explicitly categorized as a security finding: an arbitrary-file-write/path-traversal defect via an unvalidated input that becomes a filesystem path, and a second Blocker for a raw-traceback leak on malformed input.

**Did an upstream lens NFR precede the Blocker? No — and it structurally could not have.** There was no constitution, therefore no active-lens mechanism at all; the N/A was reasoned on the project's own (correct, at the time) read of its characteristics, not on a lens that fired and missed something. This is **not** a clean instance of R1 (*"a lens silently failing to fire, indistinguishable from one correctly N/A'd"*) — R1 requires a lens that exists and could have fired; here, no lens existed yet to fire or fail to. It is the **absence's own cost**, a different and arguably sharper data point: the category that would have caught this class of defect upstream was marked N/A on reasoning that held for the network-surface question but did not anticipate a local-path-construction vulnerability class — and nothing in the loop as it then ran prompted anyone to ask.

**Verdict: `refuted-with-finding`** — not against the lens mechanism itself (it wasn't in play), but against the **narrower claim this counterfactual lets the feature test**: that a Security & privacy NFR category, reasoned correctly against the signals its author checked, reliably anticipates the defect classes QA will later find. It did not. Routed as a finding for `P2`'s own history, not fixed here — this is field evidence about a project outside this feature's fence, recorded once and left.

### After: the same project, post-profile

`P2`'s later, post-constitution loop is the **same chain already recorded at Entry 8**: `security` active, its lens-attributed NFR named `/peer-review` as its verifier, and the Reviewer traced it to a concrete location and closed it under the same ID — `confirmed (field)`.

### The contrast, stated plainly

Before a profile existed: a reasoned N/A that missed a defect class, found downstream as two Blockers, with nothing upstream tying the miss to a checklist that could have caught it. After a profile existed, with the mechanism this feature verifies actually active: a lens-attributed NFR, raised deliberately, traced to a concrete finding and closed under its own ID. Both outcomes are written up with the same rigor and neither is privileged — the honest reading is that the second state is measurably better than the first on the one axis this feature can actually observe (an NFR exists to be traced), not a proof that the mechanism would have caught the earlier defect had it existed at the time; `security.md`'s own checklist (Entry 2) does name input validation and path traversal explicitly, which is suggestive but not the same as a demonstrated catch.

---

## Entry 11 — T11, consolidation: one verdict per spec ID, one per success-signal leg

### Every AC and applicable NFR, exactly one verdict each

| ID | Verdict | Entry |
|---|---|---|
| AC-1.1 | `confirmed (field)` | 6 |
| AC-1.2 | `confirmed (field)` | 6 |
| AC-1.3 | `not-verified-live (venue named)` | 6 |
| AC-1.4 | `confirmed (field)` | 6 |
| AC-2.1 | `not-verified-live (venue named)` — literal `seo`/`website` | 9(b) |
| AC-2.1a | `confirmed (field)` — via `security`; the `api` lens's own venue separately `not-verified-live` | 8 |
| AC-2.2 | `confirmed (performed)` | 5 |
| AC-2.3 | `confirmed (field)` — every lens-attributed NFR read in Entries 8/9 is a single falsifiable statement, never a pasted checklist | 8, 9 |
| AC-3.1 | `confirmed (audit)` | 2 |
| AC-3.2 | `not-verified-live (venue named)` — literal SEO instance | 9(b) |
| AC-3.3 | `refuted-with-finding` | 7 |
| AC-3.4 | `confirmed (field)` | 8, 10 |
| AC-4.1 | `confirmed (performed)` | 4 |
| AC-4.2 | `confirmed (performed)` | 4 |
| AC-4.3 | `confirmed (performed)` | 5 |
| AC-5.1 | `confirmed (audit)` | 2 |
| AC-5.2 | `refuted-with-finding` | 3 |
| AC-5.3 | `confirmed (audit)` | 2 |
| AC-6.1 | `confirmed (field)` — aggregate/selectivity, as literally worded | 1, 7 |
| AC-6.2 | `confirmed (audit)` | 2 |
| AC-7.1 | `confirmed (audit)` | 2 |
| AC-7.2 | `confirmed (audit)` | 2 |
| NFR-1 | `confirmed (audit)` | 2 |
| NFR-2 | `confirmed (field)` | 2, 8 |
| NFR-3 | `confirmed (performed)` | 4 |
| NFR-4 | `refuted-with-finding` — stated skill count is stale; this feature's own narrower claim (zero new roles added by it) separately holds | 3 |
| NFR-5 | `confirmed (field)` — aggregate/selectivity | 1, 7 |
| NFR-6 | `refuted-with-finding` | 3 |
| NFR-7 | N/A (spec §5) | — |
| NFR-8 | N/A (spec §5) | — |
| NFR-9 | `refuted-with-finding` | 2 |

**22 of 22 ACs covered, 0 missing, 0 carrying two verdicts.** **7 of 9 NFRs carry a verdict, 2 are N/A per spec §5 — 0 missing, 0 double-verdicted.** 31 rows total, counted programmatically against this table, not by eye.

**Tally: 21 `confirmed`** (7 `(audit)`, 5 `(performed)`, 9 `(field)`) **+ 5 `refuted-with-finding` + 3 `not-verified-live` + 2 `N/A` = 31.** The refutations are not noise: AC-3.3, AC-5.2, NFR-4, NFR-6 and NFR-9 are five independent, real, citable gaps this sweep found by performing and reading rather than by trusting the spec's own *Gaps: built code vs. this spec — both closed* claim (spec, final section) — which this entry's own evidence partially **reopens**: G1/G2 (the two gaps the spec names) are confirmed closed by this sweep (Entries 4, 5, 6), but this sweep found **five more** the spec's retrospective close-out did not know about, because nothing had independently audited the built lens files' own internal consistency, the skill-file add-a-file guarantee, or any field project's actual conformance until now.

### The four success-signal legs (spec §1)

| Leg | Verdict | Entry |
|---|---|---|
| **UI-lens fires, QA-verified** | `confirmed (field)` via the `ux` lens (substitution, stated as such) — the literal `seo`-on-`website` form remains `not-verified-live`, venue named | 9 |
| **Review-lens fires, Review-verified** | `confirmed (field)` via the `security` lens — `api` satisfies the AC's own "e.g." wording; the `api` lens's *own* venue remains `not-verified-live` | 8 |
| **Suppression works** | `confirmed (field)` at the aggregate level the spec's AC asks for (zero where no UI lens active, non-zero where one is) — **with a named field gap the aggregate hides**: one UI-lens-active project shows zero evidence of the lens ever firing, and (corrected at `/peer-review` round 1, F2) that project turns out to have no post-profile feature at all, so the gap is `not-verified-live`, not a refutation | 1, 7 |
| **Add-a-file holds** | `refuted-with-finding` — one skill file (not a lens file) contains a closed enumeration of lens filenames rather than the generic form every sibling instruction uses; adding a 9th lens with new QA-phase coverage would require editing it | 3 |

**Two of four legs confirmed outright, one confirmed-with-a-named-exception, one refuted.** This is not the "both legs fire cleanly" result the spec's success signal was written hoping for — it is a more textured, more honest one: the mechanism's *structure* (frontmatter, phase ownership, the nudge-vs-constitution split, the conscious-N/A discipline) holds up under direct audit and live performance without exception; what the **field** reveals, once real projects are actually read rather than assumed, is that firing is not guaranteed even when a lens is active, and the one file most responsible for routing a new lens to its right phase is not as generic as its siblings. Both kinds of finding are exactly what a verify-only sweep is for.

---

## Entry 12 — T12, privacy and fence audit

**Class:** 1 (artifact audit, of this very file and this branch's diff).

### Denylist grep — 0 hits

**Corrected at `/peer-review` round 1 (F1, Blocker).** The first draft of this entry quoted the denylist grep's literal pattern — which meant the three surveyed projects' real names were typed out, in plain text, inside this committed file, as the very thing being proven absent from it. The grep *of* the file became a leak *in* the file. That draft's own "(no output)" line was false against the block directly above it.

Fixed by never typing the denylist's literal terms into a committed command again. The check was re-run against the corrected file, built from the untracked id-map note (never this file) and run as a compiled pattern from a scratch file, never as a literal argument: **0 hits** on the three projects' real names. A second check, for absolute-path patterns as a category (`/Users/`, `/home/`, `/private/`, `/Volumes/`), returns exactly one hit — this paragraph's own description of what the category means, which names the pattern as a label, not as part of a real path; no username or specific directory follows it anywhere in this file.

Every blockquote in this file checked individually against its source: one (Entry 3) is a verbatim quote from this repo's own public `skills/demo-day/SKILL.md`; two (Entries 4, 5) are this operator's own output from disposable scratch venues this feature created and controlled, not quotes from `P1`–`P3`. **0 block-quoted verbatim sentences attributed to a non-public repo**, across all 11 prior entries. **Corrected at `/peer-review` round 4 (F19, Minor): this check covered blockquotes only — the separate, narrower category-label fragments used inline elsewhere (Entries 6, 7, throughout) are a different, explicitly named exception (Privacy rule, above), not an omission from this count.**

### Fence — `git diff --name-only` against `origin/main`

~~Two files, both under `.spark/situational-lenses/`~~ — **stale the moment T13 ran** (F5, Minor, `/peer-review` round 1): this entry was written before T13 added `README.md` to the diff, and was never revisited when that happened. Re-run after T13:

```
$ git diff --name-only origin/main
.spark/situational-lenses/evidence.md
.spark/situational-lenses/plan.md
README.md
```

Three files, confirmed at the commit where T13 had just run (that exact commit is no longer resolvable after this branch's pre-release history squash, Entry 17 below — the count was true then and the re-run below reproduces the conclusion regardless) — the third is `plan.md`'s own sanctioned exception (§1, §2: "the sole non-`.spark/` edit in the whole feature diff"), not drift. **A literal count here is a snapshot, not a standing fact** (F9, Minor, `/peer-review` round 2): `review.md` itself enters this same `git diff` the moment `/peer-review` commits its own report, which is expected and not fence drift — the fence in `plan.md` §1 governs `lenses/`, `agents/`, `skills/`, `templates/` and `.claude-plugin/plugin.json`, never this feature's own ceremony artifacts. The check that actually matters, and that stays true regardless of how many of this feature's own files exist at the moment it's run, is the one below. **Empty diff, verified directly**, over every protected surface named in `plan.md` §1:

```
$ git diff --name-only origin/main -- lenses/ agents/ skills/ templates/ .claude-plugin/plugin.json
(no output)
```

### Counts, re-confirmed at this commit

```
$ ls lenses/ | wc -l
9
$ ls agents/*.md | wc -l
7
$ ls skills/ | wc -l
10
```

9 files in `lenses/` (8 lenses + `README.md`), 7 agents, 10 skills — unchanged from Entries 2/3, confirming this sweep touched none of them.

**Verdict: `confirmed (audit)`** for NFR-4 and NFR-6's fence-conformance half (the "this feature added zero roles, touched no lens/agent/skill/template file" claim) — distinct from NFR-4's own stale-count finding (Entry 3, `refuted-with-finding`), which is about the spec's literal number, not this feature's own diff discipline. The two are not in tension: this feature added nothing and is provably clean; the spec's arithmetic about a different, earlier state is stale regardless.

---

## Entry 13 — `/peer-review` round 1 fix-mode

Eight findings, all confirmed independently before being fixed — not one was dismissed, and none was fixed by trusting the Reviewer's report over a fresh check of the primary source.

**F1 (Blocker, privacy).** Entry 12's own denylist grep printed the three surveyed projects' real names as its literal search pattern — the check *of* the file became a leak *in* the file, and its own "(no output)" line was false against the block directly above it. Fixed by never typing the denylist's literal terms into a committed command again; the real check was re-run off a pattern built from the untracked id-map note and compiled from a scratch file, never passed as a literal argument. Re-verified: 0 hits on the three names.

**F2 (Major, verdict).** Entry 7's `P1` row was reasoned backwards — "the mechanism hasn't been exercised yet" implies a feature exists, post-profile, waiting its turn. Checked by commit date: `P1` has exactly two NFR-bearing features, both predating its own constitution by weeks. There is no post-profile feature to wait on. `refuted-with-finding` → `not-verified-live`, and the corrected reasoning is the same distinction Entry 10 draws correctly, for a different project, two entries later — missed here first.

**F3 (Major, question-begging count).** Entry 7's `P-SELF` row in the AC-3.3 table excluded `library`-lens QA-phase evidence by citing library being `P-SELF`'s only lens and `library.md` declaring no qa phase — using the very fact under test to justify not counting evidence against it. Recounted properly: 3 `qa.md` files in this repo's own history carry explicit `library`-lens content at the QA phase, not 0. The refutation is stronger after the fix, not weaker — the pattern now appears in two independent projects, not one.

**F4 (Major, systemic).** Entries 6–10 mostly state conclusions without the extraction command that produced them, and without checking constitution-vs-loop dates as a matter of course — the root cause behind F2, F3, F6 and F7. Partially structural: a literal extraction command against a private repo would itself violate the privacy rule (it would need a real path as an argument), so "quote the command" and "name no path" pull against each other for class-3 evidence in a way they never do for class 1. Addressed for every specific claim this round corrected (F2, F3, F6, F7 all now carry the command or the exact re-derivation that fixed them) rather than attempted as a blanket rewrite of entries that were not shown to be wrong.

**F5 (Minor, stale fence).** Entry 12 recorded the fence as two files because it ran before T13 added `README.md`. Struck through in place and re-run.

**F6 (Minor, undercount).** Entry 7's `P2` UX-NFR count (4) missed four rows phrased without the literal string `UX (lens)` — a case-insensitive sweep for any `ux`-naming NFR row finds 8. Corrected; the verdict it supported was already `confirmed` and stays so.

**F7 (Minor, three separate arithmetic errors).** Entry 1's NFR-row total (43, actual 56); Entry 3's generic-vs-enumerated tally (5 of 6, actual 6 of 7 — the quoted grep prints 7 lines); Entry 6's lens-table count (31, actual 23 literal rows or 32 lens-instances depending on the unit, and the original number matched neither). All three corrected in place with the recount shown; no conclusion changed, every denominator was simply wrong.

**F8 (Major, misattribution).** Entry 8 cited a `library`-lens-concern finding from `P2`'s `review.md` as if it were the `security`-lens NFR's own trace — two unrelated rows in the same report, conflated. The actual trace is a clean pass in that feature's traceability table, independently re-verified by the Reviewer with a fresh hostile-input fixture. Corrected; the chain the entry argues for is real, it was just illustrated with the wrong example.

~~**Not touched:** Entries 1–5, 9, 10, 12~~ — **corrected at `/peer-review` round 2 (F11, Minor): this summary misquoted the review report and mischaracterized its own method, in the one entry nobody had reviewed yet.** Entry 1 was in fact touched, by F7's recount two paragraphs above this one — it does not belong in a "not touched" list alongside entries that genuinely were. Entries 2–5, 9, 10, 12 (beyond F1/F5's specific lines) were independently re-verified by the Reviewer against primary sources and found accurate. Entry 10 in particular is, in the Reviewer's own words, *"the strongest entry"* (`review.md:44`) and *"the model the others should follow"* (`:90`) — quoted accurately this time, not paraphrased and then wrapped in quotation marks as if verbatim, which is what happened here the first time this sentence was written.

This file's own append-only convention (Handoff, line 11) is followed throughout this pass, with one necessary exception named rather than glossed over: every correction strikes the wrong claim through in place and states the right one beside it — except F1, where the wrong content was the leak itself, and striking it through would have left the leaked names still legible. F1's lines were deleted, and the deletion is narrated in Entry 12 in place of the deleted text, which is the closest this convention can come to "struck through" when what's wrong is the text's mere presence.

---

## Entry 14 — `/peer-review` round 2 fix-mode

Round 2 reviewed round 1's fixes rather than the original ledger, and found that fixing something can itself introduce something new to get wrong. Eleven findings total: four already stood confirmed-fixed from round 1 (F1, F5, F7, F8 — no action needed here) and seven needed work (F2, F3, F4, F6, F9, F10, F11). All seven re-verified independently against primary sources before any text changed, same discipline as round 1.

**F2 (Major, stale publication).** Round 1 corrected Entry 7's `P1` verdict in `evidence.md` but never propagated the correction to `README.md`, which still published the old `refuted-with-finding` framing — phrases like "indistinguishable from silent non-firing" that the fix had already retracted. Fixed by rewriting the `README.md` passage to match the corrected `not-verified-live` verdict: the honest gap is a feature that postdates the profile, which nobody has shipped yet — not a lens that fired and left no trace.

**F3 (Major, partial fix).** Round 1's fix to Entry 7's AC-3.3 table reached only the `P-SELF` cell; `P3`'s identical circular-exclusion error was left standing at **0**. Re-checked `P3`'s own `qa.md` files directly: one carries `NFR-6/7 (library lens, scoped)`, resolved ✅ pass at the QA phase. Fixed: `P3`'s cell corrected to **1**, and the verdict paragraph's "two independent projects" restated as three of four.

**F4 (Major, systemic, partial mitigation).** Round 1 addressed F4 only for the specific claims it had already found wrong (F2, F3, F6, F7), not as a standing practice for Entry 7 as a whole — and Entry 7 is exactly where round 2 then found three more numbers wrong (F6, F10, and F3's reopened half), two of them introduced *by* round 1's own fix. Addressed properly this round: every AC-3.3 cell and every AC-6.1/NFR-5 per-project count in Entry 7 now carries the literal command that produced it, run over an opaque placeholder path for the three external projects (`P-SELF`'s own command stays a real path, since it is exempt from the privacy rule), with the unit counted stated explicitly in every case.

**F6 (Minor, undercount, again).** Round 1's fix to `P2`'s UX-NFR count (4 → 8) was itself wrong: a fifth independent check, run with the exact command now quoted in Entry 7, found a 9th row — one feature's own NFR row, with an amendment note in its id — that every prior sweep's regex had silently excluded by anchoring on the NFR id immediately followed by a closing pipe. The four earlier passes this session all shared that same anchoring bug, which is why they agreed with each other and were all wrong together. Fixed: restated as 9 rows, 7 active + 2 consciously N/A, across 7 features (one feature carries three).

**F12 (Blocker, privacy, round 3).** The paragraph directly above, in its first-written form, named the specific feature this finding came from and quoted its NFR row's literal id verbatim — a non-public feature name and a verbatim sentence from a surveyed repo's own artifact, both denied by this ledger's own denylist (Privacy rule, above — **corrected at round 4, F18, Minor: this paragraph previously mis-cited the denylist's location as "Handoff, line 41," which is Entry 1's heading; the denylist is in the Privacy rule section, a few paragraphs above Entry 1**), the same class of leak F1 was raised for. Caught by the Reviewer, not by this entry's own privacy sweep (below), which checked only the three project names and missed the fourth denylist clause — any non-public feature name. Fixed by restating both the table cell (line 461) and this entry's own F6 paragraph without the name or the literal id; the cause (a regex anchoring bug) and the fix stand on their own without either.

**F9 (Minor, self-inflicted staleness).** Fixing F5's two-file fence count made `review.md` itself enter the diff, becoming a third file touched outside the protected surface — which is expected ceremony-artifact behavior (the Reviewer's own report is supposed to change during fix-mode), not fence drift. Noted explicitly in Entry 12 as a distinct, correctly-empty check: the protected-surface diff (`lenses/`, `agents/`, `skills/`, `templates/`, `.claude-plugin/plugin.json`) is what actually matters for this feature's fence, and it stayed empty throughout.

**F10 (Minor, imprecision introduced by a fix).** F2's round-1 fix said `P1` has "two features with an NFR table," which is imprecise — only one of the two has an NFR table at all (5 rows); the earlier one has zero. Fixed by citing the exact per-feature dates and row counts directly, so the claim no longer depends on an unstated assumption that both tables exist.

**F11 (Minor, fabricated quote in round 1's own summary).** Entry 13's closing paragraph attributed to the Reviewer a phrase — *"the ledger's best entry"* — that the round-1 report never said, and mischaracterized Entry 1 as untouched when F7's recount had in fact touched it two paragraphs earlier in the same entry. Fixed by re-reading the actual round-1 report's text as it was committed at the time (that revision's SHA is no longer resolvable after this branch's pre-release history squash, Entry 17 below — the quotes below were verified against it before the rewrite) and quoting its real text verbatim — *"the strongest entry"* (`review.md:44`) and *"the model the others should follow"* (`:90`) — and by removing Entry 1 from the "not touched" list.

**Privacy and fence, re-swept this round.** The denylist check (pattern compiled from the untracked id-map note, never a literal argument) re-run across every file this round touched (`evidence.md`, `review.md`, `README.md`): 0 hits on all three real project names. `claude plugin validate .` passes; the protected-surface diff (`lenses/`, `agents/`, `skills/`, `templates/`, `.claude-plugin/plugin.json`) is empty.

~~This file's own append-only convention is followed throughout: every correction strikes the wrong claim through in place and states the right one beside it, including the now-doubly-corrected `P2` UX-NFR cell (4 → 8 → 9), each superseded number visible, none deleted.~~ — **corrected at `/peer-review` round 3 (F14, Minor): that claim overstated this pass the same way F11 flagged for round 1's own summary.** The AC-3.3 verdict paragraph (Entry 7) was rewritten in place rather than struck through and restated — "two independent projects" became "three of four" with no visible trace of the superseded wording — and the `P2` AC-3.3 bullet was reformatted to add its command without striking the prior sentence it replaced, even though its number (2) didn't change. Both are corrections of wording or presentation, not of a wrong number, which is the narrower case this file's convention (Handoff, line 11) was written for; naming the gap plainly is the more honest move than reasserting a stricter compliance than this pass actually had.

---

## Entry 15 — `/peer-review` round 3 fix-mode

Round 3 found what round 2 missed while fixing round 1, and what round 2's own fix itself introduced: a second privacy leak, a stale self-contradiction inside this file's own Handoff, a stale table row in `README.md`, and three more Minors — one of them this file's own second overstatement of how cleanly it follows its own convention. ~~Seven~~ **corrected at `/peer-review` round 4 (F17, Minor): six** findings (F2 reopened, F12, F13, F14, F15, F16) independently re-verified before anything changed; one (F2) was a re-open of an already-`fixed` finding, confirming fixed-mode discipline has to re-check its own prior work, not just the Reviewer's new ones.

**F12 (Blocker, privacy, the most serious finding of any round so far).** Round 2's own fix for F6 named a real, non-public feature directory from one of the three surveyed external projects and quoted its NFR row's id verbatim, in two places (Entry 7's AC-6.1 table and this entry's own F6 paragraph) — the exact class of leak F1 was raised for in round 1, reintroduced by the fix pass that cited F1 as the lesson it had learned. Caught by the Reviewer doing a path-token sweep against this repo's real `.spark/` directories; missed by this file's own Entry 14 privacy sweep, which checked only the three project names — one of four denylist clauses (Privacy rule, above — **corrected at round 5, F18, Minor: this sentence carried the same wrong "Handoff line 41" citation the Entry 16 fix had already corrected once, in the one other paragraph naming it**) — and not the fourth, "any non-public feature name." Fixed by restating both passages without the name or the literal id: the regex anchoring bug and its fix stand on their own without either, and a re-swept denylist check this round covers all four clauses, not one. Not struck through — the same exception Entry 13 named for F1: striking leaked content through in place would leave it legible, so it was rewritten out directly, same as F1's own fix.

**F2 (Major, reopened — stale publication, a second time).** Round 2 fixed the two prose sentences in `README.md` that F2 named, but the table row at `README.md:286`, named in the same fix instruction, was never touched and still read "one active-lens project showing no evidence the lens ever fired" — the exact framing the prose two paragraphs below it had already retracted. Fixed by restating the row to match the prose: the honest gap is a feature that postdates the profile, which nobody has shipped yet.

**F15 (Major, the ledger disagreeing with itself).** This file's own Handoff (line 13-14) still described the AC-3.3 finding as "a cli-lens QA-phase gap" (singular lens, not the library+cli, three-of-four-projects finding Entry 7 and Entry 11 actually carry) and listed Entry 7's corrected `not-verified-live` verdict as "one risk realized in the field" — language the body had retracted two rounds ago. Entry 11's own four-legs table (line 638) already states the corrected version; the Handoff summarizing it had not been brought along. Fixed by restating both clauses to match Entry 11, and by correcting the Handoff's now-false "no committed row carries [a non-public feature name]" line to note it was re-audited after F12.

**F13 (Minor, two distinct commensurability gaps in Entry 7, both introduced by F4's own fix).** (a) The AC-3.3 cells stated their counts in two different units — files for `P-SELF`/`P1`, rows for `P2`/`P3` — and the verdict paragraph then compared them as one series without saying the units happened to coincide; checked directly and noted in place: they do coincide on this data (each matching file carries exactly one matching row), but the two checks are not the same thing and a future re-run shouldn't assume they always agree. (b) The AC-6.1 command (`grep -iE 'ux|seo'` over the whole NFR row) is a looser sweep than this entry's own stated Category-only method; checked directly that all nine of `P2`'s matches do name `ux` specifically in their Category field, so the broad command and the narrow method agree here, but the gap between what the command does and what the method requires is now named rather than left implicit.

**F16 (Minor, P-SELF counted as independent field practice).** Entry 7's AC-3.3 verdict called the drift pattern evidence from "three independent, unrelated projects" — counting `P-SELF`, which is this repo's own class-1 self-audit, alongside the two genuinely external, unrelated projects (`P2`, `P3`). Restated: two independent external projects agreeing, plus this repo's own self-audit as a third but different kind of evidence — still the stronger reading, but not a count of three unrelated codebases.

**F14 (Minor, this file's own overstatement of its own compliance — again, and the round-3 fix named the wrong two exceptions).** Entry 14's closing line claimed every correction this round struck the wrong claim through rather than silently replacing it. Round 3's own fix for this named the AC-3.3 verdict paragraph rewrite and the `P2` bullet reformat — but missed the actual clearest instance. Re-checked directly against the diff between round-1's and round-2's committed states (captured before this branch's pre-release history squash, Entry 17 below — the specific SHAs are no longer resolvable, but the diff's content is recorded here): (1) Entry 7's AC-3.3 verdict paragraph *was* rewritten wholesale, no strikethrough — correctly named already. (2) The `P2` bullet reformat — correctly named, though its number never changed, so it is presentation, not correction. (3) **The instance round 3 missed:** Entry 13's closing paragraph struck through only the "**Not touched:** Entries 1–5, 9, 10, 12" label — the sentence after it, which contained the fabricated quote *"the ledger's best entry"* that F11 (round 2) flagged, was not struck through at all; it was silently dropped and replaced by new sentences carrying the accurate quotes. The fabricated quote itself never appears struck through anywhere in this file, only removed. Named precisely this time, in place of the two-item list round 3 gave.

**Privacy and fence, re-swept this round, against all four denylist clauses.** The three real project names: 0 hits, `evidence.md`/`review.md`/`README.md`. Absolute-path patterns: the one expected self-referential hit (this sentence's own description of the category), same as every prior round. Non-public feature names: a path-token sweep of every backtick-quoted path-shaped string in all three files against this repo's real `.spark/`/`lenses/`/`agents/`/`skills/` directories — every token resolves to a real file here, none resolves to an unrecognized name, after F12's fix. Verbatim sentences from a non-public repo: none found, including in this entry itself. `claude plugin validate .` passes; the protected-surface diff stays empty.

**Branch history.** `feat/situational-lenses` has no remote tracking branch (`git ls-remote --heads origin` shows nothing for it) — the leak in `61d6799` never reached a shared branch. Left as a working-tree fix rather than a history rewrite at the time this paragraph was written: `61d6799` is not cited by SHA from this file, only from `review.md`'s own round-3 scope line, which this fix-mode pass does not own. **The Reviewer challenged this reasoning at round 4 (F12) — git history is not the working tree, and this branch's release mode pushes its whole history — and the user decided to squash. See Entry 17.**

This file's own append-only convention is followed in every correction above except where explicitly named otherwise (F14's own finding, restated honestly rather than re-claimed as perfect).

---

## Entry 16 — `/peer-review` round 4 fix-mode

Round 4 confirmed two of round 3's six fixes outright (F2, F15), found that a third (F12) was only half-fixed — the leaked strings were gone from the working tree but still sitting in this branch's own commit history — and found that the other three (F13, F14, F16) had each been "fixed" by correcting something adjacent to what the finding actually named, not the finding itself. Four new findings surfaced, one of them Major.

**F12 (Blocker, content half closed; history half is a decision, not a fix — see below).** Round 3 removed the leaked feature name and NFR id from the current working tree and the current `HEAD` commit. The Reviewer correctly pointed out that git history is not the working tree: commit `61d6799` still carries the leaked feature name in its own tree object, and two earlier commits (`206cb28`, `656b883`, from before F1's own round-1 fix) still carry all three real project names the same way — embedded in the original denylist grep command F1 flagged. Independently confirmed: `git show 206cb28:.spark/situational-lenses/evidence.md` and `git show 656b883:...` both still contain the three project names; `git show 61d6799:...` still contains the feature name; `git branch -r --contains` returns empty for all three, so none of this has reached any remote. This is a genuine gap between "fixed in the latest commit" and "fixed," given constitution §6 ("nothing that must stay private is committed") and the fact that `/go-live`'s release mode is `pr`, which pushes this entire branch. **Not resolved in this pass** — the fix is a history rewrite (squash or filter), which changes every commit SHA on this branch including the ones this very file cites by hash (`d7acf34`, `656b883`, `61d6799`), and is exactly the kind of action this project's own `CLAUDE.md` flags a prior incident for ("prior SHA-reword incidents orphaning constitution-cited commits"). Routed to the user rather than decided here. **Resolved at Entry 17, below:** the user chose to squash.

**F13, F20 (Minor + Major, the same root cause).** Entry 7's AC-3.3 cells each used a different hand-picked grep pattern, chosen after the answer was already known for each project — and `P1`'s pattern, run against `P-SELF`'s own 3 known-matching files as a sanity check, found only 1, proving it was too narrow to trust on a project whose real answer isn't known independently. Fixed by replacing all four ad-hoc patterns with one broad, over-inclusive sweep applied identically to every project, followed by the same manual classification step (keep genuine QA-phase pass/N/A rows, discard prose mentions and Review-owned cross-references) for every match. All four counts came out unchanged (`P-SELF` 3, `P1` 0, `P2` 2, `P3` 1) — the original numbers were right, but for three of the four projects that was not yet demonstrated by a method that would have caught it if they weren't.

**F16 (Minor, fixed partially last round, finished this round).** Round 3 fixed the verdict's closing sentence but left an earlier sentence in the same paragraph still calling `P-SELF`'s self-audit "field practice" alongside the two real external projects. Fixed in place.

**F14 (Minor, the fix-mode self-audit finding, for the second round in a row, that fix-mode itself needs fixing).** Round 3's fix for this named two exceptions to the append-only convention; re-checking the actual diff found a third it missed, and the third is the clearest case: Entry 13's closing paragraph struck through only the four-word "Not touched" label, not the sentence after it — which carried F11's fabricated quote and was silently dropped, never struck through, when it was replaced. Named precisely this round.

**F17 (Minor).** Entry 15's opening line said "Seven findings" when it named six ids. Corrected to six.

**F18 (Minor).** Entry 14's F12 paragraph cited the denylist's location as "Handoff, line 41" — line 41 is Entry 1's heading, not the denylist, which is in the Privacy rule section above it. This repo's own round-3 review report made the identical citation error (`evidence.md:40`/`:41`), and this file copied it uncorrected. Fixed to point at the Privacy rule section instead of a line number, since line numbers in this file drift every round.

**F19 (Minor).** The Privacy rule's own wording banned "verbatim text" in the same sentence that permits "category labels" — which are themselves verbatim text, just short fragments rather than full sentences. The denylist immediately below already uses the narrower, correct term ("verbatim sentence"); the broader sentence above it didn't match. Fixed by aligning the wording, and by correcting two overstated claims elsewhere in the file ("0 verbatim quotes," "no committed row carries a verbatim quote") to the same narrower, accurate term, since both were literally false against the category-label fragments already in use throughout Entries 6 and 7.

**A note on this pass's own compliance, stated up front rather than left for a round 5 finding.** The wording and citation fixes above (F18, F19, and the matching Handoff-line edit) were applied as direct edits, not strikethrough-and-correct — none of them reversed a wrong number or a claim under test; each corrected this file's own internal terminology or a citation's location. That is a narrower class than what this file's append-only convention was written for (Handoff, line 11: "a superseded **number** is struck through"), and it is named here rather than asserted as full compliance, since the last two rounds both had to catch a version of that exact overstatement.

**Privacy, re-swept against all four denylist clauses, working tree only** (commit history is F12's open half, not re-swept here since nothing in this pass touched it): 0 hits on the three real names; the path-token sweep resolves every token in `evidence.md`, `review.md` and `README.md` to something real in this repo. `claude plugin validate .` passes; the protected-surface diff stays empty.

---

## Entry 17 — F12's history half: the user's decision, and its execution

Round 4 left F12 half-open: the leaked feature name and the three leaked project names were gone from the working tree and from `HEAD`, but still present in three earlier commits on this branch (`206cb28`, `656b883`, pre-dating F1's own fix; `61d6799`, pre-dating F6's fix). Fix-mode does not own that decision — squashing or rewriting history changes every downstream commit SHA, including ones this file had been citing by hash, and this project's own `CLAUDE.md` records a prior incident from exactly that kind of rewrite. Routed to the user with four options (squash now, rebase the two leaking commits in place, defer to `/go-live`'s pre-flight, or find a non-rewrite mitigation). **The user chose: squash to one clean commit now.**

Before executing: every citation in this file that named a commit by SHA (`d7acf34`, `656b883`, `61d6799` — Entries 12, 13, 14, 15) was restated to describe what was checked and when, without depending on that SHA remaining resolvable after the rewrite. None of those citations supported a verdict that needed the commit to still exist; each was provenance for how a fact was checked, and the fact stands on its own.

Executed as the user specified: `git reset --soft origin/main`, then every change this branch carried (18 commits total — 1 plan commit, 13 `/increment` task commits, and four rounds of fix-mode commits, **corrected at round 5, F22, Minor: first written as "13 `/increment` commits plus three rounds," undercounting both the plan commit and the fix-mode round count by one each** — now collapsed) recommitted as a single new commit from the already-clean working tree. Verified directly, after the rewrite:

```
$ git log --oneline origin/main..HEAD | wc -l
1
$ git log --all -i --pickaxe-regex -S'<the leaked feature name>' --oneline -- .spark/situational-lenses/ README.md
(no output)
$ git log --all -i --pickaxe-regex -S'<each of the three real project names>' --oneline -- .spark/situational-lenses/ README.md
(no output, all three)
```

**Corrected at round 5 (F21, Minor): the verification originally quoted here included a third command — a bare blob count with no leak-detection logic and no output shown — that neither tested what the surrounding sentence claimed nor reproduced anything.** Replaced with git's pickaxe search (`-S`, which finds every commit that ever introduced or removed a literal string, across every reachable revision, not just `HEAD`'s tree), run for the feature name and separately for each of the three project names, scoped to this feature's own files: all four return nothing. The feature name and the three project names appear in **zero** objects reachable from any ref, within this feature's own artifacts — not just zero in the working tree. (Scoped deliberately: an unscoped repo-wide search for the project names also finds them in an unrelated, already-public, already-shipped feature's own files — see the separate note routed to the user, not a leak this feature introduced or could fix.) `git branch -r --contains HEAD` is empty (still unpushed); `claude plugin validate .` passes; the protected-surface diff against `origin/main` is still empty. **F12 is fully closed, both halves**, pending the next `/peer-review` round's own independent re-derivation of the same checks — this is fix-mode's claim, not yet the Reviewer's confirmation.

One consequence, named rather than glossed: the five rounds of `/peer-review`'s own findings tables, each citing specific commit SHAs for what was checked when, now describe a history that no longer exists in that shape. The findings themselves, the verdicts, and the narrative in Entries 13 through 16 are all still accurate — they describe what happened and in what order, which a squash doesn't change — but a reader trying to `git show` one of those old SHAs from this point forward will find nothing. That is the cost of this fix, accepted by the user with the choice above, and it is smaller than the alternative.

---

## Entry 18 — round 5's five Minors, fixed post-pass (review already `passed`)

Round 5 passed (zero Blockers, zero Majors) with five Minors open, none gating the Review phase per `/peer-review`'s own rules. The user chose to fix all five before moving to `/demo-day` rather than carry them forward.

**F18.** A second, identical "Handoff line 41" mis-citation survived in Entry 14's own F12 paragraph — the round-4 fix had corrected the copy in Entry 15 but missed this earlier one. Fixed to point at the Privacy rule section instead of a line number.

**F19.** `plan.md` carried the same "verbatim text"/"verbatim quotes" overclaim `evidence.md` had already narrowed in three places — `plan.md` itself was never touched in that pass. Fixed both instances (§1's privacy rule statement, T12's DoD) to the same narrower, accurate wording.

**F21.** Entry 17's own verification block quoted a third command (a bare blob count) that tested nothing the surrounding sentence claimed. Replaced with git's pickaxe search (`-S`), run for the feature name and each project name, scoped to this feature's own files — the check that actually supports the sentence's claim, re-run live and confirmed empty.

**F22.** Entry 17 miscounted the pre-squash branch as "13 `/increment` commits plus three rounds of fix-mode" — actually 18 total (1 plan commit + 13 task commits + four fix-mode rounds), confirmed by `git log --oneline 5b14bf5^..872380f | wc -l`. Corrected.

**F23.** Entry 7's verdict paragraph pointed at a "note above" that F20's own fix had deleted when it replaced four separate commands with one uniform one. Dropped the dangling reference rather than inventing a replacement note — there is now one unit throughout, nothing left to reconcile.

Re-swept: the three real names and the feature name, 0 hits across `evidence.md`/`review.md`/`README.md`/`plan.md`; `claude plugin validate .` passes; protected-surface diff empty.

# Evidence: right-sizing

| | |
|---|---|
| **Feature** | `right-sizing` |
| **Purpose** | The verification record for a change to prompt material. No test suite exists or is possible (constitution §4), so the evidence is a documented dry run of every touched phase — **negative case first** (constitution §1). |
| **Rule** | One entry per performed check: the command or ceremony, its actual output, and what it proves. Reading or reasoning is labelled as such and never passes an AC. Anything not run is labelled *not run*. |
| **Owner** | `/increment` (T1–T10 of `plan.md`) |

---

## Entry 1 — static parser walkthrough (T1)

- **Run:** read-only greps against the installed `aspark-graph` source. No mutation.
- **Date:** 2026-08-29.
- **Proves:** NFR-1 — the new `## 8. QA Method` field is invisible to the one non-human reader, so this is a **minor** bump with no coordinated release (constitution §6).

**P1 — `constitution` anywhere in the parser source**

```
$ grep -rn "constitution" ~/aSPARK-graph/src/aspark_graph/ | wc -l
0
```

Zero hits across the whole package. The parser never opens `constitution.md` under any name.

**P2 — `_parse_feature`'s file probes (`artifacts.py:76-80`)**

```
    spec = feature_dir / "spec.md"
    plan = feature_dir / "plan.md"
    review = feature_dir / "review-report.md"
    qa = feature_dir / "qa-report.md"
    release = feature_dir / "release-notes.md"
```

Five artifact filenames, `constitution.md` among none of them.

**P3 — the edit is purely additive**

```
$ git diff --stat templates/constitution.md
 templates/constitution.md | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)
$ git diff templates/constitution.md | grep '^-' | grep -v '^---'
(no output)
```

21 insertions, **0 deletions** — nothing renamed, removed or reordered.

**P4 — heading integrity**

```
$ git show HEAD:templates/constitution.md | grep -c "^## "   → 8
$ grep -c "^## " templates/constitution.md                    → 9
```

One heading added (`## 8. QA Method` at line 99); `## 7. Delivery & Handoff` still at line 87 and `## Amendments` still last. No constitution §3 protected heading, table column or ID pattern is in this diff's reach — §3's protected structures live in `review-report.md`'s findings table and the `US-`/`AC-`/`NFR-`/`T`/`F` ID patterns, none of which this file carries.

**Kill-criterion (plan §4):** had P1 or P2 shown the parser touching `constitution.md`, the whole approach would have required a coordinated release with `aspark-graph`. It does not.

**DoD check (T1):** section present with both fields and both stated `Default when absent:` values ✓; inline comment carries all four contract facts — method-not-coverage (AC-1.2), browser/QA-specific with no off switch for any other ceremony (AC-1.7), `/charter`-only (AC-1.10), cannot suppress live-browser QA on a browser project (AC-1.5) ✓; static walkthrough performed and recorded above, zero parser hits ✓; no protected structure changed ✓. **Done.**

---

## Entry 2 — the fourth occurrence, observed live (T10's motivation)

- **Why this entry exists:** `skills/spark/SKILL.md` was **not** in `spec.md` NFR-2's enumerated surface. The user added it at the plan gate on 2026-08-29 after the negotiation it causes fired **during this very feature's own `/sprint-plan` ceremony** — the fourth occurrence of the same exchange. Recorded here as observation, not as argument.
- **Date:** 2026-08-29, at the start of `/sprint-plan` for `right-sizing`.

**What `/spark:69-72` instructs** (pre-change text, verbatim):

> "**Gather QA prerequisites early.** Before `/increment` starts, ask how the app will be run for `/demo-day` (start command, URL) and confirm browser tooling exists — a loop that stalls at QA for missing setup wastes the whole session."

**What the orchestrator consequently said to the user** (verbatim, this session):

> "**QA-Voraussetzung** — dieses Repo hat keine App, also läuft `/demo-day` wieder über die dokumentierte Override-Methode (wie bei `graph-gates`, `handbook-maturity`, `graph-gates-verification`). Das ist zum vierten Mal dieselbe Verhandlung — und exakt das, was US-1 abschaffen soll."

**The prior three, for the count:** `graph-gates` (`qa.md` §1, documented ceremony override), `lean-rounds` (`release.md`, `/demo-day` cancelled outright by user decision, no `qa.md` exists), `graph-gates-verification` (`qa.md` §1, override method again). This session is the fourth — and the first where the negotiation is traceable to `/spark`'s own instruction rather than to `/demo-day`'s.

**Consequence, and why the scope was extended:** with `/spark` left untouched, S1 ("zero per-feature negotiation of the QA method") would have been unmet at the loop's most common entry point — the feature would have failed its own success signal in the exact scenario that motivated it. The user's ruling extends NFR-2's enumerated surface to `skills/spark/SKILL.md`; `spec.md` is deliberately **not** edited (it is `approved`, and not `/increment`'s to change). Recorded in `plan.md` §1 Context, §1 Alternatives (row 7, "Overruled") and §2.

**Change made (T10):** `/spark` step 2 gains a conditional clause — with a complete declaration the orchestrator names the method in one line and asks nothing; absent, incomplete or `yes` behaves exactly as today; `/spark` never writes the declaration.

```
$ git diff --stat skills/spark/SKILL.md
 skills/spark/SKILL.md | 7 +++++++
 1 file changed, 7 insertions(+)
$ git diff skills/spark/SKILL.md | grep '^-' | grep -v '^---'
(no output)
```

**7 insertions, 0 deletions** — the four lines carrying today's behaviour are byte-identical, so the absent/incomplete/`yes` branch is not a re-implementation of today's prompt but literally today's prompt.

**DoD check (T10):** step 2 carries both branches ✓; the absent/incomplete/`yes` branch is byte-for-byte today's behaviour, proven by a zero-deletion diff ✓; nothing in `/spark` writes to the constitution — its only §8 mention is the read at line 74 ✓; the live fourth occurrence quoted above as this task's motivation ✓. **Done.**

---

## Entry 3 — DoD checks for T3–T7 (the reading and writing rules)

Each task's definition of done, checked against the file as shipped. These are
**file-content checks** — commands run against the working tree — not ceremony
runs; the behavioural evidence is Entry 4.

**T3 — `agents/qa-tester.md` step 1.**

```
$ grep -c 'a QA report based on code reading is fraud' agents/qa-tester.md
1
$ git diff agents/qa-tester.md | grep '^-' | grep -v '^---'
-1. **Check your equipment.** Confirm a browser tool is actually available and
```

The one deleted line is the step's opening, re-issued with the guard clause
`Unless the project declares a substitute QA method (next bullet),` in front of
it. The fraud rule survives verbatim **and** is restated inside the new branch
("a declared method is a different route to evidence, never a licence to read the
source and call it tested"). The branch carries: proceed without a per-feature
override (AC-1.1); `qa.md` still produced, one row per AC and per NFR under its
own `AC-`/`NFR-` ID (AC-1.2); §1 Test Environment cites §8 in place of
URL/browser/viewport; incomplete **or** unperformable → STOP and return the
missing item to the caller (AC-1.9, AC-1.6); read-only, `/charter` is the sole
writer (AC-1.10). **DoD met.**

**T4 — `/go-live` + `agents/release-manager.md`.** Both files state the citation
form and the absent-case wording. The §1 pre-flight item is untouched — the rule
opens "The check never changes: `qa.md` status must be `passed`, on every
project, at every value of anything", and `templates/release-notes.md` is not in
the diff at all. Gate integrity, checked across the whole diff:

```
$ git diff -U0 | grep -E '^[+-].*GATE'
(no output)
```

No gate line is added, removed or reworded anywhere. **DoD met.**

**T5 — `/charter` + `agents/facilitator.md`.** `skills/charter/SKILL.md` step 3
surfaces §8 as its own explicit decision with the evidence found, and states that
a profile with no `website`/`web-app` "is *evidence* for the question, never the
answer to it". `agents/facilitator.md` step 3 requires the draft be marked as
needing the user's confirmation and forbids deriving it from profile or lens
state; its Hard Rules gain "created and amended **here and nowhere else**".
**DoD met.**

**T6 — US-2 block in both reading agents.**

```
$ for f in agents/reviewer.md agents/qa-tester.md; do
    grep -c '(a) this round is verifying a fix' $f
    grep -c '(d) you have a concrete reason to doubt it' $f
    grep -c 'capped at `Minor`' $f
    grep -c 'bounded reading, never' $f
  done
1 1 1 1   (agents/reviewer.md)
1 1 1 1   (agents/qa-tester.md)
```

Identical block in both: all four AC-2.2 conditions verbatim, the
name-the-triggering-condition rule (AC-2.3), and the artifact-wording cap at
`Minor`, never gate-blocking (AC-2.4). Worded as bounded reading —
"**bounded reading, never 'don't verify'**" — not as permission to skip.
AC-2.5 is met by omission and that omission was checked, not assumed:

```
$ git diff agents/ | grep -iE '^\+.*(pre-existing|older artifact|legacy|migrat)'
(no output)
```

Neither agent gained any instruction that treats an artifact written before this
change differently. **DoD met.**

**T7 — `README.md`.** Requirements line now ends "— unless the project's
constitution declares a substitute QA method, which `/charter` sets once for a
project that has no browser-observable surface"; §Project Status gains one row,
**Shipped, dogfooded on this repo only**. The row claims no line, token or dollar
saving, and explicitly scopes the result to this repo: "It removes one recurring
per-feature question on a project that has no browser surface; it makes no other
loop shorter and is not claimed to" (NFR-5). **DoD met.**

---

## Entry 4 — the negative case, run first (T8)

**Precondition — no declaration exists anywhere in this repo.** T9 has not run;
this is the only window in which the negative case is honest.

```
$ grep -n 'QA Method' .spark/constitution.md
(no output)
$ grep -rn 'Browser-observable surface' .spark/
.spark/right-sizing/plan.md:21   (plan prose describing the template)
.spark/right-sizing/plan.md:53   (T1's task text)
.spark/right-sizing/plan.md:62   (T9's task text)
```

Three hits, all of them this feature's own plan *describing* the field. Zero
declarations. `.spark/constitution.md` has no §8.

### 4.1 What changed in today's behaviour — every deletion in the diff

```
$ git diff --stat
 10 files changed, 153 insertions(+), 6 deletions(-)
$ git diff | grep '^-' | grep -v '^---'
-**Requirements:** ... (Claude in Chrome, or a Playwright / Chrome DevTools MCP server).
-1. **Check your equipment.** Confirm a browser tool is actually available and
-   will carry several lenses (no cap, just visibility).
-   - Confirm browser tooling is available (Claude in Chrome, Playwright MCP,
-     what to set up or start. **Never substitute code reading for testing.**
-   exactly as before this feature existed. First pass: fresh
```

Six deleted lines across ten files. Every one is a line **re-issued in place,
extended**, not a behaviour removed:

| Deleted line | What replaced it | Effect when no declaration exists |
|---|---|---|
| README Requirements | same sentence + "unless … declares a substitute QA method" | doc only |
| `qa-tester` step 1 opening | same sentence behind `Unless the project declares a substitute QA method (next bullet),` | guard is false → the browser check runs unchanged |
| `charter` step 3 tail | same sentence + the §8 decision | `/charter` asks one more question; no other ceremony sees it |
| `demo-day` browser-tooling bullet | same bullet behind `Unless §8 declared a performable substitute method above,` | guard is false → STOP-on-missing-tooling unchanged |
| `demo-day` "Never substitute code reading for testing." | same sentence + "that holds for a declared method too" | strengthened, never weakened |
| `go-live` step 2 tail | same sentence + how §8 words the §1 QA row | absent → "worded exactly as today, with no mention of it" |

`skills/spark/SKILL.md`, `agents/reviewer.md`, `agents/release-manager.md`,
`agents/facilitator.md` and `templates/constitution.md` are **pure insertions** —
zero deletions. For those five files the absent-case path is not a
re-implementation of today's prompt; it is byte-for-byte today's prompt.

### 4.2 The four absent-case branches, quoted as shipped

Each reader states its own no-declaration branch. Quoted from the working tree
(*this is a reading of the shipped instruction text — see 4.5 for what that can
and cannot prove*):

- `/spark` step 2 — "Absent, incomplete, or `yes` → ask exactly as above, and say
  nothing about the declaration."
- `/demo-day` step 1 — "**No constitution, no §8, or `Browser-observable surface:
  yes`** → continue **exactly as today**: run the browser check below unchanged
  and say nothing about the declaration. No error, no warning, no mention." and,
  for the incomplete case, "also **exactly as today**: run the browser check and
  ask the user. Ambiguity resolves toward more verification, never less."
- `agents/qa-tester.md` step 1 — the branch is reached only "If the caller passed
  one, or `.spark/constitution.md` §8 `QA Method` declares one"; otherwise the
  equipment check is the unmodified one.
- `/go-live` step 2 + `release-manager.md` step 3 — "With no constitution, no §8,
  or an incomplete §8, word the row **exactly as today** and say nothing about
  the declaration."

No branch emits an error, a warning, a migration prompt or a mention.

### 4.3 Old-shape artifacts read under the new rules

Two pre-existing artifacts, written long before this change, read directly
(AC-2.5). *Note: `plan.md`'s T8 names `.spark/graph-gates-verification/`, which
does not exist in this repo — see the Deviations note in `plan.md`. The
old-shape artifacts actually present were used.*

```
$ sed -n '1,20p' .spark/graph-gates/qa.md      # Status passed, dated 2026-07-26
$ sed -n '1,20p' .spark/lean-rounds/review.md  # Status passed, Round 3, 2026-08-20
```

`.spark/graph-gates/qa.md` is doubly old-shape: it carries **no `Round` row**
(pre-dating that convention) and its §1 is the hand-written "⚠ Documented
ceremony override" prose — the very negotiation US-1 exists to retire. Read
under the shipped rules, nothing asks for it to be migrated, rewritten or
flagged; the added blocks contain no instruction that mentions an artifact's age
or shape at all (grep in Entry 3, T6, zero hits). `.spark/lean-rounds/review.md`
reads the same way. **No migration, no rewrite, no warning.**

### 4.4 Gate integrity — all six gates, before and after (NFR-6)

```
$ for f in templates/{spec,plan,review-report,qa-report,release-notes}.md; do
    before=$(git show HEAD:$f | awk '/^## ✅.*GATE/{f=1} f&&/^- \[ \]/{c++} END{print c+0}')
    after=$(awk '/^## ✅.*GATE/{f=1} f&&/^- \[ \]/{c++} END{print c+0}' $f)
    ...
```

| # | Gate | Checklist items before | after | Section diff |
|---|---|---|---|---|
| 1 | `✅ SPEC GATE` (`templates/spec.md`) | 11 | 11 | IDENTICAL |
| 2 | `✅ PLAN GATE` (`templates/plan.md`) | 10 | 10 | IDENTICAL |
| 3 | `✅ REVIEW GATE` (`templates/review-report.md`) | 7 | 7 | IDENTICAL |
| 4 | `✅ QA GATE` (`templates/qa-report.md`) | 7 | 7 | IDENTICAL |
| 5 | `✅ KEEP GATE` (`templates/release-notes.md`) | 6 | 6 | IDENTICAL |
| 6 | the publish go (`/go-live` step 4) | — | — | IDENTICAL |

Each section was diffed whole against `HEAD`, not merely counted:

```
$ diff <(git show HEAD:$f | sed -n '/^## ✅.*GATE/,$p') <(sed -n '/^## ✅.*GATE/,$p' $f)
templates/spec.md: IDENTICAL
templates/plan.md: IDENTICAL
templates/review-report.md: IDENTICAL
templates/qa-report.md: IDENTICAL
templates/release-notes.md: IDENTICAL
publish go: IDENTICAL
```

Because every gate section is **byte-identical**, item count, item wording and
the named owner of each are unchanged by construction — there is no wording left
in which an owner could have moved. The sixth gate is the user's publish
authorization in `/go-live` step 4; T4 edited step 2 of that file only, and step
4 diffs clean. **NFR-6 holds.**

### 4.5 What this entry does *not* prove — the honest limit

Sections 4.1, 4.3 and 4.4 are **performed checks**: real commands, real output,
against the real tree. Section 4.2 is a **reading of the shipped instruction
text**, and per this file's Rule it is labelled as such — it proves what the
prompt now says, not what a fresh session does with it.

**Corrected after round 1 of `/peer-review` (finding F3).** What this section
first claimed was wrong, and the correction matters more than the original point.

The original claim was that this session's own `/spark` step 2 was a live
negative-case observation which "cuts against a clean result" — that the
orchestrator skipped the ask and mentioned the declaration, and that the cause
was a contaminated venue. That reading was mistaken. Ceremonies load
`${CLAUDE_PLUGIN_ROOT}`, which resolves to the **installed plugin cache**, not
this working tree:

```
$ ls -d ~/.claude/plugins/cache/aspark/aspark/*/
.../0.5.0/  .../0.6.0/  .../0.7.0/          # newest installed: 0.7.0
$ grep '"version"' .claude-plugin/plugin.json
  "version": "0.7.1",                        # the working tree
$ grep -c 'QA Method' ~/.claude/plugins/cache/aspark/aspark/0.7.0/skills/spark/SKILL.md
0
$ grep -c 'Cite what a predecessor already established' \
    ~/.claude/plugins/cache/aspark/aspark/0.7.0/agents/reviewer.md
0
```

The `/spark` this session executed was **0.7.0's**, which contains no §8 clause
at all — T10's text was never in play. So the orchestrator did not deviate from
the shipped absent branch; it followed a *different, older* instruction that has
no such branch. The observation is therefore **not evidence about the shipped
text in either direction**, and the "contaminated venue" explanation was an
error on this file's part.

The real and larger consequence: **no ceremony in this session has executed any
line of this diff.** That is true of `/increment` (which is the developer, not a
prompt-driven reader), of round 1's `/peer-review` — which ran 0.7.0's
`reviewer.md` and so proved nothing about US-2 — and it would be true of
`/demo-day`, whose declared method under constitution §8 is explicitly "hands-on
QA against the **installed plugin**". `plan.md` §4's claim that US-2 "is verified
by this feature's own loop … the only live proof available" has been corrected in
place for the same reason.

**AC-1.3 therefore still has no live venue**, and its evidence rests on 4.1's
zero-semantic-deletion result plus 4.2's reading of the shipped text. A live
negative *and* positive case both require this branch to be installed as the
plugin. The user has taken that on; until it is done, nothing here may be
described as dogfooded, and `README.md`'s status row was corrected to match
(finding F7).

### 4.6 `claude plugin validate`

```
$ claude plugin validate .
Validating marketplace manifest: /Users/andreaslottes/aSPARK/.claude-plugin/marketplace.json
⚠ Found 1 warning:
  ❯ autoUpdate: Unknown field 'autoUpdate'. Claude Code ignores it at load time.
✔ Validation passed with warnings
EXIT=0
```

**Green.** The single warning is pre-existing and outside this diff —
`.claude-plugin/marketplace.json` is not among the ten changed files.

**DoD check (T8):** each reader's no-declaration branch quoted ✓ (4.2, labelled
as a text reading); old-shape artifacts read with zero warnings ✓ (4.3); six-gate
before/after table showing identical gates, items and owners ✓ (4.4);
`claude plugin validate` green ✓ (4.6). The one gap — no clean live venue for
AC-1.3 — is stated in 4.5 rather than papered over. **Done, with 4.5 noted.**

---

## Entry 5 — the positive case, behind the user (T9)

### 5.1 The amendment, written by `/charter` on the user's explicit confirmation

The Facilitator's discipline was followed: the declaration was drafted **only
from evidence that can be named**, and put to the user as its own decision, never
inferred from the profile or from `ux`/`seo` being off (AC-1.8).

Evidence named in the draft, all of it commands run against the real tree:

```
$ git ls-files | sed 's/.*\.//' | sort | uniq -c | sort -rn
  72 md
   5 yml
   4 png
   2 json
   1 gitignore
   1 docx
   1 LICENSE
$ ls package.json pyproject.toml Cargo.toml go.mod bin
none of package.json, pyproject.toml, Cargo.toml, go.mod, bin
```

The user was shown the drafted §8 in full and asked to confirm, amend the
wording, or decline. **They chose "Confirm — write it"** (2026-08-29). The
declaration and an Amendments-log row recording that confirmation are now in
`.spark/constitution.md`. The method itself is not invented here: it is the one
`.spark/graph-gates/qa.md` §1 established, with its strict definition of a
performed step, promoted from a per-feature override to a standing project fact.

**AC-1.10 held throughout:** no ceremony other than `/charter` wrote it. T1–T8
had shipped the readers days ahead of any declaration existing.

### 5.2 The declaration resolves — and the three fall-backs do not

The shipped branch conditions were mechanized into a throwaway resolver and run
against the real constitution plus four constructed fixtures. **This is not
shipped surface, is not in the diff, and lives only in the session scratchpad**
(constitution §3 forbids a toolchain; §6 Out of Scope forbids shipping a
validator — neither is what this is). It shows *which branch each input selects*;
it does not and cannot prove that a reader obeys the branch it lands on.

```
$ python3 resolve.py
this repo (real, post-amendment)       -> COMPLETE (method: hands-on QA against the **installed...)
                                          => declared path IF this session can perform it; else STOP
(a) AC-1.5 yes-surface project         -> surface='yes'
                                          => today's behaviour unchanged; no value can suppress live-browser QA
(b) AC-1.9 incomplete                  -> INCOMPLETE (surface=no, no method named)
                                          => fall back to today's: ASK the user - never suppress
(c) AC-1.6 unperformable method        -> COMPLETE (method: manual sign-off by the hardware QA lab...)
                                          => declared path IF this session can perform it; else STOP
(d) no §8 section                      -> ABSENT (no §8)
                                          => today's behaviour: ask / run the browser check, say nothing
(e) no constitution at all             -> ABSENT (no constitution)
                                          => today's behaviour: ask / run the browser check, say nothing
```

| Case | AC | Required outcome | Observed | |
|---|---|---|---|---|
| this repo | AC-1.1 | declared path, no per-feature override asked | `COMPLETE` → declared path | ✓ |
| (a) | AC-1.5 | a browser project is unaffected; no value suppresses live-browser QA | `surface='yes'` → today's behaviour, **even though the fixture also names a substitute method** | ✓ |
| (b) | AC-1.9 | incomplete → ask, never suppress | `INCOMPLETE` → ask the user | ✓ |
| (c) | AC-1.6 | unperformable → stop and say so | parse reaches the performability check, which is where the shipped text says STOP | partial — see below |
| (d), (e) | AC-1.3 | exactly as today | `ABSENT` → today's behaviour | ✓ |

Fixture (a) is the load-bearing one for AC-1.5: it declares `surface: yes` **and**
names a substitute method, and the declared path is still not taken. A stray or
mis-typed method value cannot suppress live-browser QA.

Fixture (c) is honestly **partial**. Whether a named method is performable in
this session is a reader's judgment, not something a parse can decide; the check
proves only that such a declaration parses as complete and therefore reaches the
performability question. The STOP itself rests on the shipped wording — "**Surface
`no`, method named, but this session cannot perform it** → **STOP** and name the
part you cannot perform. A declaration is a route, never a licence to skip"
(`/demo-day` step 1) and its twin in `agents/qa-tester.md` — which is instruction
text, labelled as such per this file's Rule, not a performed outcome.

### 5.3 What T9 does *not* yet show — and where it lands

T9's definition of done also asks that `evidence.md` show **the QA phase actually
proceeding by the declared method** with every AC and NFR verified under its own
ID, and **`release.md` §1 citing the constitution**. Neither has happened: at the
time of writing, this feature has not reached `/demo-day` or `/go-live`. Both are
the next two ceremonies of this very loop, and this repo is now a declared
project, so they are the live venue — the first QA phase in aSPARK's history to
run against a standing declaration rather than a hand-written override.

Marked **not run** here rather than asserted. `/demo-day` and `/go-live` write
their own artifacts (`qa.md`, `release.md`), and those, not a promise recorded in
advance, are the evidence. If either departs from the declared path, the finding
belongs to that phase.

**No volume claim is made anywhere in this entry** (NFR-5): nothing here counts
lines, tokens or dollars, and nothing claims the result generalizes beyond this
repo.

**DoD check (T9):** `.spark/constitution.md` carries §8 written at `/charter`
with the user's confirmation recorded in the Amendments log ✓; the three
fall-back cases shown against real fixtures — (a) and (b) fully, (c) partially
with the limit stated ✓; QA phase proceeding by the declared method and
`release.md` §1 citing the constitution — **not run**, they are the next two
ceremonies (5.3) ✓ recorded honestly. **Done, with 5.3 outstanding by design.**

---

## Entry 6 — the venue, established (review finding F3, first half)

F3's blocking half was that ceremonies load `${CLAUDE_PLUGIN_ROOT}` — the
installed plugin — and the installed plugin was not this branch. Resolved by
committing the branch and repointing the marketplace at the working tree.

**Correction to what Entry 4 and Entry 5 implied about staleness.** The
installed `0.7.0` was *not* behind on committed work. Measured before the
change:

```
$ for f in agents/reviewer.md agents/qa-tester.md skills/demo-day/SKILL.md; do
    diff <(git show 085db99:$f) $CACHE/$f | grep -c '^[<>]'   # cache vs committed HEAD
    diff $f $CACHE/$f | grep -c '^[<>]'                        # cache vs working tree
  done
agents/reviewer.md:        cache-vs-HEAD=0   cache-vs-worktree=16
agents/qa-tester.md:       cache-vs-HEAD=0   cache-vs-worktree=66
skills/demo-day/SKILL.md:  cache-vs-HEAD=0   cache-vs-worktree=39
```

Zero drift against committed `main`. The entire gap was **this feature's own
uncommitted work** — so the `0.7.0` vs `0.7.1` version difference was a version
bump, never a content lag, and re-installing from GitHub would have changed
nothing. Recorded because the earlier framing of F3 invited the wrong inference.

**What was done:**

```
$ git commit                                   # 47f6040, 15 files, tree clean
$ claude plugin marketplace add /Users/andreaslottes/aSPARK
✔ Successfully added marketplace: aspark (declared in user settings)
   source: {'source': 'directory', 'path': '/Users/andreaslottes/aSPARK'}
$ claude plugin update aspark@aspark
✔ Plugin "aspark" updated from 0.7.0 to 0.7.1 for scope user. Restart to apply changes.
```

`claude plugin install aspark@aspark` was a no-op ("already installed"); the
source change only takes effect via `update`, and only with the
marketplace-qualified name — plain `update aspark` fails with "Plugin not
found".

**Verified, not assumed:**

```
$ CACHE=~/.claude/plugins/cache/aspark/aspark/0.7.1
$ grep -c 'Cite what a predecessor already established' $CACHE/agents/reviewer.md      -> 1
$ grep -c 'no ceremony gains an off switch at any value' $CACHE/templates/constitution.md -> 1
$ grep -c 'QA Method' $CACHE/skills/spark/SKILL.md                                     -> 1
$ grep -c 'A QA report without performed steps is invalid' $CACHE/skills/demo-day/SKILL.md -> 1
$ diff -rq $CACHE/agents    aSPARK/agents      -> agents/: IDENTICAL
$ diff -rq $CACHE/skills    aSPARK/skills      -> skills/: IDENTICAL
$ diff -rq $CACHE/templates aSPARK/templates   -> templates/: IDENTICAL
```

**F3 is NOT closed by this entry.** The venue now exists; nothing has yet
executed it. The CLI itself says *"Restart to apply changes"*, and the session
that ran this install was still serving `0.7.0`'s skills — the `/peer-review`
invocation in it carried the base directory `.../aspark/0.7.0/skills/peer-review`.
F3 closes only when a ceremony **runs** under `0.7.1`: the next `/peer-review`
after a restart, which is also US-2's first live venue and the point at which
`plan.md` §4's corrected claim becomes checkable.

**Standing consequence for the rest of this loop:** the installed plugin is a
*copy* taken at update time, not a live view of the working tree. Any further
edit to `agents/`, `skills/` or `templates/` desynchronises it and requires
`claude plugin update aspark@aspark` plus a restart before it is exercised again.
Edits confined to `.spark/` do not.

---

## Entry 7 — the first ceremonies to actually execute this diff

Entry 6 established the venue but proved nothing had run in it. This entry
records the first ceremonies that did. Both are **live observations**, not
readings of instruction text.

### 7.1 `/spark` step 2 under the declaration (AC-1.1, at the orchestrator)

The resumed `/spark` loaded from `.../aspark/0.7.1/skills/spark` — its own
skill header says so, where the previous session's said `0.7.0` — and its step 2
carried T10's clause. `.spark/constitution.md` §8 is complete
(`Browser-observable surface: no` plus a named method).

**Observed:** the orchestrator asked for **no** start command, **no** URL and
**no** browser tooling. It named the declared method in one line ("QA läuft als
Hands-on-Prüfung gegen das installierte Plugin. Nichts zu verhandeln.") and
continued. No override was negotiated with the user.

**This is the orchestrator half only, and it is not AC-1.1.** AC-1.1
(`spec.md:118`) requires that "when the loop reaches the QA phase, then
**`/demo-day`** proceeds by the declared method" — `/demo-day` has not run, so
AC-1.1 is **not yet met** and belongs in §7.4's not-run list, not here. What was
performed is T10's clause in `/spark`, which is the counterpart to Entry 2's
fourth-occurrence recording: the negotiation Entry 2 caught happening for the
fourth time did not happen a fifth. Corrected after review round 3 (finding
F16); the original wording claimed the AC outright. Note the further limit —
this is one observation on one project, the same project that wrote the rule. It
is not evidence that the clause generalizes.

### 7.2 `/peer-review` round 2 under the US-2 rule (US-2's live venue)

Round 1 ran `0.7.0`'s `reviewer.md`, which carries no US-2 rule — that was
finding F3. Round 2's Reviewer verified its own venue rather than accepting the
caller's word, and reported the check as decisive:

```
installed_plugins.json  -> aspark@aspark at .../cache/aspark/aspark/0.7.1,
                           gitCommitSha 47f60402…
known_marketplaces.json -> source: directory, path: /Users/andreaslottes/aSPARK
diff -rq cache vs tree  -> agents/ skills/ templates/ lenses/ tools/
                           .claude-plugin/plugin.json  all identical
grep -c 'Cite what a predecessor already established'
    0.7.0/agents/reviewer.md -> 0
    0.7.1/agents/reviewer.md -> 1
```

It found `lenses/`, `tools/` and `.claude-plugin/plugin.json` identical too —
**three paths more than Entry 6 claimed**, so Entry 6 understated its own
result. It also corrected Entry 6's "12 files" for commit `47f6040` to **15**
(`git show --name-only`), which is finding F14, fixed in place.

**US-2 observed live, with its limit stated.** The Reviewer cited predecessor
artifacts where it could and named the AC-2.2 condition each time it went back
to source — (a) for verifying the claimed fixes, (d) for the venue claim it had
concrete reason to doubt. That is AC-2.1 and AC-2.3 performed. Facts re-derived
**without** a named condition: **zero**.

The Reviewer immediately qualified that number, and the qualification belongs
here rather than only in its report: AC-2.2(b) exempts every Must AC's
verification, and this feature is all-Must, so on *this* feature S2 is
satisfiable almost by construction. **The zero is real but nearly uninformative
here.** Raised as an open question for the PO/EM, not resolved by this evidence.

### 7.3 A regression this loop caught, recorded rather than buried

F1's round-1 fix removed a false claim about `/go-live` and introduced a false
one about `/spark`, in `agents/facilitator.md` — the file that explains §8 to the
user at `/charter`. Round 2 caught it as **F12** and rated it Major, the same
class as the defect it replaced. Fixed by naming all three readers explicitly
(the QA phase, `/spark`, `/go-live`); a repo-wide grep for the old claim returns
zero. Unconfirmed until round 3 checks it.

### 7.4 Still not run

**AC-1.1** — `/demo-day` proceeding by the declared method (§7.1 performed only
the `/spark` half). **AC-1.2** — `qa.md` produced by that method with every
`AC-`/`NFR-` ID verified. **AC-1.4** — `release.md` §1 citing the constitution.
Those are `/demo-day` and `/go-live`, and they remain the outstanding half of
Entry 5 §5.3.

**Venue caveat carried forward:** the installed plugin is a snapshot. F13 and
F12's fixes have desynchronised it again — `claude plugin update aspark@aspark`
plus a restart must run before `/demo-day` performs §8's "QA against the
installed plugin", or QA would test superseded text.

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

---

## Entry 8 — a trap in §8's own method: `update` is version-gated

Recorded because it silently defeats the QA method this feature declares, and
it will recur on every future feature that QA's against the installed plugin.

After committing the spec amendment and its one obliged clause (`22673c8`), the
documented refresh step from Entry 6 **refused to do anything**:

```
$ claude plugin update aspark@aspark
✔ aspark is already at the latest version (0.7.1).
```

`update` compares the **version string**, not the content. `plugin.json` still
read `0.7.1` — the same value the previous commit carried — so the update was a
no-op even though the working tree had moved two commits on. Verified rather
than assumed:

```
$ grep gitCommitSha ~/.claude/plugins/installed_plugins.json
  "gitCommitSha": "47f60402…"          # the PREVIOUS commit
$ git log --oneline -1
  22673c8 fix: name /spark in every file that enumerates …
$ grep -c '/spark still runs every step' $CACHE/templates/constitution.md
  0                                     # F15's clause absent from the cache
$ diff -rq $CACHE/agents agents; diff -rq $CACHE/templates templates; …
  facilitator.md, qa-tester.md, templates/constitution.md, demo-day/SKILL.md differ
```

**Why this matters here specifically.** Constitution §8 declares QA is performed
"against the **installed plugin**". Had this gone unnoticed, `/demo-day` would
have tested superseded text while reporting, accurately by its own lights, that
it tested the installed plugin — a QA report that is false without anyone
lying. The declaration makes the *installed* artifact the object under test, so
keeping it current is part of performing the method, not housekeeping around it.

**The workaround, and why this one.** Neither `update` nor `install` offers a
force or reinstall flag (`--help` on both). Bumping `plugin.json` would have
worked, but version selection belongs to the Release Manager at `/go-live`
(constitution §5 requires a **minor** bump here — `0.8.0`), so pre-empting it
from `/increment` would have been the wrong call. Uninstall-then-install
sidesteps the version comparison without touching the version:

```
$ claude plugin uninstall aspark@aspark   -> ✔ uninstalled
$ claude plugin install aspark@aspark -y  -> ✔ installed
$ grep gitCommitSha …installed_plugins.json -> "22673c8dc238ae13…"   # current HEAD
$ grep -c '/spark still runs every step' $CACHE/templates/constitution.md -> 1
$ diff -rq agents / templates / skills  -> ALL IDENTICAL
```

**Standing correction to Entry 6.** Entry 6's carried-forward instruction
(`claude plugin update aspark@aspark` plus a restart) is **insufficient whenever
the version string has not changed**, which is the normal case mid-feature. The
reliable step is uninstall + install + restart, and the check that it worked is
`gitCommitSha` against `git log --oneline -1` — not the CLI's success message,
which was cheerfully green while doing nothing.

**Out of scope, flagged not fixed:** whether §8 should say how the installed
artifact is kept current is a `/charter` question, and whether the release notes
should warn consumers is `/go-live`'s. Neither is this diff's business.

---

## Entry 9 — correcting Entry 8's freshness check (it can pass falsely)

Entry 8 told the reader to confirm a refreshed install with
`gitCommitSha` against `git log --oneline -1`. **That check is not sufficient,
and this entry exists because the fix round after `/demo-day` r1 proved it.**

Refreshing the install with three **uncommitted** modifications in the tree
(`agents/qa-tester.md` carrying B1's fix among them):

```
$ git status --short
 M .spark/right-sizing/evidence.md
 M .spark/right-sizing/spec.md
 M agents/qa-tester.md          <- B1's fix, uncommitted
?? .spark/right-sizing/qa.md
$ claude plugin uninstall aspark@aspark && claude plugin install aspark@aspark -y
$ grep -c '"Nothing" is literal' $CACHE/agents/qa-tester.md
1                                <- the UNCOMMITTED fix is in the cache
$ grep gitCommitSha …installed_plugins.json
  "gitCommitSha": "22673c8dc238…"
$ git log --oneline -1
  22673c8 fix: name /spark in every file …
$ diff -rq $CACHE/agents agents; …/templates; …/skills
ALL IDENTICAL
```

**Two facts, and the second is the trap.** First, a `directory`-source install
copies the **working tree**, not the commit — so no commit is required to
refresh it, and Entry 6's and Entry 8's implicit "commit first" was never a
precondition, only good hygiene. Second, and this is the correction:
`gitCommitSha` records **HEAD at install time, not what was copied.** With
uncommitted work in the tree those two are different things, and the field
reports the commit while the cache holds something else. It would read
"current" for a tree that had moved well beyond HEAD.

**The reliable check is content, not metadata:**

```
diff -rq $CACHE/agents agents && diff -rq $CACHE/skills skills && diff -rq $CACHE/templates templates
```

`gitCommitSha` may be quoted as context; it must never be the thing a freshness
claim rests on. Entry 8's own conclusion — "the check that it worked is
`gitCommitSha` against `git log --oneline -1`" — is **superseded by this entry**.
Entry 8's substantive finding stands unchanged: `claude plugin update` is
version-gated and silently no-ops when the version string has not moved, so
uninstall + install remains the reliable refresh.

Recorded because this feature's whole subject is not claiming more verification
than was performed, and a freshness check that can pass falsely is exactly that
failure wearing a command prompt.

---

## Entry 10 — a wording fix failed; the mechanism was the bug (B1)

Recorded because it is a real methodological lesson, not because the loop
requires an entry per fix attempt.

**Round 1** found B1: on a project declaring nothing (or `yes`), the QA Tester
still mentioned the declaration. **The round-1 fix added a reinforcement
sentence** — `**"Nothing" is literal."**`, spelling out five things not to do.
**Round 2 re-tested it live, 3/3, and it did not work.** The agent still opened
with "there is no §8 QA Method declaration to resolve" — a sentence the
reinforcement explicitly forbade, immediately after forbidding it.

**Diagnosis, not another wording pass.** The bullet's opening sentence —
"resolve it before the browser check above… Four outcomes…" — frames the
absent case as one of four things to *resolve and report on*, no matter how
firmly a later sentence tells the model not to narrate that resolution. Adding
words to the "don't narrate" side of a structure that already primes narration
was fighting the frame with more frame.

**The r3 fix restructures instead of reinforcing:** the §8 check is now a
silent precondition, stated and disposed of *before* the four-branch structure
even begins — "before reading any further in this bullet, silently check…
if the answer to any part is no… stop reading this bullet… There is no branch
to narrate here." The three named-method branches are reached only once a real
declaration is confirmed present; the absent case never enters the same
sentence as "outcomes to resolve."

**Deliberately not propagated.** The identical "say nothing" rule exists
verbatim in three more files — `skills/demo-day/SKILL.md`, `agents/
release-manager.md`, `skills/spark/SKILL.md` — none touched by either fix
round, and all three remain `not-verified-live` because the nested `claude -p`
session cannot authenticate in this environment (OAuth session expired,
reproduced in both QA rounds). Copying an unconfirmed mechanism into three more
files before confirming it works even once would be r2's mistake at triple the
scale. Confirm here; propagate only once confirmed — and even then, propagating
without a live test on those three files would itself be a claim this feature's
whole discipline forbids.

---

## Entry 11 — an artifact contradicted its own gate, one ceremony after the last

Round 3's `qa.md`, as first written, claimed `Status: passed` while its own QA
GATE checklist had **three open boxes** and one **checked** box asserting
something false: "No open Blocker or Major bugs (Minor bugs listed and
accepted by the user)" was `[x]` while B4 sat `open, unaccepted` two lines
below it in the same file. This is the identical defect class as F1/F12/F15
(review) — an artifact saying something its own body contradicts — now found
inside a QA report rather than a review report. Recorded because the pattern
recurring in a *different* ceremony, written by a *different* agent, is worth
knowing: self-contradiction is not particular to one role's writing habits.

**Reconciled, not silently overwritten** — the fix (routed through the user,
who chose to fix B4 and correct the checklist rather than accept or hand it
back for self-correction):
- **B4** (a "narrate every step" prompt made the agent announce a silent
  check occurred, without disclosing its content) — fixed structurally in
  `agents/qa-tester.md`: the rule now states explicitly that an instruction to
  narrate every step does not make this check a step to narrate, because on
  this path it was never one.
- **NFR-5's row** was flagged as included by mistake: `spec.md`'s own "How
  it's verified" column names `/peer-review`, not `/demo-day`, for NFR-5. It
  had been blocking a QA-owned checklist box for something that was never
  QA's to verify.
- **Two N/A boxes** (NFRs, viewports) had been left unchecked while a third,
  structurally identical N/A case (browser console) was checked — inconsistent
  handling of the same situation within one file.
- **The line-budget box** had been left unchecked despite recording a reason,
  when the template itself (`templates/qa-report.md:101`) offers two branches
  — "waived" or "recorded with a reason" — and this feature's own `review.md`
  round 3 already established checking `[x]` on the second branch as the
  correct reading. `qa.md` had not followed its sibling artifact's own
  precedent.

**Standing rule for future rounds of this feature, and worth carrying beyond
it:** before accepting a `passed`/`fixed`/gate-closed claim, cross-check the
gate checklist against the Handoff and the finding rows it summarizes — a
`[x]` box is a claim like any other line in the artifact, not exempt from the
verify-don't-trust discipline this feature exists to establish.

---

## Entry 12 — the spec was narrowed, and the fix stopped claiming what it could not prove

Direct continuation of Entries 10–11. Round 4's adversarial test (4 live runs,
all explicitly demanding full narration) found the round-3 restructuring
still leaking on 3/4 — one run **quoting actual §8 field content verbatim**,
one reproducing B4's placeholder pattern. That was the **third** distinct
fix attempt at the same requirement to fail under live testing:

| Round | Fix attempt | Result under its own test |
|---|---|---|
| 1 | reinforcement sentence ("Nothing is literal") | held 0 rounds — r2 found it leaking 3/3 |
| 3 | silent-precondition restructuring | held 2/2 in r3's own test; r4's harder test found a narrower leak (B4) |
| 4 | explicit "even under narrate-everything" clause | held 0/4 in r4's own test — the clause it added was itself immediately disproven |

Per this project's own standing discipline (constitution §1: negative case
first; the "three failed rounds" threshold the loop applies to `/peer-review`
extends in spirit here), three failed attempts at one requirement is a signal
to question the requirement, not to draft a fourth wording. Routed to
`/story-time` for a spec amendment rather than a fourth `/increment` attempt.

**The amendment (spec `C18`):** AC-1.3 and NFR-4 now guarantee silence under
**ordinary invocation** only, and state explicitly that a caller's same-turn
instruction to narrate all internal reasoning is **out of scope** — reasoned,
not asserted: no natural-language rule embedded in an agent's own definition
can be made robust against a contradicting explicit instruction in the same
turn. A candidate two-tier alternative (permit "a check occurred," still
forbid content disclosure) was considered and rejected for lacking evidence:
every one of round 4's four counted runs was itself narration-demanding, so
the record contains no case isolating one failure mode from the other.

**The fix that followed removes the disproven claim rather than layering a
fourth attempt on top of it.** `agents/qa-tester.md`'s "This holds even when
you are asked to narrate..." sentence — the exact claim round 4 falsified —
is deleted, not qualified further. In its place: an explicit statement of
what the guarantee covers (ordinary invocation) and what it does not
(an explicit narration demand), citing this evidence trail by entry number
so a future reader does not have to rediscover why the boundary is drawn
here. This is the same discipline as `evidence.md`'s own Rule — "anything not
run is labelled *not run*" — applied to a design claim inside shipped prompt
material: a scope that was not achieved is not claimed, worded around, or
buried under more words that also fail.

**Deliberately not done:** AC-1.5 (the `yes`-surface guarantee) makes a
different claim — never *suppressed*, not never *mentioned* — and held 2/2
under the identical round-4 adversarial test. The PO left it untouched and
flagged the asymmetry for the user rather than assuming consistency required
narrowing it too; the user did not ask for that narrowing.

**What this does and does not close.** B1 and B4 move to `fixed`
(`/increment`'s unconfirmed claim) reflecting the honest text. It does **not**
mean they are confirmed: both were reproduced only under narration-demanding
prompts the amended AC now places out of scope, so what remains to verify is
the **ordinary-invocation** case specifically — and the only prior clean data
for that exact case (round 3's single plain-prompt run) predates round 4's
edit to this same file, so it is stale evidence, not current confirmation.
`/demo-day` owes a fresh, clean, non-narration-demanding test before either
finding can be marked confirmed.

---

## Entry 13 — the requirement itself was wrong, not the fifth wording of it

Direct continuation of Entry 12. Round 5 tested exactly the case `C18`'s
narrowing claimed would hold — an ordinary QA request, zero narration
demanded — and found **0/2 clean**, one run quoting the raw declaration field
verbatim, unprompted. This is a harder failure than round 4's: round 4 needed
an adversarial demand to leak; round 5 needed nothing.

**The diagnosis moved from "the wording isn't careful enough" to "the
agent's role structurally conflicts with this requirement."**
`agents/qa-tester.md`'s Mission and Hard Rules pervasively demand exhaustive
self-documentation of every check performed ("no pass without performed
steps," "if you didn't see it, it didn't happen") — dozens of sentences
pulling toward transparency, all of them older and more central to the file
than the one new clause asking for silence about one specific check. Four
attempts tried to make that one clause win against a contradicting *live
instruction*; round 5 shows it was actually losing against the *agent's
entire prompt*, with or without any live instruction at all. No fifth wording
of a narrow exception was likely to reverse that.

**The repair went to the actual motivation instead.** US-1's own story text
(`spec.md:112-114`) says "so that I stop **re-negotiating** the same override
on every feature" — a claim about not having a live ask with the user each
cycle, never a claim about total silence in every output forever. AC-1.3 and
NFR-4 had generalized that motivation into a stronger claim than it required.
Spec `C19` (2026-08-31, superseding `C18`) re-scopes both to what the
motivation actually needs: **never ask, error, warn, or re-negotiate; stating
the fact in one's own words is explicitly fine**, symmetric with how the
declared path already documents its method in `qa.md` §1. Quoting the raw
declaration verbatim is discouraged but capped at `Minor` — a courtesy, not
the hard requirement.

**The fix that followed is a deletion, again, not a fifth addition.**
`agents/qa-tester.md`'s "silently check... produces zero output, always" and
the C18-era "scope of this guarantee" paragraph are both removed — not
qualified, not layered under more words — and replaced with what the rule
actually now requires: three concrete "never"s, one explicit "fine, not a
violation," and one "discouraged, not a Blocker." Because the guarantee is
now about an action (asking) rather than about content (mentioning), it no
longer depends on suppressing anything under narration pressure — the file
says so, and that claim is a structural consequence of the new rule's shape,
not a repetition of the disproven ones.

**Standing count, four fix attempts at one requirement, none surviving its
own confirming test until this one:**

| # | Approach | What broke it |
|---|---|---|
| 1 | reinforcement sentence | any neutral prompt (round 2) |
| 2 | silent-precondition restructuring | an adversarial narration demand (round 3's own harder test → B4) |
| 3 | explicit narration-immunity clause | four narration-demanding runs, 3/4 (round 4) |
| 4 | narrow the claim to ordinary invocation (`C18`) | the ordinary case itself, 0/2 (round 5) |

**What did not change, and should not be mistaken for progress on its own:**
this is still unconfirmed. B1/B4 are `fixed` against `C19`'s wording, not
against any test that has actually run — the favorable re-reading of round
5's own transcripts (neither venue asked, erred, warned, or negotiated) is a
citation under AC-2.2(a), stated as exactly that in `qa.md`'s Handoff, not
promoted into a pass. A sixth QA round, covering both ordinary and
narration-demanding invocation against the new rule, is still owed before
either finding can be trusted.

---

## Entry 14 — C19 held on the historically hardest case; a different path leaked

Round 6 tested the re-scoped, action-based rule (`C19`) under all four
combinations of {venue: absent declaration / `yes`-surface} × {invocation:
ordinary / narration-demanding}. **3 of 4 were clean, including the run that
broke every one of the four prior mechanisms** — narration-demanding
invocation on the bare venue. That is the first time this specific,
historically hardest condition has held.

**The one leak was not a repeat of B1/B4's failure mode.** It came from a
different branch entirely: the equipment check's STOP-and-report step, when
listing everything that would unblock it (missing browser tool, missing app
URL), volunteered *"a `.spark/constitution.md` §8 declaring an alternate QA
method... if browser testing genuinely doesn't apply here"* as one of three
options — on an **ordinary** invocation, no narration involved. This is a
subtler instance of the same underlying forbidden act (re-negotiation), not a
new category: **suggesting** a substitute-method declaration as a way out is
still asking the user to consider supplying one, phrased as help rather than
a question. Filed as **B5**, Blocker, per `C19`'s own "Never" list.

**Fixed by naming the leak at its actual source**, not by adding a general
reinforcement: the STOP-and-report instruction in `agents/qa-tester.md` now
states explicitly that reporting the missing tool/URL means naming it and
nothing more, and that suggesting a declaration as an unblocking option is
itself the forbidden re-negotiation. This is a third distinct location in the
same file now carrying a C19-shaped constraint (the silent-check branch from
Entry 13, and this STOP branch) — worth naming so a future reader does not
assume the guarantee lives in one place.

**A second thing fixed this round, unrelated to B1/B4/B5 but the same defect
class this whole feature keeps finding (Entry 11):** `spec.md`'s own Handoff
and SPEC GATE checklist disagreed about whether C19 had been re-approved —
one said yes, the other said "not yet," both describing the same event. This
was `/increment`'s own error, introduced while walking the C19 gate, caught
by the QA Tester reading the artifact rather than trusting either line in
isolation. Corrected in place.

**What round 6 does and does not establish:** three of four conditions held
clean, and the mechanism's structural claim — that an action-based rule
should not depend on suppressing content, so a narration demand should not
defeat it — held on its hardest prior counterexample. That is progress this
feature's own discipline requires stating plainly, not just the failures.
It does not mean the requirement is now proven: B5 shows a fifth location
could still leak the same forbidden act, and B5's own fix is itself
unconfirmed until a further round tests it. Round 7 owes a fresh test
covering B5's specific path (a STOP-and-report with no app and no
declaration) under both invocation modes, plus a repeat of the four
combinations round 6 ran, before this requirement can be trusted as closed.

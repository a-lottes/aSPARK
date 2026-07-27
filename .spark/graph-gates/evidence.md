# Evidence: graph-gates

| | |
|---|---|
| **Feature** | `graph-gates` |
| **Purpose** | The dogfood record required by NFR-10. There is no test suite and none is possible (constitution §3/§4, spec A2) — this file *is* the verification. |
| **Rule** | One dated entry per run, stating the command run, the output seen and the outcome. **The negative case runs first and is recorded as having run first** (constitution §1, AC-1.4). Anything not run is labelled *not run*. |
| **Owner** | `/increment` (all 15 tasks, P-Q5) |

---

## The binding reading of AC-1.1

*Quoted verbatim from `plan.md` §2 so that no later run has to re-decide it. Every
AC-1.1 grep in this file targets exactly these two surfaces and no others.*

> "Zero occurrences of `aspark-graph` and `.aspark-graph`" is measured on exactly
> two surfaces: **(1)** the artifact the ceremony produced
> (`plan.md` / `review.md` / `qa.md`), and **(2)** the ceremony's user-visible
> output — what it said to the user. **Excluded:** the detection sub-step's own tool
> calls and file reads, because the probe command and the tool-file path
> unavoidably contain the string, and a spec that mandates a CLI probe (AC-2.3)
> cannot simultaneously forbid the probe from existing. Nothing else is excluded: a
> single word about the tool in the artifact or in the narrative of an absent-case
> run is a failure of NFR-5, not a measurement artefact.

Resolved by the user as P-Q1 on 2026-07-25 (plan.md §5, risk P1 — *resolved*).

---

## Entry 1 — pre-change baseline

**Date:** 2026-07-25 · **Task:** T1 · **Label:** `pre-change baseline`
**Venue:** `/Users/andreaslottes/aSPARK` (this repo)

This entry is written **before the first edit**. "The same steps as the pre-change
version" (AC-1.2) is only checkable against something written down beforehand.

### Base commit

```
fb6af66f5eff67497be419b8172a0b7224292d50   Bump version to 0.3.1
```

`.spark/graph-gates/plan.md` is untracked at this point; the pre-change plan is
committed as part of T11, which needs a committed base for its comparison.

### The zero-hit baseline (AC-1.1, NFR-5)

```
$ grep -rni -e aspark-graph -e "\.aspark-graph" skills/ agents/ templates/ lenses/ README.md
$ echo $?
1
```

**0 hits.** Exit 1 = no match. This is the spec's own founding observation (§1,
pain 1) and the number every negative-case run must return to on its two surfaces.

### Public-surface counts (NFR-2)

| Item | Pre-change count |
|---|---|
| Skills (`skills/*/`) | **10** |
| Agents (`agents/*.md`) | **7** |
| Lenses (`lenses/*.md`, excluding README) | **8** |
| Templates (`templates/*.md`) | **6** |
| `.claude-plugin/plugin.json` version | **`0.3.1`** |

NFR-2 requires skills and agents to still read 10 and 7 after the change.

### Pre-change ceremony step lists (AC-1.2)

Quoted from `git show HEAD:skills/<ceremony>/SKILL.md`. A post-change run must
perform these same numbered steps — the availability probe is a **sub-step inside
an existing step**, never a new numbered one.

**`skills/peer-review/SKILL.md`** — 5 steps

| # | Step |
|---|---|
| 1 | Check the gate |
| 2 | Delegate to the Reviewer |
| 3 | Present the report |
| 4 | Route the findings with the user |
| 5 | Close the gate |

**`skills/sprint-plan/SKILL.md`** — 6 steps

| # | Step |
|---|---|
| 1 | Check the gate |
| 2 | Delegate to the Engineering Manager |
| 3 | Relay questions |
| 4 | Present the plan |
| 5 | Iterate |
| 6 | Close the gate |

**`skills/demo-day/SKILL.md`** — 6 steps

| # | Step |
|---|---|
| 1 | Check the gates and the gear |
| 2 | Delegate to the QA Tester |
| 3 | Relay needs |
| 4 | Present the report |
| 5 | Route the outcome with the user |
| 6 | Close the gate |

### Pre-change artifact section headings (AC-1.2)

A post-change run must produce these same sections — no section added, none
renamed, none dropped.

**`templates/review-report.md`**

```
## 1. Scope
## 2. Plan Conformance
## 3. Findings
## 4. Requirements Traceability
## 5. What Was Checked
## 6. Verdict
## ✅ REVIEW GATE
```

**`templates/qa-report.md`**

```
## 1. Test Environment
## 2. Acceptance Criteria Verification
## 3. Exploratory Findings
## 4. Console & Network
## 5. Verdict
## ✅ QA GATE
```

**`templates/plan.md`** — recorded because T2 edits this file and AC-5.3 requires
the protected structures to survive byte-identical.

```
## 1. Architecture Decision
## 2. Affected Components
## 3. Task Breakdown
## 4. Test Strategy
## 5. Risks & Mitigations
## ✅ PLAN GATE
```

Task-table header row at `HEAD`, which AC-5.3 requires to stay byte-identical:

```
| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
```

### Tool state in this venue

| Fact | Value |
|---|---|
| `.aspark-graph/` directory present? | **Yes** — see the correction below |
| `.aspark-graph/graph.json` present? | **No** |
| `aspark-graph` on `PATH`? | **No** |
| MCP surface (`staleness` / `impact` tools) in session? | **No** |
| Resolved availability state | **Silent** — nothing at all |

> **Correction, 2026-07-25, during T5.** This entry first recorded
> "`.aspark-graph/` present? **No**". That was wrong. The directory *does* exist
> in this repo, holding a single orphaned `parse-cache.json` (`"entries": {}`,
> version `aspark-graph=0.5.0`, mtime 15:08) and **no `graph.json`**. It was not
> created by this build session and is left untouched pending the user's decision.
>
> It changes nothing about this venue's suitability — with the corrected predicate
> (deviation D2) the repo still resolves to **silence**, because `graph.json` is
> absent — but it exposed a real defect in the approved design, and the honest
> baseline is the corrected one above, not the original claim.

This is exactly the state AC-1.1 describes, which is why this repo is the venue for
the negative case. It is also why the Plan-phase `impact` slice is inert here: per
`EXTENSION_LANGUAGE` (`.py .ts .tsx .js .jsx .mjs .cjs .java .go .rs`) no file in
this Markdown-and-JSON repo gets a `File` node at all, so path notes here build
**zero** `implements` edges (plan.md §1, risk P8).

### Outcome

Baseline frozen. **T1 done.** No source file has been edited yet.

---

<!-- Later entries append below, newest last. Negative case (T5, T11) before any
     positive-case run (T12–T15). Each cross-repo entry must state the user's
     recorded go and how that repo was left. -->

---

## Entry 2 — conformance sweep (T10)

**Date:** 2026-07-25 · **Task:** T10 · **Method:** static verification + parser-in-the-loop
**Venue:** `/Users/andreaslottes/aSPARK`

Every check below was run, not asserted. Commands and outputs as observed.

### AC-4.1 — `gate_health` is not callable

```
$ grep -rc gate_health skills/ agents/          → 0 files with any occurrence
$ grep -c  gate_health tools/aspark-graph.md    → 1
```

The single occurrence is inside `## Not wired (deliberate)`, with its reopen
condition. It appears in **no** call instruction anywhere.

### NFR-7 — nothing mutating is instructed

```
$ grep -rnE '\b(aspark-graph (build|serve)|build_graph|pip install|npm install)\b' \
      skills/ agents/ tools/ templates/
```

Only the permitted *name-it-to-the-user* forms survive filtering ("Never run …",
"may be **named to the user**", "would build it"). No shipped file instructs an
agent to build, serve or install anything.

### NFR-2 — public surface unchanged

| | Baseline (T1) | Now |
|---|---|---|
| Skills | 10 | **10** |
| Agents | 7 | **7** |

The product name appears in exactly **three** files — the three wired skills —
and in **no** agent, template or lens:

```
skills/peer-review/SKILL.md
skills/sprint-plan/SKILL.md
skills/demo-day/SKILL.md
```

### AC-1.2 — step counts identical to baseline

| Ceremony | Baseline | Now |
|---|---|---|
| `/peer-review` | 5 | **5** |
| `/sprint-plan` | 6 | **6** |
| `/demo-day` | 6 | **6** |

The probe is a sub-bullet of an existing step in all three. No numbered step added.

### NFR-1 / AC-5.3 — the template contract holds

**Re-run 2026-07-26 (F13), against the shipped tree.** The figures below replace
the T10 originals, which were measured before the artifact-budget workstream was
folded in and no longer described the tree they certified.

```
$ git diff --stat templates/
 templates/plan.md          | 27 ++++++++++++++++++++++++++-
 templates/review-report.md |  5 +++++
 templates/spec.md          |  5 +++++
 3 files changed, 36 insertions(+), 1 deletion(-)
$ git diff templates/ | grep -E "^[+-].*(\| # \||## |^\+\| T[0-9])"
 (no output)
```

Three templates now change, not one — `spec.md` and `review-report.md` gained
budget comments. Not one table row, column heading, section heading or task ID
was touched **in any of the three**. The change is confined to HTML guidance
comments, which is exactly what AC-5.3 requires and what the sibling repo's
parser is blind to. *Superseded original:* `templates/plan.md | 22 +` alone.

### AC-5.1 / P5 — this plan's own path notes, through the real parser

Ran the consumer's actual `_files_note` over all 16 task cells of `plan.md`:

```
16 task cells checked · 0 violations
```

One `files:` keyword per cell, note last, no trailing punctuation, every path
resolving to a plausible repo-relative file. This is **parser-in-the-loop**
evidence, not a reading — the same method that caught F5.

### NFR-11 — attention budget

**Re-measured 2026-07-26 (F13).**

```
$ wc -l tools/aspark-graph.md tools/README.md
150  tools/aspark-graph.md   (cap 150)
125  tools/README.md
```

Within budget with **zero headroom** — exactly at the ceiling, not the 3 lines
the original T10 entry recorded at 147. The file grew during the T16 fix pass
(F7's query-input table, F8's return shape) and the round-2 F11 fix was written
line-neutral for this reason. **Any further addition to that file must displace
something**, which is risk P6's prescribed compression, and is why round 2 left
F12 (`ambiguous`) open rather than appending it silently. *Superseded original:*
`147 … (cap 150)`, "3 lines of headroom".

### F4 — does the probe surface a permission prompt naming the tool?

The T16 DoD asks for this and the original entry omitted it. Run on 2026-07-26 by
the orchestrator, in this repo:

```
$ command -v aspark-graph && echo runner=yes || echo runner=no
runner=no
$ test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no
graph=no
$ echo $?
0
```

Exit 0, both facts reported, fourth state ("say nothing at all") resolved
correctly — and `.aspark-graph/` **exists** here holding only `parse-cache.json`,
so this is also live corroboration of **D2**: the directory alone does not flip
the state, only `graph.json` does. **Honest limit:** whether Claude Code showed
the *user* a permission prompt containing the string `aspark-graph` cannot be
attested from inside the session; the command was executed without one surfacing
to the agent. The user-visible-prompt leg of F4 is therefore **not proven**. It is
recorded here as owed and belongs on `plan.md` §4's post-release checklist as a
**sixth** item — it is **not** on that list yet, and the list still reads five
(corrected by `/peer-review` round 3, which found this sentence asserting a
record that did not exist).

### P4 — the three probe bullets have not drifted

The canonical wording in `tools/README.md` was diffed against the copy shipped in
`skills/peer-review/SKILL.md`: **byte-identical**. `/sprint-plan`'s copy is
byte-identical to `/peer-review`'s. `/demo-day`'s differs in exactly the two
documented places — it opens "Only once **both** gates above have passed" (it has
two hard gates) and closes with the browser/app clause. That variation is named
in `tools/README.md`.

### Build health

```
$ claude plugin validate .
✔ Validation passed with warnings
  ❯ autoUpdate: Unknown field 'autoUpdate'
```

The warning is **pre-existing**, not introduced here — verified by stashing this
change and re-running against `HEAD`, where it also appears once.

### Version

`.claude-plugin/plugin.json`: `0.3.1` → **`0.4.0`**. Minor bump: a new optional
capability, no protected structure renamed or removed, no breaking change.

### Outcome

**T10 done.** All NFR checks pass. Nothing here depended on executing a ceremony,
so none of it is affected by F3.

---

## Entry 3 — negative case, by walkthrough and static check (T5, T11)

**Date:** 2026-07-25 · **Tasks:** T5, T11 · **Venue:** `/Users/andreaslottes/aSPARK`
**Method:** static verification + manual walkthrough of the written instructions

> **This entry precedes every entry that uses the graph.** That ordering is the
> constitution §1 requirement and AC-1.4, preserved in the form still available
> after F3: nothing is claimed about the tool being useful until it is on record
> that a project without it is untouched.

### Method, and its honest limit (F3)

`/peer-review` **was** executed in this session and produced a clean, silent run —
but that run executed the **installed `0.3.1` plugin cache**, which contains no
`tools/` directory and zero occurrences of the product name. Measured:

```
~/.claude/plugins/cache/aspark/aspark/0.3.1/skills/peer-review/SKILL.md  → 0 occurrences
/Users/andreaslottes/aSPARK/skills/peer-review/SKILL.md                  → 3 occurrences
```

**That run is therefore evidence about the old material, not this change.** It is
not counted here. What follows is a walkthrough of the *changed* instructions plus
static checks — labelled as such, never as a ceremony run.

### The state this repo actually resolves to

Running the shipped probe verbatim, in this repo, right now:

```
$ command -v aspark-graph >/dev/null 2>&1 && echo runner=yes || echo runner=no
runner=no
$ test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no
graph=no
$ echo $?
0
```

State 4 of 4: **no surface, no graph → say nothing.** Note this holds *despite* a
`.aspark-graph/` directory being present (Entry 1's correction) — the corrected
predicate from deviation D2 tests `graph.json`, so the orphaned cache does not
produce a false "available". A directory test would have resolved this repo into
the wrong state; this is the case that proves D2 was necessary.

Note also that the probe **exits 0** in this, the normal case (F4's fix). Nothing
in the gate step ends on a red command.

### Walkthrough, per ceremony

Each ceremony's step 1 was read and executed by hand against this repo.

| Ceremony | Hard gate first? | Probe result | What it emits | Tool path passed? |
|---|---|---|---|---|
| `/peer-review` | yes — plan-status STOP evaluated before the probe | state 4 | **nothing** | no |
| `/sprint-plan` | yes — spec-status STOP evaluated before the probe | state 4 | **nothing** | no |
| `/demo-day` | yes — review-status **and** browser/app STOP, both before the probe | not reached in a stopped run; state 4 otherwise | **nothing** | no |

All three carry the literal instruction `say nothing at all` in the absent branch,
and all three make the step-2 hand-over conditional (`If a tool resolved as
available in step 1`), so with no tool resolved no path is passed and the agent
receives exactly the pre-change invocation.

`/demo-day` additionally states that a run stopped on the browser or app gate
**never reaches the probe sub-step** — so AC-3.5 holds by ordering, not by
promise.

### Static confirmation from the other direction (P11)

A walkthrough is a generous judge, so it does not stand alone. The static sweep in
Entry 2 catches the same leak from the opposite side and independently confirms:

- the product name appears in **three** files — the wired skills — and in **no**
  agent, template or lens;
- step counts are 5 / 6 / 6, identical to the T1 baseline;
- `templates/review-report.md` and `templates/qa-report.md` are untouched, so the
  artifact a run produces has the same sections as before;
- no gate outcome anywhere is conditioned on tool state.

An instruction that is not in the file cannot be followed. Both directions agree.

### What this does NOT establish

Stated plainly, because it is the difference between this and a real proof:

- **AC-1.1 at ceremony level** — that a *live* absent-case run of the changed
  skill emits nothing. Walkthrough only. → post-release checklist, item 1.
- **AC-1.2 for a produced artifact** — no artifact was produced by the changed
  material, so "same sections as before" rests on the untouched templates rather
  than on a compared output.
- **AC-1.3** — verified by reading that no branch conditions a gate on tool state,
  not by observing a degraded state fail to affect one.

### Outcome

**T5 done. T11 done.** The absent-case behaviour is established as far as this
session can establish it, and its limits are named rather than implied. Entries
that use the graph may now follow.

---

## Entry 4 — consumer verification (T12, T13, T14, T15)

**Date:** 2026-07-25 · **Method:** parser-in-the-loop against the live tool
**Venues:** `~/aSPARK-graph` (read-only) and a purpose-built fixture in scratch

> **Nothing was written in `~/aSPARK-graph`.** Every call below is a read-only
> `query`. `git status` there shows only the pre-existing untracked
> `.spark/BACKLOG.md`. No user go was required because no writing command was run.

### T12 — every documented call form, run for real

| Documented | Observed | Verdict |
|---|---|---|
| `staleness` → `stale, files_checked, changed, missing` | `+ advice` | **mismatch — doc fixed** |
| `impact <file>` → `files[]` with `code_entities`, `affected_stories`, `affected_acs` | `+ found, unknown_files`; per-file `+ path, in_graph` | **mismatch — doc fixed** |
| `impact --diff <range>` | works; on this repo returns `files: []` with everything in `unknown_files` | ✓ (and a live P8 demonstration) |
| both `files` and `--diff` | `{"found": false, "reason": "bad_args", "message": "pass either files or --diff, not both"}` | ✓ |
| neither | `{"found": false, "reason": "bad_args", "message": "no files given …"}` | ✓ |
| `story_trace <US-n> --feature <f>` → ACs with `qa_checks`, `latest_result`; tasks with `code` | exactly that | ✓ |
| unknown story → `{"found": false}` | `+ reason: "not_found"` | **mismatch — doc fixed** |
| unbuilt graph → stderr + **exit 1** | `exit=1`, stderr `No graph found at .aspark-graph/graph.json` | ✓ |

Three mismatches found and corrected in `tools/aspark-graph.md`. The most valuable
was **`unknown_files`** — undocumented, and it is the field that distinguishes
*"I do not index these"* from *"nothing depends on these"*. It is now documented
with that reading, which strengthens AC-4.5's caveat rather than merely restating it.

**A correction to my own first measurement.** An initial check appeared to show
`exit=0` for the unbuilt case, contradicting the documented exit 1. That was a
pipeline artefact — `$?` had captured `head`, not the tool. Re-run with redirection
instead of a pipe, the real exit code is **1**, and the documentation was right.
Recorded because the wrong reading nearly became a "finding".

### T13 — the stale path, from source and live

`queries.py::staleness` compares **sha256 content hashes**, not mtimes:

```python
digest = hashlib.sha256(path.read_bytes()).hexdigest()[:16]
if digest != node.get("hash"): changed.append(rel)
```

Two consequences, both of which corrected planned work:

1. **The tool file said `staleness` reads "file mtimes". It does not.** Corrected
   to "content hashes of indexed files".
2. **The plan's own live-check method was wrong.** T13 specified inducing
   staleness with `touch` — "an mtime change only, no content edit". A `touch`
   leaves the hash identical, so `stale` would have stayed `false` and the check
   would have silently proved nothing. The method was abandoned, not executed.

**Live corroboration arrived without any action of ours.** A separate session the
user started (the aspark-graph filename fix) created a worktree under
`~/aSPARK-graph/.claude/worktrees/`, changing indexed files. The graph, unbuilt
since, now reports:

```
stale         : True
files_checked : 98
changed       : ['.claude/worktrees/…/src/aspark_graph/artifacts.py',
                 '.claude/worktrees/…/src/aspark_graph/build.py']
advice        : "Run 'aspark-graph build' to refresh the graph."
```

So the tool file's stale rule rests on observed behaviour. **AC-3.2's *ceremony*
behaviour** — say it once, cite nothing further, still reach a verdict — remains
**not proven** (F3); only its contract half is discharged here.

*Incidental, not ours to fix:* the graph indexes files inside `.claude/worktrees/`,
so an agent worktree makes the parent repo look stale. Worth the graph repo knowing.

### T15 — the path note creates a `declared` edge

Done in a **purpose-built fixture** in scratch rather than by editing the user's
repo — same proof, nothing of theirs touched. Fixture: one `src/widget.py`, one
`spec.md` with `US-1`/`AC-1.1`, one `plan.md` with a single task.

**With** `— files: src/widget.py` in the DoD cell:

```
story_trace  T1 code links : [{confidence: 'declared', id: 'file:src/widget.py', type: 'File'}]
impact       affected_stories: [{confidence: 'declared', story: 'US-1'}]
             affected_acs    : [{confidence: 'declared', ac: 'AC-1.1'}]
```

**Without** it, same fixture rebuilt:

```
story_trace  T1 code links : []
impact       affected_stories: []   affected_acs: []   unknown_files: []
```

That is A7's prediction reproduced as a controlled before/after, and it is the
evidence for US-5. Note the signature in the control: `unknown_files: []` **with**
`affected_stories: []` means the file *is* indexed and simply has no declared link
— exactly the empty-by-construction case the tool file now teaches an agent to
recognise.

### T14 — QA slice, walkthrough only

Walked the QA slice against the real `story_trace` output above. The slice tells
the agent to use the Story→AC→Task→Code legs for scoping, not to read
`qa_checks` / `latest_result`, and never to rest a `Result` cell on a tool answer.
All three are present in `agents/qa-tester.md` and `tools/aspark-graph.md`.

**AC-2.6 is not proven and will not be.** It needs a `/demo-day` run with a graph
*and* a browser surface; no such project exists (risk P3). Labelled here, in
`plan.md` §4 and in `README.md`. Not checked off.

### Outcome

**T12, T13, T14, T15 done.** Four documentation defects found and fixed by running
the real tool — three call-shape mismatches and one wrong claim about how staleness
is computed. One planned verification method (`touch`-induced staleness) was found
to be incapable of proving what it claimed and was dropped rather than performed.

---

## Entry 8 — QA venue prepared: the working tree staged as the installed plugin

**Date:** 2026-07-26 · **Phase:** Review (`/demo-day` prerequisite) · **Method:** environment change, verified
**Venue:** `~/.claude/plugins/cache/aspark/aspark/0.3.1` (staging) and `~/aSPARK-graph` (QA target)

This is the step F3 said was missing. Every criterion labelled *not proven* in
`plan.md` §4 carries the same cause — ceremonies execute the installed plugin
cache, not this working tree — so QA is only meaningful once the tree **is** the
installed plugin. **Authorised by the user on 2026-07-26**, after the same change
was declined during the build session (declining it then was right: it would have
made the round-1 and round-2 reviews unrepeatable).

### What was changed, and how it is undone

| | |
|---|---|
| **Backup** | `cp -a 0.3.1 0.3.1.bak` — 2.4 MB, taken **before** any write |
| **Change** | `skills/`, `agents/`, `templates/`, `lenses/`, `tools/`, `.claude-plugin/`, `README.md`, `LICENSE`, `docs/workflow.md` copied over `0.3.1/` |
| **Deliberately not changed** | `installed_plugins.json` — overwriting in place keeps the existing pointer valid, so no plugin *configuration* is touched. `.in_use` and `.spark/` in the cache were left alone |
| **Copy, not sync** | `git diff --name-status` shows **no deletions** in the increment, so nothing needed removing; `--delete` was avoided so `.in_use` could not be destroyed |
| **Reversal** | `rm -rf 0.3.1 && mv 0.3.1.bak 0.3.1`, or reinstall from the marketplace |

### Staging verified

```
version                     0.4.0        (was 0.3.1)
tools/aspark-graph.md       150 lines    (absent before)
probe bullets               skills/{peer-review,sprint-plan,demo-day}/SKILL.md + tools/README.md
skills / agents             10 / 7       (NFR-2 holds in the installed copy)
/spark numbered steps       8            (the D6 step is live)
.in_use                     intact
```

### QA target verified — and it is **stale**, which is useful

```
$ export PATH="$HOME/aSPARK-graph/.venv/bin:$PATH"
$ command -v aspark-graph   → /Users/andreaslottes/aSPARK-graph/.venv/bin/aspark-graph
$ test -f .aspark-graph/graph.json → graph=yes
$ aspark-graph query staleness --repo .
{ "stale": true, "files_checked": 98,
  "changed": [".claude/worktrees/…/artifacts.py", ".claude/worktrees/…/build.py"],
  "missing": [], "advice": "Run 'aspark-graph build' to refresh the graph." }
```

Both availability facts hold there, so the hand-over path is reachable — and
`stale: true` means the **stale branch** (AC-3.2: say it once, treat the graph as
absent, cite nothing further, still reach the verdict) is exercisable live, which
no session has done yet.

> **Fork for whoever runs QA.** Left stale, a run proves AC-3.2's behaviour but
> not the populated-answer path. Proving that needs `aspark-graph build` — a
> **write** in the user's other repo, which per T13/T15 needs their explicit go,
> recorded, and is *not* taken here.

### Honest limit — why this entry proves nothing on its own

Plugins load at session start. The session that staged this had already loaded
`0.3.1`, so **it cannot test the staged material**; every ceremony it runs is
still the old one. This entry records a prepared venue, not a result. It
discharges no criterion. `known_marketplaces.json` has `autoUpdate: true`, so the
first check in the fresh session must be that the staging survived the restart.

### Outcome

Venue prepared and verified. **No criterion discharged.** The QA run itself is
owed, in a new session.

---

## Entry 9 — QA round 1 run, and the venue defect it exposed

**Date:** 2026-07-26 · **Phase:** Review (`/demo-day`) · **Method:** live ceremony runs
**Report:** `.spark/graph-gates/qa.md` (status `in-testing`) · **Verdict:** FAIL

The QA run Entry 8 said was owed. Two environment changes were made, both under
the user's explicit authorization, and both are recorded here because Entry 8's
own honest limit — a prepared venue proves nothing — applies to them too.

### Change 1 — the graph was built (authorized)

`aspark-graph build` in `~/aSPARK-graph`. Before: `stale: true`, 98 files, 2
changed. After: `stale: false`, 100 files, 932 code entities, 276 artifact
entities, 68 inferred links. Pre-build backup kept outside the repo.

**Cost, recorded:** this removed the live `stale: true` condition, so **AC-3.2's
ceremony-side branch is no longer exercisable in that venue** and is marked
`not-verified-live` rather than passed. The tool-side half was covered instead in
a throwaway repo, which produced a finding worth keeping: a stale graph's
`impact` still returns `found: true` with a confident entity list that silently
omits newly added code — the precise failure mode AC-3.2 guards against.

### Change 2 — the runner was put on `PATH` (authorized, after the run)

QA established **B2**: in a fresh shell `~/aSPARK-graph` resolved
`runner=no, graph=yes` — the *hint* state, not Offer. The runner lived only in a
venv on no shell's `PATH`; Entry 8's `export PATH=…` was masking this. **No
ceremony had ever reached the Offer path**, which accounts for all seven
`not-verified-live` criteria, four of them Must (AC-2.4, AC-2.5, AC-2.6, AC-3.1).

Fix: `~/.local/bin/aspark-graph` → `~/aSPARK-graph/.venv/bin/aspark-graph`
(symlink; `~/.local/bin` was already on `PATH`; the console script's shebang is
absolute). Verified in a plain shell with no export: `~/aSPARK-graph` now
resolves `runner=yes, graph=yes`. Reversal: `rm ~/.local/bin/aspark-graph`.

**Cost, recorded — this is the neighbour the re-test must check.** The symlink is
global, so `~/aSPARK` moved from `runner=no, graph=no` (silent) to
`runner=yes, graph=no` (hint). **The negative venue no longer exists as a natural
state on this machine.** The negative-case evidence is already banked — it was
proven live this round by real `/peer-review` and `/sprint-plan` runs — but any
re-run of the negative case must first remove the symlink, not merely override
`PATH`, since overriding `PATH` is exactly the masking that hid B2.

### What this entry does and does not discharge

**Discharged live this round** (see `qa.md` for the full table): the negative case
by real ceremony runs — both ceremonies passed their gate, ran the probe,
resolved `no/no` and said nothing, with step counts identical pre/post — and
AC-4.4, which no prior session could test, by building a graph on a Core-managed
trail (`spec.md`/`plan.md`/`review.md`).

**Not discharged:** the Offer path, still unreached by any ceremony at the time
the report was written. Change 2 makes it reachable for the first time; proving
it is the next round's job.

### One correction to the record

The report's **B1** (writing the QA artifact as `qa-report.md` breaks
`aspark-graph build`, exit 1) was caused by the caller's instruction, not by the
increment: constitution §5 instantiates the artifact as **`qa.md`**. The file was
renamed and the breakage is gone, reproduced with a control both ways. The
residual parser mismatch (`_parse_qa` wants `AC`, the template ships `Spec ID`)
is the pre-existing consumer defect already logged on 2026-07-25 as the consuming
repo's to fix. B1 does not block the gate; **B2 does.**

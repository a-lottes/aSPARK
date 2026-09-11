# Evidence: metrics-script-removal

| | |
|---|---|
| **Phase** | Act (`/increment`) |
| **Owner** | Developer (the orchestrating session) |
| **Status** | `complete` |
| **Date** | 2026-09-11 |

**Handoff**
- **Status:** `complete` for `/increment`'s original 12 tasks, **extended** by three rounds of `/peer-review` fix-mode (Entries 1–9 are the original increment; Entry 10 is round 2 fix-mode; Entry 11 is round 3 fix-mode — round 1 fix-mode is folded inline into Entries 1–9 rather than appended). Entries are append-only; a superseded number is struck through in place, never deleted — round 3 applied that convention retroactively to Entries 4, 6 and 7, which round 1/2's fixes had superseded without it.
- **Summary:** The single evidence artifact for this feature. Holds the negative case, the figure derivations (run four times now: pre-strip, post-strip, after the round-1 rebase to three reports, and independently re-verified each round since), the recovery commit for the deleted script, the command sequences `/demo-day` must perform, and the self-inflicted drift three rounds of fix-mode produced, each smaller than the last, and closed (Entries 10–11).
- **Open:** `3` — `AC-1.3`/`AC-1.5` **by design**, both `/demo-day`'s (outside-repo writes, constitution §6); and **`F20`, deliberately not closed here** — whether this session had standing to edit an approved spec's NFR-3 (`C8`) without a fresh user re-approval. `spec.md`'s own Handoff states the question for the user directly.
- **Findings raised here, for `/peer-review`:** `AC-4.1` second clause **refuted-with-finding** (Entry 6, ruled as D1); `AC-1.2`'s literal command unsatisfiable by a path-prefix bug though its intent holds (Entry 7); `F-jq` (Entry 1) resolved by the user as deviation D6; one extra §3 hunk as D7. Two pre-existing observations left in scope's way deliberately: README's "10 skills, 7 agents, 6 templates" will rot, and `ROADMAP.md`'s Shipped row names baseline Core v0.7.0 against a live 0.8.0. **Spec edits made in fix-mode without a fresh user re-approval** (`C8`–`C10`, NFR-3 and three ACs): disclosed in `spec.md`'s Handoff, not equated with the constitution's `A8` authority — `F20` tracks this as open.
- **Binding ruling:** the derivation verdicts in Entry 3 are the **only** permitted source of figures for T6 and T10. A figure not in that table may not be published.
- **On conflict:** `plan.md` §3 wins on task status; this file wins on what was observed.

**Conventions.** Every block below is a real command and its real output, pasted
unedited. `$SCRATCH` stands for the session scratchpad, which is outside the
repository — no absolute path is recorded here (NFR-6). Commands were run from
the repository root unless stated.

---

## Entry 1 — T1, the negative case (before anything is deleted)

Run at `6fd257c`, on branch `feat/metrics-script-removal`.

Constitution §4 requires the negative case first: *"For a change that adds an
optional capability, the negative case runs first — in a repo where the
capability is absent, nothing may change."* The removal's equivalent is the
proof that **nothing in the consumed contract references what is being
removed**, established before the deletion rather than after it. This entry is
committed before T8's deletion commit, so `git log` itself carries the ordering.

### AC-1.4 — no ceremony references the script

```
$ grep -rln 'spark-metrics' skills agents templates lenses tools .claude-plugin
$ echo $?
1
```

Zero hits. `grep` exit 1 is "no lines selected", not an error.

Widened in the same pass to the directory itself, which the deletion also removes:

```
$ grep -rln 'scripts/' skills agents templates lenses tools .claude-plugin
$ echo $?
1
```

Zero hits. **No skill, agent, template, lens, tool file or manifest names the
script or its directory.** Therefore removing it changes no ceremony's behaviour
and owes no deprecation path — spec A6 confirmed, NFR-2 satisfied, and the
removal is not a breaking change to the consumed contract (§6).

### NFR-7 — the project validates before the work starts

```
$ claude plugin validate .
Validating marketplace manifest: .claude-plugin/marketplace.json

⚠ Found 1 warning:

  ❯ autoUpdate: Unknown field 'autoUpdate'. Claude Code ignores it at load time.

✔ Validation passed with warnings
$ echo $?
0
```

Passes. The `autoUpdate` warning is **pre-existing and unrelated** to this
feature — it concerns `marketplace.json`, which NFR-1 forbids this increment to
touch. Recorded as the baseline so that a reviewer can tell this warning apart
from anything this work introduces; it must still be present, unchanged, at T12.

### Baseline counts at `6fd257c`

| Measure | Command | Value |
|---|---|---|
| Tracked files | `git ls-files \| wc -l` | 106 |
| Tracked `.md` | `git ls-files '*.md' \| wc -l` | 89 |
| Tracked `.py` | `git ls-files '*.py' \| wc -l` | **1** |
| Script size | `wc -c < scripts/spark-metrics.py` | 32,654 B |

**Note for T9 (deviation D2 in action).** The constitution's §8 inventory was
written at `/charter` against 104 tracked files / 87 `.md`. This branch's own
`spec.md` and `plan.md` have since made it 106 / 89 — the inventory was already
stale two commits after it was written, which is exactly the drift D2 predicted
and the reason §8 will state its counts **with the commit they were taken at**
rather than as a live claim. The only time-invariant clause is `.py` = 0, which
stays live-verifiable.

### Finding F-jq — `jq` is absent on this machine (raised at T1, blocks T6)

The approved architecture publishes the method as `jq` one-liners
(`plan.md` §1), and T6's definition of done requires that *"every printed
command was pasted into a shell and its observed output recorded"* (NFR-4:
runnable exactly as printed **and observed to run**). `jq` cannot be observed
running here:

```
$ command -v jq
$ echo $?
1
$ for p in /usr/bin/jq /usr/local/bin/jq /opt/homebrew/bin/jq /opt/local/bin/jq ~/.local/bin/jq; do
>   [ -x "$p" ] && echo "FOUND $p" || echo "no $p"
> done
no /usr/bin/jq
no /usr/local/bin/jq
no /opt/homebrew/bin/jq
no /opt/local/bin/jq
no ~/.local/bin/jq
$ command -v brew
$ echo $?
1
```

Absent, and `brew` is absent too, so there is no one-line install. Constitution
§6 forbids installing anything on the user's behalf unasked, so `/increment`
must not resolve this itself. Interpreters that **are** present: `python3`
(3.9.6), `perl`, `ruby` (2.6.10), `node` (v24.18.0).

This is the condition the plan anticipated as risk **R3**, whose named fallback
is the per-project table from §1's rejected alternatives — carrying the flaw the
plan itself recorded against it ("it publishes a derived snapshot as the method
… a reader checking the table against the JSON is checking my transcription,
not the evidence"). Choosing between that fallback, installing `jq` with the
user's go, and a third option changes §1's architecture decision, so it was
**raised to the user rather than decided here** (`/increment` does not improvise
architecture). T2–T5 do not depend on the answer and proceeded; see Entry 2.

---

## Entry 2 — T2/T3, every published figure derived (pre-strip)

Derivation ran from the session scratchpad (`$SCRATCH/derive.py`, Python 3
stdlib, **never committed, never written into the repository**). Proof it stayed
outside: `git status --porcelain` during the run showed only `plan.md`'s task
status column.

The four combination rules were read off `scripts/spark-metrics.py` before its
deletion, not invented:

| Rule | Source in the removed script | What it does |
|---|---|---|
| Union projects on `projects[].id` | `:662-664` | a repository cloned on two machines is one project |
| OR `reached.*` per `(project id, feature key)` | `:662-664` | a phase counts as reached if either machine saw it |
| **Max per project**, then sum, for `git.tags/added/deleted` | `:646-648` | two clones report the same history; the smaller number is a clone that is behind |
| Sum `transcripts.*` counters, **union** `days[]` | `:689-706` | a session elsewhere is another session; the same calendar day is not |

### Result: 23 of 23 figures reproduce exactly

```
FIGURE                    | PUBLISHED    | DERIVED      | VERDICT
-----------------------------------------------------------------------
projects                  | 10           | 10           | MATCH
features                  | 54           | 54           | MATCH
spec reached              | 54           | 54           | MATCH
plan reached              | 53           | 53           | MATCH
review reached            | 52           | 52           | MATCH
qa reached                | 41           | 41           | MATCH
release reached           | 48           | 48           | MATCH
naive feature sum         | 65           | 65           | MATCH
git tags                  | 61           | 61           | MATCH
git added                 | 114630       | 114630       | MATCH
git deleted               | 12589        | 12589        | MATCH
projects with line counts | 7            | 7            | MATCH
projects reporting n/a    | 3            | 3            | MATCH
sessions aspark           | 42           | 42           | MATCH
sessions total            | 114          | 114          | MATCH
role-agent runs           | 429          | 429          | MATCH
human gate decisions      | 377          | 377          | MATCH
active days               | 51           | 51           | MATCH
window start              | 2026-07-13   | 2026-07-13   | MATCH
window end                | 2026-09-08   | 2026-09-08   | MATCH
agent breakdown           | reviewer 108 | reviewer 108 | MATCH
ceremonies total          | 116          | 116          | MATCH
ceremony breakdown        | spark 35 / n | spark 35 / n | MATCH


23 figures checked, 0 mismatch(es)
```

**T3's verdict: every figure `reproduced`. No figure is `refuted`, none is
corrected, none is dropped.** Per this file's Handoff ruling, this is the only
permitted source of figures for T6 and T10.

Two things worth naming, because the spec expected otherwise:

- **AC-2.5's tags figure reproduces at 61.** The spec recorded `52 + 27 = 79`
  against a published `61` and treated the dedup rule as untested, with
  refutation the likely path. The rule exists and is statable: max per project,
  then sum. Per-project tags are `[0, 1, 2, 3, 5, 8, 9, 9, 12, 12]`, summing to
  61. The `79` was a naive sum across machines, which is not what the figure ever
  claimed to be. **The refutation path stayed open through this run and did not
  need to be taken** — recorded as a confirmed figure, not as a near-miss.
- **One apparent mismatch was mine, not the data's.** The first run reported a
  `MISMATCH` on the per-agent breakdown because the expected string in the
  scratch script abbreviated the role names (`po`, `rm`, `em`) while the reports
  spell them out. Every number in that breakdown matched on the first run
  (`reviewer 108 · product-owner 103 · release-manager 63 ·
  engineering-manager 61 · qa-tester 59 · designer 24 · facilitator 11`, summing
  to 429). The comparison string was corrected and the run repeated to reach
  `0 mismatch(es)`. Recorded rather than quietly re-run, so the 23/23 above is
  not mistaken for a first-try result.

---

## Entry 3 — T4/T5, the leaked paths stripped and the figures re-proven

### T4 — `transcripts.root` removed from both committed reports

The field held an absolute home directory in each report, in a **public**
repository, while `docs/reports/README.md:27` claims *"Opaque ids and counts. No
project name, no feature name, no hostname, no path."* Before:

```
$ grep -n '"root"' docs/reports/*.json
docs/reports/m-2e80b1d428827c8d.json:663:    "root": "<a home directory>/.claude/projects",
docs/reports/m-aef31f2de543f46c.json:272:    "root": "<a second, different home directory>/.claude/projects",
```

(The two values are quoted here with the paths elided on purpose — recording them
verbatim in a tracked public file would re-commit what this task removes.)

After, with the diff confined to exactly that line in each file:

```
$ git diff --stat docs/reports/
 docs/reports/m-2e80b1d428827c8d.json | 1 -
 docs/reports/m-aef31f2de543f46c.json | 1 -
 2 files changed, 2 deletions(-)
```

Verification (AC-5.1, AC-5.3, NFR-6):

```
$ grep -rn '/Users/' docs/ | wc -l
0
$ grep -rn '"root"\|/Users/\|hostname' docs/reports/*.json | wc -l
0
$ for f in docs/reports/*.json; do python3 -m json.tool "$f" > /dev/null && echo -n "ok "; done
ok ok
```

So `docs/reports/README.md`'s claim is now true as written, and both files remain
valid JSON. The round-trip preserved key order and indentation, which is why the
diff is two deletions rather than a reformat of 900 lines.

### T5 — AC-5.2: no published figure depended on the removed field

The derivation from Entry 2 was re-run **verbatim** against the edited reports
and the two outputs diffed:

```
$ diff -u $SCRATCH/run1-prestrip.txt $SCRATCH/run2-poststrip.txt
$ echo $?
0
```

**Empty diff.** All 23 figures unchanged, so stripping `transcripts.root` cost no
published number. AC-5.2 satisfied.

---

## Entry 4 — T6/T7, the method replaces the program

### T6 — `docs/metrics.md` rewritten: 254 → 242 lines

**Deviation D6 (authorised).** The approved architecture published the method as
`jq` one-liners. `jq` is absent on this machine and `brew` with it (Entry 1,
finding F-jq), so no printed `jq` command could satisfy NFR-4's *"runnable
exactly as printed **and observed to run**"*, and T6's own definition of done
requires every printed command to have been pasted into a shell. Raised to the
user rather than resolved here, because it changes §1's decision. **Ruled
2026-09-11: publish `python3` one-liners instead.**

The plan had rejected `python3 -c` as "re-creating the program inside a tracked
document". The ruling rests on three things that objection does not cover: the
removed script was 32,654 B of project discovery, transcript parsing, merging and
CLI, while each printed command is a `json.load` plus a set union — the same order
of complexity as the `jq` the plan blessed; §3's bar is no new tracked executable
*code*, and a fenced example command is not a file and is not shipped as code;
and decisively, **`python3` is present where `jq` is not**, which AC-2.2 depends
on — a stranger who must first install a tool is supplying a step of their own.

What the file ~~now~~ **at T6** carried: three commands (disk artifacts, git
history, transcript activity) — a fourth (per-agent/per-ceremony breakdown) was
added at round 1 fix-mode, F6; see Entry 10 — each with its observed output
printed beneath it, plus the four combination rules as a table. What it lost:
the flag table, the `--write-report` transport workflow, the merge-invocation
prose, and every sentence describing a program's behaviour.

### AC-2.1 / AC-2.2 — the printed commands were run *from the file*

Not "tested before writing". The three fenced blocks were **extracted from
`docs/metrics.md` itself** and executed verbatim, each output compared to the
output printed beneath it in the document:

```
$ python3 <extract-and-run, $SCRATCH>   # parses docs/metrics.md, runs each bash
                                        # block, diffs against the printed output
found 3 command/output pairs in docs/metrics.md

--- command 1: exit=0 match=YES
--- command 2: exit=0 match=YES
--- command 3: exit=0 match=YES

ALL PRINTED COMMANDS RUN AS PRINTED AND MATCH: True
```

So every figure in the document is reachable by copy-paste from the document, with
nothing supplied by the reader. `/demo-day` re-performs this independently (the
plan reserves AC-2.1/AC-2.2 to QA); this run is the builder's own evidence that
the commands are not aspirational.

**One command needed correcting before it would run**, recorded because it is the
reason NFR-4 demands observation rather than plausibility: the first draft of the
git-history command applied `max()` across *every* field of `projects[].git`,
which raised `TypeError: '>' not supported between instances of 'str' and 'int'`
on the `reason` field (`git.available: false` projects carry a prose reason, and
`adopted_at_root` is a bool). The published version names the three numeric fields
explicitly, which is both correct and clearer to a reader.

### T6/T7 — definition-of-done greps

| Check | Command | Result |
|---|---|---|
| No flag table (AC-3.3) | `grep -c '^\| \`--' docs/metrics.md` | 0 |
| No dead promises (AC-3.1) | `grep -c 'write-report\|Add yours\|should be refreshed\|Count your own' docs/metrics.md` | 0 |
| Same, reports README | same grep over `docs/reports/README.md` | 0 |
| No external-home pointer (AC-3.4) | `grep -ci 'aspark-insights' docs/metrics.md` | 0 |
| No script named as existing | `grep -c 'spark-metrics' docs/metrics.md docs/reports/README.md` | 0 |
| No absolute paths (NFR-6) | `grep -rn '/Users/' docs/ \| wc -l` | 0 |

`docs/metrics.md`'s `Related` section is gone entirely. It had existed to contrast
`aspark-insights` with "`spark-metrics.py` is deliberately smaller" — a sentence
about a file that no longer exists, and AC-3.4 forbids presenting that repository
as a place to get this counter. Removing the section satisfies both the AC's
wording and T6's stricter grep.

### T7 — `docs/reports/README.md`

The `git pull … --write-report … commit … push` workflow block and the
"Then, on any machine that has pulled them all" merge invocation are gone. In
their place the file states that the directory is a **closed ~~2026-09-09~~
2026-09-10** snapshot (the date moved at round 1 fix-mode, F1 — a third report
landed mid-increment; Entry 10), that this repository contains no tool to
produce another report, and points at `docs/metrics.md`'s ~~three~~ **four**
commands for re-deriving the figures from
what is committed.

Its "what is in a report" claim — *"Opaque ids and counts. No project name, no
feature name, no hostname, no path."* — is **kept unchanged and is now true**, per
T4's strip: `grep -rn '"root"\|/Users/\|hostname' docs/reports/*.json` returns 0.

---

## Entry 5 — T8, the script is gone, with a recovery path that survives any merge

### The recovery commit: `a2c0541`, already on `origin/main`

The plan's risk R2 warned that naming a *branch-local* commit would leave
README's provenance sentence pointing at an unreachable object if this PR is
squash-merged. That risk is closed rather than mitigated: the commit named is
`a2c0541`, which is already an ancestor of `origin/main`, so it is reachable
however this PR merges.

```
$ git merge-base --is-ancestor a2c0541 origin/main; echo $?
0
$ git show a2c0541:scripts/spark-metrics.py > <scratch>
$ wc -c < <scratch>
32654
$ cmp <scratch> scripts/spark-metrics.py
$ echo $?
0
$ git show a2c0541:scripts/spark-metrics.py | head -1
#!/usr/bin/env python3
```

Byte-identical to the deleted file, so `a2c0541` recovers the **final** version,
not an earlier one — `f446ca5` (the commit that added the script) holds a smaller,
earlier revision and is the weaker choice the plan had offered as fallback.

**A measurement artifact worth recording, since it nearly entered this file as a
figure.** An early attempt to compare blob sizes across candidate commits inside a
shell loop reported sizes of 1222–2073 B for a 32,654 B file. The cause was the
`<sha>:<path>` argument not surviving the loop's quoting, so `git cat-file -s` was
reporting *commit object* sizes rather than blob sizes. The numbers above were
re-taken with one command per step and confirmed by `cmp`. No size figure in this
file comes from that loop.

### The deletion

Pre-deletion `HEAD` was `3fa75fa`.

```
$ git rm -r scripts
$ git ls-files '*.py' | wc -l
0
$ ls scripts
ls: scripts: No such file or directory
$ git ls-files | wc -l
106
```

`scripts/` is removed as a directory, not emptied (AC-1.1). The tracked total is
106: 106 at `6fd257c`, plus `evidence.md`, minus the script.

This commit lands **after** Entry 1's negative-case commit (`f5d546d`) — the
ordering constitution §4 requires, and `git log --oneline` is the proof rather
than this sentence.

---

## Entry 6 — T9, the constitution stops describing a script that does not exist

Four edits plus one Amendments row, in a single commit placed **after** T8's
deletion, so no commit exists in which §3 forbids a script that §8's inventory
still counts.

| # | Section | Before | After |
|---|---|---|---|
| 1 | Preamble | "It has no runtime, no build and no dependencies. One standalone Python 3 script … counts what the loop has produced … ruled for removal (§3)." | "It has no runtime, no build, no dependencies **and no executable code of its own**." The claim now stands unqualified |
| 2 | §2 `cli` row | "…no stdout/stderr or exit codes **that any consumer invokes**; … (the script does print to stdout, but it is hand-run maintainer tooling … ruled for removal — §3)" | "…no stdout/stderr or exit codes **of our own**" — the parenthetical is gone and the original justification is restored. Lens activation unchanged: `library` only, load 1 |
| 3 | §3 | The *Known open exception* paragraph | Deleted. §3's own instruction was "When the deletion lands, delete this paragraph" |
| 4 | §8 | "104 tracked files (verified 2026-09-11): 87 `.md` … 1 `.py` (…, ruled for removal — §3)" | "**Zero executable files** — `git ls-files '*.py'` returns nothing, and that clause is the one here that stays true as the repo grows, so verify it live rather than against the count below", then the inventory pinned to `db4ab15` |

### A fifth touch inside §3, recorded rather than slipped in

T9's definition of done said the exception paragraph goes and *"`git diff` shows
no other hunk inside §3"*. One more clause had to change, and leaving it would
have been worse than touching it. The sentence following the exception read:

> **No new tracked executable code is added** — not while the exception is open
> and not after it closes.

With the exception deleted, "while the exception is open" refers to nothing. It
now reads **"No new tracked executable code is added."** — the same rule with an
obsolete temporal qualifier removed, no scope change in either direction.
Recorded here as a deliberate deviation from that DoD clause; `/peer-review` owns
the ruling on whether it was the right call.

### AC-4.1 — `refuted-with-finding`

The criterion (`spec.md:94`) requires:

> - [ ] AC-4.1: Given the repo at the moment this feature's PR is opened, when
>   `grep -rn 'spark-metrics' . --include='*.md' | grep -v '/\.spark/[a-z-]*/'` is
>   run, then the only hits are past-tense provenance statements (AC-2.3), and
>   **`grep -n 'spark-metrics' .spark/constitution.md` prints nothing**.

The second clause **does not hold, and was ruled not to be made to hold.**

```
$ grep -n 'spark-metrics' .spark/constitution.md
296:| 2026-09-11 | §3 stack/runtime: **no exception — Markdown + JSON only stands**, with me…
```

One hit — the `2026-09-11` Amendments row opening "§3 stack/runtime: **no
exception — Markdown + JSON only stands**", added earlier today by `36a3f17`,
which records the very ruling this feature executes and names the file four
times in doing so. Every other occurrence is gone: the preamble, §2's `cli`
row, §3's exception paragraph and §8's inventory no longer mention it.
(Cited by content, not line number, after round 1 fix-mode (F9) corrected a
`:295`→`:296` drift and round 2 found the file had since moved the same row to
`:305` — a line number in this file is a snapshot of one moment, not a stable
address, and every subsequent edit above a cited line invalidates it again.)

**Cause.** The criterion was written on 2026-09-11 before that amendment row
existed, and the spec authorises four edits plus a *new* row (`A2`/`A8`) — it does
not authorise rewriting an existing one. Satisfying the clause literally would
mean editing the audit trail of a decision so that a grep comes out clean.

**Ruling.** Put to the user at the plan gate as deviation **D1** with the
alternative (scrub the historical row) stated explicitly. The user ruled
2026-09-11 to **leave the record intact and record the clause as refuted**. The
new row added by this task is worded without the literal string, so the count
stays at one and does not grow with each amendment.

**Not a defect in the work, and not a pass either.** The first clause of AC-4.1
holds (verified at T12); the second is refuted against the current file text with
the quote and `file:line` above. Per the project's `CLAUDE.md`, a documented
refutation is a valid ceremony outcome, and forcing a "confirmed" here would have
meant damaging the record to protect a checkbox.

### AC-4.2 — satisfied under deviation D2

§8 no longer makes a live total claim. The clause that **is** live-verifiable is
the one that carries the argument:

```
$ git ls-files '*.py' | wc -l
0
```

The pinned inventory is stated against ~~`db4ab15`~~ **`62b4318`** — `db4ab15`
was the pin at T9, but round 1 fix-mode reworded that exact commit (F7),
orphaning the reference; round 2 fix-mode re-pinned to the commit's new SHA
and re-took every count there. See Entry 10 for the full correction; the
transcript below is what was taken **at T9**, against `db4ab15`, and is kept
as the historical record rather than edited to match the current pin:

```
$ git ls-files | wc -l          # at db4ab15
106
$ git ls-files '*.md' | wc -l
90
```

D2's reasoning, now visible in §8 itself: this feature's own `review.md`, `qa.md`
and `release.md` are still to come, so any live total written today is wrong by
the time QA reads it. Pinning the total and live-checking the executable count
puts the durable claim where it can be tested and the perishable one where it
cannot mislead.

---

## Entry 7 — T10, the README headline stops rotting

`### Dogfooding to date` no longer opens with a number. The non-rotting claim is
that **the evidence is committed rather than asserted** — ~~two~~ **three**
machine reports in `docs/reports/` (a third landed on `origin/main` mid-round
and this branch rebased onto it — Entry 10), and ~~three~~ **four** `python3`
commands in `docs/metrics.md` (a fourth was added at round 1 fix-mode, F6)
that re-derive every figure from them, standard library only. That sentence
stays true however much time passes, because it describes what the repository
contains rather than
what the numbers currently are. The second paragraph states plainly what the
evidence cannot do: refresh itself.

Every figure moved inside `#### Snapshot` (dated ~~2026-09-09~~ **2026-09-10**
after round 1's rebase — Entry 10), introduced by a line carrying both the
date and the word *"evidence"*. The `scripts/` bullet is gone from the
repository-layout list (`README.md:210`).

### Definition-of-done greps

| AC | Check | Result |
|---|---|---|
| AC-7.1 | `grep -c '^\*\*54 features' README.md` | 0 — the numeric headline is gone |
| AC-2.3 | `grep -c '\-\-merge' README.md` | 0 |
| AC-3.1 | `grep -c 'write-report\|Add yours\|should be refreshed\|Count your own' README.md` | 0 |
| AC-3.4 | `grep -ci 'aspark-insights' README.md` | 0 |
| — | `grep -c 'spark-metrics' README.md` | 0 |

### AC-7.2 — the table sits inside the dated block

Transcript as taken at T10, against the date and figures live at the time
(2026-09-09, two reports). Both moved at round 1 fix-mode (F1); AC-7.2's own
criterion was generalised at round 2 fix-mode (F14, `C9`) to anchor on the
`#### Snapshot` heading text rather than a date string, specifically so this
transcript would not need retaking every time the date moves — see Entry 10
for the re-run against the current file and `C9`/`C10` in `spec.md`:

```
$ grep -n -A4 '2026-09-09' README.md
258:#### Snapshot — 2026-09-09
259-
260:Dated **evidence**, taken 2026-09-09 and not updated since:
261-
262-| Spec | Plan | Review | QA | Release | Git tags | Role-agent runs | Human gate decisions |
263-|---:|---:|---:|---:|---:|---:|---:|---:|
264-| 54 | 53 | 52 | 41 | 48 | 61 | 429 | 377 |
```

The line carrying the date also carried `evidence`, and the table followed
inside four lines — true then, and (re-verified in Entry 10) still true of
the current heading-anchored check.

### AC-7.3 — no count outside the dated block

Checked mechanically rather than by eye, with a deliberately **over-broad**
pattern: every sentence outside the block containing any numeral or number-word
within the same sentence as `project(s)`, `feature(s)`, `run(s)` or `day(s)`, in
both orders. Five candidates surfaced and all five are false positives on
inspection:

| Candidate | Why it is not a count of projects/features/runs/days |
|---|---|
| "The loop — 10 skills, 7 agents, 6 templates … all five gates enforced" | Counts skills, agents, templates and gates. Matched only because "run" appears in "end-to-end run" in the same sentence |
| "QA-method declaration … the fall-backs (absent, incomplete, unperformable, and a `yes`-surface project)" | An enumeration, no number attached to "project" |
| "It removes one recurring per-feature question on a project…" | "one … question", not one project or one feature |
| `#11` / `#9` in the issue-state paragraph | Issue numbers |
| "If you run aSPARK on yours, `#4`…" | Issue links |

So AC-7.3 holds as written. **One observation for `/peer-review`, not a
violation:** the Area/State table's "10 skills, 7 agents, 6 templates" *is* a
count that will rot if the plugin gains a skill. AC-7.3 does not cover it (its
list is projects, features, runs, days) and it is pre-existing text this feature's
scope does not reach, so it was left alone rather than quietly widened into.

### AC-2.3 — provenance

The section names `docs/reports/` as the evidence and commit `a2c0541` as the
recovery point, which Entry 5 proved both reachable on `origin/main` and
byte-identical to the deleted file.

### AC-1.2 — satisfied on intent; the literal command has a path-prefix bug

The criterion's command is:

```
grep -rn 'python3 scripts/' --include='*.md' . | grep -v '/\.spark/'
```

Run literally it returns **six** hits, not three as this entry first recorded —
corrected at `/peer-review` round 1 (F8, Minor). Three are load-bearing:
`spec.md:26` (quoting the invitation being removed), `spec.md:60` (AC-1.2
quoting its own command) and `plan.md:58` (T10's definition of done quoting it
again). The other three are this very file quoting the command below, to show
its own output — a count that grows every time this entry is read back into
itself, which is the honest reason the number is wrong in any draft that tries
to state it as a constant. The exclusion pattern requires a leading slash
before `.spark`, but this environment's `grep -r .` emits paths as `.spark/…`
rather than `./.spark/…`, so the filter never matches and none of the feature's
own artifacts — this one included — are excluded as intended.

The criterion's **intent** — no document outside the feature's own artifacts
instructs a reader to run the script — is satisfied, confirmed two independent
ways:

```
$ grep -rn 'python3 scripts/' --include='*.md' . | grep -v '\.spark/' | wc -l
0
$ git ls-files '*.md' | grep -v '^\.spark/' | xargs grep -n 'python3 scripts/' | wc -l
0
```

Recorded as a **wording defect in the criterion, not a defect in the work** —
the same class as AC-4.1 (Entry 6), and the second time a grep written ahead of
the artifacts it would later match has needed this treatment. `/peer-review` owns
whether the criterion or the record should carry the correction.

---

## Entry 8 — T11/T12, final sweep and the package `/demo-day` needs

### T11 — `ROADMAP.md`

"Close the handbook honesty exception" is removed from `## Next` (it was done at
`/charter` this morning), and this feature is listed there in its place. It moves
to `## Shipped` at `/go-live`, not here.

```
$ python3 - <<'PY'   # counts scoped to the ## Next section only
'handbook honesty exception' under ## Next : 0
script removal under ## Next              : 1
still mentioned anywhere in file          : 0
PY
```

**Pre-existing drift left alone, flagged for `/peer-review`:** `## Shipped`'s
handbook row names the baseline "Core v0.7.0 · graph v0.7.0" while Core is at
`0.8.0`. It understates rather than overstates, the plan recorded it as a
follow-up for the handbook revision, and it is outside this feature's scope.

### T12 — NFR-1: the consumed contract is untouched

```
$ git diff --name-status main
M	.spark/constitution.md
A	.spark/metrics-script-removal/evidence.md
A	.spark/metrics-script-removal/plan.md
A	.spark/metrics-script-removal/spec.md
M	README.md
M	ROADMAP.md
M	docs/metrics.md
M	docs/reports/README.md
M	docs/reports/m-2e80b1d428827c8d.json
M	docs/reports/m-aef31f2de543f46c.json
D	scripts/spark-metrics.py
```

No path under `skills/`, `agents/`, `lenses/`, `templates/`, `tools/` or
`.claude-plugin/`. NFR-1 holds, and with T1's zero-hit negative case, NFR-2's
"not breaking" holds too: nothing in the consumed contract referenced the deleted
file, so no consumer can have depended on it. `.claude-plugin/plugin.json` is
untouched — version stays `0.8.0` through Act (D3); the bump is `/go-live`'s.

### T12 — `claude plugin validate`, unchanged from the T1 baseline

```
✔ Validation passed with warnings
  ❯ autoUpdate: Unknown field 'autoUpdate'. Claude Code ignores it at load time.
```

Same single warning as Entry 1, on a file this increment does not touch — so the
increment introduced no new validation finding.

### T12 — AC-4.1 sweep: every remaining hit classified

```
$ grep -rn 'spark-metrics' . --include='*.md' | grep -v '\.spark/[a-z-]*/'
.spark/constitution.md:296:| 2026-09-11 | §3 stack/runtime: **no exception …
```

**One hit repo-wide.** It is the historical Amendments row, which D1 ruled stays.
Everything else that named the script is gone: `README.md` 0, `docs/metrics.md` 0,
`docs/reports/README.md` 0, and the constitution's preamble, §2, §3 and §8 all 0.
The remaining hits under the literal filter are this feature's own `spec.md`,
`plan.md` and this file — immutable artifacts recording what was decided, which
the criterion intended to exclude and does not (see Entry 7, AC-1.2).

---

## Entry 9 — the package `/demo-day` must perform

Two acceptance criteria are deliberately **not** verified here. Both write outside
the repository, and constitution §6 reserves that to the user's explicit go:
*"Nothing is executed or installed on the user's behalf unasked."* `/increment`
did not run them, and no result for them is claimed.

### AC-1.3 — the refreshed install carries no executable

**Ask the user first.** This writes into `~/.claude`. If the answer is no, record
AC-1.3 `not-verified-live` with that as the reason — which is an honest outcome,
not a failure.

```bash
# 1. state the starting point, so the refresh is provable rather than assumed
python3 -c "import json;print(json.load(open('$HOME/.claude/plugins/installed_plugins.json'))['plugins']['aspark@aspark'])"
#    expect gitCommitSha 9c47bc95… (v0.8.0, installed 2026-08-31) BEFORE the refresh

# 2. refresh the marketplace's own source tracking (this marketplace is a local
#    directory, so this syncs its metadata to the branch's current working tree)
claude plugin marketplace update aspark

# 3. re-install the plugin itself — step 2 alone does not do this; the installed
#    plugin is a separate cached copy that does not auto-follow the marketplace
#    source directory, so skipping this step is why the original sequence failed
claude plugin update aspark

# 4. prove the refresh actually happened — gitCommitSha must now equal branch head
git rev-parse HEAD
python3 -c "import json;print(json.load(open('$HOME/.claude/plugins/installed_plugins.json'))['plugins']['aspark@aspark'])"

# 5. the criterion itself
find "$HOME/.claude/plugins/cache/aspark/aspark" -name '*.py'
#    expect: no output
```

**Step 4 is the whole point.** Without it the `find` in step 5 is a tautology: the
installed cache predates the script, so "no `.py` present" is already true today
and proves nothing about this change. A listing taken before the `gitCommitSha`
moves is not evidence.

**Correction, `/peer-review` round 1 (F4, Major).** The sequence as first written
stopped at step 2 (`marketplace update`) and went straight to the `find` — with
no step that actually re-installs the plugin. The Reviewer did not run step 2
themselves (that is the same unasked-install action §6 bars `/increment` from,
and equally not theirs to perform); they read `~/.claude/plugins/installed_plugins.json`
as it already stood — `gitCommitSha 9c47bc95…`, `lastUpdated 2026-08-31`, both
still the pre-feature baseline recorded at T1 — and reasoned correctly that
`marketplace update` alone cannot be what moves that record, since it refreshes
the marketplace's own metadata, not the installed plugin copy. `claude plugin
update aspark` (step 3, per `plan.md` §4's own "re-install" wording, which the
first draft had named but not included) is the missing step, confirmed against
the CLI's own `--help` output rather than assumed. Without it, AC-1.3 would have
failed for an install-mechanism reason — exactly the false negative the original
step-3 note warned against, just one step earlier than it located the risk.

**Risk R1, and its remedy needs a second go.** No version bump happens in this
increment (D3), so the refresh lands in the same `…/aspark/aspark/0.8.0/`
directory. If the update **merges** into that directory rather than replacing it,
a stale `spark-metrics.py` can survive and AC-1.3 fails for an install-mechanism
reason that says nothing about the repository. The remedy is an uninstall and
reinstall — **also** outside the repo, so it needs the user's go again. If they
decline, record the observed state and the mechanism as a finding; do not record
the repo as failing a criterion it met.

### AC-1.5 — a fresh clone carries neither the script nor the ignored artifacts

Needs the branch pushed, which is itself an outward action needing the user's go.
Run it after `/go-live`'s push, or on the local repo as the origin.

```bash
git clone --branch feat/metrics-script-removal <repo> /tmp/ac15-clone
find /tmp/ac15-clone -name '*.py'
for f in 'docs/aSPARK_Enterprise_Architecture_Handbook.docx.bak' '.DS_Store' \
         '.claude/settings.local.json' '.aspark-graph/graph.json' '.aspark-graph/parse-cache.json'; do
  [ -e "/tmp/ac15-clone/$f" ] && echo "PRESENT $f" || echo "absent  $f"
done
rm -rf /tmp/ac15-clone
```

Expect no `.py` and all five `absent`. **What this does and does not settle:** it
settles what a **clone** carries. It claims nothing about what a GitHub
marketplace install carries — spec A9 records that as unverified, and the
follow-up feature named in spec §6 owns it. Do not let a clean result here be
written up as "consumers are unaffected".

### What QA re-performs that was already done here

AC-2.1 and AC-2.2 are QA's by the plan's own test strategy, and the point is
independence: copy the ~~three~~ **four** commands (Entry 10) **out of
`docs/metrics.md`** and run them
from the repository root, supplying nothing. Any step QA has to invent — a
changed path, a missing field name, a tool install — fails AC-2.2 regardless of
what this file records. AC-7.4 is satisfied only if QA's own AC-2.1 run holds, so
it cannot be verified by the author at all.

---

## Entry 10 — `/peer-review` round 2 fix-mode: the fixes had their own drift

Round 1's fix-mode closed the Blockers and Majors correctly but, in doing so,
created a second tier of staleness: fixing F7 (a commit message) changed that
commit's SHA and orphaned a reference to it elsewhere; fixing F6 (a missing
command) made every "three commands" sentence wrong; the F1 rebase moved the
snapshot date and made two ACs' own literal text wrong. Round 2 caught all of
it. None of it was structural — every item below is a reference, a count, or
a sentence that needed to agree with something that had already changed.

### F10 — the self-contradicting "7,800 lines" paragraph

`docs/metrics.md`'s "Why no project is named" section carried a sentence
describing **this snapshot's** line lift as "7,800 lines" — a number that was
correct for the 1→2-machine transition, now sitting two screens above a
paragraph that correctly states the 2→3-machine lift as **+125,661**. Same
file, two numbers, both claiming to be the lift, neither labelled as to which
transition it describes.

```
$ grep -n '7,800\|125,661' docs/metrics.md
230:figure is some 7,800 lines higher than the one before it: no code was written, a
265:lines, of which 125,646 are the new machine's one large project, counted now
```

Disambiguated rather than deleted — the 7,800 figure is real history and
stays, now explicitly anchored to "an earlier, single-machine measurement"
and "the first two-machine merge", with a forward pointer to where the
current lift is explained.

### F11 — the constitution's inventory pin, orphaned by this round's own earlier fix

§8 pinned its file-count inventory to `db4ab15`. Round 1 fix-mode reworded
that exact commit to fix F7 (its subject), which gives it a new SHA
(`62b4318`) — `db4ab15` stopped being reachable from any branch the moment
that replay landed, hours before round 2 caught it:

```
$ git merge-base --is-ancestor db4ab15 HEAD; echo $?
1
$ git merge-base --is-ancestor db4ab15 origin/main; echo $?
1
```

Re-pinned to `62b4318`, with the counts re-taken at that exact commit rather
than assumed to be unchanged:

```
$ git ls-tree -r --name-only 62b4318 | wc -l
107
$ git ls-tree -r --name-only 62b4318 | grep -c '\.md$'
90
$ git ls-tree -r --name-only 62b4318 | grep -c '\.json$'
5
$ git ls-tree -r --name-only 62b4318 | grep '\.json$'
.claude-plugin/marketplace.json
.claude-plugin/plugin.json
docs/reports/m-2e80b1d428827c8d.json
docs/reports/m-382a803dcc0de961.json
docs/reports/m-aef31f2de543f46c.json
```

A "Pin history" note was added alongside the corrected figures — naming the
old SHA, the old count, and *why* a commit reference is fragile in a feature
whose own history gets reworded mid-increment — rather than silently
substituting new numbers with no trace of the old ones.

### F12 / F13 — "three commands" became four and nobody told the prose

F6 (round 1) added a fourth printed command to `docs/metrics.md` without
updating the five sentences elsewhere that promised three: the file's own
opening line, `README.md`, `docs/reports/README.md`, `ROADMAP.md`, and two
places in this file. All five corrected to "four". `ROADMAP.md` additionally
still said "two committed machine reports" and "2026-09-09" — both corrected
to three and 2026-09-10, since `ROADMAP.md` sat outside round 1's sweep
entirely (it is reader-facing prose, not one of F1's three named files).

### F14 — two Must ACs hardcoded a date that moved

`AC-2.3` and `AC-7.2` both named `2026-09-09` as literal text, written before
F1's rebase moved the snapshot to `2026-09-10`. `AC-7.2`'s own embedded
verification command (`grep -n -A4 '2026-09-09' README.md`) now printed
nothing — a Must AC whose own stated test fails on a fact that has nothing to
do with whether the work is correct.

Fixed by generalising rather than by updating one date to another, which
would only move the failure to the next time this snapshot's date changes:
`AC-2.3` now says "dates the snapshot" without naming one; `AC-7.2`'s command
anchors on the `#### Snapshot` heading text, which is stable, instead of a
date string, which is not.

```
$ grep -n -A4 '#### Snapshot' README.md
258:#### Snapshot — 2026-09-10
259-
260:Dated **evidence**, taken 2026-09-10 and not updated since:
261-
262-| Spec | Plan | Review | QA | Release | Git tags | Role-agent runs | Human gate decisions |
```

Recorded as `C9` in the spec's Clarifications table.

### F15 — the spec's own gate forgot it had grown

Adding `C8` (round 1) and `C9` (this round) without updating the two places
that summarise the Clarify pass left the Handoff and the SPEC GATE both
claiming "`C1–C7` … all resolved" while `C8`/`C9` sat unmentioned, and the
line-budget box still read "Ist 187" against a file that had grown to 189
lines. Both corrected to `C1–C9` and `Ist 189`.

**The harder part of F15, addressed directly rather than deferred:** editing
an *approved* spec's NFR/AC text has no clean precedent in this project's own
rules — `/increment`'s fix-mode is authorised to make "small, obvious
corrections" but that language is written about `plan.md`, not `spec.md`,
and the constitution edits earlier today had an explicit user ruling (`A8`)
that these corrections do not. Rather than claim equivalent authority or
silently proceed, the spec's Handoff now states plainly that `C8`/`C9` are
`/peer-review` findings corrected in fix-mode — narrow, factual, low-risk —
without a fresh spec-gate re-approval, and names that for the user to ratify
or reopen. The correction stands; the authority question is surfaced, not
resolved unilaterally.

### F9, completed

Round 1 corrected the quoted grep transcript but missed the prose sentence
one line below it, which still read `:295` against the corrected `:296` —
and by the time round 2 reached it, the constitution had moved again (to
`:305`, from this very round's F11 fix). Fixed by dropping line numbers from
the prose citation entirely and citing the row by its content instead — the
third time a line-number citation in this file has gone stale is the
argument for never doing it a fourth.

### Final sweep after all of the above

```
$ python3 <extract-and-run-4-blocks, $SCRATCH>
4 pairs, all match: True
$ claude plugin validate .
✔ Validation passed with warnings   (same single pre-existing autoUpdate warning)
$ git diff --name-status origin/main | grep -E '^.\t(skills|agents|lenses|templates|tools|\.claude-plugin)/'
(no output — NFR-1 holds)
$ git log --oneline --reverse origin/main..HEAD | grep -n 'negative case\|remove the metrics counter'
4:e8eb42c docs(evidence): record the negative case before any deletion
6:62b4318 feat: remove the metrics counter and publish the method instead
$ grep -rn 'spark-metrics' . --include='*.md' | grep -v '\.spark/[a-z-]*/'
.spark/constitution.md:305:| 2026-09-11 | §3 stack/runtime: **no exception …   (the one expected hit, D1 unchanged)
```

All 23 figures re-derived once more against the final file state: 0
mismatches, matching both this file's earlier derivations and the Reviewer's
independent one in round 2.

---

## Entry 11 — `/peer-review` round 3 fix-mode: the rebase's last two blind spots, and one inherited error

Round 3 found the same failure mode a third time, smaller each time: round
1's rebase (F1) generalised two date-bearing ACs at round 2 (`C9`) and missed
two more with the identical defect, plus three historical entries in this
file that round 2's own fixes had superseded without being struck through,
plus one factual error in `docs/metrics.md` inherited verbatim from
`origin/main` and never independently checked against the reports it
describes.

### F16 — AC-2.1's literal expected figures, 7 of 9 wrong

AC-2.1 hardcoded `10 projects, 54 features, Spec 54, Plan 53, Review 52, QA
41, Release 48` — the pre-rebase figures. `429` and `377` (role-agent runs,
human gate decisions) happened to survive unchanged, because the third
machine's report carries zero aSPARK-driven transcript activity:

```
$ python3 -c "import json,glob; print(sum((json.load(open(p))['transcripts'].get('agent_runs_total') or 0) for p in sorted(glob.glob('docs/reports/*.json'))))"
429
$ python3 -c "import json,glob; print(sum((json.load(open(p))['transcripts'].get('gates') or 0) for p in sorted(glob.glob('docs/reports/*.json'))))"
377
```

Fixed the same way as `C9`, one step further: AC-2.1 now points at the
published Snapshot block rather than a hardcoded figure set, since the
figures themselves — not just the date — are exactly what a future report
would move. A fixed number embedded in an AC that grades a live, reproducible
method is the recurring defect; the fourth occurrence is the last one worth
generalising away rather than re-dating.

### F17 — AC-3.2, the same defect `C9` missed

`C9` generalised AC-2.3 and AC-7.2 but not AC-3.2, which carried the
identical hardcoded `2026-09-09`. Generalised the same way. Recorded as `C10`
alongside F16, rather than widening `C9` after the fact — each finding that
prompts a spec edit gets its own citation, consistent with `C8`'s and `C9`'s
own precedent.

### F18 — three historical entries, not struck through where superseded

This file's own convention (`:10`, in the Handoff) is *"a superseded number
is struck through in place, never deleted."* Round 1 and round 2's fixes
changed facts that Entries 4, 6 and 7 had already recorded in prose — the
command count, the snapshot date, the constitution's inventory pin — and
none of the three entries were revisited to apply that convention to
themselves. Fixed: each stale claim now carries a `~~old~~` **new** strike
with a pointer to where the change actually happened (Entry 10, mostly), and
the two places where a literal command transcript is quoted are annotated as
"taken at T9/T10, kept as the historical record" rather than silently edited
to match current values — the same distinction this file has used throughout
between a live claim (corrected) and a transcript of a past run (kept, dated).

### F19 — a release-gap claim that was never independently checked

`docs/metrics.md`'s "Reading the gaps" section said *"Two more are
single-feature projects that stalled before review."* Re-derived from the
reports directly rather than trusted from `origin/main`'s prose (which this
branch had copied verbatim without re-checking against the expanded
three-report data):

```
$ python3 - <<'PY'
import json, glob
projects = {}
for path in sorted(glob.glob('docs/reports/*.json')):
    for proj in json.load(open(path))['projects']:
        feats = projects.setdefault(proj['id'], {})
        for f in proj['features']:
            r = feats.setdefault(f['key'], {})
            for phase, hit in f['reached'].items():
                r[phase] = r.get(phase, False) or hit
for pid, feats in projects.items():
    for k, v in feats.items():
        if not v.get('release'):
            print(pid[:12], k[:10], v)
PY
g:ef6b0fee91 0601ca7a1c {'spec': True, 'plan': False, 'review': False, 'qa': False, 'release': False}
g:c386b6cfe3 85160fa491 {'spec': True, 'plan': True, 'review': True, 'qa': True, 'release': False}
g:c386b6cfe3 b4a85d0f69 {'spec': True, 'plan': True, 'review': True, 'qa': True, 'release': False}
g:c386b6cfe3 20c034ecb7 {'spec': True, 'plan': True, 'review': True, 'qa': True, 'release': False}
g:38c2b118a2 812dde83f0 {'spec': True, 'plan': True, 'review': True, 'qa': False, 'release': False}
g:ac99ebc025 b3e86fa557 {'spec': True, 'plan': True, 'review': False, 'qa': False, 'release': False}
```

Three features in `g:c386b6cfe3` match the "specified, planned, reviewed and
QA'd, shipped nothing" description exactly. Of the remaining two
single-feature projects: `g:ef6b0fee91` genuinely stalled before plan —
"before review" undersells how early it stopped. `g:38c2b118a2` reached
`plan` **and** `review`, and stalled at QA — "stalled before review" is
simply false for this one. Corrected to name each stall point precisely
rather than group them under one claim that was right for neither.

### F20 — left open, deliberately, for the user

The Reviewer's round 3 judgement: `spec.md`'s disclosure of `C8`'s authority
(added at this round, before round 3 even ran) is *"honest and adequate... but
it discloses rather than resolves... ratification is now owed at the release
gate."* This entry does not attempt to close F20. `spec.md`'s own Handoff
states the question for the user directly; this file records that the
question exists and was not settled in fix-mode, the same way `C8`/`C9`/`C10`
are each marked with the limits of their own authority rather than presented
as settled.

### Final sweep

```
$ python3 <extract-and-run-4-blocks>
4 pairs, all match: True
$ claude plugin validate .
✔ Validation passed with warnings   (same single pre-existing autoUpdate warning)
$ git diff --name-status origin/main | grep -E '^.\t(skills|agents|lenses|templates|tools|\.claude-plugin)/'
(no output — NFR-1 holds)
$ wc -l .spark/metrics-script-removal/spec.md
190
```

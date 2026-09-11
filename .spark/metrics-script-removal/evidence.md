# Evidence: metrics-script-removal

| | |
|---|---|
| **Phase** | Act (`/increment`) |
| **Owner** | Developer (the orchestrating session) |
| **Status** | `in-progress` |
| **Date** | 2026-09-11 |

**Handoff**
- **Status:** `in-progress` — written run by run as tasks complete. Entries are append-only; a superseded number is struck through in place, never deleted.
- **Summary:** The single evidence artifact for this feature. Holds the negative case, the figure derivations (run twice, either side of the `transcripts.root` strip), the recovery commit for the deleted script, and the command sequences `/demo-day` must perform.
- **Open:** see the task table in `plan.md` §3 for what is still `todo`.
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

What the file now carries: three commands (disk artifacts, git history,
transcript activity), each with its observed output printed beneath it, plus the
four combination rules as a table. What it lost: the flag table, the
`--write-report` transport workflow, the merge-invocation prose, and every
sentence describing a program's behaviour.

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
their place the file states that the directory is a **closed 2026-09-09
snapshot**, that this repository contains no tool to produce another report, and
points at `docs/metrics.md`'s three commands for re-deriving the figures from
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

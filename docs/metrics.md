# Dogfooding metrics — method and snapshot

aSPARK is prompt material. It has no test suite, so the only evidence that the
loop holds is a documented run. This file explains how the numbers in the
README's **Project Status** section are counted, and records the snapshot they
were taken from.

Every number here is produced by [`scripts/spark-metrics.py`](../scripts/spark-metrics.py),
from two sources that can be checked by hand.

## Reproduce it

```bash
python3 scripts/spark-metrics.py
```

Standard library only — no install step, no dependencies. Useful flags:

| Flag | Effect |
|---|---|
| `~/foo ~/bar` | count only these projects instead of searching |
| `--search-root DIR` / `--depth N` | where and how deep to look (default `~`, depth 3) |
| `--exclude SUBSTRING` | skip a path — a stale second checkout, say |
| `--totals-only` | aggregate counts only, no project named — the shape meant for publishing |
| `--write-report DIR` | write this machine's report to `DIR/<machine-id>.json`, always nameless |
| `--merge a.json b.json` | combine reports from several machines (see below) |
| `--no-transcripts` | disk artifacts only |
| `--format json` | the same report as JSON |

## What is counted

**Loop artifacts on disk** — the primary source, and the one anyone can verify
with `ls`. Every project with a `.spark/` directory is a project; every
directory inside it is a feature. A phase counts as *reached* when its artifact
file exists:

| Phase | Artifact | Also accepted |
|---|---|---|
| Specify | `spec.md` | — |
| Plan | `plan.md` | — |
| Review | `review.md` | `review-report.md` |
| Review (QA) | `qa.md` | `qa-report.md` |
| Keep | `release.md` | `release-notes.md` |

The alternates are historical: earlier loops wrote `review-report.md` before the
template settled. Nothing on this table is inferred from a transcript — an
artifact is there or it isn't.

**Lines since adoption** — insertions and deletions from the first commit that
touched `.spark/` onward. Counting a repository's whole history would credit
aSPARK with code written before it was installed; this is the one number most
easily overstated, so it is bounded deliberately. Where the loop was adopted
after the first commit, the table names the date.

**Loop activity in transcripts** — role-agent runs, human gate decisions and
ceremony invocations, read from Claude Code's own session logs under
`~/.claude/projects/`. A session counts as aSPARK-driven only if it invoked a
ceremony by name or loaded a skill from the aspark plugin cache; mentioning
aSPARK is not enough, and tool results are excluded from that check so a session
that reads these transcripts cannot detect itself.

## What is deliberately not counted

**Tokens.** The obvious number — roughly 11 billion across this machine's aSPARK
sessions — is 86 % cache reads, which measure prompt size rather than work done.
It is a consumption figure dressed as an achievement figure, it says nothing
about whether the loop held, and nobody else can reproduce it. It is left out.

**Ceremony counts as a completion measure.** `/spark` runs the other ceremonies
internally without leaving a command of its own, so the by-name tally
systematically undercounts. It is reported with that caveat and never used to
claim how many loops ran; the `.spark/` artifacts answer that question properly.

## Honest nulls

A phase or a repository that cannot be measured reports `n/a` with a reason, not
a `0`. A zero in these tables always means *counted, found none*. Three live
cases in the snapshot below: three projects do not commit their `.spark/`
directory, so no line count exists for them. None is quietly folded into the
total as a zero — the aggregate says how many projects it could measure and how
many it could not.

## Counting across machines

One run measures one machine. To keep a running total across several, produce a
report on each and merge them.

**The repository is the transport.** Every machine that runs the loop already
has this repository, it syncs in both directions, and a report is nameless — so
reports live in [`docs/reports/`](reports/), one per machine, and nothing has to
be hand-carried:

```bash
# on each machine
git pull
python3 scripts/spark-metrics.py --totals-only --write-report docs/reports
git add docs/reports && git commit -m "chore: metrics report from this machine" && git push

# on any machine that has pulled them all
python3 scripts/spark-metrics.py --merge docs/reports/*.json
```

A report is named after its machine's own hashed id, so a second run overwrites
that machine's file instead of adding one. `--write-report` always writes the
nameless shape, whatever `--totals-only` says about what the run prints: the
flag governs one run's output, the directory governs what leaves the machine.

Nothing about this is required — `--format json` to any path and
`--merge a.json b.json` works the same, if the reports travel some other way.
The script itself is all that has to exist on a machine: a single file, standard
library only, no install step. `git`, if present, supplies line counts and tags;
without it those report `n/a` rather than failing.

**Artifacts are unioned, never added.** The same repository checked out on two
machines holds overlapping features; adding the reports would double-count every
one of them. Projects are keyed on a stable identity — the SHA-256 of the
repository's root commit, which is identical in every clone — and their features
are unioned on a per-feature identity, with each phase OR'd across machines. A
feature that exists on both machines counts once, and a phase reached on either
machine counts as reached, so a clone sitting at `plan.md` does not erase the QA
the other clone already passed.

The union is per feature rather than "the highest count any machine saw" because
the latter is only correct when one clone's features are a subset of the other's.
That holds when `.spark/` is committed and fails when it is not — and this
snapshot has projects in both states. Two machines each holding three features,
one shared, is five; a highest-count rule would report three.

Both identities are hashed rather than used raw, so a report can be passed
around without pointing at the repository it came from or naming a single
feature. They are the fields `--totals-only` keeps, because without them a merge
cannot tell one project from two, or one feature from another.

**Session figures are summed**, because a session on another machine is a
genuinely different session. Active days are unioned, not added — the same
calendar day can appear on two machines.

Because they are summed, they have no identity protecting them the way projects
do, and passing **one machine's report twice** would inflate every one of them.
Each report therefore carries a hashed machine id, and a repeat is refused and
named in the output rather than merged.

**A project that is not a git repository has no stable identity.** It cannot be
matched across machines, so it is counted as found and the merged report says
how many such projects there are and that they may be double-counted. `git init`
is the fix. Guessing by directory name would silently merge two unrelated
projects that happen to share one, which is the worse error.

A merged report is always rendered in the aggregate shape: it holds opaque ids
and no names, so there is nothing else it could show.

## Why no project is named

The published figures are counts, and a count needs no project name to be
checked. Naming them would put private repositories into a public README to add
nothing a reader can use, so `--totals-only` drops the per-project rows — in the
JSON output as well as the Markdown, or the flag would be a display trick rather
than a real one. The per-project view stays available to whoever runs the script
on their own machine.

## Snapshot — 2026-09-09

Two machines, merged. Each wrote its report with

```bash
python3 scripts/spark-metrics.py --depth 2 --exclude Downloads --totals-only \
  --write-report docs/reports
```

and the total is the merge of both, from [`docs/reports/`](reports/):

```bash
python3 scripts/spark-metrics.py --merge docs/reports/*.json
```

(the exclusion drops a stale second checkout that would otherwise double-count
two features).

### Loop artifacts on disk

| Features | Spec | Plan | Review | QA | Release | Git tags |
|---:|---:|---:|---:|---:|---:|---:|
| **54** | **54** | **53** | **52** | **41** | **48** | **61** |

10 projects, 54 features — one of them aSPARK itself, nine of them not.

**What the merge removed.** The two machines report 51 and 14 features, which
would add to 65 across 13 projects. The counted figure is **54 across 10**,
because **3 projects sit on both machines and 11 of their features are the same
features**. The largest of the three is aSPARK itself: 8 features on each
machine, identical, since `.spark/` is committed and both clones carry all of
them. The other two overlap one-sidedly — 9 features against 2, and 2 against 1,
with the smaller set contained in the larger both times, because one machine's
clone is simply behind.

On this particular pair of reports a highest-count rule would therefore have
produced the same 54: every overlap here happens to be a subset, which is the
one case where taking the larger count is right. The per-feature union is not
what changed this number, and is not claimed to be. It is what makes the number
hold when a machine has a feature the other does not — two clones each holding
work the other lacks, which the moment `.spark/` is uncommitted in a shared
project is the normal case, not the exception.

**The possible overcount is closed.** One of the ten projects was not a git
repository, so it had no identity that survives a machine boundary and would
have been counted twice had it existed on both machines. It has since been put
under version control, and every project in this snapshot now merges on a stable
identity. Its history counting for the first time is why the line figure below
is some 7,800 lines higher than the merge that preceded it — no code was
written, a project simply became measurable.

**+114,630 / −12,589 lines** since the loop was adopted, across the 7 of 10
projects whose line count is measurable; 3 report `n/a` (`.spark/` not tracked in
that repository). The line figure drifts with every commit — it is a snapshot,
not a standing claim.

### Loop activity in Claude Code transcripts

- **42** of 114 sessions were aSPARK-driven
- **429** role-agent runs — reviewer 108 · product-owner 103 · release-manager 63 · engineering-manager 61 · qa-tester 59 · designer 24 · facilitator 11
- **377** human gate decisions
- **51** active days, 2026-07-13 to 2026-09-08
- 116 ceremonies invoked by name — `/spark` 35 · `/next-steps` 24 · `/peer-review` 12 · `/sprint-plan` 11 · `/demo-day` 11 · `/increment` 8 · `/story-time` 6 · `/go-live` 6 · `/charter` 3 (an undercount, see above)

These are summed across both machines, not unioned: a session on another machine
is genuinely another session. Only the active days are unioned, since the same
calendar day appears on both. The window starts two days earlier than the single
machine's did, because the earlier adoption happened on the other one.

## Reading the gaps

The gaps are the interesting part, and they are not rounded away.

- **QA, 41 of 54.** Eight of the thirteen missing QA reports sit in a single
  library project with no browser surface, where `/demo-day` ran once across
  nine features. That is exactly the case
  [constitution §8's QA-method declaration](../README.md#project-status) was
  written for, and those features predate it.
- **Release, 48 of 54.** Three of the six unreleased features sit in one project
  that specified, planned, reviewed and QA'd them and then shipped nothing. Two
  more are single-feature projects that stalled before review.
- **`situational-lenses` has a spec and nothing else** — this repository's own
  feature, and the lens layer's field-proof gap, tracked as
  [#4](https://github.com/a-lottes/aSPARK/issues/4) and
  [#5](https://github.com/a-lottes/aSPARK/issues/5).

## Related

[`aspark-insights`](https://github.com/a-lottes/aSPARK-insights) computes the
richer version of this — real Story→Task and AC→QA traceability coverage against
`aspark-graph`'s facts, plus a release board mapping every git tag to the
features that shipped in it. `spark-metrics.py` is deliberately smaller: no
graph, no install, one file, so the README's headline numbers can be checked by
anyone who has cloned this repository.

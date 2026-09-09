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
a `0`. A zero in these tables always means *counted, found none*. Two live cases
in the snapshot below: one project does not commit its `.spark/` directory, so
no line count exists for it; another is not a git repository at all. Neither is
quietly folded into the total as a zero — the aggregate says how many projects
it could measure and how many it could not.

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

Taken with
`python3 scripts/spark-metrics.py --depth 2 --exclude Downloads --totals-only`
(the exclusion drops a stale second checkout that would otherwise double-count
two features).

> **Interim: this is one machine, not all of them.** A second development
> machine reports **14 features across 6 projects** with the same command, and
> the two have not yet been merged. The combined figure is therefore not yet
> known, but it is **bounded between 51 and 65**: at least 51, because every
> feature in the table below is in the union, and at most 65, because a union
> cannot exceed the sum of its parts.
>
> The true value sits below the upper bound, since the two machines demonstrably
> overlap — aSPARK's own repository is on both, and its 8 features are committed
> in `.spark/`, so any clone carries all of them. That puts the working estimate
> at **51 to 57**. Which of the other five projects also exist on both is not
> known from here, and is not guessed.
>
> A single `--merge` of both machines' reports replaces this note with a counted
> figure — see [Counting across machines](#counting-across-machines). Until then
> the range stands in place of a number, because adding 51 and 14 would count
> aSPARK's features twice and the result would not be reproducible by anyone.

### Loop artifacts on disk

| Features | Spec | Plan | Review | QA | Release | Git tags |
|---:|---:|---:|---:|---:|---:|---:|
| **51** | **51** | **50** | **50** | **40** | **47** | **52** |

7 projects, 51 features — one of them aSPARK itself, six of them not.

**+104,223 / −12,419 lines** since the loop was adopted, across the 5 of 7
projects whose line count is measurable; 1 reports `n/a` (`.spark/` not tracked
in that repository), 1 reports `n/a` (not a git repository). The line figure
drifts with every commit — it is a snapshot, not a standing claim.

### Loop activity in Claude Code transcripts

- **38** of 85 sessions were aSPARK-driven
- **411** role-agent runs — reviewer 103 · product-owner 97 · release-manager 62 · qa-tester 59 · engineering-manager 57 · designer 23 · facilitator 10
- **344** human gate decisions
- **49** active days, 2026-07-15 to 2026-09-08
- 113 ceremonies invoked by name — `/spark` 34 · `/next-steps` 23 · `/peer-review` 12 · `/sprint-plan` 11 · `/demo-day` 11 · `/increment` 8 · `/story-time` 6 · `/go-live` 6 · `/charter` 2 (an undercount, see above)

## Reading the gaps

The gaps are the interesting part, and they are not rounded away.

- **QA, 40 of 51.** Eight of the eleven missing QA reports sit in a single
  library project with no browser surface, where `/demo-day` ran once across
  nine features. That is exactly the case
  [constitution §8's QA-method declaration](../README.md#project-status) was
  written for, and those features predate it.
- **Release, 47 of 51.** Three features in one project were specified, planned,
  reviewed and QA'd but never shipped.
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

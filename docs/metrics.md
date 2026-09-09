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
a `0`. A zero in these tables always means *counted, found none*. Two live
examples in the snapshot below: `aSPARK-policy` does not commit its `.spark/`
directory, so no line count exists for it; `Reddit-Scout` is not a git
repository at all.

## Snapshot — 2026-09-09

Taken with `python3 scripts/spark-metrics.py --depth 2 --exclude Downloads`
(the exclusion drops a stale second checkout of `aSPARK-graph`).

### Loop artifacts on disk

| Project | Features | Spec | Plan | Review | QA | Release | Tags | Lines since adoption |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| aSPARK-insights | 12 | 12 | 12 | 12 | 11 | 12 | 12 | +32,545 / −506 |
| steamcore | 12 | 12 | 12 | 12 | 12 | 12 | 12 | +32,619 / −1,288 |
| aSPARK-graph | 9 | 9 | 9 | 9 | 1 | 9 | 8 | +19,754 / −1,782 |
| aSPARK | 8 | 8 | 7 | 7 | 6 | 7 | 9 | +14,803 / −1,099 (since 2026-07-15) |
| aSPARK-policy | 5 | 5 | 5 | 5 | 5 | 2 | 2 | n/a — `.spark/` is not tracked in this repository |
| Reddit-Scout | 3 | 3 | 3 | 3 | 3 | 3 | n/a | n/a — not a git repository |
| datrivo | 2 | 2 | 2 | 2 | 2 | 2 | 9 | +3,926 / −7,744 (since 2026-07-14) |
| **Total** | **51** | **51** | **50** | **50** | **40** | **47** | **52** | **+103,647 / −12,419** |

### Loop activity in Claude Code transcripts

- **38** of 85 sessions were aSPARK-driven
- **411** role-agent runs — reviewer 103 · product-owner 97 · release-manager 62 · qa-tester 59 · engineering-manager 57 · designer 23 · facilitator 10
- **344** human gate decisions
- **49** active days, 2026-07-15 to 2026-09-08
- 113 ceremonies invoked by name — `/spark` 34 · `/next-steps` 23 · `/peer-review` 12 · `/sprint-plan` 11 · `/demo-day` 11 · `/increment` 8 · `/story-time` 6 · `/go-live` 6 · `/charter` 2 (an undercount, see above)

## Reading the gaps

The gaps are the interesting part, and they are not rounded away.

- **QA, 40 of 51.** Mostly `aspark-graph`, where `/demo-day` ran once in nine
  features. A library with no browser surface is exactly the case
  [constitution §8's QA-method declaration](../README.md#project-status) was
  written for, and those nine features predate it.
- **Release, 47 of 51.** `aSPARK-policy` has three features specified,
  planned, reviewed and QA'd that were never released.
- **`situational-lenses` has a spec and nothing else** — the lens layer's own
  field-proof gap, tracked as
  [#4](https://github.com/a-lottes/aSPARK/issues/4) and
  [#5](https://github.com/a-lottes/aSPARK/issues/5).

## Related

[`aspark-insights`](https://github.com/a-lottes/aSPARK-insights) computes the
richer version of this — real Story→Task and AC→QA traceability coverage against
`aspark-graph`'s facts, plus a release board mapping every git tag to the
features that shipped in it. `spark-metrics.py` is deliberately smaller: no
graph, no install, one file, so the README's headline numbers can be checked by
anyone who has cloned this repository.

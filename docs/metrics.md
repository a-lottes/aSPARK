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

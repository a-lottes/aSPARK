# Dogfooding metrics — method and snapshot

aSPARK is prompt material. It has no test suite, so the only evidence that the
loop holds is a documented run. This file explains how the numbers in the
README's **Project Status** section were counted, and records the snapshot they
were taken from.

**This is a closed snapshot, taken 2026-09-09.** The figures were produced by a
counter that this repository no longer contains: constitution §3 allows Markdown
and JSON only, and metrics tooling now lives outside this repo. What remains here
is better than the tool — the two machine reports the figures were computed from
are committed under [`docs/reports/`](reports/), so every number below can be
re-derived from the evidence itself. Nothing here updates, and no command in this
repository will produce a newer figure.

## Check any figure yourself

Three commands, run from the repository root. They need Python 3 and nothing
else — no install, no dependencies, no tool of ours. Each one was run exactly as
printed and its output is shown beneath it.

**Loop artifacts on disk** — projects, features, and how far each feature got:

```bash
python3 - <<'PY'
import json, glob
feat = {}
for path in sorted(glob.glob('docs/reports/*.json')):
    for proj in json.load(open(path))['projects']:
        for f in proj['features']:
            reached = feat.setdefault((proj['id'], f['key']), {})
            for phase, hit in f['reached'].items():
                reached[phase] = reached.get(phase, False) or hit
print('projects', len({pid for pid, _ in feat}))
print('features', len(feat))
for phase in ('spec', 'plan', 'review', 'qa', 'release'):
    print(phase, sum(1 for r in feat.values() if r.get(phase)))
PY
```

```
projects 10
features 54
spec 54
plan 53
review 52
qa 41
release 48
```

**Git history** — tags, and lines since the loop was adopted:

```bash
python3 - <<'PY'
import json, glob
git, seen = {}, set()
for path in sorted(glob.glob('docs/reports/*.json')):
    for proj in json.load(open(path))['projects']:
        seen.add(proj['id'])
        kept = git.setdefault(proj['id'], {})
        for field in ('tags', 'added', 'deleted'):
            if field in (proj.get('git') or {}):
                kept[field] = max(kept.get(field, 0), proj['git'][field])
for field in ('tags', 'added', 'deleted'):
    print(field, sum(p.get(field, 0) for p in git.values()))
print('line counts available for', sum(1 for p in git.values() if 'added' in p), 'of', len(seen), 'projects')
PY
```

```
tags 61
added 114630
deleted 12589
line counts available for 7 of 10 projects
```

**Loop activity in Claude Code transcripts** — sessions, agent runs, gates, days:

```bash
python3 - <<'PY'
import json, glob
runs = [json.load(open(p))['transcripts'] for p in sorted(glob.glob('docs/reports/*.json'))]
for field in ('sessions_aspark', 'sessions_total', 'agent_runs_total', 'gates'):
    print(field, sum(r.get(field) or 0 for r in runs))
days = {d for r in runs for d in (r.get('days') or [])}
print('active_days', len(days), min(days), 'to', max(days))
PY
```

```
sessions_aspark 42
sessions_total 114
agent_runs_total 429
gates 377
active_days 51 2026-07-13 to 2026-09-08
```

### The four combination rules

Everything above is those three commands plus four rules about how two machines'
reports combine. The rules are what make the figures honest, so they are stated
rather than buried in code:

| Rule | Why |
|---|---|
| **Projects are unioned** on `projects[].id` | The id is the SHA-256 of the repository's root commit, identical in every clone — so one repository checked out on two machines is one project, not two |
| **Features are unioned** on `(project id, feature key)`, and each phase is **OR'd** across machines | A feature on both machines counts once; a phase reached on either machine counts as reached, so a clone sitting at `plan.md` does not erase QA the other clone already passed |
| **Git counts take the max per project**, then sum across the union | Two clones of one repository describe the same history; the smaller number is a clone that is behind, not extra work |
| **Transcript counters are summed; active days are unioned** | A session on another machine is genuinely another session, but the same calendar day is not another day |

The per-feature union matters more than it looks. "Take the highest count any
machine saw" is only correct when one clone's features are a subset of the
other's — true when `.spark/` is committed, false when it is not, and this
snapshot has projects in both states. Two machines each holding three features,
one shared, is five; a highest-count rule would report three.

## What is counted

**Loop artifacts on disk** — the primary source, and the one anyone can verify
with `ls`. Every project with a `.spark/` directory is a project; every directory
inside it is a feature. A phase counts as *reached* when its artifact file
exists:

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
easily overstated, so it is bounded deliberately.

**Loop activity in transcripts** — role-agent runs, human gate decisions and
ceremony invocations, read from Claude Code's own session logs. A session counted
as aSPARK-driven only if it invoked a ceremony by name or loaded a skill from the
aspark plugin cache; mentioning aSPARK was not enough, and tool results were
excluded from that check so a session reading those transcripts could not detect
itself.

These are the only figures here that **cannot** be re-derived from first
principles by a reader: the session logs are local to each machine and are not
committed. What the reports carry is the counts, not the logs. So the transcript
numbers are checkable against the reports — which is what the third command does
— but not auditable back to their source by anyone but the two machines that
wrote them. That limit is theirs alone; the disk-artifact figures above do not
share it.

## What is deliberately not counted

**Tokens.** The obvious number — roughly 11 billion across one machine's aSPARK
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
cases in the snapshot: three projects do not commit their `.spark/` directory, so
no line count exists for them — which is why the second command prints "7 of 10"
rather than folding the other three in as zeros.

## Why no project is named

The published figures are counts, and a count needs no project name to be
checked. Naming them would put private repositories into a public README to add
nothing a reader can use. Both the project and feature identities are hashed
rather than used raw, so a report can be read without pointing at the repository
it came from or naming a single feature — and those hashes are exactly what a
merge needs to tell one project from two.

A project that is **not** a git repository has no such identity and cannot be
matched across machines. One of the ten was in that state at an earlier merge and
has since been put under version control, which is why this snapshot's line
figure is some 7,800 lines higher than the one before it: no code was written, a
project simply became measurable.

## Snapshot — 2026-09-09

Two machines, merged, from [`docs/reports/`](reports/).

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
clone is simply behind. Adding the totals would have overstated the count by
about a fifth.

**+114,630 / −12,589 lines** since the loop was adopted, across the 7 of 10
projects whose line count is measurable; 3 report `n/a` (`.spark/` not tracked in
that repository).

### Loop activity in Claude Code transcripts

- **42** of 114 sessions were aSPARK-driven
- **429** role-agent runs — reviewer 108 · product-owner 103 · release-manager 63 · engineering-manager 61 · qa-tester 59 · designer 24 · facilitator 11
- **377** human gate decisions
- **51** active days, 2026-07-13 to 2026-09-08
- 116 ceremonies invoked by name — `/spark` 35 · `/next-steps` 24 · `/peer-review` 12 · `/sprint-plan` 11 · `/demo-day` 11 · `/increment` 8 · `/story-time` 6 · `/go-live` 6 · `/charter` 3 (an undercount, see above)

Summed across both machines, not unioned — except the active days, which are.

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

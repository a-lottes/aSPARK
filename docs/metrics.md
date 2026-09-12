# Dogfooding metrics — method and snapshot

aSPARK is prompt material. It has no test suite, so the only evidence that the
loop holds is a documented run. This file explains how the numbers in the
README's **Project Status** section were counted, and records the snapshot they
were taken from.

**This is a closed snapshot, taken 2026-09-10.** The figures were produced by a
counter that this repository no longer contains: constitution §3 allows Markdown
and JSON only, and metrics tooling now lives outside this repo. What remains here
is better than the tool — the three machine reports the figures were computed
from are committed under [`docs/reports/`](reports/), so every number below can
be re-derived from the evidence itself. Nothing here updates, and no command in
this repository will produce a newer figure.

## Check any figure yourself

Four commands, run from the repository root. They need Python 3 and nothing
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
projects 11
features 77
spec 77
plan 76
review 75
qa 64
release 71
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
tags 84
added 240291
deleted 18872
line counts available for 8 of 11 projects
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
sessions_total 138
agent_runs_total 429
gates 377
active_days 51 2026-07-13 to 2026-09-08
```

**Per-agent and per-ceremony breakdown** — which role and which command,
specifically (added at `/peer-review` round 1, F6 — the two breakdowns below
were published with no command printing them, so a reader had to invent the
step):

```bash
python3 - <<'PY'
import json, glob
agents, cer = {}, {}
for p in sorted(glob.glob('docs/reports/*.json')):
    t = json.load(open(p))['transcripts']
    for k, v in (t.get('agent_runs') or {}).items():
        agents[k] = agents.get(k, 0) + v
    for k, v in (t.get('ceremonies') or {}).items():
        cer[k] = cer.get(k, 0) + v
for k, v in sorted(agents.items(), key=lambda x: -x[1]):
    print('agent', k, v)
print('ceremonies_total', sum(cer.values()))
for k, v in sorted(cer.items(), key=lambda x: -x[1]):
    print('ceremony', k, v)
PY
```

```
agent reviewer 108
agent product-owner 103
agent release-manager 63
agent engineering-manager 61
agent qa-tester 59
agent designer 24
agent facilitator 11
ceremonies_total 116
ceremony spark 35
ceremony next-steps 24
ceremony peer-review 12
ceremony sprint-plan 11
ceremony demo-day 11
ceremony increment 8
ceremony story-time 6
ceremony go-live 6
ceremony charter 3
```

### The four combination rules

Everything above is those four commands plus four rules about how several
machines' reports combine. The rules are what make the figures honest, so they are stated
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
— but not auditable back to their source by anyone but the three machines that
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
no line count exists for them — which is why the second command prints "8 of 11"
rather than folding the other three in as zeros.

## Why no project is named

The published figures are counts, and a count needs no project name to be
checked. Naming them would put private repositories into a public README to add
nothing a reader can use. Both the project and feature identities are hashed
rather than used raw, so a report can be read without pointing at the repository
it came from or naming a single feature — and those hashes are exactly what a
merge needs to tell one project from two.

A project that is **not** a git repository has no such identity and cannot be
matched across machines. One project was in that state at an earlier, single-
machine measurement, and was put under version control before the first
two-machine merge — which is why *that* merge's line figure came in some 7,800
lines higher than the single-machine figure before it: no code was written, a
project simply became measurable. (A second, larger lift happened at the move
to three machines — see the current snapshot below for that one; the two are
separate events, not the same number restated.)

## Snapshot — 2026-09-10

Three machines, merged, from [`docs/reports/`](reports/).

### Loop artifacts on disk

| Features | Spec | Plan | Review | QA | Release | Git tags |
|---:|---:|---:|---:|---:|---:|---:|
| **77** | **77** | **76** | **75** | **64** | **71** | **84** |

11 projects, 77 features — one of them aSPARK itself, ten of them not.

**What the merge removed.** The three machines report 51, 14 and 31 features,
which would add to 96 across 15 project checkouts. The counted figure is
**77 across 11**, because **3 projects sit on more than one machine — aSPARK on
all three — and 19 of their features are the same features**. The largest of the
three is aSPARK itself: 8 features on each machine, identical, since `.spark/` is
committed and every clone carries all of them. The other two overlap
one-sidedly — 9 features against 2, and 2 against 1, with the smaller set
contained in the larger both times, because one machine's clone is simply
behind. The third machine's one other project exists on no other machine, so all
23 of its features are new to the total.

On this particular set of reports a highest-count rule would therefore have
produced the same 77: every overlap here happens to be a subset, which is the
one case where taking the larger count is right. The per-feature union is not
what changed this number, and is not claimed to be. It is what makes the number
hold when a machine has a feature the others do not — clones each holding work
the other lacks, which the moment `.spark/` is uncommitted in a shared project is
the normal case, not the exception.

**+240,291 / −18,872 lines** since the loop was adopted, across the 8 of 11
projects whose line count is measurable; 3 report `n/a` (`.spark/` not tracked in
that repository). The lift over the previous two-machine merge is +125,661
lines, of which 125,646 are the new machine's one large project, counted now
because the machine holding it joined the total, and 15 are where its fresher
clone of this repository raised the per-project maximum the merge takes.

### Loop activity in Claude Code transcripts

- **42** of 138 sessions were aSPARK-driven
- **429** role-agent runs — reviewer 108 · product-owner 103 · release-manager 63 · engineering-manager 61 · qa-tester 59 · designer 24 · facilitator 11
- **377** human gate decisions
- **51** active days, 2026-07-13 to 2026-09-08
- 116 ceremonies invoked by name — `/spark` 35 · `/next-steps` 24 · `/peer-review` 12 · `/sprint-plan` 11 · `/demo-day` 11 · `/increment` 8 · `/story-time` 6 · `/go-live` 6 · `/charter` 3 (an undercount, see above)

Summed across all three machines, not unioned — except the active days, which
are.

The third machine added 24 sessions, none of them aSPARK-driven: its `.spark/`
artifacts sit on a machine whose local session logs hold no aSPARK run, so the
loops that produced them ran elsewhere. It grows the denominator and not the
numerator — the share of aSPARK-driven sessions falls as the artifact counts
rise — and that is the honest shape of the data, not an anomaly to smooth over.

## Reading the gaps

The gaps are the interesting part, and they are not rounded away.

- **QA, 64 of 77.** Eight of the thirteen missing QA reports sit in a single
  library project with no browser surface, where `/demo-day` ran once across
  nine features. That is exactly the case
  [constitution §8's QA-method declaration](../README.md#project-status) was
  written for, and those features predate it.
- **Release, 71 of 77.** Three of the six unreleased features sit in one project
  that specified, planned, reviewed and QA'd them and then shipped nothing. Of
  the other two, both single-feature projects, one stalled before plan and one
  reached review and stalled at QA.
- **`situational-lenses` has a spec and nothing else** — this repository's own
  feature, and the lens layer's field-proof gap, tracked as
  [#4](https://github.com/a-lottes/aSPARK/issues/4) and
  [#5](https://github.com/a-lottes/aSPARK/issues/5).

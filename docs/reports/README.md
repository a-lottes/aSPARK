# Machine reports

One JSON report per machine, the input to a cross-machine total.

The repository is the transport. Both machines already have it, it syncs in both
directions, and a report is nameless — so there is nothing to hand-carry and
nothing to leak. Add yours:

```bash
git pull
python3 scripts/spark-metrics.py --totals-only --write-report docs/reports
git add docs/reports && git commit -m "chore: metrics report from this machine" && git push
```

Then, on any machine that has pulled them all:

```bash
python3 scripts/spark-metrics.py --merge docs/reports/*.json
```

The file is named after the machine's own hashed id, so a second run from the
same machine overwrites its report instead of adding one. Rerun and commit
whenever the figure should be refreshed; nothing here updates itself.

## What is in a report, and what is not

Opaque ids and counts. No project name, no feature name, no hostname, no path.
`--write-report` always writes this nameless shape, whatever `--totals-only`
says about what a given run prints — the flag governs one run's output, this
directory governs what leaves the machine.

The ids are SHA-256 prefixes: a project's is derived from its repository's root
commit, identical in every clone, which is what lets a merge tell one project
from two rather than double-counting a repository checked out twice. Features
and machines carry their own for the same reason.

What a reader can see here is therefore how many projects and features a machine
holds, how far each got through the loop, and how much git history sits behind
them — never which projects they are. That is the same trade the published
figures make, and the reasoning is in [../metrics.md](../metrics.md#why-no-project-is-named).

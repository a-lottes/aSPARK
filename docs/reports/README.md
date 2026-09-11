# Machine reports

One JSON report per machine. Together they are the evidence behind the figures in
[README §Project Status](../../README.md#project-status) and
[docs/metrics.md](../metrics.md).

**This is a closed snapshot, taken 2026-09-09, and nothing here will grow.** The
two reports below were written by a counter that this repository no longer
contains — constitution §3 allows Markdown and JSON only, so metrics tooling lives
outside this repo and no command here can produce another report. What the
directory keeps is the part that matters: the data the published figures were
computed from, so anyone can re-derive them without trusting the author or
possessing the tool. [docs/metrics.md](../metrics.md#check-any-figure-yourself)
prints the three commands that do it, and their output.

## What is in a report, and what is not

Opaque ids and counts. No project name, no feature name, no hostname, no path.

The ids are SHA-256 prefixes: a project's is derived from its repository's root
commit, identical in every clone, which is what lets a merge tell one project
from two rather than double-counting a repository checked out twice. Features and
machines carry their own for the same reason.

What a reader can see here is therefore how many projects and features a machine
held, how far each got through the loop, and how much git history sat behind
them — never which projects they are. That is the same trade the published
figures make, and the reasoning is in
[../metrics.md](../metrics.md#why-no-project-is-named).

A machine id also guards the summed figures. Projects and features are unioned on
identity, so merging a report twice cannot inflate them — but session and
agent-run counts are added, and a repeated report would inflate every one. Each
report naming its own machine is what made a repeat detectable rather than
silent.

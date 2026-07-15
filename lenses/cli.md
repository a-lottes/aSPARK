---
name: cli
applies-to: [cli]
phases: [specify, review]
---

# CLI Lens

Active when the project profile includes **`cli`** — a tool run from a terminal,
by a human *and* by scripts. A CLI's UX is its flags, its output streams and its
exit codes; get them wrong and you break both the person typing and the pipeline
that wraps it. This lens keeps that contract usable and scriptable. It adds the
*command-line ergonomics* a generic code review doesn't check.

Like every lens, it flags concerns and proposes NFRs; it never invents scope.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| Ergonomics & output contract in the spec as ACs/NFRs | Specify | Product Owner |
| Flags, streams, exit codes, help in the diff | Review | Reviewer |

> **No QA row.** `/demo-day` drives a browser; a CLI is exercised in a terminal.
> Its verification lives in Specify (ACs), Review (the diff), and the increment's
> own invocation tests.

## The checklist

### 1. Discoverability & help *(Review)*
- [ ] `--help`/`-h` exists for the tool and every subcommand, and actually documents flags, arguments and a usage example — not an empty stub.
- [ ] `--version` reports the version; the tool has a clear name and consistent subcommand structure.
- [ ] Flag naming is consistent (`--dry-run`, not `--dryRun` on one command and `--dry` on another); common conventions honored (`-v`/`--verbose`, `-q`/`--quiet`).

### 2. Output streams & scriptability *(Review)*
- [ ] **Results go to stdout, diagnostics/errors/progress to stderr** — so `tool | next` pipes clean data, not log noise.
- [ ] A machine-readable mode exists where output is consumed programmatically (`--json`/`--format`), stable across versions.
- [ ] Color and interactive prompts are **suppressed when not a TTY**, and `NO_COLOR` is respected — a piped or CI run must not emit ANSI garbage or block on a prompt.

### 3. Exit codes & errors *(Review)*
- [ ] Exit code `0` only on success; distinct non-zero codes for distinct failure classes, so scripts can branch on them.
- [ ] Error messages name what went wrong and how to fix it, on stderr — not a raw stack trace as the only signal.

### 4. Safety & feedback *(Review)*
- [ ] Destructive or irreversible actions require confirmation **or** offer `--dry-run`, and support a non-interactive `--yes`/`--force` for scripts.
- [ ] Long-running operations show progress on stderr; the tool doesn't sit silent for minutes.
- [ ] Config/secrets come from flags, env or config files — never hardcoded, never required as a positional secret that lands in shell history.

## Phase notes

- **Specify (PO):** capture the ergonomics that matter as concrete ACs/NFRs —
  e.g. "results on stdout, logs on stderr", "`--json` output is stable",
  "destructive commands need `--force` in non-interactive mode". Falsifiable, so
  the Reviewer can check them.
- **Review (Reviewer):** the whole checklist is yours to trace in the diff. A
  tool that colors piped output or exits `0` on failure is a finding tied to its
  NFR, not a nicety.

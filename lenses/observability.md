---
name: observability
applies-to: [api]
phases: [specify, review]
---

# Observability Lens

Active when the project profile includes **`api`** — a backend service that
runs somewhere and must be operated. A service can be correct (the diff does
what the spec says), contract-clean (the `api` lens) and secure (the `security`
lens) and still be undiagnosable the first time it fails in production. This
lens owns that gap: **can someone who was not there find out what happened?**
It does not re-run the Reviewer's generic correctness hunt.

**Stays silent for:** `library` (no process of its own to operate), `cli`
(the user's terminal is the diagnostic surface; `cli.md` owns stderr and exit
codes), static `website` (no server runtime) and `web-app` frontends. An `api`
that is a throwaway local script or never deployed: the Facilitator leaves the
lens off at `/charter`, with the reason in the profile's "Why it's active (or
off)" column.

**Boundary with `security`.** What must **never** be logged (credentials, PII
in the clear) is `security.md` §2 and §5 — this lens does not restate it. This
lens asks only whether the logs, metrics and signals that *should* exist do.
Where a check touches both, cite the finding once, under `security` for the
leak and under this lens for the missing signal.

Like every lens, it flags concerns and proposes NFRs; it never invents scope.

## Who owns what

| Area | Owner phase | Agent |
|---|---|---|
| Diagnosability expectations make it into the spec as NFRs | Specify | Product Owner |
| Logging, health, correlation, error reporting, alertable signals in the diff | Review | Reviewer |

> **No QA row and no Act row.** `/demo-day` is browser-shaped and an `api` has
> no UI to click; `/increment` dispatches no lens files. The Act check is
> realized through the spec's `NFR-n` and the plan's `Covers` column. Expect
> the Review gate to carry the weight.

## The checklist

### 1. Logs *(Review)*
- [ ] Logs are **structured** (key/value or JSON) and carry level, timestamp and the event's identifying fields, not free-text only.
- [ ] Each failure path logs once, at the right level, with enough context to find the cause (operation, input identifiers, upstream target) — no swallowed exception, no `catch {}` that returns a generic 500 silently.
- [ ] No log call inside a hot loop or per-item of an unbounded collection at `info` or above.
- [ ] *(What must not appear in a log line: see `security` lens — not checked here.)*

### 2. Correlation *(Review)*
- [ ] Each request gets a **correlation/request ID** (accepted from the caller or generated), included in every log line for that request, and returned to the client (header or error envelope) so a user report can be traced.
- [ ] The ID is propagated on outbound calls to other services, queues and jobs the request triggers.

### 3. Health & readiness *(Review)*
- [ ] A liveness and a readiness (or one honest health) endpoint exists, unauthenticated (stated as deliberately public, per `api` §4) or on an internal port, and readiness reflects real dependencies (database, queue), not a constant `200`.
- [ ] Startup failure from missing config or an unreachable required dependency is loud (non-zero exit with a logged reason), not a process that starts and fails every request.

### 4. Metrics & alertable signals *(Review)*
- [ ] The diff exposes, or reuses existing, request rate, error rate and latency per route/operation; a new background job or queue consumer exposes success/failure counts and age or lag.
- [ ] Failures a human must act on (job dead-lettered, dependency circuit open, data-integrity check failed) emit a **distinct, named signal** (metric, error-level event) an alert can key on — not only a line buried in info logs.

### 5. Error reporting & tracing *(Review)*
- [ ] Unhandled exceptions reach an error reporter or at least a structured error log with stack and correlation ID.
- [ ] Where the project already uses distributed tracing, new outbound calls and handlers create spans rather than silently breaking the trace. If none is in use, this item is N/A, not a finding.

## Phase notes

- **Specify (PO):** turn only the relevant expectations into measurable NFRs —
  e.g. "every request log line carries a request ID returned in the
  `X-Request-Id` header", "`/ready` fails when the database is unreachable",
  "the new import job reports success/failure counts". If the feature adds no
  runtime behaviour, record a conscious N/A rather than inventing an NFR.
- **Review (Reviewer):** trace each item in the diff. A missing signal is a
  finding tied to its `NFR-n`; with no NFR, the severity is at most Minor
  unless the diff removes or breaks an existing signal (Major). Prompt
  material makes this check likely, never certain: it is an instruction to
  the agent, not an enforcement.

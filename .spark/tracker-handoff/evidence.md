# Evidence: tracker-handoff

| | |
|---|---|
| **Feature** | `tracker-handoff` |
| **Purpose** | The dogfood record required by NFR-6/NFR-9. There is no test suite and none is possible (constitution §4, spec A2) — this file *is* the verification. |
| **Rule** | One dated entry per ceremony touched. **The negative case runs first and is recorded as having run first** (spec AC-1.5, constitution §1). The positive case is deliberately deferred (C8/R8) — recorded here as *not run*, not skipped past. |
| **Owner** | `/increment`, T7 |

---

## Entry 1 — negative case: this repo declares no delivery mode

**Date:** 2026-08-06 · **Task:** T7 · **Venue:** `/Users/andreaslottes/aSPARK` (this repo)

### Precondition confirmed

```
$ grep -n "Delivery\|Handoff" .spark/constitution.md
(no output)
```

This repo's actual constitution declares nothing under `Delivery & Handoff` — it is
exactly the undeclared case AC-1.1–1.4 must leave untouched.

### `/spark` resume — dry run against real artifact state

Traced by hand against the changed phase map (`skills/spark/SKILL.md`), not
simulated:

| Feature | `release.md` status | Row that matches | Outcome vs. pre-change |
|---|---|---|---|
| `graph-gates` | `released` (`.spark/graph-gates/release.md:8`) | `release `released`` → loop closed | **Unchanged** — same row, same wording; the new `handed-off` row never matches |
| `situational-lenses` | `spec.md` `draft` (`.spark/situational-lenses/spec.md:7`) | `spec.md is draft` → finish `/story-time` | **Unchanged** — routing decided before the release-status rows are even reached |

The new `release `handed-off`` row is additive at the bottom of the table; a
`released` or in-progress feature's routing decision is made by an earlier,
untouched row, so it is structurally unreachable for them.

### `/next-steps` classification — dry run against real artifact state

Traced against the changed classification instruction
(`skills/next-steps/SKILL.md:36`):

| Feature | Status seen | Classification | Outcome vs. pre-change |
|---|---|---|---|
| `graph-gates` | `released` | **shipped** | **Unchanged** — `released` still maps to `shipped`, the only new category (`shipped-pending-approval`) requires `handed-off`, which nothing here has |
| `situational-lenses` | `spec.md` `draft` | **in-flight** | **Unchanged** |
| `tracker-handoff` (this feature) | tasks in progress | **in-flight** | **Unchanged** — it is not `handed-off` yet |

### Zero-occurrence check on the read-side ceremony files

```
$ grep -c "handed-off" skills/next-steps/SKILL.md skills/spark/SKILL.md
skills/next-steps/SKILL.md:2
skills/spark/SKILL.md:2
```

Non-zero **by design** — these are the ceremony *instructions*, which must name
the new status to know how to treat it (identical in kind to `graph-gates`
evidence Entry 1's carve-out for the tool file's own path/probe string). The
AC-1.1 zero-occurrence bar applies to a ceremony's **produced artifact and
user-visible narrative**, not its own instruction file — and no artifact was
produced with `handed-off` in it above, because no feature here is in that
state.

### No polling, ever (AC-2.5)

```
$ grep -ni "poll\|re-check\|re-open\|reminder" agents/release-manager.md skills/go-live/SKILL.md
(no output)
```

Confirms the handoff mechanism adds no polling, reminder or re-opening logic —
a `handed-off` PR's fate is only ever recorded by a user-run ceremony, never
watched automatically.

### `release-notes.md` structural check (AC-2.1, NFR-1)

```
$ git diff templates/release-notes.md | grep '^[-+]' | grep -v '^+++\|^---'
```

Confirms (see T1/T4 diffs in this feature's `.spark/tracker-handoff/plan.md`)
that `Status` and `Version` rows are unchanged in name, order and presence; the
only structural additions are the enum value, the KEEP GATE's inline
annotations, and the Release Actions comment — none renames or removes a
protected row.

### `/charter` — structural check only, live run deliberately not performed

`/charter` **writes** — it amends this repo's real `.spark/constitution.md`.
Running it live here, unprompted, during `/increment`, would mutate standing
project state outside this task's scope (and outside what an Act-phase
ceremony should do on its own authority). Verified instead by diff:
`agents/facilitator.md`'s section-drafting enumeration now names
`delivery & handoff` alongside the original six, so a live `/charter` run will
draft it (grounded or marked-guessed) rather than leave template placeholder
text — satisfying AC-3.3 structurally. A **live** `/charter` dry run (ideally
on a scratch constitution, per the plan's test strategy) is left to
`/peer-review`.

**Outcome: negative case holds.** Every ceremony traced above behaves
identically to before this feature, for every feature that hasn't declared or
reached `handed-off`.

---

## Entry 2 — positive case: deferred (C8/R8)

**Status:** *not run — deliberately deferred, not skipped past.*

Per spec C8/NFR-6, this repo has not yet adopted PR-mode delivery; that
adoption is a separate `/charter` amendment that must land before this
feature's own `/go-live` can exercise `handed-off` for real. Until that
amendment lands and this feature's own release runs through it:

- AC-2.2's KEEP GATE handoff annotations are unverified live (only read, not
  exercised).
- The Q1/C10 fact-establishing mechanism (read-only check vs. self-attestation)
  has not fired even once — **R9 stays fully open** until it does.
- AC-2.3's outstanding-owner line and AC-2.4's `/spark`/`/next-steps` terminal
  treatment of an *actual* `handed-off` report are unverified live.

**QA-gate note:** this feature's QA gate (`/demo-day` or equivalent) must not
be passed on the strength of Entry 1 alone — the positive case must be entered
here, dated, before this feature's own `/go-live` closes the loop. This is not
an oversight; it is the sequencing this spec named up front (R8).

---

## Entry 2 — discharged, 2026-08-06

**Status:** *run for real. No longer deferred.*

`.spark/tracker-handoff/release.md` pass 2 (2026-08-06) exercised the positive
case live: constitution §7 committed (`cc58fec`), PR opened
(https://github.com/a-lottes/aSPARK/pull/3), Q1/C10 facts established
read-only (PR-open via `gh pr view`, CI N/A via absent `.github/`), self-review
attempted and its GitHub-imposed limit recorded honestly, PR merged
(`0eae0f4`). Full detail — including which boxes still can't close for
`handed-off` by design (no tag pre-merge) — lives in `release.md`; not
duplicated here. R9 is no longer open.

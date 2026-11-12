# Evidence: trail-closing-and-cost-controls

Prompt material only: every rule here makes a behaviour likely, not certain. **No rate was
observed.** One session per case, one model (`sonnet`), 2026-11-12. This change was made
directly, on the user's instruction, without a spec, plan, review or QA artifact of its own;
this file is its whole trail.

## Why

Measured on agent runs of the full loop on a real repo (not in this repository):

- Sessions started with `/spark` wrote code within the first 15 to 25 seconds, before a plan
  existed.
- The sessions' own closing statements about what had passed were mostly wrong when
  compared with the `Status` rows on disk.
- One loop cost 25 to 42 times the output tokens of a single plain session; close to 60
  percent went to the two agents pinned to `opus` (Engineering Manager, Reviewer).

## What changed

| Change | Where the agent reads it |
|---|---|
| Closing status block built from the header tables at the moment the last message is written | `skills/spark/SKILL.md` step 8, plus one rule |
| No code before an approved plan (instruction; enforcement is `aspark-guard` 0.3.0) | `skills/spark/SKILL.md` Input and Rules |
| Every agent defaults to `sonnet` | `model:` in all seven `agents/*.md` |
| Model per role from constitution §11 | the Delegate step of all nine delegating skills |
| Reviewer rounds capped at two, read from the `Round` row; constitution §11 can change it | `skills/peer-review/SKILL.md` step 4, `skills/spark/SKILL.md` step 6 |

## Negative baseline (before the edit)

`grep -rn "Reviewer rounds\|Models & Limits\|Close from the trail" skills agents templates`
on `origin/main` (2c84ad5) → empty. `grep -n "^model:" agents/*.md` → `opus` for
`engineering-manager` and `reviewer`, no line for the other five.

## Dry run: `/spark` resume at review round 2 with an open Major

Fixture: a scratch repo with `spec.md` `approved`, `plan.md` `approved` with 2 of 2 tasks
`done`, `review.md` `changes-requested`, `Round` 2, one open Major (F1), no `qa.md`, no
`release.md`, no constitution. Command, same for both cases apart from the plugin directory:

```bash
claude --plugin-dir <core> -p "/aspark:spark" --model sonnet --max-turns 30
```

| | Before (`origin/main`, 2c84ad5) | After (this change) |
|---|---|---|
| Round cap | Announced a third review round as the next step ("That would be round 3 of the review phase") | Stopped: "The Reviewer cap is two rounds, and there's no constitution that sets a different number … I'm not starting one without your decision" |
| Reviewer or `/increment` invoked | no (see limit below) | no |
| Closing status table | absent; statuses given as prose bullets | present, five rows, values matching the files (`approved`; `approved`, 2 of 2 `done`; `changes-requested`, 2, the `Open:` line verbatim; `qa.md` and `release.md` `missing`) |
| `Loop:` line | absent | present, but not in the fixed wording: it read "open, next: `/increment` (fix-mode), then `/peer-review`" plus a sentence |
| Files changed (`git status --short`) | none | none |

**Misses in the one run of the changed version.** The three options offered were one more
round, `/sprint-plan`, and stopping; **waiving the Major was not offered**, although step 4
names it. The model recommended granting the extra round; it
did not take it.

**Limit of the baseline.** The old version stopped before the fix round only because the
`-p` session was denied a read of `skills/increment/SKILL.md` in the worktree, not because
of a rule. So the baseline shows what it intended (round 3), not what it would have done.

## Not verified live

- **Model selection.** No ceremony was run far enough to invoke an agent, so neither the
  `sonnet` default nor a §11 override passed with an agent call has been observed.
  `⚠ not-verified-live`.
- **The closing block after `/go-live`** and at any stop other than the round cap.
  `⚠ not-verified-live`.
- **The cap with a constitution that names another number.** `⚠ not-verified-live`.
- **"No code before an approved plan"** as an instruction: not run. Its measured failure is
  the reason the enforcement lives in `aspark-guard`.
- **`/charter` leaving §11 out by default.** `⚠ not-verified-live`.
- **Whether `sonnet` as Reviewer finds what `opus` found.** Not measured. This is a cost
  decision with an unknown quality effect; §11 is the way back.

## Structural audits

- `claude plugin validate .` → passed, 2026-11-12, CLI 2.1.322.
- `grep -c "Pick the model first" skills/*/SKILL.md` → 1 in each of `backlog`, `charter`,
  `demo-day`, `go-live`, `look-and-feel`, `next-steps`, `peer-review`, `sprint-plan`,
  `story-time`; 0 in `spark`, `increment`, `campaign` (they invoke no agent themselves).
- `git ls-files '*.py'` empty; no executable code added.
- No protected template structure renamed or removed; `templates/constitution.md` gains an
  optional §11, the `aspark-template` marker is unchanged.

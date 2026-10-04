# adversarial-gates — Evidence

Increment 1 (US-1 + US-4). Quoted outputs are verbatim; scratch fixtures live outside the repo.

## T1 — Walking skeleton and baselines

- **Branch:** `feat/adversarial-gates`, cut from `origin/main` (not from `docs/campaign-core-released`); spec + plan are the first commit (`fe2025a`).
- **Base SHA:** `fa33f2ccc91f640f8efd623b9e29391c86f22e28` (`origin/main`). "Base" below is a git worktree of this SHA.
- **`claude plugin validate .`** (Claude Code 2.1.289):

```
⚠ Found 1 warning:

  ❯ root: CLAUDE.md at the plugin root is not loaded as project context. To ship context with your plugin, use a skill (skills/<name>/SKILL.md) instead.

✔ Validation passed with warnings
```

- **`git ls-files '*.py'`:** empty.
- **`wc -l skills/*/SKILL.md`** (pre-change):

```
      97 skills/charter/SKILL.md
     120 skills/demo-day/SKILL.md
      94 skills/go-live/SKILL.md
      79 skills/increment/SKILL.md
      67 skills/look-and-feel/SKILL.md
     107 skills/next-steps/SKILL.md
      80 skills/peer-review/SKILL.md
     136 skills/spark/SKILL.md
      78 skills/sprint-plan/SKILL.md
     116 skills/story-time/SKILL.md
     974 total
```

- **Dry-run harness proof.** Scratch repo: one commit `init`, `README.md` = `# Notes app` / `A tiny CLI that stores notes.`, no `.spark/`. Command: `claude -p "/aspark:next-steps" --plugin-dir <base worktree> --max-turns 8`. Exit 0. Output, verbatim:

```
There's nothing to propose from yet. The repo has one commit ("init"), a 42-byte README, and no `.spark/` directory. That means no shipped features, no in-flight or stalled work, and no open findings.

There's also no `.spark/constitution.md`. I recommend running **`/charter`** first. It sets the project's standing principles and constraints, which is what a good proposal would be measured against. I won't invoke it for you. If you'd rather skip it, say so and I'll continue. With a brief this thin, though, I'd only be asking you for the first idea.

Which way do you want to go?
1. Run `/charter` now.
2. Skip it and tell me the first idea or theme you have in mind. I'll pass that to the Product Owner, or you can go straight to `/story-time <idea>` or `/spark <idea>`.
```

## Method (T2) — written and committed before any scan

**A search, not a census.** The corpus is what the terms below find in the scope below, read by the session's Grep and Read tools. No script. A gate evasion the terms miss is not in it; no completeness is claimed.

**Scope.** `ls .spark/*/{review,qa,evidence}.md`, minus this file (`.spark/adversarial-gates/evidence.md`, which is the output, not a source): **51 files** across 17 feature folders. Only text already committed on `origin/main` counts. Quotes come from `.spark/` only (NFR-9).

**Search terms** (case-insensitive, each run over the whole scope): `skipp`, `bypass`, `evad`, `rationali`, `waiv`, `rounded up`, `generous`, `lenient`, `without (asking|the user|approval)`, `self-approv`, `set .*approved`, `proceeded`, `silently`, `unlogged`, `simulat`, `trust(ed)? (the|its) (prior|earlier)`, `did not (re-?)?(run|verify|read)`, `claimed .* (pass|done|verified)`. Every hit is read in context (±5 lines) before it is classed or dropped. Dropped hits are not listed.

**Gate unit (D2).** A *gate* is one ceremony's gate step: the gate check or gate close in a named `skills/<s>/SKILL.md`. An entry is attached to the one gate whose rule was evaded; if no gate rule was evaded, it has no gate and cannot be `agent-evaded-gate`.

**Entry schema (D1).** Each entry has: `E<n>` · verbatim quote · `file:line` (the quote must match that line) · gate (skill + step) · class · acting context (`ceremony session` or `<role> agent`) · US-2 flag (`yes` for every `verdict-rounded-up`, else `no`).

**Classes — decision rules.** Decide in this order; the first rule that fits wins. When two classes fit, the entry takes the one that does *not* count toward the threshold.

1. `agent-evaded-gate` — an agent (the ceremony session or a role agent) **skipped, bypassed, or satisfied by assertion** a rule a `SKILL.md` gate step states, *and the trail records that it did*. Both halves are needed: a stated gate rule, and a recorded act that did not meet it.
   - *Boundary example (in):* a session set a status to `approved` without the user's explicit approval that the gate-close step requires.
   - *Boundary example (out):* a reviewer found that a gate was evaded by something other than an agent's own act (a human instruction, a tool fault). That is `other`.
2. `verdict-rounded-up` — a review or QA **verdict, severity, or pass mark was more generous than the evidence** (a partial check marked pass, a finding downgraded without a cited reason), with no gate step evaded.
   - *Boundary example (in):* "partial pass" counted as pass in a QA Result cell.
   - *Boundary example (out):* a finding the reviewer *later corrected itself* in the same round because new evidence appeared. That is ordinary review, not an entry.
3. `other` — everything else that is a real over-claim but fits neither: a doc claim stronger than its evidence, a waiver the user granted knowingly, a fix that invalidated an earlier waiver.
   - *Boundary example (in):* a README sentence that asserted an enforced guarantee for a prompt-level check.
   - *Boundary example (out):* anything the trail shows the user knowingly accepted with the facts in front of them is not an evasion at all; drop it.

**What does not count.** A finding that a reviewer *caught* and the fix pass *repaired* is still an entry if the original act matches a class (the evasion happened); but a hit that is only a reviewer's hypothetical ("would have skipped") is dropped. A rule restated in many files is **one** entry per distinct act, not one per mention.

**Threshold (AC-1.2).** A gate needs **≥ 2** `agent-evaded-gate` entries from **two distinct acts** (different features or different rounds). `verdict-rounded-up` and `other` never count (C10). Entries are never merged or split after the scan to move a gate across the threshold.

**Ruling order.** T3 scans and counts; T4 rules which gates qualify; both read this section, which is not edited after its commit. A needed change is a deviation recorded in the plan, not an edit here.

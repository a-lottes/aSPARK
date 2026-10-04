# campaign-start — Evidence

A *performed step* is a real `claude -p` session on a scratch repo outside this repo, with the prompt quoted, its output quoted and the repo's `git status --porcelain` observed (plan §3). Scratch fixtures live in the session scratchpad; their full text is given here. Sessions are nondeterministic, so comparisons are by routing, questions asked and the porcelain, never bytes.

## T1 — Negative-case baseline (before `skills/campaign/` exists)

**Plugin under test:** this working tree. Product files equal commit `781a566` (checked: `git diff --stat 781a566 -- skills agents templates campaigns` prints nothing), because the branch's only change since then is the rebase onto `460d6fc` plus `.spark/campaign-start/`. `ls skills` lists 10 entries (charter demo-day go-live increment look-and-feel next-steps peer-review sprint-plan spark story-time). `git ls-files '*.py'` is empty.

**Fixture A** (`cs/a`, three identical copies `a1`–`a3`, one commit `init`, clean porcelain): `README.md` = `# Notes app` / `A tiny CLI that stores notes. Logger module lives in src/log.py.`; `src/log.py` = `import logging`; `.spark/constitution.md` with §1 `Small and honest.`, §2 type `cli`, lenses none, §3 `Python 3, standard library only.`; `.spark/notes/spec.md` with `Status` `approved` and one story `US-1 (Must): add a note` / `AC-1.1: Given text, when `notes add "x"` runs, then it is stored.` No `.spark/campaigns/`.

**(a) Three sessions, all with `--plugin-dir <working tree> --max-turns 10 < /dev/null`:**

1. `claude -p "/aspark:spark"` on `a1`:

```
There's no feature to resume. `.spark/` has a constitution and some notes, but no feature directory.

I won't guess an idea for you. A constitution already exists, so there are two ways to start:

- **`/next-steps`**: the Product Owner looks at the project's current state and proposes one concrete next feature.
- **Your own idea**: run `/spark <your idea>` and I'll start the loop at Specify.

Either way I'll stop at every gate for your decision. The loop runs Specify → Plan → Act → Review → Keep.

Which would you like?
```

2. `claude -p "/aspark:next-steps"` on `a2`:

```
**Recommendation: finish `notes`. Plan and build US-1, and don't start a new feature.**

The repo has an approved spec and no code. `src/log.py` is only `import logging`, so nothing stores notes and there's no CLI or tests. The README describes a CLI that doesn't exist, which doesn't fit "Small and honest". Every other feature (list, search, delete) depends on being able to add a note first. Size is S: one command, one storage mechanism, standard library only. It displaces nothing, since no other work is in flight.

The Product Owner flagged three gaps in the spec to settle before or during planning:
- **AC-1.1:** "it is stored" can't be tested as written. It should say the note is still there after the process exits.
- **Edge cases:** empty text and adding a second note aren't specified. Each needs an explicit in or out decision.
- **Verification:** there's no read path, so checking storage may need a test-only reader. That should be flagged rather than quietly adding a `list` command.

The spec also has no Handoff block, which the feature should add as it moves forward.

**Alternatives it rejected:**
1. **`notes list`:** the natural next step, but it depends on US-1 and isn't specced yet. It's the strongest candidate for the next cycle.
2. **Build out the logger:** it's infrastructure with no user-visible outcome. If the build needs diagnostics, that should be justified inside `notes`.

How do you want to proceed? I can continue with `/spark notes` (the full loop, resuming at Plan) or `/sprint-plan` directly. You can also ask for a different angle or bring your own idea. I won't start either one until you say so.
```

3. `claude -p "plan how we migrate the logger module to structlog"` on `a3` (the unrelated prompt; plan T1's wording); first 25 lines:

```
# Plan: migrate `src/log.py` to structlog

## What exists today
- `src/log.py` is one line: `import logging`. It defines no functions, no config and no handlers.
- Nothing else in the repo imports it. The only other mentions are in `README.md`.
- There are no tests, no dependency manifest (`pyproject.toml` or `requirements.txt`), and no call sites to convert.

This is closer to adding structured logging than migrating it. The risk is small. The real issue is below.

## Blocker: the constitution forbids this
`.spark/constitution.md` §3 says **"Python 3, standard library only."** structlog is a third-party dependency, so the migration breaks that rule as written. You need to decide one of these before any code changes:

1. **Amend the constitution** to allow structlog. This is the straightforward route if you want it. `/charter` is the right tool for the amendment.
2. **Stay on the stdlib.** Build structured output with `logging` plus a small JSON formatter and `extra=`/`LoggerAdapter`. This follows the "small and honest" principle and needs no dependency.

I recommend option 2 for a tiny CLI with no log call sites yet. If you want structlog for its processors, bound context or ecosystem, take option 1. The plan below assumes option 1.

## Steps (assuming the constitution is amended)
1. **Amend the constitution.** Change §3 to "stdlib plus structlog" and record why.
2. **Add dependency management.** Create `pyproject.toml` with `structlog` pinned to a compatible range. There is no manifest today.
3. **Rewrite `src/log.py` as the single configuration point.**
   - `configure(verbose: bool = False)` calls `structlog.configure(...)` once. It is idempotent.
   - Processors are `merge_contextvars`, `add_log_level`, `TimeStamper(fmt="iso")`, `format_exc_info`, then a renderer.
   - The renderer is `ConsoleRenderer` when stderr is a TTY and `JSONRenderer` otherwise.
   - `get_logger(name=None)` returns `structlog.get_logger(name)`.
[... 13 further lines of the session output omitted from this file; the cut is mine, not the session's]
```

`grep -c -i campaign` over the three outputs: `0`, `0`, `0`. Porcelain after: `a1` empty, `a3` empty, `a2` lists only `?? .spark/.guard/` (written by `aspark-guard`, which is loaded in the maintainer's environment; not by a ceremony).

**Fixture B** (`cs/b`, a copy of A): a hand-start as `campaigns/README.md` "Instantiating" describes.

- Session 1, prompt: *"The aSPARK plugin folder is <plugin> (it contains campaigns/ and templates/). Following campaigns/README.md section 'Instantiating a campaign', create a migration-campaign instance named logger-structlog under .spark/campaigns/logger-structlog/campaign.md. Subject: migrate src/log.py to structlog. Observable: running python -c 'import src.log' prints no stdlib logging import. Verifier: a fresh Parity Verifier per slice. Leave anything I have not told you as a blank, and do not approve it."* (`--allowedTools "Read Write Glob Grep"`). Output:

```
I created `.spark/campaigns/logger-structlog/campaign.md` in the working directory (`…/scratchpad/cs/b`). Its status is `draft` and nothing is approved. I haven't committed it.

I copied the template and appended the `migration-campaign` body as §8. I replaced the `SR-5…` row in §4 with the kind's rows SR-5 to SR-9. The kind file has all seven frontmatter keys.

**What I filled in:**
- **Condition:** migrate `src/log.py` to structlog.
- **Observable:** running `python -c 'import src.log'` prints no stdlib logging import.
- **Verifier:** a fresh Parity Verifier per slice.

**What I left blank:**
- Goal approved by / date.
- Thresholds.
- All of the §2 veto record. The mandatory "automatically verifiable" check is unmarked, so it still needs your call.
- Iterations and tokens in §3. The kind gives no token default, so an unset token budget keeps the campaign unstartable.
- The §5 rollback step.
- The §8 slice list (including paths and rollback per slice) and the parity check.

The campaign is not startable until those are filled in. The slice list normally comes from the Strategist, and you approve it together with the goal.
```

Porcelain after: `?? .spark/.guard/`, `?? .spark/campaigns/`. `.spark/campaigns/logger-structlog/campaign.md` exists, `Status` row `draft`. `shasum` (first 12): `6879529d1642`.

- Session 2, prompt: *"Run the campaign at .spark/campaigns/logger-structlog/campaign.md. The aSPARK plugin folder is <plugin>."* (`--allowedTools "Read Glob Grep"`). It refused before iterating. Output, first 22 lines:

```
I stopped before the first iteration. I changed nothing, and the campaign is not startable as written. The file is still `draft`.

**Why it can't run**
- **Goal not approved.** "Goal approved by / date" is blank, and §1–§3 are frozen only at approval.
- **Budget unset.** The iterations and tokens in §3 are empty. The token budget has no default, so the user has to state it, and an unset budget is not waivable.
- **No slice list.** §8 is empty, so there are no slices with owned paths or rollback steps. The Strategist has to cut this list, and you have to approve it.
- **No parity check.** §8 says "(unset — not startable)".
- **Rollback section empty.** §5 has no steps.
- **Veto record unfilled.** The mandatory "automatically verifiable" row is empty.
- **Archaeologist hasn't run.** No characterization tests have been pinned on the old `src/log.py`, and the Migrator can't start until they are green.

**Problem with the goal itself**
- The observable is "running `python -c 'import src.log'` prints no stdlib logging import". That command prints nothing whether or not `src/log.py` imports `logging`, so it can't tell a migrated file from an unmigrated one.
- A decidable version would check something concrete, for example that `src/log.py` has no `import logging` and that `structlog` is imported. It should also say what "parity" means, such as the same output for the same calls.
- I can't edit §1–§3 myself. I'm proposing the wording, and you would record the change with a reason and date.

**What I need from you**
1. A decidable observable and its threshold. I can draft the wording for your approval.
2. The iteration and token budget.
3. Whether the Archaeologist and Strategist should run now as planning-session subagents. The Strategist will then cut the slice list and parity check. After that I stop, and you approve the goal, budget and slices together.
4. The rollback step for §5.
```

`shasum` of the instance after: `6879529d1642` (unchanged); `git log --oneline | wc -l` = `1`; porcelain unchanged.

**What this baseline says.** The hand-start works as documented when the user names the plugin folder in the prompt; the kind file was found and all seven keys were present; the run refuses without goal approval. The loop ceremonies show no campaign mention in a repo without `.spark/campaigns/`. The unrelated migration prompt was answered as an ordinary plan; no skill was invoked (a skill that would have been invoked shows as a `Skill` call; none appears in the output). This is the state T8(b), T8(c) and T11 compare against.

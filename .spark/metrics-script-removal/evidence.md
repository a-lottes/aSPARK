# Evidence: metrics-script-removal

| | |
|---|---|
| **Phase** | Act (`/increment`) |
| **Owner** | Developer (the orchestrating session) |
| **Status** | `in-progress` |
| **Date** | 2026-09-11 |

**Handoff**
- **Status:** `in-progress` — written run by run as tasks complete. Entries are append-only; a superseded number is struck through in place, never deleted.
- **Summary:** The single evidence artifact for this feature. Holds the negative case, the figure derivations (run twice, either side of the `transcripts.root` strip), the recovery commit for the deleted script, and the command sequences `/demo-day` must perform.
- **Open:** see the task table in `plan.md` §3 for what is still `todo`.
- **Binding ruling:** the derivation verdicts in Entry 3 are the **only** permitted source of figures for T6 and T10. A figure not in that table may not be published.
- **On conflict:** `plan.md` §3 wins on task status; this file wins on what was observed.

**Conventions.** Every block below is a real command and its real output, pasted
unedited. `$SCRATCH` stands for the session scratchpad, which is outside the
repository — no absolute path is recorded here (NFR-6). Commands were run from
the repository root unless stated.

---

## Entry 1 — T1, the negative case (before anything is deleted)

Run at `6fd257c`, on branch `feat/metrics-script-removal`.

Constitution §4 requires the negative case first: *"For a change that adds an
optional capability, the negative case runs first — in a repo where the
capability is absent, nothing may change."* The removal's equivalent is the
proof that **nothing in the consumed contract references what is being
removed**, established before the deletion rather than after it. This entry is
committed before T8's deletion commit, so `git log` itself carries the ordering.

### AC-1.4 — no ceremony references the script

```
$ grep -rln 'spark-metrics' skills agents templates lenses tools .claude-plugin
$ echo $?
1
```

Zero hits. `grep` exit 1 is "no lines selected", not an error.

Widened in the same pass to the directory itself, which the deletion also removes:

```
$ grep -rln 'scripts/' skills agents templates lenses tools .claude-plugin
$ echo $?
1
```

Zero hits. **No skill, agent, template, lens, tool file or manifest names the
script or its directory.** Therefore removing it changes no ceremony's behaviour
and owes no deprecation path — spec A6 confirmed, NFR-2 satisfied, and the
removal is not a breaking change to the consumed contract (§6).

### NFR-7 — the project validates before the work starts

```
$ claude plugin validate .
Validating marketplace manifest: .claude-plugin/marketplace.json

⚠ Found 1 warning:

  ❯ autoUpdate: Unknown field 'autoUpdate'. Claude Code ignores it at load time.

✔ Validation passed with warnings
$ echo $?
0
```

Passes. The `autoUpdate` warning is **pre-existing and unrelated** to this
feature — it concerns `marketplace.json`, which NFR-1 forbids this increment to
touch. Recorded as the baseline so that a reviewer can tell this warning apart
from anything this work introduces; it must still be present, unchanged, at T12.

### Baseline counts at `6fd257c`

| Measure | Command | Value |
|---|---|---|
| Tracked files | `git ls-files \| wc -l` | 106 |
| Tracked `.md` | `git ls-files '*.md' \| wc -l` | 89 |
| Tracked `.py` | `git ls-files '*.py' \| wc -l` | **1** |
| Script size | `wc -c < scripts/spark-metrics.py` | 32,654 B |

**Note for T9 (deviation D2 in action).** The constitution's §8 inventory was
written at `/charter` against 104 tracked files / 87 `.md`. This branch's own
`spec.md` and `plan.md` have since made it 106 / 89 — the inventory was already
stale two commits after it was written, which is exactly the drift D2 predicted
and the reason §8 will state its counts **with the commit they were taken at**
rather than as a live claim. The only time-invariant clause is `.py` = 0, which
stays live-verifiable.

### Finding F-jq — `jq` is absent on this machine (raised at T1, blocks T6)

The approved architecture publishes the method as `jq` one-liners
(`plan.md` §1), and T6's definition of done requires that *"every printed
command was pasted into a shell and its observed output recorded"* (NFR-4:
runnable exactly as printed **and observed to run**). `jq` cannot be observed
running here:

```
$ command -v jq
$ echo $?
1
$ for p in /usr/bin/jq /usr/local/bin/jq /opt/homebrew/bin/jq /opt/local/bin/jq ~/.local/bin/jq; do
>   [ -x "$p" ] && echo "FOUND $p" || echo "no $p"
> done
no /usr/bin/jq
no /usr/local/bin/jq
no /opt/homebrew/bin/jq
no /opt/local/bin/jq
no ~/.local/bin/jq
$ command -v brew
$ echo $?
1
```

Absent, and `brew` is absent too, so there is no one-line install. Constitution
§6 forbids installing anything on the user's behalf unasked, so `/increment`
must not resolve this itself. Interpreters that **are** present: `python3`
(3.9.6), `perl`, `ruby` (2.6.10), `node` (v24.18.0).

This is the condition the plan anticipated as risk **R3**, whose named fallback
is the per-project table from §1's rejected alternatives — carrying the flaw the
plan itself recorded against it ("it publishes a derived snapshot as the method
… a reader checking the table against the JSON is checking my transcription,
not the evidence"). Choosing between that fallback, installing `jq` with the
user's go, and a third option changes §1's architecture decision, so it was
**raised to the user rather than decided here** (`/increment` does not improvise
architecture). T2–T5 do not depend on the answer and proceeded; see Entry 2.

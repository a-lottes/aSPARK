# Evidence: graph-gates-verification

| | |
|---|---|
| **Feature** | `graph-gates-verification` |
| **Purpose** | The deliverable itself: performed-run proof for issues #8–#11 plus AC-3.2's ceremony side, under a verify-only fence (spec §1, NFR-2). There is no test suite and none is possible (constitution §4, spec A2) — this file *is* the verification. |
| **Rule** | One dated entry per run: command/ceremony, venue, timestamp, resolved availability facts, exit codes, counted numbers with their counting method, findings. The negative case runs first and is recorded as having run first (AC-1.3). Every environment mutation names its authorization and its restoration (AC-1.2). Reading or reasoning is labelled as such and never passes an AC (NFR-4). Anything not run is labelled *not run*. Several entries cite exact tool-call sequences re-derived from the raw `claude -p --output-format stream-json` transcripts under `/tmp/ggv/*.jsonl` — those files are ephemeral scratch (not committed, do not survive a reboot); the quoted excerpts in this file are the durable record, not the transcripts themselves (`/peer-review` finding F8). |
| **Owner** | `/increment` (T1–T15 of `plan.md`) |

---

## Venue ledger (assigned at Entry 1, from measured state — not assumption)

| Venue | Path | Used by | Declared state | Mutations authorized there |
|---|---|---|---|---|
| V-SILENCE | `/tmp/ggv/silence-repo` (created at T2, disposable) | T2 | no MCP registration, no CLI runner during the window (symlink removed), no `.aspark-graph/` | symlink remove→restore (one sitting); venue dir create/delete itself |
| V-POSITIVE | `/tmp/ggv/positive` (created at T3, disposable) | T3–T7, T12 | source-indexed scratch repo, Core-managed trail with a passing gate, graph built once (`stale:false` at first); per-task registration states logged per entry | one `aspark-graph build`; project-scoped MCP registrations per C10/C15; source edit for the stale case (T12); venue dir lifecycle |
| V-BROWSER | `/tmp/ggv/browser` + throwaway static page served on localhost (created at T8, disposable) | T8–T10 | plain static page; Playwright MCP / Chrome DevTools MCP registered project-scoped per session | page+server lifecycle under Q1/C9; backend registrations under C15 |
| V-HINT | `/tmp/ggv/hint` (created at T11, disposable) | T11 | git repo, seed commit only; `runner=yes` (global symlink), `graph=no` (never built), no `.mcp.json` — built specifically because neither V-POSITIVE (`graph=yes` since T3) nor V-BROWSER matched the required state (Entry 11, `plan.md`'s Deviations) | none beyond ordinary scratch construction (NFR-6) — no build, no registration |
| Core repos | `~/aSPARK`, `~/aSPARK-graph` | read-only reference sites only | as measured in Entry 1 | **none** — zero mutations authorized (C7 precedent); staleness queries against them are read-only |

## Findings

Findings table is consolidated at T13; rows are appended here as they surface.

| ID | Surfaces in | Contradicts | Quote / measurement | Route |
|---|---|---|---|---|
| F1 | Entry 1 (T1) | Spec A3's asserted baseline | A3 asserts "`~/aSPARK` resolves `runner=yes, graph=no`"; measured P3: `~/aSPARK/.aspark-graph/graph.json` exists (56,668 bytes, mtime 29 Jul 18:05, alongside `parse-cache.json`) → resolves `graph=yes`. Cause not traced from within the sweep; the file predates this feature. | Operator-environment drift (Risk R6), not a tool defect — no consumer-repo or Core-side action implied by the measurement itself. Consequence applied: venues are assigned from measured state; `~/aSPARK` is never usable as a silence or positive venue |
| F2 | Entry 5 (T5), reinforced by Entry 12 (T12) | `tools/aspark-graph.md:19-20`: "**MCP first.** … use them. **Run no command.**" — contradicted by `skills/{sprint-plan,peer-review,demo-day}/SKILL.md`'s "Resolve **both** facts", whose only documented method for the second fact is a command (`tools/aspark-graph.md:22`); detection itself unspecified anywhere | Run 1 (Entry 4): `ToolSearch` confirms both MCP tools, then `mcp__aspark-graph__staleness{"repo":"."}` called directly — 0 `Bash` probes before delegation. Run 2 (Entry 5, identical MCP-registered environment): `ToolSearch` confirms both MCP tools, then `Bash: test -f .aspark-graph/graph.json` runs anyway *before* delegation, and `mcp__aspark-graph__staleness` is never called at all in this run. Run 3 (Entry 12, `/peer-review`, same MCP-registered venue): the orchestrator skips `ToolSearch` entirely — no attempt to detect the MCP tools at all — and runs only the *graph.json* half of the CLI probe (`test -f .aspark-graph/graph.json`, never `command -v aspark-graph`), then declares "surface yes / graph.json yes" on that partial basis alone. Five different detection/resolution mechanics observed across the sweep's seven nested-session transcripts. | **Re-routed on `/peer-review` (Round 1, F3):** primarily a Core documentation defect (`tools/aspark-graph.md:19-22` vs. the three SKILL.md's "resolve both facts") — not primarily model variance. See Entry 13's consolidated table for the full routing text. |

---

## Counting domains (binding for every count in this file)

Restated from `.spark/graph-gates/evidence.md` (its AC-1.1 binding reading, user-resolved P-Q1) so no run re-decides it. A "zero mentions of `aspark-graph`/`.aspark-graph`" claim is measured on exactly two surfaces:

1. **The artifact(s) the ceremony produced** (`plan.md` / `review.md` / `qa.md` / whatever the ceremony wrote) — counted over the full file text.
2. **The ceremony's user-visible output** — in `claude -p` runs, all assistant text blocks including the final result message.

**Excluded:** the detection sub-step's own tool calls and their inputs (the probe command and tool-file path unavoidably contain the string); loaded file contents inside context; agent-to-agent tool_result payloads that never reach the user. Method per claim: literal substring count via `grep -c` (lines) and `grep -o | wc -l` (occurrences) over the captured surface files. Nothing else is excluded.

**Divergence from AC-5.1, noted (`/peer-review` finding F11):** AC-5.1 (`spec.md:146`) names three counting surfaces — ceremony messages, produced artifact, and **subagent reports** — while this section declares and covers only the first two, explicitly excluding the agent tool_result payloads where a subagent report lives. This was not re-derived as a third surface for Entry 11's count. Checked directly on re-review: the `Agent` tool_result payload in T11's transcript (`t11-session.jsonl`) contains **0** occurrences of `aspark-graph build` — so Entry 11's total of exactly 1 is unaffected by the gap, but the declared method still doesn't cover a surface the AC names, and a future count under different conditions should not assume it stays zero without checking.

---

## Entry 1 — baseline environment ledger (T1)

- **Run:** neutral-shell probes, all read-only. No mutation performed; nothing to authorize, nothing to restore.
- **Venue:** operator shell, cwd `~/aSPARK` (reference site; probes do not write).
- **Timestamp:** 2026-08-25 19:37:51 +0200.
- **Resolved availability facts:** runner present machine-global via symlink; MCP registered nowhere project-scoped (checked sites listed below); graphs exist in both Core repos.

**P1 — symlink presence**

```
$ ls -la ~/.local/bin/aspark-graph
lrwxr-xr-x@ 1 andreaslottes  staff  56 27 Jul 07:31 /Users/andreaslottes/.local/bin/aspark-graph -> /Users/andreaslottes/aSPARK-graph/.venv/bin/aspark-graph
exit=0
```

**P2 — PATH resolution**

```
$ command -v aspark-graph
/Users/andreaslottes/.local/bin/aspark-graph
exit=0
```

**P3 — resolved state of `~/aSPARK`**

```
$ test -f ~/aSPARK/.aspark-graph/graph.json && echo graph=yes || echo graph=no
graph=yes
exit=0
$ ls -la ~/aSPARK/.aspark-graph/
total 120
drwxr-xr-x@ 4 andreaslottes  staff   128 29 Jul 18:05 .
drwxr-xr-x 21 andreaslottes  staff   672 25 Aug 07:08 ..
-rw-r--r--@ 1 andreaslottes  staff 56668 29 Jul 18:05 graph.json
-rw-r--r--@ 1 andreaslottes  staff   154 29 Jul 18:05 parse-cache.json
```

**P4 — project MCP registrations, `~/aSPARK`**

```
$ cat ~/aSPARK/.mcp.json
cat: /Users/andreaslottes/aSPARK/.mcp.json: No such file or directory
exit=1
```

(absence of the file = no project-scoped MCP registration on this repo)

**P5 — `~/aSPARK-graph` existence and graph state**

```
$ ls -d ~/aSPARK-graph && test -f ~/aSPARK-graph/.aspark-graph/graph.json && echo graph=yes || echo graph=no-or-missing
/Users/andreaslottes/aSPARK-graph
graph=yes
exit=0
```

**P6 — staleness of `~/aSPARK-graph` (read-only query only)**

```
$ aspark-graph query staleness --repo ~/aSPARK-graph
{
  "advice": null,
  "changed": [],
  "files_checked": 107,
  "missing": [],
  "stale": false
}
exit=0
```

**P7 — `~/aSPARK` git state (fence-audit reference for T14)**

```
$ git -C ~/aSPARK status --porcelain
?? .spark/graph-gates-verification/
exit=0
```

**P8 — scratch candidates**

```
$ ls -d /tmp/ggv
ls: /tmp/ggv: No such file or directory
exit=1
```

(no scratch venue exists yet; V-SILENCE/V-POSITIVE/V-BROWSER are created by their tasks)

**Deviations from spec A3:** exactly one — F1 above (`~/aSPARK` measures `graph=yes`, A3 asserted `graph=no`). Symlink presence (P1), runner-on-PATH (P2), and `~/aSPARK-graph` at `stale:false` untouched (P5/P6) all match A3.

**DoD check (T1):** symlink presence captured (P1); resolved state of `~/aSPARK` captured (P3); staleness of `~/aSPARK-graph` captured via read-only query only (P6); `graph.json` presence recorded for every existing candidate venue (P3, P5, P8); deviation logged as finding F1; venue ledger assigns the venue for every later state. **Done.**

---

## Entry 2 — silence case: negative run in V-SILENCE (T2)

- **Run:** `/aspark:sprint-plan` in a fresh session (`claude -p`, stream-json capture), inside V-SILENCE on fixture feature `ggv-silence-check` (minimal spec, Status `approved` — written pre-window so the ceremony's gate passes and the availability-resolution step is actually reached; an empty venue would stop at the gate *before* probing, which proves nothing).
- **Venue:** `/tmp/ggv/silence-repo` — verified immediately pre-window: no `.mcp.json`, no `.aspark-graph/`; user-scope MCP inventory empty (`jq '.mcpServers' ~/.claude.json` → no keys). Fixture spec at `.spark/ggv-silence-check/spec.md`.
- **Timestamps:** window opened 19:43:39, window closed 19:50:15 (+0200, 2026-08-25).
- **Authorization:** user granted standing sweep authorization this session (2026-08-25): scratch dirs under `/tmp/ggv`; symlink remove→restore windows bracketed by probes, never `PATH` overrides; fresh `claude -p` sessions as the standing instrument. Recorded here per instance.
- **Mutation log:** `rm ~/.local/bin/aspark-graph` at 19:43:39 → confirmed gone (`command -v` → not found; target binary untouched) → single T2 run → `ln -s ~/aSPARK-graph/.venv/bin/aspark-graph ~/.local/bin/aspark-graph` at 19:50:15. No other work interleaved.

**Session invocation (verbatim):**

```
cd /tmp/ggv/silence-repo && claude -p "/aspark:sprint-plan" \
  --output-format stream-json --verbose --dangerously-skip-permissions
```

(`--dangerously-skip-permissions` because the run must execute its real probe path unattended; venue is a throwaway empty repo, nothing else was running in it.)

**What the session did (from transcript, 1938 stream-json lines):** 9 tool calls, in order —

1. `Bash`: list `.spark/` (gate check)
2. `Bash`: grep `status` in fixture spec (gate check)
3. **`Bash`: THE availability probe** — verbatim: `command -v aspark-graph >/dev/null 2>&1 && echo runner=yes || echo runner=no; test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no`
4. `Agent`: Engineering Manager delegation (no tool file passed — neither fact held)
5. `Read` fixture spec · 6. `Read` plan template · 7. `Glob`
8. `Write` `.spark/ggv-silence-check/plan.md`
9. `Bash`: grep/wc self-check of the produced plan

**Probe result:** `runner=no\ngraph=no`, `is_error: False` (exit 0 corroborated by normal continuation). Run finished `success`, 6 turns, 327,878 ms.

**Counts (method per Counting domains above):**

| Surface | File counted | `aspark-graph` | `.aspark-graph` |
|---|---|---|---|
| 1 — artifact produced | `/tmp/ggv/silence-repo/.spark/ggv-silence-check/plan.md` | **0** lines / 0 occurrences | **0** |
| 2 — user-visible output | all assistant text blocks incl. final result | **0** | **0** |

Narrative quotes (surface 2, verbatim): *"Spec gate passed — `ggv-silence-check/spec.md` status is `approved`. No MCP staleness/impact tools in this session, so probing once for the graph runner:"* → *"Runner and graph both absent — proceeding without the graph tool."* — after which the session plans normally and never mentions the tool again. No hint sentence, no tool-file handover, no build suggestion.

**Gate outcomes unchanged:** the ceremony behaved exactly as with the tool present-but-absent-state: plan drafted to template (111 lines, header `Status: draft`, full PLAN GATE section), handed back for approval. Nothing about the absent tool altered any gate.

**Restoration probes (re-run of Entry 1's P1–P8):** P1'–P8' all match baseline state facts — same symlink target & resolution (P1'/P2'), `~/aSPARK` graph=yes (P3'), no `.mcp.json` (P4'), `~/aSPARK-graph` graph=yes (P5'), staleness byte-identical `stale:false / files_checked:107` (P6'), git state unchanged (P7'). Two honest notes: (a) P1's `ls` mtime field differs (25 Aug 19:50 vs baseline 27 Jul 07:31) — inherent metadata of remove→recreate; environment *state* is identical, and the link length/target are identical; (b) P8 now finds `/tmp/ggv` — expected: it is this sweep's declared venue root.

**Instrument caveat (recorded, not affecting the claim):** child-session stderr showed two warnings — an auth-source precedence notice and an `unrecognized_model` notice ("stealth/ox-alpha", the parent session's model id leaking via env; child ran on fallback). The silence behavior under test is ceremony logic, not model identity; noted for reproducibility.

**AC mapping:** AC-1.1 ✓ (0 mentions both surfaces, probe exit 0, gates unchanged) · AC-1.2 partially satisfied (this entry logs authorization + restoration + matching post-probes; the *post-sweep* final probe is T14's) · AC-1.3 ordering fact established (silence case precedes all positive runs — no positive entry exists yet).

**DoD check (T2):** symlink temporarily removed with authorization/removal/restoration logged, removal not a `PATH` override ✓; wired ceremony step 1 ran in ledger-confirmed `no/no` venue ✓; transcript quoted, counts 0 on both declared surfaces ✓; probe exit 0 ✓; gate outcomes unchanged ✓; restored-environment probes match Entry 1 (state facts verbatim; mtime note above) ✓. **Done.**

---

## Entry 3 — V-POSITIVE prepared: scratch repo with built graph (T3)

- **Run:** venue creation + one authorized `aspark-graph build` + performed staleness query.
- **Venue:** `/tmp/ggv/positive` (V-POSITIVE per ledger) — git repo, seed commit `fixture: positive venue seed`; indexed source: `calc.py`, `greet.py`, `README.md`; Core-managed trail: `.spark/positive-fixture/spec.md` with Status `approved` (gate-passing for `/sprint-plan`).
- **Timestamp:** 2026-08-25 19:58 (+0200).
- **Authorization:** standing sweep grant (see Entry 2) covers scratch builds in declared venues only (NFR-6). This is that one build.
- **Mutation log:** `(cd /tmp/ggv/positive && aspark-graph build .)` →

```
Built graph: 5 code entities, 3 artifact entities; full rescan
Saved to .aspark-graph/graph.json
build-exit=0
```

Artifacts on disk: `.aspark-graph/graph.json` (2,156 bytes), `.aspark-graph/parse-cache.json`.

**Performed staleness query:**

```
$ aspark-graph query staleness --repo /tmp/ggv/positive
{
  "advice": null,
  "changed": [],
  "files_checked": 2,
  "missing": [],
  "stale": false
}
query-exit=0
```

(`files_checked: 2` = the two indexed source files; genuinely fresh here, unlike the vacuous case of §2.)

**DoD check (T3):** scratch source-indexed repo outside this repo holds a gate-passing Core-managed trail ✓; build ran exactly once, logged with authorization ✓; performed staleness query returns `stale:false` ✓; venue path and outputs recorded ✓. **Done.**

---

## Entry 4 — MCP branch resolves and decides (T4)

- **Run:** `/aspark:sprint-plan` in a fresh session (`claude -p`, stream-json capture), inside V-POSITIVE on the fixture feature `positive-fixture` (spec `approved`), with the `aspark-graph` MCP server registered project-scoped beforehand.
- **Venue:** `/tmp/ggv/positive` (unchanged since Entry 3: `.aspark-graph/graph.json` present, `stale:false`, 2 files indexed).
- **Timestamp:** registration 2026-08-26 20:26 (+0200); session ran 2026-08-26 20:28–20:33 (+0200, from the `t4-session.jsonl` transcript's own timestamps) — one day after Entries 1–3 (session resumed).
- **Authorization:** C10 grant (project-scoped registration of `aspark-graph` to the positive venue only), invoked here for the first time in the sweep.
- **Mutation log:** `claude mcp add --scope project aspark-graph -- aspark-graph serve` run from `/tmp/ggv/positive`, writing `/tmp/ggv/positive/.mcp.json` (`{"mcpServers":{"aspark-graph":{"type":"stdio","command":"aspark-graph","args":["serve"],"env":{}}}}`). Registration is durable venue state (V-POSITIVE is reused by T5–T7, T12 per the ledger) — not removed after this run; no restoration is owed for a project-scoped file living inside a disposable scratch venue outside this repo, which needs no cleanup on any NFR here (unlike the machine-global symlink in Entry 2). `/demo-day` finding B1: this venue was in fact still present on disk a day later — "disposable" describes what it's authorized to be discarded as, not a claim that discarding already happened.
- **Auto-mode classifier note:** the nested `claude -p --dangerously-skip-permissions` invocation was refused once by the session's auto-mode permission classifier before the user explicitly approved this specific command; recorded for reproducibility, not a finding about the tool under test.

**Session invocation (verbatim):**

```
cd /tmp/ggv/positive && claude -p "/aspark:sprint-plan" \
  --output-format stream-json --verbose --dangerously-skip-permissions
```

**What the session did (from transcript, 137 stream-json lines), tool calls in order:**

1. `Bash`: list `.spark/` (gate check)
2. `Bash`: cat fixture spec (gate check) → "Gate passed — spec is `approved`. Now resolving optional tool availability for the graph surface."
3. **`ToolSearch`: `select:mcp__aspark-graph__staleness,mcp__aspark-graph__impact`** — the MCP tools resolve as present
4. `Read` the tool file (`tools/aspark-graph.md`)
5. **`mcp__aspark-graph__staleness`** `{"repo": "."}` → `stale:false, files_checked:2`
6. `Bash`: check for `.spark/constitution.md`, list feature dir (unrelated to availability)
7. Text: *"No constitution file. Graph is available and fresh, so I'll pass the tool reference to the Engineering Manager along with the plan template. Delegating now."*
8. `Agent` → `aspark:engineering-manager`, prompt states plainly: *"You do not have a shell of your own to run `aspark-graph` or call its MCP tools directly; if you want an `impact` or `staleness` query run, return a **tool query request** … and I will run it and hand you the result."* (matches the agent's own tool grant — `agents/engineering-manager.md` lists `Read, Grep, Glob, Write` only, no MCP tools; the orchestrator-runs/subagent-requests split is the designed mechanism, not a defect)
9. Subagent reads spec/template/tool file, drafts the plan, then emits a tool query request instead of calling anything itself
10. **`mcp__aspark-graph__impact`** `{"files": ["greet.py","banner.txt","test_greet.py"], "repo": "."}` → `found:true`, `greet.py` in-graph (`def:greet.py::greet`), `banner.txt`/`test_greet.py` in `unknown_files`
11. `SendMessage` relays the raw result back to the subagent, which edits §2 of the plan to cite it (framing the empty `affected_stories`/`affected_acs` as structural, per the tool file's own instruction)
12. Plan finalized (86 lines, `Status: draft`), presented for the user's architecture veto

**Literal MCP tool names cited (AC-2.1):** `mcp__aspark-graph__staleness`, `mcp__aspark-graph__impact` — both exposed and both used; no other name variant appeared.

**Probe-command count (method per Counting domains above, ceremony-emitted output/artifacts only):** **0.** The transcript contains the literal strings `command -v aspark-graph` / `.aspark-graph/graph.json` only 3 times, all inside `tool_result` payloads of `Read` calls on `tools/aspark-graph.md` itself (loaded file content — excluded by the declared counting domain, per the B7 lesson). No `Bash` call in the session matches either probe form; the 3 `Bash` calls present (gate-check listing, spec cat, constitution check) are unrelated to availability resolution.

**AC mapping:** AC-2.1 ✓ — MCP branch taken, both exposed tool names cited literally, 0 probe commands counted. AC-2.4 not triggered this run (registration succeeded, tools appeared) — its finding path remains untested until a failure occurs, if one does.

**DoD check (T4):** MCP server registered project-scoped on the scratch venue with C10 terms logged ✓; wired ceremony resolves the MCP branch ✓; entry cites literal registered tool names ✓; 0 probe commands counted ✓; no registration failure occurred (finding path not exercised — noted, not silently skipped: nothing to route). **Done.**

---

## Entry 5 — determinism: second run, resolution compared (T5)

- **Run:** two second-run attempts of `/aspark:sprint-plan` in V-POSITIVE, identical MCP-registered environment to Entry 4.
- **Attempt A (discarded as confounded):** `/tmp/ggv/t5-session.jsonl`, run 2026-08-26 ~20:33. `positive-fixture/plan.md` still existed as the `draft` artifact Entry 4 wrote. The gate check found it already fully drafted and re-presented it for approval without re-entering availability resolution at all (no `ToolSearch`, no tool call, no probe) — a different code path than Entry 4's, not a comparable second observation. **Discarded per this entry's own DoD** ("identical environment" must mean the resolution step is actually re-entered, not skipped by an already-drafted artifact) rather than counted as evidence either way.
- **Reset:** `rm .spark/positive-fixture/plan.md` in V-POSITIVE (disposable scratch, NFR-6) to restore the venue to its pre-resolution state, then reran.
- **Attempt B (counted):** `/tmp/ggv/t5b-session.jsonl`, run 2026-08-26 ~20:35–20:41. Same venue, same `.mcp.json`, same built graph.

**Side-by-side resolution comparison:**

| | Entry 4 (run 1) | Entry 5 attempt B (run 2) |
|---|---|---|
| Gate check | `Bash` × 2 (list `.spark/`, cat spec) | `Bash` × 3 (list `.spark/`, grep status × 2) |
| Tool discovery | `ToolSearch: select:mcp__aspark-graph__staleness,mcp__aspark-graph__impact` → both found | `ToolSearch: select:mcp__aspark-graph__staleness,mcp__aspark-graph__impact` → both found |
| Staleness/graph-presence check | **`mcp__aspark-graph__staleness{"repo":"."}`** — MCP call, no shell command | **`Bash: test -f .aspark-graph/graph.json`** → `graph=yes` — a probe command, MCP `staleness` tool never called this run |
| Declared conclusion | "Graph is available and fresh" | "Both hold — MCP surface available and graph exists" |
| Probe commands before delegation | **0** | **1** |
| Delegation | `Agent → aspark:engineering-manager` | `Agent → aspark:engineering-manager` |
| Later MCP use | `mcp__aspark-graph__impact` (relayed for subagent) | `mcp__aspark-graph__impact` (relayed for subagent) |

**Same:** both runs reach the same declared conclusion (MCP-registered surface, graph present/fresh) and the same branch label (MCP, not CLI-only) in their final delegation. Both relay exactly one `impact` query for the subagent later.

**Different — Finding F2:** run 2 executes a probe command (`test -f .aspark-graph/graph.json`) that run 1 did not, and never calls the `staleness` MCP tool that run 1 called directly — despite `ToolSearch` confirming the same two tools available in both sessions. This contradicts the tool file's "Run no command" instruction and AC-2.1's zero-probe-command requirement, on the *second* of two otherwise-identical runs. See Finding F2 above for the full quote/route.

**AC mapping:** AC-2.2 ("resolves identically … same branch, same declared surface") — **partially confirmed, partially refuted** per C4 (a failed AC is itself a valid outcome). The declared branch and surface conclusion match; the mechanics behind reaching it (probe-command count, which tool is actually invoked) do not, which is precisely what AC-2.1 also requires to hold on every run, not just the first.

**DoD check (T5):** second fresh session run in the identical registered environment ✓ (attempt B, after discarding the confounded attempt A and recording why); entry shows both resolutions side by side ✓; **outcome is a refutation of full identity, not a confirmation** — recorded as such, not smoothed over. **Done** (verification-only DoD: showing the comparison, whichever way it falls).

---

## Entry 6 — control: CLI branch in a no-MCP session (T6)

- **Run:** `/aspark:sprint-plan` in a fresh session, same V-POSITIVE scratch repo (same built graph, `stale:false`), MCP registration temporarily absent.
- **Venue:** `/tmp/ggv/positive` — `.mcp.json` moved aside to `.mcp.json.bak` before the window, restored immediately after; fixture's `plan.md` reset (removed) beforehand so resolution is genuinely re-entered, same practice as Entry 5.
- **Timestamp:** window opened 2026-08-26 20:47:36 (+0200), session ran ~20:48–20:53, `.mcp.json` restored immediately after the run (verified present with original content post-restore).
- **Authorization:** standing sweep grant (Entry 2) covers scratch-venue mutations; this is a project-local MCP-config toggle inside a disposable venue, not the machine-global symlink class of mutation — no cross-session risk, restored regardless.
- **Mutation log:** `mv .mcp.json .mcp.json.bak` → confirmed absent (`ls .mcp.json` → not found) → single T6 run → `mv .mcp.json.bak .mcp.json` → confirmed restored (content byte-identical to Entry 4's registration).

**What the session did (135 stream-json lines), resolution step:**

1. Gate check (`Bash` × 3: list `.spark/`, grep spec status) → "Gate passes — `positive-fixture` spec is `approved`."
2. **`ToolSearch: "staleness impact"`** → `No matching deferred tools found`
3. Text: *"No MCP graph tools exposed. Checking the read-only fallback probe."*
4. **`Bash` — the CLI probe form, verbatim:** `command -v aspark-graph >/dev/null 2>&1 && echo runner=yes || echo runner=no; test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no` → `runner=yes` / `graph=yes`, exit 0
5. Text: *"Both facts hold (runner present, graph exists), so I'll pass the aspark-graph tool file to the Engineering Manager and mention its one-sentence hint."*
6. Delegates to `aspark:engineering-manager`; the subagent's later blast-radius query also runs as a **CLI** call — `Bash: aspark-graph query impact banner.py banner.txt test_banner.py README.md greet.py --repo .` — not an MCP tool, consistent with no MCP server registered this session.

**AC mapping:** AC-2.3 ✓ — no-MCP session on the same scratch repo takes the CLI branch, citing the exact two-part probe form and its `runner=yes, graph=yes` result; the follow-on blast-radius query also stays CLI throughout, never reaching for an MCP tool. Read together with Entry 4/5, both branches are now demonstrated on the same underlying repo state: MCP branch when tools are exposed (Entry 4), CLI branch when they are not (this entry) — the documented order (AC-2.1: MCP first) is a real behavioral fork, not just prose, though Entry 5/F2 shows the fork's *edge* (tools exposed but not fully used) is not perfectly reliable.

**DoD check (T6):** fresh session without the MCP server, same scratch repo ✓; CLI branch resolved, probe form cited (`runner=yes, graph=yes`) ✓; both branches together demonstrate the documented order (Entry 4 = MCP, this entry = CLI) ✓. **Done.**

---

## Entry 7 — stop path with graph available: `/demo-day` halts at the gear check (T7)

- **Run:** `/aspark:demo-day http://localhost:59999 positive-fixture` in a fresh session, V-POSITIVE, MCP registration present (`.aspark-graph` graph built, `stale:false` as of Entry 3).
- **Venue:** `/tmp/ggv/positive`, `.mcp.json` restored to Entry 4's registration (verified byte-identical via `Read` before the run — see tool_result at line 24 of the transcript).
- **Fixture precondition:** `.spark/positive-fixture/review.md` hand-written for this task only — `Status: passed`, minimal body, explicitly labelled as a fixture in its own text (not a real review) — this venue's `plan.md` is still `draft`, T1–T3 `todo`, so a genuine review-passed state was never reachable here without building the fixture code first; the sweep needs a gate-passing artifact, not a genuine feature completion (parallel to Entry 2's minimal pre-written spec).
- **Config/filesystem read confirming `surface=yes, graph=yes` beforehand** (not a live probe of the session's actual tool exposure — this session's only `ToolSearch` call was `"browser playwright chrome devtools"`, never checking for `aspark-graph`'s tools; `/peer-review` finding F5 on this record): `.mcp.json` content read (contains `aspark-graph`/`serve`); `.aspark-graph/graph.json` present (`ls -la` in-session, Entry 3's build untouched). The underlying facts hold on independent grounds regardless — P1/P2's restored global symlink makes the CLI runner reachable (`surface=yes` via that path even without an MCP check), and Entry 3's build is what makes `graph=yes` — so AC-3.2's substance is unaffected by the mislabel.
- **Timestamp:** 2026-08-26 20:59–21:00 (+0200).
- **Authorization:** review.md fixture write covered by the standing sweep grant (scratch-venue artifact, NFR-6); no environment mutation beyond that (no symlink/registration change this entry).

**What the session did (29 stream-json lines), in order:**

1. `Read` `review.md` → `Status: passed` (gate 1 passes)
2. `Read` `plan.md` → `Status: draft`, tasks `todo` (read for context, not a gate)
3. `Bash`: `ls -la && curl -s -o /dev/null -w "%{http_code}\n" http://localhost:59999 --max-time 3 || echo "curl failed"` → `000` / `curl failed` — app confirmed unreachable
4. `ToolSearch: "browser playwright chrome devtools"` → `[{'tool_name': 'WebFetch'}]` — no browser-automation tool found, only the generic `WebFetch`
5. `Read` `.mcp.json` → only `aspark-graph` registered, no Playwright/Chrome DevTools/Claude-in-Chrome
6. **Stop.** No `Agent` tool call anywhere in the transcript (0 `qa-tester` delegation).

**Stop message (verbatim, in full):**

> "Two of the gates in step 1 both fail, so I'm stopping before delegating to QA:
> 1. **No browser tooling available.** The only MCP server configured here is `aspark-graph` (a graph query tool). There's no Playwright MCP, Chrome DevTools MCP, or Claude-in-Chrome integration in this session.
> 2. **The app doesn't respond at `http://localhost:59999`** — nothing is listening there (connection refused).
>
> [...] Per the demo-day rules, I won't substitute code reading for testing, and I won't fabricate a browser QA pass here. To proceed you'd need to either: Point me at an actual running web app + browser tooling this ceremony is meant for, or Recognize this fixture as CLI-only [...] Given the plan is still `draft` with all tasks `todo`, the actual next step in the loop is `/increment` to build T1–T3, not `/demo-day`."

**Counts (method per Counting domains above):** probe executions naming `aspark-graph`'s CLI or MCP resolution form: **0** (no `command -v aspark-graph` / `test -f .aspark-graph/graph.json`, no `mcp__aspark-graph__*` call — the transcript's only `aspark-graph` mentions are the `.mcp.json` file's own content and the stop message's plain-English naming of it as "the only MCP server configured", not a resolution attempt). Hint sentences (the tool file's one-sentence availability hints): **0**. Tool-file handovers (`tools/aspark-graph.md` passed to an agent): **0** — consistent with "a run that stopped on the browser or app gate never reaches this sub-step," which is exactly what happened.

**AC mapping:** AC-3.1 ✓ (stops at the gear check, names exactly what to set up: browser tooling + a running app) · AC-3.2 ✓ (the graph sub-step is never reached despite `surface=yes, graph=yes` being independently confirmed — the tool availability never softens or bypasses the browser/app prerequisite).

**DoD check (T7):** `surface=yes, graph=yes` confirmed beforehand via the config/filesystem read plus P1/P2 and Entry 3's build (per F5's correction above) ✓; `/demo-day` runs step-1 gates on a review-passed fixture with no browser backend and an unreachable URL ✓; stop message names exactly what to set up ✓; 0 `qa-tester` delegation ✓; 0 probe executions, 0 hint sentences, 0 tool-file handovers, all counted ✓. **Done.**

---

## Entry 8 — Playwright MCP: detection plus one real interaction (T8)

- **Run:** `/aspark:demo-day http://localhost:8899/index.html browser-fixture` in a fresh session, new venue V-BROWSER.
- **Venue setup (new):** `/tmp/ggv/browser` — a throwaway static page (`index.html`, `<h1>GGV Browser Fixture</h1>` + `<p id="marker">ggv-t8-marker-2f9a17</p>`) served by `python3 -m http.server 8899` from that directory (background process, disposable, outside this repo — Q1); fixture `.spark/browser-fixture/spec.md` (`approved`, one AC: marker text present) and `review.md` (`passed`, hand-written for this task, same rationale as Entry 7's fixture) written so `/demo-day`'s gate check passes.
- **Timestamp:** page serving started 2026-08-26 21:01 (+0200, verified `curl` → `200` and body matches); Playwright registration ~21:02; session ran 2026-08-26 21:04–21:07 (from `t8-session.jsonl`).
- **Authorization:** C15 grant — Playwright MCP registration authorized, project-scoped, this venue only.
- **Mutation log:** `claude mcp add --scope project playwright -- npx -y @playwright/mcp@latest` from `/tmp/ggv/browser`, writing `.mcp.json` (`{"mcpServers":{"playwright":{"type":"stdio","command":"npx","args":["-y","@playwright/mcp@latest"],"env":{}}}}`) — durable venue state for T9's separate-session reuse, not restored mid-sweep (disposable scratch venue outside this repo, needing no cleanup on any NFR here, same reasoning as Entry 4's `aspark-graph` registration; see Entry 4's B1 correction — disposable is an authorization, not a claim that deletion already happened).

**What the orchestrator session did (124 stream-json lines), gate check:**

1. `Bash`: `review.md` exists and reads `passed`
2. `Bash`: `curl … http://localhost:8899/index.html` → `200`
3. `ToolSearch: "playwright browser navigate"` and follow-ups → Playwright MCP tools resolve (`mcp__playwright__*`)
4. `Bash`: the `aspark-graph` CLI probe (`command -v aspark-graph …; test -f .aspark-graph/graph.json …`) → `runner=yes` / `graph=no` — this venue has no `aspark-graph` MCP registration (only Playwright is registered here), so the CLI branch is the correct fallback for that *separate* tool; text: *"State: runner=yes, graph=no → this is the 'yes/no' row: I'll say the hint once — graph data not built for this repo — and continue without the tool."* (an incidental but consistent sighting of the exact hint-once behavior US-5/T11 targets, on a different venue/ceremony than T11's dedicated run — noted here, not counted toward T11's DoD)
5. Text: *"Gates check complete: review status is `passed`, the app responds (HTTP 200) at the URL, and Playwright MCP browser tooling is available."* → delegates to `aspark:qa-tester`

**Subagent's interaction (via `mcp__playwright__*` tools directly — this agent's grant differs from Entry 4's Engineering Manager, which had none):**

- **`mcp__playwright__browser_navigate`** `{"url": "http://localhost:8899/index.html"}` → *"Page URL: http://localhost:8899/index.html — Page Title: GGV Browser Fixture"* (navigation #1)
- **`mcp__playwright__browser_snapshot`** → accessibility tree: `heading "GGV Browser Fixture"`, `paragraph: ggv-t8-marker-2f9a17` — on-page-content assertion #1, backend-native form
- `mcp__playwright__browser_console_messages` / `browser_network_requests` — 1 console error found (`favicon.ico` 404, benign, unrelated to the marker)
- **`mcp__playwright__browser_evaluate`** `{"function": "() => {...el.textContent === 'ggv-t8-marker-2f9a17'...}"}` → `{"tag":"P","text":"ggv-t8-marker-2f9a17","exact":true}` — on-page-content assertion #2, DOM-level, exact match confirmed
- `mcp__playwright__browser_resize` (mobile viewport) + a second `browser_navigate` + snapshot — exploratory beyond the minimal slice, not required by the AC but performed
- QA report written to `browser-fixture/qa.md`: `Status: passed`, AC-1.1 ✅

**Literal MCP tool names cited (AC-4.1/AC-4.2):** `mcp__playwright__browser_navigate`, `mcp__playwright__browser_snapshot`, `mcp__playwright__browser_evaluate`, `mcp__playwright__browser_console_messages`, `mcp__playwright__browser_network_requests`, `mcp__playwright__browser_resize`.

**Attempt/verdict semantics (AC-4.4):** one attempt, no failures at any step (availability, detection, interaction) — **Playwright MCP confirmed**, full pass on the first and only attempt.

**AC mapping:** AC-4.1 ✓ (transcript records Playwright MCP as the detected tooling, gate passes on that basis) · AC-4.2 ✓ (≥1 navigation — two performed — and ≥1 on-page-content assertion — snapshot text plus a DOM-level `evaluate`, both exceeding the minimal bar — each attributable to `mcp__playwright__*` action identifiers) · AC-4.4 ✓ (single attempt, full pass, confirmed verdict, nothing to route as a failure).

**DoD check (T8):** Playwright MCP registered project-scoped, C15 terms logged ✓; throwaway static page served on localhost from scratch outside this repo ✓; gear check detects Playwright MCP and passes on that basis ✓; ≥1 navigation and ≥1 on-page-content assertion, both attributed to backend action identifiers ✓; attempt logged with AC-4.4 verdict semantics (confirmed, 1/1) ✓. **Done.**

---

## Entry 9 — Chrome DevTools MCP: same proof, separate session (T9)

- **Run:** `/aspark:demo-day http://localhost:8899/index.html browser-fixture` in a fresh session, separate from Entry 8, same V-BROWSER venue with the static page still serving.
- **Venue swap:** `.mcp.json` moved to `.mcp.json.playwright.bak`; Chrome DevTools MCP registered project-scoped in its place — `claude mcp add --scope project chrome-devtools -- npx -y chrome-devtools-mcp@latest`, writing `.mcp.json` (`{"mcpServers":{"chrome-devtools":{"type":"stdio","command":"npx","args":["-y","chrome-devtools-mcp@latest"],"env":{}}}}`). Playwright's registration is preserved in the `.bak` file, not deleted — no restoration owed mid-sweep for the same reason as Entry 8 (disposable venue, no cross-session risk).
- **Timestamp:** registration 2026-08-26 ~21:09; session ran 2026-08-26 21:10–21:14 (from `t9-session.jsonl`).
- **Authorization:** C15 grant, same terms as Entry 8's Playwright registration.
- **Static page confirmed still serving:** `curl` → `200` immediately before the run (same process from Entry 8, untouched).

**What the orchestrator session did (201 stream-json lines), gate check:**

1. `Bash`/`Read`: locates `.spark/browser-fixture/review.md` → `passed`; `curl` → app responds `200`
2. `ToolSearch: "chrome devtools navigate page"` and `"mcp__chrome-devtools"` → Chrome DevTools MCP tools resolve
3. `ToolSearch: "staleness impact aspark-graph"` → none found; **`Bash`** CLI probe (`command -v aspark-graph …; test -f .aspark-graph/graph.json …`) → `runner=yes` / `graph=no`; text: *"Runner is on `PATH` but `.aspark-graph/graph.json` doesn't exist — that's the 'yes/no' mixed state, so per the table I say the one-sentence hint once and continue without the tool"* — same hint-once behavior as Entry 8, on the same unbuilt V-BROWSER graph state (again incidental to T9, cross-referenced not counted here)
4. Delegates to `aspark:qa-tester`, which reads the existing `qa.md` from Entry 8 and re-tests as round 2

**Subagent's interaction (via `mcp__chrome-devtools__*` tools directly):**

- **`mcp__chrome-devtools__list_pages`** → `1: about:blank [selected]`
- **`mcp__chrome-devtools__navigate_page`** `{"url": "http://localhost:8899/index.html"}` (called twice, `pageId 0` then `1`) → *"Successfully navigated … GGV Browser Fixture (http://localhost:8899/index.html) [selected]"* — navigation #1
- **`mcp__chrome-devtools__take_snapshot`** → `StaticText "ggv-t8-marker-2f9a17"` in the accessibility tree — on-page-content assertion #1
- **`mcp__chrome-devtools__evaluate_script`** (marker check) → `{"found":true,"tag":"P","text":"ggv-t8-marker-2f9a17","exactMatch":true,"title":"GGV Browser Fixture"}` — on-page-content assertion #2, exact match confirmed
- Further exploratory calls beyond the minimal bar: `list_console_messages`, `list_network_requests`, `resize_page` and `emulate` across two viewports, `take_screenshot` ×2, a full `navigate_page` reload, and a second marker `evaluate_script` post-reload
- QA report round 2 written to the same `browser-fixture/qa.md`: AC-1.1 ✅ pass, marker text exact

**Literal MCP tool names cited (AC-4.3):** `mcp__chrome-devtools__list_pages`, `mcp__chrome-devtools__navigate_page`, `mcp__chrome-devtools__take_snapshot`, `mcp__chrome-devtools__evaluate_script`, `mcp__chrome-devtools__list_console_messages`, `mcp__chrome-devtools__list_network_requests`, `mcp__chrome-devtools__resize_page`, `mcp__chrome-devtools__emulate`, `mcp__chrome-devtools__take_screenshot`.

**Attempt/verdict semantics (AC-4.4):** one attempt, no failures at any step — **Chrome DevTools MCP confirmed**, full pass on the first and only attempt, same as Playwright in Entry 8.

**AC mapping:** AC-4.3 ✓ — the same two observations (AC-4.1-style detection, AC-4.2-style navigation + content assertion) are repeated for Chrome DevTools MCP in a separate session, under the same C15 grant and the same logging discipline. AC-4.4 ✓ (confirmed, 1/1, recorded alongside Entry 8's Playwright confirmed/1/1 — both backends now have a completed verdict).

**DoD check (T9):** same two observations repeated for Chrome DevTools MCP in a separate session ✓; same grant (C15) and logging pattern ✓; attempts and verdict recorded under AC-4.4 semantics ✓. **Done.**

---

## Entry 10 — control: gear gate passes with a confirmed backend present (T10, sanctioned out-of-order exception after T8/T9)

- **No new run.** Per the plan's binding ruling, T10/AC-3.3 executes here, out of ID order, because it depends on a backend already confirmed under T8 or T9.
- **Citation:** Entry 8 and Entry 9 are each, independently, exactly this control. In both, `/demo-day`'s step-1 gate check found review `passed`, the app reachable (`curl` → `200`), and a browser backend detected (Playwright in Entry 8, Chrome DevTools MCP in Entry 9) — and in both, the ceremony **proceeded past step 1**: it resolved the optional `aspark-graph` sub-step (hint-once, `runner=yes graph=no`), then delegated to `aspark:qa-tester`, which drove real navigation and assertions and produced a `passed` QA report. Neither run stopped; both ran to completion.
- **Contrast with T7 (Entry 7):** same gear-check structure, opposite outcome — no backend, unreachable app → stop, zero delegation. T7 and T10 together are the negative/positive pair for US-3's stop-vs-proceed behavior, mirroring T2's silence-case-first pattern for US-1/US-2.

**AC mapping:** AC-3.3 ✓ — with a backend confirmed present (T8: Playwright; T9: Chrome DevTools MCP), the gear gate passes and the ceremony proceeds past step 1, cited back from Entries 8 and 9 rather than re-run.

**DoD check (T10):** `/demo-day` with a backend confirmed under T8/T9 passes the gear gate and proceeds past step 1 ✓ (shown twice, once per backend); entry cited back into US-3's evidence as the sanctioned out-of-order exception ✓. **Done.**

---

## Entry 11 — hint-exactly-once: full ceremony run in `runner=yes, graph=no` (T11)

- **Run:** `/aspark:sprint-plan` in a fresh session, new venue V-HINT — a dedicated fixture built for this task alone, since neither existing venue matches the required state: V-POSITIVE has a built graph (`graph=yes`, Entry 3), V-BROWSER's `runner=yes, graph=no` state (seen incidentally in Entries 8/9) belongs to a venue already committed to the browser-backend narrative and has no plan-gate-passing spec of its own for a full Plan-phase run.
- **Venue (new):** `/tmp/ggv/hint` — a git repo, seed commit `fixture: hint venue seed`, containing `util.py` (`double(n)`) and a fixture spec `.spark/hint-fixture/spec.md` (`approved`, minimal single-story deliverable). No `.aspark-graph/` directory, no `.mcp.json` — verified before the run: `command -v aspark-graph` → the global symlink resolves (`runner=yes`); `.aspark-graph/graph.json` absent (`graph=no`).
- **Timestamp:** venue built 2026-08-26 21:15; session ran 2026-08-26 ~21:16–21:18.
- **Authorization:** no mutation beyond ordinary scratch-venue construction (NFR-6) — no symlink change, no MCP registration, no build.

**What the session did (69 stream-json lines), full run:**

1. Gate check (`Bash` × 2) → "Gate passed — spec status is `approved` for feature `hint-fixture`."
2. `ToolSearch: select:Bash` (checking for the Bash tool itself — no `aspark-graph`-named MCP tools found/searched for by name here) → no MCP graph tools surface
3. **`Bash` — the CLI probe form:** `command -v aspark-graph >/dev/null 2>&1 && echo runner=yes || echo runner=no; test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no` → `runner=yes` / `graph=no`
4. `Read` the tool file (`tools/aspark-graph.md`)
5. **The hint sentence (verbatim, ceremony-emitted, surface 2):** *"State: runner=yes, graph=no. The aspark-graph tool isn't built for this repo yet — `aspark-graph build .` would build it, if you want blast-radius grounding later. Continuing without it."*
6. Delegates to `aspark:engineering-manager`, which reads spec/template/source, writes `.spark/hint-fixture/plan.md` (`draft`, PLAN GATE checked, blast radius section states plainly: *"Blast-radius tooling: not available. The `aspark-graph` runner is on PATH but `.aspark-graph/graph.json` does not exist for this repo, so no query was [performed]"* — no `build` mention)
7. Final summary presented to the user for the architecture veto — reviewed in full, no second hint

**Counting method (per this task's DoD and the file's Counting domains section):** literal substring `aspark-graph build`, counted separately on the two declared surfaces, loaded file contents excluded (the tool file's own `Read` result and the fixture `README.md`'s own description both contain the string and are excluded on that basis).

| Surface | Count |
|---|---|
| 1 — artifact produced (`hint-fixture/plan.md`, full text) | **0** |
| 2 — ceremony's user-visible output (all assistant text blocks incl. final result) | **1** (Entry 11 step 5 above) |

**Total: exactly 1**, matching AC-5.1's required count and the tool file's own rule (`tools/aspark-graph.md:27-28`): "at most one hint sentence fires per run, at most once."

**Mutation-absence checks:** `Bash` tool_use commands across the full transcript containing `build`, `install`, or `serve`: **0** (grep over every `Bash` command issued by any participant, orchestrator or subagent). `.aspark-graph/graph.json` in V-HINT post-run: **absent** (`ls` confirms) — no graph was created.

**AC mapping:** AC-5.1 ✓ (exactly 1 occurrence counted across the ceremony's complete emitted output) · AC-5.2 ✓ (0 build/install/serve executed by any participant, no `graph.json` came into existence) · AC-5.3 ✓ (counting domain and method stated per Counting domains, loaded-file exclusion named, both surfaces reported) · NFR-5 ✓ (the claim is a counted number with its method named, consistent with AC-5.3).

**DoD check (T11):** scratch Core-managed trail whose plan gate passes ✓; `runner=yes, graph=no` verified beforehand ✓; one wired ceremony runs start to finish ✓; counting method stated ✓; exactly 1 hint sentence counted ✓; 0 `build`/`install`/`serve` executions ✓; no `graph.json` created ✓. **Done.**

---

## Entry 12 — stale graph: announced once, then treated as absent (T12)

- **Run:** `/aspark:peer-review positive-fixture` in a fresh session, V-POSITIVE (T3's venue), MCP registration present, graph forced stale.
- **Venue prep:** the fixture's own plan (T1–T3 from Entries 4–6's `/sprint-plan` runs) implemented directly — `banner.py` (renderer + `write()` + `__main__` guard), `banner.txt` (generated, `Hello, positive venue!\n`), `test_banner.py` (2 stdlib `unittest` tests, both green), `README.md` regeneration note — so plan.md's task table shows all three tasks `done`, satisfying `/peer-review`'s own gate. Fixture's `review.md` from Entry 7/8's earlier reuse deleted first, so this round starts genuinely from zero. **Indexed-file edit:** `calc.py` (untouched by the plan) got an added `mul()` function — a deliberate, plan-undeclared change whose purpose is purely to invalidate the graph.
- **Performed staleness query (before the run, confirming the precondition):** `aspark-graph query staleness --repo /tmp/ggv/positive` → `{"stale": true, "changed": ["calc.py"], "files_checked": 2, "advice": "Run 'aspark-graph build' to refresh the graph."}`.
- **Timestamp:** venue prep + edit 2026-08-26 ~21:20–21:27; session ran 2026-08-26 21:28–21:34 (from `t12-session.jsonl`).
- **Authorization:** implementing the plan's own tasks is ordinary scratch-venue work (NFR-6, no new mutation category); the `calc.py` edit is likewise a scratch-venue source edit, not a machine or MCP-registration mutation.

**Orchestrator's tool-availability resolution (further F2 evidence):** no `ToolSearch` call at all this session — the MCP tool surface was never probed for — and only the `graph.json`-existence half of the CLI form ran (`test -f .aspark-graph/graph.json` → `graph=yes`; `command -v aspark-graph` never run). On that partial basis alone: *"aspark-graph resolves to 'surface yes / graph.json yes' — I'll pass its tool doc to the reviewer."* Folded into Finding F2 above as a third, distinct incompleteness (previously: 1 extra probe despite MCP present; 1 missed MCP call despite MCP present; now: no MCP check attempted at all, and only half the CLI probe run).

**What the `reviewer` subagent did, staleness handling (from the finalized `review.md`):**

- Ran its own read-only query directly: `aspark-graph query staleness --repo .` → `stale:true`, `changed:["calc.py"]`, `files_checked:2` — exit 0
- **The one staleness statement (verbatim, from `review.md` §1):** *"`query staleness --repo .` returned `stale: true`, `files_checked: 2`, `changed: ["calc.py"]`. Per the tool doc's stale rule the graph was then treated as **absent** for the rest of the run: `impact` and `story_trace US-1` were deliberately **not** called, and no finding below rests on graph output."*
- **Zero graph citations as evidence thereafter:** `impact`/`story_trace` confirmed never called (no such tool_use in the transcript past this point); the fixture review's own Finding FX1 (below — a separate ID space from this evidence file's F1/F2, per `/peer-review` finding F7) — the one finding the staleness result could plausibly have informed — explicitly disclaims it: *"The staleness result happens to corroborate F1, but F1 rests on `git diff calc.py` and on reading `calc.py:12-13`, not on the tool."* (quoted verbatim from the fixture's `review.md`, which still uses its own local `F1` label internally)
- Scoping done by hand instead: *"the repo is six files and all six were read in full, which is tractable here"* — followed by three separate scratch-copy probes (delete-and-regenerate, drift, hand-edit-vs-generator) actually performed, not asserted

**Verdict reached, resting on concrete `file:line` anchors (normal review outcome, `changes-requested`).** IDs below are prefixed `FX` — a separate ID space from this evidence file's own F1/F2, per `/peer-review` finding F7 (the fixture's own `review.md` still labels them `F1`–`F5` internally; only this summary table renames them, to avoid colliding with the real findings table above):

| # | Severity | Location | Finding (summary) |
|---|---|---|---|
| FX1 | Major | `calc.py:12-13` | Undeclared `mul()` addition — plan says `calc.py` untouched, spec puts it out of scope; this is what made the graph stale |
| FX2 | Minor | `banner.py:9` | Newline placed inside `render()`, contradicting plan §1/T2's DoD wording |
| FX3 | Minor | `test_banner.py:15` | Artifact test asserts against `render()`, not AC-1.1's literal string as the plan's own risk table required |
| FX4 | Minor | `README.md:7-8` | Documents a `python` binary absent from this machine (`python3` only) |
| FX5 | Nit | `banner.py:13`, `test_banner.py:14` | No explicit `encoding=` on file I/O |

Gate: REVIEW GATE left open (`No open Major findings` unchecked — FX1 open, unwaived); `Status: changes-requested`. A genuine, reasoned, non-`passed` verdict — not a rubber stamp, and not blocked or distorted by the stale/absent graph.

**AC mapping:** AC-6.1 ✓ (staleness announced exactly once, in the run's own emitted artifact) · AC-6.2 ✓ (0 graph citations as evidence after the announcement; the one finding staleness could have informed instead cites `git diff` and a `file:line` read, and says so explicitly; the review reaches a normal, fully-reasoned verdict).

**DoD check (T12):** indexed source file edited, staleness query performed and returns `stale:true` ✓; `/peer-review` runs with the tool file handed over ✓; entry counts 1 staleness statement and 0 graph citations as evidence thereafter ✓; verdict rests on ≥1 concrete `file:line` anchor (five, in fact) with the normal verdict reached ✓. **Done.**

---

## Entry 13 — consolidated findings and backend verdicts (T13)

### Findings, consolidated (NFR-3: verbatim quote + `file:line`, route named)

| ID | Contradicting documented text (verbatim, `file:line`) | Measurement / reproduction | Route |
|---|---|---|---|
| **F1** | `.spark/graph-gates-verification/spec.md:76` (A3): *"`~/aSPARK` resolves `runner=yes, graph=no`"* | Entry 1, P3: `~/aSPARK/.aspark-graph/graph.json` exists (56,668 bytes, mtime 29 Jul 18:05) → `graph=yes`. Reproducible: `test -f ~/aSPARK/.aspark-graph/graph.json`. | Operator-environment drift (Risk R6) — no consumer-repo or Core action implied; venue assignment already corrected for it (Entry 1) |
| **F2** | `tools/aspark-graph.md:19-20`: *"**MCP first.** If the session exposes tools whose names end in `staleness` and `impact` … use them. **Run no command.**"* — contradicted by `skills/sprint-plan/SKILL.md:38`, `skills/peer-review/SKILL.md:38`, `skills/demo-day/SKILL.md:40`: *"Resolve **both** facts — is there a surface, and does `.aspark-graph/graph.json` exist"* — the only documented method for the second fact is the command at `tools/aspark-graph.md:22`. Separately, the *detection* act itself is unspecified in any shipped file — `ToolSearch` (the mechanism Entry 4 actually used to check for the MCP tools) appears nowhere under `skills/ agents/ tools/ lenses/`. | Three separate sessions, same registered MCP surface, three different incomplete resolutions: Entry 4 (0 probes, correct) vs. Entry 5 (1 stray `Bash` probe despite MCP confirmed via `ToolSearch`) vs. Entry 12 (`ToolSearch` skipped entirely; only the `graph.json`-existence half of the CLI probe run; "surface yes" declared without ever checking for MCP tools or `command -v aspark-graph`). Five different detection/resolution mechanics observed across the sweep's seven nested-session transcripts (t4, t5b, t6, t7, t8/t9, t11, t12) — the signature of an underspecified instruction, not of model flakiness alone. | **Re-routed on `/peer-review` (Round 1, F3): a Core documentation defect, not primarily model variance.** `tools/aspark-graph.md:19-22` should state the detection mechanism explicitly (e.g. name `ToolSearch` or an equivalent) and reconcile "run no command" with the three SKILL.md's "resolve both facts" — either by scoping "both facts" to the CLI branch only, or by giving the MCP branch its own documented way to confirm `.aspark-graph/graph.json` presence without a shell command. A residual reliability question remains even after that fix (whether the corrected instruction is then followed consistently) — that part stays a Core reliability observation, but is no longer the primary route. |

No other documented-text contradiction surfaced anywhere in T1–T12. Every other observed deviation from an initial expectation (e.g., Entry 5's discarded confounded attempt, the auto-mode classifier's repeated denials of the nested-session command) was an artifact of the sweep's own method, not a contradiction of Core's shipped material, and is recorded in its entry without a findings-table row.

### Backend verdicts (AC-4.4 semantics: confirmed only on a full-pass attempt, refuted only if none pass, instability recorded)

| Backend | Attempts | Outcome | Verdict |
|---|---|---|---|
| **Playwright MCP** (#10) | 1 (Entry 8) | Full pass: detected, gate passed on that basis, ≥1 navigation, ≥1 on-page-content assertion (snapshot text + `browser_evaluate` exact match), 0 failures at any step | **Confirmed** |
| **Chrome DevTools MCP** (#10) | 1 (Entry 9) | Full pass: detected, gate passed on that basis, ≥1 navigation, ≥1 on-page-content assertion (`take_snapshot` + `evaluate_script` exact match), 0 failures at any step | **Confirmed** |
| **`aspark-graph` MCP registration/serve** (#8) | 1 successful registration + 3 sessions of use (Entries 4, 5, 12) | Registration and `serve` never failed; the tools appeared and answered correctly (`staleness`, `impact`) every time they were actually called. The AC-2.4 failure-path (registration fails or tools never appear) was never triggered — nothing to route there. | **Confirmed available**; AC-2.4's finding path remains untested (no failure occurred to exercise it) |

**Issue-mapping status** (per spec A4, for the user's `/go-live` act — not this diff's to close):

- **#8** (MCP-first precedence, prior AC-2.2, this spec's AC-2.1/AC-2.2) — **mixed.** The MCP branch is real and demonstrably taken when tools are exposed (Entries 4, 8, 9), and its CLI-branch control is Entry 6 (this spec's AC-2.3). But Entry 5/F2 shows the *zero-probe* half of the guarantee is not reliably reproduced session-to-session. Not a clean confirm.
- **#9** (`/demo-day` no-browser stop, prior AC-3.5, this spec's AC-3.1/AC-3.2) — **confirmed** (Entry 7): stop message names exactly what to set up, 0 `qa-tester` delegation, tool sub-step never reached.
- **#10** (browser backends, gear-check prose) — **confirmed for both backends** (Entries 8, 9, 10).
- **#11** (hint, prior AC-2.3; stale-graph reaction, prior AC-3.2 — this spec's US-5/US-6) — **confirmed**: Entry 11 (hint count = exactly 1, 0 build/install/serve, no `graph.json` created), Entry 12 (staleness announced once, 0 graph citations as evidence thereafter, verdict on five `file:line` anchors).

**DoD check (T13):** every defect has a findings row with verbatim quote, `file:line`, and route ✓ (F1, F2); each of the two US-4 backends carries a final confirmed/refuted/unstable verdict derived from logged attempts ✓ (both confirmed, 1/1); the `aspark-graph` registration itself is likewise given a verdict for completeness, beyond the letter of "each backend" ✓. **Done.**

---

## Entry 14 — fence and fidelity audit (T14)

- **Run:** neutral-shell probes and `git` queries in `~/aSPARK` (this repo), read-only.
- **Timestamp:** 2026-08-26, immediately following Entry 13.

**Fence check — `git diff --name-only` and untracked files:**

```
$ git status --porcelain
?? .spark/graph-gates-verification/
$ git diff --name-only
(empty)
```

Only `.spark/graph-gates-verification/**` is untracked; no tracked file shows a modification. `README.md` (this feature's one sanctioned non-`.spark/` edit, reserved for T15) is untouched so far.

**Byte-identical audit over shipped material:**

```
$ git diff --stat -- skills/ agents/ tools/ lenses/ templates/ .claude-plugin/plugin.json
(empty)
$ git status --porcelain --untracked-files=all -- skills/ agents/ tools/ lenses/ templates/ .claude-plugin/plugin.json
(empty)
```

Both empty — zero modifications, zero new/untracked files under any of the six paths NFR-2 protects.

**Counts:** `ls -d skills/*/ | wc -l` → **10**; `ls agents/*.md | wc -l` → **7** — unchanged from the constitution's stated ship count.

**Final neutral-shell probe (P1′–P7′, re-run of Entry 1's P1–P7):**

| Probe | Entry 1 baseline | This run | Match |
|---|---|---|---|
| P1 symlink target/resolution | → `aSPARK-graph/.venv/bin/aspark-graph`, exit 0 | identical target, exit 0 | ✓ (mtime differs — Entry 2's remove→restore artifact, already noted there; link target and length unchanged) |
| P2 `command -v` | resolves, exit 0 | resolves, exit 0 | ✓ |
| P3 `~/aSPARK` graph state | `graph=yes`, 56,668-byte `graph.json` | `graph=yes`, same byte count, same mtime (29 Jul 18:05) | ✓ unchanged (never written to — C7) |
| P4 `~/aSPARK/.mcp.json` | absent, exit 1 | absent, exit 1 | ✓ |
| P5 `~/aSPARK-graph` graph state | `graph=yes` | `graph=yes` | ✓ |
| P6 `~/aSPARK-graph` staleness | `stale:false`, `files_checked:107` | `stale:false`, `files_checked:107` | ✓ byte-identical query result |
| P7 `~/aSPARK` git state | `?? .spark/graph-gates-verification/` | `?? .spark/graph-gates-verification/` | ✓ (same line — the feature's own directory, expected) |

**Counting-method restatement (NFR-5):** every zero/exactly-once claim in Entries 1–13 states its counting domain inline at the point of the claim (T2's two-surface method restated from the Counting domains section; T4/T5/T6's probe-command counts scoped to `Bash` tool_use commands in the transcript; T11's hint count scoped to the two declared surfaces with loaded-file exclusion named; T12's staleness-statement count scoped to the produced `review.md`). Nothing here restates them again — this entry only confirms the *fence*, not the counts already made elsewhere.

**Readability check:** Entries 1–13 read in ascending order; Entry 2 (silence case, US-1) precedes every positive-case entry, satisfying AC-1.3's ordering requirement as re-confirmed here.

**AC mapping:** AC-1.2 ✓ (every mutation across Entries 1–13 was logged with authorization and restoration or reasoned non-restoration; this entry adds the closing environment probe) · AC-1.3 ✓ (silence-first ordering holds on re-read) · NFR-1 ✓ (`README.md` remains the only non-`.spark/` file this feature will touch) · NFR-2 ✓ (six protected paths byte-identical) · NFR-4 ✓ (every claim in this entry is a performed step with captured output, not an assertion) · NFR-5 ✓ (counting methods were stated at each claim's point of origin, restated in summary here) · NFR-6 ✓ (no mutation performed by this entry itself — pure audit).

**DoD check (T14):** `git diff --name-only` limited to `.spark/graph-gates-verification/**` (README.md reserved for T15) ✓; empty diffs over the six protected paths ✓; counts still 10 skills / 7 agents ✓; final neutral-shell probe identical to Entry 1 (mtime caveat noted, already explained in Entry 2) ✓; entries readable in order, silence case first ✓; counting method stated for every zero/exactly-once claim (at origin, restated here) ✓. **Done.**

---

## Entry 15 — README proof statement rewritten from the evidence (T15)

- **Edit:** `README.md` §Project Status — the `Optional tools` row and a new paragraph naming the post-sweep state for #8–#11, worded per NFR-9 (proven stays proven, refuted becomes refuted-with-finding; the row and paragraph both now also label the two never-attempted partials — AC-1.2, AC-5.2 — `unproven` and out of scope, corrected on `/peer-review` Round 1 finding F2).
- **Content, mapped to Entries 6–13:** #9 → proven (Entry 7); #11 → proven, both the hint (Entry 11) and the stale-graph reaction (Entry 12); #10 → proven for Playwright MCP and Chrome DevTools MCP (Entries 8–9), Claude in Chrome's proof status left as it was (untouched by this sweep); #8 → refuted-with-finding, citing the zero-probe-command guarantee's non-reproduction (F2/F3) rather than closing it; AC-1.2 and AC-5.2 → labelled `unproven`, never attempted by this sweep (spec §6 cut).
- **Explicitly not done:** `docs/status.md`'s six-row `partial` table was not edited — the plan (§2 Affected Components) scopes this feature's only non-`.spark/` edit to `README.md` §Project Status; the README paragraph says so plainly rather than silently leaving a stale cross-reference.
- **Fence re-check after the edit:** `git status --porcelain` → ` M README.md` plus `?? .spark/graph-gates-verification/` — nothing else touched, matching Entry 14's audit plus this one sanctioned edit.

**AC mapping:** NFR-9 ✓ — the statement is literal against the evidence record, names its own scope boundary (docs/status.md follow-up), and remains the feature's only non-`.spark/` edit.

**DoD check (T15):** `README.md` §Project Status restated to the post-sweep proof state ✓; proven stays proven, refuted becomes refuted-with-finding ✓; worded consistently with the evidence record ✓; remains the only non-`.spark/` edit in the whole feature diff ✓. **Done.**



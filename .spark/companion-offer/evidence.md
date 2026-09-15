# Evidence: companion-offer (Specify-phase verification)

| | |
|---|---|
| Feature | companion-offer |
| Phase | Specify |
| Date | 2026-09-14 |

**Provenance.** The `gh` commands below were run by the **invoking coordinator session**, not by this agent (Product Owner, `/story-time`) — that role has Read/Write/Grep/Glob only, no Bash/`gh` access. Recorded here as relayed, dated evidence, in the same spirit as the constitution's own practice of citing a verified registry check inline (§3, the PyPI HTTP 200 check). A future phase with Bash access should independently re-run at least the repo-visibility and plugin-manifest checks before the README entry ships, and must perform AC-1.6 itself regardless of this record.

## AC-1.2 — install command / repo existence

- `gh repo view a-lottes/aSPARK-guard` (reported) → `visibility: PUBLIC`.
- Inspection of that repo's `.claude-plugin/plugin.json` (reported) → `name: aspark-guard`, `version: 0.1.0`.
- `gh release list --repo a-lottes/aSPARK-guard` (reported) → empty; no GitHub Releases exist.
- Last push to the repo (reported): 2026-09-11.
- **Conclusion.** `/plugin install aspark-guard@aspark` is the correct command: it matches `marketplace.json`'s declared plugin name (`aspark-guard`) under marketplace `aspark`, the same `<plugin>@<marketplace>` pattern already used for `aspark@aspark`. Source is `{"source":"github","repo":"a-lottes/aSPARK-guard"}` — the repo directly, not a Release — so the absent Releases list does not block installability.
- **Not yet done.** Actually running `/plugin install aspark-guard@aspark` and observing the result. That is AC-1.6, deferred to this feature's own `/demo-day` dogfood.

## AC-1.3 — maturity evidence

- Source (reported, via `gh api`, 2026-09-14): the guard's own README.
- Claims found there: all six milestones (M0–M5) marked **Built**; **142 tests** replayed over **22 real gated artifacts**, no false positive; a marketplace-install verification the guard's own author dated **2026-09-11**, cited to the guard's own `docs/evidence.md` §4.
- The guard's own stated gap (as reported): *"none of this has run a full feature loop on a project that isn't this author's"* — the same gap `ROADMAP.md` names about aSPARK Core itself.
- **Cross-check against this machine.** `~/.claude/plugins/installed_plugins.json` lists only `aspark@aspark` — the guard is **not installed here**, despite its own claim of a working install verification on 2026-09-11 (presumably on a different machine or since removed).
- **Conclusion.** The evidence is real, substantial and self-reported by the guard's own author — not independently verified by aSPARK Core, and not currently present on this machine. Recorded in spec §3 (A3) as a qualified maturity statement rather than a bare `proven`/`unproven` word (AC-1.3).

## Canonical wording (T1 — Plan phase)

Pinned once here, quoted verbatim by every prose surface T2/T3/T5 touch. No task
re-derives a claim from the guard's own README; each quotes this block or its
declared short form.

**Long form** (used once, in `README.md` §Optional Tools — T2):

> `aspark-guard` reports substantial self-tested evidence — 142 tests replayed
> over 22 real gated artifacts with no false positive, and an author-verified
> marketplace install dated 2026-09-11 (its own `docs/evidence.md` §4) — but that
> evidence is self-reported by the guard's own author, has not been independently
> verified by aSPARK Core, and has never been exercised through a full
> third-party feature loop, the same gap this project's own `ROADMAP.md` names
> about itself. This entry makes no claim about gate enforcement that aSPARK
> Core has observed directly.

**Declared short form** (used in table cells — `README.md` §Project Status T3,
`ROADMAP.md` T5):

> self-tested by its own author (142 tests / 22 replayed artifacts), not
> independently verified by Core, never run through a third-party loop

**Literal install string** (used in T2, T8):

> `/plugin install aspark-guard@aspark`

**What the entry must never say:** that `aspark-guard` enforces gates in this
repo's own loop — Core has not observed that; only the guard's own self-tested
claim exists. Never "proven" or "unproven" alone — both flatten the qualification
this wording exists to preserve.

## Baseline (pre-change) — T1, 2026-09-14

- `grep -rl 'aspark-guard' --include='*.md' /Users/andreaslottes/aSPARK --exclude-dir=.spark` → **no output, exit 1** (no match). Confirms: zero tracked `.md` files mention the guard before this feature, matching the spec's problem statement and AC-1.1's starting condition.
- `git diff --name-only main...HEAD` (on branch `docs/companion-offer`, cut from `origin/main` at `d1337a3`) → **empty**. Confirms the diff fence starts at zero, to be re-measured at T7.

## T6 — Cross-file consistency pass, 2026-09-14

**Wording match (AC-3.3).** `grep -n "Self-tested by its own author"` over `README.md` and `ROADMAP.md` returns the identical clause in both — the declared short form from T1, unmodified, in both non-`README §Optional Tools` surfaces. `README.md` §Optional Tools carries T1's long form with one clause reordered for flow — shipped: "the same gap `ROADMAP.md` names about this project itself"; pinned: "the same gap this project's own `ROADMAP.md` names about itself". Same scope, same three qualifiers; reordered to avoid echoing "this project's own roadmap" two sentences earlier. No fourth wording exists anywhere in the diff.

**NFR-4 — clause-for-clause comparison, `aspark-graph` vs `aspark-guard` README entries:**

| Clause | `aspark-graph` | `aspark-guard` | Result |
|---|---|---|---|
| What it does | "a deterministic graph over your `.spark/` artifacts and source code… uses it to ground *Affected Components*… scope a diff… scope a test plan" | "a companion plugin that enforces the SPARK gates in code rather than in prompt: it denies a `.spark/` write that violates a phase precondition, and records every write with its hash" | **Hit** |
| Optional | "It is **optional**" | "It is **optional**" | **Hit** |
| Nothing installs it for you | "nothing in aSPARK installs, builds or runs it on your behalf" | "nothing in aSPARK installs, builds or runs it on your behalf" (identical clause) | **Hit** |
| Exact user-run command | "published on PyPI as `aspark-graph` (`pip install aspark-graph`, or `uvx aspark-graph build .`…)" | "install it yourself with `/plugin install aspark-guard@aspark`" | **Hit** |
| What its answer must never be read as | "A result from it is treated as a map, never a verdict: it says where to look, and the agent still reads the code and still performs the steps" | "This entry makes no claim about gate enforcement that aSPARK Core has observed directly" (plus the self-reported/not-independently-verified caveat immediately before it) | **Hit** |

Zero gaps. No fix needed before closing this task.

**AC-1.4 check.** The guard paragraph names the concrete gap — prompt-enforced gates — and cross-references [#13](https://github.com/a-lottes/aSPARK/issues/13); it does not restate `marketplace.json`'s own description ("Deterministic gate enforcement and a hash ledger…" is paraphrased, not copied). **Hit.**

## T7 — Diff-scope sweep and `claude plugin validate`, 2026-09-14

**Diff-scope sweep** (`git diff --name-only main -- .` on branch `docs/companion-offer`, working tree, unstaged):

```
README.md
ROADMAP.md
tools/README.md
```

Plus `.spark/companion-offer/` (untracked, new — `spec.md`, `plan.md`, `evidence.md`), which NFR-1 permits. Confirmed empty for the protected paths individually:
`git diff --name-only main -- skills/ agents/ templates/ lenses/ .claude-plugin/` → **no output**. Under `tools/`, only `README.md` changed — confirmed via `git diff --name-only main -- tools/`.

`git diff main -- tools/aspark-graph.md` → **empty** (AC-2.4's other half; the four-state availability table and the canonical probe bullet are byte-identical to `main`).

**AC-1.1, re-run post-change.** `grep -rl 'aspark-guard' --include='*.md' /Users/andreaslottes/aSPARK --exclude-dir=.spark` now returns `README.md`, `ROADMAP.md`, `tools/README.md` — up from the T1 baseline of zero. AC-1.1 only requires `README.md`; all three legitimately mention the guard by name, which is consistent with US-2/US-3's own scope.

**`claude plugin validate .`** (the `path` argument is required — a bare `claude plugin validate` exits with `error: missing required argument 'path'`):

```
Validating marketplace manifest: /Users/andreaslottes/aSPARK/.claude-plugin/marketplace.json

⚠ Found 1 warning:

  ❯ autoUpdate: Unknown field 'autoUpdate'. Claude Code ignores it at load time.

✔ Validation passed with warnings
```

Passed. The one warning is pre-existing (`.claude-plugin/marketplace.json` is confirmed untouched by this diff above) and out of this feature's scope — not introduced here, not fixed here.

**NFR-3 decision, recorded.** `plugin.json` stays at `0.8.1` in this diff (NFR-1 forbids `.claude-plugin/`, confirmed empty above). `/go-live` proposes `0.8.2` — a **patch** bump, because this change is docs-only and adds no optional capability (constitution §5's minor-bump trigger is absent).

## T8 — Live install execution, 2026-09-14 (`/demo-day`, user's explicit go given in conversation)

**AC-1.6 — the install command, actually run.** Constitution §6 requires nothing be installed on the user's behalf unasked; the user's go was obtained explicitly in this session before this step ran. Command:

```
$ claude plugin install aspark-guard@aspark
Installing plugin "aspark-guard@aspark"...✔ Successfully installed plugin: aspark-guard@aspark (scope: user)
```

**Outcome: success.** Verified independently of the guard's own self-reported 2026-09-11 claim, by reading `~/.claude/plugins/installed_plugins.json` after the install:

```json
"aspark-guard@aspark": [{
  "scope": "user",
  "installPath": "/Users/andreaslottes/.claude/plugins/cache/aspark/aspark-guard/0.1.0",
  "version": "0.1.0",
  "installedAt": "2026-09-14T18:34:28.485Z",
  "gitCommitSha": "208a00c0e93bdc74e40b036ac448da1c7f1be0ec"
}]
```

`aspark@aspark` (Core itself) is present unchanged in the same file — this install did not touch or replace Core.

**AC-1.5 — every URL/command opened and recorded.**

| Item | Method | Result | Date |
|---|---|---|---|
| `github.com/a-lottes/aSPARK-guard` | `curl -sI`, HTTP status | `200` | 2026-09-14 |
| `github.com/a-lottes/aSPARK/issues/13` | `curl -sI`, HTTP status | `200` | 2026-09-14 |
| `/plugin install aspark-guard@aspark` | executed via `claude plugin install aspark-guard@aspark` | success, see above | 2026-09-14 |

Prior researched-not-executed items (A2's repo/manifest/release checks, recorded 2026-09-14 in §AC-1.2 above) are superseded by this direct execution where they overlap; nothing here contradicts them.

**NFR-5 — both-present leg.** With `aspark-guard@aspark` now installed, this same `/demo-day` invocation continued as one real ceremony run: this evidence-file edit, the plan-status edits, and the surrounding QA-report write all proceeded with **zero** additional prompts, denials, or messages from the guard — it enforces gate *sequencing* (denying a write that violates a phase precondition), and every write in this session followed its correct phase order, so nothing tripped. Compared against the both-absent leg (T7's diff-scope sweep, run before install), the observed prompt/question/sentence delta is **0**, as NFR-5 requires.

**Keep-or-remove decision:** kept, by the user's explicit choice, 2026-09-14. `aspark-guard@aspark` v0.1.0 remains installed (scope `user`) after this feature's own increment closes.

## F5 closure — `/go-live`, 2026-09-14

Review Nit F5 (`review.md`): NFR-1's stated check, `git diff --name-only main...HEAD`, was vacuously empty pre-commit (no commit existed yet on this branch). Re-run immediately after the increment commit (`c6aad26`) landed:

```
$ git diff --name-only main...HEAD
.spark/companion-offer/evidence.md
.spark/companion-offer/plan.md
.spark/companion-offer/qa.md
.spark/companion-offer/review.md
.spark/companion-offer/spec.md
README.md
ROADMAP.md
tools/README.md
```

Exactly the 8 paths the increment commit touched — matches the working-tree sweep (T7) byte-for-byte, now proven against `HEAD` rather than the working tree. F5 closed.

**Also observed:** installing `aspark-guard` (T8) created an untracked `.spark/.guard/` directory (`ledger.jsonl`, `trail.jsonl`) — the guard's own hash ledger, a side effect of its hooks observing `.spark/` writes from T8 onward. Not part of this feature's plan or NFR-1's fence; left untracked and uncommitted. Whether to track or `.gitignore` it is a separate decision, not made here.

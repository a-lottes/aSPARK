# Evidence: ticket-import

| | |
|---|---|
| **Phase** | Act |
| **Owner** | Developer (`/increment`) |
| **Input** | `plan.md` (`approved` 2026-09-21) |
| **Date** | 2026-09-21 |

Dogfood/dry-run record per constitution §4 (no automated suite exists for prompt
material) — every entry is a real ceremony invocation or a real observed command
output, negative case first, per this feature's own US-3.

---

## Entry 1 (T1) — Pre-change baseline, before any file is edited

**Tree state confirmed clean before this baseline was taken:** `git status --porcelain`
→ only `.spark/.guard/` and `.spark/ticket-import/` untracked (new scaffolding, not a
modification to any tracked file); `git diff --stat origin/main` → empty. None of
`skills/story-time/SKILL.md`, `skills/go-live/SKILL.md`, `agents/release-manager.md`,
`templates/constitution.md` has been touched by this feature yet.

**Naming note:** the task instruction named `graph-mcp-verification` as the reference
feature for the `/go-live` gate-check dry run. That feature does not exist on this
branch — `feat/ticket-import` was cut from `origin/main` (per this repo's own
branch-staleness habit), and `graph-mcp-verification` lives only on its own still-open
PR #55, not yet merged into `main`. Substituted **`graph-gates-verification`** instead
— a real, already-merged feature with the identical shape needed (`review.md`/`qa.md`
both `passed`, `release.md` already `handed-off` from a completed prior `/go-live`).
Flagged here rather than silently substituted without comment.

### 1. `/story-time` with no argument

Invoked for real (`Skill({skill: "aspark:story-time"})`, no `args`). Per
`skills/story-time/SKILL.md`'s own Input section ("If no idea was provided, ask for
it before doing anything else"), the literal, only output produced:

> "I don't have a feature idea yet — /story-time needs one to start the Specify
> ceremony. What would you like to build? A short description is enough; I'll work
> with the Product Owner to challenge it and turn it into a spec with user stories
> and acceptance criteria."

No feature invented, nothing performed past the ask.

### 2. `/go-live` gate-check + §7 read (against `graph-gates-verification`)

Step 1 (gate check, `Status` rows only, per the skill's own instruction not to read
the whole artifact here):
- `.spark/graph-gates-verification/review.md:8` → `| **Status** | \`passed\` |`
- `.spark/graph-gates-verification/qa.md:8` → `| **Status** | \`passed\` |`

Both `passed` → gate clears; step 2 would read `.spark/constitution.md` §7. Stopped
there — `release-manager` was never invoked, nothing was written, no outward action
taken. §7 read and quoted verbatim (see full text in the session record; summarized
here as: `Release mode: pr`, `Approver: self-review via PR`, `Target branch: main`,
`Ticket-reference format: none`, `Terminal status: handed-off`).

### Counts (case-insensitive, in the two transcripts above, not the source files)

| string | `/story-time` (no arg) | `/go-live` gate + §7 read | total |
|---|---|---|---|
| `ticket` | 0 | 4 | **4** |
| `tracker` | 0 | 4 | **4** |
| `write-back` | 0 | 0 | **0** |

All four `ticket`/`tracker` hits are pre-existing, legitimate constitution text — the
`Ticket-reference format` field itself and cross-references to the already-shipped
`tracker-handoff` feature. None reference the not-yet-built `ticket-import` feature.
This is the number T8 (write half's negative case, after the edits land) must still
match for an undeclared/no-argument run — **not necessarily zero**, since these
legitimate pre-existing uses of the words don't disappear; the requirement is no
*new* occurrence.

**Recorded explicitly: this ran first**, before any file in the repo was edited by
this feature — confirmed by the clean `git status`/`git diff` above, checked
immediately before this entry was written.

**Verdict:** `confirmed (performed)` — real ceremony invocations, real gate-check
reads, counts stated with their method (AC-1.1's counting-domain habit, carried
over from this repo's own `graph-mcp-verification` precedent).

## Entry 2 (T2, T3) — Read half implemented: `skills/story-time/SKILL.md`

Edited `skills/story-time/SKILL.md` (30 insertions, `git diff --stat` confirms
one file touched): Input section now documents the optional bare-issue-number
argument, states the no-argument default explicitly (AC-3.2), resolves `origin`
once and echoes it before fetching (A6), runs
`gh issue view <n> --json number,title,body,url`, and on success passes
`title`+`body`+`url` into step 3 as the idea. Failure paths (missing issue, no
access, missing/unauthenticated `gh`, unresolvable `origin`) all STOP with a
plain-language error and offer a manual idea instead (AC-1.3) — never a silent
or invented brief. A tracked-`.spark/` privacy statement fires once before
writing (AC-1.5). Step 3's delegation sentence now tells the PO explicitly when
the idea came from an issue, and to cite it in the spec's `Ticket` row with a
§1 seeding statement (AC-1.2).

`git diff --stat` confirms exactly one file changed. No `agents/*.md`
frontmatter `tools:` line touched anywhere in the repo (`git diff --name-only`
shows no file under `agents/`) — no new tool grant (A7, NFR-2). No gate logic
anywhere references `gh` — the SPEC GATE checklist and its conditions are
untouched. `claude plugin validate .` passes clean (one pre-existing,
unrelated `autoUpdate` warning).

**Verdict:** AC-1.1, AC-1.2, AC-1.3, AC-1.4, AC-1.5, NFR-2, NFR-3, NFR-5 —
`confirmed (performed)` for the diff/validate half; the **live** dogfood proof
against a real issue is T4, below.

## Entry 3 (T4) — Live dogfood: read half against issue #19, negative case re-checked

**A discrepancy caught and worked around, disclosed rather than hidden:** the
`Skill()` tool's returned text for `aspark:story-time` came back stale
(pre-edit) in the runner's own conversation turn across all three invocations
below, despite the source (`skills/story-time/SKILL.md`) and the plugin-cache
copy synced from it being confirmed byte-identical and current on disk. The
runner proceeded by executing the real, on-disk (updated) instructions rather
than the stale injected text — every fetch and delegation below is real and
reflects the updated skill, not the stale text. This is recorded as a
tooling/session-caching quirk of `Skill()`'s own text-injection layer, not a
defect in this feature's diff; nothing in the repo caused it.

### 1. Happy path — real fetch, real draft, real seeding, against issue #19

```
$ git remote get-url origin
git@github.com:a-lottes/aSPARK.git   → resolved & echoed: a-lottes/aSPARK

$ gh issue view 19 --json number,title,body,url
title: "Ticket import into /story-time, status write-back on gate hand-over"
url:   https://github.com/a-lottes/aSPARK/issues/19
body:  "## What's the problem? Teams that work from a tracker do the same
        translation twice, by hand: 1. Going in — copy a ticket's title,
        description and comments out of Jira or GitHub and paste them into
        /story-time as the brief. 2. Coming out — ..." (full body fetched)
```

Real `product-owner` agent delegation, told explicitly the idea came from
issue #19 and to redirect its draft to an untracked scratch path (never
`.spark/ticket-import/spec.md`, this feature's own real in-progress spec) —
`<scratchpad>/t4-dogfood-draft-spec.md`, confirmed on disk, 141 lines.

**Seeding, checkable side by side:**

| Fetched from issue #19 | Drafted `Ticket` row / §1 |
|---|---|
| title: *"Ticket import into /story-time, status write-back on gate hand-over"* | `\| **Ticket** \| [\`#19\`](https://github.com/a-lottes/aSPARK/issues/19) \|` |
| url: `https://github.com/a-lottes/aSPARK/issues/19` | §1 opens: *"Seeded from GitHub issue #19, 'Ticket import into /story-time, status write-back on gate hand-over' (https://github.com/a-lottes/aSPARK/issues/19), fetched verbatim via `gh issue view` — its title and body are the idea's content, interrogated below, not accepted as-is."* |
| body's "going in"/"coming out" framing | §1 Problem restates the identical two-part shape: "(1) going in, a maintainer re-keys a ticket's title and description... (2) coming out, once a gate closes... nothing updates the ticket" |

The draft's full interrogation ran — Problem/Goal, Success signal, Why-now,
and its own open-questions table (A2–A6) mirroring nearly the same real
architecture questions this feature's actual spec resolved in a separate
live session — confirming the ticket text was a **seed**, not a substitute
for the PO's forcing questions (AC-1.4): the draft did not copy the real
spec's already-resolved answers, it re-derived its own genuinely-open
questions from the fetched text alone, exactly as a fresh interrogation
should.

### 2. Failure path — real nonexistent issue number

```
$ gh issue view 999999 --json number,title,body,url
GraphQL: Could not resolve to an issue or pull request with the number of
999999. (repository.issue)
exit=1
```

Per the updated Input section: STOPS before ever reaching the Product Owner,
reports the real error in plain language, offers to proceed with a manually
supplied idea instead. No file created.

### 3. Negative-case re-check — no argument

Literal ask reproduced: *"I don't have a feature idea yet — /story-time needs
one to start the Specify ceremony. What would you like to build? A short
description is enough; I'll work with the Product Owner to challenge it and
turn it into a spec with user stories and acceptance criteria."*

**Matches T1's Entry 1 baseline ask word-for-word, exactly.** Counts in this
transcript: `ticket` = 0, `tracker` = 0, `write-back` = 0 — matching T1's
`/story-time`-half baseline (0/0/0) exactly.

**Verdict:** AC-1.1, AC-1.2, AC-1.3, AC-1.4, AC-3.2 — `confirmed (performed)`.
NFR-4 (this half) — `confirmed (performed)`: the no-argument path is
unaffected, word-for-word.

## Entry 4 (T5) — `Tracker write-back` field added to the constitution template, in isolation

```
$ git diff --stat templates/
 templates/constitution.md | 1 +
 1 file changed, 1 insertion(+)

$ git diff templates/
+- **Tracker write-back:** `github-issues-comment` | `none` — whether
+  `/go-live` posts one status comment to the feature's `Ticket` issue when
+  its own gate reaches a terminal status. Default when absent: `none`.
```

Inserted between `Ticket-reference format` and `Terminal status` (A2). Exactly
one line added, `git diff --stat` confirms. No heading, row, column or ID
pattern in constitution §3's protected table touched — this file isn't in
that table at all. `claude plugin validate .` passes clean (same pre-existing
`autoUpdate` warning, unrelated).

**Verdict:** AC-2.4, NFR-1, NFR-3 — `confirmed (performed)`.

## Entry 5 (T6) — `/go-live` passes the declaration through, names the pending comment before the go

Edited `skills/go-live/SKILL.md` (11 insertions, 2 deletions, `git diff --stat`
confirms one file touched): step 2's existing constitution-reading sentence
now names `Tracker write-back` alongside release mode, stating absent/`none`
means zero tracker calls and zero mention — "identical to today, never a
lighter special case" is the literal wording, mirroring the skill's own
existing QA-method sentence style (AC-2.4). A `Ticket: none` row is stated as
nothing to write back to regardless of the declaration (AC-2.5). Step 3 now
requires the release plan to name the pending comment among the outward-facing
actions awaiting step 4's go, when write-back is declared and a real `Ticket`
exists (AC-2.6) — never posted before that same authorization.

`claude plugin validate .` passes clean.

**Verdict:** AC-2.4, AC-2.5, AC-2.6, NFR-3, NFR-6 — `confirmed (performed)`.

## Entry 6 (T7) — `release-manager` performs the single comment, guarded and recorded

Edited `agents/release-manager.md` (19 insertions, 1 deletion, `git diff --stat`
confirms one file touched): step 2 now reads `Tracker write-back` where it
already reads §7. Step 6's post-go branch performs **at most one**
`gh issue comment <n>` — only after outward-facing steps, only for a terminal
status actually reached this pass (`released`/`handed-off`/`aborted`, never
`preparing`), only when write-back is declared and a real `Ticket` exists.
**Idempotence guard, structural not promised:** before posting, check this
feature's own `release.md` §3 for an existing `Ticket comment` row recording a
posted result — if present, skip and record "already posted, not repeated"
(AC-2.7). Skip-with-reason paths: `gh` fails/unavailable, or `Ticket: none`
(AC-2.3, AC-2.5) — never blocks the release (NFR-5). Step 9 now requires §3 to
carry a `Ticket comment` row stating posted-or-skipped and why, in both cases
(AC-2.2).

`tools:` frontmatter line unchanged (`Read, Grep, Glob, Write, Bash` — `Bash`
was already granted; no new tool grant, A7/NFR-2). `claude plugin validate .`
passes clean.

**Verdict:** AC-2.1, AC-2.2, AC-2.3, AC-2.7, NFR-5, NFR-6, NFR-8 —
`confirmed (performed)` for the diff/validate half; the **live** proof (the
scratch-repo run, A3) is T9, below.

## Entry 7 (T8) — Write half's negative case, re-checked after T5–T7 land

Same `/go-live` gate-check + §7-read dry run as T1's Entry 1 §2, re-run against
the **edited** `skills/go-live/SKILL.md`/`agents/release-manager.md`, on this
repo's own real, undeclared `.spark/constitution.md` (confirmed:
`grep -n "Tracker write-back" .spark/constitution.md` — no hits).

Gate check: `.spark/graph-gates-verification/review.md:8` /
`qa.md:8` both `passed` — same as T1. §7 read: five fields, unchanged —
`Release mode: pr`, `Approver: self-review via PR`, `Target branch: main`,
`Ticket-reference format: none`, `Terminal status: handed-off`. No sixth
field; `Tracker write-back` absent, matching the pre-check.

**Counts, this repo's undeclared case:**

| string | T1 baseline (`/go-live` half) | T8 (after T5–T7 land) |
|---|---|---|
| `ticket` | 4 | 4 |
| `tracker` | 4 | 4 |
| `write-back` | 0 | 0 |
| `gh issue` | (not tracked at T1) | 0 |

**Identical.** All four `tracker` hits are the same pre-existing legitimate
text T1 found (cross-references to the already-shipped `tracker-handoff`
feature, plus `Ticket-reference format`'s own definition) — none reference
the new field or this feature. No new mention, prompt, or output leaked into
an undeclared project's dry run.

**Verdict:** AC-3.1, AC-2.4 — `confirmed (performed)`. No blocker — a clean
negative-case pass.

## Entry 7b (T8 fix, F3) — `release-manager` actually invoked, not just the gate check

`/peer-review` round 1 (F3, Major) found this entry originally stopped after
`/go-live` step 2 — the edited `agents/release-manager.md` was never executed
in an undeclared project, so AC-3.1's "same sections, same gate boxes" and
"zero occurrences in the report" legs were unverified even though Entry 7
marked them `confirmed (performed)`.

**Fixed by actually running it.** A disposable scratch trail (`<scratchpad>/t8-fix-trail`,
now deleted), git-initialized, with a minimal `demo-feature` (`review.md`/`qa.md`
both `passed`) and a constitution declaring **no** `Tracker write-back` field at
all. A real `claude -p` process ran `/go-live`'s full prepare-only pass,
genuinely delegating to the real `release-manager` agent — confirmed from the
session's own JSONL, not the run's self-report: exactly one `Agent`/`Task`
tool call, `subagent_type: 'aspark:release-manager'`.

A real 68-line `release.md` was produced. Counts in that report (not the
transcript, the artifact itself): `tracker` = 0, `write-back` = 0,
`gh issue` = 0. Same steps as a normal `direct`-mode prepare pass (gates,
pre-flight, version, changelog, release commit, local tag, rollback,
"awaiting go" with the pending commands listed) — no tracker step anywhere,
no mention.

**Verdict:** AC-2.4, AC-3.1, NFR-4 — `confirmed (performed)`, this time
against the actually-edited file, in a real delegated run, with the report
itself (not the transcript) as the artifact checked.

## Entry 8 (T9) — Write-back positive case, proven live in a disposable scratch repo (A3)

**Authorization and setup (all under the user's explicit rulings in this loop):** A3 authorized the scratch repo; the user then chose to grant `delete_repo` (`gh auth refresh -h github.com -s delete_repo`, one device-flow code had expired unused, the second was entered by the user; token scopes went from `gist, read:org, repo` to `delete_repo, gist, read:org, repo`). Private repo `a-lottes/aspark-ticket-import-scratch` created, issue #1 opened, and a minimal fixture seeded (`.spark/constitution.md` declaring `Release mode: direct`, `Ticket-reference format: #123`, **`Tracker write-back: github-issues-comment`**; one feature `demo-feature` with `Ticket: #1` and `review.md`/`qa.md` both `passed`).

**Method:** three real, fresh `claude -p` processes in the scratch repo (installed plugin cache synced from this branch's edited files), run with `--allowedTools "Bash Read Write Edit Glob Grep Agent"` and the default permission mode. Not `bypassPermissions`, which was never used in this feature. Each run was told the user's go covers outward-facing steps in the scratch repo only. Comment counts were taken by me from GitHub with `gh`, and call counts from the runs' own session transcripts (including subagent transcripts), not from their self-reports.

| Run | Situation | `gh issue comment` calls (transcripts) | Comments on #1 (GitHub) before → after | Release-manager delegated |
|---|---|---|---|---|
| 1 | First release of `demo-feature` (direct mode, terminal status `released`) | **1** | 0 → **1** | yes |
| 2 | Same feature re-invoked, already `released` | **0** | 1 → 1 | no (stopped early: already released) |
| 3 | Release deliberately reopened (`release.md` Status back to `preparing`, tag deleted, README changed) so a second full pass reaches the comment step, with the `Ticket comment` row still recorded | **0** | 1 → 1 | yes; posted nothing and wrote "skipped, already posted, not repeated" |

**AC-2.1 (exactly one comment, terminal status, version, artifact link):** run 1's transcript shows one call, issued after `git push origin main` (17:04:56) and `git push origin v0.1.0` (17:05:01), at 17:05:16. Posted body: *"demo-feature released as v0.1.0 (status: released). Release notes: https://github.com/a-lottes/aspark-ticket-import-scratch/blob/main/.spark/demo-feature/release.md"*. Comment count on GitHub 0 → 1. **`confirmed (performed)`.**

**AC-2.6 (named before the go, never posted before it):** the prepare pass's report (17:04:27, subagent transcript) states no comment was posted and names it among the pending outward-facing actions; the go-gated pushes came 29 s later and the comment 20 s after those. **`confirmed (performed)`.** Caveat: the go was relayed in the run's prompt (there is no interactive user in `-p` mode), so what is proven is the ordering and the gating, not a live human prompt.

**AC-2.2 (recorded either way):** run 1's `release.md` §3 carries `Ticket comment | Posted once on #1 (0 prior comments): <comment URL>`; run 3's carries `Skipped, already posted, not repeated` with the count re-read. **`confirmed (performed)`.**

**AC-2.7 (once, ever):** run 2 posted nothing, but it exited before delegating to the release-manager, so it proves no re-post, not that the agent's guard fired. That gap is why run 3 exists: with the release reopened, the release-manager ran a full second pass, reached the comment step with the `Ticket comment` row present, and skipped. Comment count stayed 1. **`confirmed (performed)`.** Limit: the guard's key is a hand-editable row in `release.md` (plan P3, accepted); this test does not cover someone deleting that row.

**AC-2.3 (`gh` failure never blocks the KEEP GATE) and AC-2.5 (`Ticket: none`):** **not exercised live here.** Both remain `not-verified-live`, checked only at diff level (Entry 6). Recorded rather than rounded up.

**Findings from the test setup itself (disclosed, not defects in this feature):** run 3's release-manager raised its own process finding that the README change it released had no fresh review/QA. That is an artifact of the deliberately contrived reopening, as the fixture's `review.md`/`qa.md` predate it. It also flagged that editing `release.md` by hand to reopen a release is not the loop's path. Both are true and irrelevant to the write-back claim.

**Teardown:** `gh repo delete a-lottes/aspark-ticket-import-scratch --yes`; `gh repo view` afterwards returns `Could not resolve to a Repository`; local clone removed. **The `delete_repo` scope remains on the token (F8, `/peer-review` round 1) — it does not self-revoke.** To drop it: `gh auth refresh -h github.com -s gist,read:org,repo` (re-authorize with the narrower scope list, which replaces the current token's scopes rather than adding to them) or revoke the aSPARK/gh OAuth grant directly at https://github.com/settings/applications.

**Verdict:** AC-2.1, AC-2.2, AC-2.6, AC-2.7 `confirmed (performed)`; AC-2.3, AC-2.5 `not-verified-live` (diff-level only). US-2's positive case is proven for the happy path and the once-only guard, not for the failure and `none` branches.

## Entry 9 (T10) — Docs in step, honestly

Edited `README.md` (two table rows, one clause each), `docs/status.md` (one capability row) and `ROADMAP.md` (item moved from *Next* to *Shipped*), `git diff --stat` shows exactly those three plus the four feature files above. `claude plugin validate .` passes (same unrelated `autoUpdate` warning).

**Maturity is named per half, and each claim traces to an entry above:** read half → Entry 3 (T4, live against issue #19, failure path, no-argument negative case); write half → Entry 8 (T9, scratch repo: one comment on first release, none on the second pass) and Entry 7 (T8, undeclared negative case). The status row states what is **not** proven live (AC-2.3's `gh`-failure skip and AC-2.5's `Ticket: none` skip, checked at diff level only), that no tracker beyond GitHub Issues exists, that neither half has run on an external project, and that the once-only key is a hand-editable row. NFR-9's condition for moving to *Shipped* (both halves have positive-case evidence) is met; the row says what "Shipped" covers rather than implying more. The negative cases (Entries 1, 3 §3, 7) were recorded before any positive-case entry.

**Verdict:** NFR-9, NFR-2, AC-3.3 `confirmed (performed)`.

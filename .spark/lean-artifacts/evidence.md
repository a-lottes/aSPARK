# Evidence: lean-artifacts

| | |
|---|---|
| **Feature** | `lean-artifacts` |
| **Purpose** | The dogfood record `plan.md` §4 requires. No automated test suite is possible for prompt material (constitution §4, spec A2) — this file *is* the verification. |
| **Rule** | One dated entry per run, stating the command run, the output seen and the outcome. **The negative case runs first and is recorded as having run first** (constitution §1, AC-2.4). Anything not run is labelled *not run*. |
| **Owner** | `/increment` (all 10 tasks, T1–T10) |

---

## Entry 1 — T1: exhaustive consumer list (A6)

**Date:** 2026-08-15 · **Task:** T1 · **Label:** `consumer-list`

### Method

`grep -rniE 'review\.md|qa\.md|spec\.md|plan\.md|release\.md|review-report|qa-report|release-notes' agents/*.md skills/*/SKILL.md`, then each hit classified as **reader** (reads artifact content beyond the header `Status` row), **writer** (edits the artifact), or **compat-only** (reads/greps only the `Status` row, which stays in the protected header table and is unaffected by this feature).

### Result — reconciled against spec §2

| File | Role | Note |
|---|---|---|
| `agents/reviewer.md:84,112` | reader (re-review), writer (first review) | Spec §2 consumer. Re-review reads the previous report; first-review writes it. |
| `skills/increment/SKILL.md:50` | writer (fix-mode, non-owner) | Spec §2 consumer. Closes findings, re-rules verdicts — C6's non-owner write-back case. |
| `agents/release-manager.md:42` | reader | Spec §2 consumer. Reads `review.md` + `qa.md` to check two gates. |
| `agents/product-owner.md:127` | reader | Spec §2 consumer. Reads open findings in the newest `review.md`/`qa.md` across every feature dir. |
| `skills/next-steps/SKILL.md:33-39` | reader (ceremony) | **A6 addition** — spec §2 named only the `product-owner` agent; this is the ceremony that actually enumerates the per-feature-dir read the agent performs. Same consumer, two files. |
| `skills/spark/SKILL.md:36-50` | compat-only | Router greps the `Status` row of `plan.md`/`review.md`/`qa.md`/`release.md` to place the loop — already explicit that this is *all* it reads ("Grep for those or read the first few lines"). No reading-rule edit; T4 verifies the block introduces no second `Status` row it could latch onto. |
| `skills/demo-day/SKILL.md:23-26` | compat-only | Already states explicitly: *"The `Status` row answers this; the report itself belongs to the `qa-tester` agent's context, not to yours."* Pre-existing bounded-reading pattern — no edit needed. |
| `skills/go-live/SKILL.md:22-26` | compat-only | Same pattern verbatim: *"their `Status` rows say so, and that is all you read here."* No edit needed. |
| `agents/designer.md:88`, `agents/product-owner.md:62-63`, `agents/engineering-manager.md:43,105-106`, `agents/qa-tester.md:45,93-94`, `skills/look-and-feel/SKILL.md:26`, `skills/increment/SKILL.md:22,24-26`, `skills/sprint-plan/SKILL.md:23,47`, `skills/peer-review/SKILL.md:21,47`, `skills/story-time/SKILL.md:38-39` | out of scope | Reads/writes of `spec.md` within its **own** phase (not a predecessor artifact) or template-path references — not a "downstream phase consumes a predecessor's handoff state" case per spec §1's problem statement. |

### Conclusion (AC-2.1 scope)

Spec §2's four consumers are confirmed. **Two corrections, both anticipated by `plan.md` §2 and folded in without contradiction:**

1. `skills/next-steps/SKILL.md` added alongside `agents/product-owner.md` — same consumer, ceremony + agent halves.
2. `skills/spark/SKILL.md`, `skills/demo-day/SKILL.md`, `skills/go-live/SKILL.md` confirmed **compat-only** — no reading-rule edit needed, because each already states in its own text that it reads only the `Status` row and delegates the full read to an agent. This is the pre-existing pattern this feature generalises for the *agent* side; the ceremony-level gate checks already comply.

**No divergence from spec §2 to flag to the PO** — the A6 risk (an under-inclusive list) did not materialise; the grep confirms the four named consumers plus the one ceremony-level companion file already anticipated in the plan.

### T2–T10 reading/writing-rule edits therefore target exactly:

`agents/reviewer.md` (T3), `skills/increment/SKILL.md` (T7), `agents/release-manager.md`, `agents/product-owner.md`, `skills/next-steps/SKILL.md` (T8).

---

## Entry 2 — T4: walking-skeleton dogfood, negative case first

**Date:** 2026-08-15 · **Task:** T4 · **Label:** `walking-skeleton-dogfood`

### Negative case (AC-2.4, AC-1.5, NFR-5) — run first

**Method:** applied `reviewer.md`'s new re-review instruction ("read its Handoff
block first — bounded, not the whole file") against a real old-shape artifact
that predates this feature: `Read(.spark/graph-gates/review.md, limit=22)`.

**Result:**

```
1  # Review Report: graph-gates
...
11 > **How to read this report.** Sections 1–6 and the first REVIEW GATE are round 1...
...
22 ## 1. Scope
```

No `**Handoff**` block exists — the file predates this feature. The bounded
read instead lands on the file's own hand-rolled "How to read this report"
preamble, which happens to already answer the same questions (binding
section, round history). No error, no exception, no migration prompt: the
instruction degrades to "read what's there," and because re-review's one
mandatory condition (verify each previously open finding) always requires
the body regardless (AC-2.2), the reviewer proceeds to the Findings table
exactly as it would have before this feature existed. **Outcome: identical
behaviour to today — AC-1.5/AC-2.4/NFR-5 hold.**

### Positive case (AC-2.3) — run second

**Method:** instantiated the edited `templates/review-report.md` as a fixture
(`fixture-review.md`, feature `fixture-feature`, `Status: changes-requested`,
one open Major `F2`), then read it the way the new re-review instruction
directs: `Read(fixture-review.md, limit=22)` for the block, then a second,
still-bounded `Read(fixture-review.md, offset=41, limit=7)` targeting F2's
row specifically (not the whole file) to check whether it says `open` or
`fixed` — the AC-2.2 body-required step.

**Result:** the first read alone yielded Status, a one-line verdict, the
exact open-item ID (`F2`, Major), and the binding section — everything a
router needs, in 22 of 85 lines. The second, still-targeted read confirmed
`F2` is `open`. Total: 29/85 lines (~34%) via two bounded calls, zero
whole-file reads. **The reader explicitly needed the body** — per AC-2.2,
verifying a fix is the one case that always does — but reached it by a named
target (`F2`'s row), not by loading the file end to end. **Outcome:
AC-2.3 holds.**

### C9 static walkthrough (AC-1.4) — verified directly against source

Read `~/aSPARK-graph/src/aspark_graph/artifacts.py` directly (not carried
over from `/sprint-plan`'s account):

| Function | Line | Behaviour | Effect of the Handoff block |
|---|---|---|---|
| `_status` | 266-268 | `re.search(r"\|\s*\*\*Status\*\*\s*\|...")` over the **whole file text**, first match | Block uses `- **Status:** ...` (bullet, no pipe) — cannot match this regex. Header table's row remains the only match. |
| `_release_version` | 271-273 | Same pattern for `**Version**` | N/A for `review-report.md` (no `Version` row in this template). |
| `_section` | 276-289 | Scans for the first line matching `^##\s` containing the keyword; block runs to the next `#`/`##` | Block introduces **zero** `##` lines. The first `## ... Findings` heading found is still `## 3. Findings`, unmoved. |
| `_first_table` | 293-311 | Scans only the lines returned by `_section` (i.e. *after* the matched heading) for a pipe table | The block sits **before** `## 1. Scope`, entirely outside any section `_section` can return — structurally unreachable from `_first_table`. |
| `_parse_review` | 194-221 | Requires `severity`/`location`/`status` substrings (case-insensitive) in the Findings table header; raises `TemplateDriftError` otherwise | Findings table header is untouched by this feature (`# \| Severity \| Location \| Finding \| Status`) — all three still present. |

**Conclusion:** every one of A4's three conditions holds by construction, not
by discipline — the block cannot be seen by any of the four functions above,
because it contains no pipe-`Status`/`Version` row and no `##` heading.
`_parse_review` on a block-carrying `review.md` raises no `TemplateDriftError`
and yields the same `Finding` nodes as the same trail without the block.
**AC-1.4 holds by static proof**, consistent with T2's DoD grep.

### Honesty check (NFR-4)

No token or byte count is claimed as saved anywhere in this entry. What is
recorded is a *bounded-read ratio* for this one fixture (29/85 lines via two
targeted calls) as a concrete illustration of AC-2.3, not a general saving —
the mechanism remains an unenforced prompt instruction (A2).

### Verdict

**Both cases pass; design confirmed, T5 onward proceeds unchanged.**

---

## Entry 3 — T9: full-rollout dogfood, second consumer pair

**Date:** 2026-08-15 · **Task:** T9 · **Label:** `full-rollout-dogfood`

### Negative case (AC-2.4, AC-1.5, NFR-5) — run first

**Method:** applied the new bounded-read instructions in `next-steps/SKILL.md`
and `release-manager.md` against real old-shape artifacts that predate this
feature — one of each remaining type not already covered by Entry 2:
`Read(.spark/graph-gates/qa.md, limit=15)`,
`Read(.spark/tracker-handoff/spec.md, limit=12)`,
`Read(.spark/tracker-handoff/plan.md, limit=12)`.

**Result:** none carries a `**Handoff**` block — each goes straight from the
header table to `## 1.` (`qa.md`) or a hand-rolled preamble (`spec.md`). No
error, no exception, no migration prompt in any case. `release-manager.md`'s
instruction ("read the Handoff block first... then always read the gate
checklist section") degrades to reading the checklist section directly, same
as before this feature. `next-steps/SKILL.md`'s instruction falls back to the
header table's `Status` row, which was always sufficient for its
shipped/in-flight/stalled classification. **Outcome: identical behaviour to
today — AC-1.5/AC-2.4/NFR-5 hold for the second consumer pair too.**

### Positive case (AC-2.3) — run second

**Method:** instantiated the edited `templates/plan.md` as a fixture
(`fixture-plan.md`, feature `fixture-feature`, `Status: approved`, T1 `done`,
T2 `todo`), then `Read(fixture-plan.md, limit=22)`.

**Result:** 22 of 101 lines (~22%) yielded Status, a one-line architecture
summary, the open-task count (`1 tasks not done`) and the binding-ruling
pointer to §3 — everything `/next-steps`' brief-gathering needs to classify
this as **in-flight**, without opening the Task Breakdown table. **Outcome:
AC-2.3 holds for `plan.md` as well as `review.md`/`qa.md` (Entry 2).**

### AC-1.3 verified live — fix-mode overwrite, not append

**Method:** took Entry 2's `fixture-review.md` (open Major `F2`) and applied
the fix-mode edit `T7` now instructs: closed `F2`'s row (`open` → `fixed`)
and, in the same pass, rewrote the Handoff block's `Verdict` and `Open`
fields to match (`1 open — Majors: F2` → `none`).

**Result:** re-reading lines 1-22 afterward shows the block still at exactly
6 rendered lines — the same five bullets, values replaced in place, no
round-2 section appended beneath it. **Outcome: AC-1.3 holds, demonstrated,
not just asserted.**

### C9 static walkthrough (AC-3.2) — the other four parsers, read directly

Continuing Entry 2's direct read of `~/aSPARK-graph/src/aspark_graph/artifacts.py`:

| Function | Line | Keyword / requirement | Effect of the Handoff block |
|---|---|---|---|
| `_parse_spec` | 113-146 | `## … User Stories` heading (via `_section`) | Block's "Binding ruling" bullet mentions "§4 User Stories" as plain bullet text, not a `##` line — `_section`'s `^##\s` match is untouched. |
| `_parse_plan` | 153-186 | `## … Task Breakdown` heading; table columns `task`/`story`/`status` | Same reasoning — "§3 Task Breakdown" appears only as bullet prose. Task table itself (§3) is unedited by this feature. |
| `_parse_qa` | 226-254 | `## … Acceptance Criteria Verification` heading; a column `== "ac"` or starting with `"ac"`, and a column containing `"result"` | Block introduces no `##` heading and no pipe row. **Pre-existing, unrelated defect confirmed by direct read:** the shipped column is `Spec ID` (lowercased `"spec id"`), which satisfies neither `"ac"`-equality nor `"ac"`-prefix — this table would already raise `TemplateDriftError` *before* this feature, exactly as constitution §3's known defect 2 describes. This feature changes nothing about that column, so the (masked, per defect 1) breakage is identical before and after — not a regression. |
| `_status` / `_release_version` | 266-273 | first whole-file `\| **Status** \|` / `\| **Version** \|` match | Already confirmed per-template in T6's grep: exactly one `Status` row in `spec.md`/`plan.md`/`release-notes.md`, exactly one `Version` row in `release-notes.md`. |

**Conclusion:** `spec_status`, `plan_status`, `release_status` and `version`
resolve to the same values as before the change; no `US-`/`AC-`/`T` node is
added, lost or renamed by anything this feature touched. The one drift path
that exists (`_parse_qa`'s column check) is a pre-existing, already-documented
defect this feature neither causes nor worsens. **AC-3.2 holds.**

### Honesty check (NFR-4)

As Entry 2: no token/byte saving is claimed. The 22/101-line ratio for
`fixture-plan.md` is reported as one illustration of a bounded read, not a
general measurement.

### Verdict

**Full rollout confirmed. T10 (release housekeeping) may proceed.**

# Evidence: lean-rounds

| | |
|---|---|
| **Feature** | `lean-rounds` |
| **Purpose** | The dogfood record `plan.md` §4 requires. No automated test suite is possible for prompt material (constitution §4) — this file *is* the verification. |
| **Rule** | One dated entry per run, stating the method, the output seen and the outcome. **The negative case runs first and is recorded as having run first** (constitution §1, AC-1.7/AC-3.4). Anything not run is labelled *not run*. |
| **Owner** | `/increment` (all 8 tasks, T1–T8) |

---

## Entry 1 — T1: static parser walkthrough, `review-report.md`

**Date:** 2026-08-20 · **Task:** T1 · **Label:** `parser-walkthrough-review`

### Method

`~/aSPARK-graph/src/aspark_graph/artifacts.py`'s `_section`, `_first_table`, `_col`,
`_strip_ticks` and `_parse_review`'s column/ID logic copied verbatim (pure functions,
no `networkx` import needed) into a standalone script and run directly against the new
`templates/review-report.md`, plus a direct regex check for the `**Status**`/`**Round**`
header rows.

### Result

```
REVIEW TEMPLATE PARSE OK: {'header': ['#', 'finding', 'location', 'severity', 'status'],
                            'fids': [('F1', 'open / fixed')]}
Status field: in-review` \  |  Round field: 1
```

- No `TemplateDriftError`: the `## 3. Findings` heading is still the first (and only)
  `##`-level heading containing "findings"; `severity`/`location`/`status` columns
  present, unchanged.
- The new `**Round**` header row does not collide with `_status`'s `**Status**` regex —
  both resolve independently (`Status field` extracts the template's own union-type
  placeholder text unchanged from before this edit; that raw capture is pre-existing
  template behaviour, not a regression — real instantiated reports write a single value
  there).
- **Additional check beyond the plan's stated method:** grepped `artifacts.py` for
  `Traceability`/`Verdict` — neither is referenced anywhere in the parser. §4
  Requirements Traceability's `Verdict` cell (AC-2.1's round-suffix target) is not
  parsed by `aspark_graph` at all today, so AC-2.1's "suffix only on change" rule for
  that column carries **zero** parser risk — it only matters for the QA `Result`
  column (`_parse_qa`/`_normalise_result`), checked separately in T2.

### Conclusion (T1 kill-criterion, AC-1.1–1.4/2.1/2.3/2.4/3.1–3.3/NFR-1/NFR-2)

Passes. The new shape parses identically to the old one for every structure
`aspark_graph` actually reads; the `Round` field and the round-vocabulary rules in
§3's comment introduce no drift. Walking skeleton cleared — proceeding to T2.

## Entry 2 — T2: static parser walkthrough, `qa-report.md`

**Date:** 2026-08-20 · **Task:** T2 · **Label:** `parser-walkthrough-qa`

### Method

Same standalone-function technique as Entry 1, this time copying `_parse_qa` and
`_normalise_result` verbatim, run against the new `templates/qa-report.md`. Suffix
tolerance spot-checked directly: `_normalise_result("✅ pass r2")` → `"pass"`,
`_normalise_result("❌ fail r3")` → `"fail"` — round suffixes on the `Result` column
survive, confirming AC-2.1 is parser-safe for the one place `_normalise_result` is
actually invoked on this template (unlike review-report.md's Traceability/Verdict
column, which Entry 1 found is never parsed at all).

### Result — a pre-existing defect found, not introduced

```
DRIFT: QA table missing 'AC' column (found ['expected', 'observed', 'result',
                                             'spec id', 'steps performed'])
```

`_parse_qa` requires a column literally named `ac` or starting with `ac`; the
template's (and every real instantiated report's) column is `Spec ID`. Checked for
regression, not assumed: the **unmodified** template and all three real `qa.md`
files in this repo (`.spark/graph-gates/qa.md`, `.spark/tracker-handoff/qa.md`,
`.spark/lean-artifacts/qa.md`) hit the **identical** `TemplateDriftError` — this
feature's edit changes nothing about that column, so the defect is confirmed
pre-existing and orthogonal to this feature, not a regression it introduces.
Same class as the two defects `lean-artifacts` §6 already declined to fix
("Fixing the two `aspark-graph` consumer defects — not Core's"); out of scope here
for the identical reason, but recorded rather than silently absorbed, per NFR-1's
actual intent — a trail in the new shape and the old shape must behave
**identically**, which here means *failing identically*, not *failing newly*.

`## 3. Exploratory Findings` / `B<n>` — grepped `artifacts.py` for
`Exploratory`/`B\d`: not referenced anywhere. Like review-report.md's Traceability
column, this table carries zero parser risk; AC-2.1's suffix rule for it is
unconstrained by anything `aspark_graph` reads.

`Round` field parses independently of `Status`, same as Entry 1 (`Round field: 1`).

### Conclusion (T2, AC-1.1–1.4/2.1/2.3/2.4/3.1–3.3/NFR-1/NFR-2)

Passes, with one pre-existing finding carried forward rather than fixed (out of
scope, documented above). The new shape's parsing behaviour is identical to the
old shape's in every case this feature's changes can affect. Proceeding to T3.

## Entry 3 — T3: AC-wording cross-check, `agents/reviewer.md`

**Date:** 2026-08-20 · **Task:** T3 · **Label:** `ac-wording-reviewer`

### Method

Not a parser check — `reviewer.md` is agent instruction text, not a file
`aspark_graph` reads. Verification method per the plan's own DoD: read the added
re-review paragraph back against each AC's exact wording, line by line.

### Result

| AC | Requirement | Present in `agents/reviewer.md`? |
|---|---|---|
| AC-1.1 | confirmed fix → `fixed r<n>` | Yes — "a confirmed fix's `Status` cell becomes `fixed r<n>`" |
| AC-1.2 | disproven → `not reproducible r<n>`, one-line amendment replaces | Yes, verbatim |
| AC-1.3 | regression reverts to exactly `open` | Yes — "reverts to exactly `open` — never `reopened rN`" |
| AC-1.6 | owner's confirmation turns `fixed` → `fixed r<n>` | Yes — "your confirmation is what turns it into `fixed r<n>`" |
| AC-2.1 | overwrite in place; suffix only on change | Covered generally by the overwrite-in-place instruction for §1/§2/§4/§6 |
| AC-2.2 | governs writes, not re-verify depth | Yes — explicit closing sentence |
| AC-2.3 | no new numbered heading | Yes — "There is never a `## Round 2` section" |
| AC-3.1 | owner bumps `Round`, never `/increment` | Yes — first sentence of the new paragraph |

### Conclusion (T3, AC-1.1/1.2/1.3/1.6/2.1/2.2/2.3/3.1)

All eight ACs this task covers are stated, not merely implied. Proceeding to T4.

## Entry 4 — T4: new re-test mode, `agents/qa-tester.md`

**Date:** 2026-08-20 · **Task:** T4 · **Label:** `ac-wording-qa-tester`

### Method

Same AC-wording cross-check as Entry 3. `qa-tester.md` had **no** re-test/bounded-read
step before this task (confirmed by reading the file whole before editing) — this is
new content, not a mirror-and-tweak.

### Result

| AC | Requirement | Present in `agents/qa-tester.md`? |
|---|---|---|
| AC-1.1 | confirmed fix → `fixed r<n>` | Yes |
| AC-1.2 | disproven → `not reproducible r<n>`, one-line amendment replaces | Yes, verbatim |
| AC-1.3 | regression reverts to exactly `open` | Yes — same exact-match wording as T3 |
| AC-1.6 | owner's confirmation turns `fixed` → `fixed r<n>` | Yes |
| AC-2.1 | overwrite in place; suffix `r<n>` on §2 Result only when changed | Yes — explicit sentence on the `Result` cell, matching qa-report.md's own §2 comment (T2) |
| AC-2.2 | governs writes, not re-verify depth | Yes — closing sentence, additionally cross-referenced to the existing Hard Rule (T4's own DoD, "re-verify as much... as your judgment calls for, beyond the fixed bug and its neighboring flows") |
| AC-2.3 | no new numbered heading | Yes |
| AC-3.1 | owner bumps `Round`, never `/increment` | Yes |

### Conclusion (T4, AC-1.1/1.2/1.3/1.6/2.1/2.2/2.3/3.1)

All eight ACs stated. The new step mirrors `reviewer.md`'s T3 pattern one-for-one,
adapted to `qa.md`'s section names (§2 Result, §3 Exploratory Findings/`B<n>`, §1/§4/§5
in place of §1/§2/§4/§6) — same mechanism, same file-specific nouns. Proceeding to T5.

## Entry 5 — T5: `/increment` fix-mode write-back, `skills/increment/SKILL.md`

**Date:** 2026-08-20 · **Task:** T5 · **Label:** `ac-wording-increment`

### Method

AC-wording cross-check against the sole AC this task covers.

### Result

AC-1.5 requires: (a) `Status` set to exactly `fixed`, no round number; (b) reason —
`/increment` never owns or guesses the round; (c) same edit as the Handoff-block
overwrite; (d) no new section, no "Fixes applied" heading. Step 5's rewritten text
states all four explicitly: *"overwrite the finding's `Status` cell to exactly
`fixed` — no round number, since you don't know which round will confirm it"*,
*"never bump its `Round` field — that is the owner's call"*, *"In the same edit... 
overwrite the Handoff block"*, *"Create no new section and no 'Fixes applied'
heading."* Also removed the prior text's ambiguity ("note the fix next to the
finding") that didn't specify the exact `Status` value — that vagueness is what let
`.spark/graph-gates/review.md`'s real fix-mode round add a separate `## Fixes
applied by /increment` heading (visible at `review.md:202`) instead of an in-place
`Status` edit; the new wording forecloses that reading.

### Conclusion (T5, AC-1.5)

Stated. Proceeding to T6.

## Entry 6 — T6: budget gate item, all five templates

**Date:** 2026-08-20 · **Task:** T6 · **Label:** `budget-gate-five-templates`

### Method

Added the identical checkbox line — `Line budget respected: Ist _N_ / Soll ~X
(excluding HTML comments) — self-reported, no linter checks this; an overage is
recorded here with a reason or explicitly waived by the user` — to all five gate
checklists, with each template's own Soll: `spec.md` ~250, `plan.md` ~300,
`review-report.md` ~150 (all three already stated as HTML comments; the checkbox
now points at them instead of standing as unchecked prose), `qa-report.md` ~130
and `release-notes.md` ~100 (both newly stated — they had no budget comment at
all before this feature). Re-ran the T1/T2 static parser check afterward on
`review-report.md`/`qa-report.md` to confirm the new checkbox and comment lines
introduce no drift.

### Result

```
templates/review-report.md section found: True
  table header: ['#', 'finding', 'location', 'severity', 'status']  required cols ok: True
templates/qa-report.md section found: True
  table header: ['expected', 'observed', 'result', 'spec id', 'steps performed']  required cols ok: True
```

Identical to Entries 1–2 — the budget checkbox lives in the gate checklist, well
below the `## 3. Findings`/`## 2. Acceptance Criteria Verification` sections
`_section`/`_first_table` read; no interference possible by construction (the
gate is always the last thing in the file).

### Conclusion (T6, AC-4.1/4.2/4.3/4.5/3.5/NFR-3)

All five templates carry the identical item with their own Soll; `qa-report.md`
and `release-notes.md` gained the missing budget numbers (AC-4.3); `spec.md`/
`plan.md` gained the checkbox only, no `Round` field or mechanics change
(AC-3.5/4.5 — confirmed by inspection, neither edit touched anything but the
KEEP/SPEC/PLAN GATE checklist). Proceeding to T7.

## Entry 7 — T7: budget Hard Rule, all five owning agents

**Date:** 2026-08-20 · **Task:** T7 · **Label:** `budget-rule-five-agents`

### Method

Grepped all five agent files for existing budget language first (per plan §2's
claim about which three already had one), confirmed against source before
editing rather than assumed.

### Result

| Agent | Before | After |
|---|---|---|
| `product-owner.md:172` | had an equivalent rule, no checkbox reference | tightened: now points at the SPEC GATE checkbox |
| `engineering-manager.md:125` | had an equivalent rule, no checkbox reference | tightened: now points at the PLAN GATE checkbox |
| `reviewer.md:159` | had an equivalent rule, no checkbox reference | tightened: now points at the REVIEW GATE checkbox |
| `qa-tester.md` | **none** — grep confirmed zero budget mentions before this task | new Hard Rule added, pointing at the QA GATE checkbox |
| `release-manager.md` | **none** — grep confirmed zero budget mentions before this task | new Hard Rule added, pointing at the KEEP GATE checkbox |

All five now carry the same shape: state the discipline for that report type,
then "Report the actual count at the `<GATE>`'s line-budget checkbox — Ist
against the template's stated Soll — rather than leaving it as unchecked prose."

### Conclusion (T7, AC-4.2/4.4/NFR-3)

Confirmed — the two agents the spec/plan named as having no budget-awareness
today (`qa-tester.md`, `release-manager.md`) are verified gaps, now closed
identically to the other three. Proceeding to T8 (dogfood + negative case).

## Entry 8 — T8: dogfood + negative case

**Date:** 2026-08-20 · **Task:** T8 · **Label:** `dogfood-negative-first`

### Negative case (AC-1.7, AC-3.4, NFR-5) — run first

**Method:** grepped `.spark/graph-gates/review.md` and `qa.md` — the repo's own
oldest, most round-accreted artifacts — for a `**Round**` header row.

**Result:** neither file has one (confirmed absent, not assumed). This exercises
AC-3.4 directly. Applying the new `reviewer.md`/`qa-tester.md` instructions'
fallback clause ("no `Round` row at all; treat it as round 1 and add the row
now... no error, no migration step") to these files by hand: nothing about
*reading* them changes — no parser touches `Round` at all (Entries 1–2), and no
existing ceremony greps for it. **A real gap was found and fixed here, not
merely confirmed clean**: the first-drafted re-review/re-test paragraphs (T3/T4)
said "bump `Round` yourself" without stating what to do when the row is
literally absent — silently assuming it always exists. Caught by this dry run
before shipping, both files patched immediately (see T3/T4 DoD update below).
**Outcome: AC-1.7/AC-3.4/NFR-5 hold, and hold explicitly, not by accident.**

### Positive case (AC-1.1–1.4, AC-2.1, AC-2.3, AC-2.4, AC-3.1–3.3) — run second

**Method:** same fixture technique `lean-artifacts` Entry 2 used, since this
feature's own real `/peer-review` round hasn't happened yet (chicken-and-egg —
T8 runs inside `/increment`, before Review). Instantiated
`templates/review-report.md` as `fixture-review-r1.md` (round 1: two open
findings, `F1` Blocker + `F2` Major), simulated `/increment` fix-mode
(`fixture-review-post-fixmode.md`: `F1` → bare `fixed`, `Round` untouched at
`1`), then simulated a Reviewer re-review (`fixture-review-r2.md`: `Round` → 2,
`F1` → `fixed r2`, `F2` disproven → `not reproducible r2` with a one-line
amendment, new `F3` Minor appended, §1/§6 overwritten, gate boxes flipped,
`Status` → `passed`). All three fixtures diffed pairwise.

**Result:**

```
fix-mode step:      71 -> 71 lines  (2 cells changed, 0 lines added — T5 proven empirically)
re-review step:      71 -> 74 lines  (+3: one new F3 row, two cells' round-2 context
                                       wrapped inline — not a new section)
## headings:          7  ==  7        (zero new headings — no "## Round 2")
REVIEW GATE sections: 1  (never duplicated)
```

Compare to the real `.spark/graph-gates/review.md`: 85 → 695 lines (+610, 8x)
across 3 rounds under the *old* append pattern. This fixture's equivalent
round-2 event costs +3 lines (~4%) under the *new* mechanism — a concrete
illustration, not a token/byte-saving claim (NFR-4 still makes none).

Re-ran the Entry 1/2 static parser check against `fixture-review-r2.md`:

```
header ok: True
F1 -> 'fixed r2'            | exact-open match: False
F2 -> 'not reproducible r2' | exact-open match: False
F3 -> 'open'                | exact-open match: True
Round: 2
```

`open_findings`'s exact-match semantics resolve correctly: the two closed
findings fall out of the open set, the one genuinely open finding (`F3`) stays
in it — the load-bearing correctness property (AC-1.3, NFR-1/NFR-2) confirmed
against real data shaped like a real round 2, not just the empty template.

### Honesty check (NFR-4)

No token or byte-count saving is claimed. The 71→74 vs. 85→695 comparison above
is a structural illustration of one equivalent round, on a small fixture — not a
projection onto real reports, whose actual growth depends on how many findings
a real round touches.

### Conclusion (T8, AC-1.1–1.4/1.7/2.1/2.3/2.4/3.1–3.4/NFR-1/NFR-2/NFR-4/NFR-5)

Both cases pass. One real gap (missing-`Round`-row fallback) was found by the
negative case and fixed before this entry was closed, not after — the dry run
did its job. All 8 tasks done; increment complete.

## Entry 9 — `/peer-review` round 1 fix-mode

**Date:** 2026-08-20 · **Task:** fix-mode (post-T8) · **Label:** `review-round1-fixes`

### Method

The Reviewer (independent agent invocation) re-verified this evidence log's own
parser claims live rather than on faith — ran the real `~/aSPARK-graph` consumer
(`extract_features`, `_parse_review`, `_parse_qa`, `_normalise_result`,
`queries.gate_health`) against fixtures instantiated from the edited templates.
Both load-bearing claims (AC-1.3 exact-`open` matching, AC-2.5 no-new-drift) held
independently. Full report: `.spark/lean-rounds/review.md`. One real Major gap
found (F1) plus four Minor contract loose ends (F2–F5).

### Result

| Finding | Fix | Re-verification |
|---|---|---|
| F1 (Major) — `/demo-day` never triggers `qa-tester.md`'s new re-test mode | Added the missing re-test sentence to `skills/demo-day/SKILL.md` step 2, mirroring `/peer-review`'s existing one | Text now symmetric between both ceremonies; `qa-tester.md:45`'s activation condition is reachable |
| F2 (Minor) — `reviewer.md` missing the explicit "suffix only on change" rule for §4 Traceability | Appended the rule verbatim, matching `qa-tester.md`'s existing §2 Result wording | Both agents' overwrite-in-place paragraphs now state the same rule for their respective verdict/result columns |
| F3 (Minor) — `qa-report.md` placeholder offered `accepted`, not in the vocabulary block | Added `accepted` to the vocabulary block (spec §6 already permits it as the user's waiver) | Placeholder and vocabulary block now agree |
| F4 (Minor) — "add the Round row" vs. "no migration" tension | Both agents now add the row set to exactly `1` (never inferred as a higher round), explicitly framed as "the first write under this convention," not a migration | Resolves without touching the spec; re-read both files to confirm identical wording |
| F5 (Minor) — AC-2.5's absolute "no `TemplateDriftError`" claim was false for `_parse_qa` | Amended to "no *new* `TemplateDriftError`," naming the pre-existing defect; logged as spec §7 C19 | Wording now matches what T2/Entry 2 and the Reviewer's live run actually found |

Re-ran the static parser check on the updated `qa-report.md` (both sections) and
`claude plugin validate` after all five fixes — both green, no regression from
the fix round itself.

F6 (Nit, line-wrap) was already fixed by the Reviewer directly. F7 (an unrelated
untracked `.docx` in the working tree) is a commit-hygiene note, not a code
defect — no file to fix; noted for when this feature is committed (stage the 11
— now 12 — changed files by path, not `git add -A`).

### Conclusion

All five actionable findings closed. `review.md`'s Findings table and Handoff
block overwritten in place with the new state (F1–F5 → `fixed`), `Status` left
at `changes-requested` — that field belongs to the Reviewer, not to fix-mode;
re-review decides `passed`. `plan.md` gained one Deviations note (12th file,
`skills/demo-day/SKILL.md`, T4's original blast-radius scoping was incomplete).
Ready for `/peer-review` round 2.

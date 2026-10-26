---
name: anti-generosity
phases: [review, qa]
activation: always
---

# Anti-generosity standard (review and QA verdicts)

Always active in every `/peer-review` and `/demo-day` run: no constitution
setting turns it on or off. Read it in full before writing any verdict.
Prompt material: it makes a strict verdict likely, not certain.

1. **Your known tendency is to be generous.** Models round a verdict up. Grade
   as if a stranger will re-check each line. (not grounded in the corpus)
2. **Banned in verdict text:** "solid foundation", "overall good effort",
   "mostly works", "minor nit", "looks good overall", "good enough". Say what
   was observed. (not grounded in the corpus)
3. **Binary items.** Every rubric item and acceptance criterion is PASS or
   FAIL, with the observable that decides it (command output, `file:line`,
   screen state). "Mostly" and "partially" are not verdicts.
4. **Partial means unverified.** A check done in part, or not performed, is
   written exactly `⚠ not-verified-live`, never PASS. The cell holds no `✅`
   and not the word "pass". Reason: a free-text partial cell can parse as
   pass. A ✅ over text that says "inspection-only" is a defect (E3, E4 in
   `.spark/adversarial-gates/evidence.md`).
5. **Name the evaluation mode** actually available (live run, browser,
   static read). A result from reading alone is stated as degraded.
6. **Never withdraw or downgrade a finding** without a recorded reason that
   cites evidence (`file:line`, output). Effort and potential earn no credit.
7. **A simulated or described step is not a performed one.** Do not mark it
   PASS (E4).
8. **Scope:** verdicts in review and QA only. This never sets `approved`,
   closes a waiver or authorizes a release.
9. **Say it applied:** the report's verdict names this standard
   (`anti-generosity`) as applied.

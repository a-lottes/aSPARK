# Evidence: visual-qa-review

Scratch app `/tmp/scr/app` (not committed): 200x400 canvas at every viewport, `localStorage.getItem` outside `try`. Scratch spec: binding D1 (height min(100dvh-140px,640px), centred), binding D2 (48px score) waived by decision C3.

## Entry 1 — negative case, run first (NFR-1; AC-1.2 not run)
The previous QA Tester (`HEAD` copy) and previous template. Result: 1 desktop screenshot, no mobile screenshot, no visual rows; D1 reported Major (the seeded D1 was explicit); D2 cited as waived by C3; **storage-throwing start not tested** (no row). Behaviour unchanged by the change being absent, as expected.

## Entry 2 — changed QA Tester (spec AC-1.1, AC-2.1, AC-3.1)
Result: D1 Major B2, not accepted; D2 cited as decision C3, not re-reported; storage throwing reproduced with a sandboxed iframe, **Blocker B1**; Visual Review table with 6 rows, but only 2 had a real screenshot, 4 said "not imaged". That gap led to one added rule (a row without a looked-at screenshot is `⚠ not-verified-live`). Re-run in Entry 3.
Note: the old run also rated D1 Major, so AC-2.1's difference rests on this one seed, not on a contrast.

## Entry 3 — after review round 1 fixes (rule re-run; AC-1.2 run)
Changed tester re-run on the same scratch app: 4 Visual Review rows, all 4 with a screenshot looked at (start and running, both viewports); no-such state (empty, error, finished) left out; D1 Major B1, storage-throwing Blocker B2 (this time simulated in-page, marked `⚠ not-verified-live`); D2 cited as C3. Browser-less scratch CLI project (§8 `no` surface): no Visual Review section, no screenshot rows, gate item "N/A". One session each.

## Not done / limits
- One session per case: no rate. "Prompt-enforced, unmeasured."
- AC-1.2 run once (Entry 3), one session.
- AC-4.1 is a text check: `agents/designer.md` "Scale & space use" bullet; format untouched.
- NFR-1: `claude plugin validate .` could not run (`claude` CLI not installed here); no JSON or manifest changed. Template markers untouched (`git diff` shows no change to the marker line or protected columns).

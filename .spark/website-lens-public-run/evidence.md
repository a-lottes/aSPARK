# Evidence: website-lens-public-run

| | |
|---|---|
| Feature | website-lens-public-run |
| Phase | Review / QA (evidence for `review.md` and `qa.md`) |
| Date | 2026-10-27 |
| Ticket | #96 |

## 1. Target (AC-1.1)

| | |
|---|---|
| Repo | `https://github.com/StartBootstrap/startbootstrap-agency` (MIT, `LICENSE`), Agency theme v7.0.12 |
| Pinned commit | `b2d5d5c6b1396bc5b0e8dd92c693b106cfb7cee1` (2023-03-24) |
| Reviewed files | `dist/index.html` (610 lines), `dist/js/scripts.js` (54 lines), as a whole-file diff against the empty tree: `git diff $(git hash-object -t tree /dev/null) b2d5d5c -- dist/index.html dist/js/scripts.js` (`4b825dc642cb6eb9a060e54bf8d69288fbee4904`). `src/` not reviewed. No real increment existed, so there is no PR diff |
| Re-run: clone | `git clone https://github.com/StartBootstrap/startbootstrap-agency && cd startbootstrap-agency && git checkout b2d5d5c` |
| Re-run: constitution | copy `.spark/website-lens-public-run/target-constitution.md` to `.spark/constitution.md` in the clone (untracked) |
| Re-run: serve | `cd dist && python3 -m http.server 8766`, open `http://127.0.0.1:8766/`. The run used a scratch copy `/tmp/site` where the one line `index.html:601` (jsDelivr Bootstrap 5.2.3 bundle) pointed at `bootstrap@5.2.3`'s `bootstrap.bundle.min.js` from `npm pack bootstrap@5.2.3` instead. **That swap turned out to be unnecessary** (§6 R1): the unmodified page loads its CDN assets in this container's browser. Serving `dist/` unmodified is expected to give the same page, but it was **not** re-run that way |
| Browser | Playwright MCP headless Chromium; desktop 1280x800 and mobile 390x844 |
| Run date / model | 2026-10-27; `claude-sonnet-5-5` for the orchestrator, the `reviewer` and the `qa-tester` |
| Plugin build | installed `/opt/aspark` (has no `standards/` directory; `standards/anti-generosity.md` was read from this repo) |

Citations re-resolved at the pinned commit by the author with `git show b2d5d5c:<path> | sed -n '<n>p'`: `index.html:23,97` (`alt="..."`), `:327` (placeholder-only input), `:354,366` (message divs, no live region), `:368` (submit disabled by class), `:391,394` (`role="dialog"` without name; `div.close-modal`), `:601,608` (CDN scripts), `scripts.js:46-50` (toggler click on nav-link click).

## 2. How lens activation went (AC-2.1) and what is weaker than it sounds

1. `target-constitution.md` §2 declares type `website` and characteristic `must-be-accessible`. `lenses/accessibility.md` frontmatter says `triggers: [must-be-accessible]`, `phases: [specify, design, act, review, qa]`. I resolved the active lens from that, read its `phases`, and passed `/opt/aspark/lenses/accessibility.md` to the `reviewer` (phases includes `review`) and to the `qa-tester` (includes `qa`). No lens was chosen by hand in a prompt.
2. **The dispatcher was the line orchestrator following the skills' steps, not a `/peer-review` or `/demo-day` slash command invoked by a person.** The constitution was also written by that same orchestrator (dark mode, no Facilitator, no maintainer confirmation). The profile is an **assumption** (`must-be-accessible` is not declared upstream). What this shows is that the activation text is followable and the lens reached the agents by its `phases` field. It does not show a `/charter` run, nor an independent author of the profile.
3. `type: website` would also have activated `seo` and `ux`. They were left **off in the constitution on purpose** (reason in `target-constitution.md`) to keep the run to one lens. That is an override of the default derivation, recorded, not silent.
4. The Specify half was not exercised by a `product-owner` session: the spec's NFR-1/NFR-2 (flows named, numeric contrast target) were written by the orchestrator in the shape lens §1 asks for.

## 3. Did the lens fire unprompted in Review? (AC-3.1; n=1, no rate)

The reviewer's prompt contained no per-item trace request, no checklist table and no lens item names. It did contain the spec and plan (which name the accessibility lens and talk about a lens-firing record), so the reviewer knew a count would be made; it separated "lens §4" rows from "baseline" rows on its own for that reason. That is a prompting effect, not a clean "unprompted" condition.

Lens Review items (`lenses/accessibility.md` §4, 3 items):

| Item | Surfaced in `review.md` without a request? | Where | Live-confirmed in QA? |
|---|---|---|---|
| 4.1 No keyboard trap | Yes (static PASS) | §4 traceability; F4 | Yes, PASS (qa.md NFR-1(a)); B10 adds a one-Tab focus touch on the navbar behind the modal |
| 4.2 Focus on modal open/close and route change | Yes (modal PASS, mobile-nav FAIL) | §4; F5 | Yes: modal PASS; F5 confirmed as B5, weaker than predicted (desktop link navigation also ends on `BODY`) |
| 4.3 Do not re-check ARIA correctness here | Respected: ARIA and label findings were tagged "baseline" | §1 | n/a |

**Observed: 3 of 3 Review items surfaced, one session, one model.** Separately the reviewer produced six baseline (non-§4) accessibility findings (F1, F2, F3, F6, F7, F9; three of them Major). That the reviewer went beyond the lens's narrow Review remit is also an observation: the lens text says a wrong ARIA pattern "ships unless QA's keyboard walkthrough surfaces it", and the reviewer flagged them anyway. This is one observation. It is **not a rate**, and a second session could differ.

## 4. Lens-derived live checks (AC-4.1)

All from `qa.md`, performed in the browser. Prompting caveat: my QA prompt named the three lens §5 items (keyboard-only, measured contrast, live-region confirmation), so QA firing is **prompted**, not unprompted.

| Check | Verdict | Observable |
|---|---|---|
| §5.1 Keyboard-only: portfolio modal (NFR-1a) | PASS | opens by `Enter`, closes by Close Project and `Escape`, `activeElement` back on trigger; desktop and mobile |
| §5.1 Keyboard-only: navbar incl. toggler (NFR-1b) | PASS | toggler `aria-expanded` false → true, `Enter` on Portfolio navigates and collapses |
| §5.1 Keyboard-only: contact form (NFR-1c) | PASS | four fields filled, submit by `Enter`, success message shown |
| §5.2 Measured contrast (NFR-1) | FAIL | `.text-muted` on `#f8f9fa` 4.45; white on yellow button 1.55; placeholder 1.49; borderline header-image pair: median 13.74, worst pixel 3.53 |
| §5.3 Live-region announcements (NFR-2) | FAIL | 0 `[aria-live],[role=status],[role=alert]` before and after submit; no `aria-invalid`, no `aria-describedby`; no screen reader was run, so the verdict rests on DOM semantics |
| AC-1.1…AC-6.1, NFR-3, NFR-4 | `⚠ not-verified-live` | not browser-observable; verified here and in git |

Review predictions vs. live: F2, F3, F4, F6, F7, F9 confirmed; F1 partly refuted (the accessible name is the placeholder, which has 1.49:1 contrast); F5 confirmed with a smaller impact; F8 is source-only (`⚠ not-verified-live`). QA added B9 (focus to `BODY` after submit), B10, B11 (tap targets below 44 px).

## 5. What is not shown (AC-5.1)

- **One run, one model, one session per role.** n = 1. No rate, no comparison with a lens-free control run (a plain review might have found the same defects).
- **Prompt-enforced only.** Nothing in this repo checks that the lens fired. The dispatch was an orchestrator following Markdown, and the agents followed Markdown.
- **The activation chain is partly exercised, not independently:** same agent wrote the constitution and dispatched from it; no `/charter`, no Facilitator, no maintainer confirmation; `seo` and `ux` overridden off.
- **Not run:** Specify with a `product-owner` session, Design (`/look-and-feel`), Act (the target is not changed).
- **Not assistive-tech tested:** no screen reader, no zoom/reflow, no `prefers-reduced-motion` check, no touch device. Keyboard behaviour is Chromium only.
- **The reviewed unit is a whole-file diff of a snapshot, not a real change.** The findings are about the theme as shipped in 2023, not about any upstream PR.
- **A running page on localhost, not the live public site** (`startbootstrap.github.io`), and the page's third-party scripts were whatever the CDN served on 2026-10-27 (`sb-forms-latest.js` redirected to `sb-forms-0.4.1.js`).
- Nothing in the target was fixed or re-tested after a fix.

## 6. Failures and misfires (refuted-with-finding)

- **R1 — spec A2 / review F13 were wrong about the environment.** Both said the container browser could not load Google Fonts, Font Awesome or `sb-forms-latest.js`, based on the task brief ("no network beyond this container"). QA's network log shows all of them returning 200 (`sb-forms-latest.js` 302 → `sb-forms-0.4.1.js` 200; `qa.md` B12, §4). The Bootstrap-bundle swap in §1 was therefore probably unneeded, and review F12 (the :8765 server serving the unswapped page, assumed to have a dead Bootstrap) rested on the same unverified premise; neither the bare page nor the swap was compared in the browser. The review's NFR-2 call ("static FAIL; only flips if sb-forms injects ARIA at runtime", Q1) was settled live: it does not inject any (0 live regions). A premise recorded as fact at Plan and trusted forward through review was not re-derived until QA. Spec A2 carries an update line.
- **R2 — review F1 over-stated.** "Name disappears on input" is true for the visible label, but the accessible name is the placeholder, so a screen reader is not nameless (`qa.md` B2).
- **R3 — F5 over-stated impact.** Focus-to-`BODY` also happens on desktop link navigation by default (`qa.md` B5).
- **R4 — Review verdicts were static ("degraded"), as the reviewer said.** Two of its target findings (F1, F5) changed in strength once run in the browser (R2, R3); NFR-2's static FAIL was confirmed live.
- **R5 — I gave the QA agent the lens §5 items in its prompt.** QA firing of the lens is prompted (§4).
- **R6 — first review round caught two defects of mine in the run** (wrong empty-tree hash in my prompt, F10; no recorded serve URL, F12). Fixed in `plan.md`; a stranger copying the first draft would have failed.

## 7. What this does and does not show

It shows: the `accessibility` lens, reached through a constitution's declared characteristic and the lens's own `phases` field, produced on-topic, citable, mostly correct findings in Review and was then QA-verified item by item in a real browser with measured numbers (three flows pass by keyboard; contrast and live announcements fail), on a public MIT website at a pinned commit. It does not show the lens firing at a rate, beating a plain review, or surviving an independent profile author. The `website` half of the lens proof is now **partially** closed: lens content and dispatch by `phases` exercised and QA-verified live; the profile was assumed by the orchestrator and no lens-free control exists.

## 8. Scratch and fences

Scratch: `/tmp/target/startbootstrap-agency` (clone plus `.spark/constitution.md`), `/tmp/site`, `/tmp/vendor`, `/tmp/fix.py`. Nothing there is committed; no script is committed. The target was not modified. `lenses/`, `skills/`, `agents/` unchanged (AC-6.1).

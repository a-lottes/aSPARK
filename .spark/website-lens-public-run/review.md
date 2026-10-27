# Review Report: website-lens-public-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Review |
| **Owner** | Reviewer (`/peer-review`) |
| **Input** | Whole-file diff of `dist/index.html` + `dist/js/scripts.js` against the empty tree, StartBootstrap/startbootstrap-agency @ `b2d5d5c6b1396bc5b0e8dd92c693b106cfb7cee1`; `.spark/website-lens-public-run/plan.md` |
| **Status** | `passed` |
| **Round** | 2 |
| **Date** | 2026-10-27 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** Run-side gate holds in round 2. F10–F13 are confirmed fixed, re-derived from `plan.md` §1, spec A2 and live port probes. `/demo-day` may start against `http://127.0.0.1:8766/`. The target findings F1–F9 are this run's output, not defects in the run.
- **Open:** `9 open`, all target-side and open on purpose (fixing the target is out of scope, spec §6): Majors `F1, F2, F3`; Minors/Nits `F4–F9`. Run-side: none.
- **Binding ruling:** §6 Verdict and the gate checklist below. The gate is judged on the run's own conformance to spec/plan, per the caller's ruling (round 1 and the round-2 coordinator message). Target findings are recorded as open and never gate this run. `passed` therefore does **not** mean the target is accessible: the target fails NFR-2 (static) and has three open Majors.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

- **Reviewed:** `dist/index.html` (610 lines) and `dist/js/scripts.js` (54 lines) at the pinned commit, read with `git show b2d5d5c:<path>`. Diff base: the real empty tree `4b825dc642cb6eb9a060e54bf8d69288fbee4904` (the caller's hash fails, see F10).
- **Read for context:** the behaviour of the vendored Bootstrap 5.2.3 bundle that the page depends on (`/tmp/vendor/bs/package/dist/js/bootstrap.bundle.js`, from `bootstrap-5.2.3.tgz` sha256 `60afd857…41a9d`). I also checked the served scratch copy `/tmp/site` against upstream `dist/`, and probed the localhost servers.
- **Round 2 re-verification** (condition (a): verifying fixes to F10–F13). Re-derived from source, not from the coordinator's summary:
  - `git diff` of `plan.md` and `spec.md`.
  - Live probes: `:8765` → `ECONNREFUSED` ×3; `:8766/` → 200, 39622 bytes; `:8766/js/bootstrap.bundle.min.js` → 200.
  - A TCP scan of 1024–65535 found 8766 plus four non-HTTP ports. An earlier HTTP-only scan with 300 ms timeouts returned "none", which was an artifact of the single-threaded server under load.
  - Replaying the recorded `sed` on `git show b2d5d5c:dist/index.html` gives a file `cmp`-identical to `/tmp/site/index.html`.
  - The pinned `dist/` has no local edits (`git diff --quiet b2d5d5c -- dist`).
  - The target rows F1–F9 were not re-examined: the pin and its files are unchanged, so those rows are left as written.
- **Not reviewed:** `src/` (out of scope per the caller). `css/styles.css` contrast is QA's measured check and is not judgeable from source. `sb-forms-latest.js` is CDN-only and not in the diff (Q1).
- **Evaluation mode (anti-generosity §5):** static read plus HTTP probes only. I drove no browser. Every keyboard and focus verdict below is degraded (static) and needs QA's live pass.
- **Lens applied:** `/opt/aspark/lenses/accessibility.md` §4 (Review: keyboard traps and focus). Its content is identical to `lenses/accessibility.md` in this repo (`diff` clean). Rows marked *baseline* come from the reviewer's own hunt (correctness against NFR-1/NFR-2) and fall outside the lens's Review remit (§4 item 3). Kept separate so `evidence.md` can count the lens firing (AC-3.1) without baseline noise.

## 2. Plan Conformance

| Task | Implemented as planned? | Note |
|---|---|---|
| T1 | ✅ r2 | Pinned commit matches (`git rev-parse HEAD`). The constitution is in place and byte-identical to `target-constitution.md`. `/tmp/site` differs from `dist/` only at `index.html:601` (CDN → `js/bootstrap.bundle.min.js`, `cmp`-identical to the npm 5.2.3 file), as planned. The DoD is now met: `plan.md` §1 "Serve steps" records the command, the edit and the QA URL `:8766` (replayed `cmp`-identical), and spec A2 lists every missing CDN asset. No deviation remains. |
| T2 | ✅ | This report, written by the `reviewer` agent. The lens path was passed with the dispatch rationale (frontmatter `phases` includes `review`), and the prompt contained no per-item trace request (AC-3.1). The standard was passed, at a path that does not exist (F11). |
| T3–T5 | n/a | Not yet due; downstream of this gate by plan. |

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Major | `dist/index.html:327,332,338,345` | *Baseline (lens §3 Act item).* The four contact inputs have only `placeholder`: no `<label>`, `aria-label` or `aria-labelledby` (no `<label` in the file). The name disappears on input, and this fails WCAG 1.3.1/3.3.2 under the declared AA floor for NFR-1(c). Fix: a visible or visually hidden `<label for>` per control. | open |
| F2 | Major | `dist/index.html:354,366`; `:328,333,334,339,346` | *Baseline (lens §3 Act item), NFR-2.* The submit result (`#submitSuccessMessage`, `#submitErrorMessage`) and validation messages are shown by toggling `d-none` or `invalid-feedback`. None has `aria-live`/`role="status"`/`role="alert"` (zero matches in the file), and no `aria-describedby` links a message to its input. A sighted-only state change. Fix: `role="status"` on success, `role="alert"` on error, and `aria-describedby` plus `aria-invalid` on the inputs. Static FAIL; only flips if sb-forms injects ARIA at runtime (Q1). | open |
| F3 | Major | `dist/index.html:93,108,123,138,153,168` (img `:97,112,127,142,157,172`); `:23` | *Baseline.* All six portfolio modal triggers and the brand link have one child, an `<img alt="...">`. Their accessible name is "...", so a screen-reader user cannot tell which project a link opens (WCAG 2.4.4/1.1.1, NFR-1(a)). 24 `alt="..."` in the file. Fix: alt text naming the project ("Threads", etc.) or `aria-label` on the link. | open |
| F4 | Minor | `dist/index.html:394,429,464,499,534,569` | *Lens §4 (exit path).* The top-right close control is a `<div class="close-modal" data-bs-dismiss>` with no `tabindex` or role, so it is unreachable by keyboard. Not a trap: Esc (bundle `:4818-4826`, `keyboard: true` `:4659`) and the "Close Project" `<button>` (`:414,449,484,519,554,589`) still exit. Fix: make it a `<button type="button" aria-label="Close">`. | open |
| F5 | Minor | `dist/js/scripts.js:46-50` | *Lens §4 (focus on change).* At ≤ 991 px, activating a nav link calls `navbarToggler.click()`, which collapses `#navbarResponsive` while focus is on that link. Bootstrap 5.2.3 `Collapse` (bundle `:1722` ff.) has no focus handling, so the focused element becomes `display:none` and focus falls to `<body>`. Static read; QA confirms `document.activeElement` live. Fix: after collapse, focus the target section (`tabindex="-1"`) or the toggler. | open |
| F6 | Minor | `dist/index.html:391,426,461,496,531,566` | *Baseline (Act ARIA).* `role="dialog"` with no `aria-labelledby`. Bootstrap adds `aria-modal` at runtime (bundle `:4788`) but no name, so the dialog is announced unnamed. Fix: an `id` on each modal's `<h2>` and `aria-labelledby` on the dialog. | open |
| F7 | Minor | `dist/index.html:368` | *Baseline.* The submit button is "disabled" by class only. `.btn.disabled` blocks pointer events, but the button stays focusable and keyboard-activatable, with no `aria-disabled`. Keyboard and AT users get a different state than mouse users. Fix: `aria-disabled="true"` in sync with the class, or the real `disabled` attribute. | open |
| F8 | Nit | `dist/js/scripts.js:42,48` | `navbarToggler` is not null-checked, unlike `#mainNav` (`:15`, `:34`). `getComputedStyle(null)` throws on a page without a toggler. Latent only; this page has one (`index.html:24`). Fix: `if (!navbarToggler) return;` before `:43`. | open |
| F9 | Minor | `dist/index.html:19-388` | *Baseline.* There is no `<main>` landmark and no skip link: the content sections sit directly in `<body>` (no `<main` in the file). This weakens WCAG 2.4.1 bypass for keyboard and AT users. Fix: wrap `:40-371` in `<main>`. | open |
| F10 | Minor | run: caller prompt | The empty-tree hash given for the diff (`4b825dc642cb6eb9a060e54bf8d69288fbdb2b1c`) is wrong: `git` answers `fatal: bad object`. The real one is `…fbee4904` (`git hash-object -t tree /dev/null`). A stranger copying the command fails (NFR-3, AC-1.1). Fix: use the correct hash, or `$(git hash-object -t tree /dev/null)`, in `evidence.md`. | fixed r2 |
| F11 | Minor | run: dispatch | The passed standard path `/opt/aspark/standards/anti-generosity.md` does not exist (no `standards/` in `/opt/aspark`). I read `/workspace/repo/standards/anti-generosity.md`. `/opt/aspark/templates/review-report.md` also lacks this repo's `aspark-template` marker, so the run used a plugin build different from the repo. Fix: `evidence.md` names the plugin build and the standard path actually read. | fixed r2 |
| F12 | Major | run: T1 serve | `127.0.0.1:8765` serves the upstream page byte-for-byte (`cmp` equal to `dist/index.html`). It loads Bootstrap from the CDN, `/js/bootstrap.bundle.min.js` returns 404, so `bootstrap` is undefined at `scripts.js:35` and the modals, collapse and scrollspy are dead. `:8766` serves `/tmp/site` correctly (bundle 200). No artifact names which one to use, so a QA run on `:8765` would record false FAILs for NFR-1. Fix: record `http://127.0.0.1:8766/` (served from `/tmp/site`) as the URL in the trail before `/demo-day`, and stop `:8765`. | fixed r2 |
| F13 | Minor | run: spec A2; `dist/index.html:608` | `sb-forms-latest.js` is CDN-only and cannot load. A2 lists only fonts and Font Awesome as missing. Nothing in the diff toggles the form's feedback or submit messages, so NFR-2 and part of NFR-1(c) cannot occur live. Fix: add it to the deviation list. QA marks the dependent checks `⚠ not-verified-live` instead of FAIL. | fixed r2 |

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `evidence.md` (T4, not yet written) | ⚠ not-verified-live: downstream of this gate. Inputs needed: F10, F11, F12, F13. |
| AC-2.1 (Review half) | constitution §2 `must-be-accessible` → `lenses/accessibility.md` `triggers`/`phases` includes `review` | ✅ PASS. I received exactly that one path, with the dispatch rationale. |
| AC-2.1 (QA half) | `/demo-day` dispatch (T3) | ⚠ not-verified-live: not yet run. |
| AC-3.1 (prompt half) | this reviewer's prompt | ✅ PASS. No per-item trace request appears in it. |
| AC-3.1 (evidence half) | `evidence.md` (T4) | ⚠ not-verified-live. Observable for T4: the lens §4 items in this report are F4, F5 and the two rows below. |
| AC-4.1, AC-5.1, AC-6.1 | `qa.md`, `evidence.md`, docs (T3–T5) | ⚠ not-verified-live: not yet due. AC-6.1 so far: my only write is this file. |
| Lens §4.1: no keyboard trap | Bootstrap modal (not custom); Esc bundle `:4818-4826`; "Close Project" `<button>` `:414` etc. | ✅ PASS (static read, degraded). |
| Lens §4.2: focus on modal open/close | focus trap `:4805`/`:4573`; return to the `<a href>` trigger `:4975-4979` | ✅ PASS (static, degraded). Mobile-nav focus: ❌ FAIL (F5). |
| NFR-1 | keyboard paths above; F1, F3, F4, F7 | ⚠ not-verified-live: keyboard completion and contrast are QA observables. Static read found no blocker to keyboard-only completion. |
| NFR-2 | `index.html:354,366,328-346` | ❌ FAIL (static, degraded): no live region in the diff (F2). |
| NFR-3 | every `file:line` in this report | ✅ PASS: each one was read via `git show b2d5d5c:<path>` at the pinned commit. |
| NFR-4 | `git status` of `/workspace/repo` | ✅ PASS for this phase: only `review.md` written; the target is untouched (`?? .spark/` only). |

## 5. What Was Checked

- [x] Correctness: lens §4 items and NFR-1/NFR-2 against the diff, plus the vendored-bundle behaviour the page relies on
- [x] Non-functional: NFR-1–4 and the constitution's WCAG 2.1 AA floor (static; contrast left to QA)
- [x] Error handling: `scripts.js` guards (F8); the form error path depends on sb-forms (Q1)
- [x] Security: static page; no secrets. `data-sb-form-api-token="API_TOKEN"` (`:322`) is a placeholder
- [x] Tests: none exist. The target has no test script (`package.json` scripts: build/start only), and the run commits no code (AC-6.1)
- [x] Readability: two short files; one Nit (F8)

**Open question Q1:** does `sb-forms-latest.js` inject `aria-live`/`aria-invalid` at runtime? It is not in the diff and cannot load offline. F2 stands on the diff as written.

## 6. Verdict

The run's own Review step conforms. The lens path arrived through the dispatch rule (frontmatter `phases`), with no per-item trace request in the prompt, and its §4 remit produced concrete results. Static verdicts: PASS for no keyboard trap in the modals; PASS for modal focus return through Bootstrap's data-API; FAIL for focus on mobile-nav collapse (F5); F4 as an exit-path Minor. The baseline hunt found three target Majors: unlabelled form controls (F1), no live region for the form's feedback (F2, NFR-2 FAIL), and modal triggers named "..." (F3). These are this run's output and stay open; fixing the target is out of scope. Round 2 confirms every run-side fix from primary sources:
- **F12:** `:8765` refuses connections and `:8766` is the only HTTP server, serving `/tmp/site` with the local bundle. Replaying `plan.md` §1's serve steps reproduces `/tmp/site/index.html` byte-for-byte.
- **F13:** spec A2 now names `sb-forms-latest.js` (`dist/index.html:608`), Google Fonts and Font Awesome as missing.
- **F10:** the recorded hash equals `git hash-object -t tree /dev/null`.
- **F11:** `plan.md` §1 names the plugin build and the standard path actually read.

The run-side gate therefore holds, and `/demo-day` may start at `http://127.0.0.1:8766/`. QA must mark the form-dependent NFR-2 and NFR-1(c) checks `⚠ not-verified-live`, per A2. `evidence.md` (T4) still has to carry F10 and F11 forward from `plan.md`. `passed` here certifies the run's conformance, not the target's accessibility. Applied: `anti-generosity` (read from `/workspace/repo/standards/anti-generosity.md`; see F11).

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`. On
re-review, edit this same checklist in place — never duplicate it as a second gate.*

- [x] No open Blocker findings
- [x] No open Major findings, run-side: F12 is `fixed r2` (`:8765` refused, `:8766` serves `/tmp/site`). Target Majors F1–F3 stay open by design (spec §6, caller's ruling) and do not gate the run. They are not waived and not fixed.
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated. Scoped to what is due at Review (AC-2.1 Review half, AC-3.1 prompt half); the rest are downstream by plan (§4).
- [x] All plan deviations documented and accepted: T1's DoD is now met (`plan.md` §1 Serve steps; spec A2 lists every missing CDN asset as `Accepted`), so no deviation remains open.
- [x] Test suite runs green: n/a. No suite exists in the target, and the run commits no code (AC-6.1).
- [x] Line budget respected: Ist 112 / Soll ~150 (excluding HTML comments)
- [x] Status set to `passed`

# Plan: website-lens-public-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`), drafted by the line orchestrator in dark mode |
| **Input** | `.spark/website-lens-public-run/spec.md` (`approved`) |
| **Status** | `approved` |
| **Date** | 2026-10-27 |

**Handoff**
- **Status:** `approved` (dark mode, recommended gate).
- **Summary:** Pin Start Bootstrap Agency, declare its profile in a constitution, run `reviewer` (no trace request) then `qa-tester` in the Playwright browser, write evidence, update docs.
- **Open:** `none`
- **Binding ruling:** §3 Task Breakdown.
- **On conflict:** body wins except `Status`.

## 1. Architecture Decision

- **Context:** Core is Markdown only; the lens can only be tested by running the ceremonies. The chosen target must be static so the container browser can serve it locally.
- **Decision:** Clone `StartBootstrap/startbootstrap-agency` (MIT) at `b2d5d5c` into untracked scratch; place a constitution in the clone; resolve lenses by the dispatch rule (read each active lens's `phases`); give the reviewer the whole-file diff of `dist/index.html` + `dist/js/scripts.js` against the empty tree; serve a scratch copy of `dist/` with the one CDN script swapped for the same-version local file; QA drives it in headless Chromium.
- **Alternatives considered:**

| Alternative | Why rejected |
|---|---|
| Hand-pick the lens in the prompt | That was the api run's gap (AC-2). |
| Ask the reviewer for a per-item table | AC-3 forbids it; it would measure prompting. |
| A live public URL | The browser has no network beyond localhost. |
| A SPA / larger site | Needs a build and network installs; a static page keeps the run reproducible. |

- **Consequences:** Fonts and Font Awesome do not load; the real site's look is not verified. One run, one model.

**Serve steps (T1, recorded after review F12):** `cp -r dist /tmp/site`; copy `bootstrap.bundle.min.js` from `npm pack bootstrap@5.2.3` into `/tmp/site/js/`; `sed -i 's#https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js#js/bootstrap.bundle.min.js#' /tmp/site/index.html` (the only edit, line 601); `cd /tmp/site && python3 -m http.server 8766`. QA URL: `http://127.0.0.1:8766/`. An earlier unpatched server on :8765 was stopped. Empty-tree hash for diffs: `$(git hash-object -t tree /dev/null)` = `4b825dc642cb6eb9a060e54bf8d69288fbee4904`. Plugin build used: the installed `/opt/aspark` (it has no `standards/` directory; the standard was read from this repo's `standards/anti-generosity.md`).

## 2. Affected Components

`.spark/website-lens-public-run/*`, `README.md`, `ROADMAP.md`, `docs/status.md`. Scratch: `/tmp/target/startbootstrap-agency`, `/tmp/site`, `/tmp/vendor`.

## 3. Task Breakdown

| # | Task | Story | Status | Definition of Done | Covers (AC / NFR) | Depends on |
|---|---|---|---|---|---|---|
| T1 | Pin target, write constitution, serve site | US-1, US-2 | done | commit, serve steps, deviations recorded; page responds on localhost | AC-1.1, AC-2.1 | none |
| T2 | `/peer-review` with dispatch-resolved lens, no trace request | US-2, US-3 | done | `review.md` written by the `reviewer` agent | AC-2.1, AC-3.1, NFR-3 | T1 |
| T3 | `/demo-day` in the browser | US-4 | done | `qa.md` written by the `qa-tester` agent; every lens item binary | AC-4.1, NFR-1, NFR-2 | T2 |
| T4 | Compile `evidence.md` | US-1, US-3, US-5 | done | citations re-resolved; not-shown list | AC-1.1, AC-3.1, AC-5.1, NFR-3 | T3 |
| T5 | Update ROADMAP, docs/status, README | US-5 | todo | wording matches evidence | AC-5.1, AC-6.1, NFR-4 | T4 |

## 4. Test Strategy

Re-resolve every citation with `git show b2d5d5c:<path> | sed -n`; browser observables for QA; `git diff --stat` for the fence.

## 5. Risks

- The reviewer may not apply the lens unprompted (a result, recorded).
- Missing fonts/icons change contrast measurements (disclosed).

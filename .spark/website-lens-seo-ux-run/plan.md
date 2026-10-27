# Plan: website-lens-seo-ux-run

<!-- aspark-template: aspark/0.1.0 -->

| | |
|---|---|
| **Phase** | Plan |
| **Owner** | Engineering Manager (`/sprint-plan`) |
| **Input** | `.spark/website-lens-seo-ux-run/spec.md` (`approved`) |
| **Status** | `approved` |
| **Date** | 2026-10-27 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). `approved` by the dark-mode line's recommended gate (no person was available): Q1 accepted (run tasks map to issue #105's AC-1..AC-7), Q2 accepted (AC-7 recorded as not run, the CLI does not exist in this container; run `claude plugin validate .` wherever the CLI exists before any release).
- **Summary:** Plan written after the work. The run reused the skills as they are on a scratch clone of `11ty/eleventy-base-blog` at `cf0cc1f`, served a static production build and dispatched lenses by their `phases` frontmatter. The deliverable is the `.spark/` trail plus three doc updates.
- **Open:** `1 task not done`: T8 (`claude plugin validate .` not run, no CLI in the container). See §3.
- **Binding ruling:** §3 Task Breakdown for current task status; a plan revision after review/QA findings updates §1/§3 in place, never a new section
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

**Plan-after-the-fact (disclosed).** The work was executed before this plan existed: the run commit is `fdeeab0`. So this plan does not steer anything. It is the ordered record of what was done, and it is honest only where an artifact proves a row. A task is `done` only where its named artifact exists and says what the DoD says. Nothing here was used as a gate before the work. The review ran without a plan (`review.md` §2: "There is no plan.md").

## 1. Architecture Decision

- **Context:** aSPARK Core is Markdown + JSON only, with no new tracked executable code (`constitution.md §3`). Its quality bar is `claude plugin validate` plus a documented dogfood run (`constitution.md §9` Test practice, §4). Lens behaviour therefore cannot be unit-tested. It can only be shown by running the ceremonies on a real `website` target and recording what fired. This is the second public `website` run. The first (`.spark/website-lens-public-run/`) exercised `accessibility` only, and this one exercises `seo`, `ux` and `security` through charter activation. The run may not change the target (spec A1, §6). The spec's ACs need a **production** build (spec A2, C2). The container browser reaches localhost only.
- **Decision:** Use the installed skills and agents unchanged on a scratch clone at `/tmp/scratch/eleventy-base-blog` pinned to `cf0cc1f`. `/charter` writes the target's constitution into the clone's untracked `.spark/`. Each later phase receives the **paths** of the active lenses whose `phases` frontmatter names that phase, with no item lists and no trace request. QA runs in Playwright Chromium against `npm run build` output, served statically with `python3 -m http.server 8081` from `_site/`. No new file is added to the plugin, and the only tracked changes are this trail and three docs.
- **Alternatives considered:**
  | Alternative | Why rejected |
  |---|---|
  | Serve with the dev server `npm start` (`eleventy --serve`) | It is a dev-mode build: it includes the draft `fifthpost` and emits `/.11ty/image/` URLs. AC-2.7, AC-4.5 and AC-5.7 would fail for the wrong reason (spec A2, C2). It was started once only to prove upstream's documented start works (evidence.md §1). |
  | Hand-pass lens text or item checklists in the agent prompts | That measures prompting rather than the dispatch rule. It was the gap in the earlier api run, and the first website run also rejected it. Paths only, resolved from `phases`. |
  | QA against the live public demo URL | The container has no network beyond localhost. A public deploy also would not be pinned to `cf0cc1f` and would mix in host headers (spec A6, review F10/F15). |
  | Add a reusable harness script to the repo for serving and checks | Forbidden: no new tracked executable code (`constitution.md §3`). Scratch commands only, recorded in evidence.md §1. |
- **Consequences:** Easier: the run is reproducible from evidence.md §1 (pin, build, serve). The fence can be checked with one `git diff`, and nothing ships to consumers. Harder: production-only static serving means unknown-URL routing and response headers come from the Python harness, not a host, so AC-1.7 and NFR-5c are `not-verified-live`. Design (`/look-and-feel`) is not run, so the `design` phase of `seo` and `ux` is unexercised. The result is n = 1 with no rate and no lens-free control (evidence.md §6).

## 2. Affected Components

- **Tracked (this repo):** `.spark/website-lens-seo-ux-run/` (`spec.md`, `target-constitution.md`, `review.md`, `qa.md`, `evidence.md`, this `plan.md`), `ROADMAP.md:20`, `README.md:151`, `docs/status.md:209`. No `skills/`, `agents/`, `lenses/` or `templates/` file changes. The module map comes from `constitution.md §9` (Module structure), which was not re-derived because none of those directories is touched.
- **Scratch (untracked, not shipped):** `/tmp/scratch/eleventy-base-blog` (branch `main` at `cf0cc1f1b5972d9d7d06b9a0f0488e61839f3207`, checked from `.git/refs/heads/main` at plan time), its untracked `.spark/constitution.md`, `_site/` and `node_modules/`.
- **New dependencies:** none in this repo. In scratch, `npm ci` installs the target's own locked dependencies. Playwright MCP and Python's `http.server` belong to the container and are not added anywhere.
- **Blast-radius query:** no tool file was passed, so none was requested and the scope above was set by hand.

## 3. Task Breakdown

**Traceability note:** `spec.md` is the *target's* retrospective spec (US-1..US-5, written by T3). The run's own acceptance criteria are those of issue #105, cited as `#105/AC-n` (AC-1 target and repeat, AC-2 lens activation, AC-3 browser verification, AC-4 refuted/misfires, AC-5 fences, AC-6 tracked changes and docs, AC-7 validate). Those are the headings evidence.md uses. They are **not** in `spec.md`, so the five tasks that serve only them carry `#105` in the Story column (see question Q1 in §5).

| # | Task | Story | Covers (AC / NFR) | Depends on | Status | Definition of Done |
|---|---|---|---|---|---|---|
| T1 | Pin target, build for production, serve statically | #105 | #105/AC-1, #105/AC-5 | – | `done` | evidence.md §1 records the repo, pinned commit `cf0cc1f`, Node v22, `npm ci && npm run build` output (15 files), the serve command on :8081 and the `npm start` deviation, and the scratch `main` ref equals `cf0cc1f` (no tracked file) |
| T2 | `/charter` on the scratch clone | #105 | #105/AC-2 | T1 | `done` | `target-constitution.md` exists, copied unchanged from the clone's `.spark/constitution.md`, and declares type `website`, `is-public`, `seo`/`ux`/`security` active and the six other lenses off with reasons — files: .spark/website-lens-seo-ux-run/target-constitution.md |
| T3 | Specify (`/story-time`) with lenses dispatched by `phases` (all three lenses name `specify`) | US-1, US-2, US-3, US-4, US-5 | all spec ACs and NFR-1..NFR-7 (enumerated at T5) | T2 | `done` | `spec.md` exists with Status `approved` (dark-mode recommended gate), stories US-1..US-5 in the protected heading form, and NFRs tagged `seo`/`ux`/`security` — files: .spark/website-lens-seo-ux-run/spec.md |
| T4 | `/peer-review` with `seo` + `security` only (`ux` has no `review` phase) | US-1, US-2, US-3, US-4, US-5 | #105/AC-2, AC-1.5, AC-1.7, AC-4.4, AC-5.3, AC-5.4, AC-5.5, AC-5.6, AC-5.7, AC-5.8, NFR-5 | T3 | `done` | `review.md` has Status `passed` (run-conformance gate, caller ruling), Lenses applied names `seo` and `security` only, every spec AC has a traceability row, and F1-F17 are recorded — files: .spark/website-lens-seo-ux-run/review.md |
| T5 | `/demo-day` in Playwright Chromium on the production build (:8081), 1280 and 375 px, all three lenses | US-1, US-2, US-3, US-4, US-5 | #105/AC-3, AC-1.1, AC-1.2, AC-1.3, AC-1.4, AC-1.5, AC-1.6, AC-1.7, AC-2.1, AC-2.2, AC-2.3, AC-2.4, AC-2.5, AC-2.6, AC-2.7, AC-3.1, AC-3.2, AC-3.3, AC-3.4, AC-3.5, AC-4.1, AC-4.2, AC-4.3, AC-4.4, AC-4.5, AC-5.1, AC-5.2, AC-5.3, AC-5.4, AC-5.5, AC-5.6, AC-5.7, AC-5.8, NFR-1, NFR-2, NFR-3, NFR-4, NFR-5, NFR-6, NFR-7 | T4 | `done` | `qa.md` has a `Spec ID` row with a `Result` for every AC and NFR. Status is `passed` by an orchestrator ruling recorded in its Handoff, and the tester's `failed` verdict and gate boxes are left unedited — files: .spark/website-lens-seo-ux-run/qa.md |
| T6 | Compile `evidence.md` | #105 | #105/AC-1, #105/AC-2, #105/AC-3, #105/AC-4, #105/AC-5, #105/AC-6 | T5 | `done` | evidence.md has §1 repeat steps and citations re-resolved with `git show cf0cc1f:<path>`, §2 the activation, §3 the per-phase lens-firing table, §5 R1-R6 refuted-with-finding/misfires, §6 not-shown and §7 fences — files: .spark/website-lens-seo-ux-run/evidence.md |
| T7 | Update ROADMAP, README, docs/status to the run | #105 | #105/AC-6 | T6 | `done` | commit `fdeeab0` touches the three lines named in §2, the wording claims nothing evidence.md §6 lists as not shown, and no lens/skill/agent/template file is in the commit — files: ROADMAP.md, README.md, docs/status.md |
| T8 | `claude plugin validate .` on the final tree | #105 | #105/AC-7 | T7 | `blocked` | validate exits clean. Not met: `command -v claude` printed nothing in this container, and evidence.md §7 records AC-7 as not run and not verified |

## 4. Test Strategy

There is no unit or integration layer. Core has no test suite (`constitution.md §4`), and the target has none (`target-constitution.md §4`). Verification works like this:

- **US-1..US-5 (target behaviour):** static trace by T4 (`review.md` §4). Then the live browser in T5 (`qa.md` §2) using real clicks and Tab at 375/1280 px, with raw server HTML taken via same-origin `fetch()` and CLS/LCP via PerformanceObserver. The 8 `not-verified-live` rows stay open with reasons (Lighthouse absent, harness 404/headers, no zero-post or draft-only-tag content, `build-ghpages` not run). They are not passed by reasoning.
- **Citations:** every target `file:line` in evidence.md is re-resolved with `git show cf0cc1f:<path> | sed -n '<range>p'` (evidence.md §1). Plan-time spot check: `eleventy.config.js:57` (`preAttributes: { tabindex: 0 }`) and `:77-85` (hardcoded feed metadata) match in the scratch working copy.
- **Fences:** the target fence is `git diff --stat` empty and `git status` showing only untracked `.spark/` in the clone (evidence.md §1, §7). The repo fence is `git show --stat fdeeab0` listing only Markdown under this folder plus the three docs, and no `*.py` or other executable (`constitution.md §8`: `git ls-files '*.py'` empty).
- **Plugin bar:** `claude plugin validate .` (T8). It has not run yet, so the §4 bar is not met yet.
- **Left to a person / not done:** Design phase (`/look-and-feel`), Lighthouse score, a deployed host's headers, any assistive technology.

## 5. Risks & Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Plan written after the work, so it cannot have shaped it | A reader may take it as evidence of upfront planning | Disclosed in the header block. Status is `done` only where an artifact proves the DoD, and T8 stays `blocked` |
| `constitution.md §4` bar unmet: validate not run (T8) | The run lands without the repo's own minimum check | Recorded as not run (evidence.md §7). Run `claude plugin validate .` where the CLI exists before `/go-live` |
| The run's own ACs live only in issue #105, not in a spec | The `#105/AC-n` traceability cannot be resolved from `.spark/` alone | Q1 below. The mapping is spelled out in §3's note |
| QA `Status` is `passed` by orchestrator override of the tester's `failed` | A target failure could be read as a pass | The ruling and its scope (run, not target) are recorded in the `qa.md` Handoff. The tester's verdict is unedited, with precedent in `website-lens-public-run/qa.md` |
| Spec inaccuracies F14/F15 (message-box page list, A6 headers premise) | Specify-phase `security` output partly wrong | Recorded as evidence.md R2. The spec is not edited after the fact |
| Lens profile and spec gate set in dark mode, not by a person (evidence.md R4) | `security` activation unconfirmed. The spec says "approved" without a human | Disclosed in `target-constitution.md` §2 and in evidence.md. The user decides at this plan's gate |
| Dev server on :8080 left running (evidence.md R5b) | Stray process in scratch. Not used by QA (`qa.md` §1) | Container is disposable. Stop it before any reuse of the container |
| n = 1, one model, no lens-free control; the target has little interaction for `ux` | No firing rate can be claimed | evidence.md §3 and §6 state "no rate". Docs (T7) must not claim one |

**Questions for the user (do not block reading, block `approved`):**
1. Q1: Is mapping run tasks to issue #105's `AC-1..AC-7` acceptable, or should the run's own criteria be recorded as a spec in this folder?
2. Q2: Is AC-7 (T8) accepted as not run for this increment, or must validate pass before `/go-live`?

---

## ✅ PLAN GATE

*All boxes checked → `/increment` may start. Any box open → back to `/sprint-plan`.*

- [x] Spec status is `approved` (never plan against a draft): set by the dark-mode recommended gate, not a person
- [x] Architecture decision includes rejected alternatives (a decision without alternatives is a guess)
- [x] Architecture respects the constitution's technical constraints (or a conflict is recorded): Markdown-only, no script. The §4 validate bar is unmet and recorded (T8, §5)
- [x] Every task maps to a user story — no orphan tasks, no story without tasks: T1, T2, T6, T7 and T8 map to issue #105's ACs, not to a `spec.md` story (Q1). Every spec story has tasks (T3-T5)
- [x] Every Must AC and every applicable NFR is covered by at least one task (T5 lists all; NFR-8 is N/A)
- [x] Every task has a checkable definition of done
- [x] Task order respects dependencies
- [x] Test strategy covers every Must story
- [x] Line budget respected: Ist ~95 / Soll ~300 (excluding HTML comments) — self-reported, no linter checks this
- [x] Status `approved` set by the dark-mode recommended gate, not by a person

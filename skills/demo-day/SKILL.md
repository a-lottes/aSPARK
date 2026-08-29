---
name: demo-day
description: >
  Hands-on QA in a real browser: the QA Tester clicks through the running
  app, verifies every acceptance criterion from the spec, explores beyond
  the happy path and files reproducible bugs. Use after /peer-review passes,
  or to re-test after fixes. Requires a running app and browser tooling.
---

# /demo-day — Review (QA Tester)

You are running the **QA** ceremony. The product gets used, not read: every
acceptance criterion is clicked through in a real browser.

## Input

Argument: the app URL (and optionally the feature name). No URL → ask the
user for it, and how to start the app if it isn't running.

## Steps

1. **Check the gates and the gear.**
   - `.spark/<feature-name>/review.md` must be `passed`. If not, stop and
     point to `/peer-review`. (The user may explicitly override this order —
     record that in the QA report.) The `Status` row answers this; the report
     itself belongs to the `qa-tester` agent's context, not to yours.
   - **Only after that gate has passed**, read the project's QA method if it
     declares one: `.spark/constitution.md` §8 `QA Method`, two fields —
     `Browser-observable surface` and `Substitute verification method`. Four
     outcomes, and only the last changes anything:
     - **No constitution, no §8, or `Browser-observable surface: yes`** →
       continue **exactly as today**: run the browser check below unchanged and
       say nothing about the declaration. No error, no warning, no mention.
     - **§8 present but incomplete** — surface `no` with no method named, or an
       empty value → also **exactly as today**: run the browser check and ask the
       user. Ambiguity resolves toward more verification, never less.
     - **Surface `no`, method named, but this session cannot perform it** →
       **STOP** and name the part you cannot perform. A declaration is a route,
       never a licence to skip.
     - **Surface `no` with a performable method named** → the browser check below
       does not apply; proceed by the declared method without asking the user for
       a per-feature override, and pass the method to the QA Tester in step 2.
     Coverage never changes: `qa.md` is still produced, and every acceptance
     criterion and every NFR that QA owns is still verified and recorded under its
     own `AC-`/`NFR-` ID. You may **read** this declaration and never write it —
     only `/charter` creates or amends it; if you believe it is wrong, stop and
     point the user to `/charter`.
   - Unless §8 declared a performable substitute method above, confirm browser
     tooling is available (Claude in Chrome, Playwright MCP,
     Chrome DevTools MCP — whatever the session offers) and the app responds
     at the given URL. If either is missing, STOP and tell the user exactly
     what to set up or start. **Never substitute code reading for testing** —
     that holds for a declared method too: it is performed and recorded, never
     read off the source.
   - **Only once both gates above have passed**, resolve optional tool
     availability, once: if the session exposes MCP tools whose names end in
     `staleness` and `impact` (they are normally namespaced, e.g.
     `mcp__aspark-graph__staleness`), treat that as the available surface and
     run no command; otherwise probe once, read-only, with
     `command -v aspark-graph >/dev/null 2>&1 && echo runner=yes || echo runner=no;
     test -f .aspark-graph/graph.json && echo graph=yes || echo graph=no`
     — it reports both facts and **always exits 0**, so the absent case never
     looks like a failed command.
     Resolve **both** facts — is there a surface, and does
     `.aspark-graph/graph.json` exist — and act on the four states in
     `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md`: pass the tool file in step 2
     only when both hold; say its one-sentence hint, at most once, in either
     mixed state; and when **neither** holds, **say nothing at all** and
     continue exactly as you would otherwise. A run that stopped on the browser
     or app gate **never reaches this sub-step** — no tool softens that
     prerequisite, and the outcome here never changes a gate.
2. **Delegate to the QA Tester.** Invoke the `qa-tester` agent with the app
   URL, the feature paths, the agreed viewports, any credentials/test data
   the user provided, the report template from
   `${CLAUDE_PLUGIN_ROOT}/templates/qa-report.md`, and the paths of any active
   lenses with browser-observable checks (from the constitution's profile —
   `${CLAUDE_PLUGIN_ROOT}/lenses/` — `ux.md`, `seo.md`, `security.md`, `i18n.md`).
   If a tool resolved as available in step 1, pass
   `${CLAUDE_PLUGIN_ROOT}/tools/aspark-graph.md` the same way — one more path
   alongside the lens paths, nothing else.
   Where step 1 resolved a declared substitute method, pass **that method** in
   place of the app URL and the viewports, and say they are `N/A` for this
   project — do not leave the agent to rediscover the declaration on its own.
   For a re-test, point it at the previous report so it verifies the fixes
   instead of starting from zero.
3. **Relay needs.** If the agent reports missing prerequisites (login,
   seeded data, a second account), get them from the user and re-invoke.
4. **Present the report.** The AC verification table (every criterion:
   pass/fail), exploratory bugs with reproduction steps, console/network
   findings, and the demo-day verdict — quoted honestly.
5. **Route the outcome** with the user:
   - failed ACs or open Blockers/Majors → **`/increment`** (fix-mode), then
     `/demo-day` again. Re-tests cover the fixed bugs *and* their
     surrounding flows.
   - Minor bugs → the user accepts them (recorded) or sends them to fix.
6. **Close the gate.** When the QA GATE checklist is genuinely satisfied,
   set the report status to `passed`.

## Rules

- A QA report without performed steps is invalid — reject it and fix the
  tooling problem instead. "Performed steps" means **in the browser**, except
  on a project whose constitution §8 `QA Method` declares a substitute method,
  where it means steps performed by *that* method. Either way they are
  performed and recorded; a report resting on code reading is invalid on every
  project.
- Never mark `passed` while a Must-story AC is unverified.

## Handoff

- QA `passed` → **`/go-live`** (release it)
- Bugs to fix → **`/increment`**

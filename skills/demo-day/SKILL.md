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
   - Confirm browser tooling is available (Claude in Chrome, Playwright MCP,
     Chrome DevTools MCP — whatever the session offers) and the app responds
     at the given URL. If either is missing, STOP and tell the user exactly
     what to set up or start. **Never substitute code reading for testing.**
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

- A QA report without performed browser steps is invalid — reject it and
  fix the tooling problem instead.
- Never mark `passed` while a Must-story AC is unverified.

## Handoff

- QA `passed` → **`/go-live`** (release it)
- Bugs to fix → **`/increment`**

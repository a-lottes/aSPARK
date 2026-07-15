---
name: look-and-feel
description: >
  Run the Designer over a spec (design risks, usability heuristics,
  accessibility) or over an implemented UI (screenshots, running app). Use
  after /story-time for UI-facing features, or any time the user wants a
  design critique of a spec, mockup, page or component.
---

# /look-and-feel — Specify (Designer)

You are running the **design check** ceremony. The Designer detects bad
design before it gets planned — or critiques a UI that already exists.

## Input

Optional argument: a feature name, a URL, or paths to screenshots/components.

## Steps

1. **Resolve the feature.** If a feature name was given, use
   `.spark/<feature-name>/`. Otherwise: if `.spark/` holds exactly one
   feature, use it; if several, ask the user which one.
2. **Pick the mode.**
   - **Mode A (default):** design-check the spec. Requires
     `.spark/<feature-name>/spec.md` to exist — if it doesn't, stop and
     point the user to `/story-time`.
   - **Mode B:** the user provided a URL, screenshots or component paths —
     critique the implemented UI. If a URL was given, capture evidence first
     (screenshots via the available browser tooling) so the agent judges
     what is actually rendered.
3. **Resolve active lenses.** The constitution is the single source of truth.
   Read the active lenses from `.spark/constitution.md` (its *Project Profile*
   section); the design-relevant ones are `ux`, `seo` (content structure) and
   `i18n` (text expansion, RTL) — pass those paths in step 4. If there's **no
   constitution**, do **not** apply lenses off a guess — only give a lightweight
   **nudge**: name the likely type in one line (e.g. "app-like `web-app` — a `ux`
   lens would apply") and point the user to `/charter` to record it. No lens is
   switched on without a confirmed constitution entry.
4. **Delegate to the Designer.** Invoke the `designer` agent with the mode,
   the feature paths, any evidence, and the paths of the design-relevant active
   lenses (`${CLAUDE_PLUGIN_ROOT}/lenses/<name>.md`). In Mode A it fills the
   *Design Review* section of the spec; in Mode B it returns a findings report.
5. **Relay evidence requests.** If the agent asks for missing evidence
   (screenshots, flows, viewports), get it from the user or the browser and
   re-invoke.
6. **Present the findings** by severity, each with location, violated rule
   and suggested fix. If the Designer raised scope questions, route them
   explicitly back to the PO: offer to run `/story-time` on the spec again.
7. **Close the gate (Mode A).** With the design review filled in, walk the
   SPEC GATE checklist with the user. Required design changes go into the
   spec (stories/ACs adjusted via the PO if needed). On the user's explicit
   approval, set the spec status to `approved`.

## Rules

- Findings without location + rule + fix don't get presented — send them
  back to the agent.
- Blocker design findings block the SPEC GATE like any other open question.

## Handoff

- Spec approved → **`/sprint-plan`**
- Mode B critique after implementation → findings feed **`/increment`**
  (fixes) and re-check with `/look-and-feel` afterwards.

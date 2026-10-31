# Spec: visual-qa-review

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |
| **Date** | 2026-10-30 |
| **Ticket** | issue #1 |

**Handoff**
- **Status:** mirrors the header table above.
- **Summary:** QA looks at screenshots of every UI state, a deviation from a binding design direction is at least Major, the `ux` lens checks start-up robustness, the Designer's craft check names scale and space use.
- **Open:** `none`

**Prompt material.** Every check here is an instruction to an agent, not an enforcement: the effect is likely, not certain. No hold rate is claimed; docs say "prompt-enforced, unmeasured". Approved autonomously per the issue text (mode autonomous).

## US-1 (Must): QA judges what a user sees
- [ ] AC-1.1: A QA run on a feature with a browser surface records one Visual Review row per screenshot (state x wide-desktop/phone), each with an observation.
- [ ] AC-1.2: Browser-less projects get no Visual Review requirement.

## US-2 (Must): Binding design deviations are findings
- [ ] AC-2.1: A deviation from a `binding` direction is at least Major and not marked accepted by QA; a recorded decision is cited, not re-reported.

## US-3 (Must): Start-up robustness
- [ ] AC-3.1: `ux` lens item: storage throwing, reload mid-use, resize; a failed start is a Blocker.

## US-4 (Should): Designer names scale and space use
- [ ] AC-4.1: Visual craft check includes scale and space use; finding format unchanged.

## Non-functional
- NFR-1: Template contract markers and protected structures untouched; no new agent, lens or code; release is a separate step.
- NFR-2: Honest maturity labels in README, ROADMAP, docs/status.md.

## 8. Design Review
N/A: no UI (constitution: Markdown only).

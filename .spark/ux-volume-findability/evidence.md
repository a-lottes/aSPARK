# Evidence: ux-volume-findability

| | |
|---|---|
| Feature | ux-volume-findability |
| Phase | Act |
| Date | 2026-11-18 |

## T6a — Negative case first (constitution §1)

A project without `ux` active: `ux.md` is not dispatched (activation is `applies-to: [web-app, website]`, unchanged), and the constitution template tells `/charter` to delete the volume bullet and table when `ux` is off. The Facilitator drafts the table only "when `ux` comes out active". The PO's new sentence is conditioned on "when the `ux` lens is active"; the Designer and QA Tester sentences sit inside their `ux` bullets. So nothing changes for a project without `ux`. Checked by reading the diff, not by a session.

This repo's own profile (`library`, `ux` off): no file under `.spark/` gains a volume check. Zero.

## T6b — Designer dry run on the field project, old lens vs new lens

**Setup.** Two copies of the field project (a private web-app built by an aSPARK line; closed source, so not linked) at the same commit, outside the repo. In both, the constitution §2 got the same *Expected usage volume* table (customers 4 / 50 / 150; people 4 / 250 / 750; briefing signals per customer 0 / 10 / 50; notes per customer 2 / 30 / 200), as `/charter` would now write it. One `claude -p` session each (`sonnet`, tools Read/Grep/Glob), same prompt: act as `agents/designer.md` in Mode A for `briefing-view` and `quick-capture`, apply the design-phase checks of the given `ux.md`. Arm A got the lens from `main` (v0.19.0), arm B the lens from this branch. The prompt named the two view files and the module that builds the picker options, which hints both arms equally. n = 1 per arm, one model: no rate.

**Result.**

| Problem in the real app | Arm A (old lens + volume table) | Arm B (new lens + volume table) |
|---|---|---|
| Participant picker lists every person as checkboxes | Major (UX-1, via §2 large-data and principle 2) | Major (C1, §7 choice controls) |
| "n more not shown" leads nowhere | Major (UX-3) | Major (B1, §7 no dead-end cap) |
| 50 customer groups without a jump list | Major (UX-2) | Major (B2, §7 many groups) |
| Search/filter/archive cut without a decision | not raised as such (asked the PO in a fix) | Major (B3, §7 cut rule) |
| Spec states no volume for its lists | not raised | Minor (B4, C7, §7 volume stated) |
| Customer select with 50 to 150 options, no search | not raised | Minor (C2) |

**What this shows, and what it does not.**
- The load-bearing part is the declared volume. With the numbers in the constitution, the old lens already found the three worst problems in this hinted run. The original trails had no numbers and judged against four fixture customers, and their Design Reviews accepted the long lists (one Design Review noted a long list without a filter and accepted it because filters were out of scope). This supports adding the table, and naming the fixture-size trap in the lens.
- §7 added what the old lens did not raise here: the undecided cut, the missing volume in the spec, the 50-option select.
- Not shown: Specify and QA (no `/story-time` or `/demo-day` session was run), an unhinted firing rate, a second model. The QA volume run (AC-3.1) is unexercised.

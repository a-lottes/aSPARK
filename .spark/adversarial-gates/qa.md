# QA Report: adversarial-gates

| | |
|---|---|
| **Phase** | Review (hands-on) |
| **Owner** | QA Tester (`/demo-day`) |
| **Input** | Installed plugin at branch head (declared substitute method, constitution §8), `.spark/adversarial-gates/spec.md` (Increment 1: US-1, US-4) |
| **Status** | `passed` |
| **Round** | 1 |
| **Date** | 2026-10-04 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** Yes, I would demo this: the negative case held live, every doc claim matched what shipped; two Minor wording findings, no Blocker or Major.
- **Open:** `0 open` — Blockers: none; Majors: none; B1 fixed, B2 accepted by the user (see §3)
- **Binding ruling:** §5 Verdict and the gate checklist below — the only binding location; there is no other round to point to
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/demo-day` and proceed — don't stop on it.

## 1. Test Environment

- **App URL:** N/A. Substitute method per `.spark/constitution.md` §8 (`Browser-observable surface: no`): hands-on QA against the installed plugin; a performed step is a real ceremony invocation or an observed command output. Browser, viewport: N/A.
- **Under test:** branch `feat/adversarial-gates`, head `0533366`; base `origin/main` = `fa33f2c`. Claude Code 2.1.289 (`claude plugin validate` header per evidence T1).
- **Test data:** four scratch repos outside this repo (`.../scratchpad/qa-fx-{base,branch}-{ns,sp}`): one commit `init`, `README.md` (`# Notes app` / `A tiny CLI that stores notes.`), `.spark/notes/spec.md` with `Status` `approved` and US-1 (Must) / AC-1.1 (`notes add "x"` stores the text); no plan, no constitution. Base = `git worktree` of `fa33f2c` (removed afterwards). Branch = this working tree.
- **Lenses with a `qa` phase:** none active. Tool file `tools/aspark-graph.md` used for scoping only; no Result rests on it.

## 2. Acceptance Criteria Verification

AC-1.3, AC-1.4, AC-1.6 are `N/A — AC-1.7`: no gate qualified, so no table or row exists to check or replay. They are not passes. AC-2.x, AC-4.6, plan T10–T15: Increment 2, out of scope.

| Spec ID | Steps performed | Expected | Observed | Result |
|---|---|---|---|---|
| AC-1.1 | Counted scope: `ls .spark/*/{review,qa,evidence}.md` minus this feature = 51 files, `cut -d/ -f2 \| sort -u` = 18 folders. Re-derived at `file:line` (condition: Must AC, so re-derived from source): E1 `right-sizing/evidence.md:807` ("claimed `Status: passed` while its own QA", continues :808-810); E2 `:983` ("volunteered"); E3 `project-kickoff/review.md:57`; E4 `graph-mcp-verification/review.md:80`; E8 `lean-rounds/review.md:58`; E10 `campaign-core/evidence.md:494`; also read E5 `:79`, E6 `lens-dispatch-registry/review.md:76`, E7 `situational-lenses/review.md:55`, E9 `graph-gates/review.md:694`. Counted entries and classes in the file. | Every entry has quote, `file:line`, gate, class; per-class and per-gate counts stated and correct | All 10 quotes match their lines. Counts: `agent-evaded-gate` 1 (E1), `verdict-rounded-up` 2 (E3, E4), `other` 7 (E2, E5-E10) = 10; per-gate table lists `/demo-day` step 6 = 1. 51 files / 18 folders reproduce. One attribution slip: E3's "acting context" (B1, Minor) | ✅ pass |
| AC-1.2 | `git diff origin/main -- skills` (output empty, 0 bytes); `git diff --stat origin/main -- skills agents templates lenses .spark/constitution.md .claude-plugin` (empty) | No skill gains a table or mention; empty diff | Both empty. Diff stat lists only spec/plan/evidence/review, README, ROADMAP, docs/status.md | ✅ pass |
| AC-1.3 | none | n/a | `N/A — AC-1.7`: no table shipped | N/A |
| AC-1.4 | none | n/a | `N/A — AC-1.7`: no row exists | N/A |
| AC-1.5 | Ran 4 real headless sessions, `claude -p <cmd> --plugin-dir <dir> --max-turns 10 < /dev/null`, each in its own fixture copy: `/aspark:next-steps` and `/aspark:sprint-plan notes`, each on base and on branch. `grep -ic "rebuttal\|rationali\|gate hardening\|excuse"` over all four outputs. | Same routing and questions on both; no gate-hardening mention; skill diff empty | `next-steps`, base: no constitution, recommends `/charter` first, offers skip or steer, no writes. Branch: same recommendation, 3 options (charter / skip / own idea), no writes. `sprint-plan`, base: blocked on unreadable `templates/plan.md` plus 2 architecture questions (language, storage). Branch: same template-read block plus 4 questions (language, storage, install, empty text; the first two identical to base). Grep hits: 0 / 0 / 0 / 0. Fixture `git status` unchanged on both `sp` runs (only untracked `.spark/.guard/`). Question counts differ (2 vs 4) while skill text is byte-identical, so that is run variance; n=1 each, a check, not a proof | ✅ pass |
| AC-1.6 | none | n/a | `N/A — AC-1.7`: nothing to replay | N/A |
| AC-1.7 | Read `evidence.md:125-133` (T4 ruling), `plan.md` T6/T7 rows, `git diff origin/main -- skills`, README/status/ROADMAP text | No table shipped; outcome recorded refuted-with-finding; US-4 states it | T4: "the outcome is **refuted-with-finding**", best gate 1 entry. T6/T7 `N/A — AC-1.7`. No skill diff. README heading "searched, no rebuttal rows shipped"; status.md "Shipped: none"; ROADMAP "no rebuttal rows shipped" | ✅ pass |
| AC-1.8 | Read E3, E4 in `evidence.md`; `git diff origin/main -- skills` | Kept, flagged for US-2, no `SKILL.md` row | E3, E4 present with "US-2 flag: yes — input for US-2 (Inc 2)"; line 123 repeats it; skill diff empty | ✅ pass |
| US-4 / AC-4.1 | Read README `:122-127`, ROADMAP `:44` and `:50-56`, status.md `:260-266` at head; checked each claim against the commands above | States what shipped (none), in-repo grounding, unmeasured | All three say no rows at any gate; "in-repo trails, not field reports"; "effectiveness is unmeasured"; counts (51 files; 1/2/7; 10 entries) match §2 AC-1.1 | ✅ pass |
| AC-4.2 | Read ROADMAP Next entry vs Shipped row | Updated in step; standard stays planned | Next entry retitled "Stricter verdict rules for review and QA", opens "Planned, not built"; Shipped row added. No contradiction (retitle: B2) | ✅ pass |
| AC-4.3 | Read README `:124`, ROADMAP `:55-56`, status.md `:266`; ran `grep -n aspark-guard docs/family.md` | Gates stay prompt-enforced; code enforcement is the sibling's | All three say prompt-enforced and point to `aspark-guard`; `docs/family.md:51-52` says the same ("prompt-enforced"); no contradiction | ✅ pass |
| AC-4.4 | `grep -rn` over `*.md` outside `.spark/` for dual/second reviewer | Only as not built, with re-open condition | README `:127`, ROADMAP `:56`, status.md `:266`: "not built ... re-open only on a new argument or observation, such as a recorded single-reviewer miss" (matches spec §6) | ✅ pass |
| AC-4.5 | `grep -rn -i anti-generosity --include='*.md'` outside `.spark/`: 0 hits. Read all three diffs for shipped/active wording | No claim of verdict-behavior change or active standard | README: "planned and not built; they change nothing today". ROADMAP "Planned, not built ... would change". status: "planned, not built". No "enforced guarantee", "reduces" or "proven" wording in the added lines | ✅ pass |
| NFR-1 | `git diff origin/main -- skills` empty; README subsection `awk` count of non-empty lines between its heading and `### Campaigns` | Skills byte-identical; README subsection within 8 lines | Empty diff; subsection = 4 non-empty lines (1 paragraph + 3 bullets) | ✅ pass |
| NFR-2 | Read where the docs say rows apply or stay silent; ran `/next-steps` and `/sprint-plan` on both trees (AC-1.5) | Docs name activation and silence | status.md: "Rows apply at no gate today and stay silent everywhere"; README: "every skill is unchanged"; neither non-review ceremony showed a gate-hardening item | ✅ pass |
| NFR-3 | `git diff origin/main -U0 -- skills \| grep -c '^[+-]name:'` and the skills diff | No command renamed; no frontmatter `name` changed | `0`; skills diff empty | ✅ pass |
| NFR-4 | AC-1.5's four live runs; `git diff origin/main -- .claude-plugin templates` empty | Uncovered ceremonies run unchanged | Same routing on both trees; templates and manifests untouched. `plugin.json` has no bump yet (Release Manager's at `/go-live`, per `evidence.md:199`); a go-live pre-flight item, not a QA failure | ✅ pass |
| NFR-5 | Read README subsection as a user | What shipped, where it applies, degraded behavior stated | Says what shipped (search, none), grounding, cannot-be-tested-in-Core, planned items. No behavior change exists to degrade | ✅ pass |
| NFR-6 | `git ls-files '*.py'` (empty); `claude plugin validate .` | Empty; passes | Empty. `✔ Validation passed with warnings` (one warning: root `CLAUDE.md` not loaded as context, pre-existing, same as `evidence.md:201`) | ✅ pass |
| NFR-7 | `git diff origin/main --stat`: no template, lens or skill file changed | No existing ID renumbered | No existing artifact edited, only new feature files plus three docs; no ID-bearing file changed | ✅ pass |
| NFR-8 | Grepped added doc lines for "fires" / effectiveness claims | No "fires" claim; docs say fired-ness untestable | README `:126` and status.md `:266`: "whether a row would fire cannot be tested in Core"; no effectiveness number anywhere | ✅ pass |
| NFR-9, NFR-10 | none | N/A in spec | N/A per spec (`security` lens off; no UI) | N/A |

## 3. Exploratory Findings

Also tried, no finding: all new links resolve (`ls` on `.spark/adversarial-gates/evidence.md`, `lenses`, `docs/status.md`, `docs/family.md`); README, ROADMAP and status.md agree on the count of 51 files and on "no rows"; nothing in `docs/family.md` or constitution §1 ("honesty about maturity over ambition") is contradicted; a search for self-approval or approved-without-user acts in `review.md`/`qa.md` surfaced no `agent-evaded-gate` candidate the corpus missed (a spot check, not a census, as the corpus itself says).

| # | Severity | Steps to reproduce | Expected vs. observed | Status |
|---|---|---|---|---|
| B1 | Minor | Open `.spark/adversarial-gates/evidence.md` E3 and `.spark/project-kickoff/evidence.md:321-325` | E3 says acting context is "`reviewer` agent's own earlier round". The over-claim (✅ on an inspection-only AC) was written in `project-kickoff/evidence.md` by the build session; the reviewer caught it (`review.md:57`, F9). Artifact wording only, changes no class, count or verdict (capped Minor) | fixed |
| B2 | Minor | Open `ROADMAP.md:50` and `gh issue view 13` | ROADMAP links `#13` under the title "Stricter verdict rules for review and QA"; the issue is titled "Add anti-rationalization tables to every gate" (OPEN). A reader clicking the link sees a different title. The rename is a documented deviation (`plan.md:177`); `docs/family.md:51-54` still cites #13 as the prompt-enforcement gap, which stays accurate | accepted by the user (2026-10-04): the issue title lives on GitHub; the rename is the documented deviation at `plan.md:177` |

## 4. Console & Network

N/A: no browser. Command output observed: all four headless sessions exited 0; no errors. The only `validate` warning is the pre-existing root `CLAUDE.md` one. Both `/sprint-plan` runs reported being denied read access to `templates/plan.md` under headless permissions, on base and branch alike (environmental, not a branch regression). A stale worktree `.../05fe8cfa.../scratchpad/base` from an earlier session is still registered in `git worktree list`; it is not mine and was left alone. My `qa-base` worktree was removed.

## 5. Verdict

Yes, I would demo this to a stakeholder right now. The corpus quotes reproduce from source, the skill diff is empty, the live negative runs routed identically with no gate-hardening trace, and every doc claim is "none shipped, in-repo, unmeasured, prompt-enforced, standard planned". Nothing unshipped is described as delivered. Limits I could not remove: each live run is n=1 (nondeterministic wording and question counts), and the corpus is a fixed-term search, not a census. B1 and B2 are Minor wording items for the user to accept or fix. AC-1.3, AC-1.4, AC-1.6 are N/A by AC-1.7, not passed. No row is `⚠ not-verified-live`.

---

## ✅ QA GATE

- [x] Every Must-story acceptance criterion verified by the declared method and passed (AC-1.3, 1.4, 1.6 are N/A by AC-1.7, recorded as such)
- [x] Every browser-observable NFR verified and passed (NFR-9, NFR-10 N/A per spec)
- [x] No open Blocker or Major bugs (Minor B1, B2 listed; acceptance is the user's decision)
- [x] Console free of errors on the tested flows (N/A browser; command output clean)
- [x] Tested on all agreed viewports (N/A, no UI)
- [x] Line budget respected: Ist 82 / Soll ~130 (excluding HTML comments) — self-reported, no linter checks this
- [x] Status set to `passed`

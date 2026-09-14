# Spec: companion-offer

| | |
|---|---|
| **Phase** | Specify |
| **Owner** | Product Owner (`/story-time`) |
| **Status** | `approved` |
| **Date** | 2026-09-14 |
| **Ticket** | `none` |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`). `approved` by the user, 2026-09-14, including the AC-1.3 (A3) qualified-maturity judgment call as drafted.
- **Summary:** Issue #45 asked for a setup-time *offer* of the two optional companions. The interrogation cuts it to its evidenced core: `aspark-guard` ships in `marketplace.json` and is named in **no other tracked file**, which is a §4 docs-in-step defect the repo can fix today at zero consumer attention cost. The offer ceremony, constitution §9 and update-detection are **cut** — they charge every consumer's setup for a benefit with no observed user and no success signal.
- **Open:** `none` — A2, A3, A6, A8 resolved 2026-09-14 (see §3). **A3 is a judgment call, not a mechanical resolution** — the guard's maturity is substantial-but-self-reported, flagged explicitly for the user's gate walk rather than smoothed into a clean label.
- **Binding ruling:** §4 User Stories US-1…US-3; §6 Out of Scope holds the cut of the offer, §9 and update-detection, each with its reopen condition. AC-1.2/AC-1.3 sharpened, AC-1.6 added (append-only) per the 2026-09-14 verification round.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed.

## 1. Problem & Goal

- **Problem.** Two people hurt today, and neither is the one the issue names.
  1. **A developer evaluating aSPARK from its README.** They read `README.md` §Optional Tools, which describes exactly one companion. The repo ships two: `.claude-plugin/marketplace.json:16` declares `aspark-guard`, and `grep -rl 'aspark-guard'` over the whole tree returns **that one file** (verified 2026-09-14). The README asserts of itself that it "always reflects the current state" (§4's stated bar) — so the repo currently *contradicts what it ships*. The user who most needs the guard is the one who read ROADMAP #13 ("the gates are prompt-enforced… they hold until an agent reasons its way around one"), which is the exact gap a gate-enforcing plugin addresses, and who is told nowhere that such a plugin exists.
  2. **The next contributor.** `tools/README.md` teaches two shapes, lens and tool, and a decision rule ("could the constitution know this?"). The guard is neither — it is a plugin the host installs, with no probe, no path to pass and no phase slice. Nothing says so, so the plausible next move is a `tools/aspark-guard.md` that no ceremony can ever pick up.
- **What is *not* the problem.** "Users never hear about the companions" is not evidenced. ROADMAP's own first line reads *"aSPARK has never been proven by a full loop run on someone else's real project"*, and there are no field reports. There is no observed user who was blocked by not knowing. The issue says it plainly itself — *"a distribution failure, not a product one"* — and a distribution failure is the maintainer's, not something to bill to every consumer's setup conversation.
- **Goal.** Every optional companion the repo distributes is described in the repo's own docs, with an honest maturity label and a verified install command; and the three shapes an optional capability can take are distinguishable by a contributor reading one table. **No ceremony says one word more than it does today.**
- **Success signal.** (a) `grep -rl 'aspark-guard' --include='*.md'` returns at least `README.md`, up from zero tracked `.md` files; (b) the count of new interactive prompts, questions or sentences added to any ceremony run is **zero**, verified by the diff touching no file under `skills/`, `agents/`, `templates/`, `lenses/` or `.claude-plugin/`; (c) every install command and URL added was observed to work, or clearly marked as researched-but-not-yet-executed, before it was written down.
- **Why now.** The docs defect exists regardless of whether the offer is ever built, costs one small diff, and is a precondition for the offer if it is ever reinstated — an offer that points at an undocumented plugin is worse than silence. Cutting the rest now also buys the evidence the offer lacks: ship the docs, and a field report can tell us whether discovery was ever the blocker.

## 2. Target Users

- **A developer evaluating aSPARK** from the repo README or the marketplace listing, deciding what to install.
- **A contributor adding an optional capability** to Core, choosing between `lenses/`, `tools/` and a sibling plugin.
- **The sole maintainer (`a-lottes`)**, who owns the §4 docs-in-step bar this repo currently misses.

## 3. Assumptions & Open Questions

| # | Assumption / Question | Resolution |
|---|---|---|
| A1 | The idea arrived as a solution: *"one prompt-level offer, shaped like the constitution nudge, plus constitution §9, plus version-compare re-offer."* The underlying need this spec is judged against: *a person evaluating or extending aSPARK can find out what optional companions exist, and judge them, from the repo's own documentation* | recorded per PO rule; the solution is assessed in §6, not adopted |
| A2 | `github.com/a-lottes/aSPARK-guard` is public, installable today, and the install command is exactly `/plugin install aspark-guard@aspark` | **RESOLVED** (`gh` CLI, 2026-09-14, relayed by the invoking session — this agent has no Bash/`gh` tool access, see `evidence.md`): repo is **PUBLIC**; `.claude-plugin/plugin.json` there names `aspark-guard` v0.1.0; **no GitHub Releases exist** (source is the repo directly per `marketplace.json`'s `{"source":"github","repo":"a-lottes/aSPARK-guard"}`, not a release, so this doesn't block installability); last push 2026-09-11. Install command confirmed correct by name/marketplace-membership pattern (mirrors `aspark@aspark`'s own). **Actually running the command is not yet done** — AC-1.6 (new) covers that. AC-1.2 sharpened accordingly |
| A3 | The guard's proof state is **unknown**, so §1 forces the label `unproven` | **RESOLVED — and the evidence overturns the draft's guess, judgment call flagged for the user.** (`gh api`, 2026-09-14, relayed, see `evidence.md`): the guard's own README states all six milestones (M0–M5) **Built**, **142 tests** replayed over **22 real gated artifacts** with no false positive, and an author-verified marketplace install dated **2026-09-11** (guard's own `docs/evidence.md` §4). Against that: `~/.claude/plugins/installed_plugins.json` on this machine lists **only** `aspark@aspark` — the guard is not installed here despite that claim — and the guard's own README names its own gap: *"none of this has run a full feature loop on a project that isn't this author's"*, the same gap `ROADMAP.md` names about Core. Neither a bare `proven` nor a bare `unproven` is honest: the evidence is real and substantial, but self-reported and independently unverified by Core. AC-1.3 rewritten to a qualified statement, not a single enum word |
| A4 | Nobody is observed to have been blocked by not knowing a companion exists | accepted as the ground for the §6 cut, not as a claim that nobody was |
| A5 | The guard is **not** undiscoverable: Claude Code's `/plugin` browser lists both plugins from `marketplace.json` with their descriptions. The gap is that the repo's own docs contradict that listing by omission | accepted; narrows the problem to a docs defect, which is what US-1 fixes |
| A6 | Read-only detection of an installed plugin is *technically* possible — `~/.claude/plugins/installed_plugins.json` carries name, version and commit — but it is host-internal, undocumented, outside the project root and schema-versioned (`"version": 2`) | **RESOLVED BY CUT.** The offer (§6 item 1) is out of scope, so nothing in this feature depends on plugin-install detection. Noted, not built; reopens only if the offer itself reopens |
| A7 | The §6 boundary question in issue #45 (*a gate must degrade to silence; is an onboarding offer a gate?*) needs no answer under this scope — nothing here speaks at a gate or anywhere else | deferred with the offer (§6) |
| A8 | The user accepts the cut: docs now, offer/§9/update-detection not now | **RESOLVED (user, via coordinator, 2026-09-14).** US-1/US-2/US-3 (docs only) proceed; the companion offer, constitution §9, and update-detection stay in §6 Out of Scope with their reopen conditions as drafted |

## 4. User Stories

### US-1 (Must): The second companion is documented where the first one is

> As a developer evaluating aSPARK, I want both optional companions described in the README, so that I can judge whether I want either without opening `.claude-plugin/marketplace.json`.

**Acceptance criteria:**

- [ ] AC-1.1: Given the feature branch, when `grep -rl 'aspark-guard' --include='*.md' .` is run with `.spark/` excluded, then it returns at least `README.md` — up from zero tracked `.md` files on `main` (verified 2026-09-14).
- [ ] AC-1.2: Given `README.md` §Optional Tools, when the guard's entry is read, then it states in at most four sentences: what the plugin does, that it is optional, that nothing in aSPARK installs it on the user's behalf, and the exact command the user runs — `/plugin install aspark-guard@aspark`. The command's correctness (repo public, plugin manifest present with matching name `aspark-guard`, no Releases required because the marketplace source is the repo itself) was verified via `gh` CLI 2026-09-14 and is recorded in `evidence.md`; **actually executing** the command is a separate criterion (AC-1.6), not required before this entry is written.
- [ ] AC-1.3: Given §1's honesty bar, when the guard's entry is read, then it carries a **qualified maturity statement** — not a bare `proven` / `unproven` / `planned` — naming: (a) the guard's self-reported evidence (142 tests replayed over 22 real gated artifacts; an author-verified marketplace install dated 2026-09-11, per the guard's own `docs/evidence.md` §4); (b) that this evidence is self-reported by the guard's own author and has not been independently verified by aSPARK Core; and (c) that the guard has never been exercised through a full third-party feature loop — the gap `ROADMAP.md` names about Core itself. It makes no claim about gate enforcement that aSPARK Core has itself observed.
- [ ] AC-1.4: Given the guard's entry, when it is read, then it names the concrete gap it addresses — prompt-enforced gates, cross-referenced to ROADMAP/[#13] — rather than restating the `marketplace.json` description.
- [ ] AC-1.5: Given every URL and command added anywhere by this feature, when each is opened, run, or (where only its shape was verified via a registry/API check rather than executed) marked as such, then the result is recorded in `evidence.md` with its date and method.
- [ ] AC-1.6: Given the install command named in AC-1.2, when `/plugin install aspark-guard@aspark` is actually run against the live marketplace — e.g. as part of this feature's own `/demo-day` dogfood, per §8's substitute QA method — then its outcome (success, failure, or observed prompt behavior) is recorded in `evidence.md` with date and result, independent of and in addition to the guard's own self-reported 2026-09-11 verification.

### US-2 (Should): A contributor can tell a companion plugin from a tool file

> As a contributor adding an optional capability, I want `tools/README.md` to distinguish all three shapes, so that I do not create a `tools/aspark-guard.md` that no ceremony can ever probe or pass.

**Acceptance criteria:**

- [ ] AC-2.1: Given `tools/README.md` §"Tool or lens?", when it is read, then a third shape — **companion plugin** — is presented on the same axes the existing table uses (what it is · activated by · who decides · example), with `aspark-guard` as the example.
- [ ] AC-2.2: Given that section, when it is read, then it states that a companion plugin is installed by the user in the host, is never passed by path, has no tool file and no probe — and that adding a tool file for one is a defect.
- [ ] AC-2.3: Given `tools/README.md` §Available tools, when the table is read, then it still lists exactly one row (`aspark-graph.md`); the guard is not added there.
- [ ] AC-2.4: Given `tools/aspark-graph.md` and `tools/README.md` §"The canonical probe bullet", when both are diffed against `main`, then the four-state availability table (including the `no` / `no` → **say nothing** row) and the probe bullet are **byte-identical** to `main`.

### US-3 (Should): The status surfaces stop implying there is one companion

> As a reader checking what aSPARK actually ships, I want README §Project Status and ROADMAP to account for both companions, so that a distributed-but-undocumented plugin is not presented as if it did not exist.

**Acceptance criteria:**

- [ ] AC-3.1: Given `README.md` §Project Status, when the `Optional tools` row is read, then it either carries the guard with its own qualified maturity statement or says explicitly that the row covers `aspark-graph` only and points to where the guard's state is stated.
- [ ] AC-3.2: Given `ROADMAP.md`, when `grep -n 'guard'` is run, then the guard is accounted for using the file's literal status vocabulary (**Shipped** · **Next** · **Blocked** · **Not planned**), with one sentence of *why*, and without restating the issue.
- [ ] AC-3.3: Given the three files changed by US-1…US-3, when they are read together, then the guard's maturity claim is the **same qualified statement** (or an equivalently-scoped shorthand) in all three — not a single word in one file and a contradictory or looser claim in another.

## 5. Non-Functional Requirements

| # | Category | Requirement (measurable) | How it's verified |
|---|---|---|---|
| NFR-1 | Backward compatibility (§4) | `git diff --name-only main...HEAD` lists **no** path under `skills/`, `agents/`, `templates/`, `lenses/` or `.claude-plugin/`, and under `tools/` only `README.md`. An already-installed consumer's loop behaves identically. This is the §4 negative case, and it is the whole of it — the feature touches no phase, so there is no positive dogfood to run | /peer-review |
| NFR-2 | `library` §1 — public surface | Zero addition to the consumed contract: no new slash command, no new `${CLAUDE_PLUGIN_ROOT}/…` path any skill resolves, and the §3 protected-structure table (headings, columns, ID patterns) unchanged in every template | /peer-review |
| NFR-3 | `library` §2 — compatibility & versioning | Docs-only ⇒ **patch** bump in `.claude-plugin/plugin.json`, not minor: no optional capability is added (§5's minor-bump trigger is absent). The release notes state the version and that reasoning in one line | /peer-review + /go-live pre-flight |
| NFR-4 | `library` §4 — contract clarity | The guard's README entry matches the graph's entry clause for clause: what it does · optional · nothing installs it for you · the exact user-run command · what its answer must never be read as. Falsifiable by laying the two entries side by side | /peer-review |
| NFR-5 | §6 non-negotiable — degrade to silence, and attention cost | The number of prompts, questions or sentences this change adds to any ceremony run is **0**, in a project with both companions absent and in one with both present. Implied by NFR-1's diff scope; asserted separately because it is the constraint scope creep would break first | /peer-review |
| NFR-6 | §1 honesty + §3 no false install claim | Every maturity claim added is grounded in evidence named inline, distinguishing self-reported from independently-verified where the two differ (A3). Every install command and URL added was executed or opened, or — where only its shape was researched via a registry/API check — recorded as such, with date, method and result in `evidence.md` (AC-1.2, AC-1.5, AC-1.6). No sentence describes an intention, or another repo's self-report, as this repo's own delivered proof | /peer-review |
| NFR-7 | §4 quality bar | `claude plugin validate` passes on the branch, with its output recorded — a real command whose output was observed, per §8's substitute method | /demo-day |

- **Accessibility / performance:** N/A — no UI, no runtime (constitution §4).
- **`library` §3 packaging & footprint:** N/A per constitution §2 — no bundle, no dependencies, no engines. This change adds three prose blocks and no file.

## 6. Out of Scope

Everything below is a conscious cut, each with what would reopen it.

1. **The companion offer itself** (a line in `/charter` and `/spark`). Cut: no observed user (A4), no success signal proposed, and it charges 100% of consumers' setup attention for two tools whose value here is unproven — the exact shape §1 "suppression is a feature" rejects, since it names no profile where it stays silent. **Reopens on** a field report, or any observed instance of someone wanting a companion and not finding it.
2. **Constitution §9 `Companions`** in `templates/constitution.md`. It exists only to give the offer a memory; with no offer there is nothing to remember, and an empty section is a paragraph every `/charter` must consider forever. **Reopens with 1.**
3. **Update-detection and re-offer on version change** (compare §9 against `plugin.json`). The most expensive and most nag-prone part, dependent on 1 and 2, and gated on "the release actually changed the companion story" — a judgement nothing in the repo can evaluate. **Reopens with 1.**
4. **Writing the §6 gate-vs-onboarding boundary into the constitution.** Only needed once something speaks outside a gate. Nothing here does. **Reopens with 1.**
5. **Detecting whether a plugin is installed.** No supported read-only affordance exists; the host-internal file (A6) is not a contract Core may depend on. **Reopens** if Claude Code documents one.
6. **A consumer-visible changelog for `autoUpdate: true` installs.** This is the real gap issue #45 surfaced — Core moves under installed consumers with no surface that tells them anything changed. It is bigger than a companion offer and deserves its own issue, not a rider on this one.
7. **Any change to `tools/aspark-graph.md`'s four-state table or the canonical probe bullet** (AC-2.4 asserts they are untouched).
8. **A `tools/aspark-guard.md` tool file.** The guard is not a tool: no probe, no phase slice, nothing to pass by path (US-2).
9. **The template version handshake** (issue #44, ROADMAP *Blocked*) — two-repo coordination, unchanged by this feature.
10. **Fixing the graph's artifact-filename defect** (§3, defect 1) — the consuming repo's to fix; named here only because it bounds what the guard's or graph's entry may claim.

## 7. Clarifications

| # | Date | Question | Resolution |
|---|---|---|---|
| C1 | 2026-09-14 | Functional boundary: is the deliverable a *behaviour* change or a *docs* change? | Docs only. NFR-1 states the boundary as a diff assertion, so "correct" is checkable rather than argued |
| C2 | 2026-09-14 | Is the guard truly undiscoverable? | No — the host's `/plugin` browser lists it from `marketplace.json` (A5). The defect is the repo's docs contradicting its own distribution, which is narrower and cheaper than "discovery" |
| C3 | 2026-09-14 | Roles & permissions | N/A — no actor, no data, no permission surface. Recorded so the category is not a silent gap |
| C4 | 2026-09-14 | Error / edge case: what if `aSPARK-guard` is not public or not installable? | Resolved by A2's verification — it is public, the manifest matches, the install command's shape checks out. AC-1.6 still requires actually running it before the feature is considered fully proven |
| C5 | 2026-09-14 | What stops this from re-growing into the offer during `/increment`? | NFR-1 and NFR-5, both falsifiable by diff, plus the ten named cuts in §6 |
| C6 | 2026-09-14 | Which maturity word does the guard get? | Not a single word — resolved as a qualified statement (A3, AC-1.3): substantial self-reported evidence, independently unverified by Core, not currently installed on this machine, never run through a third-party loop. **Flagged to the user as a judgment call**, not a mechanical resolution |
| C7 | 2026-09-14 | Does AC-1.5's "executed" bar apply to the gh CLI registry checks that resolved A2/A3? | No — those checks confirm a command's *shape* is correct (repo exists, manifest matches), not that it was run. AC-1.2/AC-1.5 now say so explicitly; AC-1.6 (new, appended) requires the install command itself to be run and its outcome recorded, separately |

## 8. Design Review

*N/A — no UI-facing surface. This project ships no UI (constitution §4, §8).*

---

## ✅ SPEC GATE

*All boxes checked → `/sprint-plan` may start. Any box open → back to `/story-time` or `/look-and-feel`.*

- [x] Problem, goal and success signal are concrete (no buzzwords, no "everyone")
- [x] Every story has testable Given/When/Then acceptance criteria
- [x] Stories are prioritized (MoSCoW) and at least one is a Must
- [x] Non-functional requirements are stated and measurable (or marked N/A with reason)
- [x] Clarify pass done: no ambiguity left unresolved or unparked
- [x] Open questions are resolved or explicitly accepted as risk — A2, A3, A6, A8 resolved 2026-09-14; **A3 is a judgment call, flagged for the user's explicit sign-off, not a routine close**
- [x] Out-of-scope section is filled (something was consciously cut)
- [x] Constitution (`.spark/constitution.md`) respected, or conflicts recorded as open questions
- [x] Design review done for UI-facing features (or marked N/A with reason)
- [x] Line budget respected: Ist 145 / Soll ~250 (excluding HTML comments)
- [x] Status set to `approved` by the user

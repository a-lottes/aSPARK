# Review Report: lean-artifacts

| | |
|---|---|
| **Phase** | Review (`/peer-review`) |
| **Feature** | `lean-artifacts` |
| **Diff** | commit `3d2939d` (`acfa3ac..3d2939d`) |
| **Status** | `passed` |
| **Date** | 2026-08-17 |

**Handoff**
- **Status:** mirrors the header table above (authoritative for `Status`).
- **Verdict:** PASS — additive Handoff block, parser-invisible by construction (re-verified against source); every Must AC traces; two benign Nits only.
- **Open:** `2 open` — Blockers: none; Majors: none (Nits F1, F2: see §3)
- **Binding ruling:** §6 Verdict and the REVIEW GATE below carry the binding ruling — round 1, no re-review.
- **On conflict:** the numbered body below wins for everything except `Status`; log the mismatch as a finding at the next `/peer-review` and proceed — don't stop on it.

## 1. Scope

Reviewed the single increment commit `3d2939d` — 14 files, +459/−17. Shipped surface touched: the Handoff block added to all five templates (`review-report.md`, `qa-report.md`, `spec.md`, `plan.md`, `release-notes.md`), reading/writing rules in `agents/reviewer.md`, `skills/increment/SKILL.md`, `agents/release-manager.md`, `agents/product-owner.md`, `skills/next-steps/SKILL.md`, the version bump in `plugin.json`, and the README §Project Status bullet. Non-shipped artifacts: `.spark/lean-artifacts/plan.md`, `evidence.md`. **Not reviewed:** commits `2f48497` (spec) and `acfa3ac` (constitution amendment) — prior accepted ceremonies; I read the amended constitution as binding context only.

Verification I ran myself (not taken on faith from evidence.md): read `~/aSPARK-graph/src/aspark_graph/artifacts.py` lines 194–333 directly; grepped every template for `^\s*\|\s*\*\*Status\*\*` / `\*\*Version\*\*` pipe rows and for `^##` heading positions; read `skills/spark/SKILL.md:33–52` (router) and `templates/qa-report.md:44–46` (bug-ID scheme); checked `marketplace.json` for a second version field. No graph tool query was needed — the graph is blind to Core's `review.md`/`qa.md` (defect 1), so the static walkthrough is the sound method, exactly as the plan argues.

## 2. Plan Conformance

| Task | As planned? | Note |
|---|---|---|
| T1 | ✅ | Consumer list reconciled in evidence Entry 1; `next-steps` A6 addition folded in, `spark`/`demo-day`/`go-live` correctly classed compat-only. |
| T2–T4 | ✅ | Walking-skeleton checkpoint honoured *in the record*: evidence Entry 2 gates the design ("T5 onward proceeds unchanged") before rollout. Squashed to one commit, so intra-commit ordering isn't independently git-verifiable; the evidence narrative carries it. |
| T5–T6 | ✅ | Block present in all four remaining templates, same shape, ≤12 lines, no `##`, no second pipe `Status`/`Version` row (grep confirmed by me). |
| T7 | ✅ | Fix-mode write-back is unambiguous overwrite-in-place (see AC-1.3 below). |
| T8 | ✅ | release-manager, product-owner, next-steps each state first read + read-on condition. |
| T9 | ✅ | Second-pair dogfood + AC-1.3 live overwrite + four-parser walkthrough in evidence Entry 3. |
| T10 | ✅ | `0.6.0` minor bump; README bullet honest, no saving claimed. |

Two distribution differences from the plan's §1 prose, neither a defect: (a) plan §1 says "Six fields" then enumerates five (`Status, Verdict/summary, Open, Binding ruling, On conflict`) — only reconcilable if the `**Handoff**` lead label is counted as field six; (b) plan §1 says the HTML comment states conflict precedence, but in the shipped templates that lives in the visible `On conflict` bullet while the comment omits it. NFR-3 is still met by each template as a whole.

## 3. Findings

| # | Severity | Location | Finding | Status |
|---|---|---|---|---|
| F1 | Nit | `.spark/lean-artifacts/evidence.md:107–109` | Cited parser line-ranges run a hair short at the tail (`_section` 276-289 vs actual 276-290; `_first_table` 293-311 vs 293-315; `_parse_review` 194-221 vs 194-223). Every regex and behaviour claim is exact; only end-lines are approximate. Why it matters: the evidence is the test-suite substitute, so its citations should land precisely. Fix: adjust end-lines. | open |
| F2 | Nit | `.spark/lean-artifacts/plan.md:25` | "Six fields:" enumerates five named fields. Why it matters: a reader counting fields against a template finds a mismatch. Fix: say "five fields (plus the `**Handoff**` label)" or list six. | open |

No Blocker, Major, or Minor findings. Left both Nits `open` rather than editing — both touch committed, approved-artifact prose where the author's intent (does the lead label count as a field; how precise should evidence line-cites be) is theirs to settle, not mine.

## 4. Requirements Traceability

| Spec ID | Implemented at | Verdict |
|---|---|---|
| AC-1.1 | `templates/review-report.md` + `qa-report.md` Handoff block: Status/Verdict/Open bullets | ✅ met |
| AC-1.2 | `On conflict` bullet ("body wins except `Status`") + `Status` bullet ("authoritative for Status") | ✅ met — precedence stated, no fact duplicated without it |
| AC-1.3 | `skills/increment/SKILL.md:52–57` — "overwrites the Handoff block in place… never append a round… stale block is a defect" | ✅ met — non-owner write-back is unambiguous overwrite, not append |
| AC-1.4 | Verified by me against `artifacts.py`: `_status` (267) needs `\|…\*\*Status\*\*…\|`; block uses `- **Status:**` (bullet, colon inside bold, no pipe) — cannot match. `_section` (280) matches `^##\s`; block adds zero `##`. `_first_table` reads only inside a section; block sits before `## 1`. `_parse_review` findings-table header untouched. | ✅ met — no `TemplateDriftError`, identical nodes |
| AC-1.5 | evidence Entry 2/3 negative case on real old-shape artifacts | ✅ met |
| AC-1.6 | `Binding ruling` bullet names the binding section, latest round | ✅ met |
| AC-1.7 | `Open` bullet: `none` for empty; `<n> open` + Blocker/Major IDs + "(Minors: see §3)" for over-capacity | ✅ met |
| AC-1.8 | `On conflict` bullet + `agents/reviewer.md:94–96` (proceed on authoritative, add a finding, never stop) | ✅ met |
| AC-2.1 | reviewer, increment, release-manager, product-owner+next-steps each state first read + read-on condition | ✅ met |
| AC-2.2 | `agents/reviewer.md:91–93` — "confirm each open finding… always earns a full read of the body" | ✅ met |
| AC-2.3 | evidence Entry 2 (29/85 lines) + Entry 3 (22/101) bounded first reads | ✅ met |
| AC-2.4 | evidence negative-case-first, both consumer pairs | ✅ met |
| AC-3.1 | spec/plan/release blocks same shape (lead + 5 bullets) | ✅ met |
| AC-3.2 | Verified against `_parse_spec`/`_parse_plan`/`_parse_qa`/`_status`/`_release_version`: no `##`, no pipe row added; `_release_version` (272) first `\|…\*\*Version\*\*…\|` still the header row (release block uses `` `Version` `` in backticks). `_parse_qa`'s pre-existing `Spec ID` drift (defect 2) is unchanged — not a regression. | ✅ met |
| AC-3.3 | Each block = 6 rendered lines (≤12), comments excluded; grep-confirmed | ✅ met |
| NFR-1 | Minor bump `0.5.0→0.6.0`; nothing protected renamed/removed/reordered; parser-invisible by construction | ✅ met — additive, no coordinated release needed |
| NFR-2 | Zero new skills/agents/lenses/template files (diff adds none); surface enumerated in README | ✅ met |
| NFR-3 | Each template's HTML comment (overwrite rule) + visible block (reader contract, conflict precedence) | ✅ met — distributed differently from plan prose, intent satisfied |
| NFR-4 | README + evidence: "**No token or byte saving is claimed**"; only a per-fixture bounded-read ratio, labelled not-a-measurement | ✅ met |
| NFR-5 | Old-shape/empty/stale/contradictory all degrade to body; no gate blocks on the block | ✅ met |

**Library lens (§1/§2/§4):** §1 — the block is an intentional, minimal addition to the consumed contract, deliberately parser-invisible; no accidental new protected structure. §2 — semver effect is explicit and correct (minor, backward-compatible, no protected heading/column/ID renamed; `marketplace.json` carries no second version, so the single-version rule holds). §4 — contract clarity satisfied in-template via the HTML comment + bullets, no external doc required. §3 N/A.

## 5. What Was Checked

- [x] Correctness: every Must AC (US-1, US-2) and Should AC (US-3) traces to implementing code
- [x] The single biggest risk — parser safety — re-verified against `artifacts.py` source directly, not from evidence; all three A4 conditions hold by construction
- [x] Edge cases: empty block (`none`), over-capacity block, old-shape files, stale/contradictory block — all covered by AC-1.7/1.8/2.4/NFR-5
- [x] Compat surfaces: `/spark` router greps the header pipe row (first in file, block mirrors it anyway) — no mis-route; QA bug-IDs are `B<n>`, matching the qa block's `<B..>` placeholder
- [x] Security: N/A (lens off, no runtime/data/network); no secrets in diff
- [x] Tests: dogfood evidence is the sanctioned substitute (constitution §4); negative-case-first honoured; self-contained without the external fixtures
- [x] Readability: blocks consistent across five templates; artifact-specific `Open`/`Verdict`-vs-`Summary` adaptations each make sense
- [x] Constitution non-negotiables: no silent breaking change; optional-integration degrade-to-silence preserved; version bumped

## 6. Verdict

This is a careful, boring-in-the-best-way diff that does exactly what its spec and plan promise and nothing more. The load-bearing claim — that the Handoff block is structurally invisible to the `aspark-graph` parser with no version handshake — I re-verified line-by-line against the actual parser source, and it holds by construction, not by discipline: the block carries no `##` heading and no pipe `Status`/`Version` row, so `_status`, `_release_version`, `_section` and `_first_table` cannot see it. Every Must AC traces to implementing code, the minor version bump is the correct semver call, and the honesty constraint (NFR-4) is respected in both the README and the evidence. The only findings are two Nits in the feature's own `.spark/` prose (an approximate line-cite and a five-vs-six field count) that gate nothing. **PASS** — `/demo-day` may proceed.

---

## ✅ REVIEW GATE

*All boxes checked → `/demo-day` may start. Any box open → back to `/increment`.*

- [x] No open Blocker findings
- [x] No open Major findings (or explicitly waived by the user, with reason recorded here)
- [x] Every Must AC traces to implementing code; no constitution non-negotiable violated
- [x] All plan deviations documented and accepted (two benign distribution differences, noted)
- [x] Test suite runs green — N/A; dogfood evidence (constitution §4) present, negative-case-first, self-contained
- [x] Status set to `passed`

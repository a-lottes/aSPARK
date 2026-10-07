# Campaigns — one goal, one budget, run in iterations

A **campaign** is a second way of working next to the feature loop. A feature answers
"is this story done?". A campaign answers "has this measurable end state been reached?" —
for example "every slice is parity-green" — and it runs in iterations until it has, or
until the budget or a stop rule ends it. The goal is approved by the **user**; the agent
only iterates inside it.

A **campaign kind** is one file in this directory: a ready goal shape with roles, stop rules
and budget defaults. Like a lens, a kind is **knowledge, not a new team member**: adding one
never edits an agent or a skill. Today one kind exists, [`migration-campaign`](migration-campaign.md).

> **Status, stated plainly.** The need for campaigns is *anticipated, not observed*. There is one
> kind. Budgets and stop rules are **followed by the agent, not enforced by Core** — Core is
> Markdown with no runtime; optional enforcement is `aspark-guard`'s concern. Effectiveness is
> unmeasured.

## The contract (what every kind file guarantees)

Frontmatter declares all seven keys. A file missing any of them is reported as **malformed,
naming the key**, and is not used.
**Best effort, not a guarantee:** this check is prompt material. In QA a kind with a key removed was reported malformed in 13 of 19 sessions (`stop-rules` 4 of 4, `roles` 2 of 5, `phases` 4 of 7); a miss said the kind "has all seven keys". The contribution review is the real gate for a new kind.

| Key | Meaning |
|---|---|
| `name` | The kind's name. Equals the file name without `.md`. |
| `trigger` | What kind of request this kind is for, in one line. |
| `goal-kind` | The shape of the machine-decidable goal, in one line. |
| `roles` | The role briefs the kind defines (they run as fresh subagents; no `agents/*.md`). |
| `stop-rules` | The kind's **additions** to the four Core rules in `templates/campaign.md`. |
| `budget-defaults` | Default iteration and token budget; each labelled unmeasured and overridable. |
| `phases` | Which SPARK phases the kind acts in: `specify`, `plan`, `act`, `review`. |

Below the frontmatter a kind carries whatever the format in [`templates/campaign.md`](../templates/campaign.md)
needs filled in for that kind. It may **tighten** Core's stop rules and budget floors; it may not
loosen them, grant tools, waive a gate or veto condition, or imply approval.

## Discovery is a rule, not a list

A kind is *every `campaigns/*.md` file except this `README.md`, judged by its own frontmatter*.
No skill or agent contains a list of kind names; docs name kinds only as examples. A new kind therefore reaches every
phase it declares in `phases` by adding one file — and only that file.

## Instantiating a campaign

**Start with `/campaign <name> [kind]`.** It reads the kinds and the template from the plugin itself (no path to name), asks only what the kind leaves open and writes one draft: Status `draft`, approval blank, veto record blank, no commit. It is instructed to refuse an undecidable goal, several goals or a set of stories, a goal that fits no kind, an existing name, a malformed kind and a name that is not kebab-case, and never to approve, run or commit. The hand-start below stays valid.

**Best effort, not a guarantee:** these checks are prompt material. Measured in development, five fresh sessions each (`/demo-day` re-measures): a kind with a key removed was reported malformed and not used 1 of 5 at `/demo-day` round 1 when the goal came in the same line as the command (the check sat at the kind step, and the agent went on to the goal), then 5 of 5 after the key check was moved to open the reply and gate the write; the draft state held 5 of 5; an undecidable goal was refused 5 of 5; several goals 5 of 5; an existing instance was named 4 of 5 at first (one session claimed it did not exist, and a review run showed that miss would then have overwritten it; the existence check now reads the instance file itself and held 5 of 5 with the goal given up front). A first draft creates `.spark/campaigns/`, which gives `aspark-graph` one phantom node and the `/spark` behaviour below.

1. Outside a skill the agent cannot resolve `${CLAUDE_PLUGIN_ROOT}`: **name the plugin folder in your prompt** — the folder of the installed aSPARK plugin, the one that contains `campaigns/` and `templates/` (under `~/.claude/plugins/`). If the agent cannot find it, it asks you and never invents a structure. Then copy `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md` to
   **`.spark/campaigns/<campaign-name>/campaign.md`**, then append the chosen kind's body (below its frontmatter) as §8 "Kind-specific", with the slice list and parity check filled in under it; the kind's stop rules replace the `SR-5…` placeholder row in §4. The copy is **frozen at approval**: the user
   approves exactly the text that governs the run, and a later plugin update cannot change it.
2. Fill every element. **Any blank element means the campaign is not startable.**
3. The user records goal approval (their own statement, transcribed by them or, on their instruction, by the agent) and sets `approved`.

Naming rules, because [`aspark-graph`](../tools/README.md) reads `.spark/`:
- The file is always called `campaign.md`. No other stem may contain `spec`, `plan`, `review`,
  `qa` or `release` — the graph reports those as near-misses.
- All campaigns share **one reserved directory**, `.spark/campaigns/`. `campaigns` is therefore a
  reserved name under `.spark/`: a feature folder must not use it.
- The graph does not index a campaign. It sees one extra directory and skips its files; that is
  recorded, not fixed here.

## Activation, and where it stays silent

- **Activation (this increment):** only an explicit user instruction that **names the instance**,
  for example "run the campaign at `.spark/campaigns/<name>/campaign.md`". Nothing switches a
  campaign on by itself and no ceremony proposes one yet.
- **Silence:** a repo without `.spark/campaigns/` sees no change in any ceremony — no notice,
  no question, no mention. The loop ceremonies have no campaign logic yet; routing and the
  standing rule for ordinary feature loops arrive in a later increment. Observed meanwhile, in single non-deterministic runs (not designed): in a repo
  whose only `.spark/` subdirectory is `campaigns`, `/spark` reports there is no feature to resume and describes the halted campaign, and `/next-steps` lists it; `/spark campaigns` asks for another name.
- **Hand-run:** the user names the instance; the agent reads it, refuses without recorded goal
  approval, iterates one step at a time inside the budget, logs a checkpoint after each iteration
  (`CK-<n>`), and sets `halted` and escalates when a stop rule trips. The agent may set only
  `running` (at the start, and after a halt once its cause is resolved and recorded in a `CK-` entry —
  unless the tripped rule reserves the decision to the user, as `SR-5` does; a goal, threshold or budget
  change still needs the whole spec approved afresh) and `halted`.
- **Known limits:** the freeze is a stop only if the agent notices an edit to the approved sections; an edit amended into the approval commit was **not** noticed in QA. Nothing detects it. Overlapping slice paths are not flagged. The `SR-9` trip on a real diff spanning two slices could not be produced honestly in QA (the Migrator commits only its own paths), so that half of the rule is not verified live.
- **Without `aspark-guard`:** nothing changes and nothing is reported. The rules are instructions.
- **No skill reads a campaign definition from the target project.** Only the instantiated
  `campaign.md` is written there.

## Adding a campaign kind

Open an [enhancement issue](../../../issues/new?template=enhancement.yml) or a PR, as for lenses.
Copy [`migration-campaign.md`](migration-campaign.md) as your model and keep the file within its size
cap. A kind is ready when it can answer: what is the **decidable** goal, what observable and
verifier confirm it, which roles it needs and which output each produces, what it adds to the
stop rules, and **where it stays silent**. A goal that can only be judged as "looks good" is not a
campaign — it belongs in the feature loop. See [`CONTRIBUTING.md`](../CONTRIBUTING.md).

---
name: campaign
description: >
  Start a campaign draft: build `.spark/campaigns/<name>/campaign.md` from an
  existing campaign kind. Only when the user types /campaign.
argument-hint: <name> [kind]
disable-model-invocation: true
---

# /campaign — Start a campaign draft

Walking skeleton: proves path expansion and the single write. Not the final text.

## Steps

1. **Kinds.** Glob `${CLAUDE_PLUGIN_ROOT}/campaigns/*.md`. A kind is every file
   there except `README.md`. Use the kind the user named.
2. **Template.** Read `${CLAUDE_PLUGIN_ROOT}/templates/campaign.md`.
3. **Write once.** Copy the template, append the kind's body below its
   frontmatter as `## 8. Kind-specific`, set Status `draft`, and write
   `.spark/campaigns/<name>/campaign.md`. Write no other file.

# Criteria for Tool Preferences

Reference only — load when deciding whether to update `<state_root>/preferences.md`
or whether to recommend a different tool.

## When to add to Stack

**Immediate:**

- User explicitly says they use tool X
- User asks for help with a specific tool they already chose
- The active project already standardizes on a tool

**After a pattern:**

- User repeatedly chooses the same tool for a category
- User shows muscle memory (shortcuts, idioms, mental model)

## When to suggest alternatives

**Suggest a switch when:**

- The current tool makes the task significantly harder
- The user is hitting a clear limitation they care about
- The user asked "is there a better way?"
- A different tool would save hours, not minutes, after switching cost
- Open To includes traits such as "new tools welcome" or "suggest freely"

**Keep the current tool when:**

- It already works for the task
- The user wants to finish, not evaluate
- Open To prefers stability or "ask first"
- Switching cost outweighs the benefit
- The choice is a team standard the user is not free to change alone

## How to write entries

**Stack examples:**

- `design: Figma`
- `db: Pocketbase for MVPs, Postgres for scale`
- `deploy: Docker + self-hosted`
- `notes: Obsidian`

**Preferences examples:**

- `MVPs: minimal stack, ship fast`
- `prefers CLI over GUI`
- `self-hosted when possible`
- `free tiers first, pay when needed`

**Open To examples:**

- `loves trying new tools`
- `suggest alternatives freely`
- `only if major improvement`
- `ask before suggesting`
- `skeptical of new tools; prove value first`

**Avoid-list examples:**

- `Jira (process overhead)`
- `AWS complexity for solo MVPs`
- `subscription fatigue`
- `Electron apps when a native or CLI option exists`

## Handling unknown tools

When the user names a tool you do not know:

1. Acknowledge the unfamiliar name
2. Research quickly or ask one clarifying question
3. Learn enough to help with the current task
4. Add to Stack only after regular use, not after a single mention

## Key principle

Track preferences to **help choose defaults** while leaving full capability
available. Empty Stack means no recorded default yet — propose from the task
first, then offer to save only what the user confirms. Prefer concrete keep-or-
switch heuristics over stop-only warnings.

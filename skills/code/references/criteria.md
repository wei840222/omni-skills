# Criteria for storing preferences

Reference for when to save user preferences to `<state_root>/memory.md`.

## When to save (user must request)

Save only when the user explicitly asks:

- "Remember that I prefer X"
- "Always do Y from now on"
- "Save this preference"
- "Remember that I like Z"

## Exclude from saving

- Project-only requirements that apply to a single checkout
- One-off requests ("just this once")
- Temporary preferences
- Secrets, tokens, or private credentials (use placeholders instead)

## What to save

**Preferences**

- Coding style preferences the user stated
- Tools or frameworks the user prefers
- Patterns the user explicitly likes

**Excluded patterns**

- Approaches the user marks as out of scope
- Patterns the user asked to exclude

## Format in memory.md

```markdown
## Preferences
- prefers TypeScript over JavaScript
- likes detailed comments
- wants tests for all functions

## Excluded
- no class-based React components
- keep styles external
```

## Important

- Only save what the user explicitly asked to save
- Ask before saving when the request is ambiguous: "Should I remember this preference?"
- Keep skill package files immutable; only write under the resolved `<state_root>`

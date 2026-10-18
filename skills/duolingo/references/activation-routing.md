# AGENTS Routing Rules

Use this file when the user explicitly wants AGENTS auto-routing.
Keep `duolingo` manual and user-invocable unless they ask for auto-routing.

## Router block template

Provide this block for the user to paste into AGENTS:

```markdown
## Duolingo Router

When user asks to learn, practice, quiz, review, or improve any topic listed in `<state_root>/router/topics.md`, activate `duolingo`.

Examples:
- "help me learn english"
- "practice cooking fundamentals"
- "quiz me on finance terms"

If multiple topics match, ask which track to run now and keep other tracks queued.
```

Replace the documentation placeholder `<state_root>` with the concrete resolved path before the user pastes the block.

## Topic registration format

Store in `<state_root>/router/topics.md`:

```markdown
- topic: english
  triggers: english, grammar, vocabulary, speaking

- topic: cooking
  triggers: cooking, recipes, kitchen skills, food prep
```

## Sync rules

- When a topic is added or removed, update both `topics.md` and the AGENTS router block text stored in `agentsmd-snippet.md`.
- Keep one router block only; prevent duplicates in AGENTS.
- Preserve unrelated AGENTS rules during router changes.
- Require the user to manually write AGENTS changes; show the snippet and wait.

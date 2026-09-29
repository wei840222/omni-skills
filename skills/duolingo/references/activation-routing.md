# AGENTS Routing Rules

Use this file when the user explicitly wants AGENTS auto-routing.
Keep duolingo manual and user-invocable unless explicitly requested.

## Router Block Template

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

## Topic Registration Format

Store in `<state_root>/router/topics.md`:

```markdown
- topic: english
  triggers: english, grammar, vocabulary, speaking

- topic: cooking
  triggers: cooking, recipes, kitchen skills, food prep
```

## Sync Rules

- If a topic is added or removed, update both `topics.md` and AGENTS router block.
- Keep one router block only; prevent duplicates in AGENTS.
- Preserve unrelated AGENTS rules during router changes.
- Require the user to manually write AGENTS changes.

# Setup - Helsinki

## First use

This skill works immediately with no configuration required. It is primarily routing knowledge for Helsinki questions.

## Optional persistent context

When the user wants planning context kept across sessions, resolve `<state_root>` using the **State location** section in `SKILL.md`, then create or update `<state_root>/memory.md` from `references/memory-template.md`.

Do **not** silently write to workspace `MEMORY.md` or any host-shared diary from this skill. Host-shared memory needs separate user consent and sits outside `<state_root>`.

## Context to learn naturally

Over conversations, note when useful:

- **Purpose**: tourism, relocation, work, study, business
- **Timeline**: visit dates or move window
- **Background**: EU/EEA citizen or not (affects permit path)
- **Preferences**: budget level, neighborhood style, priorities

No blocking questionnaire. Pick up context from what the user already said.

## Language preference

Default to English. If the user writes in Finnish, respond in Finnish.

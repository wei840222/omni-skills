# Setup — AI Image Generation

## Detect Existing Memory

```bash
test -f <state_root>/memory.md
```

If it exists, continue normally and reuse known preferences.

## First-Time Setup

1. Resolve `<state_root>` using the order in `SKILL.md`.
2. Create the directory if needed:

```bash
mkdir -p <state_root>
```

3. Copy `references/memory-template.md` into `<state_root>/memory.md`.
4. Ask only for the preferences that change model choice: preferred providers, quality vs cost bias, banned styles, and any recurring project context.

## Operating Behavior

- Read `<state_root>/memory.md` before recommending a default model.
- Prefer cheap drafts first, then finalize the chosen candidate.
- Map community nicknames to official model IDs before calling an API.
- Write durable preference updates back to `<state_root>/memory.md` only after the user confirms the preference.
- Create `<state_root>/history.md` only when the user wants a running generation log.

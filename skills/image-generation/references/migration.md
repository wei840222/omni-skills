# Migration Guide

Read this guide when upgrading from older published versions.

## What Changed

- State paths moved from hard-coded Clawic directories to portable `<state_root>/`.
- Supporting docs now live under `references/`.
- Community nicknames still resolve to official provider model IDs before API calls.

## Migration Steps

1. Create backup:

```bash
cp <state_root>/memory.md <state_root>/memory.md.bak
```

2. Add the new sections from `memory-template.md`.
3. Copy old content into the closest new section:
   - provider preferences → `## Preferences`
   - project notes → `## Project Context`
   - reusable prompts → `## Winning Recipes`
4. Update any old `openai.md` references to `gpt-image.md`.

## Post-Migration Verification

- [ ] `<state_root>/memory.md` exists and keeps prior preferences
- [ ] Any old `openai.md` references now point to `gpt-image.md`
- [ ] No data was deleted without explicit user confirmation
- [ ] Generation workflows still run with current model IDs

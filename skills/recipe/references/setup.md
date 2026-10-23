# Setup — recipe

First-use and migration only. Resolve `<state_root>` using the State location rules in `SKILL.md` before creating anything.

## Create on first durable need

```text
<state_root>/recipe/
  config.yaml
  memory.md
  index.md
  recipes/
  made/
```

Do not create empty folders “just in case”. Create a file when the first write needs it.

## Migration

Legacy locations that may hold a prior collection:

- `~/Clawic/data/recipe/`
- `~/clawic/recipe/`
- `~/recipes/`

Move into `<state_root>/recipe/` only when the user asks. Say in one line what moved and from where. Never merge split copies silently.

## Shared boxes

This skill may also need:

- `<state_root>/health/profile.md`
- `<state_root>/contacts/contacts.md`
- `<state_root>/projects/`
- `<state_root>/profile.yaml`

Create a shared box only when writing the first owned row; otherwise read-through is enough.

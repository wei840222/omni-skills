# Memory Setup — Golf

## Initial Setup

On first use, create the state directory and state files:
```bash
mkdir -p <state_root>/archive
touch <state_root>/memory.md
touch <state_root>/rounds.md
touch <state_root>/courses.md
```

Replace `<state_root>` with the resolved state location from SKILL.md before executing.

## Templates

Copy the appropriate template from `assets/golf-data-templates.md` into each state file:

- `<state_root>/memory.md` — use the "memory.md Template" section
- `<state_root>/rounds.md` — use the "rounds.md Template" section
- `<state_root>/courses.md` — use the "courses.md Template" section

## Archive

When archiving a past season, move old data to `<state_root>/archive/` using the naming convention in `assets/golf-data-templates.md`.

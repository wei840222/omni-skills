# Memory Setup — Golf

## Initial Setup

After the user confirms that golf records should be saved, create only the required state file:
```bash
mkdir -p <state_root>
touch <state_root>/memory.md
```

Replace `<state_root>` with the resolved state location from SKILL.md before executing.

Create optional state files after the user asks to save the relevant records:
- `<state_root>/rounds.md` — create when user logs their first round
- `<state_root>/courses.md` — create when user saves a course
- `<state_root>/archive/` — create when user archives past season data

## Templates

Copy the appropriate template from `assets/golf-data-templates.md` into each state file when creating it:

- `<state_root>/memory.md` — use the "memory.md Template" section
- `<state_root>/rounds.md` — use the "rounds.md Template" section
- `<state_root>/courses.md` — use the "courses.md Template" section

## Archive

When archiving a past season, move old data to `<state_root>/archive/` using the naming convention in `assets/golf-data-templates.md`.

# Memory Setup — Couple

## Initial Setup

Resolve `<state_root>` using the State location rules in `SKILL.md`, then create the archive directory on first use:

```bash
mkdir -p <state_root>/archive
```

Seed files from `assets/data-templates.md` only when the corresponding path does not already exist:

- `<state_root>/memory.md`
- `<state_root>/timeline.md`
- `<state_root>/ideas.md`

Never overwrite existing user state. Keep partner details limited to what the user says the partner shared directly. Do not store location traces, message logs, credentials, health, financial, or intimate data.

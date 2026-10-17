# Memory Setup — Job Search

Load this file on first use or when `<state_root>` files are missing.

## Initial Setup

```bash
mkdir -p <state_root>/materials <state_root>/archive
touch <state_root>/memory.md <state_root>/applications.md <state_root>/companies.md
```

Populate those files from the templates in `assets/data-templates.md`.

## Recovery

- If a previous vendor-specific data directory still holds live hunt records, copy it into the resolved `<state_root>` only after the user confirms; do not invent a silent migration.
- Keep closed applications in `archive/`; do not delete history to "clean up" the pipeline.

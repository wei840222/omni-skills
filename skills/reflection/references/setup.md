# Setup — Reflection

## First activation

On first use, with explicit user approval before writing:

1. Resolve `<state_root>` using the State location rules in `SKILL.md`.
2. Create the directory tree when durable logging is wanted:

```bash
mkdir -p <state_root>/archive
```

3. Seed files from `assets/data-templates.md`:
   - `<state_root>/memory.md`
   - `<state_root>/reflections.md`
   - `<state_root>/patterns.md`
4. Optional host memory pointer (only if the user already maintains a workspace
   diary and asks for it): record that reflection state lives at the resolved
   `<state_root>/`, without inventing a second root.

Do not write the literal string `<state_root>` to disk. If legacy data exists
only at `~/Clawic/data/reflection/`, propose copy → validate → cutover and wait.

## Optional heartbeat check

If the host already uses a heartbeat monitor and the user wants a light scan,
add a short check that asks only:

1. Is there a pending correction to log?
2. Has the pattern threshold been reached (≥5 reflections or category ≥3)?
3. Is the weekly review due?

Handle only when one of those is true; otherwise continue.

## Configuration

No external services. All durable state lives under `<state_root>/`.

Optional preferences in `<state_root>/memory.md`:

```markdown
## Preferences
- review_day: Sunday
- archive_threshold: 20
- reflection_depth: standard
```

## Status fields

Track in `<state_root>/memory.md`:

- `streak_days` — days without repeated mistake
- `total_reflections` — count by category
- `patterns_active` / `patterns_resolved`
- `last_review` — date of last weekly review

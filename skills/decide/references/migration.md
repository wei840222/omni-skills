# Migration Guide - Decide

## v1.0.1 Decision Logging Update

This update keeps the same home folder, `<state_root>/`, but changes the model from loose preference tracking to structured decision memory.

### Before

- `<state_root>/memory.md`
- local notes mixed across confidence or exception concepts
- no formal setup flow for workspace AGENTS and SOUL files

### After

- `<state_root>/memory.md`
- `<state_root>/decisions.md`
- `<state_root>/domains/`
- packaged guides stay in the skill: `components.md`, `confidence.md`, `exceptions.md`, `setup.md`, `memory-template.md`

## Safe Migration

1. Create the new local files without deleting anything:
```bash
mkdir -p <state_root>/domains
touch <state_root>/decisions.md
```

2. Keep the existing `<state_root>/memory.md` file exactly as it is.

3. Move durable decision rules and always-ask boundaries into the matching sections of the new memory template.

4. Move individual examples, choices, and outcomes into `<state_root>/decisions.md`.

5. If old local notes are specific to one project, client, or technical area, place them in `<state_root>/domains/<domain>.md`.

6. Apply any AGENTS or SOUL additions as small snippets only. Retain existing sections and apply edits selectively.

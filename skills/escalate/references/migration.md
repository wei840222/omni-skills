# Migration Guide - Escalate

## v1.0.1 Setup and Memory Update

This update keeps the same home folder, `<state_root>/escalate/`, but clarifies what belongs in the user's live memory versus the packaged skill guides.

### Before

- `<state_root>/escalate/memory.md`
- possible local notes mixed with `boundaries.md` or `patterns.md`
- no formal setup flow for the workspace AGENTS and SOUL files

### After

- `<state_root>/escalate/memory.md`
- `<state_root>/escalate/decisions.md`
- `<state_root>/escalate/domains/`
- packaged guides stay in the skill: `boundaries.md`, `patterns.md`, `setup.md`, `memory-template.md`

## Safe Migration

1. Create the new local files without deleting anything:
```bash
mkdir -p <state_root>/escalate/domains
touch <state_root>/escalate/decisions.md
```

2. Keep the existing `<state_root>/escalate/memory.md` file exactly as it is.

3. If old escalation notes live in loose sections or ad-hoc files, copy durable boundaries into the matching sections in the new memory template.

4. Move recent examples, corrections, and trust adjustments into `<state_root>/escalate/decisions.md`.

5. If old local files named `boundaries.md` or `patterns.md` exist inside `<state_root>/escalate/`, keep them for reference and merge them gradually. Retain them unless the user explicitly asks for cleanup.

6. Apply any workspace AGENTS or SOUL additions as small snippets only. Only append to existing sections.

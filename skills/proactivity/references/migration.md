# Migration Guide - Proactivity

## Resolve state root first

Follow `SKILL.md` **State location** before creating or moving files.

Legacy path: if data still lives at `~/Clawic/data/proactivity/`, move it into the
resolved `<state_root>/proactivity/` and state the move in one line. Do not keep
writing to the legacy Clawic path.

## v1.0.1 Architecture Update

This update keeps the same logical home folder, `<state_root>/proactivity/`, and
preserves existing files. The new version adds active-state files for recovery
and follow-through.

### Before

- `<state_root>/proactivity/memory.md`
- `<state_root>/proactivity/domains/`
- `<state_root>/proactivity/patterns.md`
- `<state_root>/proactivity/log.md`

### After

- `<state_root>/proactivity/memory.md`
- `<state_root>/proactivity/session-state.md`
- `<state_root>/proactivity/heartbeat.md`
- `<state_root>/proactivity/patterns.md`
- `<state_root>/proactivity/log.md`
- `<state_root>/proactivity/domains/`
- `<state_root>/proactivity/memory/working-buffer.md`

## Safe Migration

1. Create the new files without deleting the old ones:

```bash
mkdir -p "${STATE_ROOT}/proactivity/memory"
touch "${STATE_ROOT}/proactivity/session-state.md"
touch "${STATE_ROOT}/proactivity/heartbeat.md"
touch "${STATE_ROOT}/proactivity/memory/working-buffer.md"
```

Replace `${STATE_ROOT}` with the resolved `<state_root>` path.

2. Keep `memory.md`, `patterns.md`, and `log.md` exactly as they are.

3. If old proactive rules live in free-form notes, copy them into the new sections in `memory.md`.

4. Start writing only live task state to session state and working buffer.

5. Preserve all legacy files unless the user explicitly asks for cleanup later.

# Setup — iCloud

Read on first activation when `<state_root>/memory.md` is missing, `pyicloud`
is not importable, or the user has not confirmed persistence preferences.

## Operating attitude

- Answer the user request first, then harden execution.
- Prefer safe defaults over fast risky actions.
- Keep each step verifiable and reversible.

## First activation

1. Confirm objective: Find My, Drive, Photos, or mixed operations.
2. Confirm whether local operational notes are allowed.
3. If notes are approved, resolve `<state_root>` (see `SKILL.md` State location)
   and create the minimal structure:

```bash
mkdir -p <state_root>
touch <state_root>/{memory.md,operations-log.md,device-map.md,drive-map.md,safety-events.md}
chmod 700 <state_root>
chmod 600 <state_root>/{memory.md,operations-log.md,device-map.md,drive-map.md,safety-events.md}
```

Replace `<state_root>` with the resolved absolute path before running shell
commands. Never create a directory literally named `<state_root>`.

4. If `memory.md` is empty, initialize from `assets/memory-template.md`.
5. Ensure Python ≥ 3.10, then install and verify the pinned client:

```bash
python3 -m pip install --user "pyicloud==2026.10.1"
python3 - <<'PY'
from pyicloud import PyiCloudService
print("pyicloud import OK")
PY
```

6. Authenticate with the local prompt flow in `references/auth-session.md`.

## Integration preferences to capture

- Allowed operation domains: `findmy` | `drive` | `photos`
- Confirmation strictness for risky actions: `strict` | `standard`
- Session behavior: `persistent` | `session_only`

## Runtime defaults

- Default to read-only discovery.
- Require explicit confirmation before risky actions.
- Verify post-state after every write.

## Session-only mode

If the user declines persistence:

- Do not create or update files under `<state_root>/`.
- Keep all context in the current session output only.

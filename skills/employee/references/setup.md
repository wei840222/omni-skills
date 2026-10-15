# Setup

## Initial Setup

```bash
mkdir -p <state_root>/employees <state_root>/shared
echo '{"employees":{},"lastUpdated":null}' > <state_root>/registry.json
touch <state_root>/shared/protocols.md
```

Resolve `<state_root>` with the State location section in `SKILL.md` before
creating directories. Do not write the literal placeholder string to disk.

## Migration from legacy Clawic paths

If durable employee data still lives only under `~/Clawic/data/employee/`:

1. Resolve the target `<state_root>` for this invocation.
2. Ask the user to confirm a copy into that root.
3. Copy `registry.json`, `employees/`, and `shared/` without deleting the source
   until the user confirms cutover.
4. Report the new root in one line.

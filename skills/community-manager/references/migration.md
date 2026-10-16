# Migration from legacy Clawic paths

## Legacy location

Older installs may keep notes only at `~/Clawic/data/community-manager/`.

## Cutover procedure

1. Resolve the modern `<state_root>` candidates from `SKILL.md`.
2. If legacy Clawic data exists and no modern candidate exists, propose:

   - inventory of files to copy
   - validation that no credentials or PII are moved blindly
   - target `<workspace>/community-manager/` (or user-chosen root)
3. Wait for explicit user confirmation before copying or deleting anything.
4. After a successful copy, keep the legacy tree read-only until the user
   confirms cutover; do not auto-delete.
5. Update `memory.md` with the migration date and source path.

Never write the literal string `<state_root>` into migrated files. Expand paths
to the concrete directory chosen for the invocation.

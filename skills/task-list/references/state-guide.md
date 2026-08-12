# Persistent state guide

Read this file before creating, migrating, or updating task-list state.

## State inventory

Create only files needed by the user’s requested continuity:

```text
<state_root>/
├── memory.md     # preferences and durable task-list conventions
├── inbox.md      # optional raw captures
├── tasks.md      # optional active task records
├── projects.md   # optional finite outcomes and next actions
├── areas.md      # optional ongoing responsibilities
├── recurring.md  # optional recurrence rules
├── waiting.md    # optional blocked or delegated work
└── log.md        # optional meaningful state changes
```

Use one file per record type and create it only when that record type is needed. Copy its format from `assets/task-file-templates.md`.

## Consent and updates

Create persistent state only after the user requests continuity. A direct request to add or update a named task authorizes that precise non-destructive change. Confirm destructive, historical, or bulk changes before writing. Read the target file before editing, and report the file plus the exact operation afterwards.

## Migration

Treat older task-list directories as migration sources. Inventory the source, propose copy-and-verify steps, wait for explicit approval, and retain the source until cutover is confirmed. Keep multiple candidate roots separate; the state resolver selects one root and does not merge them.

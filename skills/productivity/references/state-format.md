# State format and maintenance

Read this file only when the user asks to persist, migrate, or review productivity notes.

## Minimal state

Create only the files that a requested feature needs:

```text
<state_root>/
├── memory.md        # current preferences, constraints, and calibration pairs
├── tasks.md         # optional actionable work
├── projects.md      # optional active projects and outcomes
└── reviews/YYYY.md  # optional dated weekly or monthly review entries
```

`<state_root>/memory.md` may contain only durable, user-confirmed preferences and constraints. Preserve user wording for sensitive constraints; keep enough detail to plan and no more.

## Write rules

- Obtain the user's request before creating, changing, moving, or deleting state.
- Read the target file before editing and report the exact write afterward.
- Record estimate/actual pairs as `date | work | estimate | actual` and calculate a calibration ratio only from comparable completed work.
- Keep task rows actionable: outcome, next physical action, due date if known, and status.
- Use a dated review entry for decisions to defer, cancel, or renegotiate rather than silently erasing history.
- Store references to a secret instead of a secret itself, for example `env:CALENDAR_TOKEN`.

## Migration

Treat an older path as a migration source, never as an active fallback. Inventory it first, propose a copy-and-verify plan, wait for explicit confirmation, and retain the source until the user confirms the cutover. Do not combine state from several candidate roots automatically.

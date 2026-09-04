# HomePod state-note template

After resolving `<state_root>` and receiving permission to write notes, create `<state_root>/memory.md` only when durable state is needed.

```markdown
# HomePod notes

## Status
status: ongoing
last: YYYY-MM-DD
integration: pending | complete | paused | no-follow-up

## Activation and control boundaries
- Activate for:
- Explicit-request-only for:
- Protected targets:

## Active incidents
- Incident:
  - Reproduction:
  - Observed behavior:
  - Probable layer:
  - Next validation:

## Confirmed fixes
- Fix:
  - Scope:
  - Validation:
  - Date:
```

Use `<state_root>/homes.md` for models, home-hub role, room mapping, and network context. Use `<state_root>/automation-log.md` for trigger, condition, expected action, actual action, latency, and validation results. Use `<state_root>/network-notes.md` for reproducible network observations.

Keep entries specific and testable. Update `last` after a meaningful session, and retain both failed attempts and successful rollback evidence.

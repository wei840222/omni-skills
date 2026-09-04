# Persistent-state template

Use this reference after the user approves persistent context. Create `<state_root>/memory.md` with this structure:

```markdown
# Home Server Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
- Hardware profile and host OS
- Core services and exposure policy
- Stated reliability and security priorities

## Service Inventory
- Service name -> purpose -> data path -> exposure level
- Owner and maintenance cadence

## Backup Coverage
- What is backed up
- Where backups are stored
- Last restore test date

## Notes
- Repeated failure patterns
- Proven recovery procedures
- Preferences explicitly provided by the user

---
*Updated: YYYY-MM-DD*
```

| Status | Meaning | Operating response |
|---|---|---|
| `ongoing` | Context is still evolving | Capture only reusable information from normal work. |
| `complete` | A stable environment model exists | Operate from the recorded assumptions and confirm changes. |
| `paused` | The user wants less onboarding discussion | Limit setup questions to explicit requests. |
| `do_not_ask` | The user declined setup discovery | Use only explicit requests for persistent-state changes. |

Use natural-language observations rather than exposed configuration keys. Update `last` when context changes, promote repeated incidents into prevention notes, and retain prior context unless the user approves a deletion or replacement.

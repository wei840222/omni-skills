# Memory Template - Tuya Smart

Create `<state_root>/memory.md` with this structure:

```markdown
# Tuya Smart Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | skip_prompts

## Activation Preferences
- When this skill should auto-activate
- When this skill should stay silent
- Proactive vs explicit-only behavior

## Environment Context
- Project name and data center
- OpenAPI endpoint in use
- Account-linking model in use
- Risk mode (read-only, guarded writes, apply)

## Device Control Context
- Device groups and critical devices
- Known command codes and constraints
- Verification checks per device category

## Automation Constraints
- Rollout ordering and blast-radius limits
- Retry policy and halt conditions
- Rollback owner and rollback criteria

## Open Risks
- Auth/signing reliability risk
- Account-linking consistency risk
- Device state drift risk

## Notes
- Durable decisions and validated fixes

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context still evolving | Keep learning environment and control patterns |
| `complete` | Stable operating context | Focus on execution and optimization |
| `paused` | User paused setup expansion | Use existing context and ask only if blocked |
| `skip_prompts` | User wants no setup prompts | Skip setup questions unless explicitly requested |

## File Templates

Create `<state_root>/devices.md`:

```markdown
# Device Registry

## Device Name (device_id)
- Product category:
- Region:
- Capability codes:
- Safety classification:
- Last verified:
```

Create `<state_root>/incidents.md`:

```markdown
# Incident Log

## YYYY-MM-DD HH:MM - Incident
- Symptom:
- Scope affected:
- Root cause hypothesis:
- Mitigation:
- Verification:
```

## Key Principles

- Keep entries concise and operational.
- Record only Tuya-relevant context.
- Store only non-sensitive operational data; exclude raw credentials or unrelated private data.

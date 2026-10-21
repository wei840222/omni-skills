# Odoo Memory Template

Create `<state_root>/memory.md` with this structure when durable notes are first
needed:

```markdown
# Odoo Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Environment
- Instance: production | staging | local
- Companies:
- Odoo version:
- Main modules:

## Operating Rules
- Read/write boundary:
- Approval boundary:
- Preferred interfaces: UI | import | XML-RPC | JSON-RPC | mixed

## Customization Notes
- Custom modules:
- Studio fields:
- Renamed states or workflows:

## Reporting Defaults
- Timezone:
- Currency:
- Standard status filters:
- Preferred output:

## Notes
- Durable context only

---
*Updated: YYYY-MM-DD*
```

## Optional companion templates

### `<state_root>/instances.md`

```markdown
# Odoo Instances

| Name | URL | Environment | Version | Auth lane | Notes |
|------|-----|-------------|---------|-----------|-------|
| prod | https://example.odoo.com | production | 18.0 | browser / env pointer | |
```

### `<state_root>/modules.md`

```markdown
# Odoo Modules and Overrides

- Custom modules:
- Studio fields:
- Renamed states / workflows:
```

### `<state_root>/incidents.md`

```markdown
# Odoo Incidents

## YYYY-MM-DD — short title
- Impact:
- Root cause:
- Recovery:
- Safe default changed:
```

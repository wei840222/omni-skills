# Memory Template — Email Marketing

Create `<state_root>/memory.md` only if the user wants continuity across sessions.

```markdown
# Email Marketing Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
- Brand or product:
- ESP / sending stack:
- Domains in use:
- Auth status (SPF/DKIM/DMARC):
- List size and primary source:
- Main metric:
- Restricted actions:

## Notes
- Approved segments:
- Active sequences:
- Known deliverability issues:
- Compliance constraints:
- Open decisions:

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning context | Gather only what improves email decisions |
| `complete` | Enough context exists | Work normally without re-asking basics |
| `paused` | User does not want more setup | Stop pushing for more detail |

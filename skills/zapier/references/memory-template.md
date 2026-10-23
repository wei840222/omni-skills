# Memory Template — Zapier

Create `<state_root>/memory.md`:

```markdown
# Zapier Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending

## Account
plan: free | professional | team | enterprise
api_access: yes | no
polling_speed: 15min | 2min | 1min

## Connected Apps
<!-- Apps they use frequently -->
- Google Sheets
- Slack
- Salesforce
- (add as discovered)

## Active Zaps
<!-- Zaps they mentioned or created -->
Format: Trigger App → Action App (purpose)

## Common Patterns
<!-- Workflows they use repeatedly -->

## Preferences
complexity: simple | advanced
notifications: slack | email | both
error_handling: alert | silent

## Notes
<!-- Things to remember; secret pointers only -->

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning |
|-------|---------|
| `ongoing` | Still learning their stack |
| `complete` | Know their main workflows |
| `paused` | Do not ask more onboarding questions |

## Key Principles

- Learn apps from context
- Track successful patterns
- Note failed attempts (avoid repeating)
- Update `last` on each use
- Never persist raw API tokens in this file

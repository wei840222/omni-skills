# Memory Template - multi-engine-web-search

Create `<state_root>/memory.md`:

```markdown
# multi-engine-web-search Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending | done | declined

## Activation
mode: always | on_request | mixed
notes: short natural-language explanation

## Engine Priority
1. Google
2. DuckDuckGo
3. Brave
4. Bing

## Blocked Engines
- none

## Search Style
style: speed | balanced | evidence

## Notes
- short user-specific preferences

---
*Updated: YYYY-MM-DD*
```

## Rules

- Keep memory minimal and preference-focused.
- Update `last` whenever preferences change.
- Store only non-sensitive user preferences.
- Never store credentials, private query logs, or personal identifiers.

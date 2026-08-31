# Deployment Preference Template

Read this reference only when initializing or updating saved Netlify deployment preferences. Create `<state_root>/memory.md` only after confirming the user wants these preferences retained.

```markdown
# Netlify Deploy Preferences

## Status
status: ongoing
last: YYYY-MM-DD
integration: pending

## Context
- Preferred deploy mode: preview first
- Default project path:
- Typical package manager:
- Typical publish directory:

## Project Notes
- repo-or-site-name: short operational notes

## Constraints
- Required approval gates before `--prod`
- Environment-variable or branch rules

## Notes
- Observed preferences from real usage
```

## Status values

| Value | Meaning | Behavior |
|---|---|---|
| `ongoing` | Defaults are still being learned. | Continue collecting confirmed deployment patterns. |
| `complete` | Core defaults are known. | Use defaults while preserving per-release confirmation. |
| `paused` | Setup details are deferred. | Use safe task-specific defaults. |
| `never_ask` | Setup questions are unwanted. | Use explicit per-task confirmations instead. |

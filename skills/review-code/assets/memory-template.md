# Memory Template - Review Code

After `<state_root>` is resolved, create `<state_root>/memory.md` with this structure when the user consents to persistence:

```markdown
# Review Code Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Review Defaults
severity_threshold:
confidence_floor:
delivery_mode: quick | standard | deep

## Project Context
primary_stack:
critical_paths:
release_risk_profile:

## Known Constraints
test_limits:
accepted_risks:
team_conventions:

## Recent Sessions
- YYYY-MM-DD: <short summary / link under sessions/>
```

Optional children (create only when needed):

- `<state_root>/findings/` — per-review finding logs
- `<state_root>/baselines/` — accepted risk baselines and conventions
- `<state_root>/sessions/` — ongoing audit session summaries

Do not pre-create empty directories. Never write the literal string `<state_root>` to disk.

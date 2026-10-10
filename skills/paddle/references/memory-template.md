# Memory template — Paddle

Optional durable notes at `<state_root>/memory.md`. Create only with user consent
for continuity. **No secrets in this file.**

```markdown
# Paddle memory

## Status
status: ongoing
last: YYYY-MM-DD
integration: pending | sandbox | live | paused

## Environment
<!-- sandbox | live | both — which keys/prices are active in the app -->

## Product shape
<!-- SaaS subscription / one-time / mixed; trials; seat vs flat -->

## Stack
<!-- language, framework, host, webhook path -->

## Price map
<!-- logical plan name → price id pointer per env, e.g. pro_monthly_sandbox: pri_… -->

## Webhooks
<!-- destination URL pointer; events subscribed; handler location — secret via env:… only -->

## Access policy
<!-- past_due: keep+warn; paused: …; cancel effective_from default -->

## Notes
<!-- migrations, Retain on/off, open incidents -->
```

Companion file `<state_root>/webhooks.md` may list destinations and event routing
without secrets.

## Status values

| Value | Meaning |
| --- | --- |
| `ongoing` | Still learning edge cases; update opportunistically |
| `complete` | Enough context to operate without setup prompts |
| `paused` | User asked to stop expanding notes |
| `never_ask` | Do not prompt for more integration context |

Update `last` when the file changes. Prefer observing repo config over repeated
questionnaires.

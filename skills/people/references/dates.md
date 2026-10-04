# Dates

## Storage

- Prefer full ISO date `YYYY-MM-DD`
- Unknown year: `--MM-DD`
- Never store a naked age; compute from birth year when needed

## Lead times

| Date type | Default surface |
|---|---|
| Birthday | `birthday_lead_days` (default 5) before |
| Milestone birthday (30/40/50…) | 3 weeks before |
| Death anniversary | on the day only if previously marked |
| Work anniversary | 3 days before if the user tracks it |

Check `do-not-surface.md` before any date nudge. Draft messages for the user; never auto-send.

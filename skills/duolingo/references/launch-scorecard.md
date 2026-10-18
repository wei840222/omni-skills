# Operating Scorecard

Use this weekly to validate that the Learning OS actually works.

## System health metrics

| Metric | Target | Signal |
|--------|--------|--------|
| Router activation accuracy | ≥ 90% | AGENTS.md triggers match user intent |
| First loop completion | ≥ 75% | setup and onboarding clarity |
| Day-1 return | ≥ 45% | immediate value |
| Day-7 return | ≥ 20% | habit formation |
| Review completion ratio | ≥ 60% | reinforcement health |
| Multi-topic continuity | ≥ 80% | no topic left stale >7 days |

These targets are operating heuristics for this Learning OS, not published Duolingo KPIs.

## Diagnostic map

- Low activation accuracy → fix router triggers in `topics.md` and AGENTS block.
- Good starts, weak returns → reduce loop friction and add an easier comeback path.
- Good XP, low checkpoints → tighten mastery gates.
- Multi-topic drift → rebalance rotation policy.

## Weekly review checklist

- Verify the AGENTS router block is still present and up to date (if enabled).
- Check each active topic has a non-empty queue.
- Check each active topic had at least one session this week.
- Prune stale or duplicate trigger phrases.
- Archive retired topics under `<state_root>/archive/`.

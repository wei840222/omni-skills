# Memory Template — Digital Marketing

Create `<state_root>/memory.md` only if the user wants continuity across sessions.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning context | Gather only what improves decisions |
| `complete` | Enough context exists | Work normally without re-asking basics |
| `paused` | User does not want more setup | Stop pushing for more detail |
| `never_ask` | User opted out of continuity | Work statelessly |

## Optional Support Files

If the user wants deeper continuity, create:

- `<state_root>/campaigns.md` — current campaigns and asset bundles
- `<state_root>/experiments.md` — hypotheses, thresholds, outcomes
- `<state_root>/signals.md` — recurring metrics, anomalies, reusable lessons

## Key Principles

- Keep the memory short enough to scan fast
- Store decisions, not whole conversations
- Prefer context that changes execution quality: audience, message, channel mix, proof, constraints
- Update `last` whenever the local workspace changes

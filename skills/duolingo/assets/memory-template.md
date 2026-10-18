# Memory Template — Duolingo Learning OS

Create `<state_root>/memory.md` with this structure:

```markdown
# Duolingo Learning OS Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Active Topics
<!-- List topic slugs currently enabled (english, cooking, etc.) -->
<!-- Mark priority and weekly target per topic -->

## Routing Policy
<!-- When this skill should auto-activate -->
<!-- Link to AGENTS routing decision and trigger phrasing -->

## Rotation Policy
<!-- Single-topic or multi-topic schedule -->
<!-- Examples: alternating days, weighted split, fixed daily stack -->

## Progress Snapshot
<!-- Streak, recent wins, recent misses, pending reviews -->

## Notes
<!-- Observations about motivation, friction, and adaptation choices -->

---
*Updated: YYYY-MM-DD*
```

## Topic namespace standard

Each topic uses this path: `<state_root>/topics/<topic-slug>/`

Required files:

- `profile.md`
- `curriculum.md`
- `queue.md`
- `sessions.md`
- `checkpoints.md`

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Skill actively teaching | Continue lessons and reviews |
| `complete` | Main goals reached | Maintain with lighter reviews |
| `paused` | User paused learning | Keep state, pause proactive lessons |
| `deactivated` | User disabled this system | Reactivate only upon explicit request |

## Key principles

- Global memory coordinates topics; topic files hold lesson details.
- Keep router decisions explicit and easy to audit.
- Update `last` on every learning session.
- Templates live under `assets/`; live copies live under the resolved `<state_root>/`.

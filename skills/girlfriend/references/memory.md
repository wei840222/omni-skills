# Memory Rules - Girlfriend

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | calibration still evolving | keep learning durable preferences |
| `complete` | enough context for consistent realism | halt setup-style questions |
| `paused` | use saved context only | pause expanding memory unless asked |
| `never_ask` | user does not want setup prompts | rely on natural conversation only |

## Key principles

- Keep memory lean, specific, and user-confirmed.
- Store only what improves future realism and care.
- Keep secrets, explicit intimate details, and third-party private data out of storage.
- Update `last` after meaningful sessions, not every trivial message.
- Write under the resolved `<state_root>/` only; never into the skill package.
- Prefer short durable facts and open loops over full conversation dumps.

## Read order when skill is active

1. `<state_root>/memory.md` — status, activation, tone baseline
2. `<state_root>/bond.md` — pet names, rituals, flirting boundaries
3. `<state_root>/moments.md` — follow-ups due soon
4. `<state_root>/profile.md` — only when life context is needed

Create missing starter files from `assets/memory-templates.md` after consent.

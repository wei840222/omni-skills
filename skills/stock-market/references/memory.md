# Memory — Stock Market

Create `<state_root>/memory.md` using the Memory Template in `../assets/templates.md`.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context still evolving | Keep collecting preferences and constraints |
| `complete` | Core process defined | Execute with minimal setup questions |
| `paused` | User deferred planning | Keep context, avoid proactive planning prompts |
| `never_ask` | User opted out of setup prompts | Execute only direct requests |

## Storage Rules

- Save only user-approved decisions and explicit constraints.
- Update `last` on each skill use.
- Keep entries concise, measurable, and actionable.

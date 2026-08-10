# Memory — Stock Market

Create `<state_root>/memory.md` using the Memory Template in `assets/templates.md` (a path rooted at this skill package) only when persistent state is enabled and the user approves creation.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context still evolving | Keep collecting preferences and constraints |
| `complete` | Core process defined | Execute with minimal setup questions |
| `paused` | User deferred planning | Keep context and wait for a direct planning request |
| `never_ask` | User opted out of setup prompts | Execute only direct requests |

## Storage Rules

- Save only when persistent state is enabled and the user approves that update; retain only user-approved decisions and explicit constraints.
- Update `last` only when persistent state is enabled and the user approves that update.
- Keep entries concise, measurable, and actionable.

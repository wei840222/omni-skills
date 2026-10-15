# Memory Template — Ticketmaster Discovery API

Create `<state_root>/memory.md` with the structure provided in `assets/data-templates.md`.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning defaults | Keep collecting context naturally |
| `complete` | Defaults are stable | Reuse them unless user overrides |
| `paused` | User said not now | Work with explicit inputs only |
| `never_ask` | User declined setup questions | Skip asking for defaults |

## Key Principles

- Keep filters in natural language, not config-key syntax.
- Store stable defaults, not full raw API payloads.
- Save IDs only when they are reused or clearly important.
- Update `last` on each meaningful use.

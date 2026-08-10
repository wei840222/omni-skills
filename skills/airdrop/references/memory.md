# Memory

Create `<state_root>/memory.md` with the structure shown in `assets/memory-template.md`.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning | Capture stable sharing preferences gradually |
| `complete` | Enough context exists | Use remembered defaults without extra setup |
| `paused` | User wants minimal setup | Avoid more preference questions unless needed |
| `never_ask` | User does not want persistence | Keep everything session-only |

## Key Principles

- Save behavior patterns, not file contents.
- Do not store recipient names or device identifiers unless the user explicitly asks.
- Keep memory focused on activation and safety defaults.
- If the user declines persistence, do not create or update `<state_root>/`.

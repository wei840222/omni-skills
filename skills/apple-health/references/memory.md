# Persistent-note lifecycle — Apple Health

Resolve `<state_root>` with SKILL.md before any note operation. Read `<state_root>/memory.md` when it exists. Persist only user-requested integration notes, reproducible SQL and minimal freshness pointers; obtain consent before retaining health-related information. Seed a needed child from `assets/memory-template.md`, preserving existing content.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Normal state | Keep refining integration and analysis habits |
| `complete` | Stable setup | Skip setup prompts, go straight to analysis |
| `paused` | User postponed integration | Do not push setup, only answer planning questions |
| `never_ask` | User declined setup | Never re-prompt integration unless user requests |

## Key Principles

- Prefer reproducible queries over ad-hoc analysis.
- Record freshness to avoid misleading "latest" claims.
- Keep health data handling minimal and privacy-first.

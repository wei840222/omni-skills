# Persistent-note lifecycle — Apple Health

Resolve `<state_root>` with SKILL.md before any note operation. Read `<state_root>/memory.md` when it exists. Persist only user-requested integration notes, reproducible SQL and minimal freshness pointers; obtain consent before retaining health-related information. Seed a needed child from `assets/memory-template.md`, preserving existing content.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Normal state | Keep refining integration and analysis habits |
| `complete` | Stable setup | Skip setup prompts, go straight to analysis |
| `paused` | User postponed integration | Answer planning questions only; wait for an explicit setup request |
| `never_ask` | User declined setup | Wait for an explicit user request before offering integration again |

## Key Principles

- Prefer reproducible queries over ad-hoc analysis.
- Record freshness so "latest" claims stay accurate.
- Keep health data handling minimal and privacy-first.

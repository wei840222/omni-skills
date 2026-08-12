# Memory and Index Procedures - Kanban

Create and manage `<state_root>/memory.md` and `<state_root>/index.md`. Use `assets/kanban-data-templates.md` for their structure.

## Status Values in `memory.md`

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | still calibrating | keep learning defaults through usage |
| `complete` | reliable routing and board norms | run without setup prompts |
| `paused` | user paused Kanban setup changes | read existing board only |
| `never_ask` | user does not want setup prompts | never request configuration questions |

## Key Principles

- Keep the index machine-readable and human-readable.
- Update `last` and `last_used` on every successful board write.
- Ensure no secrets are stored in board or memory files.
- Preserve user custom lane names while keeping core card fields stable.

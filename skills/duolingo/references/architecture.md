# Architecture

State lives in `<state_root>/`. See `memory-template.md` for global state and per-topic file templates.

```
<state_root>/
|-- memory.md                    # Global status and active topic map
|-- router/
|   |-- topics.md                # Canonical list of active topics and trigger phrases
|   `-- agentsmd-snippet.md      # Snippet to keep AGENTS routing in sync
|-- topics/
|   |-- english/
|   |   |-- profile.md           # Goal, level, pace, constraints
|   |   |-- curriculum.md        # Skill tree and lesson units
|   |   |-- queue.md             # Next lessons and review backlog
|   |   |-- sessions.md          # Session history and outcomes
|   |   `-- checkpoints.md       # Weekly and milestone checks
|   `-- cooking/                 # Same structure for any other topic
`-- archive/                     # Retired topics and old curriculum versions
```

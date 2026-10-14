# Question Session State

## Resolve `<state_root>`

Follow the State location steps in `SKILL.md` before any read or write. Keep the
chosen root fixed for the invocation.

## Layout

```text
<state_root>/
└── session.json   # optional active context notes
```

## Session JSON shape

```json
{
  "active_context": "research | sales | coaching | journalism | learning",
  "current_topic": "what we're exploring",
  "key_assumptions": [],
  "last_framework": "socratic | spin | funnel | five-whys | other",
  "updated_at": "ISO-8601 timestamp when known"
}
```

## Rules

- Write only after the user opts into persistence.
- Store labels and assumptions, not interview transcripts with PII unless the user
  explicitly requests a durable note and the host policy allows it.
- Prefer portable paths under `<state_root>`; ask for a path instead of inventing a host absolute path.
- If older notes exist only under a legacy Clawic path, move them into the resolved
  `<state_root>/` after the user confirms, and say in one line what moved and from where.

# Decision records

Use when the user says "we decided", "going with", or needs a durable supersession trail.

## Required fields

Context, options considered/rejected, rationale, effective date, and what the decision supersedes.

## Procedure

1. Create one decision note; do not bury the decision only inside a long meeting note.
2. Link meetings/projects back to this note.
3. When a later decision replaces it, update both notes with the supersession pointer.

## Template

```markdown
# Decision: <claim>
date: YYYY-MM-DD
status: active|superseded
supersedes: <optional>
superseded_by: <optional>

## Context
...

## Options considered
- A — ...
- B — ...

## Decision
...

## Rationale
...

## Consequences / follow-ups
- @owner: verb — YYYY-MM-DD
```

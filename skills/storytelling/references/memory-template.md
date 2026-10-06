# Memory Template - Storytelling

Create `<state_root>/memory.md` with this structure after the user consents to persistence:

```markdown
# Storytelling Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Context
<!-- Audience profile, narrative goals, delivery channels, and constraints -->

## Story Bank
<!-- Reusable anecdotes, examples, proof points, and outcomes -->

## Message Pillars
<!-- Core claims, supporting arguments, and non-negotiable themes -->

## Voice Preferences
<!-- Tone, cadence, sentence density, and language constraints -->

## Experiments
<!-- A/B narrative tests, edits applied, and observed impact -->

## Notes
<!-- Internal reminders that improve continuity and output quality -->

---
*Updated: YYYY-MM-DD*
```

Optional companion files under the same `<state_root>/`:

- `story-bank.md` — longer reusable scenes and proof artifacts
- `messaging-pillars.md` — stable claims and evidence map
- `edit-log.md` — draft iterations and rejected directions

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning context | Ask only when missing context changes narrative choices |
| `complete` | Context is stable | Prioritize execution and iterative improvement |
| `paused` | User deferred setup | Use existing context without extra setup prompts |
| `never_ask` | User requested no setup prompts | Skip setup questions |

## Key principles

- Keep memory in natural language, not rigid configuration lists.
- Store only details that improve story quality, consistency, or decision impact.
- Update `last` after each meaningful storytelling session.
- Preserve failed narrative attempts so the same mistakes are not repeated.
- Persist credentials or private secrets only when the user explicitly asks, and prefer pointers over raw values.

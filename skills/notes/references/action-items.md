# Action items

Use for "what do I owe", overdue chase, and commitment extraction.

## Rule

Owner + verb + absolute date, or it is not an action item. Relative language ("next week") is resolved at write time.

## Tracker

- Default: `<state_root>/notes/actions.md` when `action_target: notes`.
- External: hand the item to the user's task app and keep only a pointer when `action_target: external` (often via `task-list`).
- No owner → Open Questions / Open Threads, not the tracker.

## Escalation

1. Due today / overdue: surface first.
2. Missing owner or date: repair before chasing.
3. Repeated slips: raise in the next relevant meeting note with evidence, not blame.

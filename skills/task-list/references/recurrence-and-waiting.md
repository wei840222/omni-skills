# Dates, recurrence, and waiting

## Date fields

Keep these fields separate:

- `Due`: the task becomes late or painful after this date.
- `Start` or `defer`: the task becomes visible on this date.
- `Completed`: when the user finished it.

For ambiguous language, ask which field changes before editing. “Move to Someday” changes bucket. “Snooze two weeks” changes start or defer. “Push deadline” changes due date.

## Recurrence

Record the user’s recurrence wording and its anchor. Calendar-based rules use the calendar date; completion-based rules use the completion timestamp. Confirm a recurrence change before writing it. On completion, create only the next occurrence and record the regeneration in `<state_root>/log.md`.

## Waiting

A Waiting record includes the dependency, owner, entered-waiting date, next chase date, and the action unlocked by a response. During review, surface stale waiting work even when it has no due date.

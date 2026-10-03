# Safety checklist

Apply before any destructive or broad AppleScript action.

## Pre-execution

- Confirm exact target app and object identity (pre-read when feasible).
- Confirm scope: one item, filtered set, or full set.
- Confirm reversibility and rollback option.
- Confirm user intent in explicit language.
- Confirm dictionary commands match the inspected shape.

## Confirmation gate (mandatory floor)

Use two-step confirmation for destructive actions:

1. Summarize the action and impact in one sentence.
2. Request explicit confirmation before execution.

Require unambiguous user confirmation before execution.
User preferences may require *more* confirmation; they must not disable this floor.

## Execution guardrails

- Run a pre-read snapshot when feasible.
- Execute the smallest possible scope first.
- Keep destructive commands isolated to a single bounded script.
- Prefer dictionary delete/move that is recoverable (for example Finder trash) over permanent erase when the user did not request permanent deletion.

## Post-execution

- Run read-back verification.
- Report what changed and what did not change.
- Log failure details if the expected state was not reached (durable log only after consent).

## Halt and recover

| Condition | Recovery |
| --- | --- |
| Target identity ambiguous | Ask one clarifying question; re-run pre-read; do not execute. |
| Dictionary commands differ from expected shape | Re-open dictionary workflow; replace guessed terms; re-probe. |
| Irreversible bulk change without confirmation | Stop; present scoped summary; wait for explicit confirm. |
| Permission / Automation denied | Capture exact error; guide to Privacy settings; re-run minimal probe. |

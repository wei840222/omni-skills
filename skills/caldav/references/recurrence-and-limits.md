# Recurrence and tool limits

## khal limits

- `khal edit` is interactive and requires a TTY.
- Recurrence editing support is rudimentary.
- Event timezones cannot be edited directly through `khal` in the general case.

## Safe posture for fragile series

For recurring series, DST-sensitive events, or uncertain matches:

1. Inspect first and show the series/instance details you can see.
2. Prefer recreate-only-with-approval over aggressive in-place edits when the tool cannot express the change cleanly.
3. If the user wants bulk recurring surgery, pause, explain the corruption and DST-drift risks, and wait for explicit authorization.

## Decision aid

| Situation | Default action |
|---|---|
| Clear one-off event, unique match | Verified create/edit/delete |
| Duplicate titles in window | List candidates; require disambiguation |
| Recurring series, simple instance ask | Inspect; warn about series vs instance semantics |
| Bulk series rewrite / timezone rewrite | Stop for approval; consider another client if khal cannot express it safely |

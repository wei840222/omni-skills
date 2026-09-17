# Write and verify

## Before every write

1. Sync and read the target window so the agent sees the exact current state.
2. Confirm calendar name, start/end, timezone assumption, and whether the event is one-off or recurring.
3. Prefer the smallest mutation that satisfies the request.

## Create

- Use non-interactive `khal` create flows when available for one-off events.
- Immediately sync, then query the same window and confirm title, time, and calendar.

## Edit or delete

- Match on title + time + calendar, or UID. Never rely on title alone when duplicates exist.
- `khal edit` is interactive and needs a TTY; do not treat it as a batch API.
- For deletes, restate the matched event and obtain confirmation when the match is not unique.

## Read-back pass (mandatory)

After create, update, or delete:

1. Sync again.
2. Query the same bounded window.
3. Report the returned title, time, and calendar (and UID when present).
4. If verification is ambiguous or inconsistent, pause and surface the conflict instead of claiming success.

## Conflict policy

- `vdirsyncer` synchronizes real local `.ics` state, not a disposable cache view.
- A configured `conflict_resolution` of "a wins" or "b wins" can overwrite one side.
- Manual filesystem edits, cache resets, and storage path changes must be deliberate and reversible.

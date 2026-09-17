# Sync discipline

`vdirsyncer sync` is part of every real operation, not optional cleanup.

## Order of operations

1. If collections are missing or a server path changed, run `vdirsyncer discover` before assuming the calendar is empty.
2. Sync before reads when freshness matters.
3. After a confirmed write, sync again so local `.ics` storage and the remote collection converge.
4. Only then trust a `khal` listing for the same window.

## Why this matters

- `khal` reads local storage and cache; a stale local tree produces confident wrong answers.
- Discovery failures often look like "empty calendar" until the collection path is fixed.
- A successful local write that never syncs is not remote success.

## Practical checks

- Confirm the pair/collection name in the user's `vdirsyncer` config before inventing new paths.
- If sync reports conflicts, inspect the configured `conflict_resolution` policy before choosing a side.
- Do not claim remote success until post-write sync and read-back both succeed.

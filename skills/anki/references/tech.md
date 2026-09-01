# Technology and Domain Reference

Use this reference when an Anki version, scheduler, sync capability, or technical claim affects the recommendation. Prefer the official manual and release notes over remembered behavior.

## Current guidance

- **FSRS**: Use the manual's FSRS guidance to explain the optimizer, desired retention, and when its fit to collection history matters. Check the user's Anki version before describing available controls.
- **Scheduler and deck options**: Verify current defaults and the interactions among deck presets, daily limits, and learning/relearning steps in the manual before prescribing values.
- **Synchronization**: Treat AnkiWeb sync as replication, not backup. For self-hosted sync, use the official sync-server documentation and confirm that every client version is compatible.
- **Add-ons**: Verify compatibility against the target Anki version. Disable add-ons while diagnosing application faults and preserve a restorable `.colpkg` before upgrades or collection-wide edits.

## Authoritative sources

- Anki Manual — Deck Options: https://docs.ankiweb.net/deck-options.html
- Anki Manual — FSRS: https://docs.ankiweb.net/deck-options.html#fsrs
- Anki Manual — Synchronization: https://docs.ankiweb.net/syncing.html
- Anki Manual — Backups: https://docs.ankiweb.net/backups.html
- Anki Manual — Add-ons: https://docs.ankiweb.net/addons.html
- Anki Manual — Importing: https://docs.ankiweb.net/importing/text-files.html
- Anki Manual — Searching: https://docs.ankiweb.net/searching.html
- Anki Manual — AnkiHub / sync-server alternatives: https://docs.ankiweb.net/sync-server.html
- FSRS project documentation: https://github.com/open-spaced-repetition/fsrs4anki/wiki

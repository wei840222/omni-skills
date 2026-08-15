# Android state template

Load this reference only after the user approves local storage and the Android task produced durable information.

## Resolve the state root

1. Use `STATE_ROOT` when it is set.
2. Otherwise use `$XDG_STATE_HOME/android/` when `XDG_STATE_HOME` is set.
3. Otherwise use `~/.local/state/android/`.

Keep Android records under `<state_root>/android/`; keep shared device records in `<state_root>/devices/devices.md`. Create directories or files only after the user approves local storage.

## Files and record shapes

- `<state_root>/android/config.yaml`: user-approved preferences from the Configuration table.
- `<state_root>/android/memory.md`: durable decisions, aligned toolchain versions, non-obvious failures, benchmarks, and the `## Boxes` / `## Due` indexes.
- `<state_root>/android/releases/<year>.md`: release rows with versionCode, versionName, track, rollout, commit/tag, mapping-file location, and later vitals.
- `<state_root>/devices/devices.md`: one row per physical device or emulator, shared across skills.
- `<state_root>/projects/<project>.md`: a goal/status record for an app treated as a project.
- `<state_root>/contacts/contacts.md`: a client name only when the app owner needs a shared contact record.

For each durable write, announce the exact file and one-line change. Store credential pointers such as `env:PLAY_SERVICE_ACCOUNT_JSON` or `keychain:android-upload-key`, never secret values.

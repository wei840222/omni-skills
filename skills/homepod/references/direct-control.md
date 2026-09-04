# HomePod direct-control runbook

Load this only when the user requests active device control. `atvremote` can control compatible Apple TV and HomePod targets when its pairing and device support permit it; confirm the installed tool’s `--help` output before relying on a command or flag.

## Preconditions

1. Confirm that the user wants command execution now.
2. Confirm the control tool is installed and identify its supported target and command syntax.
3. Discover devices and select one unambiguous target.
4. Read the target’s current media and volume state before a change.

Example discovery and inspection pattern (verify flags against local help first):

```bash
atvremote scan
atvremote -n "Kitchen HomePod" device_info
atvremote -n "Kitchen HomePod" playing
atvremote -n "Kitchen HomePod" volume
```

## Command flow

Use the smallest command that satisfies the user’s goal. Confirm the exact target and intended operation immediately before a mutating command, then re-read state afterward. Keep any stream URL or local-file source explicit and user-approved.

## Recovery

| Symptom | First action | Recovery path |
|---|---|---|
| Command times out | Re-scan and verify the target is on the reachable network | Re-check the tool’s supported addressing options and retry only the selected target |
| Target is absent | Compare the requested name with discovery output | Ask the user to identify the intended device rather than guessing |
| Playback has no visible change | Re-read media state and current app | Confirm device support and pairing, then retry one reversible command |
| Volume is ignored | Verify the selected target is the active output | Validate on device, then retry only after user confirmation |

Keep pairing secrets in the tool or operating system’s secure pairing storage. When notes are enabled, record pre- and post-command state in `<state_root>/automation-log.md`.

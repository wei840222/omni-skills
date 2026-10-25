---
name: airtag
description: "Manage Apple AirTags and Find My tracking. Use when locating items, diagnosing Bluetooth connectivity issues, or responding safely to unwanted tracking alerts."
metadata:
  openclaw: '{"emoji": "A", "requires": {"bins": []}, "os": ["darwin", "linux", "win32"], "displayName": "AirTag"}'
---
## When to load
Load this skill when the user asks to manage, locate, or troubleshoot Apple AirTags, configure Find My connectivity, or respond to an unknown AirTag alert.

## State location

Airtag state may exist in `<workspace>/airtag/`, `<workspace>/memory/airtag/`, or `~/airtag/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/airtag/`, `<workspace>/memory/airtag/`, `~/airtag/`.
3. If none exists and state must be created, default to `<workspace>/airtag/`.

Use the selected `<state_root>` for every state operation in this skill.

Persistent state and logs are maintained in `<state_root>/`.

## Loading instructions
To proceed, you must load and read the following documents:
0. `assets/memory-template.md` - Structure and status fields for memory.
1. `references/setup.md` - Core initialization, access modes, and connection setup.
2. `references/access-connectors.md` - Technical details for Direct App Control, API Mode, and Shared Link Mode.
3. `references/anti-stalking-safety.md` - Safety-critical response flow for unknown AirTag alerts.
4. `references/battery-maintenance.md` - Battery replacement guidance and reliability notes.
5. `references/connection-diagnostics.md` - Troubleshooting connection and pairing issues.
6. `references/recovery-playbook.md` - Account-level recovery steps for lost items.

Load the relevant document based on the user's specific request. Begin by ensuring the appropriate connector access mode is established per `references/setup.md` before executing location or diagnostic workflows.

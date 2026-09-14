---
name: bluetooth
description: >
  Scan, connect, and control Bluetooth and BLE devices across Linux, macOS, and
  Windows. Use for device discovery, profile learning, pairing confirmation,
  audio/smart-home/fitness workflows, and secure local-only MAC handling.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📶","requires":{"anyBins":["bluetoothctl","blueutil","python3"]}}'
  related-skills: '{"iot":"Broader IoT connectivity and security when the question is not Bluetooth-specific.","smart-home":"Ecosystem-agnostic hub and automation guidance beyond Bluetooth device control.","alexa":"Alexa-specific device, routine, and skill workflows when the target is Alexa rather than raw Bluetooth.","shelly":"Shelly local RPC and cloud device control when the target is Shelly rather than generic Bluetooth.","home-server":"Always-on host placement for Bluetooth controllers, bridges, and local state."}'
---

## When to Use

Use this skill when the user needs practical Bluetooth or BLE execution: scan nearby devices, connect with confirmation, learn device profiles, switch audio endpoints, read fitness sensors, or apply pairing/security controls.
Prefer ecosystem-specific skills (`alexa`, `shelly`, `smart-home`) when the outcome depends on a vendor hub or cloud API rather than raw Bluetooth tooling.

## State location

Resolve `<state_root>` in this order:

1. `<workspace>/.agents/state` when a local workspace is active
2. `$XDG_DATA_HOME` when set
3. `~/.local/share` on Linux/macOS defaults

If the user or host configuration explicitly defines a state root, that path takes precedence. Resolve once per invocation and keep it fixed.

Skill state lives under `<state_root>/bluetooth/`. Create the directory when the first persistent write is required.

```text
<state_root>/bluetooth/
|-- profiles/         # Known device configs (one file per device)
|-- history.md        # Interaction log with success/failure
`-- pending.md        # Devices discovered but not profiled
```

## Core Workflow

1. **Scan** — Discover nearby devices
2. **Identify** — Match against known profiles or learn a new device
3. **Confirm** — Require explicit user confirmation for unknown devices
4. **Connect** — Establish the link with the appropriate protocol/tool
5. **Execute** — Send commands, read data, manage state
6. **Learn** — Update the device profile from success/failure evidence

## Progressive disclosure

| Situation | Load |
|------|------|
| OS-specific Bluetooth CLI tools (Linux/macOS/Windows) or Python libraries (Bleak) | `references/tools.md` |
| Parse, save, or manage device capabilities and connection profiles | `references/profiles.md` |
| Pairing, spoofing prevention, and security rules | `references/security.md` |
| Audio switching, smart-home control, or fitness data sync workflows | `references/use-cases.md` |

## Critical Rules

1. **Require manual confirmation** for all unknown devices before connection
2. **Whitelist first** — only interact with pre-authorized devices
3. **Log everything** — every connection attempt, command, and result under `<state_root>/bluetooth/`
4. **Handle failures gracefully** — retry with backoff, then report
5. **Keep MACs local** — never export MAC addresses to external services
6. **Profile learning** — when something works, save it; when it fails, note why

## Platform Detection

| OS | Primary Tool | Fallback |
|----|--------------|----------|
| Linux | `bluetoothctl` | `hcitool`, `gatttool`, Bleak |
| macOS | `blueutil` | `system_profiler`, CoreBluetooth, Bleak |
| Windows | WinRT/PowerShell | `pnputil`, Bleak |
| Cross-platform | Bleak (Python) | Noble (Node.js) |

## Device Interaction Pattern

```text
1. Resolve <state_root> once
2. Check <state_root>/bluetooth/profiles/ for the device
3. If known → load profile and use saved commands
4. If unknown → scan characteristics, discover capabilities, require confirmation
5. Execute the requested action
6. Verify result (read state or acknowledgment)
7. Update profile: what worked, what failed, timing
```

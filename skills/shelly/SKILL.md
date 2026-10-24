---
name: shelly
description: Control Shelly devices via local RPC and cloud APIs. Use for device
  discovery, telemetry reads, relay/switch commands, multi-device orchestration,
  and safe staged rollouts.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔌","requires":{"bins":["curl","jq"],"env":["SHELLY_CLOUD_TOKEN"]}}'
  related-skills: '{"api": "Generic HTTP/API workflow craft outside Shelly RPC method details.", "home-server": "Local always-on host and service placement for Shelly controllers and brokers.", "iot": "Broader IoT protocols and security when the question is not Shelly-specific.", "mqtt": "Broker-based messaging patterns when Shelly is one of several MQTT clients.", "smart-home": "Ecosystem-agnostic hub, automation, and network isolation guidance beyond Shelly-only workflows."}'
---

## Setup

On first use, read `references/setup.md` and align activation boundaries, local network scope, and write-safety defaults before sending Shelly commands.

## When to Use

Use this skill when the user needs practical Shelly execution: local RPC control, status and telemetry reads, cloud-assisted operations, device grouping, or staged automations.
Use this instead of generic IoT advice when outcomes depend on Shelly-specific RPC behavior, transport channel choice, and safe multi-device rollouts.

## State location

Shelly state may exist in `<workspace>/shelly/`, `<workspace>/memory/shelly/`, or `~/shelly/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/shelly/`, `<workspace>/memory/shelly/`, `~/shelly/`.
3. If none exists and state must be created, default to `<workspace>/shelly/`.

Use the selected `<state_root>` for every state operation in this skill.

Skill state lives under `<state_root>/shelly/`. If the directory does not exist, initialize it from `references/setup.md` and `references/memory-template.md`.

Memory lives in `<state_root>/shelly/`. See `references/memory-template.md` for structure and status values.

```text
<state_root>/shelly/
|-- memory.md         # Core context and activation boundaries
|-- environments.md   # LAN segments, cloud context, and endpoint mapping
|-- devices.md        # Device registry, components, and command patterns
|-- automations.md    # Sequencing rules, schedules, and rollback plans
`-- incidents.md      # Failure signatures and validated recoveries
```

## Quick Reference

Use the smallest file needed for the current task.

| Topic | File | When to load |
|-------|------|--------------|
| Setup and activation | `references/setup.md` | When initializing state or confirming boundaries |
| Memory and workspace | `references/memory-template.md` | When creating or parsing memory files |
| Protocol and transport | `references/protocol-matrix.md` | When choosing between HTTP, WS, or MQTT |
| Access and auth | `references/auth-and-access.md` | When dealing with cloud tokens or device auth |
| Device operations | `references/device-operations.md` | When issuing commands or reading telemetry |
| Rollout playbooks | `references/orchestration-playbooks.md` | When executing multi-device updates |
| Troubleshooting | `references/troubleshooting.md` | When diagnosing errors or recovering state |
| Official sources | `references/sources.md` | When validating current Shelly API or product docs |

## Core Rules

### 1. Select the Correct Control Plane Before Acting
- Decide local-only, cloud-assisted, or mixed mode before issuing commands.
- Prefer local HTTP RPC for single-device, low-latency reads and writes when the device is reachable.
- Use cloud only when remote access is required and `SHELLY_CLOUD_TOKEN` is available in the environment.
- Keep one transport for the run unless an explicit fallback policy says otherwise.

### 2. Verify Identity and Baseline Before Writes
- Resolve device id, component id, and supported methods first.
- Read current status before any write.
- Treat high-current relays, heating circuits, and security-triggering automations as high-impact and require explicit user confirmation.

### 3. Canary, Verify, Then Expand
- Run one-device canary before batch commands.
- Treat command acknowledgment as intermediate; require observed final state match.
- Halt the batch on the first critical verification failure and record the signature in `incidents.md`.

### 4. Keep Secrets Out of Skill State
- Read `SHELLY_CLOUD_TOKEN` only from environment variables.
- Store sanitized notes under `<state_root>/shelly/`; never write raw tokens into skill files or chat logs.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `http://<device-ip>/rpc` | RPC method names, params, and request identifiers | Local Shelly device control and status retrieval |
| `ws://<device-ip>/rpc` | RPC messages and event subscriptions | Local WebSocket notifications and event streaming |
| `mqtt://<broker>` | Device state and command topics with payloads | MQTT-based event and automation integration |
| `https://*.shelly.cloud` | Account-scoped API requests, device metadata, and command payloads | Shelly cloud control and remote device operations |
| `https://shelly-api-docs.shelly.cloud` | Documentation lookup queries | Validate Shelly API behavior and method constraints |

No other data is sent externally.

## Security & Privacy

Data that leaves your machine:
- local RPC or cloud API payloads needed for requested Shelly operations
- optional MQTT publish/subscribe payloads in user-configured broker setups

Data that stays local:
- environment mapping, device capability notes, and runbooks under `<state_root>/shelly/`
- incident timelines and rollback decisions

This skill does NOT:
- use undeclared third-party endpoints
- recommend bypassing device authentication or platform policy controls
- store `SHELLY_CLOUD_TOKEN` in local skill files
- execute bulk writes without user confirmation and a verification strategy

## Trust

This skill sends operational data to Shelly devices and optionally Shelly cloud services when execution is approved.
Only install if you trust your network environment, broker setup, and Shelly account scope with this automation data.

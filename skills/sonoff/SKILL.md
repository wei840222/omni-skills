---
name: sonoff
description: >
  Control and automate SONOFF devices through eWeLink cloud, LAN control, DIY
  mode local HTTP, and SONOFF iHost Open API paths with capability checks,
  read-before/after-write verification, and canary-first multi-device rollouts.
  Use when the user needs SONOFF/eWeLink plugs, switches, relays, DIY zeroconf
  control, iHost local REST/SSE, or safe fleet commands. Not for generic
  multi-protocol hub planning (`smart-home`), broker-only MQTT design (`mqtt`),
  or cross-vendor IoT architecture without a SONOFF control question (`iot`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔌","env":["EWELINK_API_TOKEN"]}'
  related-skills: '{"api":"General HTTP client and auth patterns when eWeLink cloud calls need request-shape help beyond SONOFF plane selection.","home-server":"Always-on host placement for iHost, local bridges, or controllers that run beside SONOFF automation.","iot":"Multi-protocol device and transport planning when SONOFF is only one node in a broader fleet.","mqtt":"Broker, topic, and QoS design when SONOFF state is bridged through MQTT rather than direct DIY/iHost HTTP.","smart-home":"Hub, room, and protocol product choices when the ask is ecosystem planning rather than SONOFF command execution."}'
---

## State location

Operational notes for SONOFF environments, devices, automations, and incidents may live under a portable `<state_root>/`. Resolve it once before any state read or write:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/sonoff/`, `<workspace>/memory/sonoff/`, `~/sonoff/`.
3. If none exists and persistent notes are needed, default to `<workspace>/sonoff/`.

Use the selected `<state_root>` for every state operation in this skill. Create state only when the user wants durable control context. Keep raw tokens out of state files; load `EWELINK_API_TOKEN` from the environment for cloud mode.

## When to load

Load for **SONOFF-specific control and automation**:

- eWeLink cloud command/status workflows with account-scoped credentials
- LAN control on devices that actually advertise LAN capability
- DIY mode local HTTP (`/zeroconf/*`) on compatible DIY firmware
- SONOFF iHost / eWeLink CUBE local Open API REST and SSE flows
- Multi-device rollout with canary, halt, and rollback checkpoints

Prefer sibling skills instead when:

- Protocol/hub product choice across vendors → `smart-home`
- MQTT broker/ACL design without a SONOFF plane decision → `mqtt`
- Cross-protocol IoT architecture without SONOFF execution → `iot`

## Primary workflow

Execute in order. Stop when a missing plane, capability, or confirmation blocks a safe write.

1. **Classify the ask** — single-device status/command, diagnostics, DIY/LAN setup, iHost local API, or multi-device rollout.
2. **Resolve control plane first** — eWeLink cloud, LAN, DIY mode, or iHost Open API. Load `references/control-planes.md`. Emit write payloads only after the plane is explicit.
3. **Resolve auth and identity** — environment token for cloud; reachability and mode eligibility for LAN/DIY; short-lived bridge token for iHost. Load `references/auth-and-access.md`. Map cloud id / LAN id / iHost id before mixed-plane work.
4. **Read baseline, then write** — load `references/device-operations.md`. Capture observed state, validate model-legal fields, execute, re-read, and treat acknowledgment alone as incomplete.
5. **Scale only after canary** — for fleets, load `references/orchestration-playbooks.md`. One-device canary → small batches → hard halt on divergence.
6. **Diagnose with plane-specific recovery** — load `references/troubleshooting.md` on failure; freeze further writes until identity and state reconcile.
7. **Persist only approved context** — on first durable setup, load `references/setup.md` and `references/memory-template.md`; keep structure under `references/state.md`.

## Core operating rules

1. **Plane before payload** — choose and record the control plane before any command template.
2. **Capability is a hard gate** — unsupported LAN/DIY assumptions fail closed; they are not transient retries.
3. **Observed state wins** — baseline read, write, verify; prefer reachable LAN observation for immediate local decisions when policy allows.
4. **High-impact needs explicit confirmation** — power relays on critical circuits, heating, locks, alarms, and bulk updates stay read-only until the user approves apply mode.
5. **Idempotent automation** — deterministic run ids, bounded retries, per-step expected-state checks, and a named halt condition.
6. **Secrets stay in the environment** — use `EWELINK_API_TOKEN` from env for cloud; keep production tokens out of chat and out of `<state_root>/` files.

## Quick reference

| Topic | File |
|-------|------|
| First activation and write boundaries | `references/setup.md` |
| State layout and requirements | `references/state.md` |
| Memory / device / incident templates | `references/memory-template.md` |
| Control-plane selection | `references/control-planes.md` |
| Auth and iHost token flow | `references/auth-and-access.md` |
| Single-device command loop | `references/device-operations.md` |
| Multi-device rollout and incidents | `references/orchestration-playbooks.md` |
| Diagnostics and recovery | `references/troubleshooting.md` |
| Domain rules, traps, endpoints | `references/domain.md` |
| Verified primary sources | `references/sources.md` |

## Output contract

- Name the selected control plane and the evidence used (capability, reachability, or policy).
- For writes: baseline → command → observed result; say when verification is still open.
- For missing inputs (token, device id, mode support, iHost address): list exact blockers instead of inventing success.
- For batch work: report canary outcome, batch size, halt reason, and rollback owner.

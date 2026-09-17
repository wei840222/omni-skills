---
name: zigbee
description: Deploy, manage, and troubleshoot Zigbee mesh networks. Load this skill
  when designing a home automation network, diagnosing pairing or routing issues,
  migrating coordinators, or resolving 2.4GHz interference.
metadata:
  openclaw: '{"emoji":"🐝"}'
  related-skills: '{"smart-home":"Broader hub, automation, and protocol selection when Zigbee is only one layer.","mqtt":"Broker, topic, and QoS design when Zigbee is bridged through MQTT or Zigbee2MQTT.","iot":"Cross-protocol device planning when Zigbee must coexist with Wi-Fi, Thread, or other transports.","home":"General home maintenance framing outside mesh-network operations.","thermostat":"HVAC comfort and schedule work once Zigbee climate devices are reachable."}'
---

## State location

This is a stateless skill. It does not create or require a local state tree. Keep network maps, device inventories, and recovery notes as ordinary user files outside the skill package.

## When to load

Load this skill when the user is designing, expanding, migrating, or repairing a Zigbee mesh for home automation.

Typical requests:
- "set up a Zigbee network"
- "device will not pair"
- "Zigbee is slow or drops"
- "migrate my coordinator"
- "Wi-Fi is killing my mesh"
- "groups vs binding for bulbs and switches"

Load only the reference needed for the current task:
- `references/mesh.md` for backbone design, routers, and end devices
- `references/coordinator.md` for sticks, placement, firmware, and migration
- `references/interference.md` for 2.4GHz channel planning with Wi-Fi
- `references/compatibility.md` for vendor quirks and interoperability limits
- `references/pairing.md` for join mode, reset, and first-join distance
- `references/binding-and-groups.md` for groups versus direct binding
- `references/battery.md` for sleepy end devices and reporting tradeoffs
- `references/troubleshooting.md` for online-but-dead, delays, and sparse mesh
- `references/sources.md` when verifying channel, stack, or compatibility claims

## Default operating model

Prefer a single coordinator, a router-first backbone, and local control through a maintained stack such as Zigbee2MQTT, ZHA, or another local hub the user already trusts.

Core order of operations:
1. Choose one coordinator and one channel plan before buying more end devices.
2. Pair mains-powered routers first so the mesh has a backbone.
3. Place the coordinator away from dense USB/PC noise with a short USB extension when needed.
4. Pair end devices close to the coordinator or a strong nearby router, then move them.
5. Prefer binding for direct switch-to-light links that must survive coordinator reboots; use groups when the coordinator should fan out one command.
6. Treat "Zigbee compatible" as vendor-specific until the exact model is checked against the chosen stack.

## Quick workflow

### New network
1. Confirm the user wants Zigbee rather than Wi-Fi-only or Thread/Matter-first.
2. Load `references/coordinator.md` and pick one stick/hub plus firmware readiness.
3. Load `references/interference.md` and pick a non-overlapping channel before mass pairing.
4. Load `references/mesh.md` and place routers every roughly 10-15m of usable indoor path.
5. Pair routers, then sensors/buttons, then validate hops with real commands.

### Existing flaky network
1. Load `references/troubleshooting.md`.
2. Check coordinator health, channel overlap, router density, and sleepy-device reporting before blaming a single sensor.
3. Add routers or move the coordinator before factory-resetting the whole mesh.
4. Re-pair only the failing leaf after the backbone is healthy.

### Migration
1. Backup the current network if the stack supports it.
2. Load `references/coordinator.md`.
3. Expect pairings to be lost when the coordinator hardware identity changes without a supported migrate path.
4. Rebuild router backbone first after cutover.

## Key success factors

- Battery devices are end nodes only; they do not extend range.
- One coordinator per network; a second stick usually means a second mesh.
- Channel changes usually force mass re-pairing; choose carefully once.
- Xiaomi/Aqara, Tuya, and some vendor hubs need stack-specific handling.
- Binding survives coordinator reboot better than groups for direct device links.
- "Online" in the UI is not proof the route still works; test an actual command.
- Keep secrets, network keys, and hub credentials out of chat and commits.

## Scope

This skill ONLY:
- Designs and diagnoses Zigbee mesh behavior
- Guides coordinator, channel, pairing, binding/groups, and recovery choices
- Routes to MQTT or broader smart-home skills when the problem leaves the mesh layer

This skill NEVER:
- Claims every "Zigbee compatible" device will join every hub
- Treats Wi-Fi smart plugs as mesh routers
- Recommends running two coordinators on one logical home network
- Stores live network keys or account secrets inside the skill package

---
name: smart-home
description: Set up, automate, secure, and troubleshoot smart home devices with protocol
  selection, network isolation, and ecosystem-agnostic automation patterns. Use when
  choosing hubs or protocols, inheriting devices, designing room automations, hardening
  IoT security, recovering offline devices, or planning renter-friendly installs.
metadata:
  openclaw: '{"emoji":"🏠"}'
  related-skills: '{"network":"VLAN, firewall, and reachability work that underpins IoT isolation.","wifi":"Wireless channel and client issues when smart devices share the RF environment.","zigbee":"Mesh design, pairing, and interference when Zigbee is the chosen radio layer.","iot":"Cross-protocol device and broker patterns beyond a single-home automation plan.","mqtt":"Broker, topic, and QoS design when hubs and devices exchange state over MQTT.","alexa":"Alexa-specific skill and device workflows inside a broader smart-home plan.","thermostat":"HVAC schedules and comfort control once climate devices are on the network.","home-server":"Always-on local hosts that run Home Assistant, brokers, or controllers."}'
---

## State location

Smart-home inventories, hub notes, and automation drafts may exist in `<workspace>/smart-home/`, `<workspace>/memory/smart-home/`, or `~/smart-home/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/smart-home/`, `<workspace>/memory/smart-home/`, `~/smart-home/`.
3. If none exists and state must be created, default to `<workspace>/smart-home/`.

Create state only when the user needs persistent configuration notes. Use the selected `<state_root>` for every state operation in this skill.

## When to load

Load this skill for ecosystem-agnostic smart-home planning—not brand-only skill trees.

Typical requests:
- "start a smart home from scratch"
- "which protocol should I pick"
- "take over the previous owner's devices"
- "automate lights when we leave"
- "put cameras on a separate VLAN"
- "this bulb keeps going offline"
- "renter-friendly setup with no permanent wiring"

Load only the reference needed for the current task:
- `references/setup.md` — protocols, hubs, first purchases
- `references/takeover.md` — reset, claim, and security audit on inherited gear
- `references/automations.md` — room and scenario patterns
- `references/security.md` — VLAN, credentials, local-first options
- `references/troubleshooting.md` — offline, pairing, and wrong-behavior recovery
- `references/renters.md` — portable, non-invasive installs
- `references/sources.md` — primary references for protocol and security claims

## Decision tree

| Situation | Action |
|-----------|--------|
| Starting from scratch | `references/setup.md` |
| Inheriting existing devices | `references/takeover.md` |
| Adding automations | `references/automations.md` |
| Security / privacy setup | `references/security.md` |
| Device not working | `references/troubleshooting.md` |
| Renting (no permanent changes) | `references/renters.md` |

## Universal rules

**Protocol choice matters more than brand.** Matter and Thread are the forward path for mixed ecosystems. Zigbee and Z-Wave remain mature mesh options. Wi-Fi devices consume airtime and router state; use them deliberately for high-bandwidth endpoints such as cameras.

**Local control beats cloud.** When the internet fails, lights and locks should still work. Prefer Home Assistant, Hubitat, or HomeKit-style local execution over cloud-only assistants when reliability matters.

**Network segmentation is non-negotiable.** IoT endpoints belong on an isolated VLAN or equivalent guest segment. They must not reach laptops, NAS, or admin workstations by default. One compromised bulb must not expose the trusted LAN.

**Start small, expand deliberately.** Commission a few devices, live with them, then grow. Most over-automation happens in week one and gets undone in month one.

## Quick reference

### Protocol comparison

| Protocol | Range | Mesh | Power | Best for |
|----------|-------|------|-------|----------|
| Matter / Thread | Good | Yes | Mains / battery | New mixed-ecosystem setups |
| Zigbee | Good | Yes | Battery-friendly | Sensors, buttons, bulbs |
| Z-Wave | Better wall penetration | Yes | Often mains | Switches, locks, repeaters |
| Wi-Fi | Good | No | Power-hungry | Cameras, high bandwidth |
| Bluetooth | Short | Limited | Battery | Proximity and wearables |

### Hub vs hubless

| Hubless works for | Hub required for |
|-------------------|------------------|
| Roughly 5–10 Wi-Fi devices | 20+ devices or multi-floor mesh |
| Single consumer ecosystem | Mixed protocols and vendors |
| Basic scenes | Local complex automations |
| Renters / temporary spaces | Long-term homeowner builds |

## Security essentials

1. Change default passwords on every device—cameras, routers, hubs, locks.
2. Disable UPnP; open only explicit port rules you can explain.
3. Enable MFA on accounts that control locks, cameras, and alarms.
4. Check firmware monthly, or enable auto-update where the vendor is trustworthy.
5. Audit the network quarterly and remove unrecognized devices.
6. Keep hub tokens, network keys, and camera credentials out of chat and git; store operational notes under `<state_root>/` only when the user wants persistence.

## Default operating model

1. Choose protocol and hub strategy before bulk buying.
2. Isolate IoT networking before onboarding cameras or locks.
3. Reset and reclaim inherited devices before linking personal accounts.
4. Automate presence and safety first; add convenience scenes later.
5. Verify recovery paths (hub backup, lock codes, offline behavior) before depending on automation.

## When to hand off

- Deep Zigbee mesh design or pairing failures → `zigbee`
- VLAN / DNS / firewall diagnosis beyond IoT guest setup → `network` or `wifi`
- Broker topic design and MQTT hardening → `mqtt`
- Always-on controller host placement → `home-server`
- Alexa-only skill/device operations → `alexa`
- HVAC schedule detail after devices are reachable → `thermostat`

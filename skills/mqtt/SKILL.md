---
name: mqtt
description: >
  Design, harden, and troubleshoot MQTT brokers and clients: authentication,
  TLS listeners, client IDs, ACL topic grants, QoS tradeoffs, retained/birth/will
  patterns, clean session vs clean start, and Mosquitto operations. Use when the
  user asks about MQTT topics, brokers, subscribers, publishers, bridge config,
  or broker debugging. Not for multi-protocol IoT device planning (`iot`),
  Zigbee mesh ops (`zigbee`), hub/automation product choice (`smart-home`), or
  host firewall syntax alone (`firewall`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📡"}'
  related-skills: '{"iot":"Cross-protocol device and transport planning when MQTT is only one layer.","zigbee":"Mesh pairing and routing when Zigbee is bridged through MQTT or Zigbee2MQTT.","smart-home":"Hub and room automation choices when broker design is secondary.","firewall":"Host or edge firewall rules once broker exposure and VLAN decisions are set."}'
---

This skill is stateless and does not store local configuration or persistent user state. Keep broker inventories, ACLs, and credentials in ordinary user files outside the skill package.

# MQTT

Broker- and client-centric guidance for Message Queuing Telemetry Transport: secure listeners, correct topic design, QoS semantics, session/retention pitfalls, and Mosquitto-oriented operations without turning the broker into an open internet surface.

## When to load

Load this skill when the request is **MQTT-specific**, for example:

- securing Mosquitto or another broker (auth, TLS, ACLs, bind address)
- choosing QoS 0/1/2 and making handlers idempotent
- designing topic hierarchies and subscription wildcards
- retained messages, last will/testament, and birth messages
- clean session / clean start, keep-alive, reconnect, and duplicate client IDs
- debugging with `$SYS/#`, `mosquitto_sub`, or unexpected retained state

Prefer sibling skills when the problem is already broader: `iot` for multi-protocol device planning, `zigbee` for mesh-only ops, `smart-home` for hub product choice, `firewall` for host firewall syntax after exposure decisions.

## Quick workflow

1. **Scope exposure** — local-only vs LAN vs internet; never leave anonymous listeners on non-loopback interfaces.
2. **Lock identity** — unique client IDs, per-device credentials, least-privilege ACLs on topic trees.
3. **Pick QoS deliberately** — effective QoS is min(publisher, subscriber); QoS 1 needs idempotent handlers; QoS 2 only when duplicates are harmful and cost is acceptable.
4. **Design topics** — no leading `/`, wildcards only on subscribe, document retained vs ephemeral paths.
5. **Plan sessions** — clean start/session, keep-alive (~60s default is reasonable), client-side reconnect, will/birth for presence.
6. **Verify sources** — version-sensitive protocol or Mosquitto option claims against URLs in `references/sources.md`.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/best-practices.md` | Security, QoS, topics, sessions, retained/will, Mosquitto knobs, debugging |
| `references/sources.md` | Official MQTT / Mosquitto / HA docs used for Gate 6 freshness |
| `test-prompts.json` | Evaluation harness only — do not load during normal user assistance |

## Operating rules

### Security first

- Default Mosquitto often allows anonymous connections — bots scan constantly; require authentication on any non-lab listener.
- TLS (or equivalent encrypted transport) is mandatory when credentials or payloads leave a trusted host/network path.
- Duplicate client IDs fight for one session — both sides disconnect in loops; mint unique IDs per device/process.
- ACLs must restrict publish/subscribe trees — one compromised device must not read or write the whole hierarchy.
- Prefer bind `127.0.0.1` or a private interface for local-only brokers; `0.0.0.0` is an exposure decision, not a convenience default.

### QoS semantics

- Effective QoS is the **minimum** of publisher and subscriber settings; the broker may downgrade.
- QoS 1 can deliver duplicates — handlers and downstream effects must be idempotent.
- QoS 2 has higher overhead — reserve it for commands where duplicates cause real harm.
- QoS is per message; mixing levels on one topic is allowed when intentional.

### Topics

- Do not start topics with `/` (creates an empty first level); prefer `home/temp` over `/home/temp`.
- Wildcards (`+`, `#`) work only in subscriptions — never publish to a wildcard topic.
- `#` matches the full subtree including nested levels; use it carefully.
- Some brokers limit topic depth or throughput — check limits before deep hierarchies.

### Sessions, retained, and presence

- Clean session false / persistent sessions preserve subscriptions and may queue messages while offline — surprise backlog is a design issue, not a feature accident.
- Keep-alive too long delays dead-client detection; ~60s is a common reasonable default unless the path is extremely constrained.
- Reconnect is the **client's** responsibility; many libraries do not auto-reconnect with full session restore unless configured.
- Last will fires on **unexpected** disconnect paths the broker detects — a clean disconnect typically does not publish the will.
- Retained messages persist until cleared (empty payload + retain flag on many brokers) — stale retained state confuses new subscribers.
- Birth/will presence pattern: publish retained "online" on connect; configure will to publish "offline".

### Mosquitto-oriented ops

- `persistence true` keeps retained messages and durable session state across restarts when configured correctly.
- `max_queued_messages` (and related queue limits) prevent one slow subscriber from exhausting broker memory.
- Document listener address/port pairs explicitly; local-only labs should not copy public-bind examples blindly.

### Debugging without leaking production

- `mosquitto_sub -v` (topic + payload) is the default inspection tool for lab traffic.
- Subscribing to `#` in production leaks everything — restrict to isolated test brokers or tightly ACL'd debug principals.
- `$SYS/#` exposes broker metrics (clients, bytes, subscriptions) when enabled — treat as sensitive operational data.
- After fixing bad retained data, **explicitly clear** retained messages; restarts alone may not remove them.

## Safety boundaries

- Treat broker passwords, TLS keys, and ACL files as secrets; examples use unmistakable placeholders only.
- Do not recommend anonymous internet-facing brokers, disabled authentication "for convenience", or production subscribe-to-`#` debugging.
- Medical, industrial safety, or life-critical control loops need domain specialists; this skill covers homelab and general application messaging patterns.
- Prefer local control and segmented networks before exposing any broker management or MQTT port.

## Scope

This skill ONLY:

- Designs and hardens MQTT broker/client behavior
- Guides topic, QoS, session, retained/will, and Mosquitto operational choices
- Routes to IoT / Zigbee / smart-home / firewall skills when the problem leaves the MQTT layer

This skill NEVER:

- Claims every cloud MQTT SaaS shares identical semantics with Mosquitto
- Treats validator-only packaging checks as proof of live broker correctness
- Stores live credentials or ACL inventories inside the skill package

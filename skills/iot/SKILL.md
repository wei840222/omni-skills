---
name: iot
description: >
  Design, harden, and troubleshoot IoT devices and networks: protocol selection
  (MQTT, CoAP, Zigbee, Thread/Matter, BLE, LoRa), ESP32/ESP8266 firmware choices,
  power budgets, Home Assistant / ESPHome / Zigbee2MQTT / Tasmota integration,
  and local-first security. Use when the user asks about sensors, brokers, mesh
  radios, smart-home bridges, OTA updates, or IoT VLAN isolation. Not for pure
  broker internals alone (`mqtt`), Zigbee mesh-only ops (`zigbee`), generic LAN
  firewalling without devices (`firewall`), or Arduino non-IoT sketches
  (`arduino`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📡"}'
  related-skills: '{"mqtt":"Broker, topic, QoS, TLS, and client-ID design when the work is MQTT-specific.","zigbee":"Zigbee mesh pairing, routing, and coordinator migration beyond multi-protocol IoT planning.","smart-home":"Hub and automation product choices when protocol selection is only one layer.","arduino":"General Arduino sketch and board work outside ESP/IoT deployment.","firewall":"Host or edge firewall rules once IoT VLAN and exposure decisions are set."}'
---

This skill is stateless and does not store local configuration or persistent user state. Keep inventories, credentials, and network diagrams in ordinary user files outside the skill package.

# IoT

Cross-protocol guidance for Internet of Things devices: choose transports, harden brokers and firmware, plan power and reliability, and integrate with common local smart-home stacks without cloud lock-in.

## When to load

Load this skill when the request involves **devices + network + protocol tradeoffs**, for example:

- picking MQTT vs CoAP vs HTTP vs mesh radios for sensors
- securing a self-hosted broker or IoT VLAN
- ESP32/ESP8266 framework, deep sleep, or OTA design
- Home Assistant, ESPHome, Zigbee2MQTT, or Tasmota integration paths
- Matter/Thread coexistence with Wi-Fi and Zigbee

Prefer sibling skills when the problem is already narrowed: `mqtt` for broker-only work, `zigbee` for mesh-only ops, `firewall` for host firewall syntax, `arduino` for non-IoT MCU sketches.

## Quick workflow

1. **Scope the device class** — battery vs mains, indoor vs outdoor, required latency/bandwidth, local-only vs cloud-assisted.
2. **Pick the transport** — load `references/guides.md` § Protocol Selection and Connectivity Patterns.
3. **Harden first** — authentication, TLS/mTLS where exposed, unique per-device credentials, signed firmware, IoT VLAN; see Security sections in `references/guides.md`.
4. **Plan power and reliability** — deep sleep, watchdog, offline retention, heartbeat; avoid single-sensor critical paths.
5. **Integrate locally** — Home Assistant MQTT discovery, ESPHome, Zigbee2MQTT, Tasmota; prefer local APIs over cloud-only vendors.
6. **Verify sources** — version-sensitive claims (Matter revisions, chip variants) against URLs in `references/sources.md`.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/guides.md` | Protocol matrices, MQTT essentials, security, ESP power, HA integration, debugging, vendor lock-in |
| `references/sources.md` | Official docs used for Gate 6 freshness (Matter, ESP-IDF, Mosquitto, HA, ESPHome, Z2M, Tasmota) |
| `test-prompts.json` | Evaluation harness only; not loaded during normal execution |

## Safety boundaries

- Treat device credentials, `.p8`/TLS keys, and broker passwords as secrets; examples use unmistakable placeholders only.
- Prefer **local control paths** and segmented networks before exposing any broker or device management port.
- Do not recommend disabling authentication, leaving debug UART/JTAG enabled in production, or shipping unsigned firmware updates.
- Medical, industrial safety, or life-critical control loops need domain specialists; this skill covers consumer/homelab IoT patterns.

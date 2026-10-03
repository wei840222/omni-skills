# IoT guides

Load this file when the skill needs protocol, security, firmware, power, or integration detail beyond the SKILL.md entry point.

## Protocol Selection

- **MQTT** — lightweight pub/sub, low bandwidth, ideal for sensors and HA bridges
- **CoAP** — UDP, REST-like, very low power for constrained nodes
- **HTTP/REST** — familiar on capable devices; heavier; use when bandwidth allows
- **WebSocket** — real-time bidirectional dashboards and live updates
- **Zigbee / Z-Wave** — mesh without Wi-Fi; battery-friendly sensors (see also `zigbee` skill)
- **Thread / Matter** — IP mesh + application interoperability layer across major ecosystems
- **BLE** — short range, low power; wearables and beacons
- **LoRa** — long range, low bandwidth; outdoor and agricultural links

## MQTT Essentials

- Broker is the hub — Eclipse Mosquitto is a common self-hosted choice
- Topics are hierarchical — `home/livingroom/temperature`
- QoS: 0 fire-and-forget, 1 at-least-once, 2 exactly-once
- Retain flag keeps last message for new subscribers
- Last Will announces unexpected disconnects
- Unique client IDs per device session; duplicate IDs fight for the connection
- For broker-deep work, hand off to the `mqtt` skill

## Security (Critical)

- Require authentication before any internet-facing broker listener
- TLS for external or untrusted-network access; consider mTLS for device-to-cloud
- Unique credentials per device so one compromise can be revoked alone
- Sign firmware updates; reject unsigned OTA payloads
- Place IoT devices on a separate VLAN/SSID from personal endpoints
- Disable or lock down UART/JTAG debug in production images
- Prefer Secure Boot / flash encryption on ESP32-class silicon when the threat model includes physical access

## Common Vulnerabilities

- Default credentials left unchanged
- Cleartext protocols on shared networks
- No firmware update path (permanent known CVEs)
- Cloud-only control with no local fallback
- Debug ports left enabled on deployed hardware
- Over-broad firewall allowlists for broker or manufacturer cloud callbacks

## Home Assistant Integration

- MQTT discovery can auto-configure entities when payloads follow HA conventions
- ESPHome for custom ESP devices — YAML config, OTA, native HA API
- Zigbee2MQTT bridges Zigbee networks onto MQTT
- Tasmota for many flashable off-the-shelf Wi-Fi devices
- Keep discovery and command topics documented in the user's inventory notes (outside this package)

## ESP32 / ESP8266 Development

- **Arduino framework** — fastest path, large library ecosystem
- **ESP-IDF** — FreeRTOS, production controls, steeper curve
- **PlatformIO** — dependency and multi-board management over stock IDE flows
- Deep sleep for battery life (µA-class sleep currents when designed correctly)
- OTA updates so field devices do not need physical access
- Current Espressif lines commonly referenced in docs: ESP32, ESP32-C3 (RISC-V, Wi-Fi 4, BLE 5), ESP32-S3 (vector/AI-oriented, USB OTG). Confirm pinouts and radio support in the target chip guide before locking a BOM.

## Power Management

- Battery nodes: wake on timer or interrupt, publish, return to deep sleep
- Calculate power budget: pack mAh vs average draw including radio peaks
- Solar can sustain low-duty sensors with adequate storage
- Supercapacitors smooth burst TX current on weak cells
- Monitor battery voltage and alert before brownout

## Connectivity Patterns

| Link | Strength | Typical fit |
|---|---|---|
| Wi-Fi | High bandwidth, higher power | Mains-powered cameras, hubs |
| Zigbee/Z-Wave | Mesh, low power | Battery sensors, lights |
| LoRa | Long range, low bandwidth | Outdoor / agricultural telemetry |
| BLE | Short range, low power | Wearables, proximity |
| Thread | Low-power IPv6 mesh (802.15.4) | Matter fabric members |

## Reliability

- Hardware/software watchdog to recover wedged loops
- Persist critical state across power cycles
- Heartbeat/ping so silent failures surface
- Graceful degradation when cloud or WAN is down
- Redundant sensors on critical measurements

## Data Considerations

- Match sample rate to the decision you need; avoid hoarding raw streams
- Prefer on-device or edge aggregation before WAN publish
- Synchronize clocks (NTP or equivalent) when timestamps matter
- Retain important readings locally through outages
- Document retention so SD/flash wear stays predictable

## Debugging

- Serial logs during bring-up; strip or rate-limit in production builds
- MQTT debug topics for field diagnostics
- LED/status patterns for quick visual health
- Rate-limit remote logging so diagnostics do not congest the mesh
- Sensor simulators/fixtures to test logic without waiting on hardware

## Vendor Lock-in

- Prefer devices with local APIs (local Tuya paths, Shelly, Tasmota-compatible)
- Treat cloud-only appliances as higher risk if the vendor shuts down
- Open protocols (MQTT, Zigbee, Matter) over opaque proprietary stacks when choosing new hardware
- Check whether the unit is flashable before purchase when custom firmware is a requirement
- Matter improves multi-ecosystem pairing but still needs real device certification checks

## Modern protocol notes (verify on sources.md)

- Matter is an application interoperability standard; Thread is a common low-power IPv6 mesh transport underneath many Matter devices.
- Matter feature sets evolve by revision (for example water management, EV charging, and appliance classes appear in CSA/ecosystem release notes). Treat revision numbers as version-sensitive and re-check `references/sources.md` before asserting a specific cluster set.

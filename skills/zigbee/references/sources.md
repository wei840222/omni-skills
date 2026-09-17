# Sources - Zigbee Skill

Last checked: 2026-09-18

Use these primary references when verifying channel planning, stack behavior, or device-support claims. Prefer the live page over memorized snippets.

## Standards and channel background
- Connectivity Standards Alliance / Zigbee overview — alliance positioning and specification family via https://csa-iot.org/all-solutions/zigbee/
- IEEE 802.15.4 public overview — lower-layer context for 2.4GHz PHYs via https://www.ieee802.org/15/pub/TG4.html

## Popular local stacks
- Zigbee2MQTT documentation — supported adapters, pairing, and network operations via https://www.zigbee2mqtt.io/
- Zigbee2MQTT supported devices — model-level compatibility checks via https://www.zigbee2mqtt.io/supported-devices/
- Home Assistant ZHA integration — supervisor-side Zigbee hub operations via https://www.home-assistant.io/integrations/zha/

## RF and interference practice
- Zigbee2MQTT network/FAQ guidance on channels and interference — operational channel advice via https://www.zigbee2mqtt.io/guide/configuration/adapter-settings.html
- Wi-Fi / 2.4GHz coexistence notes from stack docs and adapter vendors — re-check the adapter page before locking channels 11/25/26

## Operational note
Device converters, quirks, and legal channel availability change. Before promising support for Xiaomi/Aqara, Tuya, or a specific USB coordinator, re-open the stack's current device/adapter page for that exact model.

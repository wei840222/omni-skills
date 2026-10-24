---
name: esp32
description: Build, debug, or review ESP32 firmware and hardware integrations. Use when selecting GPIO, Wi-Fi, deep-sleep wake sources, FreeRTOS tasks, memory, peripherals, OTA, or power design for ESP32-family devices.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"✨"}'
---

## Start here

1. Identify the exact chip variant, board, framework (ESP-IDF, Arduino-ESP32, or another supported runtime), ESP-IDF/Arduino version, and requested behavior.
2. Load `references/esp32-guidelines.md` for pin, sleep, Wi-Fi, task, memory, peripheral, OTA, or power guidance.
3. Verify board-specific pin assignments and version-specific APIs against the framework documentation before proposing a wiring or firmware change.
4. State the applicable chip/framework caveat with the recommendation. With unknown board, chip, or framework version, first obtain those details, then give pin-level or API-level instructions.

## Scope boundary

Use this skill for ESP32-family hardware and firmware constraints. The reference organizes the decision areas so routine work loads one focused source instead of a broad, always-loaded pin list.

## Fast routing

- Pin assignment or analog input: GPIO and analog input.
- Battery wakeup or retained data: Deep sleep and wakeup.
- Connection instability: Wi-Fi.
- Resets, stalls, or task timing: FreeRTOS and watchdogs.
- Heap pressure: Memory.
- Electrical or field-update risk: Peripherals or OTA and power.

# Domain Knowledge: Arduino

## Overview

Arduino is an open-source electronics platform for interactive hardware. Boards such as Uno (ATmega328P, 5V) and ESP32-class modules (typically 3.3V logic) are programmed with Wiring-style C++ sketches (`.ino`) through the Arduino IDE / CLI toolchain.

## Operational Facts Agents Must Respect

- Logic-level mismatch (5V ↔ 3.3V) can damage pins; use level shifting when required.
- USB host ports commonly supply about 500 mA; motors, servos, and dense LED loads need an external supply with shared ground.
- Uno-class boards have about 2 KB SRAM; the Arduino `String` class can fragment heap — prefer `char` buffers, `F()`, and `PROGMEM` for constants.
- Prefer non-blocking `millis()` timing over `delay()` when the sketch must keep reading inputs.
- Serial Monitor holds the USB serial port; close it before uploading.

## Sources

- https://docs.arduino.cc/learn/starting-guide/whats-arduino
- https://docs.arduino.cc/learn/electronics/memory-guide
- https://docs.arduino.cc/built-in-examples/digital/BlinkWithoutDelay
- https://en.wikipedia.org/wiki/Arduino

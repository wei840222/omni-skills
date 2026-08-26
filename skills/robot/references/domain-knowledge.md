# Robotics Domain Knowledge

## Overview
This skill covers hobby-to-industrial robotics assistance: microcontroller wiring (Arduino/ESP32), sensors and actuators, ROS1/ROS2 workflows, and industrial arm motion (ABB RAPID, KUKA KRL, URScript) with safety-first defaults.

## ROS distribution freshness (as of 2026-08)
- **ROS 2 Humble Hawksbill** — LTS supported through May 2027; still the common production baseline on Ubuntu 22.04. Official overview: https://docs.ros.org/en/humble/index.html
- **ROS 2 Jazzy Jalisco** — current LTS (May 2024–May 2029) on Ubuntu 24.04; prefer for new Ubuntu 24.04 workspaces. Official overview: https://docs.ros.org/en/jazzy/index.html
- **ROS 2 Kilted Kaiju** — newer non-LTS release track; confirm package availability before recommending as default. Index: https://docs.ros.org/en/kilted/index.html
- **ROS 2 Iron Irwini** — reached end-of-life in November 2024; treat as legacy unless the user is already pinned. Status notes via https://docs.ros.org/en/rolling/Releases.html
- **ROS 1 Noetic Ninjemys** — final ROS 1 LTS; End-of-Life May 2025. Prefer migration guidance to ROS 2 rather than new Noetic greenfield work. https://wiki.ros.org/noetic

## Safety and industrial standards
- **ISO 10218-1/2** — safety requirements for industrial robots and robot systems; require clarifying simulation vs real hardware and installed safeguards before emitting motion programs. Overview via ISO store entry https://www.iso.org/standard/51330.html
- **ISO/TS 15066** — collaborative robot (cobot) safety guidance for speed-and-separation monitoring, hand-guiding, and power/force limiting. Overview via https://www.iso.org/standard/62996.html
- **Universal Robots support** — script/motion primitives and safety I/O behavior should follow vendor docs rather than guessed TCP values: https://www.universal-robots.com/articles/

## Microcontroller and sensor constraints
- **ESP32 GPIO hazards** — straps/flash pins and input-only RTC GPIOs remain common failure modes; consult Espressif GPIO docs before assigning motor or sensor pins: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html
- **HC-SR04 level shifting** — Echo is a 5 V output; 3.3 V MCUs need a divider or level shifter before GPIO input. Module characteristics summarized by SparkFun: https://www.sparkfun.com/products/15569
- **Arduino vs ESP32 PWM/servo APIs** — classic `Servo.h` / `analogWrite` assumptions do not port cleanly to ESP32; prefer board-correct APIs (`ESP32Servo`, LEDC) per Espressif / library docs.

## Motion planning heuristics that remain stable
- Prefer joint-space approach (`MoveJ` / `PTP` / `movej`) into free space, then linear segments (`MoveL` / `LIN` / `movel`) for contact or precision work.
- Treat wrist/shoulder/elbow singularities as path hazards; replan with joint moves rather than forcing linear motion through aligned axes.
- Always ask for calibrated TCP / tool name before generating paths that depend on tool-tip pose.

## Obsolete guidance corrected in this refactor
- Hardcoded `~/Clawic/data/robot/` state paths → portable `<state_root>` candidates (`./.robot/`, `~/.local/state/robot/`).
- Promotional Clawic homepage / `_meta.json` catalog residue removed.
- Absolute “never generate motion without safety discussion” phrasing softened toward verification-first prompts that still require simulation/safety confirmation.
- ROS distro name-drops updated so Iron is not implied as a current default alongside Humble.

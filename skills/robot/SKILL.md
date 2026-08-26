---
name: robot
description: Assist with robotics hardware wiring, ROS2 setup, motor control, and industrial programming. Trigger when the user needs help with Arduino/ESP32 robotics, ROS1/2, sensors, actuators, or robotic arms.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤖","os":["linux","darwin","win32"]}'
  related-skills: '{"arduino":"For Arduino specific hardware wiring.","linux":"For ROS2 environment configuration.","cpp":"For writing embedded and ROS2 C++ code."}'
---

## State location

Use `<state_root>` as the persistent storage directory for this skill following these lookup rules:
1. Workspace-local: `./.robot/` (Preferred for project-specific context)
2. Global fallback: `~/.local/state/robot/`

Create this directory structure if it does not exist.

## Architecture

Memory lives in `<state_root>/` with tiered structure. See `references/memory-template.md` for initial setup.

```
<state_root>/
├── memory.md          # HOT: inventory + active project
├── inventory.md       # Hardware owned (boards, sensors, motors)
├── projects/          # Per-project configs and learnings
│   └── {name}.md      # Project-specific notes
├── corrections.md     # What failed + fixes found
└── archive/           # Completed project summaries
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Domain knowledge & sources | `references/domain-knowledge.md` | When verifying ROS distros, industrial safety standards, or hardware constraints. |
| Memory setup | `references/memory-template.md` | When initializing a new robotics project or interpreting memory. |
| Arduino, ESP32, RPi wiring | `references/hardware.md` | When answering questions about microcontrollers or pinouts. |
| Sensors: wiring + code | `references/sensors.md` | When integrating or debugging environmental/spatial sensors. |
| Motors: types + drivers | `references/motors.md` | When selecting or controlling servos, steppers, or DC motors. |
| ROS1/ROS2, Gazebo, MoveIt | `references/ros.md` | When working on ROS frameworks, simulation, or node communication. |
| Industrial arms (ABB, KUKA, UR) | `references/industrial.md` | When writing robotic arm paths or safety-critical industrial logic. |
| Systematic troubleshooting | `references/debugging.md` | When diagnosing hardware failures, compilation issues, or unexpected behavior. |
| Common project templates | `references/projects.md` | When planning standard project architectures. |


## Core Rules

### 1. Check Memory First
Before ANY recommendation:
1. Read <state_root>/memory.md — what hardware does user have?
2. Check <state_root>/projects/ — is there an active project?
3. Check <state_root>/corrections.md — past failures to avoid?

### 2. ASK Exact Hardware
Before ANY code: exact board model, exact sensor/motor models, voltage rails.
"Arduino" is ambiguous (Uno? Nano? ESP32-based?). Add to inventory once confirmed.

### 3. Update Memory Proactively
| Event | Action |
|-------|--------|
| User mentions hardware they own | Add to inventory.md |
| User starts new project | Create projects/{name}.md |
| Something fails → fix found | Log in corrections.md |
| Project completed | Archive to archive/ |

### 4. Version Everything
Always ask and specify:
- Arduino core version, library versions
- ROS distro (Humble, Jazzy, Kilted; treat Iron/Noetic as legacy)
- Firmware versions for industrial controllers

### 5. Simulation First for Industrial
For ABB/KUKA/Fanuc/UR code:
- Always clarify: simulation or real hardware?
- Verify safety and hardware constraints before generating motion code
- Include speed limits and safety checks in ALL code

## Hardware Traps

### Board Selection
- `Servo.h` crashes on ESP32 — use `ESP32Servo.h` (different API)
- `analogWrite()` missing on ESP32 — use `ledcWrite()` + channel setup
- ESP32 GPIO 6-11 are flash pins — touching them = crash
- ESP32 GPIO 34-39 are input-only — output silently fails
- Arduino pins 0,1 are Serial — using them breaks upload

### Voltage and Current
- 5V sensor → 3.3V board without divider — burns pin permanently
- GPIO sourcing >40mA (Uno) or >12mA (ESP32) — pin damage over time
- Motor on same rail as logic — brownouts cause random resets
- No common ground between boards — erratic sensor readings

### Sensors
- HC-SR04 Echo pin 5V → 3.3V board — needs divider or level shifter
- DHT22 read interval <2s — returns stale/error values
- I2C bus >30cm without pullups — intermittent failures
- MPU6050 FIFO overflow if not read fast — readings corrupt

## ROS Traps

- Mixing `rospy` (ROS1) and `rclpy` (ROS2) — import errors
- Forgot `source install/setup.bash` — "package not found"
- QoS mismatch publisher/subscriber — messages silently dropped
- `static_transform_publisher` syntax varies by ROS2 version
- Gazebo Classic plugins ≠ Ignition/Fortress plugins

## Industrial Traps

- MoveL through singularity — joint whip, dangerous
- Wrong coordinate frame (base vs world vs tool) — unexpected position
- Omitting MoveJ before MoveL — path through obstacles
- Speed too high in shared human space — safety violation
- Bypassing SafeMove/SafetyIO signals — defeats physical safeties

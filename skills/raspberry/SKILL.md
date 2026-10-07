---
name: raspberry
description: >
  Set up, harden, and troubleshoot Raspberry Pi SBCs: power budgets, boot media,
  Imager/headless SSH, GPIO 3.3V safety, NetworkManager networking, USB/NVMe boot,
  Docker on ARM, and LED/undervoltage diagnostics. Use when the user mentions
  Raspberry Pi, Pi OS, raspi-config, GPIO headers, microSD wear, or Pi power/boot
  failures. Prefer `linux` for generic host triage, `docker` for non-Pi container
  internals, `network`/`firewall`/`wireguard` for broader networking, and `iot` or
  `smart-home` when the Pi is only one device in a multi-protocol plan.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🍓","os":["linux","darwin"]}'
  related-skills: '{"docker":"Container Engine install and image/runtime debugging once the Pi host is stable.","firewall":"Host or edge firewall rules after Pi exposure decisions.","iot":"Multi-protocol device planning when the Pi is one node among others.","linux":"Generic Linux host triage beyond Pi-specific boot, power, and GPIO.","network":"Broader LAN design when Pi networking is only one segment.","smart-home":"Hub and room automation product choice when Pi is an appliance host.","wireguard":"VPN overlay when remote Pi access should not rely on forwarded SSH."}'
---

This skill is stateless and does not store local configuration or persistent user state. Keep inventory notes, hostnames, and credentials in ordinary user files outside the skill package.

# Raspberry Pi

Board-centric guidance for flagship Raspberry Pi SBCs (and closely related Zero / keyboard models where noted): power integrity, durable boot media, first-boot and headless access, 3.3V GPIO safety, networking, storage/boot modes, Docker on ARM, and LED-based diagnostics.

## When to load

Load this skill when the request is **Raspberry Pi-specific**, for example:

- choosing a power supply for Pi 4 / Pi 5 / Zero
- flashing Raspberry Pi OS with Imager and enabling headless SSH
- undervoltage, red/green LED patterns, or boot failures
- GPIO voltage mistakes, pin mux (I2C/SPI/UART/PWM), or motor drive isolation
- microSD wear, USB SSD / NVMe boot, or read-only kiosk root
- Docker on Raspberry Pi OS / ARM image constraints
- securing remote access without raw SSH port-forward

Prefer sibling skills when the problem is already broader: `linux` for generic host triage, `docker` for Engine/image internals after the board boots, `network` / `firewall` / `wireguard` for LAN or VPN design, `iot` / `smart-home` when the Pi is only one node in a multi-protocol plan.

## Quick workflow

1. **Power first** — match official current guidance (Pi 5 → 27 W USB-C; Pi 4/400 → 3A USB-C; earlier micro-USB boards → 2.5A). Treat undervoltage LEDs as a stop-the-line signal before chasing software bugs.
2. **Boot media** — prefer durable media (USB SSD / NVMe where the model supports it) for write-heavy workloads; keep quality microSD for light or bootloader-only roles.
3. **Image + customize** — use Raspberry Pi Imager; set hostname, user (not deprecated default-only `pi` flows), Wi-Fi country, and SSH **before** first boot when headless.
4. **Network safely** — prefer DHCP reservation on the router; use `nmcli` static IP only when required. Do not expose SSH by WAN port-forward; prefer Tailscale, Raspberry Pi Connect, Cloudflare Tunnel, or WireGuard (`wireguard`).
5. **GPIO discipline** — all user GPIO is 3.3V-tolerant; never feed 5V logic into inputs; drive motors through a proper driver/H-bridge, not bare pins.
6. **Containers last** — install Docker from current Docker docs for the OS arch; pull `linux/arm64` or `linux/arm/v7` images; keep container volumes off dying microSD cards.
7. **Verify sources** — version-sensitive power, boot, LED, and OS claims against URLs in `references/sources.md`.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/rules.md` | Power, storage, GPIO, network, Docker, headless, performance, troubleshooting rules |
| `references/sources.md` | Official Raspberry Pi / Docker / GPIO Zero docs used for Gate 6 freshness |

## Safety boundaries

- Do not invent amperage, pin numbers, or boot OTP steps from memory when they affect hardware safety—open `references/rules.md` and `references/sources.md`.
- Do not store passwords, Wi-Fi PSKs, or SSH private keys inside the skill package.
- Do not recommend permanent OTP programming (`program_usb_boot_mode` and similar) without stating that OTP changes are irreversible.
- Treat third-party HATs and “5V Arduino” modules as hostile until their logic level is verified.

## Non-goals

- Do not turn this skill into a full Linux distro manual (`linux`), Docker Engine deep-dive (`docker`), or multi-protocol home hub design (`iot` / `smart-home`).
- Do not restate complete pin mux tables in `SKILL.md`; load `references/rules.md` and pinout/GPIO Zero when wiring details matter.
- Do not keep parallel “tips” lists that duplicate `references/rules.md`.

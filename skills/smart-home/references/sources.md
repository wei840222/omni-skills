# Sources — smart-home

Last checked: 2026-09-18

Use these primary references when verifying protocol, Matter/Thread, local-control, or IoT segmentation claims. Prefer the live page over memorized snippets.

## Protocols and interoperability

- **Connectivity Standards Alliance — Matter** — multi-admin smart-home application layer over Thread, Wi-Fi, and Ethernet; use for ecosystem interoperability claims — https://csa-iot.org/all-solutions/matter/
- **Thread Group — What is Thread** — low-power IPv6 mesh used under Matter; use for Thread vs Wi-Fi vs Zigbee framing — https://www.threadgroup.org/What-is-Thread/Thread-Benefits
- **Zigbee Alliance / CSA — Zigbee** — mature 2.4 GHz mesh for sensors and actuators; pair with stack docs before compatibility claims — https://csa-iot.org/all-solutions/zigbee/
- **Z-Wave Alliance — Learn about Z-Wave** — sub-GHz mesh often chosen for wall penetration and locks/switches — https://www.z-wave.com/learn

## Local control platforms

- **Home Assistant — Architecture / integration model** — local-first hub patterns and integration boundaries — https://www.home-assistant.io/docs/
- **Home Assistant — Best practices and system requirements** — host sizing and operational expectations for always-on controllers — https://www.home-assistant.io/installation/
- **Apple — HomeKit secure remote access overview** — local execution with optional secure relay framing for Apple homes — https://support.apple.com/guide/security/homekit-security-overview-secde29b4dcd/web

## Network isolation and IoT risk

- **CISA — Securing Internet-Connected Devices** — baseline consumer IoT hygiene (defaults, updates, segmentation mindset) — https://www.cisa.gov/news-events/news/securing-internet-connected-devices
- **NISTIR 8259A — IoT Device Cybersecurity Capability Core Baseline** — device capability expectations useful when advising purchase/security baselines — https://csrc.nist.gov/publications/detail/nistir/8259a/final
- **NIST SP 800-193 — Platform Firmware Resiliency** — firmware update and integrity framing when discussing long-lived hubs and routers — https://csrc.nist.gov/publications/detail/sp/800-193/final

## Practical hub and mesh ops

- **Zigbee2MQTT — Getting started / supported devices** — common local Zigbee bridge used beside Home Assistant — https://www.zigbee2mqtt.io/
- **Z-Wave JS — Documentation** — common local Z-Wave driver stack used by modern hubs — https://zwave-js.github.io/node-zwave-js/

## Notes for reviewers

- Prefer manufacturer model pages and stack compatibility lists over marketing “works with everything” claims.
- Treat cloud-only assistants as convenience layers; reliability guidance still centers local execution paths documented above.

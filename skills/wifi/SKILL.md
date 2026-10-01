---
name: wifi
description: >
  Troubleshoot wireless networks, optimize channels/bands, diagnose speed drops
  and interference, place routers, and harden home Wi-Fi security (WPA2/WPA3,
  WPS, guest SSIDs). Use when the user reports kitchen/microwave dead zones,
  sticky band steering, weak RSSI, roaming drops, extender vs mesh choices, or
  asks whether to hide the SSID. Prefer `network` for wired/DNS/routing/TLS
  reachability outside the radio layer, and `wireguard`/`vpn` for tunnel VPNs.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📶"}'
  related-skills: '{"network":"Layer-3 reachability, DNS, routing, firewall, and TLS diagnosis beyond the wireless radio.","wireguard":"WireGuard tunnel setup when the issue is VPN pathing, not Wi-Fi airtime.","vpn":"VPN provider selection and privacy trade-offs outside local WLAN design."}'
---

# WiFi

Domain guidance for **home and small-office WLAN**: band/channel choice, interference, placement, guest isolation, and baseline security. This skill is **stateless** — it does not store credentials or persistent device inventories in the package.

## When to load

Load for wireless-specific work:

- speed drops, sticky 5 GHz, 2.4 GHz congestion, microwave/USB 3.0 interference
- RSSI checks, channel scans, DFS pauses, packet-loss isolation (router vs ISP)
- router placement, mesh vs range-extender trade-offs
- WPA2-Personal minimum / WPA3-SAE, disable WPS, guest network isolation
- Wi-Fi 6E 6 GHz client fallback and Wi-Fi 7 Multi-Link Operation (MLO) context

Prefer other skills when the ask is mainly:

- DNS, routing, NAT, firewall, TLS → `network`
- WireGuard peers / AllowedIPs → `wireguard`
- VPN provider shopping → `vpn`

## Routing

Load supporting references only when needed:

- **Bands, channels, speed, drops, diagnostics** → `references/troubleshooting.md`
- **WPA/WPS/SSID/guest hardening** → `references/security.md`
- **Placement, mesh vs extenders** → `references/placement.md`
- **Gate 6 primary sources** → `references/sources.md`

## Core rules

1. **Isolate the radio first** — ping the gateway LAN IP before blaming the ISP; then check RSSI (roughly weaker than about −70 dBm is poor for interactive use).
2. **Name the band** — 2.4 GHz reaches farther but is crowded; 5 GHz is faster with shorter range; 6 GHz (Wi-Fi 6E/7 capable clients) needs device support and falls back when unsupported.
3. **Security floor** — WPA3-Personal (SAE) when the client set supports it; otherwise WPA2-Personal. Treat WEP/WPA-legacy and WPS PIN mode as unsafe defaults to replace.
4. **Guest path** — put untrusted/IoT clients on an isolated guest SSID with its own passphrase; do not rely on hidden SSID or MAC filters as security.
5. **Capacity vs coverage** — a single well-placed AP often beats a poorly placed extender; mesh with dedicated (ideally wired) backhaul beats same-channel repeaters that halve airtime.

## Safety

- Never commit real Wi-Fi passphrases, router admin passwords, or ISP credentials into the skill tree or git.
- Use placeholders such as `<WLAN_PASSPHRASE>` in examples.
- Do not claim a hidden SSID or MAC allow-list is a confidentiality control.

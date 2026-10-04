# Sources (Gate 6)

Full URLs verified while refactoring this skill. Re-check before restating
protocol behavior, product marketing claims, or platform policy.

## Agent skill format

- Agent Skills specification index: https://agentskills.io/llms.txt
- Agent Skills specification: https://agentskills.io/specification
- Reference validator package: https://github.com/agentskills/agentskills/tree/main/skills-ref

## VPN privacy threat model

- EFF Surveillance Self-Defense — Choosing the VPN That’s Right for You:
  https://ssd.eff.org/module/choosing-vpn-thats-right-you  
  Takeaways: a VPN routes traffic through another network and can mask IP from
  sites and local network observers; the VPN operator sees traffic metadata the
  ISP no longer does; VPNs are not complete anonymity tools; payment and
  fingerprinting still identify users; useful mainly for untrusted networks and
  some censorship/geo paths, not as a sole security stack.

## WireGuard protocol and ports

- WireGuard protocol & cryptography: https://www.wireguard.com/protocol/  
  Takeaway: all WireGuard packets are sent over **UDP**.
- WireGuard conceptual overview: https://www.wireguard.com/  
  Takeaway: WireGuard securely encapsulates IP packets over UDP; examples show
  diverse endpoint UDP ports, not a single mandatory listener.
- wireguard-tools `wg(8)` manual:
  https://git.zx2c4.com/wireguard-tools/about/src/man/wg.8  
  Takeaways: `ListenPort` is optional; if omitted or `0`, a random port is
  chosen when the interface comes up; `PersistentKeepalive` may be set (e.g.
  25s) to refresh NAT mappings; example configs often show `51820` but that is
  not a protocol-fixed port.

## OpenVPN transport

- OpenVPN 2.6 reference manual:
  https://openvpn.net/community-resources/reference-manual-for-openvpn-2-6/  
  Takeaways: OpenVPN supports TCP or UDP tunnel transport; `--proto`
  selects `tcp` or `udp` (with optional `4`/`6` suffix); TCP profiles remain a
  documented fallback when UDP is blocked.

## PPTP historical status

- IETF RFC 2637 (PPTP): https://datatracker.ietf.org/doc/html/rfc2637  
  Takeaway: PPTP is a 1999-era PPP-tunneling specification; do not treat it as
  a modern confidentiality baseline. Prefer WireGuard, OpenVPN TLS mode, or
  current platform IKEv2/IPsec guidance instead of PPTP for new setups.

## Notes on claims

- “Provider sees all traffic” is refined to: operator sees tunnel egress
  metadata and any unencrypted payloads; HTTPS still encrypts site content.
- Free-VPN monetization is a default caution, not a universal proven fact for
  every brand — verify the specific operator when making purchase advice.
- WireGuard battery advantage on mobile is commonly reported but
  device/client-specific; measure rather than quote a fixed percentage.

## Claim inventory (refactor)

| Claim class | Example | Disposition |
|---|---|---|
| stable-domain | VPN shifts trust to operator | retained + EFF citation |
| stable-domain | DNS can bypass tunnel | retained with verification step |
| stable-domain | Kill switch fail-closed | retained with test method |
| obsolete/wrong | "WireGuard uses fixed ports" | replaced with UDP + configurable ListenPort |
| version-sensitive | OpenVPN `--proto` tcp/udp | cited OpenVPN 2.6 manual |
| platform-specific | Wi‑Fi calling / banking blocks | retained as conditional, not universal |
| marketing | free VPN always sells data | softened to default caution pending operator docs |

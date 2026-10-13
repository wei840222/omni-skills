---
name: firewall
description: >
  Design and troubleshoot host and cloud firewall policy: UFW/nftables/iptables,
  dual-layer provider rules, SSH lockout prevention, Docker publish bypass,
  IPv6 parity, and outside-in verification. Use when opening or closing ports,
  hardening a VPS first boot, debugging "timeout vs refused", aligning cloud
  security groups with OS filters, or fixing published-container exposure.
  Prefer `docker` for Compose/publish mechanics, `wireguard`/`vpn` for tunnel
  ports, `vps` for full box lifecycle, and `network` for generic reachability.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛡️"}'
  related-skills: '{"docker":"Container publish, bridge networking, and DOCKER-USER filter placement when exposure is container-driven.","wireguard":"WireGuard ListenPort and peer path once the remaining work is WG-specific.","vpn":"VPN client/provider transport ports and kill-switch expectations outside host filter design.","vps":"Rented-box first boot, dual-layer firewalls, and lockout recovery as part of VPS lifecycle.","network":"Generic reachability, DNS, routing, and TLS diagnosis when firewall is only one hop.","linux":"Host sysctl, forwarding, and distribution firewall backends under the OS.","security-best-practices":"Application-layer secure-by-default review beyond packet filters.","nginx":"Reverse-proxy and TLS termination once only 80/443 should face the internet."}'
---

# Firewall

Host packet filters and cloud network firewalls for servers. Keep always-needed
safety and routing here; load detailed procedures only when the task needs them.

This skill is **stateless**. Keep live rule dumps, allowlists, and break-glass
notes in ordinary operator files outside the skill package.

## When to use

- First-boot hardening: default-deny inbound, allow admin path, then enable
- Opening or closing SSH, HTTP/HTTPS, VPN, mail, DNS, or monitoring ports
- Dual-layer design: provider/cloud firewall plus OS firewall
- Docker publish paths that ignore UFW `INPUT` rules
- IPv4/IPv6 parity and "IPv4 locked, IPv6 open" failures
- Outside-in checks: connection refused vs timeout, provider logs, port scans
- Recovering from lockout via provider console or serial/out-of-band access

Prefer `docker` when the problem is Compose publish or container networking.
Prefer `wireguard` / `vpn` when the remaining work is tunnel config.
Prefer `vps` for provider plan, snapshots, and full box lifecycle.
Prefer `network` for generic offline/DNS/routing triage.

## Safety order (always)

1. Confirm **out-of-band** access (provider console, serial, second session) before enabling a new default-deny policy.
2. **Allow the admin path first** (SSH or other remote management), then set defaults, then enable.
3. Keep a second live session open and verify the new rule from an external path before closing the first session.
4. Prefer **default deny inbound**, allow outbound unless the threat model needs egress control.
5. Treat every open port as intentional attack surface; name the service owner for each allow rule.
6. Apply the same intent on **IPv4 and IPv6** unless IPv6 is explicitly disabled end-to-end.
7. After changes, verify from **outside** the host network, not only with local `status`.

## Quick workflow

1. **Scope** — host OS firewall, cloud/provider firewall, or both; IPv4/IPv6; Docker/public publish.
2. **Inventory** — required inbound ports, source CIDRs, admin IP stability, UDP vs TCP.
3. **Admin path** — allow SSH (or serial/console plan) before enable; use a second session.
4. **Defaults** — deny inbound (and forwarded if acting as router only when intended); allow outbound unless restricting egress.
5. **Service allows** — least privilege: port + proto + source; avoid "temporary" any/any.
6. **Docker check** — published ports may bypass UFW `INPUT`; bind to localhost + reverse proxy, use provider firewall, or filter via `DOCKER-USER`.
7. **Verify** — `status` locally, then external connect; distinguish refused (closed/reject) vs timeout (drop/filter).
8. **Load detail** — open the matching reference below before citing vendor-specific behavior.

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/domain.md` | Operating rules, ports, dual-layer design, Docker, IPv6, debug, mistakes |
| `references/operations.md` | Concrete UFW / nftables / verification command sequences |
| `references/sources.md` | Before restating UFW, Docker, AWS, DigitalOcean, or Hetzner facts |
| `test-prompts.json` | Evaluation harness only — not runtime guidance |

## Routing to sibling skills

- Container image, Compose, or publish flags → `docker`
- WireGuard peers / AllowedIPs → `wireguard`
- Commercial VPN client privacy → `vpn`
- Whole VPS lifecycle (snapshots, resize, abuse) → `vps`
- Broad connectivity triage → `network`
- App-layer secure coding review → `security-best-practices`

## Failure recovery

- Locked out after enable: use provider console/serial first, open admin CIDR at the cloud layer, then fix guest rules with a second session (`references/operations.md`).
- Published container still reachable with UFW deny: expect Docker NAT bypass; move to loopback publish, provider FW, or `DOCKER-USER` (`references/domain.md`).
- Timeout with local ALLOW: inspect cloud attachment, IPv6 path, and public IP before rewriting the same UFW rule.

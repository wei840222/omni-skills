# Firewall domain rules

Runtime guidance for host and cloud packet filters. Prefer positive procedures
over stop-only warnings. Cite `references/sources.md` before hard vendor claims.

## Critical first steps

- Establish provider console, serial, or another out-of-band path before enabling default-deny.
- Add the remote-admin allow rule (SSH or equivalent) **before** `enable`.
- Keep a second session open; confirm external reachability of the admin path after enable.
- Use dry-run or numbered status reviews when the tool supports them (`ufw --dry-run`, `ufw status numbered`).

## Default stance

- Default **deny** inbound; open only what a named service needs.
- Default **allow** outbound for typical app hosts; tighten egress when the threat model requires it.
- Default **deny** forwarded/routed traffic unless the host is an intentional router.
- Every allow rule should record port, protocol, source, and owning service.

## Essential ports

- **SSH** (22/tcp or custom): required for remote admin; prefer source IP/CIDR limits when the admin path is stable.
- **HTTP** (80/tcp): only with a real listener; also used for HTTP-01 certificate challenges.
- **HTTPS** (443/tcp): production web front doors.
- **Databases** (3306, 5432, 27017, …): keep off the public internet; reach via SSH tunnel, VPN, or private network.
- **VPN examples**: WireGuard often uses UDP (common lab example `51820/udp`, not a protocol-fixed port); OpenVPN commonly `1194` TCP or UDP — confirm the actual listener.
- **Mail** (25, 465, 587) and **DNS** (53 TCP/UDP): only if this host is the mail or DNS server.
- Monitoring agents usually need **outbound** to collector endpoints rather than inbound public ports.

## Provider / cloud firewalls

- Cloud firewalls (Hetzner, DigitalOcean, AWS security groups, and similar) filter **before** traffic reaches the guest OS — lower host load, faster drop.
- Many provider products are **stateful**: allowed inbound flows receive return traffic without a separate outbound mirror rule (confirm per product).
- DigitalOcean Cloud Firewalls: network-based, stateful; traffic not expressly permitted is blocked; deny rules take precedence over overlapping allows when both exist.
- Hetzner Cloud Firewalls: with no rules, inbound is blocked and outbound is permitted by default; traffic matching an allow rule is permitted.
- AWS security groups: control inbound and outbound for associated instances; changes apply to all instances using the group; you can still run an OS firewall for defense in depth.
- Apply cloud policies to groups/tags for consistency; combine cloud + OS filters when both are available.

## IP restrictions

- Limit SSH (and other admin ports) to known admin CIDRs when IPs are stable.
- Home IPs change — plan VPN with static egress, update rules, or keep console break-glass.
- Use CIDR carefully: `/32` is one IPv4 host; `/24` is 256 addresses.
- Dynamic DNS in cloud rules is product-specific; verify support before relying on it.

## Docker and published ports

- On Linux, Docker installs its own iptables/nftables rules for **bridge** networks (not for `ipvlan` / `macvlan` / `host`).
- Docker and UFW are **incompatible** for published ports: Docker NATs container traffic so packets can miss UFW `INPUT`/`OUTPUT` chains and ignore UFW policy.
- Do not edit Docker-managed chains casually; put extra filters in **`DOCKER-USER`** (processed before Docker's own forward rules).
- Safer public exposure patterns:
  1. Publish to `127.0.0.1` only and terminate TLS on a host reverse proxy.
  2. Rely on a **provider** firewall in front of the host.
  3. Restrict sources with explicit `DOCKER-USER` rules (match original dest with `conntrack` when needed).
- Disabling Docker iptables (`iptables: false`) often breaks bridge networking; treat as advanced and out of default scope.

## IPv6

- Configure IPv4 and IPv6 with the **same intent**, or disable IPv6 end-to-end deliberately.
- UFW: IPv6 filtering follows `/etc/default/ufw` `IPV6=yes|no`; dual-stack rules such as `ufw allow 22` apply to both when IPv6 is enabled.
- Provider dashboards may show one policy covering both families or separate controls — read the product page for the account in use.
- Attackers probe IPv6 when only IPv4 looks locked down.

## Debugging

- Test from a network path that is **not** the host itself (phone tether, external VPS, provider netcat).
- **Connection refused** usually means a local stack rejected the port (nothing listening or reject policy).
- **Connection timeout** often means silent drop (filter, blackhole, or asymmetric path).
- Provider firewall UIs frequently expose drop counters or logs — use them before rewriting OS rules.
- Confirm the firewall is actually enabled (`ufw status`, nft list, security-group attachment), not only that a rules file exists.

## Common failure patterns (and fixes)

| Pattern | Fix |
|---|---|
| "Temporary" open port left forever | Calendar review; tag owner; close when service retires |
| 80/443 open with no web server | Remove allows until a listener exists |
| UDP forgotten (DNS, VPN, games) | Match protocol to the real listener |
| Firewall installed but never enabled | Enable only after admin allow + second session |
| IPv4 hardened, IPv6 open | Dual-stack rules or explicit IPv6 off |
| Non-standard SSH port as only control | Keep source allowlists and keys; port moves are delay, not authorization |
| UFW "blocks" Docker publish but port still open | Expect Docker bypass; use localhost bind, provider FW, or `DOCKER-USER` |

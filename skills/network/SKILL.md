---
name: network
description: Diagnose network reachability, DNS, routing, firewall, NAT, VPN, port, and TLS issues. Use when the user needs to troubleshoot connectivity, interpret network behavior, or plan a safe network change.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"vpn":"Covers VPN selection and configuration beyond network diagnosis.","wifi":"Covers wireless-network setup and troubleshooting.","wireguard":"Covers WireGuard-specific configuration and operations."}'
---

# Network Fundamentals

Load [`references/network-standards.md`](references/network-standards.md) when verifying a port-range, private-address, DNS, TLS, or certificate-lifetime claim before advising a user or changing configuration.

## TCP/IP Basics
- TCP guarantees delivery with retransmission — use for reliability (HTTP, SSH, databases)
- UDP is fire-and-forget — use for speed when loss is acceptable (video, gaming, DNS queries)
- On Unix-like systems, binding ports below 1024 normally requires privilege (subject to host policy or capabilities); higher ports are not reserved by that rule — common services have well-known ports
- Ephemeral ports for client connections — OS assigns an available client-side port for the connection; validate the platform’s configured range when it matters

## DNS
- DNS resolution is cached at multiple levels — browser, OS, router, ISP — compare authoritative and resolver answers when debugging
- TTL determines cache duration — lower before migrations, raise after for performance
- A record for IPv4, AAAA for IPv6, CNAME for aliases, MX for mail
- Use A or AAAA records, or a provider-supported alias, at a zone apex; a CNAME cannot coexist with other data at the same owner name
- `dig` and `nslookup` query DNS directly — test against a selected resolver or authoritative server for a precise comparison

## IP Addressing
- Private IPv4 ranges: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16 — do not route them on the public Internet
- CIDR notation: /24 contains 256 IPv4 addresses; /16 contains 65,536 — each prefix bit halves or doubles the address count
- 127.0.0.1 is the IPv4 loopback address; 0.0.0.0 commonly represents an unspecified address or all local IPv4 interfaces in a bind context, not a normal destination
- NAT translates private to public IPs — most home/office networks use this
- IPv6 does not require NAT for address conservation; dual-stack with IPv4 remains common

## Common Ports
- 22: SSH — 80: HTTP — 443: HTTPS — 53: DNS
- 25/465/587: SMTP (mail sending) — 143/993: IMAP — 110/995: POP3
- 3306: MySQL — 5432: PostgreSQL — 6379: Redis — 27017: MongoDB
- 3000/8080/8000: Common development servers
- IANA designates 0–1023 as System Ports, 1024–49151 as User Ports, and 49152–65535 as Dynamic and/or Private Ports; registered assignments identify conventions, not a firewall allow-list

## Troubleshooting Tools
1. Confirm the target name, address family, port, protocol, and client location before changing network configuration.
2. Resolve DNS with `dig` or `nslookup`; compare the selected resolver's answer with authoritative data when a change is recent.
3. Test the intended transport: `ping` can test ICMP reachability, while `nc -vz <host> <port>` or `curl -v https://<host>/` tests a TCP service.
4. Trace the path with `traceroute`/`tracert`; use the observed hop where traffic stops to narrow routing or filtering checks.
5. Inspect local listeners with `ss -tulpn` (Linux) or the platform equivalent before changing a firewall or port-forward rule.
6. Capture only the relevant interface, host, and port with `tcpdump` or Wireshark when previous checks disagree; redact credentials and payloads before sharing captures.

A missing ICMP reply can indicate filtering rather than downtime. Verify the service through its intended protocol before declaring the target unavailable.

## Firewalls and NAT
- Stateful firewalls track connections — allow response to outbound requests automatically
- Port forwarding maps external port to internal IP:port — required to expose services behind NAT
- Hairpin NAT for internal access to external IP — not all routers support it
- UPnP auto-configures port forwarding — convenient but security risk, disable on servers

## Load Balancing
- Round-robin distributes sequentially — simple but ignores server capacity
- Least connections sends to least busy — better for varying request durations
- Health checks remove dead servers — configure appropriate intervals and thresholds
- Sticky sessions (affinity) keep user on same server — needed for stateful apps, breaks scaling

## VPNs and Tunnels
- VPN encrypts traffic to exit point — all traffic appears from VPN server IP
- Split tunneling sends only some traffic through VPN — reduces latency for local resources
- WireGuard is modern and fast — simpler than OpenVPN, better performance
- SSH tunnels for ad-hoc port forwarding — `ssh -L local:remote:port` creates secure tunnel

## SSL/TLS
- Prefer TLS 1.3 where both peers support it; retain TLS 1.2 only when required for compatible clients, and disable obsolete protocol versions under the service's current security policy
- Certificate chain: leaf → intermediate → root — missing intermediates cause validation failures
- SNI allows multiple certificates on one IP; clients without SNI receive the default certificate
- Let's Encrypt certificates are short-lived; automate renewal and monitor the issuer's current certificate-lifetime policy

## Common Mistakes
- Treat DNS propagation as resolver-specific cache expiry; query the authoritative server and a chosen resolver before changing records again
- Permit the ICMP messages required by the environment, including path-MTU discovery where applicable, rather than applying a blanket block
- Check IPv6 and IPv4 policy together when the service is dual-stack
- Use stable hostnames or documented service-discovery names when endpoints can change
- Test the protocol a service actually uses; DNS, VPN, and games may depend on UDP as well as TCP
- Measure latency and throughput separately; high bandwidth does not guarantee low latency
- Limit packet captures to the smallest useful scope and protect any captured sensitive payloads

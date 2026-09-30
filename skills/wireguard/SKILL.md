---
name: wireguard
description: Configure and troubleshoot WireGuard VPN tunnels, peers, AllowedIPs
  routing, key management, NAT keepalives, and DNS-leak hardening. Use when writing
  wg-quick configs, diagnosing handshake failures, planning full-tunnel vs split-tunnel
  routes, or exchanging public keys safely. Prefer `vpn` for provider selection and
  privacy trade-offs, `network` for generic reachability diagnosis, and `firewall`
  for host packet-filter rules around the tunnel.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔐","requires":{"bins":["wg"]}}'
  related-skills: '{"vpn":"Provider selection, privacy trade-offs, and non-WireGuard VPN clients.","network":"Layer-3 reachability, DNS, and routing diagnosis outside WireGuard specifics.","firewall":"Host and cloud packet filters that must allow UDP ListenPort.","encryption":"Broader crypto algorithm choice beyond WireGuard key handling.","dns":"Resolver and leak fixes once tunnel DNS is configured.","linux":"Host forwarding, sysctl, and systemd concerns around the tunnel."}'
---

## When to load

Load this skill for **WireGuard-specific** work: `wg` / `wg-quick` config, peer keys, `AllowedIPs` semantics, handshake failures, PersistentKeepalive, DNS-in-tunnel, IP forwarding/NAT for exit nodes, and live `wg set` / `wg syncconf` changes.

Do **not** load as the primary skill for generic VPN-provider shopping (`vpn`), broad connectivity triage (`network`), or firewall policy design alone (`firewall`).

## State location

Optional peer inventories, endpoint notes, and lab topology sketches may live under `<workspace>/wireguard/`, `<workspace>/memory/wireguard/`, or `~/wireguard/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when available.
2. Otherwise the first existing directory in that order.
3. If multiple exist, use only the highest-precedence path and report duplicates.
4. Create `<workspace>/wireguard/` only with user consent when no candidate exists.

Keep private keys, `wg0.conf`, and PSK material **out of the skill package and out of git**. Prefer placeholders such as `<SERVER_PRIVATE_KEY>` in examples.

## Routing

Load supporting references only when needed:

- **Config patterns / AllowedIPs / keepalive**: `references/wireguard-guide.md`
- **Commands, live changes, debugging**: `references/operations.md`
- **Gate 6 primary sources**: `references/sources.md`

## Core operations

### 1. Keys stay local

Generate private keys on each host; exchange **only** public keys (and optional PSKs out-of-band). Never paste a private key into chat logs, tickets, or the skill tree.

```bash
umask 077
wg genkey | tee server.key | wg pubkey > server.pub
wg genkey | tee client.key | wg pubkey > client.pub
# optional: wg genpsk > psk.txt
```

Set config and key file modes to `600` before `wg-quick up`.

### 2. AllowedIPs means different things on each side

| Side | `AllowedIPs` meaning |
| --- | --- |
| Peer entry on a server | Crypto-routing filter: which source addresses that peer may send |
| Peer entry on a client | Which destinations to **route into** the tunnel (policy routing) |

Rules of thumb:

- One host peer: `10.0.0.2/32` on the server; matching tunnel address on the client.
- Full-tunnel client: `0.0.0.0/0` and/or `::/0` **and** exclude the server's public endpoint from the tunnel (wg-quick handles this via its routing table helpers; do not double-route the endpoint into itself).
- Overlapping `AllowedIPs` across peers is undefined — each prefix should map to one peer.

### 3. Handshake and NAT

- No recent handshake → wrong public key, UDP blocked, wrong endpoint, or clock skew. Check all four.
- Peers behind NAT need `PersistentKeepalive = 25` (seconds) on the side that must keep the mapping open (usually the client).
- WireGuard is **UDP only**; open the `ListenPort` (default often `51820/udp`) on path firewalls.

### 4. DNS leaks on full tunnel

A full tunnel without `DNS =` in the client interface still lets OS DNS bypass the tunnel. Set tunnel DNS explicitly when privacy of name resolution matters, then verify with a resolver that is only reachable via the tunnel.

### 5. Exit-node / site-to-site routing

Linux exit nodes need:

1. `net.ipv4.ip_forward=1` (and IPv6 forwarding if used)
2. Masquerade/SNAT on the WAN interface for client internet access
3. Firewall allow for `UDP/ListenPort` and forwarded traffic you intend to permit

### 6. Live changes without full bounce

Prefer `wg set` for a single peer tweak, or `wg syncconf <iface> <(wg-quick strip <iface>)` after editing the wg-quick file, so existing handshakes are not needlessly dropped. Use `wg show` and handshake age as the health signal.

## Failure recovery

| Symptom | Check first | Fix direction |
| --- | --- | --- |
| Interface up, no handshake | Keys, endpoint IP:port, UDP path | Correct pubkey/endpoint; open UDP |
| Handshake OK, one-way traffic | `AllowedIPs` both sides, rp_filter | Align prefixes; allow return path |
| Works then dies ~2 min | NAT mapping | `PersistentKeepalive = 25` on NAT side |
| Full tunnel “works” but sites know you | DNS / WebRTC / IPv6 leak | Tunnel DNS; disable or tunnel IPv6 deliberately |
| `wg-quick` refuses start | File mode / parse error | `chmod 600`; fix INI sections |

## Safety

- Treat every `*.conf` that embeds `PrivateKey` as secret material.
- Do not disable peer identity checks or share one private key across machines.
- Lab examples use RFC1918 tunnel addresses (`10.0.0.0/24` style); replace with the user's plan.
- Confirm remote access (console/SSH out-of-band) before locking firewalls around the only admin path.

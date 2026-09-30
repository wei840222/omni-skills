# WireGuard configuration guide

Operational patterns preserved and hardened from the pre-refactor skill body. Re-check live man pages via `references/sources.md` before asserting flag defaults.

## AllowedIPs traps

- **Server peer `AllowedIPs`**: addresses the peer is allowed to send (crypto routing / source filter).
- **Client peer `AllowedIPs`**: destinations the client sends **into** the tunnel.
- `0.0.0.0/0` (and `::/0`) is full-tunnel. Ensure the public endpoint is not black-holed; `wg-quick` installs policy routing helpers—do not invent a second default route that swallows the endpoint without those helpers.
- Overlapping prefixes on two peers → undefined which peer receives the packet. Keep prefixes disjoint.
- Mask mistakes fail silently: single host → `/32` (or `/128` for v6); LAN → correct subnet length.

## Connection failures

- No handshake: wrong public key, UDP blocked, wrong endpoint host/port, or interface never sent a packet (handshake is lazy—ping a tunnel IP to force one).
- One-way traffic: asymmetric `AllowedIPs` or host firewall/rp_filter dropping replies.
- NAT: set `PersistentKeepalive = 25` on the peer that sits behind NAT (commonly the client).
- Permissions: private key and conf files should be mode `600`; `wg-quick` may refuse looser modes depending on distro policy.

## DNS leaks

- Missing `DNS =` on a full-tunnel client leaves system resolvers on the physical path.
- Prefer a resolver address that is only useful via the tunnel, then test from the client.
- IPv6 dual-stack hosts can leak on `::` even when IPv4 is tunneled—decide explicitly.

## Routing and exit nodes

- Enable IP forwarding on Linux routers/exit nodes before expecting cross-interface traffic.
- Internet exit needs NAT/masquerade on the WAN egress.
- Firewall must allow **UDP** on `ListenPort` end-to-end; there is no TCP fallback in WireGuard itself.

## Key security

- Generate keys on-box; transmit only public keys.
- Optional PSK (`wg genpsk`) is an extra mutual secret—still protect it like a password.
- Rotate a compromised private key by replacing the keypair and updating every peer that listed the old public key.

## Minimal server + one peer sketch

```ini
# server wg0.conf (placeholders only)
[Interface]
PrivateKey = <SERVER_PRIVATE_KEY>
Address = 10.0.0.1/24
ListenPort = 51820

[Peer]
PublicKey = <CLIENT_PUBLIC_KEY>
AllowedIPs = 10.0.0.2/32
```

```ini
# client wg0.conf
[Interface]
PrivateKey = <CLIENT_PRIVATE_KEY>
Address = 10.0.0.2/24
DNS = 10.0.0.1

[Peer]
PublicKey = <SERVER_PUBLIC_KEY>
Endpoint = <SERVER_PUBLIC_IP>:51820
AllowedIPs = 0.0.0.0/0, ::/0
PersistentKeepalive = 25
```

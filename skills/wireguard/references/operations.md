# WireGuard operations

## Essential commands

```bash
# show interfaces, peers, latest handshakes, transfer
wg show
wg show wg0 dump

# bring conf up/down (wg-quick unit on many distros)
wg-quick up wg0
wg-quick down wg0

# live peer add without full restart
wg set wg0 peer <CLIENT_PUBLIC_KEY> allowed-ips 10.0.0.2/32

# apply edited wg-quick conf without tearing down everything
wg syncconf wg0 <(wg-quick strip wg0)
```

## Debugging checklist

1. `wg show` — handshake age. Stale (>2 minutes with keepalive expected) → path or key problem.
2. `ping` a tunnel address — forces handshake if none yet.
3. Confirm UDP connectivity to `Endpoint:ListenPort` from an external vantage (provider security groups, home router, host firewall).
4. Compare `AllowedIPs` on **both** ends against the addresses actually in use.
5. On exit nodes: `sysctl net.ipv4.ip_forward`, NAT counters, and forward chain policy.

## Live vs restart

| Change | Prefer |
| --- | --- |
| Add/remove one peer | `wg set` / `wg set ... remove` |
| Edit Address/DNS/hooks in wg-quick file | `wg-quick strip` + `wg syncconf`, or controlled bounce |
| Private key rotation | Coordinated replace on all peers; expect brief loss |

## Platform notes

- Linux: kernel WireGuard module or wireguard-go fallback; `wg-quick` from wireguard-tools.
- macOS/Windows/mobile: official apps exist; still exchange the same key and `AllowedIPs` semantics (see wireguard.com install / xplatform pages).
- Containers/NS: ensure the netns that runs `wg` is the one with the routes you intend.

## Security and remote access

### Golden rule

Keep NAS **admin and write-capable services** off the public internet unless the
user explicitly accepts the risk and compensates with strong controls.

### Secure remote access options

| Method | Complexity | Notes |
| --- | --- | --- |
| Tailscale | Easy | Overlay mesh; good default for individuals |
| WireGuard | Medium | Full control; hand detailed peers to `wireguard` |
| Cloudflare Tunnel (or similar) | Medium | No inbound port forward; still needs app auth |
| Synology QuickConnect | Easy | Convenience relay; not a hardening strategy alone |
| OpenVPN | Harder | Viable; prefer modern WireGuard when greenfield |
| Port forward + DDNS to DSM/QTS | Easy | **High risk** — avoid for admin UI |

### Common traps

1. **QuickConnect prioritizes convenience** — Acceptable for low-sensitivity
   personal use only with 2FA and strong accounts; still a relay dependency.

2. **Public DSM/QTS is a ransomware target** — Internet-wide scanners find open
   admin panels quickly.

3. **Brute force is routine** — Enable auto-block / fail2ban-style controls and
   alert on repeated failures.

4. **Prefer overlay VPN over router port forward** — Terminating remote access
   on an authenticated VPN reduces direct exposure of NAS services.

### Hardening checklist

- [ ] Default `admin` disabled or unused; named admins only
- [ ] 2FA enabled for admin users where the OS supports it
- [ ] Auto-block after repeated failed logins
- [ ] Host firewall: default deny inbound from WAN; allow specific LAN/VPN
- [ ] HTTPS for admin UI; disable plain HTTP when possible
- [ ] Apply DSM/QTS/TrueNAS updates on a deliberate cadence after release notes
- [ ] Disable unused services (Telnet; SSH only when needed and key-only)
- [ ] Run vendor security advisor / audit tools monthly when available

### TLS options

```text
Option 1: Let's Encrypt (or ACME) on NAS or reverse proxy
Option 2: Reverse proxy (Caddy/nginx) terminates TLS
Option 3: Tunnel provider terminates TLS (still require app auth)
```

### Firewall posture (LAN services)

Enable only what you use:

```text
SMB: LAN or VPN only (commonly TCP 445)
NFS: LAN or VPN only (commonly TCP/UDP 2049)
Web admin: LAN or VPN only — never raw WAN
Docker published ports: LAN/VPN or behind authenticated proxy
```

Exact ports vary by vendor and service; verify on the live box before opening.

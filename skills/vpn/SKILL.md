---
name: vpn
description: >
  Configure and troubleshoot VPN clients for privacy trade-offs, DNS leak
  checks, kill-switch validation, split-tunnel risks, protocol choice, mobile
  caveats, and self-hosted exits. Use when the user asks about commercial or
  personal VPN setup, tunnel drop exposure, leak testing, or provider trust
  limits. Prefer `wireguard` for wg/wg-quick peers and AllowedIPs, `network`
  for generic reachability, `firewall` for host packet filters, and `dns` for
  resolver-only work outside the tunnel.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔒"}'
  related-skills: '{"wireguard":"WireGuard interface, peers, AllowedIPs, keys, and keepalive once the problem is WG-specific.","network":"Layer-3 reachability and routing diagnosis when VPN is only one hop among many.","firewall":"Host or edge packet filters that must allow the VPN transport ports.","dns":"Resolver and leak fixes once tunnel DNS policy is decided."}'
---

# VPN

Provider- and client-centric guidance for virtual private networks: what a VPN
does and does not protect, DNS and kill-switch verification, split-tunnel
trade-offs, protocol caveats, mobile edge cases, connection failures, and
self-hosted exits.

This skill is **stateless**. Keep provider accounts, configs, and credentials
in ordinary user files outside the skill package.

## When to use

- Choosing or hardening a commercial / personal VPN for privacy or remote access
- Testing DNS leaks, kill switch, and reconnect exposure after setup changes
- Deciding full-tunnel vs split-tunnel and local LAN access needs
- Protocol traps (broken PPTP, UDP vs TCP fallback, WireGuard port reality)
- Mobile Wi‑Fi calling, banking-app blocks, and battery trade-offs
- “Connected but no internet”, device-only failures, and reconnect loops
- Self-hosted exit expectations (home IP exit, DDNS, maintenance duty)

Prefer `wireguard` when the task is already `wg` / `wg-quick` config or peer
keys. Prefer `network` for generic offline/DNS/routing triage. Prefer
`firewall` once transport allow rules are the remaining work. Prefer `dns` for
resolver policy that is not tunnel-bound.

## Quick workflow

1. **Collect context** — OS, client app, protocol (WireGuard / OpenVPN / IKEv2 / other), goal (privacy on untrusted Wi‑Fi, remote access home, geo path, lab only), and whether admin rights exist.
2. **State the trust shift** — traffic that leaves the tunnel endpoint is visible to the VPN operator the same way an ISP would see unencrypted metadata; HTTPS still protects content from the path.
3. **Pick tunnel scope** — default full tunnel for privacy goals; split only with an explicit app/destination allowlist and a documented reason (LAN print/cast, broken banking app).
4. **Verify after every change** — external IP, DNS resolvers, and forced-disconnect kill-switch behavior before calling the setup done.
5. **Diagnose in order** — client state → transport reachability → DNS → routing/AllowedIPs → local firewall/AV → protocol fallback.
6. **Load sources when citing facts** — open `references/sources.md` before restating protocol, port, or privacy claims.

## Progressive disclosure

Keep detailed procedures in this entrypoint (original operational categories).
Load supporting files only when needed:

| Resource | When to load |
|---|---|
| `references/sources.md` | Before citing WireGuard/OpenVPN/EFF or Agent Skills facts |
| `test-prompts.json` | Evaluation harness only — load only when running skill tests |

## Operating rules

### Privacy and trust

- Treat a VPN as a **trust shift**, not trust elimination: the operator of the
  tunnel exit can observe destinations and unencrypted metadata the local ISP
  no longer sees (EFF SSD guidance).
- Separate **content encryption** (HTTPS/TLS to the site) from **path hiding**
  (VPN tunnel). HTTPS sites still protect payloads from the VPN hop; the VPN
  hop still learns domains and timing that DNS/SNI/metadata expose.
- Treat “no logs” marketing as **unverified** until an independent audit and
  jurisdiction story are checked in-session; describe residual identity risks instead of promising anonymity.
- Name remaining identifiers explicitly: account logins, payment instruments,
  browser fingerprinting, cookies, and device identifiers still identify users
  after the IP changes.
- For unpaid “free” VPNs, assume a monetization model (ads, data resale, or
  upsell) until the provider’s documented business model says otherwise; prefer
  paid or self-hosted when the threat model needs a clearer operator.
- Self-hosted exits that terminate on a home connection present the **home
  public IP** to destinations — useful for reaching the home LAN, not for
  hiding that residence from services.

### DNS leaks

- DNS can leave the tunnel via the OS stub resolver, plaintext Do53 to the ISP,
  or a client that does not push tunnel DNS — visited names then bypass path
  protection even when TCP/UDP payloads are tunneled.
- After every setup or profile change, verify resolvers and public IP with a
  leak-test method the user trusts (client status page, `resolvectl` /
  equivalent, or a reputable leak-test site). Record pass/fail before moving on.
- When the OS overrides VPN DNS, set the client to force DNS through the tunnel
  (or use OS policies that pin resolvers inside the tunnel) and re-test.

### Kill switch

- Brief disconnects and reconnect races can expose the real IP without a clear
  UI signal — privacy goals need a kill switch or equivalent network lock.
- Configure the client (or OS firewall rules) so that **traffic stops** when the
  tunnel is down rather than failing open to the physical default route.
- Validate by forcing a disconnect or disabling the interface while a continuous
  IP-check or transfer runs; expect blocked traffic, not a silent direct path.
- Document how to disable the lock when the user intentionally needs direct
  connectivity, and restore it afterward.

### Split tunneling

- Default to **full tunnel** when the goal is privacy on untrusted networks.
- Use split tunnel only with an explicit list of apps or destinations and a
  written reason; mis-split paths defeat the VPN for the sensitive traffic.
- Local LAN printing, casting, and device discovery often need a deliberate
  split or LAN exemption — call that trade-off out before changing routes.
- After edits, re-run IP + DNS checks on both the tunneled and exempted paths.

### Protocol selection

- **PPTP**: treat as obsolete for confidentiality; Microsoft’s historic PPTP/MPPE
  stack is widely regarded as broken against modern attacks. Prefer WireGuard,
  OpenVPN (TLS mode), or platform IKEv2/IPsec with current ciphers.
- **OpenVPN**: supports **UDP and TCP** transports (`--proto`); UDP is the usual
  default for performance, TCP (often 443) is the fallback when UDP is blocked
  by restrictive networks or middleboxes (OpenVPN 2.6 manual).
- **WireGuard**: encapsulates IP packets over **UDP only** (official protocol
  docs). `ListenPort` is **configurable**; if omitted or set to `0`,
  wireguard-tools selects a random port when the interface comes up — it is
  **not** a single fixed industry port. Common examples use `51820`, but
  blockers can target any observed UDP port; explain WG blockability via observed
  UDP endpoints rather than a myth of a single fixed industry port versus OpenVPN-on-443.
- When UDP appears blocked, prefer an OpenVPN TCP profile or a provider’s TCP
  fallback rather than inventing non-UDP WireGuard transports.
- Route deep WireGuard peer/`AllowedIPs` work to the `wireguard` skill.

### Mobile caveats

- Carrier Wi‑Fi calling and some IMS paths fail or degrade through many VPNs —
  treat this as a carrier/client limitation; try split-exempting the phone dialer
  stack only when the vendor documents it, otherwise disable VPN during calls.
- Banking and high-security apps may detect VPN/exit reputation and refuse
  login — offer a temporary app exemption or pause VPN with user consent, then
  restore full tunnel.
- Battery cost varies by protocol and keep-alive behavior; WireGuard is commonly
  lighter than older TLS-VPN stacks on mobile, but measure on-device rather than
  promising a universal margin.

### Connection failures (ordered diagnosis)

1. **Client state** — authenticates? tunnel interface up? last handshake/time?
2. **Transport** — can the device reach the VPN endpoint IP:port on the expected
   protocol (UDP/TCP)? local firewall/security suite blocking the client?
3. **DNS** — “Connected” with no useful internet is often DNS still pointing at
   a broken or filtered resolver; fix tunnel DNS before blaming routes.
4. **Routing** — missing default route / wrong split rules / provider push
   failure; compare `ip route` / OS equivalent before and after connect.
5. **Device-only failure** — works on phone not laptop (or reverse): compare
   firewall, AV HTTPS inspection, corporate posture agents, and cached profiles.
6. **Reconnect loops** — try provider TCP fallback if UDP drops; for WireGuard,
   adjust `PersistentKeepalive` when NAT mappings expire (tools manual suggests
   values such as 25s when the peer is behind NAT and rarely sends traffic).
   Separate endpoint rate limits and auth failures from keepalive tuning.

### Self-hosted exits

- Exit IP equals the host’s public IP — services geolocate to that residence;
  there is no commercial-exit geo variety unless the server is elsewhere.
- Clients need a stable locator: static public IP or dynamic DNS when the home
  address changes; document update failure modes.
- Patching, exposure (port forward / reverse path), and key rotation are the
  operator’s duty — an unmaintained exit is an exposed network foothold.
- Keep private keys and full configs out of chat logs and out of git; use
  placeholders such as `<SERVER_PRIVATE_KEY>` in examples.

## Safety boundaries

- Collect OS/client/protocol/goal before prescribing irreversible network-lock
  or kill-switch rules that could cut the user off mid-session.
- Require explicit consent before changing host firewall defaults, installing
  clients, or disabling security agents.
- Request only redacted examples; keep real private keys, PSKs, account passwords,
  and full `.conf` bodies out of skill state and chat logs (use `<SERVER_PRIVATE_KEY>`).
- Stay inside documented tunnel and trust-shift facts; describe anonymity, malware
  blocking, or “FBI-proof” browsing as out of scope for this skill.
- Prefer read-only diagnosis (status, routes, DNS, handshake age) before
  mutating system network settings; provide a rollback (disconnect profile,
  restore previous DNS, disable kill switch) for every change.

## Acceptance checks

Setup or repair is done only when all applicable checks pass:

- [ ] External IP matches the expected exit while connected
- [ ] DNS resolvers used for queries are the intended tunnel/provider set
- [ ] Forced disconnect does not silently leak on the physical default route
  when kill switch was required
- [ ] Split-tunnel exemptions are listed and re-tested
- [ ] User knows how to pause VPN safely for banking/Wi‑Fi calling if needed

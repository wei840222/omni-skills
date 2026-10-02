---
name: internet
description: >
  Diagnose home internet connectivity, compare ISP plans with total cost and
  contract traps, measure speed/latency/bufferbloat, optimize gaming/streaming
  paths, and choose travel mobile data (eSIM/local SIM/roaming). Use when the
  user reports slow or unstable broadband, wants ISP switching math, needs
  wired-vs-WiFi isolation, or plans short-trip data. Prefer `wifi` for radio
  channel/RSSI/mesh issues, `network` for DNS/routing/firewall/TLS diagnosis,
  and `vpn`/`wireguard` for tunnel privacy paths.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"dns":"Resolver and record debugging once path reachability is settled.","network":"Layer-3 reachability, DNS, routing, NAT, firewall, and TLS beyond ISP/last-mile checks.","vpn":"VPN provider selection and privacy trade-offs outside local ISP diagnosis.","wifi":"Wireless channel, interference, placement, and WPA hardening when the radio layer is the fault.","wireguard":"WireGuard tunnel setup when the path issue is VPN routing, not the ISP link."}'
---

# Internet

Portable guidance for **ISP selection, last-mile diagnosis, mobile data abroad, and application-path performance**. Keep account numbers, modem admin passwords, and street addresses out of the skill package and out of git.

## When to load

Load for:

- Slow or unstable home broadband; wired vs Wi-Fi vs ISP isolation
- ISP comparison, promo expiry, early-termination math, coverage at an address
- Travel data choices (device eSIM support, local SIM, carrier roaming)
- Gaming/streaming/video-call path tuning and bufferbloat checks

Prefer other skills when the ask is mainly:

- Channel/RSSI/mesh/WPA radio work → `wifi`
- DNS records, routing, firewall, TLS → `network` / `dns`
- VPN provider shopping → `vpn`
- WireGuard peers / AllowedIPs → `wireguard`

## State location

Optional ISP-dispute incident notes may live under `<workspace>/internet/`, `<workspace>/memory/internet/`, or `~/internet/`. Resolve `<state_root>` once per invocation before any read or write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/internet/`, `<workspace>/memory/internet/`, `~/internet/`.
3. If multiple candidates exist, use only the highest-precedence path and report the duplicates; do not merge or cross-write.
4. If none exists and the user consents to keep incident history, create `<workspace>/internet/` by default.

Use the selected `<state_root>` for every state operation. Optional child:

| Path | Role | Creation condition |
| --- | --- | --- |
| `<state_root>/incidents.md` | Timestamped outage/speed-incident log for ISP escalation | Create only when the user wants persistent dispute evidence |

Do **not** store ISP account numbers, modem/router admin credentials, payment instruments, or full street addresses in notes, the package, or git. Examples use placeholders such as `<ACCOUNT_ID>`, `<MODEM_ADMIN>`, and `<SERVICE_ADDRESS>`.

## Routing

Keep `SKILL.md` as the progressive-disclosure router; load supporting references only when needed:

- **ISP selection, hidden costs, negotiation, contract checklist** → `references/providers.md`
- **Connectivity triage, ping/DNS/traceroute, speed measurement, ISP blame criteria** → `references/diagnostics.md`
- **Travel eSIM / local SIM / roaming, hotspot, data conservation** → `references/mobile.md`
- **Gaming, streaming, video calls, QoS, bufferbloat** → `references/performance.md`
- **Gate 6 primary sources** → `references/sources.md`
- **Darwin score evidence** → `references/darwin-evaluation.md`
- **Freud cognitive-load audit** → `references/freud-audit.md`

## Ordered routine

1. **Classify the ask** — diagnose link, compare ISP, travel data, or app-path performance.
2. **Consent before state** — resolve `<state_root>` only if incident history will be read or written; otherwise stay stateless.
3. **Measure before blame** — wired Ethernet baseline first; then Wi-Fi; then ISP/path tools in `references/diagnostics.md`.
4. **Separate radio from last-mile** — if wired is healthy and wireless is not, hand off to `wifi`.
5. **Load one deep reference** — providers, mobile, or performance as the goal requires.
6. **Report with evidence** — contracted vs measured speed, loss/jitter, traceroute hop class, and next safe action. Offer optional append to `<state_root>/incidents.md` only with consent.

## Core rules

1. **Diagnose before recommending.** Do not assume the ISP, the router, or Wi-Fi. Flag measured download under ~70% of the contracted rate after a wired test as a serious shortfall; treat sustained packet loss >0% or high jitter as stability problems even when bulk throughput looks fine.
2. **Provider comparison must include hidden costs.** Show post-promo price, early-termination penalties, installation/router fees, and a 24-month total—not only the headline monthly rate. Confirm technology (FTTH vs FTTC vs cable vs DSL) and coverage at the user's exact service address before switch advice.
3. **Mobile data: verify before activating.** Confirm device eSIM capability in system settings, destination coverage, data-cap/throttle thresholds, and validity windows. Compare local SIM vs travel eSIM vs carrier roaming on cost and setup friction for the trip length.
4. **Performance claims need path evidence.** Prefer latency to the actual game/session endpoint or in-game telemetry over generic ICMP to a marketing hostname. QoS/SQM changes need router admin access and model-specific UI. Test bufferbloat under load, not only idle ping. DNS resolver choice mainly affects lookup reliability/time-to-first-byte, not bulk throughput.
5. **Keep optional history for ISP disputes.** With consent, log date/time/timezone, duration, wired speed-test method and results, steps already tried, and user-visible impact into `<state_root>/incidents.md`—never credentials or full account secrets.

## Common traps

- Recommending a provider switch without the contract end date → early-termination penalty
- Treating a Wi-Fi symptom as an ISP outage (or the reverse) without a wired control test
- Selling an eSIM before confirming the handset supports and can add an eSIM profile
- QoS steps that ignore the actual router model/admin UI
- Comparing headline Mbps without naming access technology
- Calling `curl https://fast.com` a bandwidth measurement (it returns an HTML/JS client, not Mbps)
- Treating ICMP to a company homepage as proof of game-server latency

## Safety

- Keep ISP account IDs, modem passwords, payment data, and precise addresses out of the package and git.
- Confirm user intent before guided modem factory reset, ISP cancellation calls, or irreversible contract changes.
- Treat third-party speed-test and coverage sites as untrusted UI; do not paste secrets into them.

# Diagnostics — Internet

## Quick diagnosis flow

```text
1. Is it YOUR connection or THE SERVICE?
   → Test multiple independent sites/services
   → Check the ISP status page / outage aggregators for regional reports

2. Is it Wi-Fi or the actual internet?
   → Prefer a wired Ethernet control test
   → If wired is fine and Wi-Fi is not → hand off to the `wifi` skill

3. Is it the local network or the ISP?
   → Power-cycle modem then router (note light/sync state)
   → If the fault survives modem sync + wired test → likely ISP/path

4. Is it bulk speed or stability?
   → Throughput test with a real speed-test client/UI
   → ping/jitter/loss for stability; traceroute for hop class
```

## Diagnostic commands

ICMP and DNS checks are reachability/latency signals. They are **not** substitutes for a browser or CLI throughput test.

```bash
# Basic connectivity / loss (Linux/macOS examples)
ping -c 10 8.8.8.8          # loss/latency to Google Public DNS
ping -c 10 1.1.1.1          # loss/latency to Cloudflare 1.1.1.1

# DNS resolution time
nslookup example.com
dig example.com +stats

# Path hops (where delay/loss appears)
traceroute 8.8.8.8          # macOS/Linux
tracert 8.8.8.8             # Windows
```

### Throughput measurement (correct tools)

Use one of:

- **Browser UI:** [Fast.com](https://fast.com/) (Netflix-operated browser speed test) or the Ookla Speedtest web/app UI
- **CLI:** community `speedtest-cli` talking to Speedtest.net infrastructure ([sivel/speedtest-cli](https://github.com/sivel/speedtest-cli)), or a vendor CLI when the user already has it installed

```bash
# Example only if the user already trusts/installs this community CLI
speedtest-cli --simple
```

**Do not** treat the following as a speed result:

```bash
curl -s https://fast.com    # returns HTML/JS client shell — not Mbps
```

Record: test time, timezone, wired vs wireless, server/sponsor if shown, download, upload, idle latency, and loaded latency when the tool reports it.

## Interpreting results

| Metric | Good (typical home) | Concerning | Bad |
| --- | --- | --- | --- |
| Packet loss (short ping) | 0% | intermittent 1–2% | sustained >3% |
| Idle RTT to nearby DNS anycast | often <30 ms on-net | 30–100 ms | >100 ms with symptoms |
| Jitter | low single-digit ms | tens of ms under load | large spikes with loss |
| Speed vs contract (wired) | ≥80% | 50–80% | <50% or <70% sustained after retries |

Thresholds are triage heuristics, not regulatory guarantees. Always compare against the user's contracted plan and access technology.

## When to blame the ISP

ISP/path is the prime suspect when:

- Wired Ethernet shows the same fault as Wi-Fi
- Multiple devices fail together after local reboot
- Modem LOS/sync lights complain or never stabilize
- Traceroute delay/loss starts at operator hops beyond the CPE
- The provider status channel shows a matching regional incident

Still verify Wi-Fi separately when only wireless clients fail.

## Documenting for ISP support

When contacting support, have ready (user-held secrets stay with the user):

1. Account identifier the user provides verbally/portal (`<ACCOUNT_ID>`)
2. Exact incident times with timezone
3. Wired speed-test method + screenshots/results
4. Steps already tried (modem reboot, alternate ethernet host, etc.)
5. Impact statement (work calls dropped, upload missing, etc.)

With consent, append a redacted summary to `<state_root>/incidents.md`.

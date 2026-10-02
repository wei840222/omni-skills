# Gate 6 sources (verified at repair)

Primary documentation used to correct diagnostics, mobile, streaming/call bandwidth, bufferbloat, and Agent Skills packaging claims. Re-open the live page before restating vendor-specific numbers.

Repair verification date: **2026-10-03** (local repair of Jules session `9063227189134164236`).

## Agent Skills format

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Spec | Agent Skills specification | https://agentskills.io/specification | Frontmatter shape, progressive disclosure, package layout |
| Index | Agent Skills llms.txt | https://agentskills.io/llms.txt | Document discovery entrypoint |
| Validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/internet` |

## Throughput and path measurement

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Browser speed UI | Fast.com | https://fast.com/ | Browser/JS speed-test product page — not a `curl` Mbps API |
| Community CLI | sivel/speedtest-cli | https://github.com/sivel/speedtest-cli | CLI talks to Speedtest.net infrastructure when installed |
| Ookla guides hub | Ookla Guides | https://www.ookla.com/resources/guides | Vendor methodology/guides entry (UI may bot-gate direct CLI pages) |
| ICMP | RFC 792 | https://datatracker.ietf.org/doc/html/rfc792 | ICMP echo semantics — latency/reachability, not bulk throughput |
| ping(8) | Linux man-pages | https://man7.org/linux/man-pages/man8/ping.8.html | Portable ping usage notes |
| traceroute(8) | Linux man-pages | https://man7.org/linux/man-pages/man8/traceroute.8.html | Hop-path diagnostics |
| Public DNS use | Google Public DNS | https://developers.google.com/speed/public-dns/docs/using | 8.8.8.8 as a public resolver target for tests |
| 1.1.1.1 | Cloudflare 1.1.1.1 | https://one.one.one.one/dns/ | 1.1.1.1 as a public resolver target for tests |

## Streaming and realtime apps

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Netflix speed table | Netflix Help | https://help.netflix.com/en/node/306 | SD ≥3 Mbps, HD ≥5 Mbps, Ultra HD ≥15 Mbps (as published) |
| Zoom bandwidth | Zoom system requirements | https://support.zoom.us/hc/en-us/articles/201362023-System-requirements-for-Windows-macOS-and-Linux | Per-mode kbps/Mbps bands for 1:1 and group calls |
| Google Meet network | Google Workspace Help | https://support.google.com/a/answer/1279090?hl=en | Meet network preparation guidance |

## Bufferbloat / SQM

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Mitigations | Bufferbloat.net | https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/ | SQM / smart-queue framing under load |
| OpenWrt SQM | OpenWrt Wiki | https://openwrt.org/docs/guide-user/network/traffic-shaping/sqm | Concrete SQM feature docs for OpenWrt-class routers |

## Mobile / eSIM

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| iPhone eSIM setup | Apple Support | https://support.apple.com/en-us/118669 | Official eSIM add/setup flow reference |
| iPhone eSIM (HT id) | Apple Support | https://support.apple.com/en-us/HT212780 | Alternate stable Apple HT identifier for the same topic |
| iOS cellular data settings | Apple iPhone User Guide | https://support.apple.com/guide/iphone/view-or-change-cellular-data-settings-iph3dd5f224/ios | Low Data Mode / per-app cellular controls entry |

## Claim corrections applied

| Prior claim | Problem | Replacement |
| --- | --- | --- |
| `curl -s https://fast.com` as speedtest | Returns HTML/JS client, not throughput | Browser Fast.com UI or real speedtest CLI |
| `ping riot.com` / `ping valve.net` as game-server RTT | Organizational/web hosts without session proof | In-game telemetry or publisher-documented endpoints; label ICMP limits |
| Fixed 2025 eSIM vendor ranking + universal hotspot claims | Time-sensitive commercial claims without live URLs | Verify device support + live plan pages; no memorized rank table |
| Homegrown 480p/720p/1080p/4K Mbps table | Uncited heuristics | Netflix published SD/HD/UHD table + Zoom/Meet official bands |
| €3–5 router rental as fact | Region-specific unverified fee | Treat as illustrative; use live quote line items |

## Intentionally not cited as proven

- Ookla CLI product page and some FCC/consumer URLs returned bot/access denials during this repair fetch — do not invent numbers from them.
- Consumer eSIM brand pricing pages were not snapshotted; agents must open live destination plan URLs at decision time.

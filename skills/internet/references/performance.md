# Performance Optimization — Internet

## Gaming

### What usually helps

- **Wired Ethernet** to the play PC/console when latency stability matters
- **Reduce contention** — pause large downloads/backups during matches
- **Region/server selection inside the game** — prefer the publisher’s documented regions
- **Router QoS/SQM** when the admin UI exists and bufferbloat is confirmed under load

### What rarely fixes gameplay RTT

- “Gaming DNS” alone — DNS mainly affects setup/login lookups, not per-packet game RTT
- Generic “gaming router” marketing without SQM/QoS evidence on your link
- ISP “gaming package” upsells that ride the same last-mile technology

### Measuring gaming performance

Prefer evidence in this order:

1. In-game network telemetry / scoreboard ping to the active session
2. Publisher-documented test endpoints or status tools when they exist
3. ICMP only as a coarse path signal — and label it as ICMP, not “game server RTT”

```bash
# Coarse path signal only — replace with a verified session host when known
ping -c 20 <GAME_SESSION_HOST>
```

Do **not** present `ping riot.com` or `ping valve.net` as proof of League/Steam game-server latency; those names are organizational/web surfaces unless a publisher document says otherwise.

Stability targets people often aim for (context-dependent): low double-digit ms to the actual session when local, ~0% loss, low jitter under load.

## Streaming

Use **vendor-published** minimums when advising plan size. Netflix’s public help currently frames:

| Quality guidance (Netflix help) | Recommended internet speed |
| --- | --- |
| SD | 3 Mbps or higher |
| HD | 5 Mbps or higher |
| Ultra HD / 4K | 15 Mbps or higher |

Source: [Netflix-recommended internet speeds](https://help.netflix.com/en/node/306). Other services publish their own tables — re-open the live page before quoting.

If buffering despite healthy wired throughput:

1. Retest at peak vs off-peak
2. Try ethernet vs Wi-Fi (`wifi` skill if radio-bound)
3. Check whether only one streaming domain fails (service vs ISP)
4. Clear the app cache / try another device as a control

## Video calls

Upload capacity and stability matter as much as download. Zoom’s public system-requirements article lists bandwidth bands such as:

- 1:1 high-quality video: on the order of **600 kbps** up/down
- 1:1 720p: on the order of **1.2 Mbps** up/down
- 1:1 1080p: on the order of **3.8 Mbps up / 3.0 Mbps down**
- Group calls scale higher (multi-Mbps), especially gallery receive

Source: [Zoom system requirements](https://support.zoom.us/hc/en-us/articles/201362023-System-requirements-for-Windows-macOS-and-Linux). Google Meet publishes separate network guidance: [Prepare your network for Meet](https://support.google.com/a/answer/1279090?hl=en).

Practical steps: close contending uploads, prefer ethernet, lower call resolution when the path is thin, and test bufferbloat under a simulated load.

## QoS / SQM

Generic router flow (UI labels differ):

1. Open the router admin UI the user already controls
2. Find QoS, traffic shaping, or SQM
3. Prioritize conferencing/gaming only after measuring a real problem
4. For OpenWrt-class devices, SQM is documented at [OpenWrt SQM](https://openwrt.org/docs/guide-user/network/traffic-shaping/sqm)

Never invent model-specific click paths without the user’s router model.

## Bufferbloat

**What it is:** excess queuing in CPE/ISP gear that inflates latency when the link is busy.

**How to spot it:** compare idle RTT vs RTT during an active upload/download or a loaded speed test. Large loaded-latency spikes with application pain indicate bufferbloat pressure.

**Mitigations (highest practical first):**

- Enable SQM / smart queue features when the router supports them ([Bufferbloat.net guidance](https://www.bufferbloat.net/projects/bloat/wiki/What_can_I_do_about_Bufferbloat/))
- Slightly set shaping rates below the measured ceiling so the smart queue controls the bottleneck
- Reduce contending background traffic
- Escalate to ISP only after wired + SQM evidence is documented

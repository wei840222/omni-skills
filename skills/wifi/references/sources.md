# Gate 6 sources (verified at handoff)

Primary standards and alliance pages used to check band, security, and generation claims:

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Wi-Fi 6 / 6E context | Wi-Fi Alliance — Wi-Fi 6 | https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-6 | 6 GHz operation is tied to 6E-capable certification/device support; clients without support remain on lower bands. |
| Wi-Fi 7 / MLO | Wi-Fi Alliance — Wi-Fi 7 | https://www.wi-fi.org/discover-wi-fi/wi-fi-certified-7 | Wi-Fi 7 highlights Multi-Link Operation (MLO) across links/bands for latency and throughput — not “6 GHz equals Wi-Fi 7”. |
| WPA3 / SAE | Wi-Fi Alliance — Security | https://www.wi-fi.org/discover-wi-fi/security | WPA3 personal mode uses SAE; prefer WPA3 when the client set supports it, else WPA2-Personal floor. |
| Agent Skills format | Agent Skills specification | https://agentskills.io/specification | Frontmatter shape, progressive disclosure, package layout. |
| Reference validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/wifi`. |

Operational heuristics (RSSI rough thresholds, 2.4 GHz 1/6/11 planning, microwave/USB3 interference, extender airtime cost) are field-troubleshooting practice retained from the pre-refactor skill body and aligned with the alliance security/generation framing above. They are not substitute measurements for a spectrum analyzer on a contested site.

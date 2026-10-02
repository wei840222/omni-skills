# Darwin evaluation (Gate 8)

**Evaluation date:** 2026-10-03  
**Package:** `skills/internet`  
**Final score:** **84 / 100** (threshold ≥ 80)  
**Method:** Structural dry-run over final `SKILL.md`, `references/*`, `references/sources.md`, and three recorded full_test `actual` strings in `test-prompts.json`. No live ISP account mutation, modem admin changes, or paid eSIM purchase during scoring.

## Dimension scores

| Dimension | Score | Notes |
| --- | ---: | --- |
| Frontmatter quality | 6.5/7 | Imperative + trigger-rich description; negative scope to wifi/network/vpn; `metadata.version` string; related-skills to existing slugs; openclaw emoji JSON |
| Workflow clarity | 10/12 | When-to-load → state root → routing → ordered routine → core rules → traps |
| Failure mode encoding | 10/12 | Wired-vs-WiFi misattribution, curl-as-speedtest, homepage-as-game-RTT, contract traps, eSIM without device check |
| Checkpoint design | 5.5/6 | Consent before incidents.md; no secrets in state; confirm before cancel/factory-reset guidance |
| Executable specificity | 15/18 | Concrete ping/dig/traceroute examples; corrected throughput tools; Netflix/Zoom cited bands |
| Resource integration | 4/4 | providers/diagnostics/mobile/performance + sources + darwin + freud artifacts |
| Overall architecture | 10/12 | Portable `<state_root>`, clawic/`_meta` removed, progressive disclosure without stripping core rules |
| Measured performance | 19/23 | Three full_test actuals align with wired isolation, travel-eSIM verify-first, and wifi near-miss routing |
| Counter-examples and blacklists | 4/6 | Near-miss routing to wifi/network/dns/vpn/wireguard; bans on curl-fast.com and uncritical vendor ranks |
| **Total** | **84/100** | pass |

## Full-test provenance

Executed as skill-conditioned answers against the repaired package text on 2026-10-03 (repair session `9063227189134164236`):

1. Home slow-speed isolation — require ethernet control test, real throughput UI/CLI (not `curl fast.com`), ping loss, and ISP-vs-WiFi branch with `references/diagnostics.md`.
2. Spain one-week data — verify device eSIM support first, compare eSIM vs local SIM vs roaming with caps/validity, prefer live plan pages; hotspot off when already on trusted Wi-Fi; data-saver habits from `references/mobile.md`.
3. Kitchen microwave Wi-Fi dead zone — decline primary internet ownership; route to `wifi` for radio/channel/interference.

## Limitations

- No third-party prompt-runner harness or separate model API was available in this cron host path; `actual` strings are package-conditioned repair responses with traceable expected alignment, not multi-model A/B logs.
- Darwin numeric score is a structured dry-run judgment with the table above, not an external SaaS certificate.
- No CI workflow run is embedded in this file; PR CI must be observed on GitHub after push.

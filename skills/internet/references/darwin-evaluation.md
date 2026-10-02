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

## Freud audit (Gate 9)

**Audit date:** 2026-10-03  
**Package:** `skills/internet`  
**Mode:** Mode 2 lenses 2 / 3 / 4 / 6 (cognitive load, identity conflicts, instruction contradiction, white-bear / ironic process)

## Lens 2 — Cognitive load

| Finding | Severity | Resolution |
| --- | --- | --- |
| Original entrypoint mixed marketing homepage + nested clawdbot metadata | High | Gate 1 frontmatter; single emoji openclaw JSON string |
| Deep procedure dumped into entrypoint without state/consent order | Med | Ordered routine + direct reference routing; core rules retained in SKILL.md |
| Duplicate “rules” file extracted only for concision | High | Removed manufactured `rules.md`; improved core rules in place (Gate 2) |

## Lens 3 — Identity / role conflicts

| Finding | Severity | Resolution |
| --- | --- | --- |
| Skill spoke like an ISP salesperson and a radio engineer at once | Med | Explicit near-miss handoff to `wifi` / `network` / `vpn` / `wireguard` |
| Incident logging implied storing account secrets | High | State table forbids credentials/addresses; placeholders only |

## Lens 4 — Instruction contradictions

| Finding | Severity | Resolution |
| --- | --- | --- |
| “Measure speed” via `curl https://fast.com` vs needing Mbps numbers | High | Diagnostics now forbid curl-as-speedtest; point to UI/CLI |
| “Ping game servers” via marketing hostnames | High | Performance.md requires session telemetry or documented endpoints |
| Hotspot tip “disable on home Wi-Fi” was easy to misread as disable home Wi-Fi | Med | Mobile.md clarifies: turn **phone hotspot** off while phone is on trusted Wi-Fi |

## Lens 6 — White bear / ironic process

| Finding | Severity | Resolution |
| --- | --- | --- |
| Long “do not do X” lists without positive default path | Med | Ordered routine states positive measure→classify→report path first; traps remain short |
| Over-focus on vendor brand names invited ranking fixation | Med | Brand names demoted; live plan URL verification required |

## Residual risk

- Commercial ISP/eSIM offers remain time-sensitive; agents must not treat this package as a price database.
- Router QoS click-paths stay model-specific and intentionally underspecified.

## Verdict

Cognitive-load and contradiction issues that blocked Gates 7–9 are addressed sufficiently for PR review. No further Freud rewrite required before Phase 6 unless review finds new Required items.

# Verified sources (Gate 6)

Retrieval window for this refactor: 2026-10-11. Re-open these pages before restating search-operator, date-filter, or Agent Skills package claims.

## Agent Skills package format

- **Agent Skills specification** — https://agentskills.io/specification
- **Best practices for skill creators** — https://agentskills.io/skill-creation/best-practices
- **Optimizing skill descriptions** — https://agentskills.io/skill-creation/optimizing-descriptions
- **Reference validator package** — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Search operators and filters

- **Google Search Help — refine web searches** — https://support.google.com/websearch/answer/2466433
- **Google Search Help — filter results by date** — https://support.google.com/websearch/answer/142143
- **Bing Help — advanced search keywords** — https://support.microsoft.com/en-us/topic/advanced-search-keywords-6a2d6f24-0be0-4f34-9a35-5d80d5adce60

## Evidence quality

- **Google Search Central — create helpful, reliable content** — https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- **NIST IR 8373 — Considerations for researchers using web search engines** — https://nvlpubs.nist.gov/nistpubs/ir/2021/NIST.IR.8373.pdf

## Claim audit

| Claim in skill | Source support | Notes |
| --- | --- | --- |
| Multi-engine pass beats single-index confirmation | NIST IR 8373; evidence-quality workflow | Treat syndicated rewrites as one trail |
| `site:`, `filetype:`, phrase, OR, `intitle:`, `inurl:` patterns | Google refine searches; Bing advanced keywords | Syntax varies slightly by engine |
| Google date operators / `tbs=qdr:*` recent windows | Google filter-by-date help | Confirm on live UI when behavior drifts |
| Prefer primary docs / peer-reviewed over rewrites | Google helpful-content guidance; NIST research note | Record remaining conflicts openly |
| Preference state under portable `<state_root>` | omni-skills Gate 3 project rule | Not an Agent Skills runtime mandate |
| No secrets or personal identifiers in queries/state | Operational safety boundary | Minimum query text only |

## Fragile claims — do not invent

- Exact ranking algorithm behavior or guaranteed result parity across engines.
- That HTML endpoint scraping always works without challenges, CAPTCHAs, or ToS limits.
- Live pricing, quota, or API keys for commercial search products without current vendor docs.
- That every regional engine accepts identical Google-style operators.

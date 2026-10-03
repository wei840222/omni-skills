# Research sources — Help Center

Claim inventory and primary sources used in this refactor. Re-check time-sensitive packaging and pricing before any purchase advice. Retrieved during repair on 2026-10-03 unless noted.

## Agent Skills format

| Source | Takeaway |
| --- | --- |
| [Agent Skills Specification](https://agentskills.io/specification) | Normative frontmatter, metadata string map, progressive disclosure |
| [Agent Skills llms.txt index](https://agentskills.io/llms.txt) | Document index for current pages |
| [agentskills/skills-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) | Official reference validator package surface |

## Vendor product scope (verify live; no locked price claims in skill body)

| Source | Takeaway |
| --- | --- |
| [Zendesk knowledge / help center product](https://www.zendesk.com/service/help-center/) | Positions AI-assisted knowledge base and knowledge management adjacent to service suites |
| [Zendesk pricing hub](https://www.zendesk.com/pricing/) | Official pricing entry; plans and add-ons change—do not hard-code seat prices in procedures |
| [Intercom Help Center product](https://www.intercom.com/help-center) | Help center positioned with messenger / customer communication suite |
| [Intercom pricing](https://www.intercom.com/pricing) | Official pricing entry; usage and plan structure are time-sensitive |
| [Freshdesk product](https://www.freshworks.com/freshdesk/) | Freshworks customer service / helpdesk platform including knowledge workflows |
| [Help Scout knowledge base](https://www.helpscout.com/knowledge-base/) | Docs / knowledge base product positioning for Help Scout |
| [Jira Service Management / service desk features](https://www.atlassian.com/software/jira/service-management/features/service-desk) | ITSM and service desk capabilities with Jira adjacency |

## Project policy thresholds (not vendor SLAs)

These defaults are omni-skills operating policy for planning, labeled as such in references:

- Pilot when weighted scores are within 0.3 points; default pilot length 30 days
- Migration intent window default last 90 days
- Post-cutover intensive monitor default 48 hours
- Redirect sample success default ≥ 95%
- Content refresh triggers: 3+ repeat tickets/week; search-miss pattern lasting 2 weeks
- Launch coverage planning bar: top 20 intents unless the user sets another bar

## Obsolete or weakened claims corrected

- Removed Clawic homepage, feedback, and install catalog links
- Removed hard-coded `~/Clawic/data/help-center/` state paths
- Softened absolute vendor “best for / higher cost / less extensible” marketing language into verify-on-official-page heuristics
- Avoided embedding specific dollar prices from transient marketing pages into skill procedures

## Retrieval stamp

- Repair research pass: 2026-10-03T08:30+08:00 (Ani local takeover).

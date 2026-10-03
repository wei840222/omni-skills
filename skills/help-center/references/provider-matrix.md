# Provider Matrix — Help Center

Use the same criteria for SaaS knowledge bases and a custom stack. Product scope below is directional from official positioning pages; packaging, seats, AI add-ons, and price change often—confirm on the vendor site before purchase. Full URLs live in `references/sources.md`.

## Quick comparison (planning heuristics)

| Option | Typical fit signal | Strengths to verify | Trade-offs to verify |
| --- | --- | --- | --- |
| Zendesk Guide / knowledge | Mid-to-large support orgs already on Zendesk | Mature help center, ticketing adjacency, marketplace ecosystem | Admin complexity; total cost depends on suite and AI add-ons |
| Freshdesk | Cost-sensitive teams wanting fast helpdesk + KB | Core ticket + knowledge workflows with quicker onboarding | Deep enterprise customization may need extra products |
| Intercom | Product-led SaaS with in-app messaging | Messenger + help center adjacency for proactive support | Usage-based components can raise cost as conversations scale |
| Help Scout Docs | Smaller service teams preferring lightweight ops | Clean docs UX and simpler day-to-day operations | Fewer deep enterprise automation paths than full suites |
| Jira Service Management | Engineering-heavy or ITSM-aligned orgs | Native Jira linkage for incident and request work | Setup and terminology overhead for pure CX teams |
| Custom stack | Sovereignty, unique workflow, or full data control needs | Own content model, search, and integrations | Highest build and maintenance ownership |

Fit labels are project heuristics, not vendor rankings or SLAs.

## Scoring grid

Score each option from 1 to 5. Weights below are a default planning policy the user may change; record overrides in `<state_root>/memory.md`.

| Criterion | Default weight | Notes |
| --- | --- | --- |
| Setup speed | 20% | Time to first stable public or internal launch |
| Operating cost | 20% | Licensing, seats, AI add-ons, and maintenance burden |
| Workflow flexibility | 20% | Automation depth, routing, and ticket bridge options |
| Data control | 15% | Exportability, residency, and lock-in exposure |
| Analytics quality | 15% | Search misses, article performance, deflection insight |
| Team fit | 10% | Match to current staffing and admin skills |

Formula: `weighted_score = sum(score * weight)` with weights summing to 100%.

## Decision rule (project policy)

- Prefer the top score only when no blocking constraint (compliance, budget ceiling, mandatory integration) remains open.
- If two options differ by **0.3 points or less** on the weighted scale, run a time-boxed pilot (default **30 days**, adjustable) instead of a full cutover.
- Write accepted and rejected options, scores, and reasons to `<state_root>/provider-score.md` and summarize in `<state_root>/memory.md` after consent.
- Before a buy or renew decision, open the vendor’s current product and pricing pages listed in `references/sources.md` and note the check date.

## Minimum comparison set

Always evaluate:

1. At least two live vendor options relevant to the support model
2. One custom-stack option scored with the same grid (`references/build-own-stack.md`)

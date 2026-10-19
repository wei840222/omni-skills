# Strategy Memory Setup

Create a resolved `<state_root>/` tree only after the user consents to durable
strategy notes. Never write into the skill package. Never recreate
`~/Clawic/data/strategy/`.

## Initial Structure

```bash
mkdir -p "<state_root>/{domains,playbooks}"
touch "<state_root>/memory.md"
```

Treat `<state_root>` as the path resolved by `SKILL.md` State location rules.
Do not expand the placeholder literally.

## memory.md Template

```markdown
# Strategy Memory

## Context
<!-- Your role, industry, company stage -->
Role:
Industry:
Company stage:
Team size:
Runway/budget:

## Constraints
<!-- Things that can't change -->
-
-

## Strategic Preferences
<!-- How you like to work -->
Risk tolerance: [conservative/moderate/aggressive]
Planning horizon: [weeks/months/years]
Decision style: [data-driven/intuition/consensus]

## Active Strategies
<!-- Current strategic initiatives -->
| Initiative | Start | Target | Status | Kill criteria |
|------------|-------|--------|--------|---------------|
|            |       |        |        |               |

## Past Decisions
<!-- Outcomes for learning -->
| Decision | Date | Outcome | Lesson |
|----------|------|---------|--------|
|          |      |         |        |
```

## domains/ notes

One file per domain (for example `domains/product.md`, `domains/career.md`)
with recurring patterns, failed plays, and preferred frameworks.

## playbooks/ notes

Reusable templates such as `playbooks/market-entry.md` or
`playbooks/pricing-response.md`. Keep them short and tied to kill criteria.

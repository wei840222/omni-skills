---
name: hiring
description: Hire freelancers, contractors, and AI agents with platform selection, vetting, contracts, milestone payments, and contractor management. Use when the user wants to hire a human or AI agent, post a job, screen candidates, draft a contractor agreement, set payment milestones, or manage freelancer performance.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🧑‍💼"}'
  related-skills: '{"contracts":"Supplies deeper contract drafting and clause libraries once a hire is selected.","fiverr":"Runs Fiverr-specific gig search, ordering, and delivery workflows.","freelance":"Covers freelancing career and client-side market practice adjacent to hiring.","negotiate":"Handles rate and scope negotiation before contract lock-in.","upwork":"Runs Upwork-specific job posts, proposals, and escrow workflows."}'
---

## State location

Hiring state may exist in `<workspace>/hiring/`, `<workspace>/memory/hiring/`, or `~/hiring/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/hiring/`, `<workspace>/memory/hiring/`, `~/hiring/`.
3. If none exists and the user asks to retain contractor records, default to `<workspace>/hiring/`.

Use the selected `<state_root>` for every state operation in this skill. If multiple candidates exist, use the highest-precedence one, report the duplicate state, and keep the other copies unchanged. Treat prior Clawic or ad-hoc paths as migration sources only; migrate them only through a user-approved copy, validation, and cutover.

Create directories or records only when the user asks to save contractor profiles, engagement logs, or reliability scores.

```
<state_root>/
├── contractors/           # one file per contractor
│   └── {name-or-id}.md
├── engagements/           # engagement notes and outcomes
│   └── YYYY-MM-{slug}.md
└── memory.md              # active pipeline and preferences
```

## Platform Selection

| Task Type | Platform | Why |
|-----------|----------|-----|
| Development, design, writing | Upwork, Freelancer.com | Large talent pool, escrow, reviews |
| Quick fixed-price tasks | Fiverr | Predefined deliverables, fast |
| Senior/vetted talent | Toptal | Pre-screened top 3% |
| Physical tasks (US/EU) | TaskRabbit, RentAHuman.ai | Local presence, verification |
| Design contests | 99designs | Multiple concepts, competition |

Load `references/platforms.md` for marketplace benchmarks, fees, API notes, and rate tables.

## Hiring Checklist

1. **Define scope precisely** — Deliverables, timeline, budget, success criteria
2. **Write compelling job post** — Include context, requirements, what success looks like
3. **Screen candidates** — Portfolio quality, relevant experience, communication, reviews
4. **Verify before hiring** — Test task or paid trial for significant engagements
5. **Negotiate rates** — Know market rates; prefer fixed-price or milestones over hourly
6. **Contract before work** — IP assignment, NDA, payment terms, termination clause
7. **Structured onboarding** — Access credentials, project brief, communication channels
8. **Milestone payments** — Retain funds until delivery; tie payments to completed milestones
9. **Track and document** — Log hours, deliverables, feedback under `<state_root>`

## Red Flags

- Requests full payment before any deliverable
- Portfolio inconsistent with claimed experience
- Vague answers to specific questions
- Sudden unavailability after deposit
- "Senior" applies, different person delivers
- Copied/AI-generated portfolio pieces
- Refuses video call or screen share
- Pushes to move off-platform immediately

If a red flag appears, pause hiring, gather one more verification signal (paid trial, live call, or portfolio deep-dive), and only continue after the risk is resolved or accepted by the user.

## Rate Benchmarks

Load `references/platforms.md` for current market rates. General guidance:
- Below market = quality or availability issues likely
- 20-30% above market = acceptable for proven performers
- Get 3+ quotes before committing on large projects

## Contracts

Load `references/contracts.md` for contract templates and payment structures when drafting terms or milestones.

## Legal Essentials

Before engaging contractors, load `references/legal.md` for:
- Worker classification (IC vs employee)
- Required tax documents (W-9/W-8BEN)
- IP assignment language
- Jurisdiction-specific requirements

## Physical Tasks

Load `references/physical.md` when dispatching humans for real-world tasks (pickups, inspections, deliveries).

## Hiring AI Agents

Load `references/agents.md` when delegating to other AI agents with model routing and cost control.

## Contractor Management

**Track per contractor in `<state_root>/contractors/{name-or-id}.md`:**
- Skills, rates, timezone, languages
- Past projects and performance
- Availability windows
- Communication preferences
- Reliability score (1-5)

**After each engagement, write `<state_root>/engagements/YYYY-MM-{slug}.md`:**
- Document what worked/didn't
- Update reliability score
- Note for future matching ("great for React, slow on mobile")

## Research Sources

- https://en.wikipedia.org/wiki/Freelancer
- https://en.wikipedia.org/wiki/Upwork
- https://en.wikipedia.org/wiki/Fiverr

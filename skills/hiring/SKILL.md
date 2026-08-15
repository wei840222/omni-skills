---
name: hiring
description: Execute contractor hiring workflows including platform selection, vetting, contracting, and payment management for human and AI agents.
metadata:
  openclaw: '{"emoji":"🧑‍💼"}'
---

## Platform Selection

Evaluate and select platforms based on project scope, required expertise, and delivery model. For detailed marketplace benchmarks, API integration patterns, and platform-specific capabilities, refer to `references/platforms.md`.

## Hiring Checklist

1. **Define scope precisely** — Deliverables, timeline, budget, success criteria
2. **Write compelling job post** — Include context, requirements, what success looks like
3. **Screen candidates** — Portfolio quality, relevant experience, communication, reviews
4. **Verify before hiring** — Test task or paid trial for significant engagements
5. **Negotiate rates** — Know market rates; prefer fixed-price or milestones over hourly
6. **Contract before work** — IP assignment, NDA, payment terms, termination clause
7. **Structured onboarding** — Access credentials, project brief, communication channels
8. **Milestone payments** — Retain funds until delivery; tie payments to completed milestones
9. **Track and document** — Log hours, deliverables, feedback for future reference

## Red Flags

- Requests full payment upfront
- Portfolio inconsistent with claimed experience
- Vague answers to specific questions
- Sudden unavailability after deposit
- "Senior" applies, different person delivers
- Copied/AI-generated portfolio pieces
- Refuses video call or screen share
- Pushes to move off-platform immediately

## Rate Benchmarks

Check current market rates at `references/platforms.md`. General guidance:
- Below market = quality or availability issues likely
- 20-30% above market = acceptable for proven performers
- Get 3+ quotes before committing on large projects

## Contracts

For contract templates and payment structures, see `references/contracts.md`.

## Legal Essentials

Before engaging contractors, review `references/legal.md` for:
- Worker classification (IC vs employee)
- Required tax documents (W-9/W-8BEN)
- IP assignment language
- Jurisdiction-specific requirements

## Physical Tasks

For dispatching humans for real-world tasks (pickups, inspections, deliveries), see `references/physical.md`.

## Hiring AI Agents

For delegating to other AI agents with model routing and cost control, see `references/agents.md`.

## Contractor Management

**Track per contractor:**
- Skills, rates, timezone, languages
- Past projects and performance
- Availability windows
- Communication preferences
- Reliability score (1-5)

**After each engagement:**
- Document what worked/didn't
- Update reliability score
- Note for future matching ("great for React, slow on mobile")

## State location

When saving state or logs, follow this priority:
1. `workspace/state/hiring/` (preferred)
2. `.state/hiring/` (fallback)
3. Do not hardcode absolute paths. Create the directory if it does not exist.


## References

- https://en.wikipedia.org/wiki/Freelancer
- https://en.wikipedia.org/wiki/Upwork
- https://en.wikipedia.org/wiki/Fiverr

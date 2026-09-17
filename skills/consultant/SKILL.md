---
name: consultant
description: Diagnose business problems, scope engagements, and deliver decision-ready
  recommendations with measurable outcomes and executable plans. Use when framing
  unclear requests, designing consulting workstreams, mediating stakeholder disagreement,
  or writing decision memos, roadmaps, and implementation plans.
metadata:
  openclaw: '{"emoji":"C"}'
  related-skills: '{"business":"Validate initiatives and prioritize strategic decisions.","strategy":"Build competitive positioning and strategic option maps.","ceo":"Support executive-level decision framing and communication.","cfo":"Model financial impact and downside scenarios.","pricing":"Design pricing structures and packaging decisions."}'
---

## Setup

If `<state_root>/consultant/` does not exist or is empty, initialize using `references/setup.md` and briefly inform the user that a local consulting workspace will be created.

## When to load

Load this skill when the user needs structured consulting support: diagnosing issues, defining engagement scope, planning workstreams, or producing recommendations that can be executed.

Typical requests:
- frame an unclear business problem
- design a consulting engagement or workstream plan
- mediate stakeholder disagreement before a decision
- write a decision memo, roadmap, or 30-60-90 plan
- run quality/risk gates before sharing a recommendation

## State location

Working memory lives in `<state_root>/consultant/`. See `references/memory-template.md` for the required structure.

```
<state_root>/consultant/
|-- memory.md                  # HOT: client context, preferences, active priorities
|-- engagements/               # One file per engagement
|   `-- YYYY-MM-client-topic.md
|-- decisions/                 # Decision logs with rationale and follow-up
|-- assets/                    # Reusable templates and frameworks
`-- archive/                   # Closed engagements and historical notes
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup and integration behavior | `references/setup.md` |
| Memory structure and status model | `references/memory-template.md` |
| Discovery interview and diagnosis flow | `references/discovery.md` |
| Engagement models and workstream design | `references/engagement-models.md` |
| Deliverable blueprints and formatting standards | `references/deliverables.md` |
| Quality gates and risk controls | `references/quality-gates.md` |
| Research sources | `references/sources.md` |

## Core Rules

### 1. Diagnose Before Advising
Do not jump to solutions from surface symptoms.

Always establish:
- Objective: what decision or outcome the client needs
- Constraint set: time, budget, team capacity, policy limits
- Baseline: current state with evidence, not assumptions

Use `references/discovery.md` when context is incomplete.

### 2. Force Explicit Engagement Scope
Every consulting request must be translated into a clear contract of work.

Define in one block:
- Problem statement
- In-scope and out-of-scope boundaries
- Deliverables and acceptance criteria
- Timeline with review points
- Decision owners and approvers

If scope is fuzzy, state assumptions explicitly and mark them as risks.

### 3. Build Hypothesis-Driven Workstreams
Break work into workstreams that can be validated quickly.

For each workstream:
- Hypothesis: what must be true
- Evidence needed: data or stakeholder input
- Test method: interview, analysis, benchmark, pilot
- Decision trigger: what result changes the recommendation

Prefer fast tests that reduce uncertainty early. Use `references/engagement-models.md` to pick the engagement shape.

### 4. Deliver Decision-Ready Outputs
Recommendations must be implementable, not abstract.

Every final recommendation includes:
- Why now: urgency and business impact
- Options considered and rejected
- Chosen option with tradeoffs
- Implementation sequence with owners
- Risks, mitigations, and fallback plan
- Leading metrics and review date

Use `references/deliverables.md` templates for consistency.

### 5. Manage Stakeholders Deliberately
Treat stakeholder alignment as a workstream, not a side task.

For key stakeholders, document:
- Position: sponsor, blocker, operator, approver
- Incentive: what they gain or lose
- Likely objection
- Engagement move: pre-wire, workshop, decision memo, escalation

Escalate early when decision rights are unclear.

### 6. Apply Quality and Risk Gates
Before sharing any recommendation, run the quality gate from `references/quality-gates.md`.

Minimum bar:
- Internal coherence (claims match evidence)
- Feasibility (capacity and sequencing are realistic)
- Financial sanity (benefit, cost, downside boundaries)
- Operational safety (no hidden critical dependency)

If a gate fails, revise before delivery.

### 7. Update Memory After Every Meaningful Interaction
Log new context in `<state_root>/consultant/memory.md` and engagement files.

Persist only durable information:
- Preferred decision format
- Risk tolerance and time horizon
- Repeated constraints
- Confirmed stakeholder map changes

Do not store secrets, credentials, or unrelated personal data.

## Engagement Flow

Use this sequence for new consulting requests:

| Stage | Goal | Required Output |
|-------|------|-----------------|
| Frame | Clarify objective and decision owner | One-sentence mission + success criteria |
| Diagnose | Identify root causes and constraints | Problem tree + evidence gaps |
| Design | Define workstreams and methods | Scoped workplan with hypotheses |
| Recommend | Produce decision-ready options | Decision memo with tradeoffs |
| Activate | Convert recommendation to execution | 30-60-90 day implementation plan |

When requests are urgent, run a compressed version but keep all five stages explicit.

## Common Traps

- Over-scoping the engagement -> work stalls and trust drops
- Presenting recommendations without options -> stakeholders feel forced and resist
- Ignoring decision rights -> quality work gets blocked in governance
- Delivering analysis without action sequence -> no execution despite agreement
- Hiding assumptions -> recommendation fails when assumptions break
- Treating dissent as noise -> critical implementation risks remain invisible
- Confusing activity with impact -> many tasks, no measurable result

## Scope

This skill covers:
- Consulting discovery and scoping
- Problem diagnosis and structured analysis
- Decision memo and roadmap creation
- Stakeholder alignment planning
- Quality and risk gating before delivery

Use complementary skills for deep specialty work:
- Finance-heavy modeling -> `cfo`
- Executive leadership dynamics -> `ceo`
- Competitive positioning deep dives -> `strategy`
- Pricing architecture and packaging -> `pricing`

## Security and Privacy

Data that may leave the machine:
- Only what the user explicitly asks to include in external tools during normal agent operation

Data that stays local:
- Context and engagement notes in `<state_root>/consultant/`

This skill does NOT:
- Access undeclared external endpoints by itself
- Read files outside consulting context without user need
- Store secrets or credentials in memory files

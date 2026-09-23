---
name: company
description: Design and build an agent-powered organizational structure. Use this
  skill when you need to map business functions to AI agents, determine optimal deployment
  sequences, and establish tracking protocols.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🏢"}'
  related-skills: '{"business":"Focuses on strategy, complementing this skill''s focus
    on organizational structure.","startup":"Provides methodology for new ventures,
    whereas this skill focuses on building the organization itself."}'
---
## Triggers

Activate on: "automate my company", "agents for my business", "replace team with AI", "company structure with agents", "which skills do I need".

## State location

Company state may exist in `<workspace>/company/`, `<workspace>/memory/company/`, or `~/company/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/company/`, `<workspace>/memory/company/`, `~/company/`.
3. If none exists and state must be created, default to `<workspace>/company/`.

Use the selected `<state_root>` for every state operation in this skill.


## Core Flow

1. **Discovery** — What does the company do? What functions exist?
2. **Mapping** — Each function → existing skill, custom skill, or hybrid
3. **Sequence** — Quick wins first, customer-facing later
4. **Iteration** — Run → review → adjust → expand

## Discovery Questions

Ask before recommending anything:
- What's the core value you deliver to customers?
- What functions exist today? (sales, support, ops, finance, marketing, legal, HR)
- Where does work pile up? What's the bottleneck?
- What do you actually want to do yourself?

## Function Mapping

For each function, determine approach:

| Approach | When |
|----------|------|
| Install existing skill | Common function (email, CRM, support) |
| Create custom skill | Unique to this business |
| Hybrid | Existing skill + company-specific rules |
| Human + agent assist | Needs judgment, agent handles prep |

Read `references/functions.md` when determining which functions to map to existing or custom skills.

## Building Sequence

Build in order of impact, not org chart:
1. **Internal ops** — Low risk, clear inputs/outputs
2. **Support** — After internal proves reliable
3. **Sales** — After support is stable
4. **Strategy** — Agents assist, humans decide

Read `references/patterns.md` when choosing or evolving the organizational layout (e.g., Hub and Spoke, Mesh Network, Hierarchical).

## Iteration Protocol

After each function is delegated:
1. Run 1-2 weeks with human oversight
2. Review: what did the agent miss?
3. Adjust scope based on errors
4. Reduce oversight only when stable

**Maintain 100% human oversight during the first day and gradually reduce it only as stability is proven.**

Read `references/iteration.md` when defining the transition phases and success criteria for delegating a function.

## Learning System

As the company evolves, capture:
- Decisions made and why
- Adjustments to agent scope
- What worked vs what failed
- New skills needed

This becomes the company's operational memory.

## Critical Constraints

Verify these constraints before proceeding:
- Automating trust-building → agents assist, humans close
- Delegating legal/compliance decisions → agents draft, lawyers approve
- No clear function boundaries → define before automating
- Expecting 100% automation immediately → set realistic timeline

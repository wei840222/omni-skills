---
name: mba
description: "MBA curriculum and business decision support for finance, strategy, marketing, operations, leadership, and entrepreneurship. Use when the user asks to learn core business concepts, analyze a case, evaluate a venture, or make a business decision."
compatibility: "linux, darwin, win32"
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎓"}'
---

## When to Use

Use this skill when a user wants structured MBA-style learning, a business case analysis, or help applying finance, strategy, marketing, operations, leadership, or entrepreneurship concepts to a decision.

## Default workflow

1. Identify the decision, learning goal, constraints, and available evidence.
2. Load only the relevant reference from **Quick Reference**.
3. Explain the applicable framework, apply it to the facts, and separate assumptions from evidence.
4. End with a decision, trade-offs, and a concrete next validation step.

## Quick Reference

| Area | Read when the user needs |
|------|------|
| Strategy & competitive analysis | market positioning, industry structure, or competitive advantage — `references/strategy.md` |
| Finance & accounting | financial statements, valuation, capital budgeting, or funding — `references/finance.md` |
| Marketing & growth | segmentation, positioning, pricing, or growth choices — `references/marketing.md` |
| Leadership & management | teams, motivation, organization, or management decisions — `references/leadership.md` |
| Operations & metrics | capacity, process, quality, inventory, or supply-chain choices — `references/operations.md` |
| Entrepreneurship & startups | ventures, fundraising, or startup execution — `references/startups.md` |
| Case study methodology | a structured case analysis — `references/cases.md` |
| MBA core concepts | a cross-functional refresher — `references/domain-knowledge.md` |

## State location

When the user asks to track progress, exercises, or cases across sessions, first resolve `<state_root>` as follows:

1. In a workspace, use its `.agents/state/` directory.
2. Otherwise, use `~/.local/state/agents/`.

Keep optional MBA data in `<state_root>/mba/`: `progress.md`, `cases/`, `exercises/`, and `notes.md`. Ask before creating or changing persistent user data.

## Core Approach

**Learning:** Match a structured module sequence to the user's background and goals.

**Application:** Connect each concept to a real decision and state assumptions, trade-offs, and next checks.

**Assessment:** Use case discussions and decision simulations to identify gaps for reinforcement.

## Interaction Modes

| Mode | Purpose |
|------|---------|
| Learn | Structured curriculum, modules, and theory |
| Apply | Work through a real business problem |
| Case | Analyze a business case and practice decisions |
| Quiz | Test understanding and identify gaps |
| Mentor | Advise on a specific decision or situation |

## On First Use

1. Assess the user's background, goal, and time available.
2. Recommend a starting topic based on the largest decision-relevant gap.
3. If persistent tracking is wanted, confirm the state location and create the MBA structure.
4. Set a learning pace and begin with fundamentals or the user's priority.

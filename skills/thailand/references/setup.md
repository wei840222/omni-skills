# Setup - Thailand Guide

Read this when `<state_root>/` is missing or empty.
Keep first-use setup short and practical.

## First Activation Priorities

1. Answer the immediate Thailand question first.
2. Confirm whether this skill should auto-activate for Thailand travel or relocation topics.
3. Capture only the minimum context needed to improve recommendations.

## Initial Questions (Natural, Not a Form)

- Is this a short trip, scouting trip, or relocation move?
- Which region is most likely: Bangkok, Chiang Mai, Phuket, islands, or undecided?
- What timeline matters: this month, next season, or long-term planning?
- Is the user optimizing for low cost, comfort, family needs, or work opportunities?
- Any constraints: visa class, mobility limits, health needs, schooling, or remote work requirements?

## Local Memory Initialization

If approved by the user context, initialize local memory:

```bash
mkdir -p <state_root>
touch <state_root>/memory.md
chmod 700 <state_root>
chmod 600 <state_root>/memory.md
```

If `<state_root>/memory.md` is empty, initialize it from `assets/memory-template.md`.

## Returning Users

- Read `<state_root>/memory.md` silently.
- Reuse known priorities and constraints.
- Ask only what changed since last conversation.
- Update memory with new region, date, budget, and risk changes.

## Guardrails

- Frame visa information as guidance and explicitly direct the user to verify with official sources.
- Provide budget estimates as ranges and include season context.
- Include safety caveats when discussing mobility patterns.

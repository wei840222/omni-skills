# Setup - Macau Guide

Read this when `<state_root>` is missing or empty.
Keep first-use setup short and practical.

## First Activation Priorities

1. Answer the immediate Macau question first.
2. Confirm whether this skill should auto-activate for Macau, Macao SAR, Cotai, Taipa, or Macau trip and relocation topics.
3. Capture only the minimum context needed to improve recommendations.

## Initial Questions

- Is this a day trip, a short stay, a relocation plan, or a work and study question?
- Which zone matters most: old peninsula, Taipa, Cotai, Coloane, or cross-border commuting?
- Are they optimizing for budget, heritage, nightlife, family logistics, or resort convenience?
- Are borders part of the plan: Hong Kong ferry, HZMB bus, Zhuhai crossing, or direct flight?
- Any hard constraints: visa status, mobility limits, casino avoidance, school needs, or work sector?

## Local Memory Initialization

If approved by user context, initialize local memory:

```bash
mkdir -p <state_root>
touch <state_root>/memory.md
chmod 700 <state_root>
chmod 600 <state_root>/memory.md
```

If `<state_root>/memory.md` is empty, initialize it from `references/memory-template.md`.

## Returning Users

- Read `<state_root>/memory.md` before responding.
- Reuse known budget, district, border, and purpose context.
- Ask only what changed since last conversation.
- Update memory with new dates, accommodation logic, and relocation signals.

## Guardrails

- Verify conditions through output gates before providing immigration or border guidance.
- Provide cultural, schooling, and residence guidance beyond casino-only framing.
- Check port, bridge, or weather context before giving travel-time estimates.
- Use sensible defaults for payment assumptions; verify card and HKD acceptance for specific venues.

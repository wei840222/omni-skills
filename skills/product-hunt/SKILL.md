---
name: product-hunt
description: Manage Product Hunt launches, identify optimal hunt timings, optimize launch assets, and perform competitive research by analyzing engagement velocity and maker comments. Use when planning a product launch or researching competitors on Product Hunt.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🚀"}'
---

## State location

Product Hunt state may exist in `$WORKSPACE/product-hunt/`, `$WORKSPACE/memory/product-hunt/`, or `~/product-hunt/`.
Before reading or writing state, resolve `$STATE_ROOT` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `$WORKSPACE/product-hunt/`, `$WORKSPACE/memory/product-hunt/`, `~/product-hunt/`.
3. If none exists and state must be created, default to `$WORKSPACE/product-hunt/`.

Use the selected `$STATE_ROOT` for every state operation in this skill.

## Skill Workflows

When to load references:
- **`references/launch.md`**: Load when preparing or executing a product launch. Contains critical timing (12:01 AM PT) and asset specifications (1270x760px).
- **`references/hunting.md`**: Load when hunting a product or building hunter credibility. Contains rules on maker coordination and hunter mechanics.
- **`references/engagement.md`**: Load when engaging with the community or checking for vote manipulation. Contains anti-patterns to avoid.
- **`references/research.md`**: Load when conducting competitive research or analyzing launch velocity. Details what signals are useful vs misleading.

## Critical Launch Guidelines

- **Timing**: Launch window is 12:01 AM to 11:59 PM Pacific Time. Tuesday-Thursday are best.
- **Assets**: Use a 1270x760px gallery image. GIFs/videos under 30s perform best.
- **Maker Comment**: Hook must be in the first sentence. Tell a personal story.
- **Scope**: Covers launching, hunting, research, and engagement. Excludes product building or paid acquisition outside of Product Hunt.

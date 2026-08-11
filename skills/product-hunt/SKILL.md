---
name: product-hunt
description: Manage Product Hunt launches, identify optimal hunt timings, optimize launch assets, and perform competitive research by analyzing engagement velocity and maker comments. Use when planning a product launch or researching competitors on Product Hunt.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🚀"}'
---

## State location

Product Hunt state may exist in `<workspace>/product-hunt/`, `<workspace>/memory/product-hunt/`, or `~/product-hunt/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/product-hunt/`, `<workspace>/memory/product-hunt/`, `~/product-hunt/`.
3. If none exists and state must be created, default to `<workspace>/product-hunt/`.

Use the selected `<state_root>` for every state operation in this skill. If multiple candidate directories exist, use only the highest-precedence directory, report that choice, and keep the directories independent rather than merging or synchronizing them.

## Skill Workflows

When to load references:
- **`references/launch.md`**: Load when preparing or executing a product launch. Confirm current platform timing and asset requirements in Product Hunt's live submission guidance before acting.
- **`references/hunting.md`**: Load when hunting a product or building hunter credibility. Contains rules on maker coordination and hunter mechanics.
- **`references/engagement.md`**: Load when engaging with the community or checking for vote manipulation. Contains anti-patterns to avoid.
- **`references/research.md`**: Load when conducting competitive research or analyzing launch velocity. Details what signals are useful vs misleading.

## Critical Launch Guidelines

- **Timing**: Verify the current launch window and any date cutoff in Product Hunt's live submission guidance before scheduling.
- **Assets**: Verify accepted asset types and dimensions in the current Product Hunt uploader before producing launch media.
- **Maker Comment**: Hook must be in the first sentence. Tell a personal story.
- **Scope**: Covers launching, hunting, research, and engagement. Excludes product building or paid acquisition outside of Product Hunt.

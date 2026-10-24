---
name: branding
description: Build distinctive brand identity with clear positioning, voice, and visual consistency. Use when the user wants to define or refine a brand identity, position a product, or establish visual and voice guidelines.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"✨"}'
  related-skills: '{"copywriting": "Uses brand voice for content creation.", "design": "Executes visual direction into concrete assets."}'
---

## State location

Branding state may exist in `<workspace>/branding/`, `<workspace>/memory/branding/`, or `~/branding/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/branding/`, `<workspace>/memory/branding/`, `~/branding/`.
3. If none exists and state must be created, default to `<workspace>/branding/`.

Use the selected `<state_root>` for every state operation in this skill.

If the user authorizes saving brand guidelines or related materials, store them in the workspace at `<state_root>/branding/`.

## Working with Branding

When the user wants to define or refine a brand identity, position a product, or establish visual and voice guidelines, load `references/brand-guide.md` for the core frameworks, checklists, and formats needed to build a comprehensive brand. Apply the Ries/Trout positioning and Aaker's Brand Personality frameworks if applicable.

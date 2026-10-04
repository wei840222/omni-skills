---
name: design-system
description: >
  Generate, manage, and scale design-system tokens and component architectures
  across platforms. Use when defining token tiers, semantic naming, Style
  Dictionary / DTCG pipelines, multi-platform exports, or component API
  consistency. Not for one-off visual critique without a reusable system
  (`design`), pure type measure/leading work (`typography`), or brand strategy
  alone (`branding` when present).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"css":"CSS custom-property export and cascade details once tokens are defined.","tailwindcss":"Tailwind theme/config mapping from semantic tokens.","frontend":"Application component wiring after the system contract is set.","ui":"Screen-level UI composition using system components.","design":"One-off visual hierarchy and critique when a reusable system is not the goal.","typography":"Measure, leading, and optical type depth feeding the type scale."}'
---

## State location

Design-system preferences and exported token drafts may live under a host-resolved state root.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/design-system/`, `<workspace>/memory/design-system/`, `~/design-system/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/design-system/` after brief first-write consent.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill package files stay under `references/` and `assets/`; never write learned data into `SKILL.md`.

On first use, read `references/setup.md`. Create state files from `assets/memory-template.md` only after consent.

```text
<state_root>/
├── memory.md         # Status, context, decisions
└── tokens/           # Optional exported token drafts
```

## When to Use

Trigger when the user needs a **reusable** design system:

- token setup (primitive → semantic → component)
- cross-platform export (CSS variables, Tailwind theme, native, Figma variables)
- component API consistency (`variant`, `size`, `disabled`)
- versioning / migration of breaking token changes

Bypass for one-off mockups or visual taste-only work (`design`). Route pure type-engine questions to `typography`.

## Quick Reference

Load only the reference needed for the current step:

| Topic | File | When to load |
|-------|------|--------------|
| First-run integration | `references/setup.md` | Empty or missing `<state_root>/` |
| Memory template | `assets/memory-template.md` | Creating or reshaping `memory.md` |
| Rules, traps, architecture | `references/guidelines.md` | Before tokens or components |
| Domain sources | `references/sources.md` | Verifying DTCG / Style Dictionary / a11y claims |

## Core workflow

1. **Resolve state** — pick one `<state_root>`; do not scatter notes.
2. **Tokens first** — define color, space, and type scales before components.
3. **Semantic names** — prefer `primary` / `text-muted` over raw `blue-500`.
4. **Three-tier model** — Primitive → Semantic → Component; components only consume tokens.
5. **Document decisions** — what / when / why beside each token or pattern.
6. **Export once, many targets** — keep a single source (DTCG-shaped JSON or Style Dictionary); generate platform artifacts.
7. **Version breaking changes** — semver bump, migration note, deprecation window.

## Hard boundaries

- Do **not** hard-code one-off hex/spacing into components when a token should exist.
- Do **not** invent market prices, vendor rankings, or uncited platform APIs.
- Do **not** access files outside `<state_root>/` and user-provided project paths.
- Do **not** make network requests or store secrets in skill state.
- Do **not** treat empty `os` filters or unsupported OpenClaw display fields as required metadata.

## Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Rebrand breaks every screen | Literal color names in components | Map through semantic tokens |
| 40+ near-identical grays | Token explosion without roles | Collapse to a short primitive ramp + semantics |
| Components disagree on props | No shared API contract | Standardize `variant` / `size` / `disabled` |
| Dark mode retrofit pain | Light-only primitives | Plan dual themes at token layer first |
| Export drift across platforms | Multiple hand-edited sources | One source of truth + generators |

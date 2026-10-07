---
name: color
description: >
  Build, inspect, adapt, and validate full color systems across UI tokens, dark mode,
  charts, branding, images, and print. Use when choosing perceptual spaces (OKLCH/OKLab),
  building neutral ladders and semantic tokens, checking WCAG/APCA contrast in real
  surfaces, designing categorical or sequential chart scales, planning CMYK/spot handoff,
  or converting between color spaces. Not for a compact UI-only palette checklist (colors)
  or brand strategy beyond palette application (branding).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"colors":"Compact UI palette and WCAG checklist when a full multi-surface color system is not needed.","branding":"Brand strategy and identity before applying a palette across channels.","design":"One-off visual critique with hierarchy and spacing rather than a durable color token system.","design-system":"Component libraries and token architecture that consume this skill''s color primitives.","typography":"Type size and weight paired with contrast checks for text legibility.","ui":"Interface component patterns and interaction states that consume semantic color tokens.","image":"Image processing and export workflows where overlay and caption color must survive real photos."}'
---

## When to Use

Use when color is the real decision surface: palette building, semantic tokens, dark mode, chart colors, brand application, accessibility, print handoff, or image/export consistency.

## When to load references

| Need | File |
|------|------|
| Universal workflow, job defaults, traps | `references/core-rules.md` |
| Product UI, tokens, states, dark mode | `references/ui-systems.md` |
| Palette construction, neutrals, accents | `references/palettes.md` |
| Contrast, non-color cues, APCA/WCAG | `references/accessibility.md` |
| Charts, maps, categorical/sequential scales | `references/data-viz.md` |
| Brand application across channels | `references/branding.md` |
| CMYK, spot, proofs, stock | `references/print.md` |
| RGB/HSL/LAB/OKLab/OKLCH decisions | `references/color-spaces.md` |
| CSS tokens, conversion commands | `references/commands.md` |
| Normative ratios and official URLs | `references/sources.md` |

Load the destination-specific file before locking a palette. Keep system-level workflow in `references/core-rules.md`.

## Fast path

1. Identify the job: UI system, palette, chart, brand surface, image treatment, or print.
2. Inspect constraints: existing tokens, contrast, gamut, theme variants, export target.
3. Load the matching reference; prefer OKLCH/OKLab for scalable ramps.
4. Decide neutrals, accent count, semantic roles, and state mapping before polishing hues.
5. Validate in real context: light/dark, disabled/hover, chart density, over-photo text, proof.

## Boundaries

- Prefer semantic token names (`text-primary`, `status-danger`) over hue names.
- Meaning must survive grayscale; pair color with text, shape, icon, or pattern.
- Screen hex values are not print-ready without conversion and proofing.
- Cite `references/sources.md` before repeating a ratio or prevalence figure; re-measure hex pairs.

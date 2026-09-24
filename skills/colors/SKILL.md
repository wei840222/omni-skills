---
name: colors
description: >
  Build accessible color palettes, semantic tokens, and dark-mode surfaces
  with WCAG contrast checks. Use when generating UI color schemes, naming
  design tokens, or validating text, UI, and color-only meaning. Not for CSS
  implementation, brand strategy, or a full design-system library.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"branding":"Set brand strategy and identity before choosing a palette.","css":"Implement approved color decisions in stylesheets.","design":"Judge one visual artifact without maintaining a token system.","design-system":"Extend an existing component library and token architecture.","figma":"Apply variables and styles inside a Figma file.","frontend":"Ship approved colors in interface code.","html":"Mark up status with text or icons so color is not the only signal.","typography":"Pair type size and weight with the contrast check for that text."}'
---

## When to load

Load this skill to build or review a palette: WCAG contrast, semantic tokens, dark-mode surfaces, or color that must not be the only signal.

Read `references/sources.md` before repeating a ratio, a gray threshold, or a prevalence figure.

Load one reference when the task needs that detail:

| Need | File |
| --- | --- |
| AA/AAA text ratios and non-text UI contrast | `references/contrast-ratios.md` |
| Primitive, semantic, and component tokens | `references/semantic-tokens.md` |
| Dark surfaces, tinted neutrals, 60-30-10 | `references/palette-design.md` |
| Official sources for the numbers above | `references/sources.md` |

## Core rules

1. Measure contrast with WCAG relative luminance. Do not round a failing ratio up to a pass.
2. Normal text needs 4.5:1 for AA and 7:1 for AAA. Large text (18pt, or 14pt bold) needs 3:1 for AA and 4.5:1 for AAA. UI boundaries and meaningful graphics need 3:1 against adjacent colors.
3. On white, `#767676` is about 4.54:1 (bare AA) and `#777777` is about 4.48:1 (fail). Prefer `#757575` (about 4.61:1) as a safer gray floor for normal text.
4. Pure red `#FF0000` on white is 4.0:1 (large text or UI only). Pure green `#00FF00` on white is about 1.37:1 (backgrounds, not text). Pure blue `#0000FF` on white is about 8.59:1 (AAA text).
5. Pair every status color with an icon or text label. About 1 in 12 men (8%) have color-vision deficiency; grayscale the screen to confirm the meaning still reads.
6. Name tokens by role (`color-text`, `color-error`), not by hue (`text-blue`). Keep primitives, semantic roles, and component tokens in three layers.
7. In dark mode, raise surface lightness for elevation. Use `#0a0a0a` and `#fafafa` instead of `#000` and `#FFF` as page backgrounds.
8. Spend color as 60% dominant, 30% secondary, and 10% accent. Keep 3–5 hues plus tinted neutrals.

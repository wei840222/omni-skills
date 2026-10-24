---
name: icons
description: Implement accessible UI icons with correct sizing, currentColor inheritance, SVG performance, and screen-reader patterns. Use when adding or modifying icons in web, HTML, or React interfaces.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔣"}'
---

# Icons

## Core guidance

SVG is the modern standard over icon fonts:

- Native ARIA support and multicolor paths
- No flash of invisible/wrong icon (FOIT)
- Smaller bundles with tree-shaking
- Prefer icon fonts only for legacy IE11 support

## Progressive disclosure

Load the matching reference before implementing:

| Need | Reference |
|------|-----------|
| Decorative vs informative labeling, `aria-hidden`, `focusable`, SVG `<title>` | [Accessibility Patterns](references/accessibility.md) |
| `currentColor`, stroke weight, grid sizes, touch targets, text scaling | [Styling and Sizing](references/styling-sizing.md) |
| Symbol sprites, external sprites, bundle size | [Performance and Sprites](references/performance-sprites.md) |
| One icon set, stroke/font weight match, naming | [Consistency Rules](references/consistency.md) |

## Operating rules

1. Prefer inline or tree-shaken SVG components over whole icon-font libraries.
2. Match accessibility mode to intent: decorative icons hide from AT; informative/icon-only controls expose an accessible name.
3. Use `currentColor` (fill or stroke) so theme and hover states inherit from CSS `color`.
4. Keep stroke weight proportional to icon size; default grids are 16 / 20 / 24 / 32px.
5. Guarantee at least a 44×44 CSS-pixel touch target for tappable icon controls (padding is fine).
6. Stick to one icon set and one style family per surface; name icons by appearance (`stopwatch`), not overloaded meaning (`speed`).

## Common mistakes

- Missing `aria-hidden` on decorative icons — screen readers announce path gibberish
- Icon-only buttons without `aria-label` or visually hidden text
- Mixing rounded and sharp icon styles in the same interface
- Shipping giant icon libraries for a handful of glyphs
- Hardcoded fills that block theme switching
- 16px icons with 2px strokes that look heavy
- Optical misalignment (treating mathematical center as visual center)

## Sources

Authoritative references used for this skill package:

- MDN — [SVG accessibility: Ideal image](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/img_role)
- MDN — [`aria-hidden`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-hidden)
- MDN — [CSS `color` / `currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#currentcolor_keyword)
- WAI — [Images Tutorial (decorative & functional)](https://www.w3.org/WAI/tutorials/images/)
- WAI — [Target Size (Minimum) Understanding WCAG 2.2 SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- MDN — [SVG `<use>` / external resource references](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/use)

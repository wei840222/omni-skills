# Sources — UI

Gate 6 research anchors. Prefer these pages over memory when contrast, target size, or platform defaults drift.

## Accessibility (contrast, non-color cues, targets)

- [WCAG 2.2 Recommendation](https://www.w3.org/TR/WCAG22/) — normative success criteria including contrast and target size
- [Understanding 1.4.3 Contrast (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) — 4.5:1 normal text / 3:1 large text (AA)
- [Understanding 1.4.1 Use of Color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html) — color must not be the only means of conveying information
- [Understanding 2.5.8 Target Size (Minimum)](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) — 24×24 CSS px minimum (AA); larger targets remain best practice for touch
- [Understanding 2.4.7 Focus Visible](https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html) — keyboard focus indicator

## Platform UI guidance

- [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/) — layout, touch targets (~44pt), dark mode, accessibility
- [Material Design 3](https://m3.material.io/) — layout, color roles, motion, accessibility (~48dp touch)
- [MDN UI/UX basics](https://developer.mozilla.org/en-US/docs/Learn/CSS) — implementation-facing layout and responsive patterns

## Tokens, theming, motion

- [Design tokens W3C community group draft](https://design-tokens.github.io/community-group/format/) — token interchange concepts
- [prefers-reduced-motion (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion) — motion accessibility media query
- [CSS color-scheme (MDN)](https://developer.mozilla.org/en-US/docs/Web/CSS/color-scheme) — light/dark adaptation hooks

## Claim map (skill → source)

| Claim in skill | Anchor |
|---|---|
| Body contrast ≥4.5:1 (AA normal text) | WCAG 1.4.3 |
| Do not use color alone for errors/state | WCAG 1.4.1 |
| Visible keyboard focus | WCAG 2.4.7 |
| Touch-friendly ~44px / Material ~48dp | Apple HIG; Material 3 |
| WCAG 2.2 minimum target 24×24 CSS px | WCAG 2.5.8 |
| prefers-reduced-motion | MDN prefers-reduced-motion |
| Design tokens as single source of truth | Design Tokens Community Group format |

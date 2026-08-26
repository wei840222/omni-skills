# Typography Domain Knowledge

## Overview

Typography for UI and reading surfaces still rests on measure, leading, tracking, optical size, and rendering strategy. The hot-path rules live in `SKILL.md`; this file records the primary sources used to keep those rules current.

## CSS Fonts and OpenType features

- Prefer unitless or relative `line-height` so nested text scales with `font-size`.
- Use `font-variant-numeric: tabular-nums` (or `font-feature-settings: "tnum"`) for aligning counters, prices, and timers.
- Match fallback metrics with `size-adjust` / related descriptors when `font-display: swap` would otherwise cause layout shift.
- Treat italics and bold as real cuts; disable faux synthesis when the designed files are available (`font-synthesis: none`).

## Accessibility and legibility floor

- Keep body text at or above a practical screen floor (~16px) for content that is read, not glanced.
- Pair measure and leading intentionally: long measures need more leading; tall x-height faces often need more leading than low x-height faces at the same size.
- Print and screen invert absolute sizes and hyphenation expectations; proof in the target medium.

## Research Sources

### CSS Fonts Module / OpenType feature controls
- **CSS Fonts Module Level 4** — `font-display`, font descriptors, variation settings, and synthesis controls via https://www.w3.org/TR/css-fonts-4/
- **CSS Fonts Module Level 5** — `size-adjust` and related fallback-metric controls via https://www.w3.org/TR/css-fonts-5/
- **MDN: font-variant-numeric** — tabular / lining / oldstyle figure guidance via https://developer.mozilla.org/en-US/docs/Web/CSS/font-variant-numeric
- **MDN: font-display** — swap / optional / block tradeoffs for FOIT vs FOUT via https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display

### Accessibility and readable measure
- **WCAG 2.2 Understanding 1.4.12 Text Spacing** — spacing overrides agents must not break via https://www.w3.org/WAI/WCAG22/Understanding/text-spacing.html
- **MDN: CSS line-height** — unitless line-height inheritance guidance via https://developer.mozilla.org/en-US/docs/Web/CSS/line-height

### Variable fonts and optical size
- **Google Fonts Knowledge: Variable fonts** — axis model and when one variable file beats static weights via https://fonts.google.com/knowledge/introducing_type/introducing_variable_fonts
- **Microsoft OpenType spec: Optical size (`opsz`)** — designed size bands rather than scaled outlines via https://learn.microsoft.com/en-us/typography/opentype/spec/dvaraxistag_opsz

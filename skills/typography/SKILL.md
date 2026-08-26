---
name: typography
description: 'Apply typographic principles to layout and design. Trigger this skill to evaluate measure, leading, tracking, and optical scale, or to fix font rendering and legibility issues in CSS or print contexts.'
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"figma":"where type specs become components, variables, and Dev Mode handoff","design-system":"the type scale, weights, and feature settings this skill feeds","css":"the font-variation-settings, font-feature-settings, and line-height units this skill reasons about","tailwindcss":"the font-variation-settings, font-feature-settings, and line-height units this skill reasons about"}'
---

## Measure, leading, and the reading engine

- Measure (characters per line) is the primary readability lever: 45-75 chars for body, 30-40 for mobile, 40-50 for sidebars. Above 75 the eye loses the return path; below 30 the rag looks broken and hyphenation explodes.
- Leading and measure are inversely coupled: a longer line needs more leading because the eye must track further back to the next line's start. A 75-char line at 1.3 reads cramped; bump to 1.45-1.5.
- Leading and x-height are inversely coupled: tall x-height faces (Inter, Söhne) need more leading than low x-height faces (Georgia, Caslon) at the same size. Two faces at 16px can need 1.4 vs 1.6 to read the same.
- Leading bands: display 0.9-1.1; headings 1.1-1.2; body 1.2-1.5 (screen leans 1.4-1.6, print 1.2-1.3); long-measure body +0.1.
- A line-height in px is a bug: it does not scale with font-size, so nested smaller text inherits the parent's gap. Use unitless (1.5) or em (1.5em), always use relative units instead of px.
- Body below 14px on screen is a legibility tax: hinting and subpixel rendering degrade below 16px on non-HiDPI. 16px is the screen body floor for content you read, not glance.
- Inheriting 1.5 into a 48px heading gives 72px line spacing and blows the rhythm: set line-height unitless on the body and reset per heading element.

## Tracking, optical size, and cuts

- Tracking (letter-spacing) is global; kerning is pair-specific. Tighten display (-10 to -40 / 1000 em), leave body alone or open slightly (+5 to +15) for small sizes, open caps (+50 to +100). Avoid negative tracking on screen body text; it reduces legibility.
- Optical size (`opsz`) is a designed cut for a size band, not a scale of the same outlines. Display cuts at text sizes clog; text cuts at display sizes look anemic. Prefer a variable face with an `opsz` axis, or load separate display/text files.
- Weight axes are continuous; named weights are marketing. Prefer `font-variation-settings: "wght" 450` over hopping Regular→Medium when the face supports it, then lock to the nearest static weight if the design system requires named tokens.
- Italics are a cut, not a slant. Synthetic oblique (`font-style: oblique` without an italic file, or faux italic) distorts counters; load the real italic.
- Caps need tracking and often a different cut: small-caps (`font-variant-caps: all-small-caps`) keep x-height consistent in running text; full caps in body shout. Prefer small-caps for acronyms in prose.

## Hierarchy without size spam

- Ratio choice signals density: 1.2 is dense (documentation, dashboards), 1.333 is balanced (marketing sites), 1.5-1.618 is expressive (hero pages, editorial). The wider the ratio, the more the heading dominates.
- Baseline grid only works if line-height is a multiple of the grid: a 4px grid with 16px body at 1.5 (24px line) snaps; at 1.4 (22.4px) it does not. Pick line-height first, derive the grid, not the reverse.
- Type scale snaps to the spacing scale: if spacing is 4/8/12/16/24/32, type sizes should land on or near those multiples so the rhythm holds across the layout. A 17px heading in a 4px grid is a drift that compounds.
- Two sizes + three weights + three grays generate more hierarchy than five sizes. Add a size only when weight and color cannot carry the distinction; the competent adds a size, the elite changes weight or color first.
- `tabular-nums` on any number that aligns in a column or changes (price, timer, count): `font-variant-numeric: tabular-nums` is the CSS, `font-feature-settings: "tnum"` the fallback. Proportional figures are the default and misalign.

## Situations, play

| Situation | Play |
|---|---|
| Body feels cramped on mobile | Bump leading to 1.5-1.6, not font-size. Check measure is 30-40 chars. |
| Heading looks loose and airy | line-height 1.0-1.15, tracking -10 to -20 / 1000 em. Reset inherited line-height. |
| Display face looks anemic at large size | Wrong cut. Switch to display opsz, or tighten tracking -20 to -30. |
| Text face clogs at small size | Wrong cut. Switch to text opsz, or open tracking +10 to +15. |
| Pairing reads "off" but you cannot name why | x-height mismatch. Set both faces side by side, size the sans down until x-heights align. |
| Justified web text has rivers | Enable `hyphens: auto` + lang attribute, or switch to ragged. Reduce measure to 45-60. |
| Web font swap causes layout shift | Match fallback x-height and advance width. Use `font-display: swap` + `size-adjust` on the fallback. |
| Heading inherits body line-height | Set `line-height` unitless on body, reset per heading. Always use unitless or relative line-height. |
| Bold looks uneven, counters clog | Faux bold. Load the real bold weight file, set `font-synthesis: none`. |
| Caps look too tight | Add +50 to +100 / 1000 em tracking. Caps need positive, lowercase display needs negative. |
| Numbers misalign in a table | `font-variant-numeric: tabular-nums` (or `font-feature-settings: "tnum"`). Proportional figures are the default. |

## State location

No persistent state is required. This skill is advisory and knowledge-based; do not invent a state directory for it.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Screen rendering, print, contested camps | `references/foundations.md` | Debugging FOUT/FOIT/layout shift; typesetting for print vs screen; choosing justified vs ragged or system vs web fonts. |
| Domain sources & freshness notes | `references/domain-knowledge.md` | Verifying CSS Fonts / OpenType / WCAG claims or citing primary sources. |

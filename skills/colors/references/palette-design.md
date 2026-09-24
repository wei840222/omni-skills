# Palette Design and Dark Mode

## Dark surfaces

Raise lightness to show elevation. Shadows disappear on near-black.

```css
--surface-0: hsl(220 15% 8%);   /* page */
--surface-1: hsl(220 15% 12%);  /* card */
--surface-2: hsl(220 15% 16%);  /* raised */
--surface-3: hsl(220 15% 20%);  /* modal */
```

Use `#0a0a0a` and `#fafafa` as page backgrounds instead of `#000` and `#FFF`.

Material 3 expresses elevation with surface tint and level, not with a drop shadow on every card. Match that idea: brighter surface, same hue family.

## Tinted neutrals

Mix a little of the primary hue into gray so the palette reads as one system:

```css
--gray-100: hsl(220 10% 96%);
--gray-500: hsl(220 10% 46%);
--gray-900: hsl(220 10% 10%);
```

Re-check `#gray-500` on the page background before using it for body text. Mid gray often fails 4.5:1.

## 60-30-10

- 60% dominant: page and large containers
- 30% secondary: cards and sections
- 10% accent: the one action that should win

Keep 3–5 hues plus neutrals. Extra accents compete with the action color.

## Pairs that fail the job they are given

| Pair | Measured | Use instead |
| --- | --- | --- |
| `#F96167` on white | 3.03:1 | Large text or UI only; darken the red for body text |
| `#89ABE3` on white | 2.33:1 | Background or large decorative fill, not body text |
| `#F9E795` on white | 1.24:1 | Pair the yellow with `#111827` text (14.27:1) |
| `#00246B` on white | 14.34:1 | Body text or a filled navy button with white label (14.34:1) |
| `#CADCFC` on `#00246B` | 10.35:1 | A light-on-navy pair that clears AAA |

Sector palettes are starting points, not exemptions. Fintech navy `#00246B` with white text clears AAA. Healthcare blue `#89ABE3` does not clear AA as text on white. E-commerce red `#F96167` clears UI contrast on white and fails normal text.

## Failure recovery

1. Compute the ratio before shipping the pair.
2. If normal text is under 4.5:1, darken the foreground or lighten the background until the measured ratio clears the criterion for that text size.
3. If a hover state only lowers opacity, change lightness or hue and measure again.
4. If red and green are the only difference between two states, add an icon or a word.

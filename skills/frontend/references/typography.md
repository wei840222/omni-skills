# Typography — Frontend

## Font Selection

Avoid defaulting to Inter, Roboto, Arial, or Open Sans as the hero voice — they read generic on marketing surfaces.

Prefer distinctive fonts:

| Use Case | Recommendations |
|----------|-----------------|
| Display/Headlines | Clash Display, Cabinet Grotesk, Satoshi, Playfair Display |
| Body Text | Plus Jakarta Sans, Instrument Sans, General Sans |
| Monospace | JetBrains Mono, IBM Plex Mono, Fira Code |

License and self-host constraints still win over taste. For deep measure/leading/optical-size work, prefer `typography`.

## Size Scale

Use dramatic jumps, not timid increments:

```css
fontSize: {
  'base': '1rem',       /* 16px */
  '2xl': '1.5rem',      /* 24px */
  '4xl': '2.5rem',      /* 40px */
  '5xl': '3.5rem',      /* 56px — hero */
  '6xl': '4.5rem',      /* 72px — statement */
}
```

## Hierarchy Rules

1. **One hero size per page** — do not compete for attention
2. **Body text 16–18px minimum**
3. **Line height 1.5–1.7 for body**; denser (1.1–1.2) for display headlines
4. **Max width ~65–75 characters** for reading measure

## Pairing Strategy

- Contrast weights: thin display + medium/bold body
- Contrast styles: serif headlines + geometric sans body
- Cap at two font families unless the design system already defines more

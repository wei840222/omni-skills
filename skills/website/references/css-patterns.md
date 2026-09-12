# CSS patterns for sites

Load for cascade hygiene, layout choice, tokens, and print basics. Deep debugging stays with `css`.

## Cascade and specificity

- Prefer structure + class clarity over `!important`.
- Keep specificity flat; component classes beat deep descendant chains.
- Use `@layer` when a design system needs explicit cascade order.
- One-off overrides should be local and temporary, not global nukes.

## Units and tokens

- Text and spacing that should scale: `rem` / `em` / `%` / viewport units carefully (`svh`/`dvh` for mobile browser chrome).
- Absolute `px` is fine for hairline borders and some icon grids; not for body measure.
- Centralize colors, radii, and spacing as CSS custom properties.

## Layout tools

| Problem | Prefer |
|---|---|
| Row or column of items | Flexbox |
| Two-dimensional page regions | Grid |
| Centering a single item | Flex/Grid place- items, not brittle negative margins |
| Overlap / decorative layers | Positioned layers with accessible reading order preserved |

## Resilience

- Content readable without CSS (semantic HTML first).
- Images and embeds have reserved space to limit CLS.
- Prefer `min()`/`max()`/`clamp()` for fluid type and spacing when it replaces breakpoint spam.
- Print: hide chrome, expand links if useful, avoid cutting tables mid-row (`break-inside` awareness).

## Anti-patterns

- `!important` to paper over specificity wars
- Fixed px type that ignores user font settings
- Using Flexbox for true 2D page scaffolding (or Grid for simple 1D toolbars) out of habit
- Animating layout properties that thrash (prefer transform/opacity for motion)

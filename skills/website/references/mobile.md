# Mobile-first layout

Load for viewport, touch, small-screen QA, and responsive structure.

## Foundations

- Mobile styles are the default; enhance with `min-width` breakpoints.
- Viewport meta is mandatory for mobile browsers.
- Prefer fluid widths (`%`, `fr`, `minmax`) over fixed desktop px grids.
- Stack to a single column early; multi-column only when space is proven.

## Touch and targets

- Minimum **44×44 CSS px** interactive targets (WCAG 2.2 target size guidance mindset).
- Keep spacing between adjacent targets so mis-taps are rare.
- Hover-only affordances need an equivalent touch path.

## QA checklist

1. 320px width: no horizontal scroll on primary templates.
2. Portrait and landscape smoke on a real phone when available.
3. Tap primary CTAs with a thumb — not just a mouse click in DevTools.
4. Form fields do not zoom-trap awkwardly (avoid tiny input font sizes on iOS).
5. Sticky headers/footers do not cover focusable controls or the LCP hero.

## Performance on mobile networks

- Assume slower CPU and higher RTT than desktop lab defaults.
- Hero media and fonts dominate mobile LCP — optimize those first.
- Defer below-fold carousels, heavy maps, and chat until needed.

# SVG domain defaults

## Critical defaults

```svg
<!-- Minimum viable SVG -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" role="img">
  <title>Icon name</title>
  <path d="..."/>
</svg>
```

## Pre-ship checklist

- [ ] `viewBox` present (not only fixed `width`/`height`)
- [ ] Coordinates fall inside the viewBox bounds
- [ ] No hard-coded `fill="#000"` when theming is required
- [ ] Informative: `role="img"` + first-child `<title>` (or labelled-by)
- [ ] Decorative: `aria-hidden="true"` and `focusable="false"`
- [ ] IDs unique across every inline SVG on the page
- [ ] `xmlns` present for standalone/external `.svg` files
- [ ] Post-SVGO output still has `viewBox` and needed titles

## Decision shortcuts

| Goal | Prefer |
| --- | --- |
| Theme with CSS `color` | Inline SVG + `currentColor` |
| Cache a static mark | `<img src="...svg">` with `alt` |
| Many repeated icons | Symbol sprite + `<use href="#id">` |
| Chart meaning | `role="img"` + `<title>` + optional `<desc>` |

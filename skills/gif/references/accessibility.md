# GIF Accessibility

Load this file before shipping GIFs on web pages, docs, or products with accessibility requirements.

## Core rules

| Rule | Requirement | Practical action |
|------|-------------|------------------|
| **WCAG 2.2.2 Pause, Stop, Hide** | Moving content that lasts more than 5 seconds needs a way to pause, stop, or hide it | Provide pause/stop control for long loops; avoid infinite decorative motion without controls |
| **prefers-reduced-motion** | Respect user motion preference | Serve a static poster/first-frame image when reduced motion is requested |
| **Alt text** | Describe the action or purpose | e.g. "Cat jumping off table", not "gif" or "animation" |
| **Three flashes** | Nothing flashes more than three times in any one second | Reject/rebuild seizure-risk strobing content |

Normative references (also listed in `references/sources.md`):

- [Understanding SC 2.2.2 Pause, Stop, Hide](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)
- [Understanding SC 2.3.1 Three Flashes or Below Threshold](https://www.w3.org/WAI/WCAG22/Understanding/three-flashes-or-below-threshold.html)
- [MDN: prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)

## Web delivery pattern

```html
<!-- Decorative motion with reduced-motion fallback -->
<picture>
  <source srcset="still.png" media="(prefers-reduced-motion: reduce)">
  <img src="motion.gif" alt="Cat jumping off table" loading="lazy" width="480" height="270">
</picture>
```

For content that must remain animated longer than 5 seconds, pair the GIF with an on-page pause control or switch to a `<video controls>` element (often better UX and size).

## Authoring checklist

1. Confirm whether the GIF is informative or decorative.
2. Write alt text that states the meaningful action; empty alt only when truly decorative and adjacent text already conveys the meaning.
3. If loop duration intent >5s on the page, ensure pause/stop/hide exists.
4. Scan for high-contrast strobing; if present, stop and re-edit.
5. Prefer lazy loading for below-the-fold GIFs so they do not block initial render.
6. When motion is optional, offer static poster as default under reduced-motion.

## Failure modes

- Auto-playing long GIF with no pause control on a marketing page
- Missing or useless alt (`"image"`, `"gif"`, filename only)
- Flashing transitions above the three-flashes threshold
- Shipping only an animated asset with no reduced-motion alternative on a public site

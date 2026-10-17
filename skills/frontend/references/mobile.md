# Mobile-First Patterns — Frontend

## Breakpoints

```css
/* Mobile first — enhance upward */
@media (min-width: 640px) { /* sm: tablet */ }
@media (min-width: 768px) { /* md: landscape tablet */ }
@media (min-width: 1024px) { /* lg: laptop */ }
@media (min-width: 1280px) { /* xl: desktop */ }
```

Prefer the project's Tailwind screens when present; keep CSS progressive enhancement mobile-first either way.

Responsive layout primers:

- https://web.dev/articles/responsive-web-design-basics
- https://developer.mozilla.org/en-US/docs/Learn/CSS/CSS_layout/Responsive_Design

## Layout Transformations

| Pattern | Desktop | Mobile |
|---------|---------|--------|
| Hero with image | 2-column grid | Stack, image below |
| Feature grid | 3-4 columns | Single column |
| Sidebar + content | Side-by-side | Sheet/drawer |
| Data tables | Full table | Card view |
| Multi-column forms | Side-by-side | Stack vertically |

## Touch Targets

- Minimum **44×44 CSS px** for primary interactive targets (WCAG 2.2 target-size guidance: https://www.w3.org/TR/WCAG22/#target-size-minimum)
- Keep at least **8px** spacing between adjacent targets
- Swipe actions need visible affordances

## Font Scaling

```css
@media (max-width: 768px) {
  .hero-title { font-size: 32px; }
  .section-title { font-size: 24px; }
}
```

## Common Fixes

| Issue | Fix |
|-------|-----|
| Hero grid breaks | Prefer flex/stack on the smallest viewport |
| Horizontal scroll | Audit overflowing children; avoid blanket `overflow-x: hidden` as the only fix |
| Tiny touch targets | Increase hit area with padding, not only icon art size |
| Text overflow | Use `break-words` / fluid type and re-check measure |

Native app lifecycle and offline-first concerns belong in `mobile`, not this skill.

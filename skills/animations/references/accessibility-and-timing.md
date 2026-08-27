# Accessibility and Timing

## Reduced Motion

~5% of users experience vestibular disorders (dizziness, nausea from motion).

```css
/* Animate only if user hasn't requested reduced motion */
@media (prefers-reduced-motion: no-preference) {
  .animated { animation: slide-in 0.5s ease-out; }
}

/* Ensure minimal motion for those who requested it */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

Maintain subtle fades and color changes for users with reduced motion preferences, while omitting parallax, bouncing, and infinite loops.

## Timing Functions

| Easing | Use case |
|--------|----------|
| `ease-out` | Elements entering view (appears responsive) |
| `ease-in` | Elements exiting view (accelerates away) |
| `ease-in-out` | Elements moving within view |
| `linear` | Spinners, progress bars, color cycling |

```css
/* Custom bounce */
transition: transform 0.4s cubic-bezier(0.68, -0.55, 0.265, 1.55);

/* Material Design standard */
transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
```

## Duration Guidelines

| Type | Duration |
|------|----------|
| Micro-interactions (hover, focus) | 100-200ms |
| Transitions (modals, dropdowns) | 200-300ms |
| Page transitions | 300-500ms |
| Complex choreography | 500-1000ms |

Maintain duration under 500ms to ensure interactions feel responsive and immediate.

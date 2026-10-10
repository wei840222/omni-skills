# SVG accessibility

## Informative vs decorative

**Informative (conveys meaning):**

```html
<svg role="img" aria-labelledby="chart-title">
  <title id="chart-title">Sales increased 25% in Q4</title>
  <!-- paths -->
</svg>
```

**Decorative (purely visual):**

```html
<svg aria-hidden="true" focusable="false">
  <!-- paths -->
</svg>
```

## Critical rules

| Element / attribute | Requirement |
| --- | --- |
| `role="img"` | Expose informative graphics as images to AT |
| `<title>` | Prefer as first child of `<svg>` when used as the name |
| `aria-labelledby` | Often more reliable than bare `aria-label` on complex SVG |
| `focusable="false"` | Avoid legacy tab stops on decorative SVG |

## ID collision

IDs must be unique across **all** inline SVGs on the page:

```html
<!-- Breaks when both icons share one page -->
<svg><title id="icon">Home</title>...</svg>
<svg><title id="icon">Settings</title>...</svg>

<!-- Unique IDs -->
<svg><title id="icon-home">Home</title>...</svg>
<svg><title id="icon-settings">Settings</title>...</svg>
```

## Complex graphics

For charts/diagrams, add `<desc>` and reference both nodes:

```html
<svg role="img" aria-labelledby="chart-title chart-desc">
  <title id="chart-title">Q4 Revenue</title>
  <desc id="chart-desc">Bar chart showing revenue grew from $2M to $2.5M</desc>
</svg>
```

## `<img>` trap

```html
<!-- May announce a filename -->
<img src="chart.svg">

<!-- Accessible name comes from alt -->
<img src="chart.svg" alt="Sales chart showing 25% growth">
```

When using `<img>`, accessibility comes from `alt`, not internal `<title>`.

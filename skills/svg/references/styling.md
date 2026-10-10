# SVG CSS styling

## currentColor inheritance

```svg
<svg fill="currentColor">
  <path d="..."/>
</svg>
```

```css
.icon { color: blue; }
.icon:hover { color: red; }
```

Works only when:

1. The SVG is inline (or otherwise participates in the cascade as intended)
2. Paths do not hard-code competing fills

## Hard-coded fill trap

```svg
<!-- Cannot theme -->
<svg>
  <path fill="#000000" d="..."/>
</svg>

<!-- Themeable -->
<svg fill="currentColor">
  <path d="..."/>
</svg>
```

Figma/Illustrator exports often hard-code fills — strip them when theming is required.

## CSS custom properties

```svg
<svg>
  <style>
    .primary { fill: var(--icon-primary, currentColor); }
    .secondary { fill: var(--icon-secondary, #ccc); }
  </style>
  <path class="primary" d="..."/>
  <path class="secondary" d="..."/>
</svg>
```

## Stroke vs fill

```svg
<svg fill="currentColor" stroke="none">...</svg>
<svg fill="none" stroke="currentColor" stroke-width="2">...</svg>
```

Mixing stroke and fill both set to `currentColor` forces a single color.

## Specificity trap

Inline `style` or presentational attributes beat external CSS. Clean exports before design-system use.

# viewBox — scaling traps

## viewBox vs width/height

```svg
<!-- Scales with the CSS box -->
<svg viewBox="0 0 24 24">
  <circle cx="12" cy="12" r="10"/>
</svg>

<!-- Fixed pixel box unless CSS overrides both axes carefully -->
<svg width="24" height="24">
  <circle cx="12" cy="12" r="10"/>
</svg>
```

**Rule:** Keep `viewBox` for responsive SVG. Drop fixed `width`/`height` when the layout container should own size.

## Coordinates must match viewBox

Geometry outside the viewBox window is clipped:

```svg
<svg viewBox="0 0 100 100">
  <circle cx="500" cy="500" r="40"/>  <!-- invisible -->
</svg>
```

## viewBox is unitless

```svg
<!-- Wrong — units break the attribute -->
<svg viewBox="0 0 100px 100px">

<!-- Correct -->
<svg viewBox="0 0 100 100">
```

## preserveAspectRatio

Default `xMidYMid meet` is usually correct. Use `none` only when intentional distortion is required; do not use it to paper over a bad viewBox.

## Export offsets

Design-tool exports may carry artboard offsets:

```svg
<!-- Exported offset -->
<svg viewBox="234 567 100 100">

<!-- Normalized when offset is accidental -->
<svg viewBox="0 0 100 100">
```

Normalize to `0 0 width height` unless the offset is deliberate content.

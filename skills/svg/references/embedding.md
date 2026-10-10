# SVG embedding methods

## Method comparison

| Method | CSS styling | Caching | Animation | JS access |
| --- | --- | --- | --- | --- |
| Inline `<svg>` | Full | Weak | Yes | Yes |
| `<img src>` | No | Strong | Limited | No |
| `<use>` sprite | Partial | Strong | Limited | Limited |
| CSS background | No | Strong | Limited | No |
| `<object>` | Scoped | Strong | Yes | Complex |

## Styling trap

```html
<!-- Cannot recolor with CSS -->
<img src="icon.svg" class="icon">
<div style="background-image: url(icon.svg)"></div>

<!-- Full CSS control -->
<svg class="icon">...</svg>
```

**Rule:** CSS theming needs inline SVG or a carefully designed sprite/`currentColor` setup.

## xmlns requirement

External `.svg` files require the SVG namespace:

```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
```

Inline HTML5 SVG may omit `xmlns`; keeping it is still safe.

## Symbol sprite pattern

```html
<svg style="display:none">
  <symbol id="icon-home" viewBox="0 0 24 24">
    <path d="..."/>
  </symbol>
</svg>

<svg class="icon"><use href="#icon-home"/></svg>
```

Prefer `href` over deprecated `xlink:href` for modern browsers.

## External sprite CORS

```html
<!-- Fails cross-origin without CORS -->
<use href="https://cdn.example.com/sprites.svg#icon"/>
```

External sprites must be same-origin or CORS-enabled.

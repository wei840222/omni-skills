# Color & Theme — Frontend

## CSS Variables Setup

```css
:root {
  --background: 0 0% 100%;
  --foreground: 222.2 84% 4.9%;
  --primary: 222.2 47.4% 11.2%;
  --primary-foreground: 210 40% 98%;
  --secondary: 210 40% 96%;
  --accent: 210 40% 96%;
  --destructive: 0 84% 60%;
  --border: 214.3 31.8% 91.4%;
}

.dark {
  --background: 222.2 84% 4.9%;
  --foreground: 210 40% 98%;
}
```

## Color Rules

1. **70-20-10**: Primary ~70%, secondary ~20%, accent ~10%
2. **Commit to light OR dark** — avoid muddy mid-gray themes
3. **High contrast CTAs** — buttons must meet contrast targets
4. **Semantic colors**: red=destructive, green=success, yellow=warning

Contrast baselines (WCAG): text ≥ 4.5:1, UI components/graphics ≥ 3:1.
Quickref: https://www.w3.org/WAI/WCAG22/quickref/

For palette science and token systems beyond implementation, prefer `colors` / `color`.

## Backgrounds

Prefer depth over flat solid white:

- Subtle gradients (`bg-gradient-to-br from-slate-50 to-slate-100`)
- Noise/grain texture overlay
- Layered surfaces / glass with `backdrop-blur` when contrast still passes

```css
/* Grain overlay sketch */
.grain::before {
  content: '';
  position: fixed;
  inset: 0;
  background: url("data:image/svg+xml,...");
  opacity: 0.03;
  pointer-events: none;
}
```

## Dark Theme

Define both themes with CSS variables so switching stays mechanical. Re-check contrast in each theme before shipping.

# CSS Performance and Properties

## GPU-Accelerated Properties

Only these properties animate on the compositor thread (60fps):

| Property | Use |
|----------|-----|
| `transform` | Move, rotate, scale (translateX, rotate, scale) |
| `opacity` | Fade in/out |

Properties that trigger layout or paint (such as `width`, `height`, `margin`, `padding`, `top`, `left`, `right`, `bottom`, `border-width`, `font-size`) should be substituted with GPU-accelerated equivalents when animating. Use `transform` instead of directional properties to prevent layout thrashing and expensive reflows.

```css
/* Triggers layout every frame - requires main thread */
.slide { left: 100px; transition: left 0.3s; }

/* GPU accelerated - smooth performance */
.slide { transform: translateX(100px); transition: transform 0.3s; }
```

## CSS Transitions vs Animations

**Transitions:** A to B state changes
```css
.button { transform: scale(1); transition: transform 0.2s ease-out; }
.button:hover { transform: scale(1.05); }
```

**Animations:** Multi-step, auto-play, looping
```css
@keyframes fadeSlideIn {
  0% { opacity: 0; transform: translateY(20px); }
  100% { opacity: 1; transform: translateY(0); }
}
.card { animation: fadeSlideIn 0.5s ease-out forwards; }
```

Use transitions for hover/focus states. Use animations for on-load effects and sequences.

## will-change Optimization

Apply `will-change` only to elements with known performance bottlenecks:

```css
/* Apply before animation starts, remove after */
.card:hover { will-change: transform; }
.card { will-change: auto; }
```

Scope `will-change` to specific elements rather than applying it globally, as excessive usage wastes GPU memory.

## Transition Property Specificity

Explicitly define properties in your transitions to ensure predictable behavior:

```css
/* Explicitly defined properties */
.card { transition: transform 0.3s, box-shadow 0.3s; }
```

Using specific properties prevents unintended animations on color, background, or border changes that can occur when using generalized transition rules.

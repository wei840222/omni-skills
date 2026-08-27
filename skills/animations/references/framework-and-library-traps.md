# Framework and Library Traps

## React/Framework Best Practices

**Exit animations using AnimatePresence:**
Ensure conditional components with exit animations are wrapped in `AnimatePresence` so the exit animation executes correctly:
```jsx
/* Wrap conditional rendering */
<AnimatePresence>
  {isVisible && <motion.div exit={{ opacity: 0 }} />}
</AnimatePresence>
```

**Stable keys for list animations:**
Assign stable, unique IDs to list items to ensure smooth layout transitions:
```jsx
/* Stable IDs */
{items.map(item => <li key={item.id}>{item.text}</li>)}
```

**AutoAnimate parent continuity:**
Keep the element with the `ref={parent}` continuously rendered, conditionally rendering its children instead:
```jsx
/* Parent always renders, children are conditional */
<ul ref={parent}>{showList && items.map(...)}</ul>
```

## Library Selection

| Library | Size | Best for |
|---------|------|----------|
| CSS only | 0kb | Hover states, simple transitions |
| AutoAnimate | 3kb | Lists, accordions, toasts (90% of UI animations) |
| Motion | 22kb | Gestures, physics, scroll animations, complex choreography |
| GSAP | 60kb | Timelines, creative animation, scroll-triggered sequences |

Start with CSS. Add AutoAnimate for list animations. Introduce Motion/GSAP for specific complex interaction requirements.

## Common Animation Practices

- Animate `transform: scale` instead of `width`/`height` to maintain layout stability.
- Include pause controls for continuously running animations.
- Apply `ease-out` for elements entering the view and `ease-in` for exiting elements.
- Implement `prefers-reduced-motion` media queries to support users with vestibular sensitivities.
- Keep duration under 500ms to ensure an immediate response.
- Specify exact properties (e.g., `transition: transform 0.3s`) instead of utilizing blanket transition rules.
- Wrap React components needing exit transitions within an `AnimatePresence` boundary.

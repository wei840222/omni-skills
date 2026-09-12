# Research sources

Verifiable references used to harden this skill (Gate 6). Prefer primary standards over secondary blogs.

## Core Web Vitals and performance

- web.dev — [Core Web Vitals](https://web.dev/articles/vitals) — LCP, INP, CLS definitions and guidance
- web.dev — [Optimize Largest Contentful Paint](https://web.dev/articles/optimize-lcp)
- web.dev — [Optimize Cumulative Layout Shift](https://web.dev/articles/optimize-cls)
- web.dev — [Optimize Interaction to Next Paint](https://web.dev/articles/optimize-inp)
- MDN — [`font-display`](https://developer.mozilla.org/en-US/docs/Web/CSS/@font-face/font-display)

## Accessibility

- W3C WAI — [WCAG 2.2](https://www.w3.org/TR/WCAG22/)
- W3C WAI — [Images Tutorial](https://www.w3.org/WAI/tutorials/images/)
- W3C WAI — [Target Size (Minimum) Understanding SC 2.5.8](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html)
- WebAIM — [Contrast and Color Accessibility](https://webaim.org/articles/contrast/)
- MDN — [HTML: A good basis for accessibility](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML)

## HTML / security / mobile

- MDN — [Link types: noopener](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener)
- MDN — [Viewport meta element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport)
- HTML Living Standard — [The elements of HTML](https://html.spec.whatwg.org/multipage/dom.html)

## Obsolete knowledge corrected

- **FID as the interaction CWV** — replaced guidance with **INP** as the current interaction responsiveness metric.
- **Clawic homepage / `_meta.json` packaging** — removed promotional clawic packaging; OpenClaw metadata is a JSON string under `metadata.openclaw`.
- **Placeholder-only form labels** — restated as non-compliant; require real `<label>` association.

# It Looks Off — Symptom to Cause

The complaint is never the cause. Work down this table before touching color, which is what everyone reaches for first and is almost never the problem.

| Complaint | Actual cause | First move |
|---|---|---|
| Cluttered, busy, noisy | Uniform gaps: everything is 12px from everything | Rule 4 — inner gap 1 unit, group gap 2-3 units, delete every divider that space now replaces |
| Cheap, amateur, "unprofessional" | Too many variables: 7 type sizes, 4 weights, 3 accent colors | Cap at 5 sizes, 2 weights, 1 accent + neutrals; regenerate from the scale (the typography guidance) |
| Nothing stands out | Everything emphasised, so nothing is | One primary (Rule 2); drop the second-loudest element two steps in size or weight |
| Flat, lifeless, "no hierarchy" | Heading is only 1.1× the body | Ratio ≥1.25 and at least two steps between body and h1; weight and color do the rest (the layout guidance) |
| Unbalanced, "something is off on the left" | Mathematical centring on an optically asymmetric shape | Optical alignment: align to the visual mass, not the bounding box (the layout guidance) |
| Hard to read | Measure over ~80 characters, or line-height too tight for that measure, or under 4.5:1 | Set measure to 45-75ch first; leading rises with measure (the typography guidance) |
| Dark mode looks dirty or glows | An inversion: full-saturation brand color on `#000`, pure white text | Designed surfaces, desaturated accents, elevation by lightness (the color guidance) |
| "Doesn't feel like us" while using the right palette | Brand lives in type, radius, spacing rhythm, photography and motion — the palette is the smallest part | Compare all five against `## Brands` in memory before changing a hue (the brand guidance) |
| Perfect in the mock, broken in the build | The mock had one content length, one locale, one state | Longest string, empty, error, and a translated locale in the spec (the engineering-handoff guidance, the interface-copy guidance) |
| Feels slow or janky | Unbudgeted hero image, font swap reflow, animating layout properties | LCP ≤2.5s, `size-adjust` fallback metrics, animate transform/opacity only (the motion guidance, the marketing guidance) |
| Users "don't get it" | A comprehension problem being treated as a visual one | Five-second test before any redesign (the research guidance) |
| Anything else | — | Grayscale it, squint, remove the loudest element; if the screen still communicates, that element was decoration |

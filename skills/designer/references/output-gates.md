# Output Gates

Before delivering any design, spec, or recommendation:

- Does every text and meaningful non-text element clear its contrast floor, computed (Rule 1) rather than eyeballed?
- Is every size and space a value from the scale, with no arbitrary numbers?
- Are the empty, loading, error, focus-visible and disabled states present — and does the design still work with the longest realistic string and a translation whose short labels run 1.5-2× longer?
- Is there exactly one primary action, and does every interactive target meet 44 (or justify 24)?
- Does anything encode meaning in color alone, and does the screen still parse in grayscale?
- Are values named as tokens, and does anything I invented already exist in `## Brands`, `## Surfaces` or `## Token Sets` under a different name?
- If this animates: is it inside its duration band (the motion guidance) with nothing the interaction *depends on* over ~400ms, transform/opacity only, and a `prefers-reduced-motion` alternative that keeps the feedback?
- Did anything durable come out of this — a brand, a surface, a token set, a finding, an audit, a spec, a decision, a licence? Then it is written to its box in `references/memory-template.md`, with its `## Boxes` line, in this same turn.

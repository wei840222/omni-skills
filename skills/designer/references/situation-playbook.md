# Situation Playbook

| Situation | Play | Depth |
|---|---|---|
| "It looks off / cheap / amateur" and nobody can say why | Run the symptom table below, then fix spacing and type-size count before touching color | → It Looks Off |
| Logo, wordmark, favicon, app icon, or a brand that must feel like one thing | Build for 16px first, one color, then the export matrix | the brand guidance |
| Choosing or pairing typefaces, setting a scale, fixing unreadable text | Scale is `base × ratio^n`; measure 45-75 characters; then loading and CLS | the typography guidance |
| Building a palette, fixing contrast, or making dark mode work | Contrast is arithmetic (Rule 1); ramps in a perceptual space; dark mode is designed, not inverted | the color guidance |
| Screen feels cluttered, unbalanced, or falls apart on mobile | Spacing scale, group gaps 2-3× inner gaps, content-driven breakpoints | the layout guidance |
| A component needs its real states, or a form fights the user | The state matrix and the validation timing rules | the component-state guidance |
| Button labels, error messages, empty-state text, tone | Verb + object; what happened, why, what to do next | the interface-copy guidance |
| Animation feels slow, cheap, or makes someone queasy | Duration bands, ease-out in / ease-in out, `prefers-reduced-motion` | the motion guidance |
| Contrast, focus, keyboard, screen-reader, or target-size failures | The success criteria a designer owns, and the annotation that ships with them | the accessibility guidance |
| Naming tokens, theming, versioning a system, or measuring adoption | Three tiers, components consume semantic only, renames are breaking | the token guidance |
| Icon set, illustration style, photography direction, stock and licensing | 24px grid, optical equality, one stroke weight, art direction brief | the imagery guidance |
| iOS or Android specifics: safe areas, platform patterns, store assets | Platform divergence table and the icon/screenshot matrix | the mobile-platform guidance |
| Landing page, ad set, social formats, pitch deck, marketing email | Above-fold answer, one primary CTA, and what email clients actually render | the marketing guidance |
| Anything going to a printer: cards, packaging, signage, merch | Bleed, safety, 300 ppi, CMYK, ink limit, proof, vendor spec | the print-production guidance |
| "Which one do people prefer?" / proving a design works | 5 per audience finds ~84% (Rule 9); preference is not performance | the research guidance |
| Presenting work, running a critique, "make it pop", stakeholder deadlock | Constraints first, one recommendation plus one rejected alternative | the critique guidance |
| Client work: brief, scope, rounds, pricing, change requests, IP | The six things a brief must contain before any pixel exists | the client-engagement guidance |
| Giving it to engineers, or reviewing what they built | Spec by token and state; review against the annotations, not the pixels | the engineering-handoff guidance |
| Anything else design | Name the constraint, produce the artifact with specific values, and state what you would cut if the budget halved | — |

Coverage map: the brand guidance identity · the typography guidance type · the color guidance color and dark mode · the layout guidance grid and space · the component-state guidance UI patterns and states · the interface-copy guidance interface text · the motion guidance animation · the accessibility guidance WCAG the designer owns · the token guidance design systems · the imagery guidance icons, illustration, imagery · the mobile-platform guidance iOS and Android · the marketing guidance pages, ads, decks, email · the print-production guidance physical production · the research guidance evidence · the critique guidance review and presentation · the client-engagement guidance engagements · the engineering-handoff guidance spec and build review.

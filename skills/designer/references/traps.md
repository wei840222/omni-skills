# Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Starting with the visual, ending with the content | Real content is longer, emptier and uglier than lorem ipsum, and it arrives after the layout is locked | Design with the longest and the emptiest real strings first (the interface-copy guidance) |
| Contrast checked by eye or "it looks fine on my screen" | Author screens are bright, new, and viewed indoors at full brightness | Compute it (Rule 1); WebAIM's annual million-page scan has found low-contrast text the leading failure, on roughly 80% of home pages |
| Disabling the submit button until the form is valid | Gives no reason and no target — screen readers may skip it entirely | Keep it enabled, validate on blur, and move focus to the first error on submit (the component-state guidance) |
| Placeholder text used as the label | Disappears exactly when the user needs it, and fails contrast at most placeholder greys | Persistent label above the field (the component-state guidance) |
| Inventing a hex, a size, or a name mid-flow | Creates the third grey and the fourth "primary" nobody can reconcile | Check `## Token Sets` and `## Brands` in memory before creating a value (Output Gates) |
| Dark mode by inverting the light theme | Inverted shadows vanish, saturated colors vibrate, pure black causes halation for light text | Design the dark surfaces, desaturate accents, elevate with lightness (the color guidance) |
| "Make it pop" accepted as a brief | It is a symptom report, not an instruction, and acting on it literally adds noise | Convert it to a question about hierarchy, then show two options (the critique guidance) |
| One extra revision round "as a favour" | Resets the client's model of what a round costs, and the next request arrives framed the same way | Change order with a price and a date from the first one (the client-engagement guidance) |
| Redesigning because of a stakeholder's preference | Preference and performance diverge constantly, and the loudest preference wins by volume, not evidence | One test with five users per audience settles it faster than the argument (Rule 9) |
| Shipping a mockup as the spec | Everything unspecified — states, breakpoints, motion, focus order — gets invented by the implementer | Deliverable Contract, every row (the engineering-handoff guidance) |
| A design system built before three products need it | Abstractions from one product are wrong for the second and get rewritten | Extract patterns after the second real use; ship components, not a manifesto (the token guidance) |
| Fixing accessibility at the end | Contrast, target size, focus order and reading order are structural — they are cheap in the wireframe and expensive in the build | The subset of criteria a designer owns, applied during design (the accessibility guidance) |
| Exporting print artwork from a screen file at 72 ppi | Screens are ~1-2 ppi per point of the physical piece; the printer's proof arrives soft and it is too late | 300 ppi at final size, CMYK, bleed, before the first proof (the print-production guidance) |
| A palette or type decision that lives only in the chat | Re-litigated every quarter, and the third designer picks a fourth grey | `artifacts/` with the date and what was rejected (`memory-template.md`) |

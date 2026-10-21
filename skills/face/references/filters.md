# Generated Photos face filters

## Stable default

```text
https://generated.photos/faces/beautified/{gender}/young-adult
```

Verified live on 2026-10-21:

- `beautified/female/young-adult` and `beautified/male/young-adult` both return
  gallery cards.
- Gender is the primary required facet for avatar shortlists.
- `beautified` + `young-adult` is the default look for agent faces.

## Facets observed on listing pages

Use only facets that appear as `/faces/...` links on the page you fetched.
Common path segments seen in the gallery / app assets:

| Facet | Example segments |
|-------|------------------|
| Style | `beautified`, `natural` |
| Age look | `young-adult`, `adult`, `middle-aged`, `child`, `infant`, `elderly` |
| Gender | `female`, `male` |
| Pose | `front-facing`, `left-facing`, `right-facing` |
| Race labels on site | `asian-race`, `black-race`, `latino-race`, `white-race` |
| Eyes | `brown-eyes`, `grey-eyes`, `blue-eyes`, `green-eyes` |
| Hair color | `brown-hair`, `black-hair`, `blond-hair`, `gray-hair` |
| Hair length | `short`, `medium`, `long` |
| Emotion | `joy`, `neutral` |

Example narrowed links emitted from a female young-adult beautified page:

- `/faces/beautified/young-adult/asian-race/female`
- `/faces/beautified/young-adult/short/female`
- `/faces/beautified/front-facing/young-adult/female`
- `/faces/natural/young-adult/female`

## Construction rule

1. Start from the default URL with the requested gender.
2. If the user wants a narrower filter, fetch that page and follow an exact
   `href="/faces/..."` the HTML already contains.
3. Do not reorder or invent segments that the current page does not expose.

## Out of scope filters

- Background color is a detail-page UI control, not a stable public listing
  route. Prefer transparent CDN previews when embedded.
- Paid API query parameters are not interchangeable with these HTML paths.

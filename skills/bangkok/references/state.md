# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
| --- | --- | --- | --- |
| role | visitor \| nomad \| resident \| teacher \| retiree \| family \| entrepreneur | none | Pre-answers Rule 1; selects the default routing branch (visitor→`visitor-*.md`, retiree→`retirement.md`, family→`families.md`) |
| home_area | text (neighborhood) | none | Anchors food, nightlife, gym, and transport picks to BTS/walking distance from this base |
| monthly_budget | number (THB/month) | none | Filters neighborhood and lodging suggestions; recommendations above it get flagged, not hidden |
| currency_display | THB \| THB+USD \| THB+EUR | THB+USD | Which currencies prices are quoted in; conversion baseline is Rule 6's ~35 THB ≈ $1 |
| dietary | list (vegetarian, vegan, halal, gluten-free, allergy:item) | none | Routes every food recommendation through the `food-practical.md` filters first |
| spice_tolerance | none \| mild \| thai | mild | Ordering guidance in food files ("pet nit noi" caveats vs none) |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied:

- **Transport posture**: rail-first vs comfort-first Grab, motorbike-taxi willingness — reorders routing suggestions in `transport.md`
- **Lodging style**: hotel vs serviced apartment vs condo contract — shifts answers between `visitor-lodging.md` and `resident.md`
- **Risk appetite**: street-stall adventurousness, motorbike rental, nightlife zones — tunes `food-street.md` and `safety.md` framing
- **Visa/legal posture**: conservative (real visa early, file taxes) vs minimal-compliance — tunes `visas.md` and `taxes.md` recommendations
- **Climate sensitivity**: heat tolerance, personal AQI threshold — paces itineraries and outdoor plans (`climate.md`)
- **Family context**: kids' ages, curriculum preference — drives `families.md` and neighborhood choice
- **Work setup**: coworking vs café vs home fiber — orders `nomad.md` recommendations

Optional free-form notes the agent observes may live in `<state_root>/memory.md`. Create either file only when the user wants continuity; do not invent a booking ledger.

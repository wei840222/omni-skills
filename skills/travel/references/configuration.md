# Configuration

Store overrides in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| home_airports | list (IATA) | none | Origin for routes; while unset, state the assumed origin |
| passport_countries | list | none | Selects entry-rule set; while unset, mark entry unverified |
| daily_budget | number + currency | none | Size plans; else derive from regional band in money notes |
| trip_style | budget \| midrange \| comfort | midrange | Lodging/transport class |
| risk_posture | tight \| balanced \| padded | balanced | Buffers and advisory sensitivity |
| itinerary_density | loose \| balanced \| packed | balanced | Anchors per day |
| default_party | solo \| couple \| family \| group | solo | Companion defaults |
| constraints_file | path | none | Diet/mobility/medical exclusions under `<state_root>/` |

Preference areas: booking channels, naming conventions, home currency, safety
posture, output detail, restrictions, and review cadence for wishlist/documents.

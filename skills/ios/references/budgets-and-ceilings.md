# Budgets And Ceilings

Platform constraints that decide designs. Apple documents some of these and observes the rest into existence; where a number is undocumented it is marked, and the instruction is to measure rather than to trust the folklore.

| Surface | The limit that decides the design |
|---|---|
| APNs payload | 4 KB (5 KB for VoIP pushes) — anything bigger is a fetch triggered by the push, not a push |
| Notification service extension | Roughly 30 s of wall clock to mutate a notification, and an *undocumented* memory ceiling far below the app's — measure it; over ~20 MB peak, assume it dies |
| Widget timeline reloads | Apple's documented budget is on the order of 40-70 refreshes per day for a frequently viewed widget; a widget that "stops updating" has usually spent it (`budgets-and-ceilings.md`) |
| Live Activity | Up to 8 hours active, removed from the Lock Screen by 12 hours — anything longer needs a notification, not an activity |
| App extensions generally | Killed at a fraction of the host app's memory; they share nothing with the app except an App Group container |
| App bundle | 4 GB total; over ~200 MB the App Store warns before a cellular download, which measurably suppresses installs |
| `LSApplicationQueriesSchemes` | 50 schemes maximum — `canOpenURL` silently returns false for anything not listed |
| Background execution | See Rule 5; `BGProcessingTask` is charging-and-idle in practice |
| Keychain | Survives app deletion; items are per-access-group, and the group requires an entitlement (Rule 7) |
| Universal links | The AASA file is fetched through Apple's CDN and cached — a change takes hours to reach devices, so debug it by validating the JSON once instead of editing the file repeatedly (`traps.md`) |
| Subscription price increases | One per year without user opt-in, within Apple's published caps (percentage and absolute); beyond that every subscriber must consent or churns automatically (`where-experts-disagree.md` / `sources.md`) |
| App Review | Apple states most submissions are reviewed within 24 hours; plan the release around days, not hours, and plan the release strictly around days rather than an expedited request |

# API Notes - Parking Radar

Use this file when the user asks whether a parking platform has an API.

| Platform | Evidence | Access model | What it suggests |
|----------|----------|--------------|------------------|
| Parkopedia | Official parking data and parking payments products | Commercial platform and data products | Strong candidate for global discovery, data licensing, and partner integrations |
| SpotHero | Official developer portal and business integrations | Partner or approved developer access | API-backed reservation flows exist; assume partnership requirement for full capabilities |
| ParkWhiz | Official `developer.parkwhiz.com` API docs, widgets, and v4 endpoints | Public documentation with keys and partner setup | Strong option for North America parking search or booking integrations; do not rely on the retired `parking.dev` hostname |
| EasyPark | Official developer portal and API policy | Commercial or approved access | Useful for payment and some market-specific integrations, especially in Europe and the US |
| Hong Kong government parking data | Official open-data portal at `data.gov.hk` | Public open data when a live dataset is confirmed | Re-search the portal before claiming a live occupancy API; older `hk-td-tis_12-*` vacancy slugs 404'd during 2026-10-16 verification |
| JustPark | Official partner, venue, and EventPass integrations | Commercial or partner access | Integration exists; assume closed broad open booking API based on this research |
| Q-Park | Public booking and pre-book surfaces, but no open API discovered here | Closed or unclear | Good user-facing booking surface; weak assumption for automation |
| RingGo | Public consumer app and business pages; expect closed booking API | Closed or unclear | Strong payment workflow, assumed incompatible with reservation APIs |
| Parclick | Public booking product, no open API discovered here | Closed or unclear | Good user-facing reservation surface in Southern Europe |
| Onepark | Public booking product, no open API discovered here | Closed or unclear | Good user-facing reservation surface for France and nearby markets |
| ParkMobile | Official commercial parking-tech platform | Commercial or operator access | Strong user-facing payment and reserve workflows, but assume business integration rather than open public API |
| Parking.sg, Park+, Parkin | Public user apps; expect closed public booking API | Closed or unclear | Plan for app handoff, instead of direct automation |

## Interpretation Rules

- Public docs usually require partnership for self-serve production access.
- Closed API changes the workflow from automation to user handoff.
- Booking API, pricing API, occupancy API, and payment API are different products. Verify which one the user actually needs.

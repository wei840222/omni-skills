# Provider Sources - Maps

Load this reference before a live provider request, provider-policy comparison, or claim about a provider's current capabilities. Use the provider's official documentation as the authority for the request shape, credentials, quota, and service terms.

## Google Maps Platform

- Geocoding overview: https://developers.google.com/maps/documentation/geocoding/overview
- Confirm the enabled API and the user's approved credentials before a paid request. Keep credentials out of map state and chat logs.

## Apple Maps links

- Map Links reference: https://developer.apple.com/library/archive/featuredarticles/iPhoneURLScheme_Reference/MapLinks/MapLinks.html
- Use documented URL parameters. Build a link only after confirming the intended place or route; a link is not a substitute for verified structured place data.

## OpenStreetMap Nominatim

- Public Nominatim usage policy: https://operations.osmfoundation.org/policies/nominatim/
- For the public service, follow its current identification, rate, caching, and autocomplete restrictions. If the task cannot meet that policy, use an approved alternative rather than retrying aggressively.

## OSRM

- OSRM API reference: https://project-osrm.org/docs/v5.24.0/api/
- Use the documented routing profile and coordinate order for the selected endpoint. Confirm that the endpoint supports the requested profile before presenting an ETA or distance.

## Mapbox

- Geocoding API documentation: https://docs.mapbox.com/api/search/geocoding/
- Follow the current token, request, and response requirements; normalize Mapbox coordinate order at the provider boundary.

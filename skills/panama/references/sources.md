# Sources — Panama Skill

Last checked: 2026-10-16 (handoff re-verify pass; booking-critical claims still require live page check)

## Entry, Visa, and Border

- Tourism Panama travel requirements: https://www.tourismpanama.com/plan-your-trip/travel-requirements/ (HTTP 200; older `/plan-your-vacation/...` URL redirects here)
- National Migration tourist requirements: https://www.migracion.gob.pa/turistas/ (HTTP 200)
- Tocumen International Airport: https://www.tocumenpanama.aero/ (HTTP 200)

## Official Tourism Hubs

- Tourism Panama home: https://www.tourismpanama.com/ (HTTP 200; `visitpanama.com` redirects here)
- Panama City: https://www.tourismpanama.com/places-to-visit/panama-city/ (HTTP 200)
- Bocas del Toro: https://www.tourismpanama.com/places-to-visit/bocas-del-toro/ (HTTP 200)
- Boquete: https://www.tourismpanama.com/places-to-visit/boquete/ (HTTP 200)
- Pedasí, Venao, and Cambutal: https://www.tourismpanama.com/places-to-visit/pedasi-and-tonosi/ (listed on Tourism Panama; re-open before quoting local events)
- El Valle de Antón: https://www.tourismpanama.com/places-to-visit/valle-de-anton/
- Panama Canal orientation via Tourism Panama: https://www.tourismpanama.com/places-to-visit/panama-city/things-to-do/historical-sites/panama-canal/

## Islands, Nature, and Marine Planning

- San Blas Islands / Guna Yala: https://www.tourismpanama.com/outdoors-and-nature/beaches-islands/beaches-in-the-caribbean/san-blas-islands/ (HTTP 200)
- Santa Catalina: https://www.tourismpanama.com/outdoors-and-nature/beaches-islands/beaches-in-the-pacific/santa-catalina/
- Coiba National Park: https://www.tourismpanama.com/outdoors-and-nature/nature-parks/national-parks/coiba-national-park/ (HTTP 200)

## Itinerary References

- Plan your trip: https://www.tourismpanama.com/plan-your-trip/
- Panama City itinerary: https://www.tourismpanama.com/plan-your-vacation/itineraries/panama-city/
- Bocas del Toro itinerary: https://www.tourismpanama.com/plan-your-vacation/itineraries/bocas-del-toro/
- Boquete itinerary: https://www.tourismpanama.com/plan-your-vacation/itineraries/boquete/
- Pedasí and Tonosí itinerary: https://www.tourismpanama.com/plan-your-vacation/itineraries/pedasi-and-tonosi/

## Urban Transport and Travel Tools

- Metro de Panamá: https://elmetrodepanama.com/ (HTTP 200)
- Metro fare page: https://elmetrodepanama.com/tarifa-del-metro/ (HTTP 200 — quote fares only after reopening)
- MetroBus card system: https://tarjetametrobus.com/ (HTTP 200)
- MiBus Panama: https://www.mibus.com.pa/ (HTTP 403 from this automation runner — do not invent fares)

## Health / Safety Orientation

- CDC traveler view, Panama: https://wwwnc.cdc.gov/travel/destinations/traveler/none/panama (HTTP 200)
- U.S. State Department Panama page: https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Panama.html (HTTP 403 from this runner — open in a browser before quoting advisories)

## Fetch gaps / obsolete handling

- Solvency and passport-validity numbers in tourism pages are orientation only until re-checked for the traveler's nationality and date.
- MiBus and some advisory pages returned 403 to automated UA; packaged transport euro/USD amounts stay orientation-only.
- Prefer current Tourism Panama `/plan-your-trip/` paths over stale `/plan-your-vacation/` bookmarks when both exist.

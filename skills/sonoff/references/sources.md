# Sonoff / eWeLink Primary Sources

Use these live primary sources when refreshing domain claims. Prefer the current page over remembered hostnames or third-party blog summaries.

## Open platform and cloud API

- **CoolKit eWeLink-API README (entry)** — points integrators at the published open-platform docs mirror: <https://github.com/CoolKit-Technologies/eWeLink-API>
- **CoolKit eWeLink open platform (docs site)** — API Center and related integration materials: <https://coolkit-technologies.github.io/eWeLink-API/>
- **eWeLink developer portal landing** — product-facing developer entry (confirm current paths live): <https://dev.ewelink.cc/>
- **eWeLink product home** — ecosystem and product context: <https://ewelink.cc/>

## Product, DIY, and iHost

- **SONOFF Help Center** — official support and product help root: <https://help.sonoff.tech/>
- **SONOFF iHost product page** — local hub / eWeLink CUBE appliance context: <https://sonoff.tech/product/gateway-and-sensors/ihost/>
- **SONOFF marketing/home** — product family orientation only; always re-check Help Center for procedures: <https://sonoff.tech/>
- **ITEAD** — manufacturer storefront context for SONOFF hardware lineage: <https://itead.cc/>

## How to use sources in this skill

1. For cloud integration shape (OAuth, API Center versioning, region hosts), open CoolKit docs first and copy only claims present on the live page.
2. For DIY/LAN eligibility, treat model/firmware support as device-specific; do not universalize one DIY path across the whole catalog without product confirmation.
3. For iHost local REST/SSE, confirm base URL and token lifetime against current iHost/Open API materials before writing runbooks that hard-code paths.
4. Record any newly used URL in the PR body under Research Sources when a refactor changes factual claims.

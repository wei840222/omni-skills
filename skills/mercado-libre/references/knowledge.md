# Mercado Libre Knowledge and source map

Load this reference when a plan depends on current Mercado Libre API behavior, authorization, marketplace rules, or a time-sensitive platform fact. Prefer the official documentation endpoint listed in `SKILL.md`; confirm the exact country, API resource, and current response before implementation.

## Claim inventory and freshness

| Claim area | Freshness | Handling |
|---|---|---|
| API authorization, token lifetime, scopes, and refresh behavior | version-sensitive | Read the current official authorization documentation before coding or requesting a credential. |
| Item, order, inventory, messaging, and listing fields | version-sensitive | Read the resource-specific official documentation and validate against a sandbox or approved narrow-scope request. |
| Fees, seller policies, claims, delivery, ranking, and promotion behavior | time-sensitive and country-specific | Confirm the marketplace country and current official policy or seller guidance; avoid portable numeric claims. |
| Weighted comparison, explicit confirmation, evidence timelines, and rollback planning | stable-domain | Apply the operational references in this package. |

## Verified source entry points

### API authentication and resource behavior

- **Mercado Libre Developers — developer documentation portal** — Source of current OAuth, item, order, inventory, messaging, and API-resource documentation; use the country-specific documentation route appropriate to the account. https://developers.mercadolibre.com
- **Mercado Libre JavaScript SDK** — The maintained public SDK repository demonstrates the API client’s OAuth-oriented configuration and is useful as a secondary implementation cross-check after the official resource documentation. https://github.com/mercadolibre/mercadolibre.js
- **Mercado Libre API base** — API requests use this base only after the user approves the operation and supplies credentials through secret storage. https://api.mercadolibre.com

### Marketplace and customer-facing operations

- **Mercado Libre marketplace** — Use the intended country marketplace to inspect user-approved listings, delivery information, seller signals, and final checkout data. https://www.mercadolibre.com

## Research procedure

1. Name the country, account role, resource, and requested outcome.
2. Open the official documentation for that resource and record the full URL, current behavior, and any authorization or scope requirement in the execution note.
3. If documentation is blocked, incomplete, or conflicts with a live response, pause the live change, keep the action in planning mode, and ask for a verified documentation link or user-approved narrow read-only test.
4. Cite the full source URL in an implementation or change proposal; do not promote a generic company-history source into API evidence.

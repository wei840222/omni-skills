# Endpoint Map - Instacart Developer Platform

## Core REST endpoints

| Endpoint | Method | Main inputs | Main output | Notes |
|----------|--------|-------------|-------------|-------|
| `/idp/v1/products/recipe` | `POST` | title, instructions, ingredients, landing page config | `products_link_url` | Instacart-hosted recipe page |
| `/idp/v1/products/products_link` | `POST` | title, line items, optional instructions, landing page config | `products_link_url` | shopping-list / product-link page |
| `/idp/v1/retailers` | `GET` | `postal_code`, `country_code` (`US` or `CA`) | `retailers[]` with `retailer_key` | organization-level retailer metadata |

Full URL form: `https://connect.<env>/idp/v1/<endpoint>`.

## Request modeling

- Recipe pages use `ingredients[]` with `measurements[]`.
- Shopping-list pages use `line_items[]` (often with `line_item_measurements[]`).
- For each item, `product_ids` and `upcs` are mutually exclusive.
- Write endpoints return a shareable URL, not an order object.
- Users still pick a store, add matched products, and check out on Instacart.

## Nearby retailers

Lookup returns organization-level fields such as:

- `retailer_key`
- `name`
- `retailer_logo_url`

Treat `retailer_key` as a selection hint, not a store-inventory guarantee.

## MCP coverage

Official MCP create tools mirror page creation only:

- `create-recipe`
- `create-shopping-list`

Use REST for retailer lookup and any unsupported diagnostics.

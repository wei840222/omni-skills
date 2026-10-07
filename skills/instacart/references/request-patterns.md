# Request Patterns - Instacart

## Recipe page

```bash
curl -sS "https://connect.dev.instacart.tools/idp/v1/products/recipe" \
  -H "Authorization: Bearer $INSTACART_API_KEY" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Weeknight tomato pasta",
    "image_url": "https://example.com/pasta.jpg",
    "instructions": ["Boil pasta", "Simmer sauce", "Combine and serve"],
    "ingredients": [
      {
        "name": "spaghetti",
        "measurements": [{"quantity": 1, "unit": "lb"}]
      },
      {
        "name": "crushed tomatoes",
        "filters": {"brand_filters": ["Muir Glen"]},
        "measurements": [{"quantity": 1, "unit": "can"}]
      }
    ],
    "landing_page_configuration": {
      "partner_linkback_url": "https://example.com/recipes/pasta",
      "enable_pantry_items": true
    }
  }' | jq
```

Keep only the searchable product name in `name`. Put brand and health intent in
filters. See `references/units.md` for valid units.

## Shopping list page

```bash
curl -sS "https://connect.dev.instacart.tools/idp/v1/products/products_link" \
  -H "Authorization: Bearer $INSTACART_API_KEY" \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Sunday staples",
    "line_items": [
      {
        "name": "bananas",
        "quantity": 6,
        "unit": "each"
      },
      {
        "name": "whole milk",
        "line_item_measurements": [{"quantity": 1, "unit": "gallon"}]
      }
    ],
    "landing_page_configuration": {
      "partner_linkback_url": "https://example.com/staples",
      "enable_pantry_items": true
    }
  }' | jq
```

## Nearby retailers

```bash
curl -sS \
  "https://connect.dev.instacart.tools/idp/v1/retailers?postal_code=90210&country_code=US" \
  -H "Authorization: Bearer $INSTACART_API_KEY" \
  -H "Accept: application/json" | jq
```

## Canonicalization for URL cache

Before hashing a payload into `<state_root>/url-cache.md`:

- Lowercase unit aliases to a supported form.
- Keep product names generic; move brand intent to filters.
- Sort filter arrays when order is not semantic.
- Strip empty optional fields.
- Hash normalized request + environment (dev/prod).

Reuse a cached `products_link_url` when title, items, instructions, filters, and
link settings are unchanged.

## Identifier rules

- Prefer `product_ids` when Instacart ids are already trusted.
- Prefer `upcs` when UPC-priority matching is required.
- Send only one identifier family per item.
- Keep each identifier unique across items in one payload.

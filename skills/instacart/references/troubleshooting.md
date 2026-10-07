# Troubleshooting - Instacart

## HTTP status handling

| Code | Meaning | First action |
|------|---------|--------------|
| 200 | Success | Parse `products_link_url` or retailer list |
| 400 | Bad request | Fix required fields, units, mutually exclusive ids |
| 401 | Unauthorized | Validate token and environment host |
| 403 | Forbidden | Check key permission / endpoint access / approval |
| 404 | Not found | Verify path and resource identifiers |
| 408 | Timeout | Retry with backoff if still needed |
| 429 | Rate limited | Exponential backoff; respect limits |
| 5xx | Server error | Retry with backoff; record incident |

## 400 payload errors

Likely causes:

- missing required fields
- invalid measurement quantity
- invalid health filters
- `product_ids` and `upcs` both present on one item
- duplicate product ids or UPCs across items

Fix the payload locally; retry only after correction.

## 401 or 403

Likely causes:

- wrong API key
- wrong environment host
- insufficient key permission
- production key still pending review

Verify key source, dev vs prod host, and dashboard approval status.

## Weak product matches

Common causes:

- product name includes brand, size, and diet text together
- unsupported or vague units
- filter spelling does not match Instacart expectations
- poor UPC quality

Simplify `name`, move brand/health intent to filters, use supported units, then
add constraints gradually.

## No good retailers

Common causes:

- wrong postal code or country
- market with low assortment coverage
- assuming retailer lookup equals ingredient coverage

Re-run nearby retailer lookup, confirm `country_code`, and compare markets when
the user operates in more than one region.

## Retry policy

Retry only for transient conditions:

- `429`
- `5xx`
- obvious network transport failures

Use exponential backoff. Do not blindly retry payload-validation failures.

## Launch and messaging issues

If production or public messaging is blocked:

- check approval status first
- confirm the production key is active
- review Instacart messaging and trademark requirements before changing copy or logos

Record durable notes in `<state_root>/incidents.md` and `<state_root>/launch-notes.md`.

# Core Rules - Instacart

### 1. Choose the right surface before sending traffic

Decide explicitly between:

- Developer Platform MCP for agent-native `create-recipe` and `create-shopping-list`
- Developer Platform REST for recipe pages, shopping list pages, and nearby retailers with full request control
- Instacart Connect for branded ecommerce, fulfillment, post-checkout, sandbox callbacks, or retailer workflows

Mixing surfaces casually creates auth failures, wrong expectations, and rework.

### 2. Lock environment, auth, and scope first

Before any request, confirm:

- development or production
- the correct base URL for that environment
- `Authorization: Bearer <API key>` for Developer Platform REST
- whether the API key has the required permission level and endpoint access

Use production keys only after the integration has passed Instacart review and is active.

### 3. Normalize inputs for matching, not human prose

Instacart matching is heuristic. For each ingredient or line item:

- keep `name` generic and searchable
- keep brand preferences in `filters.brand_filters`
- keep health preferences in `filters.health_filters`
- use either `product_ids` or `upcs`, never both
- use supported units and positive quantities only

Do not hide size, brand, dietary intent, and geo assumptions inside one noisy string.

### 4. Validate geo and retailer context up front

For nearby retailer lookup, use `postal_code` plus `country_code`.

- public docs currently document `US` and `CA`
- retailer lookup returns organization-level `retailer_key`, not a specific store id
- a valid postal code does not guarantee good ingredient coverage

Run retailer lookup before presenting a user-facing link when store relevance matters.

### 5. Add client-side idempotency

Recipe and shopping-list creation return a fresh `products_link_url`. Cache until content changes:

- canonicalize the request payload
- hash the normalized payload plus environment
- reuse the stored URL when nothing material changed
- regenerate only when title, items, instructions, filters, or link settings changed

Avoid recreating identical pages on every run.

### 6. Treat measurements and filters as ranking inputs

- for countable items, prefer `each`
- if multiple measurements are provided, order them intentionally
- keep brand and health filters separate from the product name
- keep brand spelling and health filters exact
- stay conservative on filter count per item for better matches

Poor units and noisy names commonly cause missing quantity or weak matches.

### 7. Respect launch and messaging constraints

Before production:

- complete development testing
- pass the pre-launch and approval workflow
- treat a new production key as non-functional while pending approval
- keep public messaging and logo usage aligned with Instacart guidelines

Claim only approved, guideline-aligned messaging; skip endorsement language and invented brand rules.

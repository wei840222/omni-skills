# Security and Privacy - Instacart

## Data that leaves the machine

- request bodies for recipe pages and shopping list pages
- retailer lookup parameters such as postal code and country
- API key authentication headers
- optional MCP tool payloads

## Data that stays local

- caches and operating notes in `<state_root>/`
- request diffs, retry notes, and approved retailer defaults
- secrets only in the environment or secret manager (never in skill state files)

## This skill does not

- request API keys in chat
- bypass Instacart approval gates
- imply retailer fulfillment features are available through Developer Platform page APIs
- send undeclared traffic outside the documented Instacart surfaces the user selected

## Trust boundary

Using this skill sends data to Instacart services and any explicitly configured
Connect workflows. Install and run it only when the user trusts Instacart with
the grocery and integration data they send.

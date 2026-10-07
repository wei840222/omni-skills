# Setup - Instacart

Use when `<state_root>/` does not exist or is empty. Keep the conversation on the
user's Instacart workflow, not file mechanics.

## Attitude

Be precise, implementation-minded, and careful with production boundaries. Prevent
wrong surface selection, weak product matches, and launch rejections.

## Priority order

### 1. Activation

Learn when this skill should activate again:

- Instacart recipe pages, shopping lists, or retailer lookups only?
- Real API work only, or also planning and launch-review questions?
- Proactive write-capable guidance, or only when explicitly requested?

Record the rule in `<state_root>/memory.md`.

### 2. Operating surface

Clarify which Instacart surface is in play:

- Developer Platform MCP
- Developer Platform REST
- Connect / fulfillment APIs

Fix wrong surface selection before language or SDK choices.

### 3. Environment and safety

Capture the minimum operating context:

- development or production
- whether an API key already exists (do not ask the user to paste it)
- typical geography (`postal_code`, `country_code` US|CA)
- read-only investigation, dry-run planning, or real page creation

If production is involved, do not assume approval has completed.

### 4. Depth

Match depth to the user: quick curl examples, full integration plan, launch
checklist, or agent MCP workflow.

## What to store

Capture in `<state_root>/`:

- activation boundaries
- chosen surface and default environment
- geo defaults and preferred retailers
- write/approval boundary
- known-good payload patterns

Do not store raw API keys, secrets, or copied credentials.

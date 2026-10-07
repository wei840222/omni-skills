# MCP Integration - Instacart

## What MCP covers

Instacart Developer Platform MCP currently exposes create tools for:

- `create-recipe`
- `create-shopping-list`

MCP is ideal when the agent only needs page creation without custom retailer
lookup or deep REST diagnostics.

## Server URLs

| Environment | URL |
|-------------|-----|
| Development | `https://mcp.dev.instacart.tools/mcp` |
| Production | `https://mcp.instacart.com/mcp` |

## Validation flow

1. Connect MCP Inspector with Streamable HTTP.
2. Use the development URL first.
3. Authenticate with a valid Developer Platform development key.
4. List tools and confirm both create tools.
5. Run a small recipe or shopping-list create only after tools appear.

If tools are missing, stop agent integration and fix auth or environment.

## Prefer MCP when

- Fast agent handoff is the goal
- Natural-language page creation is enough
- Minimal custom request assembly is desired

## Prefer REST when

- Nearby retailer lookup is required
- You need request logging, payload diffs, custom retries
- Cache-keyed idempotency must be explicit
- The task exceeds the two create tools

## Operating rule

Default to MCP only when its tool surface fully covers the task. Switch to REST
as soon as retailer discovery, launch diagnostics, or tighter request control is
required.

Note: Instacart also documents broader MCP server offerings with OAuth-oriented
client onboarding under `docs.instacart.com/mcp_servers`. For this skill's
Developer Platform page-creation path, use the Developer Platform MCP tutorial
and API-key auth model above unless the user is explicitly onboarding the other
MCP product family.

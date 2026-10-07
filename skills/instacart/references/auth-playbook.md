# Auth Playbook - Instacart

## Surface matrix

| Surface | Primary auth | Base / entrypoint | Use it for |
|--------|--------------|-------------------|------------|
| Developer Platform REST | `Authorization: Bearer $INSTACART_API_KEY` | `https://connect.dev.instacart.tools` or `https://connect.instacart.com` | recipe pages, shopping list pages, nearby retailers |
| Developer Platform MCP | Developer Platform API key via MCP client config | `https://mcp.dev.instacart.tools/mcp` or `https://mcp.instacart.com/mcp` | agent-native `create-recipe` and `create-shopping-list` |
| Instacart Connect | Separate partner auth (often OAuth client credentials) | Connect API family | branded ecommerce, fulfillment, post-checkout, sandbox |

## Key rules

- Keep development and production keys separate.
- Key scopes include read-only, read-write, and admin; confirm scope before write calls.
- Creating a production key triggers Instacart review; a pending production key does not function.
- Keep keys out of chat, markdown, screenshots, and repo files.
- Always use HTTPS; plain HTTP requests fail.

## Hosts

| Environment | REST base | Path prefix |
|-------------|-----------|-------------|
| Development | `https://connect.dev.instacart.tools` | `/idp/v1/...` |
| Production | `https://connect.instacart.com` | `/idp/v1/...` |

## REST smoke test

Low-risk nearby-retailers probe before page creation:

```bash
curl -sS \
  "https://connect.dev.instacart.tools/idp/v1/retailers?postal_code=94103&country_code=US" \
  -H "Authorization: Bearer $INSTACART_API_KEY" \
  -H "Accept: application/json" | jq
```

## MCP smoke test

1. Point MCP Inspector at `https://mcp.dev.instacart.tools/mcp` (Streamable HTTP).
2. Authenticate with a valid development Developer Platform key.
3. List tools and confirm `create-recipe` and `create-shopping-list`.

If those tools are missing, fix auth or environment before agent integration.

## Production readiness

- Finish development testing first.
- Creating a production key starts review; pending keys stay non-functional.
- Approval also gates public messaging about the integration.

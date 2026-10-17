# Advanced Auth and Permissions — Whop

Use this file only when the user is doing embedded apps, API automation, or
permission-sensitive backend work. Most Whop business work does not need this
layer first.

## Choose the right credential

Live docs describe five credential types (retrieved 2026-10-18):

| Credential | Acts as | Where it belongs | Use when |
|------------|---------|------------------|----------|
| Account or App API key | Your account, or your app across installs | Server only | Backend reaches your own account, or every account that installed your app |
| Account-scoped user token | One user inside one account | Minted on server, used in client | Your product has its own users and needs Whop access without a Whop sign-in |
| Account access token | Your account with narrowed permissions | Minted on server, used in client | Client needs short-lived account access without holding the API key |
| iframe user token (`x-whop-user-token`) | The user viewing your app | Sent by Whop, verified by you | App renders inside Whop and you need to know who is looking |
| OAuth token | A user who signed in with Whop | Your server after OAuth | Sign in with Whop / delegated access outside the iframe path |

Practical routing for agents:
- Server-to-server REST → `Authorization: Bearer ***` with an API key or OAuth
  token against `https://api.whop.com/api/v1` (or sandbox-api in sandbox)
- Embedded Whop app iframe → verify `x-whop-user-token` before trusting identity
- Official embedded components → short-lived access token path, not long-lived
  secrets in the browser

## REST API basics

- Production base URL: `https://api.whop.com/api/v1`
- Sandbox base URL: `https://sandbox-api.whop.com/api/v1`
- Security scheme: bearer auth
- Common scoping ID: `company_id` / account IDs such as `biz_...`
- Common list pagination: `after`, `before`, `first`, `last`

```bash
curl -s https://api.whop.com/api/v1/companies \
  -H "Authorization: Bearer ***"
```

## Embedded app user auth

Whop's iframe sends a JWT in the `x-whop-user-token` header on requests to the
app's `window.location.origin`.

Keep these rules tight:
- Reject missing or invalid `x-whop-user-token` headers
- Verify the token before reading claims
- Treat the header as user identity for the iframe request only
- Use normal bearer auth for background jobs, scheduled tasks, and generic REST

SDK caveat (live docs, 2026-10-18): `verifyUserToken` is documented for
reference, but availability differs by language/package. Prefer the helper your
installed SDK actually ships, and do not invent a TypeScript client method that
is not present.

## Access checks

Use `GET /users/{id}/access/{resource_id}` to confirm whether a user can access
a company, product, or experience and to retrieve their access level.

```bash
curl -s "https://api.whop.com/api/v1/users/$WHOP_USER_ID/access/$WHOP_RESOURCE_ID" \
  -H "Authorization: Bearer ***"
```

The response includes:
- `has_access`
- `access_level`

Treat access levels as increasing privilege:
- `view`
- `read`
- `write`
- `mod`
- `admin`

## Permissions are endpoint-specific

The official API reference lists required permissions on each endpoint. Useful
anchors from published docs / OpenAPI:

- `GET /products` requires `access_pass:basic:read`
- `GET /payments` requires `payment:basic:read` plus related plan, member, and
  promo scopes depending on the fields you need
- `GET /webhooks` requires `developer:manage_webhook`
- `GET /stats/describe`, `GET /stats/raw`, and `GET /stats/sql` require
  `stats:read`

Practical rule: never guess a scope name when the endpoint already documents it.

## Permission lifecycle

When an embedded app needs new permissions:

1. Add the requested permissions in the app's settings
2. Install or re-approve the app for the target company
3. Expect old installs to keep failing until re-approval happens
4. Record which company has approved which permission set

Whop's permissions guide notes:
- Required vs optional permissions change the install experience
- New permissions trigger a re-approval flow
- Creators can re-approve inside Authorized apps settings

For testing installs, the docs use this pattern:

```text
https://whop.com/apps/app_xxxxxxxxx/install
```

## OAuth and access tokens

Use OAuth when the integration needs delegated user access outside the embedded
iframe path. Prefer the `oauth` skill for generic OAuth lifecycle coaching, and
stay here for Whop-specific product wiring.

Use short-lived access tokens when official embedded components need a client
credential. Do not place Account API keys in browser code, mobile apps, or
public repositories.

## Safe defaults

- Keep bearer credentials and webhook secrets in env vars
- Separate sandbox permissions and installs from production
- If auth is ambiguous, choose the narrowest valid credential rather than the
  most powerful one
- Prefer-other to `api` / `oauth` / `webhook` when the ask is not Whop-specific

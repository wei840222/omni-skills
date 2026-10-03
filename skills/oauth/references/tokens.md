## Tokens

- Access token: short-lived (minutes to hour), used for API access. Best practice is to use Sender-Constrained Tokens (e.g. DPoP or MTLS) where possible to prevent stolen tokens from being used.
- Refresh token: longer-lived, used only at token endpoint for new access tokens. OAuth 2.1 requires refresh token rotation or sender-constraining for public clients.
- ID token (OIDC): JWT with user identity claims—authenticate identity with the ID token; authorize API calls with access tokens only
- Do not send refresh tokens to resource servers—refresh only at the authorization server token endpoint

## Scopes

- Request minimum scopes needed—users trust granular requests more
- Scope format varies: `openid profile email` (OIDC), `repo:read` (GitHub-style)
- Server may grant fewer scopes than requested—check token response
- `openid` scope required for OIDC—triggers ID token issuance

## OpenID Connect

- OIDC = OAuth 2.0 + identity layer—adds ID token and UserInfo endpoint
- ID token is JWT with `sub`, `iss`, `aud`, `exp` + profile claims
- Verify ID token signature before trusting claims
- `nonce` parameter prevents replay attacks—include in auth request, verify in ID token

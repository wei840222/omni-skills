## Flow Selection

- Authorization Code + PKCE: use for all clients—web apps, mobile, SPAs
- Client Credentials: service-to-service only—no user context
- Implicit flow: deprecated—use Auth Code + PKCE instead; was for SPAs before PKCE existed (OAuth 2.1 officially omits it)
- Device Code: for devices without browsers (TVs, CLIs)—user authorizes on separate device
- Resource Owner Password Credentials: deprecated in OAuth 2.1—use Auth Code + PKCE instead; highly insecure as it requires the app to see user passwords

## Client Types

- Confidential: can store secrets (backend apps)—uses client_secret
- Public: cannot store secrets (SPAs, mobile)—uses PKCE only
- Omit client_secret in mobile apps or SPAs—it will be extracted

## Token Endpoints

- `/authorize`: user-facing, returns code via redirect
- `/token`: backend-to-backend, exchanges code for tokens; requires client auth for confidential clients
- `/userinfo` (OIDC): returns user profile claims; requires access token
- `/revoke`: invalidates tokens; accepts access or refresh token

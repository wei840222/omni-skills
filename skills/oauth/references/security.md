## PKCE (Proof Key for Code Exchange)

- Required for public clients (SPAs, mobile), recommended for all clients in OAuth 2.1
- Generate `code_verifier`: 43-128 char random string, stored client-side
- Send `code_challenge`: SHA256 hash of verifier (S256 method required), sent with auth request
- Token exchange includes `code_verifier`—server verifies against stored challenge
- Prevents authorization code interception—attacker can't use stolen code without verifier

## State Parameter

- Always include `state` in authorization request—prevents CSRF attacks
- Generate random, unguessable value; store in session before redirect
- Verify returned `state` matches stored value before processing callback
- Can also encode return URL or other context (encrypted or signed)

## Redirect URI Security

- Register exact redirect URIs—no wildcards, no open redirects
- Validate redirect_uri on both authorize and token endpoints
- Use HTTPS always—except localhost for development
- Path matching is exact—`/callback` ≠ `/callback/`

## Security Checklist

- HTTPS everywhere—tokens in URLs must be protected in transit
- Validate `iss` and `aud` in tokens—prevents token confusion across services
- Bind authorization code to client—code usable only by requesting client
- Short authorization code lifetime (10 min max)—single use
- Implement token revocation for logout/security events
- Prevent mix-up attacks using the `iss` response parameter if supporting multiple authorization servers (RFC 9207)

## Common Mistakes

- Using access token as identity proof—use ID token for authentication
- Storing tokens in localStorage—vulnerable to XSS; prefer httpOnly cookies or memory
- Not validating redirect_uri—allows open redirect attacks
- Accepting tokens from URL fragment in backend—fragment is inaccessible to the server
- Long-lived access tokens—use short access + refresh pattern

# Sessions and cookie security

## SECRET_KEY

- Required to sign the session cookie. Generate with `secrets.token_hex(32)` (or equivalent CSPRNG)—never a guessable string or repo default left in production.
- Missing or weak key ⇒ unsigned or forgeable session payload.
- Rotating the key invalidates existing sessions; plan dual-key strategies only when you intentionally support a rotation window.

## Cookie flags (production)

| Setting | Purpose |
|---------|---------|
| `SESSION_COOKIE_SECURE=True` | Cookie only on HTTPS |
| `SESSION_COOKIE_HTTPONLY=True` | Not readable from JavaScript |
| `SESSION_COOKIE_SAMESITE="Lax"` (or `"Strict"`) | CSRF reduction on cross-site navigation |
| `PERMANENT_SESSION_LIFETIME` | Bound session lifetime when `session.permanent = True` |

## Practices

- Mark only needed keys on `session`; treat session as server-trusted signed client state, not an encrypted vault for secrets.
- Prefer server-side session interface (Redis/DB) when payload size, revocation, or secrecy matters.
- Never log full session contents or put tokens in query strings.

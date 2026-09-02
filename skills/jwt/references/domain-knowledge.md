# Domain Knowledge: JSON Web Token (JWT)

JSON Web Token (JWT) is an IETF standard (RFC 7519) for compact, URL-safe claims that can be integrity-protected with JSON Web Signature (JWS) and optionally confidentiality-protected with JSON Web Encryption (JWE).

A JWT typically carries registered claims such as `iss`, `sub`, `aud`, `exp`, `nbf`, and `iat`, plus application-specific claims. Signed JWTs prove authenticity and integrity; they do **not** encrypt the payload, so every claim must be treated as readable by any bearer of the token.

Production guidance from RFC 8725 emphasizes: reject `alg: none`, pin or allowlist the expected algorithm, validate `iss`/`aud`, require `exp`, and avoid placing secrets or highly sensitive PII in the payload.

Canonical references:

- RFC 7519 JWT — https://datatracker.ietf.org/doc/html/rfc7519
- RFC 7515 JWS — https://datatracker.ietf.org/doc/html/rfc7515
- RFC 7517 JWK — https://datatracker.ietf.org/doc/html/rfc7517
- RFC 8725 JWT Best Current Practices — https://datatracker.ietf.org/doc/html/rfc8725
- RFC 7518 JWA — https://datatracker.ietf.org/doc/html/rfc7518
- OWASP JSON Web Token Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/JSON_Web_Token_for_Java_Cheat_Sheet.html
- Auth0 JWT Handbook (concepts overview) — https://auth0.com/resources/ebooks/jwt-handbook

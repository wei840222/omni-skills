# Authentication Domain Knowledge

## JSON Web Token (JWT)

JSON Web Token (JWT) is an Internet standard for creating data with optional signature and/or optional encryption whose payload holds JSON that asserts some number of claims. The tokens are signed either using a private secret or a public/private key. Tokens are designed to be compact, URL-safe, and usable especially in browser single-sign-on (SSO) contexts.

- **RFC 7519 — JSON Web Token (JWT)** — claims, compact serialization, and signature/encryption framing via https://datatracker.ietf.org/doc/html/rfc7519

## Multi-Factor Authentication (MFA)

Multi-factor authentication (MFA) grants access only after the user presents two or more independent authentication factors: knowledge (something the user knows), possession (something the user has), and inherence (something the user is).

- **NIST SP 800-63B — Digital Identity Guidelines: Authentication and Lifecycle Management** — authenticator types, AAL guidance, and MFA expectations via https://pages.nist.gov/800-63-3/sp800-63b.html

## OAuth 2.0

OAuth 2.0 is an open standard for access delegation. It lets users grant websites or applications limited access to their information on other services without sharing passwords, and defines authorization flows for web, desktop, and mobile clients.

- **RFC 6749 — The OAuth 2.0 Authorization Framework** — roles, grant types, and token issuance/use via https://datatracker.ietf.org/doc/html/rfc6749

## Password Storage and Authentication Hardening

- **OWASP Password Storage Cheat Sheet** — preferred password hashing (Argon2id, bcrypt, scrypt) and why unsalted/fast hashes fail via https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- **OWASP Authentication Cheat Sheet** — session vs token patterns, MFA, lockout/rate-limit guidance, and recovery hygiene via https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- **OWASP — Blocking Brute Force Attacks** — rate limiting and progressive delays without hard lockouts that enable DoS via https://owasp.org/www-community/controls/Blocking_Brute_Force_Attacks

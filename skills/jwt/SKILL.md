---
name: jwt
description: "Implement and validate secure JWT authentication. Use when working on authentication, authorization, or token management."
metadata:
  openclaw: '{"emoji":"🔐"}'
---

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Algorithm selection | `references/algorithms.md` | When deciding or reviewing JWT signing algorithms |
| Token lifecycle | `references/lifecycle.md` | When implementing token expiration, refresh, or revocation |
| Validation checklist | `references/validation.md` | When verifying incoming JWTs on the server |
| Common attacks | `references/attacks.md` | When auditing JWT security or investigating vulnerabilities |
| Implementation | `references/implementation.md` | When writing or updating JWT code using libraries |
| Key Rotation | `references/key-rotation.md` | When managing JWKS or rotating signing keys |
| Common Mistakes | `references/common-mistakes.md` | When reviewing JWT implementation for standard errors |
| Storage | `references/storage.md` | When deciding where to store tokens on the client side |
| Audience & Issuer | `references/audience-and-issuer.md` | When verifying cross-service tokens or setting scope |
| Required Claims | `references/required-claims.md` | When defining what goes into the token payload |
| Algorithm Choice | `references/algorithm-choice.md` | When choosing between HS256, RS256, and ES256 |
| Security Fundamentals | `references/security-fundamentals.md` | When reviewing core JWT concepts |
| Domain Knowledge | `references/domain-knowledge.md` | When general facts about the standard are needed |
| Research Sources | `references/sources.md` | When citing or refreshing JWT standards and guidance |

## Workflow

1. Confirm the expected algorithm and key material before parsing any token.
2. Verify the signature first; only then evaluate `exp`, `nbf`, `iat`, `iss`, and `aud`.
3. Reject `alg: none` and any algorithm outside an explicit allowlist.
4. Keep access tokens short-lived; pair them with refresh-token rotation when sessions must survive.
5. Prefer httpOnly Secure cookies with CSRF defenses over localStorage when the browser is the client.
6. Load only the reference file needed for the current trap (algorithm, lifecycle, storage, JWKS, or attacks).

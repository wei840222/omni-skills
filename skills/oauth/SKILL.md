---
name: oauth
description: Implement OAuth 2.0 and OpenID Connect flows securely. Use when writing OAuth clients, designing auth flows, validating OIDC tokens, or configuring scopes and token endpoints.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔑","os":["linux","darwin","win32"]}'
  related-skills: '{"auth":"General authentication architecture context.","jwt":"Handling JWT validation and claims in OAuth."}'
---

# OAuth 2.0 and OpenID Connect

This skill defines rules for securely implementing OAuth 2.0 and OpenID Connect (OIDC).

## References

Load the following references based on the current task:

- `references/flows.md`: Read when selecting an OAuth flow (e.g., Auth Code, Client Credentials), defining client types (public vs confidential), or interacting with token endpoints.
- `references/tokens.md`: Read when working with access tokens, refresh tokens, OIDC ID tokens, scopes, and token rotation.
- `references/security.md`: Read when implementing PKCE, generating state parameters, securing redirect URIs, or mitigating common OAuth attacks (XSS, CSRF, mix-ups).
- `references/sources.md`: Read when citing OAuth 2.1 / OIDC / BCP sources or verifying Gate 6 URLs.

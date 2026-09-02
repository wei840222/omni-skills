# Audience & Issuer

- `iss` (issuer): who created the token—verify to prevent cross-service token theft
- `aud` (audience): intended recipient—API should reject tokens for other audiences
- `sub` (subject): who the token represents—typically user ID
- Token confusion attack: without aud/iss validation, token for Service A works on Service B

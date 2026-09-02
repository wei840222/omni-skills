# Required Claims

- `exp` (expiration): always set and verify—tokens without expiry live forever
- `iat` (issued at): when token was created—useful for invalidation policies
- `nbf` (not before): token not valid until this time—for scheduled access
- Clock skew: allow 30-60 seconds leeway when verifying time claims

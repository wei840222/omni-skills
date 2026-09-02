# Key Rotation

- Use `kid` (key ID) claim to identify which key signed the token
- JWKS (JSON Web Key Set) endpoint for public key distribution
- Overlap period: accept old key while transitioning to new
- After rotation, old tokens still valid until they expire—plan accordingly

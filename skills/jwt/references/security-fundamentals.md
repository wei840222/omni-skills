# Security Fundamentals

- JWTs are signed, not encrypted—anyone can decode and read the payload; ensure all stored data is safe for public visibility
- Always verify signature before trusting claims—decode without verify is useless for auth
- The `alg: none` attack: reject tokens with algorithm "none"—some libraries accepted unsigned tokens
- Use strong secrets: HS256 needs 256+ bit key; short secrets are brute-forceable

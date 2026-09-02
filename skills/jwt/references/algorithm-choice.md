# Algorithm Choice

- HS256 (HMAC): symmetric, same key signs and verifies—good for single service
- RS256 (RSA): asymmetric, private key signs, public verifies—good for distributed systems
- ES256 (ECDSA): smaller signatures than RSA at comparable security—preferred for size-sensitive cases
- Configure the verifier with an explicit algorithm allowlist; ignore the token header's `alg` claim

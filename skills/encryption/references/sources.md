# Encryption sources

Checked 2026-09-24. Re-read the live page before repeating a numeric threshold.

## Password hashing

- **OWASP Password Storage Cheat Sheet** — prefer Argon2id at a minimum of 19 MiB memory, iteration count 2, and parallelism 1; scrypt minimum N=2^17, r=8, p=1; legacy bcrypt work factor 10 or more with a 72-byte input limit; FIPS PBKDF2-HMAC-SHA-256 at 600,000 or more iterations. Passwords should be hashed, not encrypted.
  - https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

This skill keeps bcrypt cost ≥12, which is stricter than OWASP's legacy floor of 10 and matches the pre-refactor operational rule.

## Symmetric and asymmetric storage

- **OWASP Cryptographic Storage Cheat Sheet** — AES with a key of at least 128 bits, ideally 256, in an authenticated mode (GCM or CCM first); ECB is not a general mode; RSA needs OAEP and, if ECC is unavailable, a key of at least 2048 bits; prefer Curve25519-family ECC; use a CSPRNG, not `Math.random()`.
  - https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html

## What this skill does not cite as a live measurement

CLI examples (`age`, `gpg`, `openssl`, Vault, certbot) are operational patterns, not benchmark results. Treat library defaults as untrusted until the code sets the work factor, nonce size, and algorithm allow-list explicitly.

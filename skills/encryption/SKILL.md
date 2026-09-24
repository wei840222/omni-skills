---
name: encryption
description: >
  Encrypt data at rest, hash passwords, manage keys, and audit cryptographic
  choices. Use when selecting algorithms, generating secrets, wrapping fields
  with envelope encryption, or reviewing TLS, mobile storage, and backups.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔐"}'
  related-skills: '{"passwords":"Password policy, reset, and storage handoff when hashing is the whole task.","crypto-tools":"CLI encrypt, decrypt, sign, and verify commands after the algorithm is chosen.","security-best-practices":"Broader application security review beyond cryptographic primitives.","ssl":"Certificate issuance, renewal, and TLS termination after cipher policy is set.","jwt":"Token signing and verification once the signing algorithm and key rotation are chosen."}'
---

## When to load

Load this skill to choose algorithms, encrypt files or fields, hash passwords, generate secrets, rotate keys, or audit crypto mistakes. It does not replace a password-manager product, a payment-card vault, or a formal compliance audit.

## Progressive disclosure

- **Code patterns:** load `references/patterns.md` for password hashing, CSPRNG tokens, envelope encryption, JWT signing, and key rotation.
- **Mobile storage:** load `references/mobile.md` for Keychain, Keystore, SQLCipher, biometrics, and pinning.
- **Infrastructure:** load `references/infra.md` for TLS renewal, Vault policy, mTLS, encrypted backups, and evidence collection.
- **Sources:** load `references/sources.md` before stating a numeric work factor, key size, or mode preference.

## Algorithm selection

| Purpose | Use | Avoid |
| --- | --- | --- |
| Passwords | Argon2id (19 MiB, t=2, p=1 minimum); bcrypt cost ≥12 only on legacy systems | MD5, SHA-1, plain SHA-256, reversible encryption |
| Symmetric | AES-256-GCM or ChaCha20-Poly1305; unique nonce per message | AES-ECB, DES, RC4, reused GCM nonce |
| Asymmetric | X25519 / Ed25519; RSA-2048+ with OAEP only when ECC is unavailable | RSA-1024, PKCS#1 v1.5 encryption |
| Key derivation | Argon2id, scrypt (N≥2^17, r=8, p=1), or PBKDF2-HMAC-SHA-256 ≥600,000 for FIPS | Single-pass hash |
| JWT signing | RS256 or ES256 with an allow-list and `kid` rotation | `alg=none`, HS256 with a short secret |
| TLS | TLS 1.2+ with AEAD ciphers; prefer TLS 1.3 | TLS 1.0/1.1, SSLv3 |

## Rules

1. Generate a fresh IV or nonce for every encryption and store it with the ciphertext. A repeated AES-GCM nonce under the same key is a confidentiality failure.
2. Prefer an AEAD mode (GCM or ChaCha20-Poly1305). If only CBC or CTR is available, add Encrypt-then-MAC; do not ship unauthenticated ciphertext.
3. Store passwords as adaptive hashes, not encrypted blobs. Hashing is one-way; encryption implies a recoverable key.
4. Load keys from an environment variable, KMS, or Vault. Keep key material out of source, git history, logs, and skill files.
5. Draw keys, IVs, and tokens from a CSPRNG (`crypto.randomBytes`, `secrets`, `SecureRandom`). `Math.random()` and `random()` are not secret generators.
6. Compare secrets with a constant-time function so early mismatches do not leak timing.
7. Use separate keys for encryption, signing, and backup. A key used for two purposes expands blast radius.

## File encryption

```bash
# age: passphrase mode for a local file
age -p -o file.age file.txt
age -d -o file.txt file.age

# GPG symmetric AES-256 when age is unavailable
gpg -c --cipher-algo AES256 file.txt
```

Confirm decryption of a known sample before deleting the plaintext. Do not commit `file.age` keys or GPG passphrases.

## Audit checklist

- [ ] Passwords are adaptive hashes, not plaintext or reversible ciphertext
- [ ] Git history and logs contain no keys, tokens, or `.p8` / `.pem` secrets
- [ ] Keys come from env, KMS, or Vault, not string literals
- [ ] Secrets use a CSPRNG, not `Math.random()`
- [ ] Algorithms match the selection table; MD5, SHA-1, DES, and ECB are absent from new code
- [ ] TLS clients verify the certificate chain; pinning, if used, has a backup pin
- [ ] Each message has a unique IV/nonce stored beside the ciphertext and tag
- [ ] Argon2id meets 19 MiB / t=2 / p=1, or PBKDF2-HMAC-SHA-256 is ≥600,000, or legacy bcrypt cost is ≥12
- [ ] TLS 1.2+ is required and TLS 1.0/1.1/SSLv3 are disabled
- [ ] A written rotation path names the old-key grace window and the verification step

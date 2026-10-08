# Certificate format conversions

## Common formats

| Format | Extension | Description |
| --- | --- | --- |
| PEM | `.pem`, `.crt`, `.cer` | Base64 + headers; default on Linux |
| DER | `.der`, `.cer` | Binary; common in Java/Windows toolchains |
| PKCS#12 | `.p12`, `.pfx` | Password-protected bundle of key + cert (+ chain) |
| PKCS#7 | `.p7b` | Certificate chain **without** private key |

## Conversion commands

**PEM → DER**

```bash
openssl x509 -outform der -in cert.pem -out cert.der
```

**DER → PEM**

```bash
openssl x509 -inform der -in cert.der -out cert.pem
```

**PEM → PKCS#12 (Windows/Java import)**

```bash
openssl pkcs12 -export -out cert.pfx \
  -inkey privkey.pem -in cert.pem -certfile chain.pem
```

**PKCS#12 → PEM**

```bash
# Certificate (no key)
openssl pkcs12 -in cert.pfx -clcerts -nokeys -out cert.pem

# Private key
openssl pkcs12 -in cert.pfx -nocerts -nodes -out privkey.pem
```

Prefer `-nodes` only on a secure admin host; otherwise omit it and set a strong export passphrase, then restrict file modes.

**PKCS#7 → PEM chain**

```bash
openssl pkcs7 -print_certs -in cert.p7b -out cert.pem
```

## Combining and matching

**Build a full chain for Nginx-style stacks**

```bash
cat leaf.pem intermediate.pem > fullchain.pem
```

Order is leaf first, then intermediates toward the root. Roots are usually already in client trust stores and should not be required in the served chain.

**Confirm key matches certificate**

```bash
openssl x509 -noout -modulus -in cert.pem | openssl md5
openssl rsa -noout -modulus -in privkey.pem | openssl md5
# ECDSA keys: compare public keys instead of RSA modulus
openssl x509 -noout -pubkey -in cert.pem | openssl md5
openssl pkey -pubout -in privkey.pem | openssl md5
```

Matching digests mean the files belong together; mismatched digests explain many "key does not match certificate" reload failures.

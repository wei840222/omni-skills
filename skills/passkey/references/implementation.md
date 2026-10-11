# Implementation workflow

## Libraries (start here)

| Stack | Package / project |
|-------|-------------------|
| JS/TS RP | `@simplewebauthn/server` + `@simplewebauthn/browser` — https://simplewebauthn.dev/ |
| Python | `py_webauthn` |
| Rust | `webauthn-rs` |

Prefer these (or equivalent maintained stacks) over custom crypto. They encode ceremony option generation, attestation/assertion verification, and counter checks.

## Registration (create)

1. Authenticate the user by an existing factor (or bootstrap policy).
2. Server generates a **fresh challenge**, stores it with expiry, builds `PublicKeyCredentialCreationOptions` (RP ID, user id/name, pubKeyCredParams, authenticatorSelection, timeout, excludeCredentials).
3. Client calls `navigator.credentials.create({ publicKey })` (or library helper).
4. Server verifies attestation/authenticator data, **origin**, challenge, and stores credential ID + public key + sign count (+ transports).
5. Invalidate the challenge. Confirm success UX and offer adding another device.

## Authentication (get)

1. Server generates a **fresh challenge**, optional `allowCredentials` for known credentials, timeout, `userVerification`.
2. Client calls `navigator.credentials.get({ publicKey })` (or conditional mediation when enabled).
3. Server loads the credential by ID, verifies assertion signature, **origin**, challenge, user presence/UV flags as required, and updates sign count.
4. Invalidate the challenge and establish the application session.

## Option defaults (product-tunable)

| Option | Guidance |
|--------|----------|
| Challenge lifetime | ~60–120s server-side; one-time use |
| Timeout (client) | ≥120s when hybrid/cross-device is in scope |
| `userVerification` | `"required"` for high assurance; `"preferred"` when availability matters more |
| Resident key | Request only when discoverable login (usernameless) is a product goal |
| Attestation | `"none"` for most consumer apps |

## Conditional UI

Where supported, use `mediation: "conditional"` with an input marked for WebAuthn autocomplete so saved passkeys can appear during login. Fall back to an explicit “Sign in with passkey” button.

## Failure recovery

| Symptom | Check |
|---------|-------|
| Immediate client error | HTTPS / localhost, RP ID match, feature support |
| Server verify fail | Challenge expired/reused, wrong origin, credential ID mismatch |
| Works on one device only | User needs a second passkey or recovery factor |
| Random lockouts after loss | Recovery path missing — add password/email/IdP recovery |

## Do

- Generate challenges on the server with a CSPRNG.
- Bind ceremonies to the authenticated user session where applicable.
- Log verification failures without logging raw authenticator private material (there is none on the server) or full attestation blobs in shared logs if policy forbids it.

## Avoid

- Trusting client-supplied challenges or public keys without server verification.
- Implementing CBOR parsing or signature checks by hand.
- Single-passkey accounts with no recovery.
- Copying clawic/homepage promo text into production docs.

# Passkey domain knowledge

Facts below track W3C WebAuthn, FIDO passkey guidance, and common RP libraries.
Re-check `sources.md` when library versions or platform sync behavior may have drifted.

## Security-critical rules

- **Unique challenge per ceremony** — Reused or client-only challenges enable replay.
- **Origin / RP ID validation** — Missing checks allow phishing from similar domains.
- **Sign count** — Store and verify the authenticator signature counter; a non-incrementing count can indicate a cloned authenticator (some syncing passkeys may not advance usefully — treat library guidance as authoritative).
- **No hand-rolled CBOR/COSE** — Parse attestation and authenticator data with established libraries.

## Credential storage

Persist at least:

| Field | Why |
|-------|-----|
| Credential ID | `allowCredentials` / lookup key (store as base64url or equivalent) |
| Public key | COSE key for signature verification |
| Sign count | Clone / replay signal |
| Transports hint | Helps the client pick USB / NFC / internal / hybrid |
| User handle / user ID | Discoverable credential association |

## Registration traps

- `userVerification: "required"` enforces biometric/PIN; `"preferred"` may complete without UV.
- Attestation is usually unnecessary for consumer RPs; requiring it reduces compatibility.
- Allow **multiple passkeys** per account (phone, laptop, security key).
- Resident / discoverable key support varies — do not assume every authenticator can store discoverable credentials.
- Exclude credentials already registered for the user when creating a new one (`excludeCredentials`).

## Authentication traps

- Empty `allowCredentials` enables discoverable-credential flows; not every passkey is discoverable.
- Timeouts that are too short fail hybrid / QR cross-device auth — budget ~120 seconds minimum.
- Cross-device auth adds latency (QR + Bluetooth/cable); keep the RP session and challenge alive through the handshake.
- Always map the returned credential ID back to the stored public key before verifying the assertion.

## User experience

- Keep a **password or recovery** path for devices without passkeys and for hardware loss.
- Conditional UI (`mediation: "conditional"`) can surface passkeys in the username field where supported.
- Prefer plain language over “security key” jargon during registration.
- Account recovery must exist — lost hardware must not mean permanent lockout.

## Platform sync behavior (high level)

| Ecosystem | Typical sync |
|-----------|----------------|
| Apple iCloud Keychain | Apple devices in the Apple ecosystem |
| Google Password Manager | Android + Chrome (Google account) |
| Windows Hello | Often TPM-local unless a syncing provider is used |
| 1Password / Bitwarden | Cross-platform vault sync when the user enables it |

Exact availability depends on OS version and vendor settings — verify against current platform docs before promising sync.

## Testing

- Chrome DevTools → Application → WebAuthn: virtual authenticators without hardware.
- CI: virtual authenticators / library test helpers instead of physical keys only.
- Cover both discoverable and non-discoverable credentials.
- Cross-browser: Safari, Chrome, Firefox (and platform authenticators) differ in UX and transports.

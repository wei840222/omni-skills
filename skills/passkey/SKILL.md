---
name: passkey
description: >
  Implement and review WebAuthn passkeys for registration, authentication,
  credential storage, and cross-platform UX. Use when the user builds or audits
  passkey/WebAuthn flows, chooses libraries, sets userVerification/resident-key
  options, or debugs challenge, origin, or sign-count failures. Prefer oauth or
  passwords for those products; use auth for general auth architecture.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🔐"}'
  related-skills: '{"auth":"General authentication architecture beyond WebAuthn.","oauth":"OAuth/OIDC flows instead of passkeys.","passwords":"Password and recovery paths alongside passkeys.","security-best-practices":"Broader app security controls.","chrome":"Chrome WebAuthn DevTools and platform quirks.","safari":"Safari/Apple passkey and iCloud Keychain behavior."}'
---

# Passkey

WebAuthn / FIDO2 **passkeys** replace shared passwords with device-bound public-key
credentials. This skill is **knowledge-only** and keeps no local runtime state tree.

## When to use

- Design or review registration / authentication ceremonies
- Choose server libraries and credential storage fields
- Set `userVerification`, resident keys, timeouts, and allowCredentials
- Debug replay, phishing-adjacent origin mistakes, or cloned-authenticator signals
- Plan password fallback and account recovery when hardware is lost

Prefer `oauth` or `passwords` when the product is not WebAuthn. Hand general auth
layout to `auth`.

## Progressive disclosure

| Need | Load |
|------|------|
| Security rules, storage, registration/auth traps | `references/domain.md` |
| Ceremony workflow and library defaults | `references/implementation.md` |
| Official anchors for fact checks | `references/sources.md` |

## Core rules

1. **Server-issued unique challenge** — Generate a fresh cryptographic challenge per ceremony, store it server-side, bind it to the session, and expire it quickly (about 60–120 seconds). Client-only `new Uint8Array(32)` is not a server challenge.
2. **Validate origin / RP ID** — Verify `origin` and relying-party ID on every response so look-alike domains cannot complete the ceremony.
3. **Persist credential ID, public key, and sign count** — Store credential ID (encoded), COSE public key material, and signature counter; reject or flag when the counter fails to advance (clone signal). Use established libraries for CBOR/COSE — do not hand-roll parsers.
4. **Prefer battle-tested libraries** — SimpleWebAuthn (JS/TS), py_webauthn (Python), webauthn-rs (Rust), and platform stacks that implement the W3C WebAuthn verification steps.
5. **`userVerification` is a product decision** — `"required"` enforces biometric/PIN; `"preferred"` may skip UV. Document the choice; do not assume UV always ran.
6. **Attestation is optional for most RPs** — Requiring attestation reduces device compatibility; enable only when enterprise policy needs it.
7. **Support multi-device + recovery** — Allow multiple passkeys per account; keep a password or other recovery path so hardware loss does not permanently lock the user.
8. **UX timeouts for cross-device** — Cross-device (QR / hybrid) flows need generous timeouts (about 120s+); keep the session alive through the Bluetooth/cable handshake.

## Workflow

1. Confirm product scope (passkey vs OAuth vs password) and platforms (Apple / Google / Windows / security keys).
2. Load `references/domain.md` for storage fields and traps; load `references/implementation.md` for ceremony steps.
3. Implement registration then authentication with server challenges, origin checks, and sign-count updates.
4. Add conditional UI (`mediation: "conditional"`) and clear recovery messaging when the product needs passwordless login UX.
5. For mutable API/library claims, re-open URLs in `references/sources.md` rather than relying on memory.
6. When a ceremony fails, load recovery checks in `references/implementation.md` and offer a clear next step (retry, another device, or password recovery) instead of only listing prohibitions.

---
name: passwords
description: >
  Protect credential-handling requests by keeping passwords, API keys, tokens,
  and recovery codes out of agent context. Use when a user asks to store,
  retrieve, rotate, audit, share, or check a password or other secret.
metadata:
  version: "1.2.0"
  openclaw: '{"emoji":"🔐"}'
---

## Safety boundary

Keep every credential value, master password, recovery code, and TOTP seed inside a user-controlled password manager or the target service's local interface. This skill guides the user through the surrounding decision and process; it does not create a vault, accept secret values, retrieve secrets, or persist credential data.

Credential-bearing text in chat, logs, tool arguments, environment variables, and agent-created files crosses that boundary. Ask the user to remove or redact it, then continue with non-secret metadata only.

## Workflow

### Step 1: Classify the request

Identify the requested action: store, retrieve, rotate, audit, share, or leak check. Capture only non-secret metadata such as the service name, account label, and the user's stated goal.

🔴 **Before a credential would enter the agent context:** keep the value in the user's password manager or local service UI and continue with a redacted description.

Done when: the request has a clear action and contains no credential material.

### Step 2: Choose the safe path

| Action | User-controlled path |
|---|---|
| Store | The user creates or updates an item directly in their existing password manager. Provide field names and a password-policy checklist, but the user enters values locally. |
| Retrieve | The user opens the matching item locally. If the target supports a password-manager integration or secret injection, explain its documented setup without receiving the value. |
| Rotate | The user changes the password through the target service, verifies sign-in locally, then updates the manager item. Help define the new-password policy without generating or seeing the final value. |
| Audit | Review a user-provided, redacted inventory for duplicate, stale, weak-policy, or missing-MFA risks. Keep identifiers and timestamps only when they are needed for the review. |
| Share | Use the password manager's native sharing feature and have the user verify recipient identity and scope in that interface. |
| Leak check | Prefer the password manager's built-in breach monitor. For a user-approved local checker, follow the Pwned Passwords range-query procedure in [references/verification.md](references/verification.md); the password remains local. |

Done when: the user has a local action that keeps the secret outside the agent boundary.

### Step 3: Verify the destination before a user acts

For retrieval, rotation, or sharing, have the user compare the service's registrable domain and HTTPS indicator in their browser or application. Treat an unexpected domain, certificate warning, or account-recovery prompt as a pause condition; direct the user to the service's known official entry point.

Done when: the user has verified the intended destination locally or has stopped to investigate a mismatch.

### Step 4: Close with a redacted result

Report only the completed action and non-secret follow-up: for example, “the user updated the manager entry locally” or “the user will verify the recovery address.” Keep secret values, lengths, character classes, and recovery-word positions out of the summary.

Done when: the requested guidance is complete and no secret has been retained by the agent.

## Password policy checklist

- Use a unique, randomly generated password for each service.
- Prefer the service's MFA or passkey option where available.
- Store recovery codes only in the user's password manager or another user-controlled recovery method.
- Treat financial, primary-email, government, and medical accounts as high-impact: the user performs all reveal, rotation, sharing, and recovery actions locally.

## Failure recovery

| Trigger | Recovery |
|---|---|
| A credential appears in the request | Treat it as potentially compromised: instruct the user to revoke, rotate, or reissue it locally, remove it from the conversation where the platform permits, and continue with redacted metadata. |
| No password manager is available | Provide selection criteria (local control, encryption, recovery process, device support) and wait for the user to choose one; create no agent-managed vault. |
| The requested site or recipient is unexpected | Use the known official site or a verified out-of-band contact before any user action. |
| A leak-check service is unavailable | Record that the check was not completed and use the password manager's local breach-monitoring feature later. |

## Gotchas

- An encrypted file is not a complete password-manager design: recovery, access control, auditability, and secret-delivery boundaries still need a user-controlled implementation. See [references/verification.md](references/verification.md) before recommending a local checker or encryption tool.
- A manager's browser autofill warning or a changed domain is a phishing signal for the user to investigate locally, not a condition for the agent to override.
- A secret passed through an environment variable, command line, or chat can be exposed to unrelated processes, logs, or history. Keep it inside the user's chosen credential manager.
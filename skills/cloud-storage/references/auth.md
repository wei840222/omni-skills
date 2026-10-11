# Authentication Setup

## Service accounts vs user accounts

| Aspect | Service account / workload identity | User account / OAuth |
|--------|-------------------------------------|----------------------|
| Best for | Automation, servers, CI | Interactive user file access |
| Quotas | Often project/workload scoped | Per-user limits common |
| MFA | N/A for pure SA keys; use federation | May be required |
| Audit | Clear machine identity | Mixed with human activity |

**Rule:** Prefer workload identity / IAM roles over long-lived keys for automation. Use user OAuth for consumer drives the human owns.

---

## AWS

```bash
# Session environment (short-lived preferred)
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...
export AWS_DEFAULT_REGION=us-east-1

# Named profiles (~/.aws/credentials + config)
# IAM roles on EC2/ECS/Lambda via instance/task metadata — preferred in AWS
```

**Traps:**

- Long-lived access keys need rotation automation
- Root account keys are an incident, not a convenience
- Region mismatch surfaces as missing bucket/object errors

---

## Google Cloud

```bash
# Service account key file (minimize use; prefer attached SA / WIF)
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json

# User ADC
gcloud auth application-default login

# Impersonation for local dev
gcloud auth application-default login \
  --impersonate-service-account=SA@PROJECT.iam.gserviceaccount.com
```

**Traps:**

- User OAuth tokens are short-lived; refresh before multi-hour jobs
- `gcloud auth login` credentials ≠ Application Default Credentials
- Prefer Workload Identity Federation over downloadable SA JSON keys

---

## Azure

```bash
# Service principal
export AZURE_CLIENT_ID=...
export AZURE_TENANT_ID=...
export AZURE_CLIENT_SECRET=...

az login
az account set --subscription SUBSCRIPTION_NAME_OR_ID

# Managed identity on Azure compute via IMDS — preferred in Azure
```

**Traps:**

- Tenant vs subscription confusion
- SAS tokens leak easily; short expiry + narrow scope
- RBAC assignments can take minutes to become effective

---

## OAuth for consumer services

### Google Drive / Dropbox / OneDrive

1. Create an OAuth app in the provider console
2. Request minimal scopes (example: Google `drive.file` instead of full `drive` when sufficient)
3. Store refresh tokens with host secret handling — never in the skill package
4. Refresh access tokens before long bulk operations

**Traps:**

- Users can revoke refresh tokens at any time
- Scopes silently block operations that look “almost” authorized
- Rate limits are often per user, not only per client ID

### Credential hygiene

- Use placeholders like `AKIA...`, `/path/to/key.json` in examples
- Never commit real keys, tokens, or SAS URLs
- Rotate on suspicion; treat chat logs as untrusted storage

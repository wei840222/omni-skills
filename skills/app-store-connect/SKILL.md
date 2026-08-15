---
name: app-store-connect
description: Execute Apple App Store Connect API workflows for app management, TestFlight distribution, metadata updates, and build submission. Use when the user needs JWT auth, list or update apps, upload/process builds, manage TestFlight groups/testers, submit for App Review, or download sales reports via the App Store Connect API.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🍎","requires":{"env":["ASC_ISSUER_ID","ASC_KEY_ID","ASC_PRIVATE_KEY_PATH"]}}'
  related-skills: '{"ios":"iOS development patterns","swift":"Swift language reference","xcode":"Xcode IDE workflows","mobile-app-analytics":"Mobile metrics including App Store Connect analytics"}'
---

## When to Use

User needs to manage iOS/macOS apps on App Store Connect. Agent handles API authentication, build management, TestFlight distribution, App Review submissions, and analytics retrieval.

## Setup and Operations

When the user requests App Store Connect operations (like TestFlight uploads, API calls, or metadata updates):
1. For authentication rules, JWT generation, and key formats, refer to `references/api-auth.md`.
2. For specific API call sequences, test distribution, and submission flows, refer to `references/workflows.md`.

## Core Rules

### 1. JWT Authentication Required
App Store Connect API uses JWT tokens signed with your private key.

```bash
# Required environment variables:
# ASC_ISSUER_ID     - From App Store Connect > Users > Keys
# ASC_KEY_ID        - From the API key you created
# ASC_PRIVATE_KEY_PATH - Path to your .p8 private key file
```

Generate JWT with ES256 algorithm, 20-minute expiration max. See `references/api-auth.md` for code examples.

### 2. API Versioning
Always specify API version in requests.

```bash
curl -H "Authorization: Bearer $JWT" \
     "https://api.appstoreconnect.apple.com/v1/apps"
```

Current stable version: `v1`. Check Apple docs for v2 endpoints.

### 3. Build Processing States
Builds go through states after upload:

| State | Meaning | Action |
|-------|---------|--------|
| PROCESSING | Upload received, processing | Wait |
| FAILED | Processing failed | Check logs |
| INVALID | Validation failed | Fix issues, re-upload |
| VALID | Ready for testing/submission | Proceed |

Only submit a build once its state reaches `VALID`.

### 4. TestFlight Distribution
- **Internal Testing**: Up to 100 members, builds available immediately after processing
- **External Testing**: Up to 10,000 testers, requires Beta App Review for first build of version
- External groups need at least: app description, feedback email, privacy policy URL

### 5. App Review Submission
Before submitting for review:
- All required metadata complete (descriptions, keywords, screenshots)
- App Preview videos under 30 seconds
- Privacy policy URL valid and accessible
- Contact information current

Submission creates an `appStoreVersion` in `PENDING_DEVELOPER_RELEASE` or `WAITING_FOR_REVIEW`.

### 6. Rate Limits
API has rate limits per hour. Handle 429 responses with exponential backoff.

```bash
# Respect Retry-After header
HTTP/1.1 429 Too Many Requests
Retry-After: 60
```

### 7. Bundle ID Management
Bundle IDs are permanent once created; ensure names are final before registration.

- Use reverse-domain notation: `com.company.appname`
- Plan naming carefully before registration
- Each bundle ID can only belong to one team

## Common Traps

- **Expired JWT** - Tokens expire in 20 min max. Regenerate before long operations.
- **Wrong key permissions** - API keys need specific roles (Admin, App Manager, etc.)
- **Missing export compliance** - Apps with encryption need ECCN or exemption documentation
- **Build version collision** - Each build needs unique version+build number combo
- **Screenshot dimensions** - Must match exactly for each device type (no scaling)
- **Phased release confusion** - Phased release is for App Store only, not TestFlight

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| api.appstoreconnect.apple.com | App metadata, build info | App Store Connect API |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- App metadata sent to Apple for App Store listing
- Build information for processing
- Analytics queries

**Data that stays local:**
- API private key (.p8) - keep only on disk at `ASC_PRIVATE_KEY_PATH`
- JWT tokens - generated locally, short-lived
- Downloaded reports

**Operating boundaries:**
- Keep the `.p8` private key out of commits, chat logs, and shared storage
- Use credentials only for the authorized App Store Connect team
- Scope API keys to the least role required for the task

## State location

App Store Connect API primarily manipulates remote Apple state. Optional local artifacts (JWT scratch files, downloaded reports, working notes) may exist in `<workspace>/app-store-connect/`, `<workspace>/memory/app-store-connect/`, `<workspace>/.app-store-connect-state/`, or `~/app-store-connect/`.

Before reading or writing local state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/app-store-connect/`, `<workspace>/memory/app-store-connect/`, `<workspace>/.app-store-connect-state/`, `~/app-store-connect/`.
3. If none exists and local artifacts must be created, default to `<workspace>/app-store-connect/` after user confirmation.

Use the selected `<state_root>` for every local state operation in this skill. Never store `.p8` keys inside the skill package or any version-controlled path; keep keys at `ASC_PRIVATE_KEY_PATH` outside git. Exclude `<state_root>` from version control when it holds reports or temporary files.

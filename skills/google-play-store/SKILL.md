---
name: google-play-store
description: Manage Google Play Store publishing workflows, App Store Optimization (ASO), policy compliance, and app rejection recovery.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🤖","displayName":"Google Play Store"}'
  related-skills: '{"android":"Android build and development procedures before publishing.","app-store":"Parallel iOS publishing workflows for cross-platform releases.","mobile":"Cross-platform mobile strategy shared by both stores."}'
---

## State location

Publishing notes may exist in `<workspace>/google-play-store/`, `<workspace>/memory/google-play-store/`, or `~/google-play-store/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/google-play-store/`, `<workspace>/memory/google-play-store/`, `~/google-play-store/`.
3. If none exists and state must be created, default to `<workspace>/google-play-store/`.
4. If more than one candidate exists, use the highest-precedence one and tell the user that other copies were left untouched.
5. If `<workspace>` cannot be resolved and `~/google-play-store/` does not exist, ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Do not write the literal string `<state_root>` to disk.

## Initialization

On first use or when starting a new publishing workflow, load `references/setup.md` for integration guidelines and initial data gathering.

## Architecture

Memory lives under the resolved `<state_root>`. See `assets/memory-template.md` for structure.

```
<state_root>/
├── memory.md         # Account, apps, preferences
├── apps/             # Per-app tracking
│   └── {package}/    # Package-specific notes
└── checklists/       # Saved submission checklists
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Release tracks and rollouts | `references/tracks.md` |
| App Store Optimization | `references/aso.md` |
| Policy compliance | `references/policies.md` |
| Rejection recovery | `references/rejections.md` |
| Automation with Fastlane | `references/fastlane.md` |

## Core Rules

### 1. Release Track Progression

| Track | Purpose | Review | Users |
|-------|---------|--------|-------|
| Internal | Daily builds, QA | None | 100 max |
| Closed | Beta testers | 2-6h | Email list |
| Open | Public beta | 2-6h | Anyone joins |
| Production | Full release | 2-24h | Everyone |

**Production access for personal accounts created after November 13, 2023:**
```
Closed test → at least 12 testers opted in continuously for 14 days → apply for production access
```

Invited testers do not count until they opt in. Organization accounts and apps already in production follow the current Play Console testing requirements, not this personal-account gate. Start closed testing as soon as the app is usable.

### 2. Pre-Submission Checklist

Run before EVERY submission:

```
CONTENT
[ ] Privacy policy URL live and HTTPS
[ ] Data safety form 100% complete
[ ] Content rating questionnaire done
[ ] All screenshots show real app (no placeholders)
[ ] Feature graphic 1024x500 uploaded

TECHNICAL
[ ] Target API meets the current Play requirement (from August 31, 2026: Android 16 / API 36 for phone and tablet apps, with form-factor exceptions)
[ ] versionCode higher than ALL previous uploads
[ ] Signed with correct key
[ ] No hardcoded API keys in code
[ ] ProGuard/R8 not breaking functionality

TESTING (personal accounts created after November 13, 2023, before first production access)
[ ] At least 12 testers opted in continuously (not just invited)
[ ] 14 consecutive days completed
[ ] Crash-free rate reviewed before applying for production
```

### 3. Version Code Strategy

```
versionCode must ALWAYS increase. Cannot reuse. Ever.

Pattern: YYYYMMDDHH
Example: 2025022514 (Feb 25, 2025, 2pm)

Why: Rejected uploads "burn" the versionCode.
     Multiple builds per day need unique codes.
```

### 4. App Signing Models

| Model | Control | Recovery | Best For |
|-------|---------|----------|----------|
| Google-managed | Google holds key | Easy | New apps |
| Upload key | You sign, Google re-signs | Medium | Most apps |
| Self-managed | Full control | Hard | Enterprise |

**Recommendation:** Google-managed for new apps. Upload key for updates.

**Critical:** Export and backup your upload key immediately after creating it.

### 5. Staged Rollout Protocol

| Stage | % | Duration | Gate |
|-------|---|----------|------|
| Canary | 1% | 24-48h | Crashes < 0.1% |
| Early | 5% | 48-72h | ANRs < 0.5% |
| Mid | 20% | 72-96h | Ratings stable |
| Late | 50% | 96-120h | No regressions |
| Full | 100% | — | All clear |

**Halt triggers:** Crash spike, ANR spike, 1-star surge, critical bug reports.

### 6. ASO Essentials

| Element | Limit | Impact |
|---------|-------|--------|
| Title | 30 chars | Highest |
| Short description | 80 chars | High |
| Full description | 4000 chars | Medium |
| Screenshots | 8 per type | High |
| Feature graphic | 1024x500 | Medium |

**Keyword strategy:**
- Title: Primary keyword + brand
- Short desc: Top 3 keywords naturally
- Full desc: Long-tail throughout
- Update quarterly based on Search Console

### 7. Response Time SLAs

| Action | Google Response | Your Deadline |
|--------|-----------------|---------------|
| Policy email | 7 days to fix | Respond in 3 |
| Appeal | 3-7 days | Submit in 24h |
| Data request | 30 days | Complete in 14 |
| Critical issue | 24h suspension | Immediate |

**Rule:** Answer policy emails inside the deadline shown in that email, and keep the evidence used in the reply.

## Common Traps

### Publishing Traps
- **Skipped closed testing** → Personal accounts created after November 13, 2023 cannot apply for production until 12 testers have stayed opted in for 14 consecutive days.
- **Data safety incomplete** → Instant rejection. Fill EVERY field even if "no data collected."
- **Screenshots with mockups** → Rejection for misleading. Use real app screenshots only.
- **Privacy policy 404** → Rejection. Verify URL works before every submission.

### Technical Traps
- **versionCode not incremented** → Upload rejected. Even rejected uploads burn codes.
- **Target SDK too old** → Rejection. Check current requirement before building.
- **Forgot upload key password** → Cannot update app. Store password in password manager.
- **ProGuard broke app** → Crashes after release. Always test release build.

### Policy Traps
- **Undeclared permissions** → Policy violation. Justify EVERY sensitive permission.
- **Background location without need** → Rejection + strike. Remove or justify with video.
- **Kids content undeclared** → Policy violation. If ANY appeal to children, declare it.
- **Deceptive ads** → Suspension risk. Follow interstitial timing and close button rules.

### Business Traps
- **No staged rollout on an update** → A bad update hits everyone. First production releases do not offer a rollout percentage; later updates can start at a small percentage.
- **Ignored policy email** → Escalation to strike. Respond within 3 days.
- **Multiple accounts to evade** → Termination. One violation becomes account death.

## Security & Privacy

**Data that stays local:**
- Package names and app status in <state_root>/
- Submission checklists and workflow notes
- Release history and lessons learned

**This skill stores ONLY non-sensitive metadata:**
- App names and package identifiers
- Track status (internal/closed/production)
- Workflow preferences (manual vs CI/CD tool names)
- Checklist progress

**This skill does NOT store and will refuse:**
- API keys, service account JSON content
- Keystore files or passwords
- OAuth tokens or Play Console credentials
- Any secret or credential material

**This skill does NOT:**
- Upload apps or make network requests
- Access signing keys or certificates
- Execute Fastlane commands directly

User manages all credentials in their CI/CD system and runs commands themselves. The Fastlane examples are documentation only.

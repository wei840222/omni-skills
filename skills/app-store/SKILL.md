---
name: app-store
description: Manage App Store Connect and Google Play Console publishing, review
  compliance, signing, TestFlight/closed testing, and release readiness. Use when
  submitting mobile apps, handling rejections, setting up developer accounts, or
  coordinating iOS/Android store releases. Do not load for pure ASO keyword work
  already covered by specialized listing skills, or for App Store Connect API-only
  automation (use app-store-connect).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📱"}'
  related-skills: '{"app-store-connect":"API workflows for JWT auth, builds, TestFlight, metadata, and App Review submission.","play-store":"Android Play Console listing, ASO, policy, and release-track details."}'
---

## When to load

Use this skill for cross-platform store publishing and review operations. Load references on demand:

| Situation | Reference |
|-----------|-----------|
| TestFlight / Play testing tracks | `references/testing.md` |
| Fastlane, ASC API, Play Developer API, CI secrets | `references/automation.md` |
| Primary policy and requirement sources | `references/sources.md` |
| Apple App Store Connect API sequences | `app-store-connect` skill |
| Android listing limits, ASO, Play policies | `play-store` skill |

## Scope

App Store Connect (iOS) and Google Play Console (Android). Covers the publishing lifecycle from account creation through updates, rejection handling, monetization setup, and multi-app team roles.

## Account Setup

| Platform | Cost | Time | Key Steps |
|----------|------|------|-----------|
| Apple Developer Program | $99/year | 1-7 days | Enroll → D-U-N-S (orgs) → Payment → Agreements |
| Google Play Console | $25 once | Minutes-48h | Register → Identity verification → Payment profile |

**Apple gotchas:**
- D-U-N-S number required for organizations (free, takes 1-2 weeks)
- Legal entity name must match D-U-N-S exactly
- Agreements (Paid Apps, Apple Pay) must be accepted before features work

**Google gotchas:**
- Identity verification can take 48h+ for new accounts
- Closed testing track required before production (20+ testers, 14+ days for new personal developer accounts)

## iOS Signing

| Asset | What It Is | Where Created | Expires |
|-------|------------|---------------|---------|
| Distribution Certificate | Signing identity | Keychain → App Store Connect | 1 year |
| Provisioning Profile | Links cert + app ID + devices | App Store Connect | 1 year |
| App ID | Unique identifier (bundle ID) | App Store Connect | Never |

**When Xcode says "No signing identity":**
1. Confirm the certificate exists in Keychain Access (login keychain)
2. Confirm the provisioning profile includes that certificate
3. Confirm the Xcode bundle ID matches the App ID exactly
4. Revoke and recreate only after the checks above fail

**Automatic vs Manual Signing:**
- Automatic: Xcode manages certificates/profiles (fine for solo devs)
- Manual: Required for CI/CD, teams, or multiple apps
- Pick exactly one approach per project and use it consistently

## Submission Checklist

Pre-submit verification (both platforms):

- [ ] Privacy policy URL live and accessible
- [ ] All required permissions have usage descriptions
- [ ] App works offline or handles offline gracefully
- [ ] No placeholder content, "lorem ipsum", or test data
- [ ] Screenshots match actual app UI
- [ ] Support email is valid and monitored

**iOS-specific:**
- [ ] Export Compliance (`ITSAppUsesNonExemptEncryption` in Info.plist)
- [ ] App Tracking Transparency if using IDFA
- [ ] Privacy manifest (`PrivacyInfo.xcprivacy`) for required reason APIs

**Android-specific:**
- [ ] Target SDK meets current Play requirement (API 34+ for existing guidance; verify against current Play Console policy before submit)
- [ ] Data safety form completed
- [ ] Content rating questionnaire filled
- [ ] Closed-testing eligibility met for new personal developer accounts (20+ testers, 14+ days)

## Common Rejections

| Code | Meaning | Fix |
|------|---------|-----|
| **4.2** (iOS) | Minimum functionality | Add meaningful features, or clarify value in resolution notes |
| **4.3** (iOS) | Spam/duplicate | Differentiate significantly from similar apps |
| **5.1.1** (iOS) | Data collection | Implement ATT where required; update privacy labels/manifest |
| **2.1** (iOS) | Crashes/bugs | Test on real devices; fix crash reports before resubmit |
| Deceptive behavior (Android) | Misleading metadata | Match screenshots and copy to real functionality |
| Broken functionality (Android) | App doesn't work as described | Full QA on the production build |

**Appeal strategy:**
1. Read the rejection reason carefully to understand the specific issue
2. If misunderstanding: Explain with screenshots or video
3. If valid: Fix the issue and document what changed in resolution notes
4. Resolve the underlying issue completely before resubmitting the binary

## Review Timeline

| Platform | Typical | Expedited | Slower Periods |
|----------|---------|-----------|----------------|
| Apple | 24-48h | Request via App Review form | New iOS launches, holidays |
| Google | Hours to a few days depending on review queue and changes | N/A | Initial submissions, policy flags |

**Apple expedited review:** Reserve for critical bugs or time-sensitive events. Frequent use reduces effectiveness.

## Monetization Setup

**In-app purchases (IAP):**
1. Create products in App Store Connect / Play Console
2. Implement StoreKit (iOS) / Play Billing (Android)
3. Implement server-side receipt/purchase validation
4. Handle sandbox vs production environments

**Subscriptions:**
- Configure introductory offers, free trials, grace periods
- Implement renewal, cancellation, and billing-retry paths
- Use server notifications for real-time status updates
- Test with sandbox / license-test accounts on both platforms

**Revenue splits:** Apple/Google commission is commonly 15–30% depending on program eligibility and subscription year. Confirm current program rules before promising net revenue.

## Multi-App Management

**Organization structure:**
- Apple: One enrollment, multiple apps, team roles per app
- Google: One developer account, multiple apps, user permissions

**Team roles:**
- Separate "submit builds" from "release to production"
- Marketing should access metadata only
- Finance sees revenue, not code

**Cross-platform releases:**
- Submit iOS first when review is the longer path
- Hold Android production until iOS approval when launch parity matters
- Use staged / phased rollout to catch issues early

## Credentials and secrets

- Keep `.p8`, distribution certificates, provisioning profiles, and Play service-account JSON outside git
- Prefer CI secret stores over local plaintext copies
- For App Store Connect API automation, hand off to `app-store-connect` after account/review context is clear

---
name: xcode
description: Resolve common Xcode compilation and signing errors. Trigger when diagnosing Derived Data cache corruption, bundle identifier mismatches, code signing / provisioning profile issues, build settings overrides, archive-vs-simulator failures, or xcodebuild CLI destination problems.
metadata:
  openclaw: '{"emoji":"🔨","os":["darwin"],"requires":{"bins":["xcodebuild"]}}'
  related-skills: '{"ios":"Native iOS app lifecycle, permissions, entitlements, and App Store review beyond IDE/build settings.","swift":"Swift language mechanics, concurrency, packages, and compiler diagnostics.","app-store-connect":"ASC API for builds, metadata, and TestFlight after a successful archive.","react-native":"Cross-platform RN projects that still hit Xcode signing and archive steps."}'
---

## State location

This skill is mostly operational guidance. Optional local notes (device UDIDs, team IDs, recurring signing traps) may live under a portable state root.

Resolve `<state_root>` before any read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/xcode/`, `<workspace>/memory/xcode/`, `~/xcode/`.
3. If none exists and state must be created, default to `<workspace>/xcode/`.

Never hard-code `~/Library/...` as the only path in instructions that agents will copy. Prefer:

- Derived Data: `<state_root_user_library>/Developer/Xcode/DerivedData` where the user Library is the real macOS home Library (`~/Library` on the developer machine).
- When giving shell commands on the user's Mac, expand to `$HOME/Library/Developer/Xcode/DerivedData`.

Do not store certificates, `.p12`, provisioning profiles with embedded secrets, or App Store Connect API keys under the skill package or git.

## When to load

Load this skill when the user hits Xcode IDE / `xcodebuild` problems rather than pure Swift language or pure iOS lifecycle questions:

- signing / provisioning / team / certificate errors
- Derived Data or module-cache corruption
- build settings hierarchy surprises
- archive works differently from simulator Debug builds
- CLI destination / notarization / `xcodebuild` flag issues

Route elsewhere when the core question is:

- Swift language / concurrency / packages → `swift`
- app lifecycle, permissions, StoreKit, App Review policy → `ios`
- ASC API automation after the archive exists → `app-store-connect`

## Progressive disclosure

| Reference | Load when |
| --- | --- |
| `references/signing.md` | Certificate, profile, team, bundle ID, CI manual signing |
| `references/derived-data.md` | Random module-not-found, stale cache, indexing stuck |
| `references/build-settings.md` | xcconfig / `$(inherited)` / flag hierarchy |
| `references/archive-cli.md` | Archive vs Debug, destinations, notarization CLI |
| `references/sources.md` | Verify Apple doc URLs behind the guidance |

## Reliable defaults

1. Name the failure class first: signing, cache, settings hierarchy, archive config, or CLI destination.
2. Prefer the smallest reversible fix (clean Derived Data) before nuking simulators or keychains.
3. Simulator Debug success does **not** prove Release/archive signing is healthy.
4. Automatic signing is for local interactive Xcode; headless CI needs manual signing (or carefully unlocked keychain + `-allowProvisioningUpdates` with explicit constraints).
5. Bundle IDs and profile app IDs are case-sensitive exact matches.
6. Use `xcodebuild -showBuildSettings` before guessing which flag "won".

## Quick triage

```bash
# Resolved settings for the scheme/config that actually fails
xcodebuild -scheme "<Scheme>" -configuration Release -showBuildSettings | rg 'CODE_SIGN|PROVISIONING|PRODUCT_BUNDLE|DEVELOPMENT_TEAM'

# Derived Data reset on the developer Mac
rm -rf "$HOME/Library/Developer/Xcode/DerivedData"

# List simulators / destinations
xcrun simctl list devices available
xcodebuild -scheme "<Scheme>" -showdestinations
```

## Safety boundaries

- Do not commit signing certificates, private keys, or provisioning profiles.
- Do not recommend disabling SIP, deleting the entire login keychain, or sharing team private keys in chat.
- Do not claim App Store submission success from a local archive alone.
- Prefer Apple documentation commands over third-party "clean my Mac" utilities.

## Common Fixes (entry checklist)

- Build fails with no clear error → Report Navigator / full `xcodebuild` log, not only the Issues pane summary
- Simulator stuck → `xcrun simctl shutdown all` then targeted erase of the broken device, not always `erase all`
- Indexing / autocomplete broken → restart Xcode; if it persists, delete Derived Data
- Capability missing at runtime → Xcode capability, entitlements file, and provisioning profile must all agree

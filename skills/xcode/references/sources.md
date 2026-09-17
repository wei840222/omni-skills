# Xcode domain sources

Primary documentation behind this skill's operational guidance.

## Signing, capabilities, distribution

- **Apple — Maintaining your signing assets** — certificates, identifiers, and profiles via https://developer.apple.com/documentation/xcode/maintaining-your-signing-assets-and-certificates
- **Apple — Distributing your app for beta testing and releases** — archive and distribution overview via https://developer.apple.com/documentation/xcode/distributing-your-app-for-beta-testing-and-releases
- **Apple — Capabilities overview** — capability enablement vs entitlements via https://developer.apple.com/documentation/xcode/capabilities-overview

## Build systems and settings

- **Apple — Build settings reference** — configuration hierarchy and common keys via https://developer.apple.com/documentation/xcode/build-settings-reference
- **Apple — Creating a production-level build** — Release/archive expectations via https://developer.apple.com/documentation/xcode/creating-a-production-level-build

## CLI, simulators, notarization

- **Apple — xcodebuild** — build/archive/export CLI via https://developer.apple.com/documentation/xcode/building-from-the-command-line-with-xcodebuild
- **Apple — `simctl`** — simulator control via `xcrun simctl` man/help on a Mac with Xcode CLT; product overview https://developer.apple.com/documentation/xcode
- **Apple — Customizing the notarization workflow** — `notarytool` via https://developer.apple.com/documentation/security/customizing-the-notarization-workflow

## Application in this skill

- Signing and archive guidance maps to Apple distribution + signing asset docs.
- Build-settings triage prefers `-showBuildSettings` against Apple's build settings reference.
- CLI sections prefer `xcodebuild` / `notarytool` over deprecated `altool` notarization paths.

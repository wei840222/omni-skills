# iOS Domain Sources

Primary sources that back the practices encoded in this skill.

## App lifecycle, background, and termination

- **Apple — Preparing your UI to run in the background** — scene save/restore and background execution limits via https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background
- **Apple — BGTaskScheduler** — `BGAppRefreshTask` / `BGProcessingTask` scheduling and discretionary execution via https://developer.apple.com/documentation/backgroundtasks/bgtaskscheduler
- **Apple — Responding to memory and resource warnings** — jetsam and memory pressure handling via https://developer.apple.com/documentation/xcode/responding-to-memory-and-resource-warnings

## Permissions, privacy, and entitlements

- **Apple — Requesting authorization to use location services** — purpose strings and prompt-at-point-of-use guidance via https://developer.apple.com/documentation/corelocation/requesting-authorization-to-use-location-services
- **Apple — Protecting the user’s privacy** — Info.plist usage descriptions and privacy practices via https://developer.apple.com/documentation/uikit/protecting_the_user_s_privacy
- **Apple — Privacy manifest files** — required-reason APIs and third-party SDK manifests via https://developer.apple.com/documentation/bundleresources/privacy_manifest_files

## Deep links, StoreKit, and App Review

- **Apple — Supporting universal links in your app** — AASA, path patterns, and CDN caching via https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app
- **Apple — StoreKit 2** — transactions, entitlements, and on-device verification via https://developer.apple.com/documentation/storekit
- **Apple App Store Review Guidelines** — functional completeness, privacy disclosure, and digital-goods rules via https://developer.apple.com/app-store/review/guidelines/

## Application in this skill

- Core rules and traps map permission, background-budget, and review failures to the Apple docs above.
- Termination-code and budget tables stay operational; Apple lifecycle and memory docs are the authority for watchdog/jetsam behavior.
- Store and privacy guidance stays checklist-oriented; App Review Guidelines and privacy-manifest docs are authoritative for rejection categories.

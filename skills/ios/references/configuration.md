# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| ui_framework | swiftui \| uikit \| mixed | mixed | Which API every example is written in, and which lifecycle model `core-rules.md` assumes |
| min_deployment_target | current \| n-1 \| n-2 \| explicit (e.g. `iOS 17`) | n-1 | Which APIs may be used without an availability guard, and the drop threshold in Rule 2 |
| target_devices | iphone \| ipad \| universal \| universal+mac | iphone | Size-class, multitasking and orientation guidance in `core-rules.md`; which review rules apply |
| dependency_manager | spm \| cocoapods \| mixed | spm | Integration steps, and where third-party privacy manifests come from (`security-privacy.md`) |
| release_tooling | xcodebuild \| fastlane \| xcode-cloud \| manual | xcodebuild | Dialect of every release and upload example in `traps.md` / `output-gates.md` and `output-gates.md` |
| crash_reporter | organizer \| metrickit \| sentry \| firebase \| bugsnag | organizer | Where `termination-codes.md` sends you first, and whether symbolication is manual |
| tracking_policy | none \| att | none | Whether ATT, IDFA and tracking-label guidance appears at all (`security-privacy.md`) |
| audience | general \| kids \| health \| finance | general | Extra review and data rules applied unprompted — kids category forbids tracking outright and changes ads, analytics and login rules |
| beta_os_policy | adopt-early \| wait-for-x1 | wait-for-x1 | Whether beta APIs get used, and when the annual regression pass lands in `## Due` |
| build_number_scheme | increment \| ci-run \| timestamp | increment | How the next build number is produced and recorded in `<state_root>/releases/<year>.md` |

Preference areas — customizable dimensions; a stated preference gets recorded in `<state_root>/config.yaml` and applied from then on:

- **Tooling** — Swift Testing vs XCTest for platform tests, XCUITest usage, Instruments vs MetricKit for measurement, mock vs sandbox StoreKit, snapshot testing — affects which shape every verification step takes
- **Conventions** — bundle-id and App Group naming, scheme and configuration layout, feature-flag mechanism, xcconfig vs build settings, folder structure for extensions — affects generated identifiers and file placement
- **Platform** — supported orientations, iPad multitasking stance, Mac Catalyst or visionOS ambitions, minimum device class the app must stay usable on — affects `core-rules.md` and every performance budget
- **Safety posture** — appetite for beta APIs, whether destructive migrations are ever emitted, phased release vs full release by default, expedited-review usage — affects Output Gates and `traps.md` / `output-gates.md`
- **Monetization** — StoreKit 1 vs 2, server-side receipt validation vs on-device, paywall placement, free-trial and offer strategy — affects `where-experts-disagree.md` / `sources.md`
- **Accessibility and localization commitments** — the level the team holds itself to (VoiceOver-complete, Dynamic Type to the largest size, which locales ship) — affects `core-rules.md` and `configuration.md` and what the Output Gates enforce
- **Cadence** — annual OS regression pass, certificate and membership renewals, privacy-manifest review on SDK updates, screenshot refresh, crash-triage rhythm — every accepted cadence becomes a row in the `## Due` table of `<state_root>/memory.md`
- **Output register** — diff vs whole file, code-first vs explanation-first, how much guideline text to quote — affects every answer's shape

# Archive vs build, and CLI

## Archive vs Debug build

| Concern | Typical Debug / simulator build | Archive |
| --- | --- | --- |
| Configuration | Debug | Release (default for archive) |
| Signing | Often relaxed for simulator | Valid signing required for device/distribution |
| Failure mode | "Works on simulator" | Fails at archive/export with cert/profile errors |

Always re-test the Release/archive path after signing changes.

## Useful CLI

```bash
# Inspect destinations for a scheme
xcodebuild -scheme "<Scheme>" -showdestinations

# Example simulator destination (names change by Xcode version)
xcodebuild -scheme "<Scheme>" -destination 'platform=iOS Simulator,name=iPhone 16' build

# Show resolved settings
xcodebuild -scheme "<Scheme>" -configuration Release -showBuildSettings

# CI auto-sign assist (only with real keychain access)
xcodebuild -scheme "<Scheme>" -destination 'generic/platform=iOS' -allowProvisioningUpdates archive
```

Destination strings must match an available runtime/device exactly; list first, do not guess stale names like old "iPhone 15" if the runtime is gone.

## Notarization

- `xcrun altool` is deprecated for notarization flows.
- Prefer `xcrun notarytool` for current notarization submission/status.

## Dependencies traps

- SPM and CocoaPods can both embed the same library → duplicate symbols.
- `pod install` respects lockfile; `pod update` may drift versions intentionally.

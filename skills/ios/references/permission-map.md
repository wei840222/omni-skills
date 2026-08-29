# Permission Map

Every row is a prompt that fires once per install. Missing purpose string = crash on first access, not a denial.

| Capability | Info.plist key | Notes that decide the implementation |
|---|---|---|
| Camera | `NSCameraUsageDescription` | Simulator has no camera; guard the code path or the demo fails in review |
| Microphone | `NSMicrophoneUsageDescription` | Also required for video capture with audio |
| Photos (read) | `NSPhotoLibraryUsageDescription` | **PHPicker needs no permission at all** — if you only import photos, ask for nothing |
| Photos (write) | `NSPhotoLibraryAddUsageDescription` | Separate prompt from read; limited-access mode returns a subset without telling you |
| Location, in use | `NSLocationWhenInUseUsageDescription` | Always ask for when-in-use first; "always" is a second, later escalation |
| Location, always | `NSLocationAlwaysAndWhenInUseUsageDescription` | The system re-asks the user later and can silently downgrade it |
| Notifications | none (runtime request) | Provisional authorization delivers quietly with no prompt at all — the way to earn the prompt instead of spending it (`traps.md`) |
| Tracking (ATT) | `NSUserTrackingUsageDescription` | Only if you actually track across apps; denial zeroes the IDFA. Governed by `tracking_policy` |
| Contacts / Calendar / Reminders | `NSContactsUsageDescription`, `NSCalendarsUsageDescription`, `NSRemindersUsageDescription` | Newer OSes offer limited or write-only variants — prefer them, they are granted more often |
| Local network | `NSLocalNetworkUsageDescription` + Bonjour services list | Discovery silently returns nothing when the list is missing |
| HealthKit / Motion | `NSHealthShareUsageDescription`, `NSMotionUsageDescription` | Health requires the capability *and* the entitlement, and read denials are indistinguishable from empty data |
| Faceless failure anywhere | — | Check the console for the exact key name; the crash message names it (`permission-map.md`) |

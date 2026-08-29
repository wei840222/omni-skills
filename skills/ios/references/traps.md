# Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Asking for every permission during onboarding | Each prompt fires once per install; a denial before the feature exists is permanent | Prime, then prompt from the action that needs it (Rule 4) |
| Treating a denied permission as an error state | The user is allowed to say no, and review rejects apps that stop working when they do | Ship a degraded path for every permission, and test with all of them denied |
| Debugging universal links by editing the AASA repeatedly | Apple's CDN caches it; you are testing yesterday's file | Validate the JSON once, then check the on-device install with the diagnostics in `traps.md` / `sources.md` |
| Testing push in the simulator and declaring victory | The simulator's push path is not APNs; environment and topic errors never appear | One physical device, production build, before believing push works (`traps.md`) |
| Assuming background refresh runs | The system decides, and it decides "no" for apps the user rarely opens | Make every background path idempotent and reachable in the foreground (Rule 5) |
| Keeping a Core Data or SQLite handle open in an App Group container | Suspension while holding the lock is `0xdead10cc`, and it looks random | Close shared-container handles when entering background |
| Storing tokens in `UserDefaults` | It is a plist in the container, included in unencrypted backups | Keychain with a chosen accessibility class (Rule 7) |
| "Clean reinstall" as a debugging step for credential bugs | Keychain items survive deletion; the reinstall sees the old token | Delete the keychain item explicitly, or key it to an install id |
| Symbolicating with whatever dSYM is on disk | A dSYM whose UUID does not match the build produces plausible, wrong frames | Match `dwarfdump --uuid` to the report's UUID before reading a single line (`termination-codes.md`) |
| Shipping a widget that reads the app's database directly | The extension has its own memory ceiling and no access outside the App Group | Write a small shared snapshot the widget reads (`budgets-and-ceilings.md`) |
| Unlocking entitlements from a local flag after purchase | Local flags are trivially flipped and lost on reinstall | Derive entitlement from current transactions at launch (`where-experts-disagree.md` / `sources.md`) |
| Adding an SDK without its privacy manifest | Since the manifest requirement, a listed SDK without one blocks the upload, at the worst moment | Check the manifest and signature at integration time, not at submission (`security-privacy.md`) |
| Fixing a rejection with an appeal instead of a build | Appeals are for misapplied guidelines; most rejections are a real, small code change | Read the guideline number, change the code, resubmit (`traps.md` / `sources.md`) |
| Releasing to 100% on a Friday | Phased release is the only rollback iOS has, and it only helps if it is switched on | Phased release plus a crash-free-rate gate (Rule 9, `traps.md` / `output-gates.md`) |
| Testing only on the newest device | The oldest supported device is where launch time, memory and jetsam decide | Keep one old physical device in the matrix and record it in the shared inventory (`where-experts-disagree.md`) |
| A hard-won platform fact left in the chat | The same 24-hour AASA cache, entitlement quirk or review objection gets rediscovered every quarter | `## Platform Facts` in `<state_root>/memory.md`, one line (`<state_root>/memory-template.md`) |

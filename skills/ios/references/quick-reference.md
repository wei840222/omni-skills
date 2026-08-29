# Quick Reference

| Situation | Play | Depth |
|---|---|---|
| Rejected by App Review | Read the guideline number literally; the fix is almost always code, not an appeal | `traps.md` / App Review Guidelines in `sources.md` |
| "Missing entitlement" or a capability that does nothing | The capability triangle: App ID, entitlements file, provisioning profile (Rule 3) | `core-rules.md` |
| Permission prompt fails to appear | The purpose string is missing, or it already fired once and was denied | `permission-map.md` |
| Push fails to arrive on device | Token, environment, topic, payload — in that order | `core-rules.md` / `traps.md` |
| Background refresh or upload fails to run | Budget, not bug: registration timing, discretionary transfers, Low Power Mode | `budgets-and-ceilings.md` / `core-rules.md` |
| Universal link opens Safari | AASA fetch, path patterns, and Apple's CDN cache | `traps.md` / `sources.md` |
| Killed with no crash log | Decode the termination code (→ Termination Codes) | `termination-codes.md` |
| Crash only in TestFlight or production | dSYM UUID mismatch; symbolicate before theorizing | `termination-codes.md` |
| Slow launch, jank, or "hangs" reports | 400 ms first frame, 250 ms hang threshold, then Instruments (Rule 6) | `budgets-and-ceilings.md` / `core-rules.md` |
| Widget blank, stale, or killed | Reload budget and the extension memory ceiling | `budgets-and-ceilings.md` |
| Share, notification or keyboard extension crashes | Extensions die far below the app's memory limit and share nothing but the App Group | `budgets-and-ceilings.md` |
| Purchase, subscription or restore fails | Transaction listener, sandbox vs production, entitlement source of truth | `where-experts-disagree.md` / `sources.md` |
| Where should this data live | UserDefaults, Keychain, files, SwiftData/Core Data — and the protection class | `security-privacy.md` |
| Requests fail on device but work in the simulator | ATS, cellular, constrained networks, waiting for connectivity | `traps.md` |
| Privacy manifest, required-reason API, tracking prompt, data label | The four-part manifest and what each SDK owes you | `security-privacy.md` / `sources.md` |
| Layout breaks on another device, in landscape, or at large text | Safe areas, size classes, Dynamic Type, keyboard avoidance | `core-rules.md` |
| VoiceOver unusable, or an accessibility audit failed | Labels, traits, focus order, contrast, 44 pt targets | `core-rules.md` |
| Second language, plurals, or right-to-left | String catalogs, formatters, mirroring | `configuration.md` |
| Version, build number, size limit, or phased release | Release mechanics and what cannot be undone (Rule 9) | `traps.md` / `output-gates.md` |
| Works in the simulator, fails on a device | The simulator is not iOS: sixteen differences, ranked | `where-experts-disagree.md` |
| App launch, scene, or state restoration behaving oddly | Launch paths, scene lifecycle, and what runs before the first frame | `core-rules.md` |
| New iOS version broke a shipped app | Seasonal regression pass and the deprecation ladder | `traps.md` / `output-gates.md` |
| Need the exact command | `simctl`, `devicectl`, `log stream`, symbolication, plist and entitlement dumps | `output-gates.md` |
| Anything else iOS | Name the layer of the five, then reproduce on a physical device before believing anything | — |

Coverage map (load from this package): `core-rules.md` platform rules · `permission-map.md` prompts and purpose strings · `budgets-and-ceilings.md` memory/background ceilings · `termination-codes.md` kill codes · `traps.md` common failures · `security-privacy.md` credentials and manifests · `configuration.md` defaults · `output-gates.md` ship checklist · `where-experts-disagree.md` architecture tradeoffs · `sources.md` primary citations.

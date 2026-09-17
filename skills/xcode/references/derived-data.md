# Derived Data and caches

## Symptoms that point here

- Random "Module not found" after the module clearly exists
- Builds flip between pass/fail without code changes
- Indexing stuck; autocomplete dead
- Failures that started right after an Xcode upgrade

## Preferred cleanup

On the developer Mac:

```bash
# Quit Xcode first when possible
rm -rf "$HOME/Library/Developer/Xcode/DerivedData"
```

Notes:

- `xcodebuild clean` is often insufficient for corrupted module caches.
- Prefer deleting Derived Data over broad "clean my Mac" tools.
- If only indexing is broken, try restart Xcode once before wiping Derived Data.

## Simulator hygiene

```bash
xcrun simctl shutdown all
# Prefer erasing the specific broken device UDID over erase all
xcrun simctl erase <DEVICE_UDID>
```

Use `erase all` only when multiple simulators are corrupted or the user explicitly wants a full reset.

## Package resolution (SPM)

If SPM resolution is stuck:

1. Delete `Package.resolved` only when intentionally forcing re-resolve.
2. Reset package caches from Xcode or the equivalent CLI for the project setup.
3. Watch for SPM + CocoaPods duplicate symbols when both are present.

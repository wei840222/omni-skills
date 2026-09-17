# Build settings hierarchy

## Override order (later wins)

Project → Target → xcconfig → command line

## Preserve parent values

- Use `$(inherited)` when appending. Omitting it replaces parent values and silently drops flags.
- Swift active compilation conditions: prefer `SWIFT_ACTIVE_COMPILATION_CONDITIONS` over stuffing defines into unrelated flag fields.
- Obj-C preprocessor defines: append to `GCC_PREPROCESSOR_DEFINITIONS` instead of wholesale replace when you need both project and target values.

## Debug the winner

```bash
xcodebuild -scheme "<Scheme>" -configuration Debug -showBuildSettings
xcodebuild -scheme "<Scheme>" -configuration Release -showBuildSettings
```

Compare the configuration that fails (often Release/archive), not only Debug.

## Frameworks and install

- "Framework not found": check Framework Search Paths and embed-vs-link.
- `SKIP_INSTALL = YES` for frameworks that should not be copied as top-level archive products incorrectly.

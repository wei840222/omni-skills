# Android Studio Guide

Deep-dive IDE panels, traps, build/emulator tips, and plugins. Confirm the installed
Studio version before asserting menu paths ([releases](https://developer.android.com/studio/releases)).

## Debugging traps

- Breakpoints in hot loops freeze the IDE — use conditional or log breakpoints.
- Debugging release builds often lacks useful symbols — use a debug (or profileable) variant.
- Unfiltered Logcat drowns signal — filter by app package or tag.
- Missing early startup — use **Attach Debugger to Android Process** or "Debug" launch, not only Run.

## Profiling traps

- Profiling pure debug builds skews CPU/Memory — prefer release with `profileable` or a benchmark build ([profile docs](https://developer.android.com/studio/profile)).
- CPU Profiler without filtering is overwhelming — focus call charts on suspect methods.
- Memory heap dumps during GC skew results — trigger GC, then dump.
- Ignoring Network Profiler misses slow API calls — check timing and payload size together.

## Essential IDE features

### Layout Inspector

- Live view hierarchy on a running app ([Layout Inspector](https://developer.android.com/studio/debug/layout-inspector)).
- 3D mode for layer depth; attribute inspection for constraints.
- Works with Compose and the View system when the process is inspectable.

### Database Inspector

- Query Room / SQLite in real time; edit values for testing; export for analysis.
- Requires API 26+ on device/emulator ([Database Inspector](https://developer.android.com/studio/inspect/database)).

### Network Inspector

- Inspect OkHttp/Retrofit-style traffic without ad-hoc logging.
- Request/response bodies and timeline for slow calls.
- Release builds may need explicit instrumentation policy — verify against current docs.

### App Inspection

- Combined Database, Network, and Background Task views when available on the installed build.
- WorkManager / background scheduling inspection where the panel is present.

### Profiler tools

| Tool | Use case |
|------|----------|
| CPU Profiler | Method timing, thread analysis |
| Memory Profiler | Leaks, allocation tracking |
| Energy Profiler | Battery usage patterns (when available) |
| Network Profiler | Request timing, payload size |

## Refactoring shortcuts

| Refactoring | macOS | Windows/Linux |
|-------------|-------|---------------|
| Rename | Shift+F6 | Shift+F6 |
| Extract Method | Cmd+Alt+M | Ctrl+Alt+M |
| Extract Variable | Cmd+Alt+V | Ctrl+Alt+V |
| Extract Constant | Cmd+Alt+C | Ctrl+Alt+C |
| Inline | Cmd+Alt+N | Ctrl+Alt+N |
| Move | F6 | F6 |
| Change Signature | Cmd+F6 | Ctrl+F6 |

## Build configuration (IDE surface)

### Gradle sync issues

- **File → Invalidate Caches / Restart** for stubborn IDE indexes.
- Delete project `.gradle` / `.idea` only as last resort (loses local IDE state).
- Check **Settings/Preferences → Build, Execution, Deployment → Build Tools → Gradle → Gradle JDK**.
- Toolchain version pins belong with the `android` skill; the IDE only points at a JDK.

### Build variants

- Select variant in the **Build Variants** tool window.
- Debug vs Release changes debugging and profiling fidelity.
- Product flavors change applicationId and resources — confirm the selected variant before debugging.

### SDK Manager

- **Tools → SDK Manager** for platform and build-tools updates.
- Install platform tools matching target devices.
- Keep build-tools reasonably current for the AGP in use.

## Emulator tips

- Quick Boot for speed; Cold Boot when state is corrupted ([emulator](https://developer.android.com/studio/run/emulator)).
- Extended Controls for sensors, location, battery, network.
- Snapshots for saving specific device states.
- Device mirroring features vary by Studio version — verify in-product.

## Plugin recommendations (optional)

| Plugin | Purpose |
|--------|---------|
| Key Promoter X | Learn shortcuts |
| Rainbow Brackets | Bracket matching |
| ADB Idea | Quick ADB commands |
| JSON To Kotlin Class | Data class generation |
| Compose Color Preview | Color visualization |

Treat marketplace plugins as optional; prefer built-in tools when they already solve the job.

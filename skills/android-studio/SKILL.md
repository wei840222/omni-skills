---
name: android-studio
description: >
  Optimize Android Studio IDE workflows: debugging, profiling, Layout/Database/Network
  Inspector, platform-specific shortcuts, Gradle sync recovery, emulator tips, and
  refactoring. Use when the user works inside Android Studio or asks for IDE hotkeys,
  profiler setup, or build-sync fixes. Prefer `android` for app/build/runtime code,
  `kotlin` for language craft, and `java` for Java-only syntax.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🤖"}'
  related-skills: '{"android":"App build, runtime, targetSdk, signing, and Play shipping outside the IDE surface.","kotlin":"Kotlin language mechanics, coroutines, and null-safety rather than IDE navigation.","java":"Java syntax and interop details when the codebase is Java-first."}'
---

# Android Studio

IDE-first guidance for **Android Studio** (IntelliJ-based): shortcuts, debugger/profiler,
inspectors, Gradle sync recovery, and emulator productivity. This skill does not replace
platform build or shipping advice in `android`.

## When to load

- Keyboard shortcuts, navigation, Live Templates, and refactoring inside Android Studio
- Debugger strategy (conditional/log breakpoints, Evaluate Expression, attach on startup)
- CPU / Memory / Energy / Network Profiler and App Inspection panels
- Layout Inspector, Database Inspector, Network Inspector
- Gradle sync failures, Build Variants panel, SDK Manager, emulator snapshots

Prefer other skills when the ask is mainly:

- Gradle modules, `targetSdk`, crashes, Play upload → `android`
- Kotlin language / coroutines / collections → `kotlin`
- Java syntax depth → `java`

## State location

Optional IDE preference notes may live under `<workspace>/android-studio/`,
`<workspace>/memory/android-studio/`, or `~/android-studio/`. Resolve `<state_root>` once
per invocation:

1. Use an explicitly configured path when available.
2. Otherwise the first existing directory in that order.
3. If multiple exist, use only the highest-precedence path and report duplicates.
4. Create `<workspace>/android-studio/` only with user consent when no candidate exists.

```
<state_root>/
├── memory.md      # IDE version, platform keymap, project types, pain points
└── shortcuts.md   # Custom shortcuts the user prefers
```

Never commit secrets, keystores, or `local.properties` into the skill package. Load
`assets/memory-template.md` before writing state.

## Routing

Keep `SKILL.md` as the progressive-disclosure router; load supporting files only when needed:

- **First-run intake and preference capture** → `references/setup.md`
- **Full shortcut tables** → `references/shortcuts.md`
- **Breakpoint types and debugger playbooks** → `references/debugging.md`
- **Inspectors, profiler traps, build/emulator/plugins** → `references/android-studio-guide.md`
- **Gate 6 primary sources** → `references/sources.md`
- **State shape** → `assets/memory-template.md`

## Core rules

1. **Confirm the IDE version first** — feature names and menu paths differ across Arctic Fox → Ladybug+ codenames; do not invent panels for an unconfirmed version ([release notes](https://developer.android.com/studio/releases)).
2. **Platform-aware shortcuts** — macOS and Windows/Linux keymaps differ; quote both when the host is unknown.
3. **Prefer IDE inspectors over print-debug** — Layout Inspector for UI hierarchy, Profiler for timing/leaks, Database/Network inspectors for live data and traffic.
4. **Debug the debug variant** — release builds strip symbols; use conditional breakpoints in hot loops; attach debugger for startup races.
5. **Profile release-like builds** — debug overhead skews CPU/Memory; filter profiler recordings to the methods under test.
6. **Sync before guessing Gradle** — invalidate caches only after confirming JDK/AGP alignment; delete `.gradle`/`.idea` as last resort (coordinate with `android` for toolchain pins).

## Quick shortcuts

| Action | macOS | Windows/Linux |
|--------|-------|---------------|
| Search Everywhere | Double Shift | Double Shift |
| Find Action | Cmd+Shift+A | Ctrl+Shift+A |
| Recent Files | Cmd+E | Ctrl+E |
| Navigate to Class | Cmd+O | Ctrl+N |
| Navigate to File | Cmd+Shift+O | Ctrl+Shift+N |
| Refactor This | Ctrl+T | Ctrl+Alt+Shift+T |
| Run | Ctrl+R | Shift+F10 |
| Debug | Ctrl+D | Shift+F9 |
| Evaluate Expression | Alt+F8 | Alt+F8 |
| Rename | Shift+F6 | Shift+F6 |
| Extract Method | Cmd+Alt+M | Ctrl+Alt+M |

## Failure modes


| Symptom | First move |
|---------|------------|
| IDE freezes on breakpoint in a hot loop | Convert to conditional or log breakpoint |
| No symbols / wrong line mapping | Switch to debug build variant; disable minify for that variant |
| Profiler numbers look too slow | Re-run on a non-debuggable or profileable release build |
| Gradle sync loops or JDK errors | Check Preferences → Build → Gradle JDK; align with AGP (see `android`) |
| Layout Inspector empty | App must be debuggable / running; prefer physical device API support matrix |
| Database Inspector unavailable | Requires API 26+ device/emulator and a debuggable app |

## Safety

- Do not recommend shipping debug keystores or disabling verification permanently.
- Treat Logcat dumps and heap dumps as potentially sensitive; redact tokens before pasting.
- Prefer placeholders such as `<PACKAGE_NAME>`, `<DEVICE_SERIAL>` in examples.

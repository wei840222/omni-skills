# Linux and Server-Side Swift

The language is identical; the platform is not. What breaks a macOS-developed package on Linux is almost always one of four things: an Objective-C runtime dependency, a Foundation module split, a case-sensitive filesystem, or a missing runtime library in the container.

## What Simply Does Not Exist

- Apple Objective-C runtime APIs such as KVO, selectors, and method swizzling are unavailable in ordinary Linux Swift builds. Check `@objc` and framework-specific bridging at each use site rather than treating all Swift `dynamic` dispatch or Foundation APIs as Objective-C-only (`interop.md`).
- Apple frameworks: UIKit, AppKit, SwiftUI, Combine, Core Data, Security, os.log. `import os` fails; use swift-log.
- Some Foundation corners behave differently even where they exist — `NSKeyedArchiver`, locale and formatter behavior, and `URL` resource-value APIs are the usual suspects.

Guard with capability checks rather than OS checks: `#if canImport(FoundationNetworking)` says what you actually need, while `#if os(Linux)` breaks the day you add Windows or Android.

## The Foundation Module Split

On Linux, corelibs-Foundation is split, and the pieces are separate modules:

```swift
import Foundation
#if canImport(FoundationNetworking)
import FoundationNetworking   // URLSession, URLRequest
#endif
#if canImport(FoundationXML)
import FoundationXML          // XMLParser, XMLDocument
#endif
```

Missing these imports is one cause of "compiles on my Mac, fails in CI" errors; inspect the actual compiler diagnostic and module availability. Newer toolchains ship a Swift-native Foundation that narrows the behavioral gap between platforms, but the module split still governs what you must import.

## Filesystem and Environment

- Case-sensitive filesystem: `import MyModule` vs a directory named `mymodule`, or `Bundle.module.url(forResource: "Data")` against `data.json`, work on macOS and fail on Linux. This is the second most common CI-only failure.
- Path separators are the same, but `~` is not expanded by the shell in a Swift string — use `FileManager.default.homeDirectoryForCurrentUser`.
- No app bundle: `Bundle.main.resourcePath` points next to the executable. Package resources still work through `Bundle.module` (`packages.md`).
- Signals, process handling, and `Glibc` APIs come from `import Glibc`, mirrored by `import Darwin` on Apple platforms — wrap the difference in one small shim rather than at every call site.

## Building and Shipping

- Multi-stage container: build with the full `swift` image, run on a slim base. The runtime image needs the Swift runtime libraries plus whatever your code links (`libcurl`, `libxml2`, `zlib`, `ca-certificates` are the frequent ones) unless you link statically.
- Static Swift standard-library linkage and a fully static executable are different targets. Verify the selected Swift SDK, native dependencies, runtime libraries, and container base with a deployment smoke test; do not infer scratch-image compatibility from a linker flag alone.
- For macOS-to-Linux cross-compilation, first confirm an installed SDK supports the destination and toolchain; build and run the result in a matching Linux environment before shipping.
- Build in release for anything measured; debug on Linux is as unrepresentative as anywhere else.
- Backtraces: the runtime backtracer is enabled via the `SWIFT_BACKTRACE` environment variable and turns an opaque crash in a container into a symbolicated stack — set it in the image, not per-incident.

## Concurrency and Runtime Differences

- Swift concurrency works on Linux. Measure cooperative-worker and throughput behavior under the deployed container CPU limits rather than assuming a particular host-core mapping.
- Dispatch is available, but there is no main runloop unless you create one: a command-line tool that fires async work and returns exits before the work runs. Use `await` in `@main`'s async entry point, not a semaphore (SKILL.md rule 4).
- Confirm runtime-library and ABI compatibility for the chosen Linux distribution and Swift toolchain; package or link required libraries explicitly and test the resulting artifact on the destination.
- Thread Sanitizer is available on Linux and is worth keeping in CI even after a Swift 6 migration.

## Server Practicalities

- Keep the HTTP framework at the edge and the domain logic in a plain, framework-free target: it stays testable on macOS and portable across framework versions.
- Logging goes through swift-log with a backend chosen by the executable, metrics through swift-metrics; libraries depend on the API packages only, never on a backend.
- Graceful shutdown means catching SIGTERM, cancelling the root task, and awaiting in-flight work — the container will SIGKILL after its grace period regardless.
- Foundation's `JSONDecoder` is portable and adequate; if it becomes the bottleneck, measure before swapping.
- CI matrix: build and test on both a Linux image and macOS if you claim both. A package that only runs its tests on macOS will break on Linux, on a schedule set by your users.

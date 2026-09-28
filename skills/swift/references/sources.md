# Swift source audit (2026-09-28)

This file records primary sources consulted for the refactor. The current Swift language guide identifies itself as Swift 6.4; these pages do not prove historical behavior of every earlier toolchain. Verify version-specific APIs against the actual project compiler, SDK, and deployment target before applying them.

## Language, ARC, and concurrency

- **The Swift Programming Language — Version Compatibility:** https://docs.swift.org/latest/documentation/the-swift-programming-language/compatibility/ — compiler version and language mode are separate; strict-concurrency checking and target migration require explicit configuration.
- **The Swift Programming Language — Concurrency:** https://docs.swift.org/latest/documentation/the-swift-programming-language/concurrency/ — actors, isolation and async suspension; synchronous waiting for asynchronous work can deadlock. It does not guarantee a fixed cooperative-worker count in containers.
- **The Swift Programming Language — Automatic Reference Counting:** https://docs.swift.org/latest/documentation/the-swift-programming-language/automaticreferencecounting/ — class instances remain alive while strongly referenced; a missing `deinit` is not by itself proof of a retain cycle.
- **The Swift Programming Language — Closures:** https://docs.swift.org/latest/documentation/the-swift-programming-language/closures/ — closure capture and escaping behavior; non-escaping closures cannot be stored to outlive the call.

## Collections and portability

- **The Swift Programming Language — Collection Types:** https://docs.swift.org/latest/documentation/the-swift-programming-language/collectiontypes/ — collection behavior; a universal `sorted()` trap for NaN is not established here.
- **Swift Documentation Index:** https://www.swift.org/documentation/ — entry point for Swift, SwiftPM, SDK and platform documentation.
- **Swift Package Manager documentation:** https://docs.swift.org/latest/documentation/packagemanagerdocs — package configuration entry point; check exact tools-version behavior for conditions and unsafe flags before prescribing a manifest change.

## SwiftPM PackageDescription

- **PackageDescription — Swift tools version:** https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html#about-the-swift-tools-version — selects the manifest API and minimum Swift tools version.
- **PackageDescription — SupportedPlatform:** https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html#supportedplatform — undeclared deployment defaults follow the installed SDK, except the documented macOS starting floor.
- **PackageDescription — Package Dependency:** https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html#package-dependency — a local path dependency uses that directory as-is without source-control access.
- **PackageDescription — Resource:** https://docs.swift.org/package-manager/PackageDescription/PackageDescription.html#resource — common Apple resource types may be handled automatically; `process` and `copy` differ in processing and path preservation.

- **Apple PackageDescription — `SwiftSetting.swiftLanguageMode`:** https://developer.apple.com/documentation/packagedescription/swiftsetting/swiftlanguagemode(_:_:) — available in SwiftPM 6.0+, supporting the manifest example with tools version 6.0; actual compilation remains untested here.

## Outstanding checks

The source screen covered `SKILL.md` and all topic references, but did not independently prove every version-specific claim. Four manifest claims were corrected against the linked PackageDescription documentation. In particular, confirm SwiftPM platform-condition availability, Apple SDK floors, Linux SDK/static-linking behavior, and concrete example compilation with a matching Swift toolchain. The local validation machine has no `swift` executable, so no Swift example is certified as compiled here.

- **Swift Evolution SE-0238 — Package Manager Build Settings:** https://github.com/swiftlang/swift-evolution/blob/main/proposals/0238-package-manager-build-settings.md — `unsafeFlags` restrict products of a package from being used as dependencies of versioned packages; a trait is not an exemption.

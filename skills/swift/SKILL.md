---
name: swift
description: Write, debug, and optimize Swift code. Use for Swift concurrency
  deadlocks, EXC_BAD_ACCESS and ARC ownership, Codable failures, compiler type-checking
  timeouts, SwiftUI state resets, or SwiftPM package resolution. Route Xcode signing, IDE settings, App Store
  submission, or iOS app lifecycle.
metadata:
  openclaw: '{"emoji":"🦅","os":["darwin","linux"],"requires":{"bins":["swift"]}}'
  version: '1.0.3'
  related-skills: '{"ios":"iOS apps and platform frameworks","xcode":"Xcode signing, build settings, and IDE issues","macos":"macOS platform behavior"}'
---
## State location

Before reading or writing preferences, use an explicitly configured state root when available. Otherwise choose the first existing directory in this order: `<workspace>/swift/`, `<workspace>/memory/swift/`, `~/swift/`. The host must supply `<workspace>`; do not substitute the current directory. If none exists and the user asks to save preferences, create `<workspace>/swift/` only when the host provides a workspace; otherwise ask for a location. If multiple candidates exist, use only the first and disclose the others without merging or moving data. Keep that directory as `<state_root>` for this invocation. Write only to the resolved concrete state path, and obtain user consent under the host policy before persisting preferences.

User preferences and memory live in `<state_root>/` (see `references/setup.md` on first use, `assets/memory-template.md` for the file format). Existing legacy data elsewhere must not be moved or overwritten without explicit permission.

## When To Use

- Writing, reviewing, or refactoring Swift: models, protocols, generics, async code, SwiftUI views, packages
- Diagnosing a crash from its message, or a hang with no message: nil unwrap, arithmetic overflow, unowned dangling, exclusivity violation, continuation never resumed
- Fixing Swift 6 data-race errors, `Sendable` conformance failures, and actor-isolation diagnostics during a language-mode migration
- Chasing memory: retain cycles, objects that never `deinit`, growth Instruments blames on nothing
- Making builds and binaries faster: type-check blowups, generic bloat, ARC traffic, existential boxing
- Shipping Swift off Apple platforms: Linux and server builds, static linking, Foundation gaps, C interop
- Route Xcode project settings, signing, and provisioning to `xcode`; route App Store review, app lifecycle, and platform frameworks to `ios`

## Work sequence and output checks

For source-sensitive Swift or SwiftPM claims, consult `references/sources.md` and check the actual compiler, SDK, and deployment floor.

1. Collect the user's code, exact diagnostic or crash stack, target platform, compiler version, language mode, and project conventions. Output the confirmed facts and unknowns. If source or crash evidence is absent, provide a conditional example and request the smallest missing artifact rather than claiming a concrete fix.
2. Load the matching Quick Reference path; test the most likely cause against the observed evidence. If it is contradicted, inspect the next plausible cause before editing. Output one scoped fix and the observation that would falsify it.
3. Check the complete proposed change before presenting it: confirm helper visibility across types, every referenced symbol's scope, and all callers shown. If a Swift toolchain is available, type-check the complete snippet and run the narrowest relevant test; otherwise label it uncompiled and state what could not be verified.
4. Apply the relevant safety checks:

- Check the entire emitted Swift snippet, including usage examples, for `!`, `try!`, `as!`, and IUOs beyond `force_unwrap_policy`; replace fallible demo setup with `Data(json.utf8)` or explicit error handling. Give a reviewer-acceptable reason for each survivor.
- For each escaping closure touching `self`, inspect who retains it and choose strong, weak, or unowned capture by the observed ownership graph; every `unowned` passes the lifetime test (rule 2).
- Every `withCheckedContinuation` resumes exactly once on every path, thrown errors included
- Move blocking operations (`.wait()`, `Thread.sleep`, synchronous file or network I/O) off the cooperative executor before awaiting their results (rule 4)
- Mutable global or static state is `let`, actor-isolated, or explicitly justified — it is a data-race error in language mode 6
- Propagate or explicitly handle every error; rethrow `CancellationError` so cancellation remains effective (`references/errors.md`)
- For numeric conversions, check integer fit with `exactly:`/`clamping:`; for floating-point inputs check `isFinite` and representable bounds before converting. Keep monetary values out of `Double`.
- New public API follows the naming rules and carries availability when `deployment_floor` is set (`references/api-design.md`)
- Shared helpers have an access level that permits all shown callers; type-check complete code examples with the available toolchain and report when compilation could not be run

5. **CHECKPOINT — Authorization:** First confirm the exact target. Before migrating state or committing a user-owned change, obtain the authorization required by the host and user. If compilation or reproduction fails, report the first error and missing evidence; keep the unverified fix conditional.


## Quick Reference

| Situation | Play |
|---|---|
| Crash with a Swift message ("Unexpectedly found nil", "Index out of range") | Decode it in Crash Messages below, then `references/debugging.md` for the chain |
| Crash with no message (EXC_BAD_ACCESS, bare SIGTRAP) | Inspect the stack; for Objective-C objects try zombies, for unsafe memory use sanitizers → `references/debugging.md` |
| Object never deallocates, `deinit` never runs | Inspect the memory graph for a remaining strong owner; if it forms a cycle, use `references/arc.md` |
| "Sending value of non-Sendable type", "actor-isolated property" | `references/concurrency.md` for the rule, `references/swift6-migration.md` for the order to fix them in |
| Async code hangs with no error and no CPU | Continuation never resumed, or a blocked cooperative thread (rule 4) → `references/concurrency.md` |
| Upgrading a codebase to Swift 6 language mode | Per-target ratchet, not a big bang → `references/swift6-migration.md` |
| Too many `!`, `try!`, or IUOs; nil handling is noisy | `references/optionals.md` |
| Designing the failure channel: `throws` vs `Result` vs optional, typed throws, retry, cancellation | `references/errors.md` |
| JSON decode throws, keys missing, dates rejected | `references/codable.md` (fractional-second ISO 8601 is the usual one) |
| `any` vs `some` vs generic; a protocol default never gets called | `references/types.md` |
| Unicode, string indices, substrings, regex, locale-sensitive compare | `references/strings.md` |
| Array/Dictionary/Set behavior, ordering, or an O(n²) blowup | `references/collections.md` |
| Arithmetic traps at runtime, a numeric conversion crashes, floats compare wrong, or money needs a type | `references/numerics.md` |
| SwiftUI state resets, views redraw constantly, layout fights back | `references/swiftui.md` |
| Tests flaky, async tests pass before the work finishes | `references/testing.md` |
| Package won't resolve, resources missing, plugin blocked | `references/packages.md` |
| Slow build, slow runtime, oversized binary | `references/performance.md` |
| Objective-C, C, or C++ bridging; unsafe pointers; C callbacks | `references/interop.md` |
| Builds on macOS, fails on Linux or in a container | `references/linux.md` |
| Designing public API: naming, access control, availability, ABI | `references/api-design.md` |
| Property wrappers, result builders, macros, key paths | `references/metaprogramming.md` |
| Anything else | Reduce to the smallest file that still reproduces, compile with `-Onone`, and read the FIRST compiler error — the rest is usually cascade noise |

## Core Rules

1. **`!` is a deliberate crash, not a shortcut.** Recoverable nil → `guard let x else { return }`. Nil that means the program is already broken → `guard let x else { fatalError("config missing: \(key)") }`; the crash log then names the invariant instead of "Unexpectedly found nil while unwrapping an Optional value", which names nothing. Use an implicitly unwrapped `T!` only where initialization or framework lifecycle establishes the invariant (for example IBOutlets or two-phase initialization); a preference never overrides this safety condition.
2. **`weak` when the target can die first; `unowned` only when lifetimes are provably nested.** Test: can the referenced object deallocate while this reference exists? Yes → `weak` (becomes nil, no crash). Provably no, because the referenced object is guaranteed alive whenever the reference is used → `unowned` (a failed lifetime assumption traps rather than returning nil). For an escaping closure, inspect who retains the closure: use `[weak self] in guard let self else { return }` when its owner can form a cycle or `self` may die before callback; a strong capture alone does not prove a cycle. A genuinely non-escaping closure cannot itself be retained beyond the call, so it cannot create a persistent cycle through that call; ordinary `map` and `forEach` callbacks do not need a weak capture merely to avoid a cycle.
3. **Reference type only for identity or lifecycle.** Default `struct`. Reach for `class`/`actor` when the thing has identity (two copies with equal fields are still different things), needs `deinit`, or is genuinely shared and mutated in place. Copy cost is not the tiebreaker: standard-library collections are copy-on-write, so a copy is a retain until someone writes (→ `references/types.md`).
4. **Keep the cooperative pool threads unblocked.** The cooperative executor has limited worker threads; enough blocking `DispatchSemaphore.wait()` calls inside `async` functions can starve tasks needed to signal them, leaving the process hung without a useful error. Bridge blocking work out to a dedicated `DispatchQueue` or thread, and `await` everything else.
5. **Every `withCheckedContinuation` resumes exactly once on every path.** Twice = runtime trap ("SWIFT TASK CONTINUATION MISUSE"). Zero times = the awaiting task hangs forever with no error and no log. Audit every early return, every error branch, and every delegate callback that can fire more than once. Use the `Checked` variants everywhere except measured hot paths — the `Unsafe` ones diagnose nothing.
6. **Actor state is only consistent between `await`s.** Actors serialize access but are reentrant: any `await` inside an actor method lets other calls run and mutate state. Check-then-act across a suspension is a bug. Deduplicate in-flight work by storing the `Task` handle and returning it, not by flipping an `isLoading` flag around an `await`.
7. **`@unchecked Sendable` is a promise you must implement.** Legal only when every mutable stored property is reached through one lock (`Mutex`, `NSLock`, serial queue) with no path around it, and that lock is documented in the type. Otherwise the compiler stops checking and the race ships. Prefer making the type actually Sendable: `let` properties of Sendable types, or an `actor`.
8. **Budget the type-checker.** One unsolvable expression stalls its whole file. Build with `-Xfrontend -warn-long-expression-type-checking=500 -Xfrontend -warn-long-function-bodies=500` (milliseconds) and split whatever it flags — long `+` chains, mixed numeric literals, and large collection literals without type annotations are the repeat offenders. Annotating one intermediate `let` routinely takes a multi-second expression under the threshold.

## Crash Messages

Swift runtime traps surface as `EXC_BREAKPOINT` on arm64 and `EXC_BAD_INSTRUCTION` on x86_64; the human-readable line goes to stderr and lands in crash reports under Application Specific Information. If there is no Swift diagnostic, inspect the crash report and stack before classifying it; memory corruption is one possibility, not the only cause.

| Message | Means | First move |
|---|---|---|
| "Unexpectedly found nil while unwrapping an Optional value" | `!` or IUO on nil | Symbolicate to the line, then replace with `guard let` or a `fatalError` that names the invariant (rule 1) |
| "Index out of range" | Collection subscript past the end | Off-by-one, or an index captured before a mutation; `enumerated()` offsets are not slice indices (`references/collections.md`) |
| "Attempted to read an unowned reference but the object was already deallocated" | `unowned` outlived its target | Switch to `weak`; the lifetimes were not nested (rule 2) |
| "SWIFT TASK CONTINUATION MISUSE: … tried to resume its continuation more than once" | Continuation resumed twice | One-shot guard around the resume, or restructure the callback (rule 5) |
| "Simultaneous accesses to 0x…, but modification requires exclusive access" | Exclusivity violation | Two `inout` arguments aliasing one variable, or a mutating method re-entering itself; copy to a local first |
| "Fatal error: Duplicate keys of type 'X' were found in a Dictionary" | `==` and `hash(into:)` disagree, or duplicates in `uniqueKeysWithValues` | Hash exactly the fields `==` compares (`references/collections.md`) |
| Unexpected sort order | Comparator inconsistent, or NaN in the data | Define an ordering for all values or filter NaN before sorting |
| "Range requires lowerBound <= upperBound" | Computed range inverted | Clamp before constructing — empty ranges are legal, inverted ones trap |
| "Arithmetic operation '… + 1' (on type 'Int') results in an overflow" | Signed/unsigned overflow on `+`, `-`, `*`, or `<<` — traps in release too | Widen the accumulator or use `addingReportingOverflow`; `&+` only when wrapping IS the algorithm (`references/numerics.md`) |
| "Division by zero", "Division results in an overflow" | Integer `/` or `%` with a zero divisor, or `Int.min / -1` | Guard the divisor where it enters the system; floating-point division yields `.infinity` instead of trapping |
| "Negative value is not representable", "Double value cannot be converted to Int…" | Signed → unsigned, or a NaN/infinite/out-of-range `Double` → integer | For integer sources use `Int(exactly:)` or `Int(clamping:)`; for floating-point sources reject nonfinite or out-of-range values first |
| EXC_BAD_ACCESS / KERN_INVALID_ADDRESS with no Swift message | Possible invalid memory access; the fault alone does not identify the cause | Inspect symbolicated frames and ownership; use Zombies for suspected Objective-C lifetime bugs or Address Sanitizer for suspected unsafe memory (`references/debugging.md`, `references/interop.md`) |
| Hang, low CPU, no message | Blocked cooperative thread (rule 4) or an unresumed continuation (rule 5) | Pause in the debugger, `bt all`, look for tasks parked on a semaphore or lock |

## Arithmetic Defaults

Swift traps on integer overflow and on impossible conversions in **release builds too** — arithmetic is a crash surface, not only a correctness one. Choose the operator that states the intent:

| Intent | Write | Not |
|---|---|---|
| Ordinary arithmetic on validated values | `+`, `-`, `*` | `&+` "to be safe": wrapping hides the bug the trap was reporting |
| Wrapping IS the algorithm (hash, checksum, PRNG, ring index) | `&+`, `&*`, `&<<` | `+`, which traps the first time real input wraps |
| Overflow is possible and recoverable | `let (v, o) = a.addingReportingOverflow(b)` | `do`/`catch` — arithmetic never throws, it traps |
| Convert a value that might not fit | For integer sources, `Int(exactly: x)` → nil or `Int(clamping: x)` saturates; for floating-point sources, check `isFinite` and bounds before conversion | `Int(x)`, which traps on out-of-range, NaN, and infinity |
| Money, prices, tax, invoice lines | Integer minor units, or `Decimal` built from a string | `Double` at any stage, including "only for display" |
| Compare two computed `Double`s | Choose an absolute and/or relative tolerance from the domain's error budget, including behavior near zero | A universal fixed ULP multiplier or unqualified `==` |
| Midpoint or average of two arbitrary integers | Use reporting-overflow operations or a wider accumulator when available | Both `(a + b) / 2` and `a + (b - a) / 2` can overflow at the integer bounds |
| Test evenness | `x.isMultiple(of: 2)` | `x % 2 == 1`, false for every negative odd number (`%` takes the dividend's sign) |
| Sort or reduce floats that may contain NaN | Define a total ordering or filter with `isFinite` first | Assuming ordinary `<` defines an order for NaN |

Overflow, conversion, floating-point and money depth: `references/numerics.md`.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| swift_language_mode | 5 \| 6 | project setting, otherwise 5 | Language-mode input for `references/concurrency.md` and `references/swift6-migration.md`; diagnostic severity also depends on compiler and strict-concurrency settings |
| build_tool | swiftpm \| xcode | swiftpm | Examples use `swift build`/`swift test` or a scheme-based invocation; changes where build settings are edited (`references/packages.md`) |
| test_framework | swift-testing \| xctest \| both | swift-testing | Syntax of generated tests and which half of `references/testing.md` applies |
| target_platforms | apple \| linux \| cross-platform | apple | Gates Foundation, `@objc`, and Dispatch assumptions; cross-platform forces `#if canImport` guards (`references/linux.md`) |
| deployment_floor | text (e.g. "iOS 17, macOS 14") | none | When set, every suggested API is checked against it and wrapped in `@available`/`#available` instead of assumed present (`references/api-design.md`) |
| force_unwrap_policy | forbidden \| tests-only \| allowed | tests-only | Whether emitted non-test code may contain `!`, `try!`, or IUO; `forbidden` also rejects `as!` |
| money_representation | minor-units \| decimal | minor-units | Which type the Arithmetic Defaults row for money resolves to when emitting a currency model |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Tooling** — formatter and linter (swift-format vs SwiftLint) and its rule set, whether macro-based libraries are acceptable given their build cost (`references/metaprogramming.md`)
- **Conventions** — default access level, explicit `self.`, doc-comment expectations, one type per file, naming of async vs completion-handler variants
- **Platform** — toolchain version, OS floors, static vs dynamic linking on Linux, architectures built in CI
- **Safety posture** — tolerance for `try!`, `fatalError`, `@unchecked Sendable`, unsafe pointers, and wrapping operators, and whether to flag them unprompted or only on review
- **Dependencies** — Foundation-only vs swift-collections/algorithms/async-algorithms, Combine vs `AsyncSequence`, the vetted third-party list
- **Output format** — full files vs minimal diffs, comment density, whether every change ships with a test
- **Work order** — test-first vs implementation-first, and whether to build and run the suite before handing work back

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| `[weak self]` on every closure | Non-escaping callbacks such as `map` cannot outlive the call; weakening them solely to prevent a cycle adds unnecessary optional handling | Choose capture semantics by the actual ownership and lifetime, especially for escaping or stored closures (rule 2) |
| `DispatchQueue.main.async` inside an `async` function | Hops to main by hand, defeats actor isolation, and hides the requirement from the compiler | `@MainActor` on the function or type; `MainActor.assumeIsolated` when already provably on main |
| `Task { }` fired and forgotten | Unstructured tasks are not cancelled when their scope ends, and a thrown error inside vanishes silently | `async let`/`TaskGroup` for scoped work; store the handle and cancel it when it must stay unstructured |
| `@unchecked Sendable` to silence the compiler | Converts a compile error into a race that only appears under load | Fix the isolation, or implement the lock the annotation promises (rule 7) |
| Retry loop whose `catch` also catches cancellation | Swallowing `CancellationError` makes the task uncancellable and the loop immortal | Rethrow cancellation first, then handle domain errors (`references/errors.md`) |
| `print()` left in shipping code | The string is fully constructed even when nothing reads it, and stdout is synchronized | `os.Logger` or `#if DEBUG`; `Logger` interpolation is lazy and redacts by default |
| Storing a `Substring` | A Substring keeps its parent String's entire buffer alive — parse a 10 MB file, keep 20 short fields, keep 10 MB | `String(substring)` at the boundary (`references/strings.md`) |
| `Array(repeating: MyClass(), count: n)` | The initializer runs once; all n slots hold the SAME instance | `(0..<n).map { _ in MyClass() }` |
| Comparing optionals with `<` | Optional lost its comparison operators in Swift 3; code that "worked" was comparing something else | Unwrap first, or compare with an explicit default |
| Force-trying a decode to "see the error" | `try!` destroys the `DecodingError`, the only thing that names the offending key path | `do`/`catch` and print the error in full (`references/codable.md`) |

## Where Experts Disagree

- **`any` existentials vs generics.** Existential-first reads better and compiles faster; generic-first runs faster (no boxing, no witness-table lookups) and specializes. The honest boundary is measurement: `any` for heterogeneous storage and API surfaces, `some`/generics on hot paths and wherever the concrete type is already known.
- **Swift Testing vs XCTest.** Swift Testing is the better authoring experience (parameterized cases, `#expect` with expression capture, in-process parallelism). XCTest still owns UI automation and performance measurement, so mixed suites are normal rather than a smell. Migrating a green XCTest suite for style alone buys nothing.
- **How hard to fight for value semantics.** One camp makes everything a struct and threads state explicitly; the other accepts reference-typed models where persistence or an Objective-C framework already imposes identity. The line worth defending in either camp: no shared mutable reference type crosses a concurrency boundary without isolation.

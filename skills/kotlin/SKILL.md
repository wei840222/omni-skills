---
name: kotlin
description: >
  Write, debug, and review Kotlin: coroutines and flows, null safety, collections,
  Java interop, Compose state, Multiplatform, and server Kotlin. Load when an NPE
  hits a non-null type, `!!` or a Java platform type blows up, a coroutine leaks or
  fails to cancel, a StateFlow halts emissions, Compose recomposes too much or loses
  state, kapt/KSP or JVM-target errors break the build, JSON puts null into a non-null
  property, or a coroutine test hangs. Not for Java-only codebases or Android
  release/signing configuration.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🟠","requires":{"bins":["kotlin"]},"os":["linux","darwin","win32"],"displayName":"Kotlin"}'
  related-skills: '{"java":"The language on the other side of every interop boundary.","android":"Android build system, release configuration, and deployment.","android-studio":"IDE workflow: debugging, profiling, refactoring.","swift":"The Swift side when Kotlin Multiplatform ships an iOS framework."}'
---

User preferences and memory live under the resolved `<state_root>/` (see `references/setup.md` on first use, `assets/memory-template.md` for the file format).

## State location

Optional durable notes may exist in `<workspace>/kotlin/`, `<workspace>/memory/kotlin/`, or `~/kotlin/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/kotlin/`, `<workspace>/memory/kotlin/`, `~/kotlin/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to `<workspace>/kotlin/`.

Use the selected `<state_root>` for every state operation in this skill. Never write runtime state into this skill package. Do not store credentials, API keys, or keystore material under `<state_root>/`.

Optional layout:

```text
<state_root>/
├── config.yaml     # target_platform, kotlin_floor, ui_toolkit, serialization_lib, annotation_processor, explicit_api
└── memory.md       # stack, pain points, preferences (see assets/memory-template.md)
```

Load `references/sources.md` when verifying language, coroutines, Compose, Multiplatform, or serialization claims against primary docs.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| target_platform | auto \| android \| server \| multiplatform \| library | auto | Picks the default deep-dive file and the idiom set; `auto` infers from build files (AGP plugin → android, Ktor/Spring dependency → server, `kotlin("multiplatform")` → multiplatform) |
| kotlin_floor | text (e.g. "2.0", "1.9") | 2.0 | Gates every version-dependent recommendation in `references/build.md`; below 2.0 the K2-only and Compose-compiler-plugin advice is suppressed |
| ui_toolkit | compose \| views \| none | compose | Switches Android examples between `references/compose.md` state handling and View/ViewBinding lifecycle patterns in `references/android.md` |
| serialization_lib | kotlinx \| moshi \| gson \| jackson | kotlinx | Selects the annotation set, config defaults, and null-safety warnings in `references/serialization.md` |
| annotation_processor | ksp \| kapt \| none | ksp | Drives library setup snippets and the build-speed advice in `references/build.md` |
| explicit_api | bool | false | When true, emitted library code carries explicit visibility and public return types, matching `explicitApi()` strictness |

Preference areas to record as the user reveals them:

- **tooling** — DI (Hilt, Koin, manual), networking client (Retrofit, Ktor client), persistence (Room, SQLDelight, Exposed, JPA), test stack (JUnit4/5, MockK, flow-testing library, Kotest) — affects which examples and setup snippets are offered
- **conventions** — package layout (feature vs layer), formatter/linter (ktlint, ktfmt, detekt), trailing commas, explicit types on public API, naming of sealed state hierarchies — affects generated code and review verdicts
- **platform** — JVM toolchain version, Android min SDK, KMP target list, whether Java sources coexist in the module — affects which floors and interop rules apply
- **safety posture** — tolerance for `!!`, experimental/opt-in APIs, warning suppression, `allWarningsAsErrors` — affects how hard to push back in review
- **legacy bridges** — RxJava, LiveData, callback APIs still in the codebase — affects whether answers stay pure-coroutine or include adapters
- **output format** — KDoc density, tests emitted alongside code, snippet vs full file — affects the shape of every deliverable

## When To Use

- Writing or reviewing Kotlin for correctness: nullability, coroutines, collections, sealed hierarchies, equality
- Debugging Kotlin runtime surprises: NPE on a non-null type, coroutine that fails to finish or fails to cancel, flow that halts emissions, recomposition storm, test that hangs
- Java interop and Java→Kotlin migration, including making Kotlin APIs pleasant to call from Java
- Build and compiler problems that are Kotlin's, not Gradle's: kapt/KSP, JVM-target mismatch, opt-in, K2 migration
- Sharing code across Android, iOS, JVM, or web with Kotlin Multiplatform, or writing server-side Kotlin
- Not for Java-only codebases (→ `java`), Android release configuration, signing and distribution (→ `android`), or IDE workflow (→ `android-studio`)

## When to load references

| Situation | Go to |
|---|---|
| NPE on a non-null type, platform type from Java, `lateinit` not initialized, smart cast refused | `references/null-safety.md` |
| Coroutine leaks, fails to cancel, blocks the main thread, wrong dispatcher, `runBlocking` in production | `references/coroutines.md` |
| StateFlow halts emissions, SharedFlow drops events, `stateIn`/`shareIn` choice, backpressure, cold vs hot | `references/flows.md` |
| Exception vanishes, `async` failure surfaces late, `runCatching` breaks cancellation, error type design | `references/errors.md` |
| Wrong list/map/sequence choice, O(n²) lookup, mutation leaking through a read-only type | `references/collections.md` |
| Scope functions, sealed hierarchies, delegation, destructuring, `use`, DSL builders | `references/idioms.md` |
| Variance/`out`/`in` compile error, type erasure, `reified`, inline/`crossinline`, contracts | `references/generics.md` |
| Calling Kotlin from Java, `@Jvm*` annotations, SAM, checked exceptions, converting a Java file | `references/interop.md` |
| Lifecycle, ViewModel, SavedStateHandle, process death, leaked Context, flow collection on Android | `references/android.md` |
| Recomposition storms, `remember` vs `rememberSaveable`, stability, side effects, lazy lists | `references/compose.md` |
| Coroutine test hangs, passes alone but fails in a suite, virtual time, flow assertions, mocking final classes | `references/testing.md` |
| Allocation in a hot path, boxing, sequences vs lists, inlining cost, value classes, benchmarking | `references/performance.md` |
| kapt vs KSP, JVM-target mismatch, opt-in/experimental, K2, slow incremental builds, library API rules | `references/build.md` |
| JSON null in a non-null property, defaults dropped, polymorphic types, unknown keys, Parcelize | `references/serialization.md` |
| `expect`/`actual`, source sets, Swift/ObjC interop, suspend and Flow across the iOS boundary | `references/multiplatform.md` |
| Spring/Ktor, JPA entity as data class, blocking JDBC in a coroutine, MDC/ThreadLocal lost | `references/server.md` |
| Anything else | The rules and tables below; for pure language semantics, `references/idioms.md` then `references/generics.md`; with no situational match at all, open the file `target_platform` resolves to (`android` → `references/android.md`, `server` → `references/server.md`, `multiplatform` → `references/multiplatform.md`, `library` → `references/build.md`) |

## Core Rules

1. **Nullability is a boundary problem.** Non-null Kotlin types are only as true as the code that fills them: Java, reflection-based JSON, and framework callbacks can all put null into a `String`. Validate at the boundary — parse into a nullable DTO, then map into a non-null domain type. An NPE thrown at the boundary names the field; one thrown three layers later names nothing.
2. **`!!` requires an alternative to have been rejected.** Decision order: value arrives later on one thread → `lateinit var`; computed once on first use → `by lazy`; legitimately absent → nullable + `?:`; caller broke a contract → `requireNotNull(x) { "id missing" }` (throws `IllegalArgumentException`) or `checkNotNull` (`IllegalStateException`). Each of those produces a message; `!!` produces a line number and nothing else.
3. **Every coroutine belongs to a scope whose lifetime is ≥ the work's.** `GlobalScope`, and a `CoroutineScope(Dispatchers.IO)` stored in a field with no cancellation, are leaks by construction: an abandoned screen keeps its network call, its callbacks, and everything they captured. Structured concurrency is the guarantee that "the caller returned" means "the work is over" (→ `references/coroutines.md`).
4. **Cancellation is cooperative.** A cancelled coroutine keeps burning CPU until it reaches a suspension point: `while (true) { transform(chunk) }` with no `suspend` call inside runs continuously. Add `ensureActive()` (or `yield()`) per iteration. Cleanup that suspends after cancellation must run inside `withContext(NonCancellable)`, or it is cancelled before it does anything.
5. **Rethrow `CancellationException` explicitly.** `catch (e: Exception)`, `catch (t: Throwable)` and `runCatching` all capture it, converting "the parent cancelled me" into "I failed" — and the parent then waits on a child that reported success. Shape: `catch (e: CancellationException) { throw e } catch (e: IOException) { … }` — cancellation first, specific types after (→ `references/errors.md`).
6. **StateFlow conflates by `equals`.** Emitting a value equal to the current one runs no collector. Mutate a list in place and re-assign the same reference and nothing is emitted (the new value equals the old one), so the UI "halts updates" with no error anywhere. Publish a new immutable value: `_state.update { it.copy(items = it.items + new) }`.
7. **Choose the dispatcher by what the code blocks on.** CPU work → `Dispatchers.Default` (parallelism = CPU cores, minimum 2). Blocking calls, JDBC, file I/O, legacy SDKs → `Dispatchers.IO` (64 threads by default, property `kotlinx.coroutines.io.parallelism`). UI → `Dispatchers.Main`. For a bounded resource, size the slice to the resource: a 10-connection pool wants `Dispatchers.IO.limitedParallelism(10)`, not 64 threads queueing for 10 connections.
8. **`equals`, `hashCode` and `copy` see only the constructor properties.** A property declared in the class body is invisible to all three: two objects differing only there are equal, collide in a `HashSet`, and `copy()` silently resets it to its initializer. `copy()` is also shallow — the copy shares every mutable object the original held.
9. **Make `when` an expression.** Assigned or returned, a `when` over a sealed type is checked for exhaustiveness, so adding a subclass breaks the build at every decision point that must change. As a bare statement it has only been an error since Kotlin >=1.7, and an `else` branch over a sealed hierarchy silently absorbs every case you add later.

## Nullability Decision Table

| The value | Use | Why not the others |
|---|---|---|
| May genuinely be absent in the domain | `T?` with `?:` / `?.let` | Absence is data, not an error state |
| Set once before first use, non-primitive, no sensible default | `lateinit var` | Nullable would push `?.` into every call site; `lateinit` fails loudly with "property X has not been initialized" |
| Expensive, computed on first read | `by lazy` | Thread-safe by default (SYNCHRONIZED), and no initialization-order trap |
| Required by contract, may be violated by a caller | `requireNotNull` / `checkNotNull` | Produces a message and the right exception type at the boundary |
| Primitive type, or null is an acceptable value | nullable or a default value | `lateinit` supports neither primitives nor nullable types |

Generic caveat: an unbounded `T` includes `T?`, so `fun <T> firstOr(x: T): T` happily accepts null. Write `<T : Any>` when the parameter must be non-null.

## Concurrency Primitive Selection

| Need | Primitive | Trap it avoids |
|---|---|---|
| Work tied to a lifecycle | `scope.launch` | Detached work that outlives its owner |
| Two independent results, both required | `async` + `awaitAll` | Sequential awaits that double latency |
| Move blocking work off the caller's thread | `withContext(Dispatchers.IO)` | Blocking a UI or request thread |
| Fan-out where one failure must not kill the rest | `supervisorScope` | One failed child cancelling its siblings |
| A stream of values over time | `Flow` (cold) | Manual callback registration and its leaks |
| Current state, always has a value | `StateFlow` | A late subscriber with nothing to render |
| One-shot events no subscriber may miss | `Channel` | Navigation/toast events dropped during a configuration change (→ `references/flows.md`) |
| Mutual exclusion inside suspend code | `Mutex.withLock` | `synchronized` pins a thread while a coroutine holds the lock across a suspension |
| Bounded producer/consumer pipeline | `Channel(capacity)` | Unbounded buffering that becomes a memory leak |

## Equality, Copy, And Identity

- `==` calls `equals` (structural); `===` compares references. This is the opposite convention to Java — a Java-trained reviewer reads `==` as identity and approves a real bug.
- Floating point has two behaviours. With a static type of `Double`/`Float`, `==` is IEEE 754: `Double.NaN == Double.NaN` is false and `0.0 == -0.0` is true. Once the values go through a boxed or generic path (`listOf(Double.NaN).contains(Double.NaN)`, `sortedBy`, `distinct`), Kotlin switches to total order: `NaN` equals itself and `-0.0 < 0.0`. Same values, two answers, chosen by the static type.
- `hashCode` must follow `equals`: a hand-written `equals` with no `hashCode` produces objects that are equal to each other and omitted from `HashMap` retrieval.
- A `data class` holding an `Array` compares by reference, because `Array.equals` is identity. Use `List`, or write `equals`/`hashCode` with `contentEquals`/`contentHashCode`.
- Value classes (`@JvmInline value class`) are the underlying type at runtime *until* they are used as a generic argument, made nullable, or passed through an implemented interface — then they box (→ `references/performance.md`).

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| `x?.let { … } ?: fallback` | The Elvis also fires when the lambda returns null — the fallback runs even though `x` was non-null | `if (x != null) { … } else { … }`, or keep the lambda's result non-null |
| `runBlocking` to call a suspend function | Blocks the calling thread; on a UI or request thread it is a freeze, and inside a coroutine it can deadlock the dispatcher | Make the caller `suspend`, or use the scope that owns the work; `runBlocking` belongs in `main` and in tests |
| `GlobalScope.launch` for convenience | Nothing cancels it, and everything it captured lives until process death | A scope owned by the lifecycle of the work (→ `references/coroutines.md`) |
| Collecting a flow in `onCreate` or a bare scope | Collection keeps running while the screen is invisible and can touch a destroyed view | `repeatOnLifecycle(STARTED)` or `collectAsStateWithLifecycle` (→ `references/android.md`) |
| `@Entity data class` (JPA) | Generated `equals`/`hashCode` break against lazy proxies and against an id assigned at persist time | Regular class with id-based `equals` (→ `references/server.md`) |
| Reflection-based JSON into non-null properties | The instance is built without calling the constructor, so defaults are skipped and non-null fields hold null | kotlinx.serialization, or Moshi with codegen (→ `references/serialization.md`) |
| `it` in nested lambdas | The inner `it` shadows the outer one; it compiles and does the wrong thing | Name the parameter the moment lambdas nest |
| `companion object` for constants | Every `val` becomes a getter call, and Java callers must go through `Companion` | `const val` for primitives and strings, top-level or in the companion |
| Mutable `var` in a class used as a `Map` key | `hashCode` changes after insertion and the entry becomes unreachable | `val` properties for anything used as a key or put in a `Set` |
| Custom getter or `open var` used after a null check | Smart cast is refused because the value can change between reads; the reflex fix is `!!` | Assign to a local `val` and smart-cast that |
| `try/catch` wrapped around `flow.collect` | Breaks exception transparency and hides which stage failed | The `catch` operator upstream of `collect` (→ `references/errors.md`) |

## Output Gates

Before emitting Kotlin code or a review verdict, verify:

- No `!!` that rule 2's decision order could have replaced?
- Every coroutine started in a scope something cancels, and every long CPU loop cooperating with cancellation?
- No `catch (Exception)` or `runCatching` around suspend code without re-throwing `CancellationException`?
- Every blocking call inside `withContext` on a dispatcher sized for the resource, and keep off `Main`?
- Every `when` over a sealed type used as an expression, with no `else` covering future subclasses?
- Library module: explicit visibility and return types if `explicit_api` is on, plus `@Jvm*` annotations wherever Java calls in?
- State published as a new immutable value, not a mutated collection re-emitted through the same reference?

## Where Experts Disagree

- **Typed failures vs exceptions.** Return a typed failure for expected outcomes (validation, not-found, offline); throw for broken invariants and unrecoverable I/O. The test that settles most arguments: if every caller writes `try/catch` around it, it was a standard value rather than exceptional. The contested part is `kotlin.Result` as a public return type — it boxes, it cannot be matched exhaustively, and it hides which failures exist, while a sealed hierarchy enumerates them (→ `references/errors.md`).
- **One-shot events: `Channel` vs state.** A `Channel` delivers exactly once to one consumer and survives a gap between subscribers; modelling the event as a field of the UI state with an explicit "consumed" acknowledgement survives process death but costs a round trip. Both are defensible. `SharedFlow(replay = 0)` is the option that quietly drops events while nobody is collecting.
- **Mocks vs fakes.** Kotlin classes are final by default, so mocking frameworks need bytecode tricks that make brittle tests brittler; a hand-written fake implementing the interface survives refactors. Mocks earn their keep for verifying interactions with something you do not own (→ `references/testing.md`).
- **Scope-function density.** One camp reads `apply`/`also`/`run` chains as idiomatic Kotlin, the other as write-only code. The neutral line: a scope function that removes a temporary variable is a win; nesting beyond one level is a named function waiting to be extracted.

---
name: java
description: Write, debug, and tune Java and the JVM. Trigger this skill to resolve
  exceptions (NullPointerException, ClassCastException, OutOfMemoryError, etc.), thread
  deadlocks, memory leaks, high CPU usage, build and packaging issues (Maven/Gradle),
  date/text rendering bugs, database connection exhaustion, or Spring @Transactional
  failures. It also provides expertise for JDK version upgrades (8 to 17/21+), memory
  sizing in containers, and library configuration. Not for Kotlin, JavaScript, or
  Android app development.
metadata:
  openclaw: '{"requires": {"config": ["<state_root>/Clawic/data/java/", "<state_root>/Clawic/profile.yaml",
    "<state_root>/java/", "<state_root>/clawic/java/"]}, "emoji": "☕", "configPaths":
    ["<state_root>/Clawic/data/java/", "<state_root>/Clawic/profile.yaml", "<state_root>/java/",
    "<state_root>/clawic/java/"]}'
---
User preferences and memory live in `<state_root>/Clawic/data/java/` (see `references/setup.md` on first use, `references/memory-template.md` for the file format). If you have data at an old location (`<state_root>/java/` or `<state_root>/clawic/java/`), move it to `<state_root>/Clawic/data/java/`, and say in one line that you moved it and from where.

## Routing
Load the specific reference files when handling corresponding tasks:

- **Classes, Collections, Nulls:** Load `references/classes.md`, `references/collections.md`, `references/nulls.md`.
- **Concurrency & Threads:** Load `references/concurrency.md`, `references/async.md`.
- **Debugging, Logging, Memory:** Load `references/debug.md`, `references/logging.md`, `references/memory.md`, `references/jvm.md`.
- **Errors & Exceptions:** Load `references/exceptions.md`.
- **Build & Migration:** Load `references/build.md`, `references/migration.md`.
- **Text, DateTime, I/O:** Load `references/text.md`, `references/datetime.md`, `references/io.md`.
- **Testing:** Load `references/testing.md`.
- **Web & Databases:** Load `references/http.md`, `references/jdbc.md`, `references/spring.md`.
- **Serialization & Security:** Load `references/serialization.md`, `references/security.md`.

## Quick Reference

| Situation | Go to |
|---|---|
| An exception or error whose name you must decode; hang, deadlock, 100% CPU, works-in-IDE-only | `references/debug.md` |
| OutOfMemoryError, heap grows over days, heap dump analysis, container OOM-kill | `references/memory.md` |
| Choosing a GC, setting `-Xmx` in a container, slow startup, JVM flags, `-Xlog` | `references/jvm.md` |
| Slow code and no idea where; JMH benchmark, JFR recording, allocation pressure | `references/performance.md` |
| Shared mutable state, locks, `volatile`, atomics, deadlock design, virtual threads | `references/concurrency.md` |
| CompletableFuture chains, executors, timeouts, cancellation, structured concurrency | `references/async.md` |
| Which collection, the `equals`/`hashCode` contract, iteration traps, comparators, maps | `references/collections.md` |
| Stream pipeline wrong or slow, collectors, `groupingBy`, parallel streams | `references/streams.md` |
| Lambdas and method references, designing a `@FunctionalInterface`, capture rules, a checked exception inside a lambda | `references/lambdas.md` |
| Designing against null, `Optional`, autoboxing, nullability annotations | `references/nulls.md` |
| Type erasure, wildcards, `List<Dog>` vs `List<Animal>`, unchecked warnings | `references/generics.md` |
| Class design: records, sealed types, pattern matching, immutability, inheritance | `references/classes.md` |
| Custom annotations, runtime metadata, `setAccessible`, `MethodHandle`/`VarHandle`, dynamic proxies, annotation processors | `references/reflection.md` |
| Checked vs unchecked, try-with-resources, retries, interrupts, logging failures | `references/exceptions.md` |
| Strings, `StringBuilder`, regex, `String.format`, charsets, locale-sensitive output | `references/text.md` |
| Dates, time zones, DST, `Instant` vs `LocalDateTime`, formatting patterns | `references/datetime.md` |
| Files, `Path`, classpath resources, temp files, streams that leak handles | `references/io.md` |
| Jackson/JSON mapping, records in JSON, Java serialization and its CVEs | `references/serialization.md` |
| Calling another service: HTTP client choice, timeouts, DNS caching, TLS handshake errors | `references/http.md` |
| JDBC connections, pool exhaustion, batching, fetch size, driver and transaction behavior | `references/jdbc.md` |
| SLF4J bindings, duplicate or missing log output, MDC, log levels, structured logs | `references/logging.md` |
| Maven/Gradle version conflicts, scopes, fat jars, multi-module, reproducible builds | `references/build.md` |
| Upgrading a JDK, javax → jakarta, removed APIs, `--add-opens`, illegal reflective access | `references/migration.md` |
| Deserialization gadgets, XXE, path traversal, SQL injection, TLS, secrets, crypto choices | `references/security.md` |
| JUnit 5, Mockito, AssertJ, Testcontainers, flaky tests, tests that stalled | `references/testing.md` |
| Spring Boot: `@Transactional`, proxies, JPA lazy loading, N+1, bean wiring, config precedence | `references/spring.md` |
| Anything else | Exception Triage and Core Rules below; then reproduce it in a single `main` with no framework |

## Core Rules

1. **`.equals()` for content; `==` only for primitives, enums, and deliberate identity.** `Integer a = 128, b = 128; a == b` is **false**, while at 127 it is true — the autobox cache is −128..127 (`-XX:AutoBoxCacheMax` moves only the upper bound). Use `Objects.equals(a, b)` whenever either side can be null.
2. **`equals` and `hashCode` ship together, over fields that remain constant.** Contract: equal objects must return the same hash; unequal objects may collide. Failure mode: `set.add(o)`, then mutate a field used in `hashCode()` → `set.contains(o)` is false and the entry is unreachable forever. Hash only final fields (→ `references/collections.md`).
3. **Restore the interrupt flag upon catching `InterruptedException`.** `catch (InterruptedException e) { Thread.currentThread().interrupt(); return; }` — the flag is the only channel that tells the pool to stop; swallowing it makes every `shutdownNow()` wait out the full timeout and every cancellation silently fail.
4. **Every `AutoCloseable` in try-with-resources** — including `Files.lines`, `Files.walk`, JDBC `Connection`/`Statement`/`ResultSet`, and `Scanner`. Resources close in reverse order, and a failure inside `close()` arrives as `e.getSuppressed()` instead of masking the real exception. Leaked handles surface hours later as "Too many open files" (→ `references/io.md`).
5. **Size the container, not just the heap.** `RSS ≈ Xmx + metaspace + code cache + (threads × Xss) + direct buffers + GC structures`. Worked: `-Xmx512m` + ~100 MB metaspace + ~100 MB code cache + 200 threads × 1 MB stack + 64 MB direct ≈ 976 MB — a 1 GiB limit gets OOM-killed at peak with the heap only half full. In containers set `-XX:MaxRAMPercentage=75` (the JVM's own default is 25%) and leave the remainder for the non-heap terms (→ `references/jvm.md`).
6. **`Optional` is a return type.** `orElse(buildDefault())` evaluates its argument on every call even when a value is present; `orElseGet(() -> buildDefault())` does not. Restrict its usage strictly to method returns, as placing it in fields or collections creates ambiguous empty states and breaks serialization (→ `references/nulls.md`).
7. **Pin dependency versions in exactly one place.** Maven picks the **nearest** declaration in the tree (ties: first declared, not the highest); Gradle picks the **highest** version it sees. The same dependency graph therefore yields different jars in the two tools. Declare in `<dependencyManagement>` or a Gradle `platform`, and verify the winner with `mvn dependency:tree -Dverbose` (→ `references/build.md`).
8. **Compile with `--release N` exclusively.** `-source 8 -target 8` on a JDK 17 compiles happily against JDK 17 APIs and then dies at runtime on Java 8 with `NoSuchMethodError`; `--release 8` also restricts the visible API set. Class-file major version = **JDK + 44** (52 = Java 8, 55 = 11, 61 = 17, 65 = 21).
9. **Streams to transform, loops to mutate.** Go parallel only when all three hold: per-element work is real, the source splits evenly (arrays, `ArrayList`, `IntStream.range` — not `LinkedList`, `Files.lines`, `Stream.iterate`), and nothing shared is mutated. Parallel streams run on `ForkJoinPool.commonPool`, whose parallelism is `availableProcessors() − 1` — in a 1-CPU container that is 0 extra threads, so "parallel" runs entirely on the calling thread (→ `references/streams.md`).

## Exception Triage

Read the FIRST exception in the log, not the last: the later ones are usually consequences. The `getCause()` chain matters more than the top frame.

| Symptom | What it really means | First move |
|---|---|---|
| `NullPointerException` with a helpful message ("Cannot invoke ... because `x.y` is null") | Helpful NPE messages, on by default since JDK 15 | Read the message — it names the exact expression that was null |
| `NullPointerException` with **no stack trace** | The JIT recompiled a hot throw site to reuse a preallocated exception | Restart with `-XX:-OmitStackTraceInFastThrow` and reproduce |
| `NoClassDefFoundError` | The class existed at compile time but not at runtime — OR its static initializer threw earlier | Search upward in the log for the first `ExceptionInInitializerError`; that one carries the real cause |
| `ClassNotFoundException` | A by-name lookup (reflection, JDBC driver, SPI) failed | Check the runtime classpath, and whether shading dropped `META-INF/services` (`references/build.md`) |
| `NoSuchMethodError` / `NoSuchFieldError` | Version skew: compiled against one jar, running against another | `mvn dependency:tree -Dverbose -Dincludes=<artifact>` (`references/build.md`) |
| `UnsupportedClassVersionError: class file version 65.0` | Built for a newer JDK than the one running it; major − 44 = JDK (65 → 21) | Align `--release` with the runtime JDK (`references/migration.md`) |
| `ClassCastException` naming the SAME class on both sides | Two classloaders loaded it (fat jar plus a container-provided copy) | Remove the duplicate; mark the provided one `provided`/`compileOnly` |
| `ConcurrentModificationException` | Structural modification during iteration — single-threaded in most sightings, not a concurrency bug | `Iterator.remove()` or `removeIf` (`references/collections.md`) |
| `StackOverflowError` | Unbounded recursion, or two objects whose `toString`/`equals` call each other | Read the repeating frame cycle in the trace |
| `OutOfMemoryError` (any flavour) | Six distinct causes with different fixes | `references/memory.md` — the message text selects the chain |
| `IllegalStateException: stream has already been operated upon or closed` | A stream reused after its terminal operation | Rebuild the stream from its source (`references/streams.md`) |
| `IllegalMonitorStateException` | `wait`/`notify` called without holding that object's monitor | `references/concurrency.md` |
| Process hangs with no exception at all | Deadlock, a non-daemon thread that stalls indefinitely, or a blocked unbounded queue | Three thread dumps 10s apart (`references/debug.md`) |

## Version Floors

Check before suggesting an API: it compiles on your JDK and fails on theirs.

| Feature | Minimum JDK | Note |
|---|---|---|
| `var` for locals | 10 | Lambda parameters: 11 |
| `HttpClient`, single-file source launch | 11 | Last LTS where `javax.*` was still the norm |
| Text blocks (`"""`) | 15 | Incidental trailing whitespace is stripped |
| Helpful NullPointerException messages | 15 | On by default from 15; before that, opt-in |
| `instanceof` pattern, records, `Stream.toList()` | 16 | `toList()` is unmodifiable and null-tolerant; `Collectors.toUnmodifiableList()` rejects nulls |
| Sealed classes and interfaces | 17 | First LTS enforcing strong encapsulation of JDK internals |
| UTF-8 as the default charset | 18 | JEP 400 — before this the default was platform-dependent |
| Virtual threads, pattern matching for `switch`, record patterns, sequenced collections | 21 | `SequencedCollection.getFirst()`, `reversed()` |
| `synchronized` no longer pins a virtual thread's carrier | 24 | On 21-23, use `ReentrantLock` inside virtual threads (`references/concurrency.md`) |
| Structured concurrency (`StructuredTaskScope`) | preview | Still a preview API through JDK 25 — requires `--enable-preview`, and its shape changed between previews |

## Output Gates

Before emitting Java code or a build change, verify:

- Every `AutoCloseable` is inside try-with-resources?
- `equals` and `hashCode` overridden together, computed from final fields only?
- Charset, `Locale`, and time zone explicit wherever text, numbers, or time cross a boundary?
- No raw types, and every `@SuppressWarnings("unchecked")` justified in a comment?
- Every caught `InterruptedException` restores the flag or rethrows?
- Every API used is at or below the configured `jdk_version` (→ Version Floors)?
- New dependency versions declared in one place, not inline per module?
- No SQL, shell command, or file path built by concatenating input (`references/security.md`)?

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/Clawic/data/java/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| jdk_version | number (JDK major, 8-25) | from `maven.compiler.release`, `<java.version>`, or the Gradle toolchain if present, else 21 | Gates every API and syntax suggestion against Version Floors; selects flag syntax in `references/jvm.md` and the target in `references/migration.md` |
| build_tool | maven \| gradle \| other | detected (`pom.xml` → maven, `build.gradle*` → gradle), else maven | Selects the resolution rules, commands, and packaging advice in `references/build.md`, which covers Maven and Gradle only; `other` (Bazel, Ant, plain `javac`) suppresses tool-specific commands and keeps the advice at classpath and jar level |
| framework | spring-boot \| other \| none | detected from dependencies, else none | `spring-boot` enables `references/spring.md` routing for proxies, `@Transactional`, and JPA; `other` (Quarkus, Micronaut, Jakarta EE) keeps guidance at JDK and specification level and states that container-specific DI and transaction semantics are not covered here; `none` assumes plain Java |
| locale | text (BCP 47 tag, e.g. `es-ES`) | none — `Locale.ROOT` for machine-facing output, the caller's locale for display; `<state_root>/Clawic/profile.yaml` is the fallback | Fills the explicit `Locale` argument in formatting, collation, and case-mapping guidance (`references/text.md`) and picks the locale used in worked examples |
| timezone | text (IANA zone id, e.g. `Europe/Madrid`) | none — every example takes an explicit `ZoneId`, require an explicit `ZoneId` for every example; `<state_root>/Clawic/profile.yaml` is the fallback | The zone assumed when a wall-clock time arrives without one, and the zone shown in `references/datetime.md` examples |
| default_charset | text (charset name) | utf-8 | The charset written into every explicit `Charset` argument in `references/text.md` and `references/io.md`; any value other than utf-8 also turns on the legacy-encoding warnings around `file.encoding` and the JDK 18 default change |
| lombok | bool | false | false writes explicit constructors, getters, and `equals`; true writes Lombok annotations and skips the boilerplate sections of `references/classes.md` |
| nullability_style | jspecify \| jakarta \| jetbrains \| none | none | Which `@Nullable`/`@NonNull` annotations appear in generated signatures (`references/nulls.md`) |
| preview_features | bool | false | When true, `--enable-preview` APIs (structured concurrency) become admissible suggestions |
| test_stack | junit5 \| junit4 \| testng | junit5 | Selects assertion and lifecycle idioms in `references/testing.md`; junit4 turns on the vintage-engine warnings |

Preference areas to record as the user reveals them:

- **tooling** — IDE, formatter (google-java-format, palantir, spotless), static analysis (ErrorProne, SpotBugs, NullAway)
- **conventions** — package layout, immutability default, builder vs constructor, logging facade and message style, checked-exception policy
- **platform** — container vs bare metal, target CPU architecture, GC choice, cloud provider, application server, and the deployment's locale, time zone, and charset when they differ from the `locale`/`timezone`/`default_charset` variables
- **output** — depth of explanation (one-line fix vs full diagnosis), whether the reasoning precedes or follows the patch, diff vs whole file, comment density in generated code
- **work order** — propose-then-apply vs editing directly, review gate before touching build files or dependency versions, whether to compile and run the tests before handing back, coverage gate
- **cadence** — how often to rebuild for CVEs with no code change (`references/build.md`), the JDK upgrade window (`references/migration.md`), and whether to raise upgrades between windows
- **safety posture** — how proactively to flag legacy APIs (Java serialization, `SimpleDateFormat`, raw types) and to propose dependency or JDK upgrades, vs only on request
- **restrictions** — banned APIs or libraries, no-preview-features rule, compliance regime (FIPS crypto, no reflection, offline builds)

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| `log.error(e.getMessage())` | Drops the stack trace, and the message is `null` for NPEs and many wrapped exceptions | `log.error("context", e)` — the throwable is a separate argument |
| `new String(bytes)`, `getBytes()`, `FileReader`, `PrintWriter(file)` | Platform default charset; UTF-8 only became the default in JDK 18, so the same code writes different bytes on an older JVM or on Windows | Pass `StandardCharsets.UTF_8` explicitly every time |
| `list.remove(someInt)` on a `List<Integer>` | The `remove(int)` overload wins over `remove(Object)` — it removes by INDEX and can throw `IndexOutOfBoundsException` | `list.remove(Integer.valueOf(x))` |
| `SimpleDateFormat` in a static or shared field | Not thread-safe; under load it returns silently wrong dates rather than throwing | `DateTimeFormatter` — immutable and thread-safe (`references/datetime.md`) |
| `Collectors.toMap(k, v)` on data where a key can repeat | Throws `IllegalStateException` only for inputs that collide, so it passes tests and fails in production | Supply a merge function: `toMap(k, v, (a, b) -> b)` |
| `@Transactional` called from another method of the same class | Self-invocation bypasses the proxy: no transaction, no warning, no rollback | Move the annotated method into another bean (`references/spring.md`) |
| JUnit 4 annotations left in a JUnit 5 project | `org.junit.Test` classes are simply not executed by the Jupiter engine — a green build running zero tests | One engine, or add the vintage engine deliberately (`references/testing.md`) |
| `Files.lines()` / `Files.walk()` outside try-with-resources | Holds the file handle until GC; the failure shows up hours later as "Too many open files" | try-with-resources (Core Rule 4) |
| `printStackTrace()` in server code | Writes to stderr, detached from the request context and invisible to log aggregation | Logger with the throwable |
| `catch (Exception e) {}` around a retry loop | Also catches `InterruptedException` and programming errors, turning an outage into silence | Catch the specific exception; rethrow `Error` and restore interrupts (`references/exceptions.md`) |
| An HTTP or JDBC call with no read timeout | The default in most Java clients is unlimited: one slow dependency parks every worker thread and the whole service stops answering | Set connect AND read timeouts on every client (`references/http.md`, `references/jdbc.md`) |
| Double-checked locking without `volatile` | The reference can be published before the constructor finishes — another thread sees a half-built object | Holder-class idiom, or `volatile` on the field (`references/concurrency.md`) |
| Turning on `spring.jpa.open-in-view` to silence `LazyInitializationException` | Holds a DB connection for the whole request, converting a query bug into pool exhaustion under load | Fetch what the view needs in the query (`references/spring.md`) |

## Where Experts Disagree

- **Checked exceptions.** Bloch defends them for conditions a caller can actually recover from; most modern frameworks wrap everything unchecked. Working boundary: checked only when the caller has a real alternative path — and keep them strictly outside lambdas or streams where they fail to compose.
- **`Optional` beyond return types.** Its designers scoped it to library return values; a school uses it for fields and parameters anyway. Boundary: return types yes; entity fields, DTOs, and hot loops no (extra allocation, not serializable, two empty states to test).
- **Lombok.** Removes real boilerplate vs it is an annotation processor that breaks on JDK upgrades and hides behavior from readers and tools. Since records (16) cover immutable carriers, its honest remaining use is `@Slf4j` and `@Builder` on mutable entities.
- **Mocks vs real dependencies in tests.** Mock what you own and what is slow or non-deterministic; run repositories and SQL against a real engine (Testcontainers). A mocked JDBC layer verifies the mock, not the query.
- **Virtual threads vs reactive.** Since 21, virtual threads deliver most of the throughput of reactive code with straight-line control flow and readable stack traces. Reactive still wins where you genuinely need backpressure across a streaming pipeline — that need, not fashion, is the criterion.

## Related Skills
- `kotlin` — the other JVM language; same bytecode, different null and concurrency model
- `android` — Android SDK, lifecycle, and app packaging
- `sql` — the queries your JDBC and JPA code actually sends
- `docker` — containerizing a JVM and matching memory limits to heap

## Feedback

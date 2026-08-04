---
name: flutter
description: 'Builds, debugs, and ships Flutter apps. Use when writing Dart widgets or screens, decoding framework exceptions (overflow, unbounded constraints, setState during build, deactivated ancestor), fixing jank or memory issues, routing with Navigator or go_router, handling platform channels, localizing strings, or shipping release builds. Not for React Native or native-only Swift/Kotlin work.'
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"🐦"}'
  related-skills: '{"animate":"Cross-framework motion systems and reduced-motion policy.","app-store":"Store listing, metadata, and review process for builds produced in release.md.","in-app-purchases":"Subscriptions and paywalls on top of a Flutter app.","kotlin":"Native-only Android work outside Flutter scope.","react-native":"The other cross-platform stack; when comparing or migrating.","swift":"Native-only iOS/macOS work outside Flutter scope.","testflight":"Distributing the iOS build produced in release.md."}'
---

## State location

Flutter skill state may exist in `<workspace>/flutter/`, `<workspace>/memory/flutter/`, or `~/flutter/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/flutter/`, `<workspace>/memory/flutter/`, `~/flutter/`.
3. If none exists and state must be created, default to `<workspace>/flutter/`.

Use the selected `<state_root>` for every state operation in this skill.

## Quick Reference

| Situation | Play |
|---|---|
| "A RenderFlex overflowed by N pixels" | A child asked for more than the parent allows — `Expanded`/`Flexible` for a flex child, or make the axis scrollable → `references/layout.md` |
| "Vertical viewport was given unbounded height" | A scrollable inside a `Column` or another scrollable — `Expanded`, a fixed height, or slivers; `shrinkWrap: true` is the slow escape → `references/layout.md` |
| "RenderBox was not laid out" | Almost always a knock-on: scroll UP to the FIRST exception in the console and fix that one → `references/debug.md` |
| "setState() or markNeedsBuild() called during build" | A notifier fired, or navigation/snackbar ran, inside `build` — move it to a callback or a post-frame callback → `references/debug.md` |
| "setState() called after dispose()" | An `await` outlived the widget — `if (!mounted) return;` after every await (rule 2) → `references/async.md` |
| "Looking up a deactivated widget's ancestor" | A captured `BuildContext` used after its widget left the tree — capture the `NavigatorState` or `ScaffoldMessengerState` BEFORE the await → `references/async.md` |
| "Incorrect use of ParentDataWidget" | `Expanded`/`Flexible`/`Positioned` is not a direct child of `Row`/`Column`/`Flex`/`Stack` → `references/layout.md` |
| List items keep the wrong state after reorder or delete | Missing or unstable keys — `ValueKey(item.id)`, never `UniqueKey()` in a builder (rule 4) → `references/state.md` |
| A widget rebuilds far more than it should | Climb the Rebuild Scope Ladder below, then confirm in DevTools' rebuild counter → `references/performance.md` |
| Scrolling stutters, frames dropped | Profile mode on a real device first, then image decode size, `saveLayer`, and per-item work → `references/performance.md` |
| Memory climbs while scrolling images | Decoded bytes = width × height × 4, independent of file size — set `cacheWidth`/`cacheHeight` → `references/performance.md` |
| Choosing or migrating a state management library | Match the repo (`state_management: auto`); greenfield defaults and migration cost → `references/architecture.md` |
| Route needs an argument, a result, or a deep link | Typed routes and result handling with Navigator or go_router → `references/navigation.md` |
| Keyboard covers the field, focus jumps, validation fires too early | Controller lifetime, `AutovalidateMode.onUserInteraction`, scroll-on-focus → `references/forms.md` |
| Parsing, caching, or persisting data | Isolate for large payloads, local DB as the source of truth for offline → `references/data.md` |
| An animation stutters, leaks, or never restarts | Controller lifetime, `child:` hoisting, implicit vs explicit choice → `references/animations.md` |
| `MissingPluginException` right after adding a plugin | Hot restart does not register plugins — full restart required → `references/platform.md` |
| Right on the phone, broken on tablet, web, or desktop | Window size classes, `LayoutBuilder` vs `MediaQuery`, platform-adaptive widgets → `references/adaptive.md` |
| Text overflows once the user enlarges the system font | Text scaling is a layout input, not a cosmetic setting → `references/accessibility.md` |
| A chart, gauge, signature pad, or anything no widget can express | `CustomPaint`, and the `shouldRepaint` contract that keeps it cheap → `references/custom-painting.md` |
| Translated text overflows, dates look wrong, or the layout must mirror for Arabic | ARB workflow, ICU plurals, and the directional widgets → `references/localization.md` |
| A test hangs, or passes locally and fails in CI | `pumpAndSettle` against an endless animation; goldens are platform-specific → `references/testing.md` |
| Works in debug, broken in the release build | AOT, tree-shaken icons, stripped asserts, obfuscation, undeclared assets → `references/release.md` |
| `pub get` cannot resolve, or a plugin breaks after an upgrade | Version solving, overrides, transitive plugin constraints → `references/dependencies.md` |
| A Dart language question (records, patterns, `late`, `==`) | → `references/dart.md` |
| Anything else | Read the FIRST exception in full including "The relevant error-causing widget", reproduce it in a widget test, then open the file the message names → `references/debug.md` |

## Reference Routing

Load the matching reference only when the task requires it:

| Load when... | Reference |
|---|---|
| Layout exception, flex, overflow, or slivers | `references/layout.md` |
| Lifecycle, keys, or state preservation question | `references/state.md` |
| State management choice, DI, folder structure | `references/architecture.md` |
| Widget composition, `BuildContext`, `build` discipline | `references/widgets.md` |
| Futures, streams, isolates, cancellation | `references/async.md` |
| Routing, deep links, back-button handling | `references/navigation.md` |
| Text input, focus, validation, keyboard | `references/forms.md` |
| JSON, HTTP, persistence, offline-first | `references/data.md` |
| Jank triage, rebuilds, image memory, Impeller | `references/performance.md` |
| Animation lifecycle, implicit vs explicit, transitions | `references/animations.md` |
| CustomPainter, canvas, custom RenderObjects | `references/custom-painting.md` |
| Platform channels, FFI, plugins, permissions, SPM, HCPP | `references/platform.md` |
| Responsive/adaptive layout, phone/tablet/web/desktop | `references/adaptive.md` |
| Semantics, text scaling, tap targets | `references/accessibility.md` |
| Translations, plurals, RTL, date/number formats | `references/localization.md` |
| Widget tests, golden tests, integration tests | `references/testing.md` |
| Build modes, flavors, signing, obfuscation, store artifacts | `references/release.md` |
| Symptom-to-cause debugging, exception decoder | `references/debug.md` |
| pub resolution, version solving, codegen | `references/dependencies.md` |
| Dart language features (records, patterns, null safety, Dart 3.12) | `references/dart.md` |
| CLI commands, `flutter clean`, native-side troubleshooting | `references/commands.md` |

## Core Rules

1. **Constraints go down, sizes go up, parent sets position.** Every layout exception decodes from this one sentence. A widget's size is determined by its parent's constraints; given unbounded constraints, a child that wants "as much as possible" has nothing to resolve and throws.
2. **`mounted` is the gate on every async gap.** After each `await`, before touching `setState`, `context`, or any controller: `if (!mounted) return;`. The `use_build_context_synchronously` lint catches the context case only — controllers, tickers, and `ScaffoldMessenger` calls need the same guard and nothing warns you.
3. **Every disposable gets a matching line in `dispose`, in reverse creation order.** Controllers (`TextEditingController`, `ScrollController`, `AnimationController`, `PageController`, `TabController`), `FocusNode`s, `StreamSubscription`s, `Timer`s, `ValueNotifier`s. The leak is invisible in debug and surfaces as a climbing memory graph plus callbacks firing on dead widgets. Cheap check: a widget test that pumps the widget, pumps an empty tree, and asserts no exception (`references/testing.md`).
4. **Keys decide identity; without a key, position does.** Flutter matches a new widget to an existing `Element` by `runtimeType` + `key` at the same position, so inserting, removing, or reordering stateful children without keys hands state to the wrong item. Use `ValueKey(item.id)` for stable identity. `UniqueKey()` inside a builder creates a fresh key every build, destroying and recreating the subtree — including its scroll offset and running animations — on every frame.
5. **`const` is the rebuild firewall.** Identical `const` widget expressions are canonicalized to a single instance, so `Element.update` sees `identical(oldWidget, newWidget)` and skips that subtree entirely. This is why extracting a static subtree into a `const` widget beats trying to "scope" a `setState` that still sits above it. A widget cannot be `const` if anything inside it reads `context` or a runtime value — that, not style, is the real constraint.
6. **Frame budget = 1000 / refresh rate ms — 16.7 ms at 60 Hz, 8.3 ms at 120 Hz — shared by the UI thread (build, layout, paint) and the raster thread (GPU).** Any single synchronous unit of work that can exceed it (decoding a large JSON payload, image processing, crypto, sorting tens of thousands of items) belongs in an isolate (`references/async.md`). Wrapping it in a `Future` changes nothing: the work still runs on the same isolate and still blocks the frame.
7. **Only profile mode produces real numbers.** Debug builds run the JIT with assertions, service extensions, and widget-inspector instrumentation; frame timings there are noise. `flutter run --profile` on a physical device — simulators and emulators have GPU behavior the shipped app never sees.
8. **Side effects go in callbacks or post-frame hooks, not in `build`.** Navigation, snackbars, dialogs, notifier writes, network calls: each marks something dirty while the tree is building, which is exactly the "setState() or markNeedsBuild() called during build" exception. Put them in an event callback, a listener (`ref.listen`, `BlocListener`, `addListener`), or `WidgetsBinding.instance.addPostFrameCallback` when no other hook exists.
9. **A feature is not done until its release artifact runs.** AOT compilation, icon tree-shaking, stripped `assert`s, obfuscation, and asset declarations change behavior only in release. Build and launch the `--release` artifact on a device before calling it finished (`references/release.md`).

## Layout Error Decoder

Flutter's layout exceptions name the mechanism, not the mistake. The first move below is right in most cases; `references/layout.md` carries the reasoning.

| Message | What it actually means | First move |
|---|---|---|
| `A RenderFlex overflowed by N pixels` | A flex child's chosen size exceeds the space left after its fixed siblings | `Expanded`/`Flexible` on the growing child, or make the axis scrollable |
| `Vertical viewport was given unbounded height` | A scrollable sits inside another scrollable or a `Column`'s main axis | `Expanded`, a fixed height, or convert the parent to `CustomScrollView` + slivers |
| `BoxConstraints forces an infinite width/height` | An unbounded constraint reached a widget that expands (`double.infinity` under a `Row`, `Expanded` inside a scroll axis) | Bound it at the nearest parent that knows the real size |
| `RenderBox was not laid out` | A previous layout exception aborted the pass | Fix the FIRST exception in the console; this one disappears with it |
| `Incorrect use of ParentDataWidget` | `Expanded`/`Flexible` outside a `Flex`, or `Positioned` outside a `Stack` | Make it a DIRECT child of the right parent — a `Padding` in between breaks it |
| `Cannot hit test a render box with no size` | The box was laid out with zero constraints, usually inside a zero-size parent | Give the parent a real size; check for an empty `Container` wrapper |
| `Failed assertion: 'constraints.hasBoundedHeight'` under `IntrinsicHeight` | Intrinsic sizing under unbounded constraints | Remove the intrinsic widget; intrinsics can cost O(N²) over the subtree |
| `No Material widget found` / `No Directionality widget found` | The widget is outside the app's `MaterialApp` scope | Wrap in `Material`/`MaterialApp` — in tests this is the usual cause (`references/testing.md`) |
| `Scaffold.of() called with a context that does not contain a Scaffold` | The context is the one that CREATED the Scaffold, not one below it | A `Builder`, a child widget, or `ScaffoldMessenger.of(context)` for snackbars |
| Anything else | The console block above the stack names the offending widget and the constraints it received | Read `The relevant error-causing widget was:` and open that line |

## Rebuild Scope Ladder

Ordered cheapest to costliest. Take the first rung that removes the rebuild, and confirm it in DevTools' rebuild counter rather than by feel (`references/performance.md`).

1. **`const` the parts that never change.** Free at runtime, and it stops the rebuild at that boundary (rule 5).
2. **Hoist the unchanging subtree into the `child:` slot.** `AnimatedBuilder`, `ValueListenableBuilder`, and `Consumer` all take a `child` that is built once and handed back on every rebuild — the highest-yield single edit in animation and list code.
3. **Extract the changing part into its own widget.** `setState` rebuilds the whole `State`'s subtree; a smaller widget is a smaller subtree. This is the fix for "setState rebuilds my entire screen".
4. **Listen to one value, not one object.** `ValueListenableBuilder`, `Selector`, `context.select`, `ref.watch(provider.select(...))` — rebuild on the field you render, not on every notification.
5. **Move state DOWN, not up.** State lifted higher than its only consumer forces every sibling to rebuild. Lift only to the lowest common ancestor of the widgets that actually read it.
6. **Isolate repaints with `RepaintBoundary`.** Only after build cost is gone: it addresses painting, not building, and each boundary is a separate GPU layer with its own memory cost.
7. **Restructure with slivers or a different scroll widget.** When per-item work is genuinely unavoidable, stop rebuilding the items that are off-screen (`references/layout.md`).

## Widget Choice

Pick the least capable widget that expresses the need — each row costs something the row above does not.

| Need | Use | Cost or trap |
|---|---|---|
| Fixed size, or space between widgets | `SizedBox` | `const`-friendly; a `Container` with only a size drags in the whole decoration pipeline |
| Padding | `Padding` | `Container(padding:)` is the same thing wrapped in more objects |
| Any list longer than one screen | `ListView.builder` / `.separated` | `ListView(children: [...])` builds and retains every item, on-screen or not |
| List with uniform row height | `ListView.builder` + `itemExtent` | Lets the viewport skip measuring items; required for instant jumps in long lists |
| Headers, grids, and lists in one scroll view | `CustomScrollView` + slivers | Nesting scrollables inside a `Column` is the wrong shape (`references/layout.md`) |
| Rebuild on one value | `ValueListenableBuilder` | No package needed; `setState` rebuilds the whole `State` |
| A future rendered once | `FutureBuilder` with the future held in a FIELD | Creating the future inside `build` re-runs it on every rebuild (`references/async.md`) |
| A continuously changing value | `StreamBuilder` over a cached stream | Re-listening to a single-subscription stream throws `Bad state: Stream has already been listened to` |
| Show/hide without losing state | `Offstage`, or `Visibility(maintainState: true)` | A conditional `if` in the child list DISPOSES the subtree — often the actual bug |
| Fade, size, or color change on a state change | `AnimatedContainer`, `AnimatedOpacity`, `AnimatedSwitcher` | Implicit animations need a CHANGED value and, for `AnimatedSwitcher`, differing keys (`references/animations.md`) |
| One animation driving several widgets | `AnimationController` + explicit transitions | Owns a ticker: `TickerProviderStateMixin` plus a `dispose` line (rule 3) |
| Read theme, media, or an inherited value | `Theme.of`, `MediaQuery.sizeOf`, `context.watch` | Creates a dependency: the widget rebuilds whenever that value changes |
| Reach into a child's state | A callback or a shared notifier passed down | `GlobalKey` works, but forces a global registry and blocks subtree reuse (`references/widgets.md`) |
| Anything else | Compose from existing widgets before writing a `RenderObject` | A custom `RenderObject` is right for genuinely custom layout and a maintenance tax everywhere else |

## Output Gates

Before emitting Flutter code, verify:

- Every `await` inside a `State` is followed by a `mounted` check before `setState`, `context`, or a controller is touched
- Every controller, `FocusNode`, subscription, and timer created has a matching line in `dispose`
- Every list of stateful children carries a stable `ValueKey`
- All side effects (future creation, network calls, navigation, snackbars, notifier writes) go in callbacks or post-frame hooks
- Static subtrees are `const`; `AnimatedBuilder`/`ValueListenableBuilder` pass their unchanging subtree through `child:`
- Long lists use `.builder`; images from network or disk set `cacheWidth`/`cacheHeight`
- Text that can grow (labels, buttons, chips) survives a large text scale without overflowing (`references/accessibility.md`)
- Interactive targets meet the platform minimum, and icon-only controls carry a semantic label
- `flutter analyze` is clean — not merely "it compiles"

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`. You record preferences the moment they are stated, maintaining continuous workflow without interruption.

| Variable | Type | Default | Effect |
|---|---|---|---|
| state_management | auto \| setstate \| provider \| riverpod \| bloc | auto | `auto` reads `pubspec.yaml` and matches the repo; the resolved value selects the idioms in `references/architecture.md` and the listener form used in Core Rule 8 examples |
| router | auto \| navigator \| go_router | auto | `auto` reads `pubspec.yaml`; drives every routing example, deep-link setup, and back-button pattern in `references/navigation.md` |
| target_platforms | list (android, ios, web, macos, windows, linux) | android, ios | Which platform sections surface in `references/platform.md`, `references/adaptive.md`, and `references/release.md`, and which store steps appear in the release checklist |
| target_fps | 60 \| 120 | 60 | Sets the frame budget used everywhere (1000 / target_fps ms, Core Rule 6) and therefore the jank threshold in `references/performance.md` and `references/debug.md` |
| project_layout | feature-first \| layer-first | feature-first | Where new files go, and how `references/architecture.md` names folders and boundaries |
| codegen | allowed \| avoid | allowed | `avoid` bans `build_runner` solutions (freezed, json_serializable, route generators) and emits hand-written equivalents in `references/data.md` and `references/architecture.md` |
| destructive_confirm | bool | true | Confirms before `flutter clean`, `--update-goldens`, and deleting `Podfile.lock`/`pubspec.lock` (`references/commands.md`) |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Tooling**: DI (`get_it` vs scoped providers), HTTP client (`http` vs `dio`), local storage (`drift`, `isar`, `sqflite`, `hive`), image caching package, lint set — affects every "add a package" recommendation in `references/data.md` and `references/dependencies.md`
- **Conventions**: widget file granularity, naming of state and notifier classes, private-widget vs builder-method style, `const`-everywhere policy — affects the shape of emitted code in `references/widgets.md`
- **Platform**: min SDK and deployment targets, flavor names, web hosting shape, desktop window behavior — affects `references/release.md` and `references/adaptive.md`
- **Design system**: Material vs Cupertino vs custom, theming through `ThemeExtension` vs constants, dark-mode obligation — affects `references/adaptive.md` and every styling example
- **Testing posture**: golden-test policy, coverage gate, whether integration tests run in CI, mocks vs fakes — affects the gates in `references/testing.md`
- **Safety posture**: how proactively to raise release-only and accessibility risks vs answering only what was asked — affects Output Gates verbosity
- **Integrations**: backend (Firebase, Supabase, REST, GraphQL), crash reporting, analytics, CI provider and distribution channel — affects `references/data.md` and `references/release.md`

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Creating a controller or a future inside `build` | `build` can run many times per second; each run makes a new object, restarts the request, and abandons the old one | Create in `initState` or as a field; dispose in `dispose` (rules 2-3) |
| `Container` everywhere | It composes decoration, constraints, padding, and transform whether or not you use them, and blocks `const` | `SizedBox`, `Padding`, `ColoredBox`, `DecoratedBox` — one job each |
| `UniqueKey()` to "force a refresh" | New identity every build: state, scroll offset, and animations reset every frame | `ValueKey(stableId)`, or change the value the widget renders |
| `GlobalKey` to reach another widget's state | Global lookup, blocks subtree reuse, and throws "multiple widgets used the same GlobalKey" on reparenting | Pass a callback down, or share a notifier (`references/architecture.md`) |
| `shrinkWrap: true` to silence an unbounded-height error | Lays out every child on every scroll frame; the list gets slower as it grows | `Expanded`, a bounded height, or slivers (`references/layout.md`) |
| `MediaQuery.of(context)` just for a size | Subscribes to ALL of `MediaQueryData`: the widget rebuilds on keyboard open, rotation, and inset changes | `MediaQuery.sizeOf(context)` (`flutter >=3.10`), or `LayoutBuilder` for the parent's real constraints |
| `Platform.isIOS` in shared code | `dart:io` does not exist on web — the app fails to compile or throws at startup | `defaultTargetPlatform`, guarded by `kIsWeb` (`references/adaptive.md`) |
| `Opacity` inside an animation | Wrapping a subtree triggers `saveLayer`: an offscreen buffer allocated and composited every frame | `FadeTransition`/`AnimatedOpacity`, or animate the alpha of a leaf's color |
| Network images without `cacheWidth`/`cacheHeight` | Decoded cost is width × height × 4 bytes regardless of the compressed file size; one photo can evict the whole image cache | Decode at display size (`references/performance.md`) |
| `flutter clean` as the first debugging move | Deletes build outputs and guarantees the slowest possible next build; it only fixes stale-artifact bugs | Read the first exception; reach for `clean` after a plugin, SDK, or native-config change (`references/commands.md`) |
| Catching channel failures with a bare `catch (e)` | Hides `MissingPluginException` (registration) behind `PlatformException` (the native side said no) — two different bugs | Catch `PlatformException` explicitly and branch on `code` (`references/platform.md`) |
| Judging performance from a debug build or a simulator | Debug is JIT plus instrumentation; simulators do not model the device GPU | `--profile` on a physical device (rule 7) |
| `if (visible) child` to hide a subtree | Removing the widget disposes its `State` — the "why did my half-filled form clear itself" bug | `Offstage`, or `Visibility(maintainState: true)` when the state must survive |

## Where Experts Disagree

- **State management library.** Bloc's camp buys testability and an explicit event log and pays in ceremony per feature; the Riverpod/Provider camp buys terseness and pays with looser conventions. The line both accept: plain `setState` is correct for state owned by one widget, and state read by two sibling subtrees needs something above them. Repo consistency outranks the ranking — a codebase running two of them is worse than either alone.
- **Codegen (`freezed`, `json_serializable`, route generators).** One camp treats generated code as the only defensible way to keep 200 models correct; the other refuses the `build_runner` step, the diff noise, and the CI minutes. Boundary: hand-written parsing scales to a few dozen models and stops scaling once nested optional fields appear. Set `codegen` once and stop re-litigating it.
- **`BuildContext`-free navigation.** A global `navigatorKey` makes navigation callable from anywhere (interceptors, notification handlers) and hides the tree dependency that makes routes testable. Reserve it for the few entry points with genuinely no context; anything triggered by a widget navigates with its own context.
- **Golden tests.** Advocates catch visual regressions no widget test sees; skeptics point at a suite that breaks on every font, platform, and SDK bump. Where the evidence lands: goldens pay off for design-system components on a pinned CI platform, and cost more than they return on full screens (`references/testing.md`).

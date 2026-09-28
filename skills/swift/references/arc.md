# ARC — Retain Cycles, Lifetime, and Objects That Never Die

ARC releases class instances when they are no longer strongly referenced; observe `deinit` rather than assuming a precise release point in optimized code. If an object stays alive, identify the retaining path before deciding whether it is an unintended leak. There is no garbage collector to blame and no delay to wait out.

## Prove It Leaked Before You Fix Anything

1. Put a breakpoint (or a `print`) in `deinit`. Navigate away. If `deinit` does not run, inspect remaining strong references in the memory graph before calling it a leak; an intentional cache may retain it.
2. Xcode's Debug Memory Graph shows the retaining chain — read it backwards from the leaked node to the root. Purple `!` marks cycles specifically.
3. Instruments → Leaks finds unreachable allocations; it will NOT report a growing cache, an array nobody empties, or a Substring pinning a huge parent (`debugging.md`).
4. Only then edit. A `[weak self]` added on suspicion usually moves the bug rather than fixing it.

## The Five Cycles That Cause Most Leaks

| Cycle | Signature | Fix |
|---|---|---|
| Closure ↔ self | Object strongly owns a stored closure that strongly captures the same object | Break the demonstrated cycle at its ownership edge, often with `[weak self]` (SKILL.md rule 2) |
| Delegate ↔ owner | `var delegate: FooDelegate` declared strong | `weak var delegate: (any FooDelegate)?` — requires the protocol be `AnyObject`-constrained |
| Timer ↔ target | `Timer.scheduledTimer(target: self, …)` never fires `deinit` | The timer retains the target and the runloop retains the timer; invalidate from `viewWillDisappear`-style teardown, ensure teardown outside `deinit` (it will never run), or use the block API with `[weak self]` |
| NotificationCenter ↔ observer | Block-based `addObserver(forName:object:queue:using:)` | The center retains the block; store the returned token and `removeObserver(token)` — the selector-based API auto-removes on modern OSes, the block one does not |
| Parent ↔ child | Two objects each holding the other strongly | The child's back-reference is `weak` or `unowned` (rule 2) |

## Capture Lists, Precisely

- Capture lists evaluate at closure *creation*, not at call. `[value = self.count]` freezes the value then; `[weak self]` takes a weak reference then.
- `[weak self] in guard let self else { return }` pins `self` alive for the rest of that closure body — after the guard you are back to strong semantics, deliberately.
- `[unowned self]` is a bet that `self` outlives the closure. Losing the bet is a crash, not a nil (SKILL.md Crash Messages).
- A genuinely non-escaping callback cannot be retained after its call; `map`, `filter`, `forEach`, and `sorted(by:)` do not need weak captures merely to prevent a persistent cycle (SKILL.md Traps). Confirm custom `withLock` APIs really are non-escaping before applying this shortcut.
- Capturing a property (`[count]`) instead of `self` is often the cleanest fix — no weakness, no cycle, no optional.
- Nested closures each need their own treatment: an inner closure that captures `self` strongly recreates the cycle even when the outer one is weak.

## `Task`, `async`, and Lifetime

- `Task { await self.load() }` retains `self` until the task finishes. That is usually correct — you want the work to complete — but a task that never finishes (an unbounded `for await`) keeps the object alive forever.
- Store long-lived tasks and cancel them in teardown. `.task` in SwiftUI does this for you.
- `[weak self]` inside a `Task` is only useful when the task can outlive the object legitimately; otherwise it turns a completed operation into a silently skipped one.
- An actor holding a `Task` that captures it can remain alive while the task is active; determine whether the task is finite and cancel or clear its handle at the appropriate lifecycle boundary. A stored task alone is not proof of a permanent leak.

## Weak, Unowned, and Their Costs

- `weak` yields an optional reference that becomes nil after the target is deallocated; checked `unowned` assumes the target outlives its use and traps if that assumption fails. Measure overhead before making a performance-based capture choice.
- `unowned(unsafe)` removes even the crash check — a dangling read becomes EXC_BAD_ACCESS at some later, unrelated point. Only with a measured reason.
- `weak` cannot be used with non-class types, and cannot be `let`.
- Do not rely on observing a target through another weak reference during its deinitialization; put required teardown in an explicit lifecycle method.
- Collections do not hold weakly: `[Delegate]` retains everything. Use `NSHashTable.weakObjects()` on Apple platforms or a small `struct WeakBox<T: AnyObject> { weak var value: T? }` wrapper elsewhere, and prune nils on access.

## Growth That Is Not A Cycle

- **Caches without eviction.** `NSCache` evicts under pressure; a `[Key: Value]` dictionary does not. Anything called "cache" needs a bound.
- **Substrings and Data slices** keep their parent buffer alive (SKILL.md Traps). Copy at the boundary.
- **Unbounded streams**: an `AsyncStream` with default buffering holds every unconsumed element — give the stream an explicit `bufferingPolicy` or a slow consumer becomes a leak.
- **Autorelease growth on Darwin**: a tight loop creating Objective-C objects (image decoding, `NSString` bridging) accumulates until the runloop drains. Wrap the loop body in `autoreleasepool { }`.
- **Retain of the whole view hierarchy** via one captured closure — the leaked node is small, the graph behind it is not. Fix the edge, not the node.

## Deinit Discipline

- `deinit` is not a substitute for main-actor lifecycle teardown. Run UI cleanup explicitly in the appropriate isolation context before the final reference disappears.
- Actor `deinit` isolation rules depend on the Swift language and compiler version (`concurrency.md`); check the target toolchain and prefer explicit asynchronous teardown when needed.
- Allow objects to complete deallocation; passing `self` out of `deinit` is undefined behavior.
- A class that needs `deinit` for correctness (file handles, C resources, observers) is a signal the resource should own its own small wrapper type rather than living on a large object.

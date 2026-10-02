# Debugging — Android Studio

Official overview: [Debug your app](https://developer.android.com/studio/debug).

## Breakpoint types

### Line breakpoints

Standard breakpoint on a line. Execution pauses when reached.

### Conditional breakpoints

Right-click breakpoint → add condition, for example:

```kotlin
i > 100 && user.isActive
```

Only breaks when the condition is true — preferred in hot loops.

### Log breakpoints

Right-click breakpoint → Suspend: unchecked, Log: checked. Logs an expression while
continuing execution:

```text
"User: " + user.name + ", count: " + items.size()
```

### Exception breakpoints

**Run → View Breakpoints → Add (Exception)**

- Caught exceptions: breaks on handled exceptions
- Uncaught exceptions: breaks on crashes

Filter by exception class for targeted debugging.

### Method breakpoints

Set on a method signature. Breaks on entry/exit. Slower than line breakpoints — use sparingly.

### Field watchpoints

Set on a field declaration. Breaks when the field is read/modified. Useful for unexpected state changes.

## Debugger features

### Evaluate Expression (Alt+F8)

Execute code in the current frame:

```kotlin
user.calculateScore()
items.filter { it.isValid }.size
```

Can modify state — avoid casual mutation when attaching to shared or production-like data.

### Watches

- Right-click variable → Add to Watches, or type an expression in the Watches panel.
- Watches re-evaluate in the current frame context.

### Frames panel

- Click a frame to see locals at that point.
- **Drop Frame** re-enters an earlier frame when supported.
- Filter library frames for clarity.

### Variables panel

- Expand objects to inspect fields.
- Right-click to set value when safe.
- Mark objects to track across scopes when the UI offers it.

### Inline values

Values beside variables in the editor (enable under Debugger settings if missing).

## Strategies

### Reproduce first

1. Identify exact reproduction steps.
2. Confirm the bug is consistent.
3. Note device, API level, build variant, and data preconditions.

### Binary search with breakpoints

1. Set a breakpoint at a suspected midpoint.
2. Check whether the bad state already exists.
3. Move earlier or later until the window is small.

### Startup races

Use **Debug** configuration or **Attach Debugger to Android Process** so early
`Application` / `ContentProvider` work is visible.

### Release-only bugs

Reproduce with a non-minified debug build when possible; if minify is required, keep
mapping files and use a profileable release build rather than guessing from stripped stacks.

## Logcat hygiene

- Filter by application package id and a stable tag.
- Avoid logging secrets, tokens, or PII.
- Clear the buffer before a focused repro so timestamps stay readable.

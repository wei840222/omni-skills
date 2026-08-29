# Termination Codes

Not every kill is a crash. These codes appear in the crash or termination report and name the subsystem outright; anything ending in a hex word is the OS explaining itself.

| Code / type | Meaning | First move |
|---|---|---|
| `0x8badf00d` "ate bad food" | Watchdog: main thread unresponsive too long, usually at launch or on resume | Find the synchronous work on the main thread in `application(_:didFinishLaunching…)` (`budgets-and-ceilings.md` / `core-rules.md`) |
| `0xdead10cc` "dead lock" | Held a file lock or an SQLite/Core Data handle in a shared App Group container while being suspended | Close or relinquish shared-container handles in `sceneDidEnterBackground`; this is the classic widget + app database bug (`core-rules.md`) |
| `0xc00010ff` "cool off" | Thermal shutdown of the app | Sustained GPU/CPU load — profile energy, not correctness (`budgets-and-ceilings.md` / `core-rules.md`) |
| `0xbaaaaaad` | Stackshot of the whole system, not a crash of your app | Usually a side effect; look for the real report next to it |
| `0xbad22222` | VoIP app resumed too frequently | PushKit misuse: a VoIP push must report a call, every time |
| `JetsamEvent` report, no crash log | Out of memory; the OS reclaimed the app | Memory footprint per device class, images and caches first (`budgets-and-ceilings.md` / `core-rules.md`) |
| `EXC_BAD_ACCESS` | Memory error — dangling pointer, over-released object, unowned reference | Zombies and Address Sanitizer; the language-level causes are in `swift` |
| `EXC_CRASH (SIGABRT)` with an NSException | Uncaught exception — the message is in the report's last exception backtrace | Read the exception message before the stack (`termination-codes.md`) |
| `EXC_BREAKPOINT (SIGTRAP)` | Swift runtime trap: force unwrap of nil, array bounds, integer overflow, precondition failure | The failing line is exact — no theory needed |
| `EXC_RESOURCE` CPU or WAKEUPS | Exceeded a sustained CPU or timer-wakeup budget | Background timers and polling loops (`budgets-and-ceilings.md`) |
| Anything else | Symbolicate first — an unsymbolicated report is a list of addresses, not evidence | `termination-codes.md` |

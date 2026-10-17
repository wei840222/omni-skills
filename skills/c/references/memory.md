# Memory Management Traps

- `malloc(0)` may return NULL or a valid pointer — implementation-defined; always check the result.
- `realloc(ptr, 0)` may free and return NULL — keep the original pointer until the new one succeeds.
- `free()` on stack memory corrupts the heap / process.
- Missing free on every exit path — use `goto cleanup` or a single owner wrapper.
- `calloc` zeros memory; `malloc` does not — reading uninitialized bytes is UB.
- Double free and use-after-free are UB and often security-relevant.
- Leaks inside loops — allocate once outside, or free each iteration.
- Prefer `sizeof(*ptr)` over `sizeof(type)` so refactors stay correct.

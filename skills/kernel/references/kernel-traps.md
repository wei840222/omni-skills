# Linux Kernel Review Traps

Load this reference when reviewing code or investigating a kernel warning, panic, lockup, data race, or module initialization failure.

## Review with positive invariants

Anchor each finding in the invariant the code must preserve: constrained contexts remain non-blocking, user-memory transfers cross the uaccess boundary, lockless readers and writers share one publication protocol, and partial setup has symmetric teardown.

## Context and allocation mismatch

**Signal:** a `might_sleep()` or sleeping-in-atomic-context warning, or allocation under a lock or interrupt path.

**Recovery:** identify the caller's context and active locks. Move sleepable work to process context, preallocate before the constrained section, or use an explicitly failure-aware non-blocking allocation only when the call path requires it. Test the failure path as well as the successful allocation.

## Incomplete IRQ locking

**Signal:** the same lock protects data in process context and a hard IRQ handler, but only one path changes interrupt state.

**Recovery:** apply the matching IRQ-safe locking discipline to all users of that shared lock, then inspect lock ordering and context annotations with lockdep enabled where available.

## Unsafe userspace transfer

**Signal:** direct dereference or `memcpy` from a `__user` pointer, or a return value from `copy_from_user()` treated as a conventional negative errno.

**Recovery:** use the appropriate uaccess helper, interpret a nonzero uncopied-byte count as an incomplete transfer, and propagate a suitable error after releasing or avoiding constrained locks.

## Lockless publication without a protocol

**Signal:** a pointer or state flag becomes visible to another CPU without a clear acquire/release, barrier, or lock protocol.

**Recovery:** document the reader/writer ownership model and use the kernel memory-model primitive that matches it. Validate with the relevant concurrency tooling and an architecture-aware review.

## Partial module initialization

**Signal:** a later setup step fails after registrations, allocations, or hardware resources have already succeeded.

**Recovery:** record resource ownership at each setup step, unwind only completed steps in reverse order, and exercise the injected-failure path before accepting the fix.

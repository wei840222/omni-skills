# Linux Kernel Development Basics

Load this reference when classifying execution context, choosing an allocation API, transferring user memory, reasoning about publication ordering, or designing initialization cleanup.

## Execution context and locking

Establish the actual context before choosing a locking or allocation rule. Process context can sleep; hard IRQ and softirq paths require non-blocking behavior. A path holding a conventional non-RT spinlock must keep its critical section non-sleeping. When the same lock is used from hard IRQ and process context, use the IRQ-safe lock variant consistently for that lock.

PREEMPT_RT changes `spinlock_t` implementation and its sleepability characteristics. Preserve the kernel's existing lock class and follow the documented PREEMPT_RT locking rules; use `raw_spinlock_t` only when its documented raw semantics are required.

## Allocation and failure handling

Use `GFP_KERNEL` where the caller may sleep and reclaim memory. Use `GFP_ATOMIC` only for allocations that must remain non-blocking, and handle its failure path explicitly. For allocations that need bounded failure behavior, evaluate a documented mempool design rather than relying on an allocation flag alone.

`kmalloc` provides physically contiguous memory within its allocator limits. `vmalloc` provides virtually contiguous memory and is unsuitable for APIs that require physically contiguous DMA memory. Use zero-initialized allocation when data can reach userspace before every byte has otherwise been initialized.

## User-memory access

Treat `__user` pointers as untrusted addresses. Copy through the uaccess helpers and check their return contract: `copy_from_user()` returns the number of bytes that were not copied, so zero means a complete copy. Establish whether the helper may fault or sleep before invoking it from a constrained context; when needed, first copy or pin data in an appropriate caller context.

## Memory ordering

Use the synchronization primitive that expresses the ownership and publication relationship. Locks provide ordering for their protected data. For lockless publication, pair the appropriate acquire/release or barrier operations with a documented reader/writer protocol; `READ_ONCE` and `WRITE_ONCE` address compiler-access semantics but do not, by themselves, define a complete inter-CPU synchronization protocol.

## Initialization cleanup

Track each successfully acquired resource and unwind in reverse acquisition order when a later initialization step fails. Structure the error path so every cleanup operation corresponds to a completed setup operation, then verify both the partial-failure path and the normal unload or teardown path.

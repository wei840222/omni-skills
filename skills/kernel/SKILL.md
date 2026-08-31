---
name: kernel
description: Diagnose and prevent Linux kernel development faults involving execution context, memory allocation, user-memory access, locking, memory ordering, or module error cleanup. Use when reviewing or debugging kernel C code, driver code, kernel panics, lockups, or warnings such as sleeping-in-atomic-context.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🐧"}'
---

## State location

This skill is stateless. Keep diagnosis artifacts in the host project's approved issue tracker or notes rather than in the skill package.

## Core triage

Choose the reference by task: use `kernel-basics.md` to establish a rule; use `kernel-traps.md` to turn an observed failure into a repair and verification plan.

1. Capture the affected kernel version, configuration, call path, execution context, active locks, and whether the path can run in hard IRQ, softirq, or process context.
2. Load `references/kernel-basics.md` for context, allocation, user-memory, ordering, and cleanup rules that apply to the finding.
3. Load `references/kernel-traps.md` when reviewing a patch or diagnosing a warning, panic, lockup, or failed initialization path.
4. State the violated invariant, identify the smallest safe code change, and name the verification method: a targeted test, relevant lockdep/KASAN/KCSAN configuration, or a focused code-path review.

## Review output

For each finding, report the execution context, the relevant API contract, the unsafe pattern, a concrete replacement, and any architecture-specific or PREEMPT_RT caveat. Keep uncertain conclusions conditional on the kernel configuration and call path.

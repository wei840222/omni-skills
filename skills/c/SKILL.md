---
name: c
description: >
  Write, review, and harden C for memory safety, pointer lifetime, bounds,
  strings, integer conversion, preprocessor traps, and undefined behavior.
  Use when malloc/free, realloc, dangling pointers, buffer overflows,
  strncpy/snprintf, signed overflow, sequence-point bugs, or ISO C UB show
  up. Prefer `cpp` for C++ RAII/modernization, `rust` when ownership/FFI is
  the primary language choice, `go` for Go memory/concurrency, `code` for
  plan→execute delivery loops, and `security-best-practices` for
  line-by-line secure-code patches beyond C language traps.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⚙️","requires":{"bins":["gcc","clang"]},"displayName":"C"}'
  related-skills: '{"cpp":"C++ RAII, smart pointers, and modernization instead of C memory discipline.","rust":"Rust ownership and borrow-checker work, or C FFI from the Rust side.","go":"Go memory, slices, and concurrency when the codebase is Go rather than C.","code":"Plan→execute→verify delivery loops before language-specific C fixes.","security-best-practices":"Minimal-diff secure coding review beyond C-language UB and memory traps."}'
---

## When to use

Use this skill for C source that needs memory, pointer, string, type, preprocessor, or undefined-behavior discipline. Load one `references/` file for the active trap class instead of restating every rule.

## Prefer other skills

| Ask | Prefer |
|---|---|
| C++ RAII / smart pointers / Rule of 0/3/5 | `cpp` |
| Rust ownership, Cargo, borrow checker | `rust` |
| Go slices, goroutines, net/http | `go` |
| Multi-step feature plan with approval gates | `code` |
| Secure-code patching across languages | `security-best-practices` |

## State location

This skill is **stateless**. It does not read or write `<state_root>` files. Capture durable project coding preferences with `code` / `coding` instead.

## Quick Reference

| Topic | File |
|-------|------|
| malloc/free, leaks, double free | `references/memory.md` |
| Null, dangling, pointer arithmetic | `references/pointers.md` |
| Null terminator, buffer overflow | `references/strings.md` |
| Integer overflow, signed/unsigned | `references/types.md` |
| Macro traps, include guards | `references/preprocessor.md` |
| Common undefined behavior | `references/undefined.md` |
| Spec and CERT source map | `references/sources.md` |

## Critical Rules

1. Check every `malloc` / `realloc` / `calloc` result before use; pair each success path with a single cleanup owner (`goto cleanup` or equivalent).
2. After `free(ptr)`, set `ptr = NULL` before any later use or second free.
3. Pass explicit lengths into functions — `sizeof` on a parameter decays to pointer size.
4. Keep room for the NUL terminator; prefer `snprintf` / bounded copies that always terminate.
5. Treat signed overflow, missing sequence points, and string-literal mutation as hard defects, not style nits.
6. Use `memmove` when regions may overlap; use `memcpy` only for disjoint buffers.
7. Initialize before read; avoid returning addresses of automatic storage.

## Workflow

1. Identify the trap class (memory, pointers, strings, types, preprocessor, UB).
2. Load the matching `references/` note and `references/sources.md` when citing standard/CERT wording.
3. Propose the smallest fix that removes the UB or leak, with a compile/test check.
4. If the ask is actually C++/Rust/Go delivery process, hand off per Prefer other skills.

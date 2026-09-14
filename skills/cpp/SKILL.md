---
name: cpp
description: Apply C++ standard practices to manage memory safely, eliminate undefined
  behavior, enforce RAII, and modernize legacy pointer and class architectures.
metadata:
  version: "1.1.0"
  requires:
    bins:
    - g++
  openclaw: '{"emoji": "⚡"}'
---

## When to use

Use this skill when writing, reviewing, or modernizing C++ that touches ownership, lifetime, containers, concurrency, templates, or undefined-behavior traps.

## Quick Reference

| Category | When to load | File |
|---|---|---|
| Memory | To manage RAII, smart pointers (`std::unique_ptr`), and `new`/`delete` traps. | `references/memory.md` |
| Pointers | To audit raw pointers, references, `nullptr`, and dangling references. | `references/pointers.md` |
| Classes | To implement Rule of 3/5/0, inheritance hierarchies, and virtual destructors. | `references/classes.md` |
| STL | To debug iterator invalidation, containers, and algorithmic complexities. | `references/stl.md` |
| Templates | To diagnose SFINAE, concepts (C++20), and two-phase lookup failures. | `references/templates.md` |
| Concurrency | To fix data races, deadlocks, and use `std::mutex` or atomics correctly. | `references/concurrency.md` |
| Modern C++ | To refactor using C++11/14/17/20 features like move semantics and structured bindings. | `references/modern.md` |
| Undefined Behavior | To detect integer overflow, strict aliasing violations, and out-of-bounds access. | `references/ub.md` |
| Sources | To verify domain guidance against primary cppreference pages. | `references/source-notes.md` |

## Core Practices

- Enforce **RAII** by defaulting to smart pointers (`std::unique_ptr`, `std::make_unique`) over raw `new`/`delete`.
- Prevent **Undefined Behavior** by validating signed arithmetic, checking for null/dangling pointers, and ensuring base classes have virtual destructors.
- Safely use **Move Semantics** with `std::move` and reassign moved-from objects before reuse.
- Ensure thread safety with `std::mutex` and `std::atomic` to eliminate data races.
- Choose safe container practices, such as `deque<bool>` over `vector<bool>` and boundary-checked element access.

## High-signal traps

- C-string `==` compares pointers — prefer `std::string` or `strcmp`.
- `map[key]` inserts a default value when missing — use `find()` / `contains()` to probe.
- Braced init `{}` prevents narrowing; parenthesized init can silently truncate.
- `vector` `push_back` may reallocate and invalidate iterators/references/pointers.
- `string_view` does not own data — the underlying buffer must outlive the view.
- Returning a reference or pointer to a local is dangling UB after return.

## Notes

- This skill is stateless guidance. Do not invent a package-local writable state path.
- Load only the reference file needed for the current failure mode.

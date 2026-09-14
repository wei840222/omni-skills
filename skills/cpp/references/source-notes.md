# C++ Source Notes

Primary references used to verify RAII, undefined behavior, ownership, and concurrency guidance in this skill.

## Core language and library

- **cppreference — Smart pointers** — `unique_ptr` / `shared_ptr` / `weak_ptr` ownership model via https://en.cppreference.com/w/cpp/memory
- **cppreference — new / delete** — allocation and deallocation forms via https://en.cppreference.com/w/cpp/memory/new/operator_new
- **cppreference — RAII** — resource lifetime tied to object scope via https://en.cppreference.com/w/cpp/language/raii
- **cppreference — Move semantics** — move constructors/assignment and moved-from state via https://en.cppreference.com/w/cpp/language/move_constructor
- **cppreference — Undefined behavior** — language UB categories via https://en.cppreference.com/w/cpp/language/ub
- **cppreference — Object lifetime** — construction/destruction rules via https://en.cppreference.com/w/cpp/language/lifetime

## Classes, pointers, and containers

- **cppreference — Virtual destructor guidance** — destroying derived objects through base pointers via https://en.cppreference.com/w/cpp/language/destructor
- **cppreference — Reference initialization / lifetime extension** — temporary binding rules via https://en.cppreference.com/w/cpp/language/reference_initialization
- **cppreference — std::vector** — iterator invalidation and capacity rules via https://en.cppreference.com/w/cpp/container/vector
- **cppreference — std::vector<bool>** — proxy-reference specialization caveats via https://en.cppreference.com/w/cpp/container/vector_bool
- **cppreference — std::map operator[]** — default insertion on missing keys via https://en.cppreference.com/w/cpp/container/map/operator_at
- **cppreference — std::string_view** — non-owning view lifetime via https://en.cppreference.com/w/cpp/string/basic_string_view

## Concurrency

- **cppreference — Memory model / data races** — concurrent conflicting access without sync is UB via https://en.cppreference.com/w/cpp/language/memory_model
- **cppreference — std::atomic** — atomic operations as race-free shared state via https://en.cppreference.com/w/cpp/atomic/atomic
- **cppreference — std::mutex / lock_guard** — RAII locking patterns via https://en.cppreference.com/w/cpp/thread/lock_guard
- **cppreference — std::scoped_lock** — deadlock-avoiding multi-lock acquisition via https://en.cppreference.com/w/cpp/thread/scoped_lock

## Templates and modern C++

- **cppreference — SFINAE** — substitution failure is not an error via https://en.cppreference.com/w/cpp/language/sfinae
- **cppreference — Constraints and concepts (C++20)** — requires-clause constraints via https://en.cppreference.com/w/cpp/language/constraints
- **cppreference — auto type deduction** — value category and reference collapsing notes via https://en.cppreference.com/w/cpp/language/auto

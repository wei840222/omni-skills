---
name: csharp
description: Load when reviewing or writing C# code to enforce robust practices, mitigate
  null traps, prevent async deadlocks, and write efficient LINQ.
metadata:
  openclaw: '{"emoji": "💜", "requires": {"bins": ["dotnet"]}}'
---
## When to load

Load this skill when reviewing or writing C# / .NET code that risks null-reference faults, async deadlocks, LINQ multiple-enumeration bugs, value/reference type confusion, collection mutation during iteration, or IDisposable leaks. Prefer progressive loading of `references/` files rather than restating every trap inline.

Load `references/domain-knowledge.md` when verifying nullability, async, LINQ, dispose, or money-precision guidance against primary Microsoft docs.

## Quick Reference

When triggered on a C# topic, load the specific reference file to diagnose the issue:

| Topic | File |
|-------|------|
| Null reference, nullable types | `references/nulls.md` |
| Async/await, deadlocks | `references/async.md` |
| Deferred execution, closures | `references/linq.md` |
| Value vs reference, boxing | `references/types.md` |
| Iteration, equality | `references/collections.md` |
| IDisposable, using, finalizers | `references/dispose.md` |

## Critical Rules

- `?.` and `??` prevent NRE but `!` overrides warnings — still crashes if null
- `.Result` or `.Wait()` on UI thread — deadlock, use `await` or `ConfigureAwait(false)`
- LINQ is lazy — `query.Where(...)` doesn't execute until iteration
- Multiple enumeration of IEnumerable — may re-query database, call `.ToList()` first
- Closure captures variable, not value — loop variable in lambda captures last value
- Struct in async method — copied, modifications lost after await
- String comparison culture — `StringComparison.Ordinal` for code, `CurrentCulture` for UI
- `GetHashCode()` must be stable — mutable fields break dictionary lookup
- Modifying collection while iterating — throws, use `.ToList()` to iterate copy
- `decimal` for money — `float`/`double` have precision loss
- `readonly struct` prevents defensive copies — use for performance
- `sealed` prevents inheritance — enables devirtualization optimization

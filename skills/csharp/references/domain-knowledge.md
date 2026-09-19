# C# domain knowledge (Gate 6)

Primary references for nullability, async, LINQ, types, collections, and disposal guidance in this skill:

## Nullability and nullable reference types
- Nullable reference types — https://learn.microsoft.com/en-us/dotnet/csharp/nullable-references
- Nullable value types — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/nullable-value-types
- `!` null-forgiving operator — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators/null-forgiving

## Async / await
- Asynchronous programming patterns — https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/
- Task-based Asynchronous Pattern (TAP) — https://learn.microsoft.com/en-us/dotnet/standard/asynchronous-programming-patterns/task-based-asynchronous-pattern-tap
- ConfigureAwait FAQ — https://devblogs.microsoft.com/dotnet/configureawait-faq/
- Cancellation in managed threads — https://learn.microsoft.com/en-us/dotnet/standard/threading/cancellation-in-managed-threads

## LINQ
- Language Integrated Query (LINQ) — https://learn.microsoft.com/en-us/dotnet/csharp/linq/
- Query execution (deferred vs immediate) — https://learn.microsoft.com/en-us/dotnet/csharp/linq/get-started/query-expression-basics#query-execution
- Enumerable.ToList — https://learn.microsoft.com/en-us/dotnet/api/system.linq.enumerable.tolist

## Types, collections, dispose
- Value types — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/value-types
- Collections and data structures — https://learn.microsoft.com/en-us/dotnet/standard/collections/
- IDisposable — https://learn.microsoft.com/en-us/dotnet/api/system.idisposable
- Implement a Dispose method — https://learn.microsoft.com/en-us/dotnet/standard/garbage-collection/implementing-dispose
- IHttpClientFactory — https://learn.microsoft.com/en-us/dotnet/core/extensions/httpclient-factory
- decimal floating-point — https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types#decimal-type

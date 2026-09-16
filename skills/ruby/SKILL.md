---
name: ruby
description: Write reliable Ruby code by avoiding mutable string traps, block pitfalls,
  and metaprogramming bugs.
metadata:
  openclaw: '{"emoji":"💎"}'
---

## When to load

- Load `references/objects.md` when diagnosing unexpected mutable string changes or object equality bugs.
- Load `references/blocks.md` when working with Procs, lambdas, or closures where return behaviors matter.
- Load `references/methods.md` when troubleshooting method visibility, implicit receivers, or `method_missing`.
- Load `references/collections.md` when debugging Array or Hash mutation problems (e.g. shared default values).
- Load `references/metaprogramming.md` when using `define_method`, `eval`, or creating dynamic methods.
- Load `references/rails.md` when addressing ActiveRecord performance (N+1), transactions, or callback skipping.
- Load `references/sources.md` when verifying current Ruby/Rails docs before hard claims.

## Critical Rules

- Strings are mutable — `s = "hi"; s << "!"; t = s` means t also has "!"
- `==` vs `equal?` vs `eql?` — `==` value, `equal?` identity, `eql?` hash equality
- Default hash value is shared — `Hash.new([])` shares same array, use block form
- `return` in proc returns from enclosing method — use lambda for local return
- Block variable shadows outer scope — `x = 1; [2].each { |x| }; x` is still 1 (3.0+)
- `method_missing` without `respond_to_missing?` — breaks `respond_to?` checks
- `private` in Ruby is per-object — `self.private_method` fails, implicit receiver works
- `||=` doesn't work for false/nil distinction — `false ||= true` replaces false
- Frozen string literals — `# frozen_string_literal: true` makes strings immutable
- `Symbol#to_proc` — `&:method_name` only works with no-argument methods
- `rescue => e` without type — catches StandardError, not Exception
- `ensure` always runs — even after return, use for cleanup

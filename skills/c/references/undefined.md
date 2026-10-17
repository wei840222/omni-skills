# Undefined Behavior Traps

- Mutating a string literal.
- Reading an uninitialized automatic variable.
- Signed overflow (`INT_MAX + 1`) — not defined wraparound.
- NULL dereference — optimizers may delete adjacent NULL checks.
- Falling off a non-void function without `return` when the value is used.
- Shifts by negative counts or ≥ width (`1 << 32` on 32-bit `int`).
- Modifying the same scalar twice between sequence points (`i = i++`).
- Type punning via incompatible pointer casts — use `memcpy` or a union where the implementation allows.
- Strict-aliasing violations such as `*(int *)&float_var`.
- Infinite loops with no side effects may be deleted by the optimizer.

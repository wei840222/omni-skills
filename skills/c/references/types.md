# Type Traps

- Signed integer overflow is UB — compilers may delete "impossible" checks.
- Unsigned subtraction that underflows wraps to a large positive value.
- `-1 > 1u` is true after the usual arithmetic conversions.
- Plain `char` signedness is implementation-defined — pick `signed char` or `unsigned char` explicitly for byte math.
- `1 << 31` on a 32-bit `int` can be UB (shift into / past the sign bit).
- `sizeof` yields `size_t` (unsigned) — mixed signed comparisons surprise easily.
- Float-to-int conversion truncates toward zero — `(int)3.9` is `3`.
- `INT_MIN / -1` overflows and is UB on two's-complement hosts.

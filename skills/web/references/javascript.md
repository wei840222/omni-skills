# JavaScript patterns for the web

Load for type coercion, async control flow, DOM safety, and form handlers.

## Type coercion

- Prefer **`===` / `!==`** — `"0" == false` is true; `"0" === false` is false.
- **`typeof null`** is `"object"` (legacy); check with `value === null`.
- **`NaN !== NaN`** — use `Number.isNaN(value)`.
- Empty array `[]` is truthy — check `.length` for emptiness.

## Async

- **`forEach` does not await** — use `for...of` for sequential awaits, or `Promise.all` / `Promise.allSettled` for parallel.
- Always handle rejections (`.catch` or `try/catch`); unhandled rejections fail Node and muddy browser logs.
- `async` functions always return a Promise — callers must await or chain.
- Avoid racey state updates: prefer functional updates / abort controllers when overlapping fetches share UI state.

## DOM

- **`querySelector` may return `null`** — guard before property access.
- Prefer **event delegation** on a stable parent; inspect `event.target` / `closest`.
- **Never assign untrusted HTML via `innerHTML`** — use `textContent`, DOM APIs, or a maintained sanitizer. XSS is a security boundary, not a style preference.
- `getElementsByClassName` is live; `querySelectorAll` is static — do not assume both update the same way during mutation.

## Objects and arrays

- Spread (`{...obj}`, `[...arr]`) is **shallow**; nested objects still share references.
- `Array(n)` creates holes that `.map` skips — prefer `Array.from({ length: n })` or `.fill`.
- `delete arr[i]` leaves a hole — use `.splice` to remove and shift.
- String-key insertion order is stable; integer-index keys sort numerically.

## Functions and forms

- Arrow functions lexically bind `this` — they ignore `.bind` / `.call` / `.apply` for `this`.
- Default parameters evaluate **per call**, not once at definition.
- Rest parameters must be last.
- On-page submit handlers must call **`event.preventDefault()`** or the browser navigates/reloads.

## Critical rules

- **`===` not `==`** for control flow and authz checks.
- **No raw `innerHTML` for user content**.
- **Await loops correctly** — never rely on `forEach(async …)` for completion.

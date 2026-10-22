# Solidity security pitfalls

Primary narrative aligned to the official Solidity Security Considerations and Common Patterns docs. Re-verify mutable details via `sources.md`.

## Reentrancy

Any interaction with another contract—including Ether transfer—hands over control before the caller finishes. A malicious callee can call back and double-withdraw if balances are updated after the external call.

Safe baseline:

1. **Checks** — validate inputs and authorization.
2. **Effects** — update balances / state.
3. **Interactions** — then `call` / external functions.

OpenZeppelin `ReentrancyGuard` / `nonReentrant` (and the transient-storage variant) are useful defenses, but CEI remains the first design rule. Do **not** treat the historical 2300-gas stipend of `transfer`/`send` as a security boundary; use CEI or a guard instead.

## Ether send / receive

- Contracts and EOAs cannot fully prevent unsolicited Ether (`selfdestruct` / forced sends are classic paths).
- `receive` / `fallback` may run with a limited gas stipend on plain transfers; do not assume that stipend is forever fixed.
- Prefer `addr.call{value: x}("")` with an explicit success check when you must send, and prefer a **withdraw** pattern so recipients pull funds.
- `send` returns `false` on failure; `transfer` reverts. Both still invoke recipient code and are poor primary reentrancy defenses.

## Gas and loops

Unbounded loops over storage-grown collections can hit the block gas limit and permanently stall state-changing paths. Paginate, cap iterations, or move large enumeration off-chain. `view` helpers can still be called on-chain by other contracts—document that risk.

## Auth and visibility

- State variables default to `internal` (derived contracts see them). `private` only hides from other contracts' Solidity access; chain data remains public.
- Never authorize with `tx.origin` (phishing via intermediate contracts). Use `msg.sender`.
- `external` functions are not callable as internal methods without `this.fn()` (extra call + gas).

## Integers

- Solidity **0.8+** defaults to checked arithmetic and reverts on overflow/underflow.
- `unchecked { ... }` restores wrapping; use only with a proven invariant.
- Division truncates toward zero. For fixed-point work, multiply before divide or use a reviewed math library.
- Prefer `type(uint256).max` over magic large literals; still bound untrusted inputs with `require`.

## Storage vs memory vs calldata

- `storage` persists; `memory` is temporary; `calldata` is read-only external input and often cheaper for large arguments.
- Explicit `storage` references are required when a function should mutate a state struct/array.
- Upgradeable contracts: **append** new storage variables; never reorder/remove; use EIP-1967 slots for proxy metadata so implementation and proxy layouts do not clash.
- Transient storage (`tstore`/`tload`, EIP-1153) is for intra-transaction state and is cheaper than durable storage when the host EVM supports it—confirm target chain support before relying on it.

## Upgradeable contracts

- Constructors do not run through proxies—use `initialize` + `initializer` (or equivalent).
- `delegatecall` executes implementation code against the caller's storage; layouts must stay compatible.
- Avoid depending on `selfdestruct` of an implementation; destroying or replacing implementation code can break proxies that still point at it. Treat internal-function pointers in upgradeable state as ephemeral across code updates.

## Other common mistakes

- Block timestamps are miner/builder-influenceable within protocol bounds—unsuitable for randomness or precise deadlines alone.
- Prefer `require` for user/input errors; reserve `assert` for invariants that should never fail.
- String equality via `==` is not available for `string` contents—compare `keccak256` hashes of the data (mind Hash-Collision caveats for ABI packing).
- Index event parameters that callers will filter; at most three `indexed` fields per event.

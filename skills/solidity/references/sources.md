# Sources for Solidity language and security claims

Prefer the live page over memorized constants. Re-check before stating gas stipends, hard-fork behavior, or library API names.

| Topic | Source | Applied guidance |
|---|---|---|
| Security pitfalls overview | [Security Considerations](https://docs.soliditylang.org/en/latest/security-considerations.html) | Reentrancy, CEI, loops/gas, ether send/receive, `tx.origin`, overflow/unchecked, mappings, upgradeable function pointers. |
| Withdraw / access patterns | [Common Patterns](https://docs.soliditylang.org/en/latest/common-patterns.html) | Withdraw-from-contract pattern and access restriction examples. |
| 0.8 checked math | [Solidity v0.8.0 Breaking Changes](https://docs.soliditylang.org/en/latest/080-breaking-changes.html) | Default checked arithmetic; `unchecked` restores wrapping. |
| Storage / transient layout | [Layout in Storage](https://docs.soliditylang.org/en/latest/internals/layout_in_storage.html) | Durable vs transient storage layout rules for authors and upgrade designers. |
| Proxy storage slots | [EIP-1967](https://eips.ethereum.org/EIPS/eip-1967) | Canonical proxy implementation/admin/beacon slots to avoid clashes. |
| Transient storage opcodes | [EIP-1153](https://eips.ethereum.org/EIPS/eip-1153) | `TSTORE`/`TLOAD` semantics for intra-transaction state. |
| Reentrancy utilities | [OpenZeppelin ReentrancyGuard](https://docs.openzeppelin.com/contracts/5.x/api/utils#ReentrancyGuard) | `nonReentrant` and transient-storage guard variants as library defenses on top of CEI. |
| Agent Skills format | [Agent Skills Specification](https://agentskills.io/specification.md) | Frontmatter and package shape for this skill. |

## Obsolete or softened claims

- Do not teach “`transfer`/`send` 2300 gas makes reentrancy safe.” Official docs still describe the stipend for receive/fallback paths, but also show that CEI (or a guard) is the real defense; stipend size may change.
- Do not treat `private` as confidentiality—chain observers can still read state.
- Do not present `selfdestruct`-based cleanup of implementations as a normal upgrade step.

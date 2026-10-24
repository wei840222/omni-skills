# Research Sources — Blockchain & EVM Fundamentals

Primary sources used for verifying EVM contract interactions, tooling, and distributed ledger security principles.

## Developer Libraries and Tooling

- **viem Documentation** — https://viem.sh/docs/getting-started
  - Typed client creation (`createPublicClient`, `createWalletClient`), contract read/write patterns, and transaction simulation (`simulateContract`).
- **Foundry Book** — https://book.getfoundry.sh/
  - Solidity testing, fast fuzzing, and deployment scripting with `forge` and `cast`.
- **The Graph Documentation** — https://thegraph.com/docs/en/
  - Subgraph indexing, GraphQL schema definitions, and event mapping.

## Ethereum Improvement Proposals (EIPs)

- **EIP-20: Token Standard** — https://eips.ethereum.org/EIPS/eip-20
  - Core ERC-20 interface (`transfer`, `approve`, `transferFrom`, `balanceOf`).
- **EIP-712: Typed Structured Data Hashing and Signing** — https://eips.ethereum.org/EIPS/eip-712
  - Safe off-chain message signing preventing blind transaction execution.
- **EIP-4337: Account Abstraction Using Alt Mempool** — https://eips.ethereum.org/EIPS/eip-4337
  - UserOperation flow, bundlers, and smart contract wallet abstraction without consensus-layer changes.

# Technical operations and troubleshooting

## Fees and timing

- Child-chain fees combine **L2 execution** and a **parent-chain data** component (calldata/blob posting economics).
- Congestion on Ethereum can raise the L1 data portion even when L2 execution is cheap.
- Sequencer soft-confirmation is fast (sub-second block production targets on public chains); that is not the same as parent-chain finality for withdrawals.
- No Ethereum-style priority-gas auction is required for ordinary inclusion ordering on the sequencer path; tip fields may still appear in wallet UX but ordering follows sequencer receipt.

## Stylus

- Stylus runs WASM contracts (Rust/C/C++ toolchains) alongside EVM/Solidity on Nitro.
- Fraud proofs can replay disputed execution via WASM; normal execution uses native speed paths.
- **Operational caveat:** Arbitrum docs note the Security Council has **temporarily paused new Stylus contract activations** on Arbitrum One and Nova; already-activated contracts may keep running until they expire. Re-read the Stylus intro / notices before telling a user to deploy new Stylus code.
- Source: [A gentle introduction to Stylus](https://docs.arbitrum.io/stylus/gentle-introduction).

## Sequencer and force inclusion

- Public chains use a sequencer path operated in the Arbitrum system (historically Offchain Labs operated sequencing; progressive decentralization is documented separately).
- Sequencer delay or outage affects fast inclusion; it does not by itself let the sequencer steal bridged funds.
- Users can **force-include** transactions via parent-chain inbox mechanisms if the sequencer censors or stalls beyond protocol delays—expect slower, more expensive inclusion than the happy path.
- Soft confirmation from `eth_sendRawTransaction` to the sequencer means ordered/executed on the child view; batch posting and L1 finality are additional stages when the application needs them.

## BoLD and the dispute window

- **BoLD** (Bounded Liquidity Delay) is the dispute protocol described as active on Arbitrum One, Nova, and Sepolia.
- It bounds how long disputes delay confirmation and supports broader participation in validation/challenges versus older permissioned assumptions.
- Native withdrawals and other child→parent messages still wait for assertion confirmation after the challenge/dispute window—see bridging reference for user-facing steps.
- Source: [Overview of BoLD](https://docs.arbitrum.io/how-arbitrum-works/bold/gentle-introduction), [Chain parameters](https://docs.arbitrum.io/for-devs/dev-tools-and-resources/chain-info).

## Common failures → first checks

| Symptom | First checks |
|---|---|
| `Insufficient funds for gas` / cannot deploy | Child-chain **ETH** balance; ARB does not pay gas. |
| Tx pending forever | Correct RPC/network; sequencer status; nonce gaps; try official status tools. |
| Withdrawal “stuck” multi-day | Still inside dispute window? Claim available in bridge history? L1 ETH for claim? |
| Revert on swap/bridge | Allowance, slippage, paused pool, wrong token address for **this** chain ID. |
| “Wrong network” / missing funds | Same address on Ethereum vs One vs Nova; check each explorer. |
| Stylus deploy rejected | Current activation pause / expiry policy on target chain. |

## Security posture (agent guidance)

- Smart-contract and bridge risk remain even when the rollup dispute game is healthy—audit status and allowlists matter.
- After the dispute window, confirmed assertions inherit Ethereum settlement assumptions for the rollup path; Nova adds AnyTrust DA assumptions.
- Prefer official bridge contracts and documented RPCs over random airdropped “support” links.

# LINK Token and Network Context

## LINK basics

- LINK is an ERC-20 (18 decimals) used to pay Chainlink node operators and many product fees.
- Contract addresses differ per chain — always verify on the official LINK token contracts page before transfer or approval.
- Standard ERC-20 rules apply: gas is paid in the native token of that chain; no tax/rebase mechanics.

## Bridging

- Prefer **official Chainlink CCIP** paths for moving LINK or other assets across supported lanes.
- Confirm lane availability and fee token (LINK or native) before sending; finality depends on source and destination chain rules.
- Third-party bridges add extra smart-contract risk — disclose that trade-off explicitly.

## Network trade-offs (oracle consumers)

| Environment | Typical posture |
|---|---|
| Ethereum mainnet | Highest security / highest gas; default for critical collateral feeds |
| L2s (Arbitrum, Optimism, Base, …) | Lower fees; still verify L2 sequencer uptime feeds when relevant |
| Alt-L1s (Polygon, Avalanche, …) | Native integrations exist; trust assumptions differ from Ethereum L1 |
| Testnets (e.g. Sepolia) | Use faucet/testnet LINK; never treat test addresses as mainnet |

## Prefer other skills when

- Stuck nonce / EIP-1559 gas on a Chainlink consumer tx → `ethereum`
- Writing the Solidity consumer itself safely → `solidity`
- Chain-native Avalanche or Polygon ops without Chainlink products → `avalanche` / `polygon`
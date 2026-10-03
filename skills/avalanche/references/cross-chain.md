# Cross-chain and bridging

## Primary Network atomic transfers (C ↔ X ↔ P)

Moving **AVAX** between Primary Network chains is not a normal C-Chain ERC-20 send.

1. **Export** from the source chain.
2. **Import** on the destination chain.
3. Use a wallet that supports all involved chains (Core / Avalanche wallet). MetaMask alone cannot complete X/P legs.

Remind the user that:

- Balances are per-chain. "I have AVAX" is incomplete without the chain name.
- Atomic transfers are usually fast once both legs complete, but a stuck flow is often an export without import (or the reverse).
- Address formats differ across chains; do not paste a C-Chain `0x` address into an X-Chain-only field.

## Bridging from other networks

- Official Avalanche Bridge entry points are commonly reached via `https://bridge.avax.network/` and Core (`https://core.app/`).
- Cross-ecosystem bridges (LayerZero, Stargate, and similar) are third-party paths with their own fees, finality, and wrapped-asset semantics.
- Budget **source-chain gas + bridge fee + destination gas**. Destination C-Chain still needs AVAX for later transactions.
- Withdrawals back to Ethereum or other L1s can take longer than the Avalanche leg; read the bridge's own status page rather than assuming sub-second finality.

## Interoperability inside Avalanche

Avalanche also documents Interchain Messaging / ICTT style protocols for L1-to-L1 messaging and token transfer. Use those only when the user is operating across Avalanche L1s; do not conflate them with C↔X↔P atomic transfers or Ethereum bridges.

## Advice pattern

1. Ask source network, destination network, asset, and whether the destination wallet can see that chain.
2. Prefer official Core/bridge UI steps for non-developers.
3. After completion, verify the destination balance on the correct chain explorer or wallet network switch—not only the source receipt.

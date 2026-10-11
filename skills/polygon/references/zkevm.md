# Deprecated Polygon zkEVM boundary

## Current official stance

Polygon developer docs for adding networks state plainly:

> **Polygon zkEVM is deprecated.** It is no longer recommended for new integrations … New chains and applications should use Polygon Chain or Polygon CDK.

Treat zkEVM mainnet/testnet guidance in older blogs as **historical**. Do not design new production flows on zkEVM.

## Practical differences (legacy context only)

| Topic | Polygon Chain (current) | Legacy zkEVM |
|-------|-------------------------|--------------|
| Role today | Default public settlement chain for this skill | Deprecated; migration/exit only |
| Gas token | POL | Historically ETH on that network |
| Explorer / RPC | polygonscan + PoS RPCs | Separate historical endpoints |
| Bridge | Portal ↔ Ethereum | Distinct bridge path; exit before assuming PoS balances |

## Safe agent behavior

1. If the user already holds assets on zkEVM, help them **identify the network**, bridge out via official Portal flows where applicable, and land on Polygon Chain or Ethereum.
2. If the user asks "should I build on zkEVM?", answer **no for new work**; point to Polygon Chain or [Polygon CDK](https://docs.polygon.technology/chain-development/cdk/) / Agglayer docs instead.
3. Do not invent chain ID `1101` operational runbooks as current best practice; if a wallet still shows a zkEVM network, treat it as legacy connectivity.
4. MATIC stranded on zkEVM: Portal bridge to Ethereum, then MATIC→POL upgrade on Ethereum (`migration.md`).

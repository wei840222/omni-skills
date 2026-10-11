# Research sources (Gate 6)

Retrieval window for this refactor: **2026-10-11**. Re-open these pages before restating chain IDs, RPCs, migration steps, or deprecation claims.

## Agent Skills package format

- **Agent Skills specification** — https://agentskills.io/specification
- **Document index** — https://agentskills.io/llms.txt
- **Reference validator package** — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Polygon developer docs

- **Docs index (llms.txt)** — https://docs.polygon.technology/llms.txt
- **Building on PoS / Polygon Chain** — https://docs.polygon.technology/pos/get-started/building-on-polygon
- **RPC endpoints (mainnet 137, Amoy 80002, POL gas)** — https://docs.polygon.technology/pos/reference/rpc-endpoints
- **MATIC → POL migration** — https://docs.polygon.technology/pos/concepts/tokens/matic-to-pol
- **POL token reference** — https://docs.polygon.technology/pos/concepts/tokens/pol
- **Polygon Portal bridge overview** — https://docs.polygon.technology/pos/how-to/bridging/ethereum-polygon/portal-ui
- **Portal wallet guide** — https://docs.polygon.technology/tools/wallets/portal
- **MetaMask on Polygon** — https://docs.polygon.technology/tools/wallets/metamask
- **Add Polygon network (includes zkEVM deprecated warning)** — https://docs.polygon.technology/tools/wallets/metamask/add-polygon-network
- **Gas Station** — https://docs.polygon.technology/tools/gas/polygon-gas-station
- **Faucet** — https://docs.polygon.technology/tools/gas/matic-faucet
- **Polygon CDK (post-zkEVM direction)** — https://docs.polygon.technology/chain-development/cdk/

## Live product / explorer entry points

- **Polygon Portal** — https://portal.polygon.technology
- **POL upgrade UI** — https://portal.polygon.technology/pol-upgrade
- **Polygonscan** — https://polygonscan.com/
- **Amoy explorer** — https://amoy.polygonscan.com/
- **ChainList mainnet** — https://chainlist.org/chain/137
- **ChainList Amoy** — https://chainlist.org/chain/80002
- **Public RPC (community)** — https://polygon-rpc.com

## Governance / narrative context

- **MATIC/POL migration blog (Sept 4 migration announcement context)** — https://polygon.technology/blog/save-the-date-matic-pol-migration-coming-september-4th-everything-you-need-to-know
- PIP threads cited from POL docs (PIP-17/18/19/25/26) via https://docs.polygon.technology/pos/concepts/tokens/pol

## Fragile claims

- Do not quote live gas USD or gwei as timeless facts.
- Do not treat deprecated Polygon zkEVM as a recommended integration target.
- Do not use `bridge.polygon.technology` as the official bridge URL (prefer Portal).
- Do not invent exact withdrawal durations; describe checkpoint + claim and tell the user to verify Portal/explorer status.
- Do not claim all third-party bridges or exchanges support every token/network pair.

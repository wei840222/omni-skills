# Tokens, DeFi orientation, and staking

## Tokens

- ERC-20 / ERC-721 / ERC-1155 patterns match Ethereum; always verify the **Polygon** contract address, not the Ethereum twin by ticker alone.
- Bridged assets are pegged representations—unwrapping/bridging back is required to hold the L1 native form.
- Lower liquidity than Ethereum mainnet is common; large swaps need slippage and route checks.

## DeFi orientation (not trading advice)

- Familiar surfaces (DEX, lending, perps) often deploy on Polygon Chain with the same UX metaphors as Ethereum.
- Prefer protocol-specific skills or live docs when giving contract-level steps.
- This skill does **not** recommend buy/sell/hold or yield targets—hand market questions to `crypto-tools` after mechanics are clear.

## Staking (orientation)

- POL staking secures Polygon Chain validator set economics; details and UIs change with governance (PIP lineage).
- Unbonding / undelegation delays are protocol-defined—read current staking docs or UI before promising unlock times.
- Liquid-staking receipts (historical names like stMATIC / MaticX and successors) are separate tokens with their own risks; verify the live product docs.
- Never ask for validator keys or seed phrases in chat.

## When to stop and switch skills

- Generic EVM approval/Permit debugging → `ethereum`
- Smart-contract architecture → `blockchain` / Solidity skills
- Price, TVL, explorer bulk lookup → `crypto-tools`

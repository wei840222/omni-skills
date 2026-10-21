# Hedera Token Service (HTS)

## Native vs EVM tokens

- HTS creates fungible tokens and NFTs as native network entities without requiring a custom Solidity token contract.
- Hedera also supports ERC-style tokens via the EVM and hybrid patterns that combine HTS operations with smart-contract logic.
- Prefer HTS guidance for association, admin keys, and fixed network fees; prefer `ethereum` / Solidity skills when the user is debugging ERC-20/721 contract code on Hedera's EVM.

## Association requirement

- Before an account can receive a custom fungible or NFT token, it usually must associate with that token ID (`TokenAssociateTransaction` or wallet equivalent). The receiving account key signs the association.
- Association failure is a common root cause of failed airdrops and peer transfers. Confirm the receiver's associations (or max automatic associations) before blaming balances or memos.
- Some auto-create / alias flows can associate during creation; do not assume every path skips association—check the transfer receipt and docs for the exact path in use.
- NFT association is per token type; after association, the account can hold multiple serials of that type.

## Admin and compliance keys

- Token admin, freeze, wipe, KYC, and supply keys can materially change holder risk. Inspect token info before treating a token as immutable or non-custodial.
- Custom fee schedules can attach fixed or fractional fees to transfers without a separate royalty contract. Surface those fees when estimating what a receiver or seller actually nets.

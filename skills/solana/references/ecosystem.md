# RPCs, explorers, and wallet safety

## RPCs and explorers

- Public RPC endpoints can apply rate limits. Choose an RPC service and commitment configuration that matches the application's reliability and throughput requirements.
- Use `getRecentPrioritizationFees` when current prioritization-fee samples are relevant to a submission decision.
- Solana Explorer, Solscan, and SolanaFM can help inspect transaction signatures and instruction data. Treat explorer output as diagnostic evidence and confirm critical data through the RPC or program's authoritative source.

## Wallet safety

- Read a wallet's transaction simulation and requested accounts before approving a signature.
- Use a separately funded wallet for unfamiliar applications and keep primary holdings isolated from unverified interactions.
- Verify the program ID, destination accounts, token mint, and expected token amount before signing. A wallet confirmation is authorization, not proof that the request is safe.

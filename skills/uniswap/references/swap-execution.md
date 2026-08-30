## Swap Execution
- Slippage tolerance sets max acceptable price change — 0.5% for stablecoins, 1-3% for volatile pairs, higher for low liquidity tokens
- "Price impact" and "slippage" are different — impact is immediate effect of your trade size, slippage is protection against price movement
- High price impact (>2%) means you're moving the market — split large trades or use limit orders on Uniswap X
- Transaction deadline prevents stale swaps — 20-30 minutes default is usually fine, but pending tx beyond deadline will fail

## Gas Optimization
- Approve + swap is two transactions on first use — budget gas for both
- L2s (Arbitrum, Base, Optimism) have Uniswap with 10-50x lower fees — same interface, same liquidity depth
- Swapping during low gas periods (weekends, UTC night) saves significantly on mainnet
- Failed transactions still cost gas — simulate first if unsure about slippage or liquidity

## Failed Swap Causes
- "Insufficient liquidity" — try smaller amount or different route
- "Slippage exceeded" — price moved during pending period, increase slippage or retry
- "Transfer failed" — token has transfer tax or restrictions, may be a scam token
- "Deadline exceeded" — transaction was pending too long, just retry
- "Approve first" — need to approve token before swap, this is normal

## Uniswap X and Limit Orders
- Uniswap X uses off-chain orders filled by market makers — no gas if order isn't filled
- Limit orders let you set target price — order sits until price is reached or expires
- Partial fills possible — large orders may fill incrementally
- Check order status in the app — pending orders can be cancelled

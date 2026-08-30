## MEV and Frontrunning
- Public swaps on Uniswap are visible in mempool before execution — bots can sandwich your trade
- Use MEV protection: swap through Uniswap wallet (built-in protection), or connect via Flashbots Protect RPC
- Signs of sandwich: execution price worse than quoted, with suspicious buy before and sell after your tx
- Uniswap X routes through private order flow — significantly reduces MEV extraction

## Token Approval Traps
- First swap of any token requires approval transaction — this is normal, costs gas, and happens once per token per spender
- "Infinite approval" is the default — convenient but risky if Uniswap router is ever compromised
- Check and revoke old approvals at revoke.cash — approvals persist forever until explicitly revoked
- Approval transaction can succeed while swap fails — user pays gas for approval but swap reverts on slippage

## Fake Tokens
- Anyone can create a token with any name and symbol — "USDC" on Uniswap might not be real USDC
- Always verify token contract address on CoinGecko, CoinMarketCap, or project's official site
- Warning signs: no liquidity, recently created, honeypot (can buy but not sell), tax on transfer
- Uniswap shows warning for unverified tokens — heed this warning, especially for tokens you found via links

## Safety Checklist Before Large Swaps
- Verify token contract address matches official source
- Check price impact percentage — high impact means bad execution
- Confirm slippage is set appropriately for the pair
- Use MEV protection for mainnet trades
- Consider splitting very large trades
- Double-check recipient address if sending to different wallet

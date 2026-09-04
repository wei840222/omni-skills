# MEV Protection

- Public mempool transactions can be frontrun or sandwiched — especially swaps on DEXs
- Flashbots Protect RPC (protect.flashbots.net) hides transactions from public mempool until mined
- Private transaction options: MEV Blocker, Flashbots Protect, or DEXs with native protection (CoW Swap)
- Signs of sandwich attack: swap executed at worse price than quoted, with suspicious txs immediately before and after yours

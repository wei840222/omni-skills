# Address Validation

- Ethereum addresses are case-insensitive but the checksum (mixed case) catches typos — `0xABC...` vs `0xabc...` are the same address
- ENS domains can expire — always verify current owner before sending to a .eth name
- Contract addresses vs EOA: contracts can reject ETH transfers or behave unexpectedly — check on etherscan if address has code
- Some tokens have multiple addresses (official + scam clones) — verify contract address on CoinGecko or project's official site

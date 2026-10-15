# Mining orientation

Load for RandomX, solo/pool trade-offs, or P2Pool setup questions. The Monero
Project does not endorse a specific commercial pool.

## Proof of work

Monero uses **RandomX**, designed for egalitarian, ASIC-resistant mining on
consumer hardware. Official mining guidance states CPUs are much more efficient
than GPUs for Monero.

## Solo vs pool vs P2Pool

| Path | Why choose it | Watch-outs |
|---|---|---|
| Solo via official GUI/CLI | Strengthens network independence; no pool operator | Block discovery can take a long time at low hashrate ("lottery") |
| Centralized pool | More frequent payouts proportional to shares | Pool fees, third-party miner software, and >50% hashrate concentration risk |
| **P2Pool** | Peer-to-peer pool with 0% fee and miner-controlled templates | Need a synced node + P2Pool + miner; low hashrate may belong on mini/nano |

Official project pages encourage solo mining with Monero software and also
encourage P2Pool as a decentralized alternative to trusted pools.

## P2Pool practical notes (from p2pool.io / project posts)

- Mine to a **primary `4…` address** unless you intentionally pass both main and
  subaddress parameters; mining exposes the configured address on the sidechain,
  so a dedicated mining wallet is recommended.
- Confirmed wallet support called out by P2Pool docs includes recent official
  CLI/GUI, Monerujo, Cake, and Feather releases—re-check version floors before
  stating compatibility.
- Typical stack: synced `monerod` (ZMQ pub enabled) → `p2pool` → XMRig to local
  stratum (`127.0.0.1:3333`).
- There is no conventional "pending balance"; progress is share-based inside a
  PPLNS window, then payouts land when P2Pool finds Monero blocks.
- Low hashrate miners who wait too long for shares should consider P2Pool mini
  or nano rather than inventing a third-party pool recommendation.

## Software pointers

- Solo: official GUI/CLI miner paths.
- Dedicated miners often discussed in community docs include XMRig; treat
  developer-fee claims as software-specific and verify the chosen release notes.
- Pool comparison sites such as miningpoolstats.stream are informational only.

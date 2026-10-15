# Troubleshooting

Work the smallest matching check first. Do not invent exchange status, fee USD
amounts, or daemon flags when the wallet UI already shows a clearer state.

## Wallet shows 0 / still scanning

1. Confirm the wallet is connected to a synced daemon (local or remote).
2. Wait for the wallet's own refresh/scan to finish—background scanning often
   looks like a zero balance until outputs are found.
3. If restoring from seed, expect a longer first scan; wrong restore height
   delays discovery.
4. Only after sync completes, reconsider whether the seed/account is the one
   that actually received funds.

## "Daemon not connected" / node lag

1. Check that `monerod` is running and reachable at the configured host/port.
2. If using a remote node, try another trusted endpoint or fall back to a local
   node; network filters and RPC auth mismatches are common.
3. For P2Pool setups, ensure `monerod` is not stuck behind the network tip and
   that required ZMQ/pubsub flags from current P2Pool docs are present.

## Received funds not spendable yet

1. Distinguish **normal output maturity** (wallet shows pending/locked for a
   short block count) from a sender-set **custom `unlock_time`**.
2. Inspect the transfer details (`show_transfers` in CLI, or GUI transfer
   metadata) for an unexpected unlock height.
3. Custom unlock times are public and discouraged; if present, wait for the
   absolute height/time rather than attempting RBF-style acceleration—Monero
   does not provide Bitcoin-style replace-by-fee.

## Stuck outgoing transaction

1. Confirm whether the tx was relayed and which daemon sees it.
2. Because Monero lacks Bitcoin RBF, "stuck" usually means waiting for inclusion
   or fixing daemon connectivity—not bumping a fee field the way BTC wallets do.
3. Do not advise double-spend experiments; focus on node health, fee priority
   selected at creation time, and wallet status screens.

## Payment disputes

1. Gather tx ID, tx key, and recipient address.
2. Use the official prove-payment flow rather than a transparent explorer.
3. View-key screenshots alone are insufficient proof of an outgoing payment.

## Safety stops

- Refuse seed-phrase "recovery service" workflows.
- If download corruption is suspected, re-fetch from getmonero.org and verify
  hashes before opening the wallet again.

# Sources for Arbitrum operational claims

Re-verify time-sensitive protocol, product, and parameter claims against these primary pages before giving irreversible advice.

| Topic | Source | Applied guidance |
|---|---|---|
| Docs index for agents | [Arbitrum llms.txt](https://docs.arbitrum.io/llms.txt) | Discover canonical markdown routes; append `.md` to docs URLs when scraping. |
| Official bridge UX | [Bridge quickstart](https://docs.arbitrum.io/arbitrum-bridge/quickstart) | Parent/child deposit and withdraw flows; seven-day user messaging for One/Nova native exits; claim step. |
| Withdrawal monitoring | [Monitor withdrawals](https://docs.arbitrum.io/arbitrum-bridge/withdrawal-monitoring) | Lifecycle, timelines, SDK/onchain status checks. |
| Public chains | [Arbitrum chains overview](https://docs.arbitrum.io/build-decentralized-apps/public-chains) | One = Rollup; Nova = AnyTrust; Nitro stack shared. |
| Chain IDs / RPC / dispute window | [Chain info](https://docs.arbitrum.io/for-devs/dev-tools-and-resources/chain-info) | `42161` / `42170` / `421614`; example RPCs; dispute window ~45818 blocks (~6.4 days) on One/Nova. |
| BoLD disputes | [BoLD overview](https://docs.arbitrum.io/how-arbitrum-works/bold/gentle-introduction) | BoLD active on One, Nova, Sepolia; bounds dispute delay; permissionless validation path. |
| Stylus model + activation notice | [Stylus gentle introduction](https://docs.arbitrum.io/stylus/gentle-introduction) | WASM + EVM; check Security Council pause on **new** activations. |
| FAQ (gas tip, disputes, messages) | [Arbitrum FAQ](https://docs.arbitrum.io/learn-more/faq) | Sequencer ordering vs tips; disputes delay L2→L1 confirmation, not ordinary L2 txs. |
| Risk / TVS dashboards | [L2Beat Arbitrum One](https://l2beat.com/scaling/projects/arbitrum) | Live TVS, stage, and risk notes—do not hard-code stale TVL. |
| Token withdraw guide | [Withdraw tokens to parent chain](https://docs.arbitrum.io/arbitrum-essentials/bridging/withdraw/tokens) | Gateway withdraw path and challenge-period framing (~6.4-day language in essentials). |

## Obsolete claims removed or softened in this refactor

- “Stylus coming soon” → Stylus exists; **new activations** may be paused—check live notice.
- Hard-coded multi-billion TVL → point to L2Beat (time-sensitive).
- “Exactly 7.00 days always” → user docs say ~seven days; parameters list ~6.4 days / 45818 blocks.
- “Decentralized sequencer coming” as a vague promise → describe current sequencer path + force-inclusion + BoLD docs instead of roadmap marketing.

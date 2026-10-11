# Setup — Polymarket CLI

Read on first use, when the user changes their use case, or when optional preference
tracking is requested. Public market queries work without saved state or a wallet.

1. Answer the immediate market query first. Ask whether future activation should be
   relevant-request automatic or direct-request only when this preference matters.
2. Identify read-only exploration, active trading, data analysis, or automation.
   Ask before saving any preference; persistence is optional. Resolve the root
   through SKILL.md and save only agreed fields in `<state_root>/memory.md`.
3. For requested tracking, confirm markets and whether the user wants on-demand
   checks or a separately authorized scheduled monitor. A preference is not a job.
4. For trading only, hand wallet setup to the user in their own terminal. User-only
   operations include `polymarket setup`, wallet create/import/show/address/reset,
   and any secret entry. The agent can explain these actions but does not execute
   them, read CLI credential files, or collect keys in chat.
5. Before an authorized trade, follow the entry-point pre-trade confirmation and
   allowance/gas checks. Approval transactions are separately confirmed mutations;
   existing allowance may already be sufficient. Verify current native gas and
   collateral requirements before asking the user to fund anything.

## Permitted persistence

With consent, keep activation choice, main use case, requested tracked markets,
and voluntarily shared trading/risk preferences in `<state_root>/memory.md`.
Use `references/memory.md` for enum semantics and `assets/memory-template.md` for
initial content. Host shared-memory writes require a separately supplied path,
explicit consent and the minimal activation pointer only.

## Interaction

Acknowledge a stated interest, query relevant public markets, then present observed
results with timestamps. For an election request, run a public election search and
report the returned questions and prices; a documentation example is not a live quote.
Keep wallet onboarding for users who actually request trading. Installation needs
separate consent; load `references/commands.md` for supported installation options.

# Campaign operations — TikTok Ads

Use with TikTok Ads Manager auction campaigns. Re-open `sources.md` before quoting current floors or quotas.

## Structure

- Keep **one primary objective per campaign** so optimization signals stay coherent.
- Start with a focused set of ad groups (often about 3–5) and a focused creative set per ad group (often about 3–5). Treat those counts as operating heuristics, not hard platform laws.
- Prefer broad-enough targeting early so delivery and creative signals can train; tighten only after stable delivery.
- Behavior and engagement signals often outperform stacked interest stacks on TikTok; validate with account data.

## Budgets (platform floors)

From TikTok Ads Manager **About Budget** (verify live):

- **Daily budget**: campaign budget must **exceed $50**; ad group budget must **exceed $20**.
- **Lifetime budget**: campaign budget must **exceed $50**; ad group lifetime minimum scales with days × the minimum daily ad-group budget (example in the help article: 31 days × $20 = $620).
- Campaign budget should not sit below ad group budget, or delivery can stall.
- Budget type (daily vs lifetime) cannot be switched after the campaign or ad group is live.

## Learning phase

From TikTok Ads Manager **About Learning Phase** (verify live):

- The learning phase is when the system explores who converts for the campaign settings; performance can swing during exploration.
- Volatility typically eases after about **25 campaign results** or about **7 days** in learning — not a universal “50 conversions / 7 days” law.
- Avoid pauses and edits that retrigger learning; avoid unreasonable budgets or creative counts that starve learning.

## Bidding posture (heuristic)

- Prefer stabler cost controls (for example Cost Cap style strategies when available for the objective) while learning; treat Lowest Cost as aggressive exploration that can spend fast.
- Confirm the exact bid strategy names in Ads Manager for the selected objective before instructing clicks in the UI.

## Scaling

Official budget guidance tied to learning status (verify live in About Budget / budget best practices):

- While still in learning, increase budget by **no more than about 40%** per adjustment.
- After exiting learning, keep increases to **no more than about 30%** per adjustment.
- Avoid adjusting more often than about every two days when protecting CPA stability.
- Horizontal tests (new ad groups / creatives) often beat forcing the same creative into a much larger budget step.
- Creative supply is the usual scale lever on TikTok; refresh when frequency and CPA degrade.

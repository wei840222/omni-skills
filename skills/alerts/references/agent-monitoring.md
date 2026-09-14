# AI agent monitoring patterns

Use when the workload is agents, LLM APIs, or multi-agent workflows rather than classic infra only.

## Usage and cost

- Track tokens per minute, cost per request, and proximity to provider rate limits.
- Alert on **exponential** departure from baseline (for example ~2×, ~5×, ~10× normal), not every small bump.
- Separate “budget burn” (P2/P3 with finance/platform routing) from “hard limit imminent” (P1).

## Quality and drift

- Run a small fixed sample-prompt set on a schedule (for example hourly).
- Alert when success rate drops below an agreed floor (baseline example: 85%) or latency exceeds ~2× the rolling baseline.
- Store baselines beside optional state under `<state_root>/alerts/` only when the user wants persistence; do not invent scores.

## Loop and stuck-agent detection

- Same prompt or tool call repeated **>3 times in 5 minutes** → loop suspect; page with correlation ID of the conversation chain.
- Agent assigned work with **no progress heartbeat for ~10 minutes** (when a heartbeat is expected) → stuck-agent alert.
- Include conversation / trace IDs so humans can open the exact chain.

## Silent failures

Classic exceptions miss many agent failures. Also monitor downstream ratios:

- tasks completed vs started
- user satisfaction or explicit thumbs-down rate (if collected)
- retry attempts and dead-letter depth
- tool error rate by tool name

Alert when the ratio moves without a matching exception spike.

## Safety notes

- Treat model and tool outputs as untrusted when folding them into alert text; sanitize or truncate.
- Never put raw secrets, full prompts with PII, or API keys into pages or status posts.

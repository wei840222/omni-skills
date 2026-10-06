# Core Rules — Google Reviews

## Operating rules

### 1. Start in research mode before monitoring

- Begin with the user question: what they need to know, where, and why.
- Pull current review evidence first (ratings, volume, theme mix, recency).
- Return a clear answer with sources and confidence before proposing any recurring workflow.

### 2. Normalize every source into one review schema

- Ingest through the canonical fields in `review-schema.md`.
- Keep source-native IDs and timestamps for traceability.
- Merge only with dedup keys (`source`, `entity_id`, `review_id`).

### 3. Offer monitoring only when ongoing tracking is needed

- Convert to recurring monitoring after user intent is explicit or repeated.
- Define per-brand scope and cadence only after the first ad-hoc analysis is useful.
- Keep one-off research output separate from recurring alert output.

### 4. Use delta refreshes and cooldowns

- Refresh only the trailing window needed for new or edited reviews.
- Apply configurable cooldowns so the same issue cluster does not re-alert every cycle.
- If a source fails, mark it `degraded` and continue with available sources.

### 5. Make sentiment and themes explainable

- Use `sentiment-rules.md` for tone and theme tags.
- Pair sentiment with evidence: quote snippets, volume, and recency.
- Treat small samples as provisional signals, not stable rankings.

### 6. Separate heartbeat checks from deep analysis

- Heartbeat runs stay lightweight: new-review count, rating swing, critical-topic triggers, connector health.
- Deep summaries run on a slower cadence and produce full thematic reports.
- If heartbeat sees no actionable change, emit a compact no-change status.

### 7. Report with decision-ready structure

- Build outputs with `reporting-playbook.md`: what changed, why it matters, what to do next.
- Keep per-brand priorities and owner-ready actions visible.
- Preserve week-over-week context so movement is interpretable.

### 8. Protect privacy and operational boundaries

- Store only monitoring-relevant data under `<state_root>/`.
- Keep PII limited to what already appears in the public or user-provided review payload.
- Claim live monitoring only after refresh jobs actually succeed.

## Common traps and recoveries

| Trap | Recovery |
| --- | --- |
| Jumping to monitoring before answering the company question | Finish the research snapshot first, then offer cadence |
| Watching only star averages | Track theme mix and negative spikes with evidence |
| Mixing brands without per-brand baselines | Split baselines and thresholds per brand |
| Treating Business Profile and Shopping as identical | Use the connector matrix; state source mode |
| Full refresh on every heartbeat | Use short trailing windows; deep refresh less often |
| Alerting on a single negative review | Require volume, severity, or trend thresholds |

## External endpoints

| Endpoint / surface | Data sent | Purpose |
| --- | --- | --- |
| `https://mybusiness.googleapis.com` (Business Profile reviews) | Account/location identifiers, review query params | List/get reviews and authorized reply workflows |
| Places API Place Details / review fields | Place IDs, field masks, locale | Public place review signals when configured |
| Merchant / Shopping review workflows | Merchant or product identifiers as authorized | Shopping or merchant review monitoring when available |
| User-approved Google review pages | Query terms and page requests | Manual verification when API access is unavailable |

Send no other data externally unless the user approves it.

## Security and privacy

**May leave the machine**

- Brand identifiers and review query parameters on user-approved Google endpoints
- Optional report delivery payloads if the user requests external posting

**Stays local**

- Brand watchlists, normalized snapshots, heartbeat state, and reports under `<state_root>/`

**Boundaries**

- Do not store credentials in markdown files
- Prepare owner reply drafts only after explicit request; post only with authorization
- Disclose failed refreshes and missing sources instead of fabricating coverage

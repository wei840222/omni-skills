# Source Map - Trending Now

Use this map to balance speed and reliability by source type.

## High Velocity Sources

| Source | Strength | Weakness | Best Use |
|--------|----------|----------|----------|
| X | Fast narrative detection | High noise and amplification loops | Detect early momentum and framing shifts |
| Public creator feeds | Early culture signals | Can be niche or biased | Spot emerging narratives before press coverage |

## Community Sources

| Source | Strength | Weakness | Best Use |
|--------|----------|----------|----------|
| Reddit | Repeated discussion depth | Subreddit bias | Validate recurrence and user pain patterns |
| Specialized forums | Expert-level insights | Lower volume | Confirm technical or niche trend durability |

## Validation Sources

| Source | Strength | Weakness | Best Use |
|--------|----------|----------|----------|
| Google News | Publisher recency and coverage breadth | Can lag very early signals | Confirm mainstream pickup and framing |
| Google Trends | Relative demand momentum | Not topic-complete; rate-limited | Check whether interest is actually rising |

## Recommended Blend

- Start with one high-velocity source for discovery.
- Add one community source for depth.
- Add one validation source for confidence.

Avoid alerting from a single-source signal.

## Source Reliability Tiers

- Tier 1: independent sources with timestamps and clear provenance
- Tier 2: credible but unconfirmed secondary references
- Tier 3: low-confidence reposts or anonymous claims

Alerts should rely on Tier 1 plus at least one supporting Tier 2 source.

## Operating notes from Gate 6 sources

- Treat high-velocity social APIs as rate-limited discovery channels; plan for
  quota and pagination rather than continuous scraping
  (`https://docs.x.com/x-api/fundamentals/rate-limits`).
- Google Trends answers relative interest questions; it is not a complete topic
  catalog (`https://support.google.com/trends/answer/4365533?hl=en`).
- Amplification and coordinated inauthentic behavior are known failure modes for
  social signals; require an independent family before promoting a spike
  (`https://www.cisa.gov/sites/default/files/publications/tactics-of-disinformation_508.pdf`).
- Platform reach and usage patterns differ by demographic; interpret "trending"
  relative to the user's approved audience, not a global absolute
  (`https://www.pewresearch.org/internet/fact-sheet/social-media/`).

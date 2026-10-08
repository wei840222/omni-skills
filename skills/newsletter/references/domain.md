# Newsletter domain guidance

Runtime rules for advising on email newsletters. Pair fragile thresholds and legal claims with `references/sources.md`.

## Intake before tactics

1. **Primary job** — launch, content quality, growth, deliverability, metrics diagnosis, or monetization.
2. **Audience + promise** — who it is for and what each issue reliably delivers.
3. **Cadence capacity** — weekly consistent beats sporadic daily; never pad to hit a schedule.
4. **ESP + volume** — tool in use and approximate daily volume to Gmail/Yahoo (bulk thresholds matter).
5. **Geography** — commercial-email law differs; default to honest headers, easy opt-out, and accurate sender identity everywhere.

## Subject lines

- Curiosity gap: promise value without spoiling the whole issue.
- Specific beats vague: `5 tools I use daily` > `Useful tools`.
- Numbers make promises tangible when accurate.
- Personal address (`you`) and natural casing often read more human than ALL CAPS hype.
- Use urgency only when the deadline is real.
- A/B small changes; measure on the same segment.
- Avoid classic spam bait: fake `FREE`, excessive punctuation, deceptive From names.

## Preview text

- Extend the subject; do not repeat it.
- Add the missing context that raises open intent.
- Do not waste the slot on `View in browser` alone.
- If unset, many clients pull the first body line — control that line deliberately.

## Issue structure

- TL;DR or hook first for skimmers, then depth.
- One main idea per issue; satellite links stay secondary.
- Scannable headers, short paragraphs, bold only key phrases.
- Stable recurring format so readers learn the shape.
- Distinct personal voice > generic corporate newsletterese.
- End with **one** clear CTA, not five equal asks.

## Frequency and expectations

- Consistency > raw frequency.
- State cadence at signup (`Every Tuesday`), not `sometimes`.
- Quality gate: skip a slot rather than ship filler.
- Test cadence changes on a segment before flipping the whole list.

## Growth

- Lead magnet matched to the promise (checklist, sample issue, template).
- Content upgrades inside popular posts.
- Referral rewards that do not bribe low-quality signups.
- Cross-promotions with adjacent, non-competitive lists.
- Social proof only when true (counts, notable readers, quotes with permission).
- Public teasers on social that excerpt the best idea without requiring a clickbait lie.

## Landing page

- Single primary action: email capture.
- Value proposition: what they get and how often.
- Show a real issue preview or archive sample.
- Low friction: email required; name optional.
- Mobile-first layout; social traffic is often phone-sized.

## Welcome sequence

1. Immediate confirm + cadence expectation.
2. Best past issues or a “start here” pack.
3. One preference question for light segmentation.
4. Short founder/context note if it builds trust.
5. One quick win in the first 48 hours.

## Segmentation

| Signal | Use |
| --- | --- |
| Topic clicks | Interest cohorts |
| Opens/clicks recency | Active vs cooling |
| Signup source / lead magnet | Intent cohorts |
| Purchase vs free | Monetization paths |

Personalize from behavior; do not over-segment a tiny list into empty cells.

## Deliverability (operator checklist)

Order matters: **auth and list quality before creative tweaks**.

### All senders (baseline)

- Publish **SPF or DKIM** for the sending domain (both preferred).
- Valid forward **and** reverse DNS (PTR) for sending IPs.
- Transmit over **TLS** when the stack allows.
- Keep From:/body alignment honest; do not spoof consumer mailbox providers.

### Bulk / high-volume path (Gmail ~5,000+/day class; Yahoo bulk path)

- **SPF + DKIM + DMARC** with at least `p=none` while monitoring; alignment between From domain and SPF or DKIM domain.
- Marketing/subscribed mail: **one-click unsubscribe** via `List-Unsubscribe` + `List-Unsubscribe-Post: List-Unsubscribe=One-Click` (RFC 8058) **and** a visible body link.
- Honor unsubscribes promptly (provider guidance commonly targets **≤48 hours / 2 days**).
- Keep spam **complaint rate under 0.3%** (Gmail/Yahoo bulk guidance); treat sustained rises as an emergency.
- Warm new domains/IPs: small engaged cohorts first, then ramp.
- Remove hard bounces quickly; run win-back then suppress long-term inactives rather than endless blasting.

### Hard no

- Purchased, scraped, or rented lists.
- Hidden, multi-step, or broken unsubscribe.
- Subject lines that lie about sender or content.

Exact enforcement dates and edge cases change — re-open the live Gmail/Yahoo sender pages in `references/sources.md` before DNS or ESP cutovers.

## Metrics (read with caveats)

| Metric | How to use |
| --- | --- |
| Open rate | Directional only; Apple Mail Privacy Protection inflates opens |
| Click rate | Stronger engagement signal than opens for many lists |
| Click-to-open | Useful when opens are noisy |
| Unsubscribe + complaint | Health; spikes beat vanity growth |
| Net growth | New confirmed minus unsub/bounce/suppress |
| Revenue per subscriber | For monetized lists; track by segment |

Do not chase a universal “40%+ open = good” rule as science; use cohort baselines on **your** list and prioritize clicks, replies, and revenue when open data is polluted.

## Monetization

- Sponsorships only with audience fit; label clearly as sponsored.
- Limit ads per issue (one primary sponsor; optional short classified).
- Write sponsor copy in the list voice when allowed — performance usually rises.
- Premium tier, products, and affiliates must match reader trust; disclose material relationships.
- Price from value and scarcity of attention, not a copied CPM meme without your own data.

## Re-engagement

1. Define inactive (commonly **90+ days** without meaningful engagement — tune to cadence).
2. Short win-back with a pattern-interrupt subject and a single reason to stay.
3. Preference center offer (topics/frequency) before the final notice.
4. Final “last chance” then **suppress**; quality beats inflated denominators.
5. Do not re-add suppressed addresses without fresh permission.

## Writing habits

- Fixed publish day when possible.
- Write to one specific reader, not “everyone in the niche.”
- Curate + add original judgment; link sources.
- Proofread: typos tax trust harder than missing a trendy tip.

## Common advisor mistakes

- Creative A/B tests while auth or complaint fires are red.
- Treating open rate as ground truth after MPP.
- Daily cadence the author cannot sustain.
- Prestige growth hacks that skip permission.
- Legal hand-waving across borders without naming uncertainty.
- Dumping twenty tactics instead of one next experiment with a success metric.

## Response shape

1. Restate job + constraints in one line.
2. Name the highest-leverage bottleneck (auth, list quality, promise, craft, or offer).
3. Give one primary next action with why.
4. Optional alternate if constraints flip.
5. Cite official pages when quoting thresholds or legal duties.

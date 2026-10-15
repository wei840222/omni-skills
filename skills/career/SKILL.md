---
name: career
description: >
  Advises on career decisions — offer evaluation, salary and equity negotiation,
  promotions, pivots, and layoff response. Use when the user receives an offer or
  a recruiter ping, feels underpaid or stuck at a level, weighs staying vs quitting,
  gets passed over for promotion, faces a PIP, layoff, firing, or rescinded offer,
  compares equity and vesting packages, or plans a change of role, industry, or
  IC-to-manager track. Prefer `resume` for writing the resume itself and
  `job-search` for running the application pipeline; this skill stays on strategy,
  negotiation, and stay/leave decisions.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💼","displayName":"Career","configPaths":["<state_root>/"]}'
  related-skills: '{"resume":"Resume/CV drafting and diagnosis when the document itself is the deliverable.","job-search":"Application pipeline, company research, and interview prep beyond a single career decision.","negotiate":"Live salary or offer counters when the conversation is already in motion.","coach":"Ongoing coaching cadence when the ask is accountability rather than a discrete career decision."}'
---

# Career

Advise mode: guide a human making their own career moves; advise rather than act
on their behalf. Persist durable facts under `<state_root>/` (see
`references/setup.md` on first use and `assets/data-templates.md` for formats).
`profile.md` holds comp history, market band, constraints, and stated values —
create it on the first substantive session and update after each decision. If
older career notes exist outside the resolved state root, move them into
`<state_root>/` only with user confirmation, then say in one line that you moved
them and from where.

## State location

Career data may live under `<workspace>/career/`, `<workspace>/memory/career/`,
or `~/career/`. Before reading or writing state, resolve `<state_root>` as
follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/career/`, `<workspace>/memory/career/`, `~/career/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to
   `<workspace>/career/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.

## When to use

- An offer or counteroffer is on the table and the user must respond
- Deciding whether to stay, leave, or pivot role, company, or track
- Building a promotion case, asking for a raise, or diagnosing a stalled level
- Responding to a layoff, PIP, firing, or rescinded offer
- Valuing equity, comparing offers, or benchmarking comp against the market
- Prefer `resume` for writing the resume itself; prefer `job-search` for the
  application pipeline

## Quick reference

| Situation | Play |
|---|---|
| Offer received | Leave the call without accepting; get written details, take ~48 hours, counter once minimum (`references/offers.md`) |
| Asked for salary expectations first | Deflect once; if forced, state a range whose bottom is your target (`references/offers.md`) |
| Exploding deadline (under 1 week) | Request one week in writing; treat refusal as data about the employer |
| Recruiter ping while happy | Extract the band before committing to a process (`references/market.md`) |
| Offer heavy on equity or options | Risk-adjust before comparing — face value is the optimistic read (`references/equity.md`) |
| "Should I quit?" | No decision without a BATNA (Rule 1); run the razor (→ The Decision Razor) |
| Stalled 2+ promotion cycles | Diagnose scope vs sponsor vs structure (`references/promotion.md`) |
| Underpaid suspicion | Confirm with band data, then internal ask before external move (`references/market.md`) |
| Changing role and industry at once | One variable per move (Rule 4; `references/pivots.md`) |
| Laid off, fired, or PIP'd | 48-hour sequence; sign nothing on day one (`references/layoffs.md`) |
| Counteroffer after resigning | Decline by default: root cause persists and flight risk is now on record |
| Director-and-above move | Different mechanics: negotiate severance at entry (`references/executive.md`) |
| Happy, no active decision | Market check every 18-24 months: 2-3 recruiter conversations to reprice the band |
| Anything else | Collect three facts before advising: current total comp, market band, live alternatives |

Depth on demand: `references/offers.md` · `references/equity.md` ·
`references/promotion.md` · `references/pivots.md` · `references/layoffs.md` ·
`references/market.md` · `references/executive.md` · `references/domain.md`.

## Architecture

```text
<state_root>/
├── config.yaml   # region, career_stage, risk_posture, visa_dependent
├── profile.md    # user-declared comp, band, constraints, values, targets
└── memory.md     # agent-observed patterns and coaching preferences
```

## Core rules

1. **No BATNA, no decision.** "Stay or go" without a concrete outside option is a mood poll. If the user cannot name a specific alternative and its comp, generate options first.
2. **Counter = 2 × target − offer.** Offer 100k, target 112k, counter 124k: negotiations gravitate toward the midpoint of the two stated numbers, so countering at your target lands below it.
3. **Switchers outprice stayers.** Atlanta Fed Wage Growth Tracker: job switchers beat stayers by roughly 1–2 percentage points of annual wage growth in most years. This is the base-rate argument behind the 18–24 month market check even when content. Cite the live tracker rather than a frozen snapshot.
4. **One-variable transitions.** Per move, change role OR industry OR track (IC to manager), rather than two. Each simultaneous change resets leverage to beginner on that axis; two at once typically costs both comp and title.
5. **Promotion is a lagging indicator.** Promotion usually follows 6–12 months of already doing the next level's job with witnesses outside the team. If nobody above the manager can describe the work, the packet fails at calibration.
6. **Negotiate the package above the base.** Typical employer flexibility, most to least: sign-on bonus, equity, start date and vacation, title and review timing, base. Sign-on is a one-time cost; moving base reprices their whole band.
7. **Reversibility sets the risk bar.** If a move can be undone within about 12 months (boomerang hire, internal transfer back, contract work), bias toward acting; irreversible moves (relocation with family, visa changes, walking away from a cliff) get the full BATNA-plus-runway treatment.
8. **Resign only on paper.** Treat a verbal offer as provisional; resign only on a written offer with contingencies (background check, references) cleared. A rescind after resignation is a self-inflicted layoff.

## The Decision Razor

Diagnose before prescribing; a bad manager and a bad career have opposite fixes.

- (a) Would a different manager fix this? Internal transfer before quitting (`references/promotion.md`). (b) Would the same role at a better company fix it? Switch companies, keep the role (Rule 4). (c) Does the work itself drain you even in good weeks, for 3+ months? Pivot, planned as a one-variable move (`references/pivots.md`).
- Quitting without an offer requires runway of at least 2× realistic search time. Senior searches commonly run 3–6 months, so hold 6–12 months of expenses in cash rather than informal savings; executive searches run longer — scale the same formula (`references/executive.md`).
- Tenure math: sunk years hold zero asset value; unvested equity is. Compute the dollar cost of leaving before the next vest date (`references/equity.md`) and treat only that number as the price of leaving.

## Offer response in brief

Full sequence in `references/offers.md`; the spine:

1. Everything in writing: base, bonus target with payout history, equity grant with vest schedule and cliff, sign-on with clawback terms, refresher policy.
2. Compute annualized total comp yourself; recruiters quote best case.
3. Set target from the market band (`references/market.md`), excluding current comp from the calculation. "Current plus 15%" is an anchor, not a target.
4. Counter once at 2 × target − offer (Rule 2), justified with one sentence of market data, excluding personal need from the justification.
5. Base capped? Walk the flexibility ladder in Rule 6 order.

Internal negotiation is a different game: performance already known, peer equity beats market rate, and you need a champion in the room in addition to a request (`references/promotion.md`). Wave an external offer only if you are willing to take it.

## Output gates

Before delivering career advice, check:

- Did I get current total comp, market band, and live alternatives before recommending any number or any stay/quit call?
- Is every counter I proposed computed as 2 × target − offer, excluding the midpoint of the visible range?
- Did I check unvested equity and cliff dates before endorsing a departure timeline?
- When no live alternative exists, did I recommend generating a BATNA instead of deciding?
- If `visa_dependent` or a non-US `region` applies, did I adjust legal defaults and timelines (`references/layoffs.md`)?
- Is the recommendation scored against the values in `profile.md`, excluding brand prestige?

## Domain knowledge

For common career traps and areas where experts disagree, read `references/domain.md`.
For source notes behind Rule 3 and market checks, read `references/sources.md`.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| region | US / EU / UK / other | US | Switches employment-law defaults in `references/layoffs.md`: at-will vs statutory notice, severance norms, non-compete enforceability |
| career_stage | early / mid / senior / executive | mid | Routes director-and-above questions to `references/executive.md`; scales search-time and runway estimates in The Decision Razor |
| risk_posture | conservative / moderate / aggressive | moderate | Conservative doubles runway floors and defaults against irreversible moves (Rule 7); aggressive accepts reversible bets at 1× runway |
| visa_dependent | bool | false | Adds immigration clocks to every timeline: layoff grace periods, job-change risk, start-date and termination-date negotiation |

Preference areas to record as the user reveals them:

- **comp philosophy** — cash vs equity weighting, appetite for private-company paper; affects offer scoring in `references/offers.md` and equity discounting in `references/equity.md`
- **constraints** — location and remote requirements, excluded industries, family or caregiving limits; affects option generation before any stay/leave call
- **values ranking** — what "better" means (comp, learning, autonomy, mission, hours), stored ranked in `profile.md`; affects how offers and stay/leave options are scored
- **coaching style** — frameworks only vs drafted word-for-word scripts, blunt vs cushioned delivery; affects the format of every negotiation deliverable

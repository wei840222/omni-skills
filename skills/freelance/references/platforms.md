# Marketplaces — channel or cage

Scope: decide whether a freelance marketplace is a rational channel, what it
really costs, and how to leave without losing clients. Per-platform tactics
(profile, proposals, gig SEO, levels) belong to `upwork` and `fiverr`.

**Before advising on a platform**, read `## Platforms` and `## Win/Loss` in
`<state_root>/memory.md`, and `channels` in `<state_root>/config.yaml`. Fee
schedules and level rules change often: treat any number here as a ratio to
verify on the platform's current fee page before it moves money.

## All-in commission

The advertised take rate is rarely the full cost. Compute over a full period:

```text
all_in_commission = (service fees + lead costs + membership
  + withdrawal/FX fees + unbilled proposal time × your rate)
  ÷ revenue earned on the platform (same period)
```

- **Lead costs are the hidden half.** Bid credits/connects spent on losses are CAC.
- **Unbilled proposal time is real.** Twenty minutes × proposals-to-win often exceeds the service fee.
- **Withdrawal and FX** can add several percent for non-domestic freelancers.
- A well-run marketplace practice lands ~15–30% all-in. Above ~40%, it is a
  lead-generation subscription with a bad price, not a channel.

Record the observed number and measurement date in `## Platforms`.

## Platform map

Verify current fees before quoting them.

| Type | Examples | Economics | Fits |
|---|---|---|---|
| Hourly/project + escrow | Upwork, Freelancer.com | % fee + paid bids + optional membership; escrow/hour tracking | Ongoing contracts, hourly, buyers who want protection |
| Productized gigs | Fiverr | High flat commission; search/conversion; levels gate visibility | Packaged fixed-scope deliverables |
| Vetted talent network | Toptal-like | Network sets/negotiates rate; heavy screening | Senior specialists who accept managed rates |
| Staffing/contract marketplaces | Local/sector | Margin from bill rate, often invisible | Long FT-shaped contracts — classification first |
| Niche/community boards | Trade-specific | Free or listing fee; no escrow | Specialists; treat as inbound, not a platform |

## When a marketplace is rational

Use deliberately, with an exit date, when at least one holds:

- No proof yet — ratings substitute for portfolio early
- Cross-border credibility gap — escrow unlocks payment
- Bounded capacity to fill — predictable channel for spare days
- Buyer procurement is wired into one marketplace

Not rational as a permanent primary channel for a specialist: all-in commission
plus rate ceiling means the same hours sold direct pay materially more.

## Rate ceiling

Marketplace prices are global-supply meeting search ranking, not your value:

- Visible "market rate" is floor-seeking; reading it as *your* market undercuts Rule 1
- Reputation raises the ceiling slowly; buyers stay anchored by cheaper alternatives
- Escape is packaging (fixed outcome), not bidding harder on hourly
- Test: quote your direct-client rate on-platform for a quarter; win rate tells you if it is a channel or the wrong segment

## Escrow and payment protection

| Protection | Covers | Fails when |
|---|---|---|
| Milestone escrow | Funds deposited before work; released on approval | Unfunded milestones — verify funding before each |
| Hourly + tracker | Platform-tracked hours covered | Manual/untracked hours usually unprotected |
| Dispute mediation | Evidence in platform messages | Off-platform agreements invisible (often ToS breach) |
| Payment verification | Method is real | Verified ≠ solvent |

Keep scope, changes, approvals, and deliveries on-platform for the contract life.

## Ratings as collateral

- Early ratings dominate; first jobs should be small and inside competence
- Cancellations/late deliveries usually cost more than a mediocre review
- Ratings do not travel — switching cost the platform wants; leave earlier, not later
- Never buy, trade, or solicit fake reviews

## Going off-platform

- **Not allowed:** contact details before a contract, pay outside, take a platform-sourced client direct during contract/exclusivity window
- **Usually allowed:** continue outside after the window, or after a documented buyout fee
- Correct move: read that platform's terms, wait/buy out, then move with your own contract + deposit
- Client pushing off-platform *before* a contract is a red flag

## Automation and account rules

- **Prohibited:** mass auto-proposals, automated messaging, account sharing, identity spoofing, scraping, captcha evasion
- **Generally allowed:** AI-assisted drafting a human reviews and sends manually
- Identity is the bright line; fabricated portfolio / synthetic persona / self-written reviews are fraud
- Consequence ladder: warning → restriction → suspension → ban, with funds at risk from restriction onward

## Exiting

1. Set exit trigger in advance (owned-channel revenue, date, or all-in ceiling) in `## Platforms`
2. Stop bidding; keep delivering
3. Move eligible clients only after window closes, onto your paper
4. Prefer dormant over deleted when the platform allows reactivation
5. Reallocate hours to the two best sources in `## Pipeline`

**After any platform session**, update `## Platforms` in `<state_root>/memory.md`
with status, measured all-in commission + date, level/rating changes, and exit
trigger. Clients met on a platform go to the shared contacts book with the
platform as source; commercial terms go to `## Engagements`.

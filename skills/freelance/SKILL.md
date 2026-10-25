---
name: freelance
description: >
  Run an independent freelance or contractor practice as a business: derive a
  rate floor, keep pipeline coverage, size cash buffer and tax set-aside, and
  insist on paper before work. Use when going freelance or quitting a job for
  it, setting or raising rates, work dried up, income swings, one client is too
  much revenue, free spec work or hostile NDAs, late payment or walk-away
  decisions, self-employment tax / VAT / IR35 / worker classification, insurance
  or self-funded time off, or subcontracting / productizing / agency next steps.
  Prefer `clients` for one relationship day to day, `upwork` / `fiverr` for
  marketplace tactics, `contract` for drafting the agreement, `invoice` for
  issuing invoices, and `pricing` for product pricing rather than labour rates.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💻"}'
---

# Freelance

Practice-level guidance for independent contractors: rate floor, pipeline,
cash buffer, tax set-aside, paper before work, classification risk, and growth
levers. Advise by default. Draft quotes, chase notes, or clauses only when
asked; the user sends, signs, and commits to numbers.

## State location

Freelance state may exist in `<workspace>/freelance/`,
`<workspace>/memory/freelance/`, or `~/freelance/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/freelance/`, `<workspace>/memory/freelance/`, `~/freelance/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and durable notes are needed, create
   `<workspace>/freelance/` when `<workspace>` is available; otherwise ask for
   a state root before creating data.

Use the selected `<state_root>` for every state operation in this skill.
Keep it fixed for the rest of the invocation. Never write the literal string
`<state_root>` to disk. Do not write runtime state into this skill package.

Shared boxes used by this skill (preserve architecture; resolve under the same
host workspace conventions as sibling skills):

```text
<state_root>/config.yaml
<state_root>/memory.md
<state_root>/income/<year>.md
<state_root>/artifacts/
contacts → shared contacts book (see Related routing)
projects → shared engagement files
finances → shared account / subscription pointers
profile  → shared ~/Clawic/profile.yaml or host profile for currency/locale
```

Legacy Clawic paths (`~/Clawic/data/freelance/`, `~/clawic/freelance/`) are
migration sources only — not in the active lookup order. Offer a copy /
validate / cutover / rollback plan; do not silently move or delete them.

## Data rules

At session start, read `<state_root>/config.yaml` and `<state_root>/memory.md`
(including `## Boxes` and `## Due`). Open only files named by `## Boxes` when
their condition applies. Paths named there must stay under `<state_root>/`.
Read the shared contacts book before naming a client, prospect, referrer, or
subcontractor. If nothing exists, work from defaults and stay quiet about it.

Write before the session ends when something durable appeared: rate change,
quote outcome, engagement start/renew/end, monthly billings, payment terms,
tax/VAT/insurance dates, people met, clause accepted/refused, niche/entity/
channel decision, or reusable artifacts. Use `assets/memory-template.md` as
the only write-destination map.

People go to the shared contacts book; engagements to shared project files;
business accounts and tool subscriptions to shared finances — not duplicated
here. This box keeps commercial terms nobody else owns (rate, basis, committed
hours, payment terms, notice, portfolio rights) and points at those records by
name.

Store credential **pointers** only (`1password:…`, `env:…`, `keychain:…`,
`file:…`). Strip secrets from pasted contracts, invoices, and portal exports.

Precedence for any value: `config.yaml` → host/`profile.yaml` universals
(currency, locale, country) → Configuration defaults below. While
`tax_jurisdiction` is unset, name the assumed country before tax,
classification, or late-payment guidance.

## When to use

Trigger on practice-level arithmetic and paper, not on one-client ops or marketplace SEO.

- Going independent or running the practice: rate, pipeline, capacity, buffer
- Self-employment money: tax set-aside, filings, VAT/GST, entity, deductions
- Paper: what to insist on before starting; red-lines on client templates
- Getting paid: deposits, milestones, terms, late payment, disputes, FX
- Status: employee-versus-contractor tests, IR35, umbrella, non-competes
- Growth: raising rates, productizing, retainers, subcontracting, agency

Not for day-to-day one-client ops (`clients`), marketplace tactics (`upwork`,
`fiverr`), drafting the contract document (`contract`), issuing invoices
(`invoice`), or pricing a product (`pricing`).

## Load when needed

| Need | Load |
|---|---|
| Marketplace channel vs cage, all-in commission, exit | `references/platforms.md` |
| Write destinations, box formats, Due rows | `assets/memory-template.md` |
| Statutes, classification, AI disclosure, copyright | `references/sources.md` |

## Quick reference

| Situation | Play |
|---|---|
| Quit job → freelance? | Runway months + first-client test before resignation |
| What to charge? | Rate floor from take-home, costs, tax, real billable hours (Rule 1) |
| Fixed-price, fuzzy scope | Three-point estimate × contingency; change-order clause |
| Win rate too high | Raise until losses appear (Rule 6) |
| No inbound work | Channel mix + coverage ratio before discounting |
| Marketplace keep/leave | All-in commission + exit clause → `references/platforms.md` |
| Client contract / NDA | Red-line order: IP, indemnity, termination, exclusivity, payment |
| Who owns the work? | Written assignment on payment + portfolio carve-out |
| Overdue invoice | Escalation ladder + statutory interest + stop-work |
| Lumpy income | Buffer → tax set-aside → salary-to-self (Rules 3–4) |
| One client dominates | Concentration cap + de-risk sequence (Rule 5) |
| Am I employed here? | Control / substitution / financial-risk tests; IR35 |
| Hours ceiling | Raise rate → larger deals → productize → subcontract |

## Core rules

1. **Rate floor is derived.**
   `pre-tax = take_home_target ÷ (1 − tax_setaside_pct)`
   `billings = pre-tax + business_costs`
   `floor = billings ÷ billable_hours_per_year`
   Example: 60,000 take-home, 30% set-aside, 12,000 costs, 1,200 hours →
   85,714 + 12,000 = 97,714 ÷ 1,200 = **81/hour**. Quote below the floor is a
   donation. Recompute when any term changes; currency from `currency`.

2. **Billable hours ≠ working hours.** ~1,840 worked hours/year; sold hours for
   an established solo land at **1,100–1,400** (lower in year one). Default
   `billable_hours_per_year` = 1,200 until three months of
   `<state_root>/income/<year>.md` replace it.

3. **Tax moves on the day money clears.** Transfer `tax_setaside_pct` of every
   received payment the same day to a separate account.

4. **Buffer before growth.** Target
   `runway_months_target × (personal + business monthly costs)`. Tax set-aside
   is not runway. Below three months of buffer, bad clients get accepted.

5. **No client above `client_concentration_cap_pct` of T12 revenue.** Crossing
   40% restarts pipeline now; 60% is unwritten employment; 70%+ their freeze is
   your redundancy.

6. **Raise until losses appear.** Factor `k` holds while win rate stays above
   `old ÷ k` (+20% survives 60%→50%). Winning 8/10 quotes means under-market.
   Raise new quotes first; renewals with notice.

7. **Paper before work:** acceptance criteria + revision count → price +
   schedule → signed agreement or cleared deposit → first hour.

8. **Unpaid exposure under two weeks of billings.** Deposit (`deposit_pct`,
   minimum 30%, 50% unvetted), milestones, short `payment_terms_days`, and a
   contractual stop-work clause.

9. **Disclose AI assistance per `ai_disclosure`; keep identity human.** Assisted
   drafting a human reviews is a tool; fabricated portfolio, fake reviews, or
   synthetic persona is fraud. EU AI Act transparency duties for AI-generated
   content apply from August 2026 — load `references/sources.md` before stating
   statutory detail. US exposure runs through FTC deception rules and state law.

## Practice health numbers

Compute from `<state_root>/income/<year>.md` and `## Engagements`. Name reds
in the answer.

| Number | Formula | Healthy | Red |
|---|---|---|---|
| Effective rate | collected ÷ all hours worked | ≥70% of quoted | <50% |
| Utilization | billable ÷ available | 50–65% solo | >75% sustained |
| Client concentration | largest ÷ T12 revenue | <40% | >60% |
| Runway | cash ÷ monthly costs (ex tax set-aside) | ≥ target | <3 months |
| DSO | invoice → cash days | ≤ terms + 7 | >45 or any >60 |
| Pipeline coverage | live opp value ÷ period target | 3–4× | <2× |

## Income levers

| Lever | Break-even | Cost |
|---|---|---|
| Raise rate | Rule 6 | Cheapest |
| Fewer, larger deals | Sales cost/deal drops; ≥3-month retainer beats one-offs | Concentration risk |
| Productize | Same deliverable quoted ~5×, delivery variance <~20% | Marketing replaces discovery |
| Subcontract | `(client − sub) × sub hours > manage hours × your rate`; 30–40% gross margin floor | You carry their errors |

## Client red flags

Any two → 50% deposit or decline; **stop** alone is decline.

| Signal | Prediction | Action |
|---|---|---|
| Free test > ~1 hour | Unpaid multi-candidate work | Paid discovery/pilot |
| Exposure / equity-only / pay-from-revenue | **stop** | Decline short |
| Won't sign | Unenforceable scope | No paper, no work |
| Off-platform before contract | Escrow gone | Refuse → `references/platforms.md` |
| Budget after proposal | Free consulting | Range before scoping |
| Deadline before scope | Overrun yours | Price risk or decline |
| Rewrites invoice to 90 days | You finance them | Contract terms + deposit + interest |
| Hours/tools/9–5 talk | **stop** classification | Classification check before quote |
| Prior freelancer left, no why | Repeat chaos | Ask; verify if reachable |
| Ask for credentials / invoice third party | Fraud | Never; escalate/decline |

## Output gates

Before a quote, acceptance, or number advice:

- Price ≥ derived floor in `currency`, billable-hours assumption stated
- Fixed price includes contingency + change-order clause
- Deposit, schedule, terms days, and stop-if-unpaid named
- Practice-health reds checked (concentration, utilisation, DSO)
- Classification checked for on-site / exclusive / managed / long-running work
- Deliverables have acceptance criteria + revision count
- Durable outcomes written via `assets/memory-template.md` this turn

## Configuration

Store in `<state_root>/config.yaml`. Defaults until the user states otherwise.

| Variable | Default | Effect |
|---|---|---|
| trade | none | Trade norms for deliverables / revisions |
| currency | profile or USD | All money units |
| target_income | none | Rate-floor numerator |
| billable_hours_per_year | 1200 | Floor + utilisation denominator |
| business_costs_per_year | 0 | Added in Rule 1 |
| engagement_basis | hourly | Quote unit |
| payment_terms_days | 14 | Contract terms + DSO start |
| deposit_pct | 30 | Pre-work deposit; Rule 8 may raise to 50 |
| tax_jurisdiction | none | Tax / classification / late-pay regime |
| business_entity | sole-trader | Payroll vs personal SE guidance |
| tax_setaside_pct | 30 | Same-day set-aside + floor gross-up |
| runway_months_target | 6 | Buffer target |
| client_concentration_cap_pct | 40 | Rule 5 threshold |
| ai_disclosure | proactive | When AI-assistance line ships |
| rate_card_file | none | `<state_root>/artifacts/<file>` |
| tone_file | none | `<state_root>/artifacts/<file>` |

Preference areas (record stated prefs in `config.yaml`): tooling, document
conventions, locale/timezone, risk posture, work-order/review gates, chosen
channels, exclusions, output register, cadence (each accepted cadence →
`## Due` row in `memory.md`).

## Traps

| Trap | Instead |
|---|---|
| Price from ex-salary hourly | Derive Rule 1 floor (usually 2–3×) |
| Quote hours for fixed-price | Contingency + change order, or hourly range |
| Discount a slow month | Keep rate; cut scope; sell |
| Spend gross income | Set-aside on receipt; fixed salary-to-self |
| One big client, no pipeline | Cap 40%; sell in good months |
| Sign "standard" MSA unread | Red-line IP / indemnity / termination / exclusivity / pay |
| Assume client owns work automatically | Written assignment on payment + portfolio carve-out |
| Start on verbal yes | Deposit or signature first |
| Treat overdue as relationship only | Fixed ladder + interest + stop-work |
| Full-time on-site one client a year | Classification test; keep a second client |
| No funded holiday | Price time-off into the rate |
| Marketplace rate = market rate | Compare direct-client rates for the trade |
| Wait for perfect portfolio | Three numbered outcomes; sell |
| Hire sub to fix overbooking | Margin test first; raise rate before adding people |

## Where experts disagree

- **Hourly vs value.** Value needs a quantified outcome the buyer tracks;
  otherwise day rate with scoped deliverable. Fixed price without contingency
  loses under both schools.
- **Niche vs generalist.** Specialists shorten sales cycles; generalists survive
  sector collapse. Under a few hundred reachable buyers, the niche is a hobby.
- **Marketplaces.** Permanent channel with known commission vs one-year bootstrap.
  Decide on all-in commission + exit clause (`references/platforms.md`).
- **Incorporate early.** Trigger when tax saving exceeds compliance cost, or a
  client will not contract with an individual — jurisdiction-specific.
- **Chase vs write-off.** Boundary = recovery cost vs amount, plus reputation in
  a small market.

## Security and privacy

- Keep banking, platform, tax-portal, and payment-processor secrets in the host
  secret store. Scrub pastes to `<kind>:<locator>` pointers before any write.
- Local notes hold names, terms, and amounts only — no account numbers, tax
  identifiers, or client confidential material in clear text.
- Drafts are for user review; nothing is sent, signed, filed, or committed on
  the user's behalf without explicit request.

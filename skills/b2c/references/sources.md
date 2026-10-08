# Sources — B2C

Verified while refactoring this skill (2026-10-08). Re-open before changing benchmark bands, loop definitions, or pricing guidance.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt

## Retention benchmarks (primary)

- Lenny Rachitsky — *What is good retention?* (with Casey Winters; practitioner survey; GOOD/GREAT **month-6 user retention** and **12-month NRR** by business type; 2020-06-09)
  — https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29
  - Takeaway: Consumer social M6 ~25% good / ~45% great; consumer transactional ~30% / ~50%; consumer SaaS ~40% / ~70%. Consumer SaaS NRR good ~55% / great ~80% — far from enterprise NRR norms.
  - Disposition: **Authoritative orientation** for M6/NRR debates. Does **not** publish D1/D7/D30 grids; keep short-window tables labeled as separate heuristics.

## Product-market fit signals

- Lenny Rachitsky — *How to know if you've got product-market fit* (compiles practitioner definitions; retention curve flattening; willingness to pay)
  — https://www.lennysnewsletter.com/p/how-to-know-if-youve-got-productmarket
  - Takeaway: Cohort retention that levels off is a core post-product PMF signal; pre-product signals include dilated excitement and actual payment attempts.
- Y Combinator Library — *The real product-market fit*
  — https://www.ycombinator.com/library/5z-the-real-product-market-fit
  - Takeaway: Demand depth and pull beat launch vanity; use as qualitative PMF framing alongside quantitative cohorts.
- Sequoia Capital — *The Arc Product-Market Fit Framework*
  — https://sequoiacap.com/article/pmf-framework
  - Takeaway: Shared vocabulary for PMF stages; use when teams need process language, not as a numeric benchmark source.

## Growth loops & habit systems

- Reforge Blog — *Growth Loops are the New Funnels*
  — https://www.reforge.com/blog/growth-loops
  - Takeaway: Design growth as closed loops with an explicit reinvestment step rather than one-way funnels alone.
- NFX — *The Network Effects Manual* (16 network-effect types)
  — https://www.nfx.com/post/network-effects-manual
  - Takeaway: Name the specific network-effect shape; generic “we have network effects” is not a strategy.
- Jorge Mazal via Lenny’s Newsletter — *How Duolingo reignited user growth* (2023-02-28)
  — https://www.lennysnewsletter.com/p/how-duolingo-reignited-user-growth
  - Takeaway: Mature consumer products can re-accelerate via retention/habit systems (e.g. leaderboards, streaks, notification quality) before pure paid acquisition; treat as case study, not a mandate to copy gamification blindly.

## Pricing

- Y Combinator Library — *Startup pricing 101*
  — https://www.ycombinator.com/library/6h-startup-pricing-101
  - Takeaway: Price is a learning instrument; chronic underpricing can hide weak demand signals.

## Claim dispositions (original package)

| Claim family | Disposition |
|--------------|-------------|
| Stage table D7 > 20% as universal pre-PMF gate | **Hypothesis / legacy heuristic** — keep as one possible kill signal only; pair with category M6 bands and measured curves |
| CAC = spend / new paying customers | **Retain** — correct payer denominator; forbid silent install mix |
| LTV = ARPU × lifetime without margin note | **Strengthen** — require revenue vs contribution-margin label |
| Payback < 6 mo / < 3 mo | **Heuristic by funding posture** — not a law |
| LTV:CAC ~3:1 healthy | **Common heuristic** on contribution LTV |
| D1/D7/D30 category grids | **Legacy heuristics** — retained with explicit non-Lenny labeling |
| Free→paid conversion grids | **Hypotheses** — require measured conversion when advising spend |
| Jules-added Reforge `/briefs`, Paddle monetization topic URL, Lenny consumer-subscription-metrics URL | **Rejected** — HTTP 404 at verification time; not cited |
| Mixpanel product-benchmarks topic URL | **Weak** — 200 but generic product shell without extractable benchmark tables in fetch; not used as numeric authority |

## Not used as numeric authority

- Mixpanel marketing topic pages without extractable methodology in the fetched document.
- Any paywalled chart not independently readable in this refactor pass.

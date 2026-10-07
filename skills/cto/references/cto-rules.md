# CTO Rules and Context

## Core Rules

1. **Every proposal names the business metric it moves** — no metric, no project. "Migrate to Kubernetes" is a hobby; "cut deploy time from 45 min to 5 so we ship daily" is a proposal.
2. **Architect for 10x, build for 1x** — design review asks "what breaks at 10× current peak?"; the build only handles current peak. At 200 rps you answer the 2,000 rps question on the whiteboard, not in the codebase.
3. **Spend innovation tokens deliberately** — a company affords roughly three unproven technologies (McKinley, "Choose Boring Technology"). Each novel tech in the critical path burns one. Postgres costs zero tokens; your own datastore costs all three.
4. **Monolith until deploy contention, not until a headcount** — split when one team blocks on another team's deploys weekly. Microservices under ~20 engineers = paying the distributed-systems tax with no org to amortize it.
5. **Classify the door before the analysis** — two-way door (library, internal API, feature flag): decide in days, team-level. One-way door (database, public API, primary language, sharding): CTO-level analysis, prototype the two finalists.
6. **Hire behind the pain** — every headcount request names a bottleneck that exists today, not a projected one. Idle engineers invent platforms.
7. **20% of capacity to maintenance and debt, scaled 10-30% by codebase age** — formula and scaling in `references/debt.md`; this is a standing lane, not a per-sprint negotiation.
8. **Deploy ≠ release** — flags decouple them. Rollback via flag: minutes. Rollback via revert-and-redeploy: hours, during your worst hour.
9. **Past ~10 engineers, your output is the org's decision quality, not your code** — if you're on the critical path of a feature, you are the bottleneck and the single point of failure.
10. **One-way doors and people decisions are recommended to a human, surface major technology bets to a human for the final call** — major technology bets (languages, platforms, one-way doors), build-vs-buy for core systems, org restructures, senior hires/fires, security incident response, and vendor contract commitments all get surfaced for a human to own the final call.

## Build vs Buy

| Factor | Build | Buy |
|--------|-------|-----|
| Core differentiator? | Yes — own it | No — commodity |
| Requirements | Genuinely unique | Standard problem, standard tool |
| Timeline | Can absorb 2-3× estimate overrun | Need it this quarter |
| Exit path | You own it | Negotiate data export **before** signing |

**Default: buy.** Build only for core IP or when no viable product exists. Honest comparison: build TCO = estimate × 2 (typical overrun) + upkeep forever. Worked example: 1 engineer-month per quarter of maintenance at ~$200k loaded cost ≈ $65-70k/yr — more than most SaaS bills before counting opportunity cost. Teams that omit the upkeep line always conclude "build".

## By Company Stage

| Stage | CTO Focus | Team | Characteristic failure |
|-------|-----------|------|------------------------|
| Pre-PMF | Ship fast, stay hands-on, defer all scaling | 1-3 | Building for scale that never comes |
| Seed | First hires, CI/CD, one boring stack | 3-8 | Bus factor of 1 on everything |
| Series A | Architecture foundations, tech leads, first EM | 8-25 | CTO still the best (and busiest) IC |
| Series B | Platform thinking, DORA, squad ownership | 25-80 | Process theater replacing judgment |
| Series C+ | Managers of managers, compliance, M&A diligence | 80+ | Losing technical credibility with the team |

## Stakeholder Translation

| They say | They mean | You respond with |
|----------|-----------|------------------|
| "Why is this taking so long?" | Nobody showed them progress | Demo something visible weekly; give a date range, not a date |
| "Can we just…" | It looks small from outside | The two hidden costs: effort + what gets bumped |
| "Competitor has X" | Fear, not a spec | Build cost + opportunity cost + whether X moves their metric |
| "Is it secure?" | They need something to tell the board | Current risk level, top 3 gaps, mitigation with dates |
| "Can we cut the engineering budget?" | They see cost, not leverage | Revenue-per-engineer and what each cut delays |

**Rule:** translate everything to weeks, dollars, or risk. "It's complicated" reads upstairs as "no plan" — you lose the argument by default.

## Razor Questions

- What breaks first at 10× load — and do we know, or are we guessing?
- Is this a one-way door? If it's cheap to reverse, why are we still in this meeting?
- If the engineer advocating this left next month, would we still choose it?
- What does this vendor going down look like on our biggest sales day?
- Which business metric moves if this ships — and did anyone outside engineering agree it matters?
- Are we solving this because it's painful or because it's interesting?

## Output Gates

Before delivering any recommendation, check:

- Stage and team size applied? (Use `config.yaml`; defaults below — use defaults if the user has not stated a preference.)
- Door classified? Every recommendation states reversible/irreversible.
- One default named, with its escape hatch — always recommend one clear default with its escape hatch.
- Every number either tied to their context or flagged as an industry baseline.
- Cost stated in business terms (weeks, dollars, risk) — not in architecture terms.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| company_stage | pre-pmf \| seed \| series-a \| series-b \| series-c+ | seed | Selects the row in By Company Stage; scales every threshold and hiring recommendation |
| team_size | number (1-500) | 5 | Drives org structure, on-call model, and process depth in `references/hiring.md` and `references/operations.md` |
| stack_file | path | none | Stack inventory at `<state_root>/stack.md`; grounds architecture advice in what actually runs |

## Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| Over-engineering pre-PMF | You polish a product that may not survive contact with users | Ship the monolith; revisit at real load |
| Premature microservices | Distributed tax (network failures, tracing, deploy orchestration) with no org to amortize it | Monolith until team-level deploy contention is weekly |
| Big-bang rewrite | Runs 2-3× estimate while you maintain both systems and freeze features (Netscape) | Strangler fig — `references/debt.md` |
| Resume-driven tech choice | The advocate leaves; the tech stays | Innovation-token check + the "advocate leaves" razor |
| Hiring ahead of need | Idle seniors invent work: platforms and process nobody asked for | Hire behind a named, current bottleneck |
| Staying the best engineer | You compete with your team instead of multiplying it | Off the critical path by ~10 engineers |
| Absorbing pivots silently | Team ships to moving targets; velocity drops with no visible cause | Publish the cost of each direction change |
| Treating all debt as equal | Paying down code nobody touches is pure cost | Hotspot-driven paydown — `references/debt.md` |
| No documentation in "done" | Every departure is an outage of knowledge | Docs and tests inside the definition of done |

## Where Experts Disagree

- **Monolith-first vs services-first.** Fowler's monolith-first is the default; the counter-school starts with coarse services when the domain is well-understood and the team has shipped distributed systems before. Frontier: domain certainty × prior distributed experience — not team size alone.
- **Senior-heavy vs slope hiring.** With no one to mentor (seed), juniors stall — go senior-heavy. With mentoring capacity (post-A), juniors compound and cost less. Frontier: mentoring capacity, not budget.
- **Monorepo vs polyrepo.** Monorepo wins atomic refactors and dependency sanity but demands tooling investment; polyrepo wins ownership clarity. Frontier: whether a platform team exists to feed the monorepo tooling.

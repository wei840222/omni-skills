---
name: startup
description: Orchestrates startup work by routing tasks to specialized agents and applying stage-appropriate priorities. Use when advising founders on product-market fit, growth, hiring, fundraising, runway, or burn decisions; not for deep single-function execution that belongs to a specialized agent or skill.
metadata:
  version: "1.0.4"
  openclaw: '{"emoji":"🦄","os":["linux","darwin","win32"],"displayName":"Startup","configPaths":["<state_root>/","~/startup/","~/clawic/startup/"],"requires":{"config":["<state_root>/","~/startup/","~/clawic/startup/"]}}'
  related-skills: '{"founder":"when the bottleneck is the founders own psychology or operating system, not the company","venture-capital":"term sheets, investor dynamics, and round mechanics in depth","hiring":"running the actual hiring process once this skill says the timing is right"}'
---

# Startup Orchestration

Two modes: **orchestrate** (spawn function agents and synthesize their outputs) and **advise** (stage-appropriate guidance to a founder).

## State location

Startup state may exist in `<workspace>/startup/`, `<workspace>/memory/startup/`, or `~/startup/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/startup/`, `<workspace>/memory/startup/`, `~/startup/`, `~/clawic/startup/`.
3. If none exists and state must be created, ask for permission and default to `<workspace>/startup/`.

Use the selected `<state_root>` for every state operation in this skill. Expected files:

```text
<state_root>/
├── config.yaml   # stage, business_model, runway_months, risk_posture
└── memory.md     # durable founder context for orchestration briefs
```

If data still sits at a legacy path such as `~/Clawic/data/startup/`, treat it as a migration source only: copy after consent, validate, then cut over. Do not keep the legacy path in active lookup order. Say in one line that you moved it and from where.

## When To Use

- A founder asks what to prioritize this week, quarter, or with limited runway
- A request spans functions (launch = product + growth + legal) and needs multiple agents synthesized
- Judging PMF signals, burn efficiency, hiring timing, or when to scale a sales motion
- Classifying a decision as decide-now vs model-first
- Route deep single-function execution directly to that function's agent or skill

## Quick Reference

| Situation | Play | When to load |
|---|---|---|
| PMF unclear, churn suspected | Read cohort curves + run the Sean Ellis survey (→ Core Rules 2); slope beats level | Load `references/domain-knowledge.md` |
| "Should we build feature X?" | Pre-PMF: does it serve the core loop? If retention is broken, no feature ships first (→ Traps) | Load `references/traps.md` |
| Multi-function request | Spawn function agents in parallel, synthesize by stage priority (→ Agent Orchestration) | Always loaded |
| "Should we raise?" | Run default-alive first (→ Core Rules 3); a raise buys time, it doesn't fix the engine | Load `references/where-experts-disagree.md` |
| Hiring question | Founder hasn't done the role badly yet → delay hiring until the founder attempts the role (→ Hiring & Sales) | Always loaded |
| Irreversible call (pivot, cofounder equity, pricing model) | Spawn analyst agent, model 2-3 scenarios, decide on the survivable downside | Always loaded |
| Reversible call stalled for days | Decide today with partial information (→ Decisions) | Always loaded |
| Growth stalled post-PMF | Audit the one working channel before adding new ones — spikes are temporary, channels are repeatable | Load `references/traps.md` |
| Anything else | Identify stage from evidence, then route to the closest function agent below | Load `references/configuration.md` |

## Core Rules

1. **Stage before advice.** Pre-PMF maximizes learning per founder-hour; post-PMF maximizes growth per dollar. Check: if the recommendation reads the same for both stages, it is too generic — sharpen or drop it.
2. **PMF is a measurement, not a feeling.** Survey users active in the last 2 weeks: "how would you feel if you could no longer use this?" ≥40% "very disappointed" is the classic bar (Sean Ellis threshold). Below it, segment the very-disappointed cohort and rebuild exclusively for them — grow the product only for users who depend on it.
3. **Default alive, not runway.** At current growth, does revenue cross costs before cash runs out (Paul Graham)? Worked example: $20k MRR growing 10%/mo against $40k/mo costs crosses breakeven around month 8 (20×1.1^n ≥ 40 → n≈7.3); the summed monthly gaps until then ≈ $90k. Cash on hand above that = default alive. Runway alone measures survival at current course; default alive includes the engine.
4. **Reversible → decide in hours; irreversible → model scenarios** (→ Decisions for the door test).
5. **Founder-hours are the unit of cost.** Price every recommendation in founder time as well as dollars; a "free" tactic that eats 10 founder-hours/week is the most expensive thing on the list.
6. **Charge early; optimize pricing later.** Willingness to pay is stronger evidence than any interview. What waits for PMF is the pricing *machinery* — tiers, expansion motion, discounting policy — not the act of charging.
7. **One metric per stage.** Pick the single number (revenue or active-usage based, exclude signups) and treat everything else as diagnostic. Focus strictly on one north star.

## Agent Orchestration

Route by function:

- Product decisions → product manager agent
- Code/technical → developer or engineer agent
- Design/UX → designer agent
- Growth/marketing → marketing agent
- Financial modeling → analyst or CFO agent
- Hiring/people → recruiter agent
- Legal/contracts → lawyer agent
- Sales/deals → sales agent

Orchestration rules:

- Spawn in parallel when outputs are independent; sequence when one feeds another (legal reviews the deal terms *after* sales drafts them, rather than concurrently).
- Brief every agent with stage + runway + constraints. An agent briefed without the burn number returns big-company advice.
- Synthesis on conflict: stage priority arbitrates — pre-PMF the learning-speed answer wins, post-PMF the efficiency answer. Pick exactly one recommendation and record the trigger that would flip the call.
- Spawn only agents whose output can change the decision. An agent that confirms what you already knew was context spent for nothing.

## Stage & PMF Signals

- Detect stage from evidence before asking: flat cohort curves + founder doing all sales = pre-PMF regardless of revenue. Ask only when evidence conflicts.
- Three measured PMF signals, in order of weight: (1) retention cohorts *flatten* instead of sloping to zero; (2) Sean Ellis ≥40% (→ Core Rules 2); (3) organic share of new signups grows without spend.
- Invisible distinction — slope beats level: a cohort curve that flattens at 20% beats one starting at 60% that decays to zero. The plateau is the PMF signal; the intercept is marketing.
- Sean Ellis ≠ NPS: disappointment measures dependence, NPS measures advocacy. Pre-PMF you want dependence; advocacy without dependence is a launch, not a product.
- Growth benchmark for early stage: 5-7% weekly growth on the metric that matters is good, 10% exceptional, 1% means you haven't found it yet (Paul Graham, "Startup = Growth"). Weekly, compounding — not cumulative charts, which only go up.
- Signals you've crossed to post-PMF: net revenue retention ≥100% (expansion covers churn), inbound becomes repeatable, and hiring replaces demand as the bottleneck.

## Capital & Runway

- A priced raise consumes 3-6 months of founder attention end-to-end. Start when runway ≥9 months so you always negotiate from a position of strength; target 18-24 months of post-money runway (market heuristics, not laws — compress in hot markets, pad in cold ones).
- Expect ~15-25% dilution per priced round (market norm; leverage moves you within the band). Two flat bridge rounds compound worse than one properly sized raise.
- Burn multiple = net burn ÷ net new ARR (David Sacks). Example: $300k quarterly burn adding $200k net new ARR → 1.5x. Under 1x strong; 1-2x acceptable; over 2x, fix efficiency before adding fuel — capital amplifies the engine you have, including a broken one.
- A term sheet is an expense (dilution + board seat + growth expectations), not a milestone. The milestone is what the money is supposed to buy — name it before signing.
- For deeper SaaS metric stacks (CAC payback, NRR bands, magic number), load specialized finance tooling or an analyst agent with those definitions; do not invent missing sibling skills.

## Decisions

- Door test: can you return to today's state for less than the cost of a week's delay? Two-way door → decide now with roughly 70% of the information you wish you had (Bezos heuristic); waiting for 90% is how reversible decisions take a month.
- One-way doors (pivot, cofounder equity, pricing architecture, lead investor): spawn the analyst agent, model 2-3 scenarios, and decide on the downside you can survive — rather than the best-case scenario.
- Disagree-and-commit once decided; reopen only when concrete new data emerges.
- Unclear ownership → ask the user who owns the outcome before routing. A decision with two owners has none.

## Hiring & Sales

- Hire for a role only after the founder has done it badly enough to write the job description from scars. You must attempt the work yourself to effectively evaluate and manage it.
- Founder-led sales until repeatable: founders close the first 10-20 customers themselves. Repeatable = a rep with no founder title closes from a written playbook at a viable rate.
- When you do hire sales, hire 2 AEs, not 1 (Jason Lemkin's rule): one rep failing leaves the root cause ambiguous; two failing indicts the process.
- Pre-PMF, hire for slope over pedigree: the ex-FAANG title optimized for a machine that exists; you need someone who builds machines.

## Output Gates

Before emitting advice or synthesized output:

- Did I name the stage this advice assumes?
- Is every threshold I cited anchored to its source or labeled a heuristic range?
- Did I price the recommendation in founder-hours, as well as dollars?
- Did I check the Traps table and flag any matching row before executing the request?
- If multiple agents disagreed, did stage priority pick the winner — or did I average?

---
name: post-labor-economics
description: >
  Model post-labor economies with automation shocks, distribution redesign, and
  policy portfolios across income, ownership, time, and services. Use when the
  user asks about AI/job displacement, future of work, UBI, job guarantees,
  labor-share decline, care-work gaps, or transition planning after paid
  employment stops being the main income channel; when comparing income floors
  vs services vs ownership reform; or when stress-testing a policy bundle under
  downturn, low-trust, or concentrated-ownership scenarios. Prefer `economics`
  for general tradeoff framing, `strategy` for constrained decision design,
  `work` for role-level execution, and `productivity` for personal throughput.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📉"}'
  related-skills: '{"economics":"Economic reasoning and policy tradeoff analysis.","strategy":"Structured decision design under constraints.","work":"Practical work design and role-level execution planning.","productivity":"Throughput and workflow optimization at task level.","collaborate":"Multi-stakeholder communication and coordination patterns."}'
---

## State location

Post-Labor Economics state may exist in `<workspace>/post-labor-economics/`, `<workspace>/memory/post-labor-economics/`, or `~/post-labor-economics/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/post-labor-economics/`, `<workspace>/memory/post-labor-economics/`, `~/post-labor-economics/`.
3. If more than one candidate exists, use only the highest-precedence directory and report the split; do not merge trees automatically.
4. If none exists and durable notes must be created, default to `<workspace>/post-labor-economics/` when `<workspace>` is available; otherwise ask for a state root instead of guessing from the current directory.

Use the selected `<state_root>` for every state operation in this skill. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path.

## Setup

If `<state_root>/` does not exist or is empty, read `references/setup.md`, explain that you can save local preferences for continuity, and ask for explicit confirmation before writing memory files.

## When to Use

User wants to analyze a world where paid employment is no longer the main channel for income, status, or social coordination. Use for automation transition strategy, post-work policy design, distribution modeling, and labor market scenario planning.

## Architecture

Memory lives in `<state_root>/`. See `references/memory.md` for templates.

```text
<state_root>/
|- memory.md       # Core context and integration preferences
|- portfolios.md   # Policy portfolio drafts and decision logs
|- indicators.md   # Chosen metrics, targets, and thresholds
`- scenarios.md    # Transition scenarios and stress tests
```

## Data Storage

Local working memory and transition artifacts are stored in `<state_root>/` only.

## Quick Reference

Load these references on demand to expand analysis:

- `references/setup.md`: map the initial decision context and persistence consent.
- `references/memory.md`: format schemas for memory, portfolios, indicators, and scenarios.
- `references/frameworks.md`: apply analytical lenses (automation, social provision, durability).
- `references/policy-portfolio.md`: construct concrete policy bundles across security, work, wealth, and time.
- `references/indicators.md`: establish transition dashboards and alert patterns.
- `references/scenarios.md`: stress-test policies against alternate futures.
- `references/research-notes.md`: retrieve empirical baselines and source pointers.

## Core Rules

### 1. Define the Transition Mechanism Before Debating Policy

Start by naming what changed in production:

- task automation,
- capital concentration,
- platform coordination,
- energy and ecological limits,
- demographic pressure.

No mechanism means no credible post-labor recommendation.

### 2. Separate Production Logic from Distribution Logic

Model these as two distinct layers:

- how goods and services are produced,
- how purchasing power, rights, and access are distributed.

Treat efficient production and fair distribution as separate models that must be designed together.

### 3. Design Bundles, Not Single-Idea Policies

Always propose a portfolio with at least three categories:

- baseline security (income or services),
- coordination of socially necessary work,
- ownership and bargaining architecture.

Single-policy answers are fragile and usually fail under political stress.

### 4. Make Power and Ownership Explicit

For each design, state:

- who owns productive assets,
- who controls allocation decisions,
- who captures automation gains,
- who absorbs transition risk.

If power is hidden, the model is incomplete.

### 5. Quantify the Path, Not Just the End-State

Require phased planning:

- near term (0-3 years),
- transition (3-10 years),
- structural horizon (10+ years).

For each phase, define financing, institutions, and measurable checkpoints.

### 6. Evaluate Multiple Human Profiles

Every recommendation must score effects on:

- displaced workers,
- care workers,
- young entrants,
- older workers,
- disabled people,
- small producers and local communities.

A policy that works only for one profile is not a post-labor solution.

### 7. Maintain an Evidence Ledger

Tag every claim as one of:

- empirical finding,
- modeling assumption,
- normative preference,
- political constraint.

Label assumptions and values clearly rather than presenting them as settled facts.

## Common Traps

- Treating post-labor economics as "no one works" -> ignores care, coordination, and public goods labor.
- Debating UBI as the whole system -> misses services, institutions, and ownership design.
- Assuming automation gains distribute automatically -> reproduces inequality under new technology.
- Mixing descriptive and moral claims -> analysis becomes rhetorical instead of decision-grade.
- Skipping implementation sequencing -> creates elegant theory with no transition path.
- Ignoring political feasibility entirely -> proposal cannot survive first contact with institutions.

## Security & Privacy

**Data that leaves your machine:**

- None from this skill itself.

**Data that stays local:**

- Policy drafts, indicators, and scenarios in `<state_root>/`.

**This skill does NOT:**

- Make undeclared network calls.
- Collect or infer sensitive personal data beyond what the user provides for analysis.
- Write outside its declared local path.

## Scope

This skill focuses on:

- Structuring post-labor economic analysis.
- Building policy portfolios and transition scenarios.
- Separating empirical evidence from assumptions and values.

Out of scope (route elsewhere or decline):

- Deterministic macro forecasts presented as certainty.
- Legal or fiscal sign-off that belongs to institutions.
- Treating one country template as universally transferable.

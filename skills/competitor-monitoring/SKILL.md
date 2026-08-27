---
name: competitor-monitoring
description: Monitor competitors by tracking pricing, features, and positioning. Maintain strategic dossiers and alert the user to critical market shifts.
metadata:
  openclaw: '{"emoji":"🔍","displayName":"Competitor Monitoring","requires":{"os":["linux","darwin","win32"]}}'
  related-skills: '{"market-research":"broader market analysis","business":"strategic frameworks","analytics":"data analysis patterns"}'
---

## Setup

On first use, read `references/setup.md` for integration guidelines.

## When to Use

User needs competitive intelligence. Agent tracks competitors, monitors changes, analyzes positioning, and maintains strategic dossiers with pricing, features, and market moves.

## State location

- **Target Directory**: `<state_root>/` (workspace-first convention)
- **Creation**: On first run, create this directory and initialize `memory.md` following `references/memory-template.md`.

## Architecture

See `references/memory-template.md` for structure.

```
<state_root>/
├── memory.md           # Status + preferences + active competitors
├── competitors/        # Individual dossiers
│   ├── {company}.md    # Per-competitor intelligence
│   └── ...
├── alerts/             # Triggered alerts
│   └── YYYY-MM-DD.md   # Daily alert log
└── analysis/           # Strategic analyses
    └── {topic}.md      # Comparison reports
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | On first use |
| Memory template | `references/memory-template.md` | When initializing or updating state |
| Domain knowledge | `references/domain-knowledge.md` | When performing competitive analysis or structuring dossiers |


## Core Rules

### 1. Check Dossiers Before Acting
Before any competitor question, load the relevant `competitors/{company}.md` file. Build on existing intelligence to maintain continuity.

### 2. Track These Signals
| Signal | Where to Look | Impact |
|--------|---------------|--------|
| Pricing changes | Pricing page, announcements | Direct competitive threat |
| New features | Changelog, blog, social | Capability gap/parity |
| Positioning shifts | Homepage copy, ads | Market narrative |
| Hiring patterns | Jobs page, LinkedIn | Strategic direction |
| Funding/acquisitions | News, Crunchbase | Resource changes |

### 3. Alert Priorities
- **Critical:** Pricing undercut, feature that blocks your advantage
- **High:** Major feature launch, positioning change
- **Medium:** Blog posts, minor updates, team changes
- **Low:** Social activity, routine content

### 4. Maintain Signal-to-Noise
Filter alerts to surface only actionable changes or strategic awareness. If no actionable changes occurred, explicitly state that the landscape is stable.

### 5. Compare Objectively
When analyzing competitors, be honest about their strengths. Acknowledge where they're ahead. False confidence leads to bad strategy.

**Framework:**
```
For each competitor, answer honestly:
- Where are they better than us?
- What do their customers love that ours don't have?
- If I were a customer, why would I choose them?
```

### 6. Update Dossiers Proactively
After any research or mention of a competitor, update their dossier. Update the dossier proactively after any research or mention.

### 7. Connect to Strategy
Every observation should connect to "so what?" What does this mean for user's positioning, roadmap, or priorities?

**Template:**
```
OBSERVATION: Competitor X launched feature Y
SO WHAT: This means...
→ For our roadmap: [accelerate/deprioritize/ignore]
→ For positioning: [adjust messaging/double down/no change]
→ For sales: [new objection/new advantage/neutral]
```

## Monitoring Patterns

### Regular Check-ins
```
Weekly: Scan pricing pages, homepages, changelogs
Monthly: Deep dive on positioning, feature comparison
Quarterly: Full competitive landscape review
```

### Trigger-Based
- User mentions competitor → refresh dossier
- Industry news → check all relevant competitors
- User launches feature → compare to competitor alternatives

## Competitor Dossiers & Analysis

- **Dossiers**: See `references/memory-template.md` for the dossier structure.
- **Analysis**: Use the frameworks in `references/domain-knowledge.md` (e.g., SWOT, Porter's Five Forces) when performing head-to-head, landscape, or gap analysis.

## Best Practices

- **Focus on Actionable Metrics**: Prioritize pricing, feature, and positioning changes over social metrics.
- **Maintain Objectivity**: Honestly assess competitor strengths to provide a realistic strategic view.
- **Curate Signal**: Filter reports for actionable changes to avoid information overload.
- **Keep Intelligence Fresh**: Proactively update dossiers after every mention.
- **Track Substitutes**: Monitor both direct rivals and indirect competitors.
- **Proactive Monitoring**: Scan for threats early rather than waiting for breakage.
- **Diverse Sources**: Combine insights from pricing pages, changelogs, blogs, job postings, and reviews.

## Security & Privacy

**Data that stays local:**
- All competitor dossiers stored in `<state_root>/`
- Analysis reports and alert history
- User preferences and monitoring settings

**What happens on first use:**
- Creates folder `<state_root>/` with your data
- Asks how you want monitoring to work (proactive vs on-demand)

**This skill does NOT:**
- Access competitor internal systems
- Scrape data in violation of ToS
- Store credentials or sensitive tokens
- Send your data externally

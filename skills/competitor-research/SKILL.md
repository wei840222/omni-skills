---
name: competitor-research
description: Conduct competitor audits, market positioning, and gap analysis for strategic
  decisions.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji": "🔬", "requires": {"bins": [], "paths": ["<state_root>/competitor-research/"]},
    "os": ["linux", "darwin", "win32"], "displayName": "Competitor Research"}'
  related-skills:
  - market-research
  - business
  - competitor-monitoring
---
## Setup

On first use, read `references/setup.md` for integration guidelines.

## When to load

Load this skill when the user requests competitor analysis, market positioning research, or gap analysis in a specific niche.

## Architecture

Memory lives in `<state_root>/competitor-research/`. See `assets/memory-template.md` for structure.

```
<state_root>/competitor-research/
├── memory.md              # Status + research preferences + niche context
├── niches/                # Research by market/niche
│   └── {niche}/           # One folder per niche
│       ├── overview.md    # Market landscape
│       └── {company}.md   # Individual competitor deep dives
└── insights/              # Cross-cutting findings
    └── {date}-{topic}.md  # Strategic insights and recommendations
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Research frameworks | `references/frameworks.md` |
| Core rules | `references/core-rules.md` |

## Core Rules

Load `references/core-rules.md` to review required frameworks, structure, iteration strategy, and how to deliver actionable recommendations.

## Research Frameworks

### Market Landscape
Start broad, then narrow:
1. List all players (direct, indirect, substitutes)
2. Categorize by segment (enterprise, SMB, prosumer, etc.)
3. Map by positioning (premium vs budget, generalist vs niche)
4. Identify white space

### Competitive Matrix
Compare on dimensions that matter:

| Competitor | Price | Feature X | Feature Y | Target | Differentiator |
|------------|-------|-----------|-----------|--------|----------------|
| Player A   | $$$   | ✅        | ❌        | Enterprise | Security |
| Player B   | $     | ❌        | ✅        | SMB    | Simplicity |
| (User)     | $$    | ✅        | ✅        | Mid-market | Best of both |

### Win/Lose Analysis
For each competitor, answer:
- Why would a customer choose them over user?
- Why would a customer choose user over them?
- What type of customer is a slam-dunk for each?

### Positioning Audit
Analyze how competitors position:
- Homepage headline and subhead
- Three main value props
- Social proof strategy
- Pricing presentation
- Comparison pages (if any)

Look for positioning gaps nobody owns.

## Iterative Research Workflow

**Session 1: Landscape**
```
"I want to research competitors in [niche]"
→ Quick scan of market
→ Identify 5-10 key players
→ Create overview.md for the niche
→ Ask: want to deep dive any specific competitor?
```

**Session 2+: Deep Dives**
```
"Let's analyze [Company X]"
→ Load niche overview for context
→ Full competitor analysis
→ Save to niches/{niche}/{company}.md
→ Update overview with new findings
```

**Return Visit**
```
"What do we know about [niche/company]?"
→ Load existing research
→ Note what might be outdated
→ Offer to refresh specific sections
```

## Common Traps

- **No scope = bad research** → Always clarify what decision this informs before starting
- **Feature obsession** → Business model and positioning often matter more than features
- **Outdated pricing** → Verify pricing pages directly instead of relying on cached data
- **Missing substitutes** → Direct competitors aren't the only threat. What else solves the same job?
- **Analysis paralysis** → Set time limits. Good-enough research beats delayed perfect research
- **No recommendations** → A list of competitors isn't strategy. What should user DO with this?
- **Forgot to save** → Update memory and niche files after every session

## Security & Privacy

**Data that stays local:**
- All research stored in `<state_root>/competitor-research/`
- Niche analyses and competitor profiles
- User preferences and context

**This skill does NOT:**
- Access private competitor systems
- Create fake accounts for research
- Scrape content violating ToS
- Send your research externally
- Store any credentials

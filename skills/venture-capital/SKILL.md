---
name: venture-capital
description: Evaluate startup pitches, perform due diligence, structure term sheets,
  analyze market opportunities, and advise on fundraising strategy.
metadata:
  openclaw: '{"emoji": "💰", "requires": {"bins": []}, "os": ["linux", "darwin", "win32"],
    "displayName": "Venture Capital"}'
  related-skills:
  - cfo
  - ceo
  - business
  - founder
  - startup
---

## When to load

- The user provides a startup pitch deck or business plan.
- The user asks for help evaluating an early-stage company investment.
- The user requests guidance on structuring a term sheet or negotiating terms.
- The user needs an analysis of a startup's market size, unit economics, or competitive dynamics.
- The user wants to write or review a venture capital deal memo.

## Quick Reference

| Topic | File |
|-------|------|
| Due diligence | `references/due-diligence.md` |
| Term sheets | `references/term-sheets.md` |
| Valuation | `references/valuation.md` |

## Core Rules

### 1. Evaluate Team First
- Founders matter more than ideas at early stage
- Check: domain expertise, complementary skills, founder-market fit
- Red flags: solo technical founder for B2B sales, no skin in game, part-time commitment

### 2. Size the Market Correctly
- TAM/SAM/SOM must be bottoms-up, not top-down
- Require specific, bottoms-up justification for market capture rather than generic top-down percentages
- Look for markets that are small now but growing fast

### 3. Understand Unit Economics
- CAC payback period under 12 months for healthy SaaS
- LTV/CAC ratio above 3x for sustainable growth
- Gross margins above 60% for software, above 40% for marketplaces

### 4. Check Competitive Dynamics
- Why now? What changed to enable this company?
- What is the moat? Network effects, switching costs, data advantages
- Who else is funded in this space? What is the differentiation?

### 5. Structure Deals with Alignment
- Pro-rata rights protect against dilution
- Liquidation preferences should be 1x non-participating standard
- Anti-dilution provisions: weighted average preferred over full ratchet

### 6. Apply Stage-Appropriate Criteria
| Stage | Focus | Typical Check Size |
|-------|-------|-------------------|
| Pre-seed | Team, vision, early signal | $100K-$500K |
| Seed | Product-market fit signals | $500K-$2M |
| Series A | Repeatable go-to-market | $5M-$15M |
| Series B+ | Scale and efficiency | $15M+ |

### 7. Document Investment Thesis
- Write the memo before deciding
- Include: why this team, why this market, why now, key risks, path to exit
- Update thesis quarterly to track against assumptions

## Common Traps

- Falling in love with founders instead of the business
- FOMO investing without proper diligence
- Ignoring red flags because of hot market
- Overweighting past success of repeat founders
- Missing the competitive threat from adjacent markets
- Underestimating capital requirements for hardware/biotech

## Security & Privacy

**Data that stays local:**
- Deal memos and investment notes
- Portfolio company analysis

**This skill does NOT:**
- Make investment recommendations without full context
- Guarantee returns or predict outcomes
- Replace legal review of term sheets

## State location
- `<state_root>/venture-capital/`

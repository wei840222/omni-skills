---
name: geo
description: "Audit and optimize Generative Engine Optimization (GEO). Trigger to improve AI recommendations for brands, run multi-model visibility audits, or develop platform-specific presence strategies."
metadata:
  openclaw: '{"emoji":"🤖"}'
  related-skills: '{"seo":"For traditional Google search ranking", "ads":"For paid advertising campaigns"}'
---

## State location

This skill is completely stateless. It does not store any local configuration, credentials, or audit logs on the file system. Output artifacts should be presented to the user or saved in the current working directory based on instructions.

## Quick Reference

| Reference File | When to load | Purpose |
|----------------|--------------|---------|
| `references/audit.md` | When measuring current AI visibility or designing query simulations. | Complete audit workflow, query matrix, and documentation structure. |
| `references/strategies.md` | When developing execution playbooks for specific business types or platforms. | Playbooks for SaaS, E-commerce, local businesses, and content creators. |
| `references/domain-knowledge.md` | When evaluating content structure or seeking advanced optimization tactics. | Academic research insights (Quotation Addition, Fluency Optimization). |

## Core Execution Loop

1. **Audit First**: Load `references/audit.md` to design a query matrix and measure baseline visibility across ChatGPT, Claude, and Perplexity.
2. **Identify Gaps**: Analyze win/loss patterns and competitive positioning.
3. **Select Strategy**: Load `references/strategies.md` to map the appropriate tactic (e.g., technical authority, platform dominance) to the business type.
4. **Optimize Content**: Load `references/domain-knowledge.md` to apply proven semantic and fluency optimizations.
5. **Monitor**: Establish a monthly audit routine to track position, context, and phrasing sensitivity.

## Red Flags

- AI never mentions the brand → Execute awareness campaigns (no presence in training data).
- AI mentions the brand negatively → Execute reputation management across scraped sources.
- AI confuses the brand with a competitor → Execute differentiation content strategies.
- AI recommends the brand for the wrong use case → Execute targeted positioning corrections.

## Scope Boundaries

- For traditional search engine ranking, route to the `seo` skill.
- For paid visibility, route to the `ads` skill.
- For social media marketing, route to relevant platform skills.

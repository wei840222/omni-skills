---
name: tech-debt
description: Guide technical debt categorization, track inventory, and implement payoff cadences without freezing delivery. Trigger when discussing refactoring, code quality, or legacy systems.
metadata:
  openclaw: '{"emoji": "⚙️"}'
  related-skills: '{"ci-cd":"Provides the test and staged-rollout safety net that lowers repayment risk.","review-code":"Helps reviewers evaluate and scope debt-payoff changes."}'
---

## Start here

Identify whether the request is about classifying, prioritizing, recording, or repaying technical debt. Load only the matching reference below; use `industry-research.md` when a recommendation needs its source context.

## Quick Reference

| File | Topic | When to load |
|---|---|---|
| `references/what-counts-as-debt.md` | What counts as debt | To categorize technical debt vs. bad code |
| `references/three-numbers-per-item:-interest-blast-radius-payoff-cost.md` | Tracking | To evaluate and rank debt items |
| `references/the-inventory.md` | The inventory | To establish a debt register |
| `references/payoff-cadence.md` | Payoff cadence | To plan debt reduction iterations |
| `references/debt-types-by-interest-profile.md` | Debt types | To identify specific forms of debt (architecture, test, etc.) |
| `references/reading-the-interest-from-the-code.md` | Code signals | To spot hidden debt via cycle time or bugs |
| `references/when-not-to-pay-it.md` | Exclusions | To decide when to leave debt alone |
| `references/refactor-vs-rewrite.md` | Fix strategies | To choose between refactoring and a full rewrite |
| `references/the-metaphor-as-a-translation-device.md` | Communication | To explain debt to non-engineers |
| `references/situations.md` | Situations | To apply specific plays for common debt scenarios |
| `references/where-camps-disagree.md` | Controversies | To navigate conflicting opinions on debt management |
| `references/industry-research.md` | Domain research | To reference established practices and definitions |

## State location

This skill is completely stateless. It provides conceptual guidelines on identifying and managing technical debt and does not read, write, or maintain any local configuration or state files.

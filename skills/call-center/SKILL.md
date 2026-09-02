---
name: call-center
description: Handle inbound and outbound customer voice calls. Use this when the user needs to provide support, run sales campaigns, de-escalate issues, or log call interactions.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📞"}'
  related-skills: '{"customer-support": "Provides customer support workflows.", "escalate": "Provides escalation patterns.", "crm": "Manages customer data.", "chat": "Handles text conversations."}'
---


## When to Use

Agent handles customer interactions via phone or voice channels. Covers inbound support, outbound campaigns, issue resolution, and call documentation.

## State location

Call Center state may exist in `<workspace>/call-center/`, `<workspace>/memory/call-center/`, or `~/call-center/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/call-center/`, `<workspace>/memory/call-center/`, `~/call-center/`.
3. If none exists and state must be created, default to `<workspace>/call-center/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for setup.

```
<state_root>/
├── memory.md          # HOT: active calls, recent issues
├── scripts/           # Call scripts by type
├── escalations.md     # Escalation log and patterns
└── metrics.md         # Call stats and performance
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Memory setup | `assets/memory-template.md` | When setting up or reviewing the structure of persistent call memory. |
| Call scripts | `references/scripts.md` | When actively handling an inbound, outbound, or complaint call. |
| Escalation guide | `references/escalation.md` | When the caller requests a supervisor or the issue exceeds your authority. |
| Domain research | `references/research.md` | When updating KPI targets, escalation criteria, or call-center metric guidance. |

## Core Rules

### 1. Greet and Identify
- Open with company greeting and agent name
- Verify caller identity before discussing account details
- Note caller mood and adjust tone accordingly

### 2. Active Listening First
- Let caller explain fully before responding
- Paraphrase to confirm understanding
- Allow caller to speak continuously; interrupt only for immediate safety concerns

### 3. Follow Script Structure
| Call Type | Script Flow |
|-----------|-------------|
| Support | Greet, identify issue, troubleshoot, resolve/escalate, confirm, close |
| Sales | Greet, qualify, present, handle objections, close/schedule |
| Collections | Greet, verify, state balance, offer options, document |

### 4. Document Everything
- Log call reason, actions taken, resolution
- Note any promises made with deadlines
- Flag recurring issues for pattern analysis

### 5. Escalation Triggers
Escalate immediately when:
- Caller requests supervisor
- Issue outside agent authority
- Legal or compliance mention
- Threat or safety concern
- 3+ failed resolution attempts

### 6. Close with Confirmation
- Summarize actions taken
- Confirm caller satisfaction
- Provide reference number
- Offer additional help before ending

### 7. Post-Call Wrap
- Complete documentation within 2 minutes
- Update CRM with interaction notes
- Flag any follow-up required

## Call Center Traps

- **Jumping to solutions** before understanding the problem fully leads to repeat calls and frustrated customers
- **Over-promising** resolution timeframes creates broken commitments
- **Skipping verification** risks sharing info with wrong person (compliance violation)
- **Long holds without updates** make callers hang up and call back angry
- **Not documenting** verbal promises leads to "but they told me..." disputes

## Metrics to Track

| Metric | Target | Why |
|--------|--------|-----|
| First Call Resolution (FCR) | 70-80% | Reduces callbacks |
| Average Handle Time (AHT) | 3-6 mins (Context-dependent) | Balance efficiency/quality |
| Customer Satisfaction (CSAT) | >85% | Quality indicator |
| Escalation Rate | <15% | Agent empowerment |
| After-Call Work | <2 min | Documentation efficiency |

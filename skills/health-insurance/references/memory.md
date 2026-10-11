# Memory Template — Health Insurance

Create `<state_root>/memory.md` with this structure:

```markdown
# Health Insurance Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Coverage Profile
- Coverage scope:
- Region:
- Current plan type:
- Renewal month:

## Care Utilization
- Primary care frequency:
- Specialist frequency:
- Recurring prescriptions:
- Expected major procedures:

## Financial Boundaries
- Comfortable monthly premium range:
- Comfortable deductible exposure:
- Maximum annual out-of-pocket tolerance:

## Plan Preferences
- Must-keep providers/facilities:
- Network flexibility:
- Plan type preference (if any):
- Referral tolerance:

## Active Decisions
- Option A:
- Option B:
- Recommendation status:
- Next deadline:

## Notes
- Short, durable observations approved by user.

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | still learning profile | continue collecting context naturally |
| `complete` | stable profile | optimize for quick decisions |
| `paused` | user paused updates | keep read-only unless reopened |
| `skip_setup` | user wants minimal setup prompts | bypass follow-up setup questions |

## Key Principles

- Store only context the user explicitly approves.
- Store only non-sensitive data, excluding policy numbers, government IDs, and payment credentials.
- Keep notes concise and decision-focused.
- Update `last` whenever memory changes.

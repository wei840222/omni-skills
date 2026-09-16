# Sources — subscriptions

Gate 6 research anchors for personal subscription tracking, renewal hygiene, and waste reduction. Prefer primary consumer-finance and regulator guidance over listicles. Re-verify product prices and plan names before quoting them as current.

## Consumer spending and subscription waste

- [Consumer Financial Protection Bureau — Manage your spending](https://www.consumerfinance.gov/consumer-tools/money-as-you-grow/manage-your-money/) — practical framing for tracking recurring household obligations.
- [FTC — Subscriptions and negative option marketing](https://www.ftc.gov/business-guidance/resources/negative-option-rule) — disclosure, consent, and cancellation expectations that shape how agents should talk about renewals (business rule context; still useful for user-facing cancel hygiene).
- [FTC Consumer Advice — Online shopping and subscriptions](https://consumer.ftc.gov/articles/online-shopping) — consumer-facing reminders about recurring charges and account access control.

## Recurring-charge and card hygiene

- [CFPB — What is a recurring payment?](https://www.consumerfinance.gov/ask-cfpb/what-is-a-recurring-payment-or-preauthorized-debit-en-2145/) — definitions useful when classifying bank descriptors vs true subscriptions.
- [CFPB — How to stop automatic payments](https://www.consumerfinance.gov/ask-cfpb/how-do-i-stop-automatic-payments-from-my-bank-account-en-2147/) — recovery path when merchant cancel UI fails (user-controlled; agent does not initiate bank disputes unilaterally).

## Practice notes for this skill

- Default thresholds in SKILL.md (unused 30+ days, 7-day annual reminder, quarterly value review) are **starting defaults**, not legal requirements.
- Example prices (Netflix $15.49, sample $147/month totals) are illustrative fixtures for prompts and docs; replace with the user's real inventory.
- Merchant billing architecture (Stripe subscriptions, webhooks, revenue recognition) belongs to `billing`, not this skill.
- Obsolete packaging removed in this refactor: Clawic homepage, top-level `slug`/`homepage`/`version`, clawdbot OS metadata, and `_meta.json`.

# Cost Estimation & ROI

## Cost inputs

Use current rate cards for the *exact* model, training method, region, account tier and data-sharing setting. Record the source URL and checked date in the project estimate; the primary entry points are in `sources.md`. Published API rates generally use **per million tokens** rather than per thousand; confirm the quoted unit before multiplying. Hosted GPU prices depend on provider, instance, reservation and duration.

For a token-billed supervised job, estimate `training_cost = sum(billable_training_tokens_by_epoch) × rate_per_million / 1_000_000`. Some providers use hourly compute or additional storage/hosting charges instead; match the actual billing model. Include repeated experiments and data preparation, not just the successful run.

## Comparable inference calculation

For each candidate, measure production input/output token distributions, retries, cache/batch eligibility, and expected request volume. Compute:

```
base_monthly = requests × (base_input_tokens × base_input_rate + base_output_tokens × base_output_rate) / 1_000_000
candidate_monthly = requests × (candidate_input_tokens × candidate_input_rate + candidate_output_tokens × candidate_output_rate) / 1_000_000 + hosting + operations
monthly_net_savings = base_monthly - candidate_monthly
break_even_months = (training + data_preparation + evaluation + migration) / monthly_net_savings
```

Use the same currency and billing period throughout. When `monthly_net_savings <= 0`, there is **no cost break-even** at that traffic level; tuning may still be justified by measured quality. Divide by measured requests per month only when costs were computed per request. Label assumptions and show sensitivity to traffic, output length, failure/retry rates and rate-card changes.

### Numerical illustration — hypothetical rates, not provider quotes

Suppose the base costs $0.004/request and a trained candidate $0.002/request inclusive of hosting, at 100,000 requests/month; preparation plus training costs $600. Savings are $200/month and break-even is three months, *if* the candidate meets the same held-out quality and privacy requirements. Recompute with actual model/account rates before recommending it.

## Cost levers and constraints

- Shorter prompts or smaller models help only if held-out quality and safety criteria remain satisfied.
- Batch/caching and data-sharing discounts depend on current vendor terms, feature compatibility and privacy permission; never opt into data sharing solely to reduce costs.
- Self-hosting includes idle GPU capacity, energy, storage, monitoring, maintenance, reliability and operational staffing. Avoid universal volume thresholds for when it becomes cheaper.
- Retraining and multiple evaluation rounds affect ROI. Keep the base and few-shot baselines in the comparison.

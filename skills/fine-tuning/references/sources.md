# Source checks — 2026-09-28

Check the exact provider model, account and region again immediately before a paid training recommendation. These links are entry points, not a guarantee of future eligibility or pricing.

## Format and training availability

- Agent Skills specification: https://agentskills.io/specification — source for package/frontmatter format.
- OpenAI fine-tuning guide: https://developers.openai.com/api/docs/guides/fine-tuning — method/model support, conditional on account.
- OpenAI deprecations: https://developers.openai.com/api/docs/deprecations — self-serve fine-tuning restricted to existing qualifying organizations since 2026-05-07; further eligibility cutoff 2026-07-02; new jobs end 2027-01-06 for active existing customers. Model shutdown dates may be earlier.
- Google model tuning: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/tuning — check current supervised/preference tuning models, region and data requirements.
- Amazon Bedrock custom models: https://docs.aws.amazon.com/bedrock/latest/userguide/custom-models.html — verify Claude model and region support rather than treating a historical GA announcement as current availability.
- AWS historical Claude 3 Haiku announcement: https://aws.amazon.com/blogs/aws/fine-tuning-for-anthropics-claude-3-haiku-model-in-amazon-bedrock-is-now-generally-available/ — historical only; current model/region availability must be checked separately.

## Rates, evaluation and compliance

- OpenAI API pricing: https://developers.openai.com/api/docs/pricing — check method, units and model; current self-serve eligibility still applies.
- Google pricing: https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing — model/region-specific pricing.
- Amazon Bedrock pricing: https://aws.amazon.com/bedrock/pricing/ — model/region/method-specific pricing.
- OpenAI preparation guide: https://developers.openai.com/api/docs/guides/fine-tuning-best-practices — review supported data formats and evaluation guidance for the chosen method.
- EU GDPR legal text: https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng — legal obligations depend on jurisdiction and role; seek legal review, not a model-generated compliance verdict.

## Replaced historical assertions

The original package's fixed GPT-4o/mini and GPT-4.1 training rates, Claude 3 Haiku-only region, Gemini 1.5 availability, universal sample minimums, volume-based ROI, hardware minima, universal LoRA multiplier, and two unattributed benchmark improvements are not promoted as current facts. The former OpenAI CLI command and pinned model ID are examples from an earlier ecosystem, not verified procedures. Current model lists and prices must be tied to a dated source and account eligibility; unknown values remain unknown.

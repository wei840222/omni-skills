# Model and platform adaptation

Use this reference when moving a prompt between model families, changing a deployed model version, or selecting platform features.

## Adapt through evaluation

1. Pin the deployed model version or snapshot when the platform supports it.
2. Run the same evaluation set on the candidate model with the existing prompt.
3. Diagnose the observed regression before changing prompt wording: model capability, context-window fit, tool/structured-output behavior, cost, or latency can be the limiting factor.
4. Change the smallest relevant prompt component and repeat the evaluation.

## Portable guidance

- Use high-authority instruction channels for stable behavior, goals, and output rules; keep task-specific input in the user or input content according to the platform's role model.
- Define a schema and validate the returned value when structured output is required. Prefer the platform's supported structured-output feature to a prompt-only JSON request when it is available.
- Use examples when the desired mapping, format, or edge behavior is difficult to express as a rule. Keep them representative of the real evaluation cases.
- Let results determine whether additional reasoning scaffolding helps. It can add latency and token cost without improving simple tasks.
- Treat model-family labels as insufficient compatibility evidence: validate the actual model and version used in production.

## Official references

- OpenAI, *Prompt engineering*: https://developers.openai.com/api/docs/guides/prompt-engineering
- Anthropic, *Prompt engineering overview*: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

# Provider Selection

Provider catalogs and fine-tuning eligibility change. Verify the *specific model ID*, training method, region, quota, data-retention terms, and rates in the selected account before recommending a paid job. Primary vendor entry points and the date checked are recorded in `sources.md`.

| Requirement | Selection test |
|---|---|
| Managed supervised tuning | Check the provider's current supported-model list, input format, account eligibility, region, and pricing. OpenAI and Vertex AI publish separate tuning guidance. |
| Claude is mandatory | Check Amazon Bedrock customization's current model/region table and the direct Anthropic API capabilities separately; do not infer that every Claude model supports tuning. |
| Private/local training | Compare model license, downloadable weights, compute capacity, local data handling, and evaluated quality before choosing LoRA/QLoRA. |
| Multilingual task | Use held-out examples in the actual languages and compare available providers; branding does not prove quality. |

## Managed-provider workflow

1. From the official supported-model documentation, select an eligible model and training method for the task; distinguish supervised, preference, and reinforcement tuning.
2. Confirm the account's actual access and regional/data-processing constraints. A public documentation example is not proof of current account availability.
3. Validate examples with the provider's current schema, estimate billable training tokens and inference requests using current rate cards, and run a small authorized experiment.
4. Evaluate the trained model against a baseline on the same untouched held-out dataset. Publish or deploy only after the required approval.

The original package listed GPT-4o, GPT-4o-mini, GPT-4.1 variants, o4-mini, Claude 3 Haiku, Gemini 1.5, Mistral, and open-weight Llama/Qwen models with hard-coded availability, price, region, quality, and minimum-example claims. Those snapshots are not a current compatibility matrix. Consult each linked vendor catalog and record the exact checked model ID, region, method, date and rate in the project-specific assessment rather than copying historical figures.

## Open-weight training

LoRA/QLoRA via PEFT/Unsloth, Axolotl, TorchTune, or similar tooling may reduce memory use for supported architectures. Quantization, target modules, GPU memory, licensing, software versions and quality tradeoffs depend on the actual model and implementation; run a small device-memory test before reserving compute. Serving stacks such as vLLM have different requirements from training stacks. Match the base model and tokenizer versions between training and serving, then compare validation behavior after any quantization or adapter merge.

## Decision checkpoint

Record: task, dataset authorization, target model/version, region, training method, budget ceiling, data-sharing setting, privacy review, held-out metric and rollback path. If any required approval or eligibility check is missing, return a plan instead of uploading data or starting training.

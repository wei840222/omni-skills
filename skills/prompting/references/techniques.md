# Advanced prompting techniques

Load this reference when the minimal prompt fails a measured success criterion. Add one technique, then compare it to the baseline on the same evaluation set.

## Examples

Use two to five representative input/output examples when a format, transformation, or classification boundary is hard to describe. Include a boundary case when it represents a real user request.

## Decomposition

Split a task into staged prompts when an intermediate result can be inspected, validated, or safely corrected before it becomes input to the next stage. Define the input and output contract for each stage.

## Structured output

State the desired schema, required fields, and invalid-output recovery. When the target platform supports structured outputs, use that mechanism and validate the returned value before downstream use.

## Sampling and comparison

For uncertainty-sensitive tasks, generate multiple candidate answers only when the evaluation plan explains how to select or reconcile them. Record the added cost and latency with the quality result.

## Constraint placement

Keep the task, constraints, supplied context, and output contract in clear labeled sections. Repeat only the constraints that evaluation shows are being lost; remove redundant wording during the compression pass.

## Roles and voice

Specify a role only when it changes useful behavior. For voice work, include observable style evidence and test the complete output rather than relying on the role label alone.

## Sources

- OpenAI, *Prompt engineering*: https://developers.openai.com/api/docs/guides/prompt-engineering
- Anthropic, *Prompt engineering overview*: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

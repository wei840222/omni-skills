# Sources

Pinned references for claims used by `compress`. Prefer these over model memory when updating ratios, validation guidance, or trigger wording.

## Agent Skills format and craft

- Agent Skills document index — https://agentskills.io/llms.txt
- Agent Skills specification — https://agentskills.io/specification
- Skill creation best practices — https://agentskills.io/skill-creation/best-practices
- Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions
- Reference validator (`skills-ref` / `agentskills`) — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Long-context recall and prompt compression

- Lost in the Middle: How Language Models Use Long Contexts (Liu et al., 2023) — https://arxiv.org/abs/2307.03172
- LLMLingua: Compressing Prompts for Accelerated Inference of Large Language Models (Jiang et al., 2023) — https://arxiv.org/abs/2310.05736

## How this skill uses them

- Lost-in-the-middle evidence supports compressing for recall quality, not only for hard context limits.
- LLMLingua supports the general claim that prompt compression can reduce tokens while preserving task utility; this skill still requires its own anchor/reconstruction loop rather than treating any compressor as lossless.
- Agent Skills docs govern frontmatter, progressive disclosure, and description trigger quality for the package itself.

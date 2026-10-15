# Sources

Gate 6 citations for claims retained in this skill. Prefer live docs over
frozen snapshots.

## Agent Skills format

- Agent Skills specification: https://agentskills.io/specification
- Skill-creation best practices: https://agentskills.io/skill-creation/best-practices
- Description optimization: https://agentskills.io/skill-creation/optimizing-descriptions
- LLMs index: https://agentskills.io/llms.txt
- Reference validator package: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Delegation / autonomy design (conceptual)

This skill's graduated autonomy ladder (shadow → draft-only → review →
autonomous) is an operational policy for workspace agents, not a vendor SLA.
When comparing with human organizational practice, treat the following as
background framing only; do not invent numeric quotas from them:

- Levels of Autonomy for AI Agents (overview of human-in-the-loop vs full
  autonomy trade-offs): https://www.ibm.com/think/insights/ai-agent-autonomy
- NIST AI Risk Management Framework 1.0 (govern / map / measure / manage for
  AI systems that act with delegated authority):
  https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf

## Related omni-skills boundaries

Routing boundaries in the description point at packages that exist in this
repository (`hiring`, `recruiter`, `management`, `roleplay`, `paperclip`).
Re-check package presence before adding a new related-skill edge.

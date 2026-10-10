# Research sources — Meditate

Domain claims in this skill are mostly **stable-domain** process rules (sandbox reflection, feedback loops, queue limits). Re-open these URLs when auditing freshness or expanding guidance. Do not invent pricing, product limits, or vendor SLAs from memory.

## Agent skill format and packaging

- **Agent Skills specification** — frontmatter, progressive disclosure, resource layout — https://agentskills.io/specification
- **Agent Skills document index** — entry points for normative docs — https://agentskills.io/llms.txt
- **skills-ref / agentskills validator** — reference validation tooling — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Reflection and metacognition (stable-domain)

- **APA — Metacognition** — monitoring and control of one’s own thinking; supports observation-before-action framing — https://www.apa.org/pubs/highlights/peeps/issue-135
- **Harvard Business Review — The Power of Reflection at Work** — structured reflection improves learning transfer vs action-only loops — https://hbr.org/2017/03/why-you-should-make-time-for-self-reflection-even-if-you-hate-doing-it
- **NIH / PMC — Feedback and self-regulated learning** — feedback quality shapes subsequent strategy selection (used for cadence/feedback tables) — https://pmc.ncbi.nlm.nih.gov/articles/PMC7912127/

## Privacy and data minimization

- **NIST Privacy Framework 1.0** — data minimization and limited retention patterns (archive TTL rationale) — https://www.nist.gov/privacy-framework
- **OWASP — Sensitive Data Exposure** — keep secrets and raw private dumps out of insight queues — https://owasp.org/www-project-top-ten/

## Claim handling notes

| Claim class in skill | Handling |
|----------------------|----------|
| Queue cap = 3, archive TTL = 30 days | Project policy defaults; adjustable via user feedback, not external SLA |
| Adaptive frequency bands | Heuristics for engagement; not clinical or medical guidance |
| Profile labels (developer, etc.) | UX taxonomy only; confirm before high confidence |
| No executable output | Safety contract; stronger than generic “be careful” advice |

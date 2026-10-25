## Description:

Typed knowledge graph for structured agent memory and composable skills.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oswalpalash](https://clawhub.ai/user/oswalpalash)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to create, query, relate, and validate typed ontology records for shared agent memory, project state, tasks, events, documents, and cross-skill data access.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist and delete shared ontology memory records in the workspace.

Mitigation: Use it only in workspaces where persistent ontology state is intended, review destructive operations before execution, and keep recoverable history for important memory files.

Risk: Credential-like ontology entries could expose sensitive values if users store secrets directly.

Mitigation: Store only secret references, not secret values, and validate records for forbidden credential properties before relying on shared memory.

Risk: Persistent ontology state may become trusted cross-skill context even when records are stale, incorrect, or insufficiently reviewed.

Mitigation: Run validation before depending on ontology records and add human confirmation for memory that drives high-impact actions.

## Reference(s):

- [Ontology Schema Reference](references/schema.md)
- [Query Reference](references/queries.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON, YAML, Python, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local ontology records in JSONL storage and optional YAML schema updates when the CLI is used.]

## Skill Version(s):

1.0.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

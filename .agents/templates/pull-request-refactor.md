# Pull Request Template

Use this template when creating a skill refactor pull request. Replace all placeholder text with actual evidence from the refactor.

---

# <skill-name> Skill Refactor

## Why This Skill

<Explain why this skill was selected for refactor.>

## Nonconformities Found

### Gate 1: Agent Skills Format Compatibility
- **<SPEC|VALIDATOR|RECOMMENDATION>**: <finding>
- ...

### Gate 2: Official Resource Directories and Reference Paths
- **<SPEC|VALIDATOR|PROJECT|RECOMMENDATION>**: <finding>
- ...

### Gate 3: Persistent State Location
- **<SPEC|VALIDATOR|PROJECT|RECOMMENDATION>**: <finding>
- ...

### Gate 4: Related-Skill Metadata Integrity
- **<SPEC|VALIDATOR|PROJECT|RECOMMENDATION>**: <finding>
- ...

### Gate 5: Removal of Clawic Feedback and Promotional Content
- **<SPEC|VALIDATOR|PROJECT|RECOMMENDATION>**: <finding>
- ...

## File Changes

### Moved
- `<old-path>` → `<new-path>`
- ...

### Created
- `<path>` — <purpose>
- ...

### Deleted
- `<path>` — <reason>
- ...

### Rewritten
- `<path>` — <summary of changes>
- ...

## Semantic-Preservation Inventory

Record every pre-refactor operational rule, safety boundary, recovery path, threshold, platform caveat, state/data semantic, and user-visible example. A concise entry point is not evidence that the original behavior survived.

| Original item | Source | Disposition (`retain` / `move` / `split` / `replace` / `remove`) | Destination or replacement | Evidence / rationale |
|---|---|---|---|---|
| `<specific behavior>` | `<old-path>#<section>` | `<disposition>` | `<new-path>#<section>` | `<why this is equivalent-or-stronger, or why removal is justified>` |

For every `remove` entry, cite evidence that the content is obsolete, incorrect, duplicate of a canonical source, or prohibited. “Keep `SKILL.md` concise” is not a sufficient rationale. For every `replace` entry, explain why the replacement preserves the same outcome or is explicitly stronger without removing a user decision, recovery path, or portability boundary.

## Research Sources and Knowledge Updates

### <Topic 1> (e.g., Retention Benchmarks)
- **<source title>** — <what data or guidance was taken> via <full URL>
- ...

### <Topic 2> (e.g., CAC Benchmarks)
- **<source title>** — <what data or guidance was taken> via <full URL>
- ...

### Obsolete Knowledge Corrected
- <what was removed or replaced and why>
- ...

## Best-Practices and Description Optimization

- <improvement made>
- ...

## Darwin Skill Score

**Final score: <score>/100** ✓ (threshold: 80)

### Dimension Scores

| Dimension | Before | After |
|-----------|--------|-------|
| Frontmatter quality | <n>/7 | <n>/7 |
| Workflow clarity | <n>/12 | <n>/12 |
| Failure mode encoding | <n>/12 | <n>/12 |
| Checkpoint design | <n>/6 | <n>/6 |
| Executable specificity | <n>/18 | <n>/18 |
| Resource integration | <n>/4 | <n>/4 |
| Overall architecture | <n>/12 | <n>/12 |
| Measured performance | <n>/23 | <n>/23 |
| Counter-examples and blacklists | <n>/6 | <n>/6 |
| **Total** | **<before>** | **<after>** |

### Key Improvements

- <improvement>
- ...

## Freud Cognitive Load and White Bear Corrections

Use `/freud-skill` (Mode 2: Diagnostic Optimization) to scan for patterns that increase cognitive load or trigger white bear effects. Apply only the 4 lenses appropriate for skills (Lens 1 and Lens 5 are for personas, not skills).

### Lenses Applied

| Lens | Focus | Patterns Found |
|------|-------|----------------|
| Lens 2: Positive vs Negative | Prohibitions that make prohibited behavior more salient | <count or "none"> |
| Lens 3: Consistency | Contradictory instructions causing unstable behavior | <count or "none"> |
| Lens 4: Anchoring precision | Vague instructions without concrete steps | <count or "none"> |
| Lens 6: Working space hygiene | Critical instructions buried, cognitive load exceeded | <count or "none"> |

### White Bear Corrections

For each prohibition pattern found, convert to positive definition:

| White bear (prohibition) | Positive definition |
|---|---|
| "Don't execute without confirmation" | "Verify conditions through output gates and proceed when met" |
| <pattern found or "No corrections required"> | <positive reframing or "N/A"> |

### Validator Regression Check

After applying Freud-based corrections, re-run the validator:

```bash
$ uvx --from skills-ref agentskills validate skills/<slug>
<output>
exit=<code>
```

- Validator still passes: <✓|✗>
- Gates regressed: <none or list specific regressions>

## Test Prompts and Results

All test prompts must be written in English for consistency across the skill library.

```json
[
  {"id": 1, "prompt": "<typical user request in English>", "expected": "<expected behavior>", "actual": "<actual output>", "pass": <true|false>},
  ...
]
```

**Results: <n>/<total> passed**

## Verification Commands and Results

### Official Validator

```bash
$ uvx --from skills-ref agentskills validate skills/<slug>
<output>
exit=<code>
```

### Gate Checks

- Gate 1: <✓|✗> <result>
- Gate 2: <✓|✗> <result>
- Gate 3: <✓|✗> <result>
- Gate 4: <✓|✗> <result>
- Gate 5: <✓|✗> <result>

## Commit History

```
<commit-hash> darwin(<skill>): <summary>
<commit-hash> optimize(<skill>): <summary>
<commit-hash> research(<skill>): <summary>
<commit-hash> refactor(<skill>): <summary>
```

## Unresolved Risks

<list any unresolved risks or blocked checks, or "None">

## Newly Discovered Anti-Patterns

<list any newly discovered recurring anti-patterns that may require a completion-definition update, or "None (all anti-patterns covered by existing Gate definitions)">

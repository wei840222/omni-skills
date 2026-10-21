# Research Pipeline — Vibe Research

Human-directed, AI-led cycle. Scale source volume to the agreed depth budget; do **not** treat a fixed "100+ sources" quota as mandatory for every ask.

## Depth budgets

| Budget | Typical scope | Source target (guidance) |
| --- | --- | --- |
| Quick | Orient + answer one focused question | 5–15 high-signal sources |
| Standard | Gap map + synthesis + recommendations | 15–40 sources with triangulation on key claims |
| Thorough | Full cycle through protocol + draft report | Broad sweep plus deep reads on contested claims |
| Exhaustive | Prefer handing off to `in-depth-research` | Halt criteria and multi-engine depth first |

Confirm budget with the human before a large literature sweep.

## Phase 1: Gap Identification

**Goal:** Find what is unknown, contested, or under-explored.

### Process

1. Receive research question, constraints, and success criteria from the human.
2. Scan literature and practitioner sources appropriate to the depth budget.
3. Identify established consensus, active debates, unexplored territories, and methodological gaps.

### Output

```markdown
## Knowledge Gap Analysis: [Topic]

### Established (High confidence)
- [Fact 1] — supported by [n] independent sources

### Contested (Debate exists)
- [Claim] — [Source A] argues X; [Source B] argues Y

### Unexplored (Opportunity)
- [Gap 1] — no literature found / mentioned but not studied

### Recommended Focus
[Which gap to pursue and why]
```

## Phase 2: Literature Synthesis

**Goal:** Build a cited understanding from sources.

### Process

1. Retrieve papers, reports, datasets, and primary docs.
2. Extract key claims with citations (source, locator, short quote when useful).
3. Cross-reference findings; separate consensus from outliers.
4. Note methodology patterns and quality limits of the evidence base.

### Techniques

- Semantic / keyword search, citation chaining, author follow-ups
- Claim extraction with verification against primary sources
- Temporal view: how consensus changed

### Output

Synthesized summary with key findings (cited), methodology patterns, consensus vs outliers, and source-quality notes.

## Phase 3: Hypothesis Generation

**Goal:** Propose testable claims that address identified gaps.

### Process

1. Review gaps and synthesis.
2. Draft candidate hypotheses.
3. Score each for testability, novelty, and feasibility under the available budget.
4. Rank and recommend one primary path.

### Output

```markdown
## Hypothesis Candidates

### H1: [Statement]
- Testability: [High/Medium/Low]
- Evidence for / against: [...]
- Test approach: [brief methodology]

### Recommendation
Pursue H[n] because [reasoning]
```

## Phase 4: Analysis Design

**Goal:** Define a reproducible methodology.

### Components

1. Data requirements and inclusion/exclusion rules
2. Analytical methods
3. Success / falsification criteria
4. Confounds and bias checks
5. Reproducibility plan (steps, tools, artifacts)

### Output

Research protocol ready for human methodology review **before** heavy execution.

## Phase 5: Execution

**Goal:** Run the analysis and gather results.

### Agent responsibilities

- Execute the approved protocol
- Log steps, decisions, and anomalies
- Iterate only within the approved scope; request a checkpoint for course changes

### Human checkpoints

- Validate methodology before execution
- Review intermediate results when stakes are high
- Approve material course corrections

## Phase 6: Synthesis

**Goal:** Turn findings into actionable, cited knowledge.

### Output options

- Executive summary (≤1 page)
- Full research report with methodology
- Citation list
- Reproducibility package (commands, data pointers, step log)

### Structure

1. Question addressed
2. Methodology used
3. Key findings (cited)
4. Limitations and confidence
5. Implications
6. Future directions / open gaps

## Routing notes

- User already supplied the documents → prefer `synthesize`.
- Need exhaustive answering with halt criteria → prefer `in-depth-research`.
- Discovery across engines only → start with `multi-engine-web-search`, then return here if a full cycle is still needed.

# Core Rules and Traps

## Output contract

When this skill is active, produce a naming deliverable that is decision-ready.

| Output | Purpose |
|--------|---------|
| Brief summary | Lock the object, audience, constraints, and success criteria |
| Option families | Show structured variation instead of random isolated names |
| Shortlist with scores | Explain why finalists survive the filters |
| Recommendation | Pick one winner plus two backups |
| Risk notes | Flag collisions, ambiguity, rollout risk, or missing verification |

If the user only asks for ideas, keep the internal structure. Raw lists without rationale usually create another round of confusion instead of a decision.

## Naming lanes

Identify the lane first. Good names are surface-specific.

| Lane | Optimize for | Common failure | File |
|------|--------------|----------------|------|
| Product or brand | Memorability, distinction, room to grow | Sounds clever but says nothing | `assets/brief-template.md` |
| Feature or workflow | Instant comprehension in UI and docs | Marketing language hides the job | `references/surface-patterns.md` |
| API, endpoint, schema, method | Consistency, predictability, low ambiguity | Mixed verbs, nouns, and tense | `references/surface-patterns.md` |
| Package, repo, command, file, folder | Scan speed, exactness, maintainability | Decorative naming hurts retrieval | `references/surface-patterns.md` |
| Internal codename | Fast alignment and low collision | Leaks into public language accidentally | `references/rename-playbook.md` |

## Core rules

### 1. Start with the RALLY brief before generating names
- Use `assets/brief-template.md` to lock the asset, audience, lexical guardrails, and why the name matters.
- RALLY stands for **Role, Audience, Limits, Lexicon, Yardstick**.
- If the brief is vague, clarify Role and Yardstick before ideation. Ambiguous briefs create attractive but unusable names.

### 2. Separate utility naming from brand naming
- Utility surfaces such as features, APIs, files, and commands bias toward clarity and predictability.
- Brand surfaces may trade a little exactness for recall, story, and distinctiveness, while still remaining comprehensible fast enough for the context.
- Judge feature names with the feature rubric, not the company-name rubric. The lane defines the winning tradeoff.

### 3. Generate option families, not one flat list
- Create at least three families with different angles: descriptive, metaphorical, compound, outcome-first, or system-consistent.
- Keep siblings internally coherent so the user can compare strategies, not only individual words.
- A strong family often reveals the right direction even when none of the exact first-pass candidates survive.

### 4. Run every finalist through the CLASH scorecard
- Use `references/scorecard.md` before recommending a winner.
- CLASH stands for **Clarity, Load, Adjacency, Search collision, Harm**.
- A name is ready when it survives spelling, pronunciation, ambiguity, namespace overlap, and negative connotations—not only when it sounds good.

### 5. Match the surrounding system before optimizing the single name
- Check product architecture, menu hierarchy, endpoint family, file layout, or taxonomy before choosing the local label.
- Prefer the name that makes the whole system easier to scan and predict, even when a flashier local option exists.
- Prefer consistency across sibling names over isolated cleverness.

### 6. Recommend one winner, two backups, and the deciding reason
- Provide exactly one clear recommendation with two backups, unless the user explicitly asks for open exploration.
- State why the winner wins in this context: better comprehension, lower collision risk, stronger recall, better family fit, or safer rollout.
- If legal, trademark, domain, or live namespace verification still matters, state that remaining check explicitly.

### 7. Treat renames as migrations
- A rename can break routes, docs, API clients, analytics, onboarding, and mental models.
- Use `references/rename-playbook.md` when the job modifies live systems or published language.
- Map what changes, which aliases are needed, and what must remain backward-compatible during transition.

### 8. Learn durable naming taste
- Store recurring constraints in local memory: words the user excludes, tone preferences, naming style, and family patterns that keep winning.
- Store only reusable signals that improve future naming quality.
- If the user rejects multiple options for the same reason, promote that reason into a durable rule under `<state_root>/`.

## Common traps

| Trap | Why it fails | Better move |
|------|--------------|-------------|
| Brainstorming before defining the object | Different people optimize for different jobs | Lock the brief first |
| Picking the cleverest name in the room | Clever often decays into explanation debt | Score for clarity and retrieval first |
| Mixing external and internal names | Teams start leaking placeholder language | Decide what is public, internal, and transitional |
| Renaming one node without the system | Adjacent labels become inconsistent | Audit sibling names before final choice |
| Using invented spelling for distinctiveness | Search, pronunciation, and trust degrade | Prefer real words unless the lane truly justifies invention |
| Confusing category fit with legal clearance | Similarity risk stays hidden | Mark live trademark or namespace verification as still required |
| Ending at "here are some ideas" | The user still has no recommendation | Pick a winner and defend it |

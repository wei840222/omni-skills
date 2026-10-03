# Setup — Help Center

Load when `<state_root>/memory.md` is missing or empty, or when integration preference is still unset.

## First-run transparency

Tell the user what local planning files this skill can create after consent:

- Workspace path: the already-resolved `<state_root>/` (never a literal folder named `<state_root>`)
- Decision memory: `<state_root>/memory.md`
- Optional later files: `<state_root>/provider-score.md`, `<state_root>/content-inventory.md`, `<state_root>/rollout-log.md`

Create or modify files only after named user confirmation that includes the real path.

## First conversation flow

### 1. Integration preference

Ask once how this skill should activate:

- Automatically when the user mentions help center, support docs, knowledge base, or ticket deflection
- Only when explicitly requested

Store the answer in `Status.integration` inside `<state_root>/memory.md` after consent.

### 2. Situation mapping

Collect the minimum support-model inputs before recommendations:

- Current provider or stack
- Team size and support channels
- Monthly ticket volume and SLA expectations
- Required integrations and compliance boundaries

### 3. Scope the immediate objective

Clarify a single primary objective:

- New help center build
- Migration from an existing platform or doc set
- Operational optimization of an existing help center

Propose one focused plan for that objective. Defer secondary work.

## Allowed learning

Store only explicit user information that improves later decisions:

- Approved provider preferences
- Budget, compliance, and staffing constraints
- Decisions and rejected options with rationale and date

Base preferences on explicit user statements, not inferred private data.

## Boundaries

- Keep local files inside the resolved `<state_root>/`
- Require explicit approval before editing provider production content
- Ask before creating or modifying any local planning file
- If the user declines setup, continue with stateless guidance and skip durable writes

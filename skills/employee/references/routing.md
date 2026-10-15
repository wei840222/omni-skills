# Task Routing

## Routing Decision Flow

```
Request arrives
    │
    ├─ Explicit mention: "Luna, do X"
    │   └─ Route to Luna directly
    │
    ├─ Explicit self: "I'll handle this"
    │   └─ Main agent handles
    │
    └─ No mention: analyze request
         │
         ├─ Matches employee role?
         │   ├─ High confidence → suggest: "Want Luna to handle this?"
         │   └─ Auto-route if user enabled auto-delegation
         │
         └─ Generic/orchestration?
             └─ Main agent handles
```

## Role Matching

Load `<state_root>/registry.json` on each request. Match against:

1. **Role keywords**: "research" → Research Assistant
2. **File patterns**: reviewing `.py` files → Code Reviewer
3. **Task type**: "write tests" → Test Writer

Skip employees whose registry status is `paused` or `retired`.

## Auto-Delegation Rules

User can enable per-employee:

```json
"autoDelegation": {
  "enabled": true,
  "confidenceThreshold": 0.8,
  "excludePatterns": ["urgent", "confidential"]
}
```

Before auto-routing, confirm the employee autonomy level can perform the
requested effect (shadow never acts; draft-only stops before send/commit).

## Execution Flow

When routing to an employee:

```
1. Load <state_root>/employees/{name}/employee.json → get config
2. Load linked, embedded, or registry skill
3. Inject <state_root>/employees/{name}/memory/context.md as context
4. Spawn as a subagent with the employee's model
5. Execute the task inside permissions
6. Log to <state_root>/employees/{name}/logs/YYYY-MM-DD.md
7. Update stats in employee.json
8. Return the result to the main agent
```

## Handoff Protocol

When an employee needs to escalate:

```
1. Employee recognizes an escalation trigger
2. Returns: "ESCALATE: [reason] | context: [summary]"
3. Main agent receives and presents to the user
4. User decides: handle manually or redirect
```

## Multi-Employee Tasks

For complex work that needs more than one employee:

```
1. Main agent decomposes the task
2. Route subtasks to relevant active employees
3. Collect results
4. Synthesize and present
```

Example:
- "Research X and write a report"
- → Research Assistant: gather information
- → Writer: draft report from research
- → Main agent: review and deliver

## Routing Standards

- Route only to `active` employees listed in the registry.
- Keep work inside each employee's permissions and file-access allowlist.
- Check autonomy level before any external effect.
- Keep urgent or confidential tasks with the main agent unless the user
  explicitly assigns them.

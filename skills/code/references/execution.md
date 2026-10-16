# Execution guidance

Reference for executing multi-step implementations.

## Recommended flow

When the user approves a step:

1. Execute that step
2. Verify it works
3. Report completion to the user
4. Wait for the user to approve the next step

## Progress tracking

Show the user the current state:

```
- [DONE] Step 1 (completed)
- [WIP] Step 2 <- awaiting user approval
- [ ] Step 3
- [ ] Step 4
```

## When to pause and ask the user

- Before starting any new step
- When encountering an error
- When a decision is needed (A vs B)
- When credentials or permissions are needed

## Error handling

If an error occurs:

1. Report the error to the user
2. Suggest possible fixes
3. Wait for the user decision on how to proceed

## Patterns to follow

- Report completion of each step
- Ask before proceeding to the next step
- Let the user decide the retry strategy
- Keep the user informed of progress

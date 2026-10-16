# Planning reference

Consult when breaking down a multi-step request.

## When to plan

- Multiple files or components
- Dependencies between parts
- UI that needs visual verification
- User says "build", "create", or "implement"

## Step format

```
Step N: [What]
- Output: [What exists after]
- Test: [How to verify]
```

## Good steps

- Clear output (file, endpoint, screen)
- Testable independently
- No ambiguity in what "done" means

## Anti-patterns

- Steps with vague outputs
- Steps lacking a defined test
- Steps relying on undefined prior steps

## Bypass planning for

- One-liner functions
- Simple modifications
- Questions about existing code

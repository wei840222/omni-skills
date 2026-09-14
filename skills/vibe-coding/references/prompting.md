# Prompting Techniques for Vibe Coding

## The Specificity Spectrum

**Too vague** (AI guesses wrong):
> "Make a dashboard"

**Just right** (clear intent, room for AI judgment):
> "Dashboard with 3 KPI cards (revenue, users, churn), line chart for 30-day trend, table of recent signups. Dark theme, Tailwind."

**Over-specified** (micromanaging, defeats the purpose):
> "Create a div with class flex gap-4, inside put 3 divs each with..."

## Effective Prompt Patterns

### 1. Context + Task + Constraints
```
[Context] I'm building a SaaS billing system with Stripe
[Task] Add a webhook handler for subscription.updated events
[Constraints] Use existing error handling pattern in /lib/errors.ts
```

### 2. Behavior Description
Instead of implementation details:
- Ineffective: "Add an if statement to check if user.plan === 'pro'"
- Effective: "Pro users should see the advanced analytics tab"

### 3. Error Pasting
Just paste the error. No explanation needed:
```
TypeError: Cannot read properties of undefined (reading 'map')
    at UserList (UserList.tsx:23)
```

### 4. Incremental Building
Build incrementally, asking for one feature at a time:
1. "Create user signup form with email/password"
2. "Add validation: email format, password 8+ chars"
3. "Add loading state and error display"
4. "Connect to Supabase auth"

### 5. Reference Existing Code
```
"Add a new endpoint for orders, following the same pattern as 
/api/users/route.ts"
```

## Anti-Patterns

### Vague Adjectives
- Ineffective: "Make it better" / "Make it cleaner" / "Make it more professional"
- Effective: "Add loading skeleton, reduce padding to 8px, use Inter font"

### Unbounded Scope
- Ineffective: "Build a complete e-commerce platform"
- Effective: "Build product listing page with grid of cards, filter by category, sort by price"

### Assuming Context
- Ineffective: "Fix the bug" (which bug?)
- Effective: "Users can't checkout when cart has 0 items — should show error message"

### Multiple Unrelated Tasks
- Ineffective: "Add dark mode, fix the login bug, and set up email notifications"
- Effective: One task per prompt. Chain them.

## Recovery Prompts

When stuck:
- "Let's start fresh. I need [X]. What's the simplest approach?"
- "Ignore previous attempts. Describe what you would build for [requirement]"
- "The approach isn't working. What are 3 alternative ways to do this?"

When AI is confused about codebase:
- "Read [file] and summarize what it does before making changes"
- "List all files that would need to change for [feature]"

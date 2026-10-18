# Setup — Meal Planner

Use this file only after `<state_root>` is resolved per `SKILL.md`. When
`<state_root>/meal-planner/` does not exist or is empty, guide onboarding in
plain language.

## Storage notice

On first use, tell the user:

- meal plans and preferences will be saved as markdown under
  `<state_root>/meal-planner/`
- they can open or edit those files anytime
- nothing is created until they want durable planning state

## Getting started

### 1. Integration preference

Ask early:

- help whenever food planning comes up, or only on explicit ask?
- proactive reminders, or wait for the user?

### 2. Household basics

**Who is eating**

- solo vs household
- kids or regular guests with distinct tastes

**Dietary needs (safety-critical)**

- allergies, intolerances, foods they refuse
- vegetarian / pescatarian / other approaches
- severity: allergy vs intolerance vs preference

**Time and effort**

- weeknight cooking minutes
- cooking as enjoyment vs chore

**Budget (optional)**

- track spend vs menus only
- if they give a number, store it as a user-stated target rather than an
  official USDA band

### 3. Preferences (build over time)

Keep the first conversation short. Capture favorites, comfort foods, recurring
meals, and disliked ingredients as they appear.

### 4. First durable files

After consent, create:

- `<state_root>/meal-planner/memory.md` from `assets/data-templates.md`
- empty `weeks/`, `recipes/`, `shopping/`, `inventory/`, `templates/`,
  `archive/` as needed

Legacy `~/Clawic/data/meal-planner/` or `~/clawic/meal-planner/` trees move only
when the user asks; report source and destination in one line.

## Status values for memory.md

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning preferences | Gather context, suggest gently |
| `complete` | Solid household model | Plan confidently |
| `paused` | User said "not now" | Work with what exists |
| `never_ask` | User said stop probing | Never probe for preferences |

## Key principles

- Restrictions are sacred — check before suggesting
- Learn from feedback — "too much work" becomes a time constraint
- Observe patterns — history often beats questionnaires
- Pace questions — preferences emerge while planning together
- Update `last` on each planning session

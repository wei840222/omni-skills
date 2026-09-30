# Setup — Naming

Read this when the resolved `<state_root>/` does not exist or is empty. Start naturally and make the skill useful immediately.

## Attitude

Be decisive, language-sensitive, and practical. Good naming reduces friction across teams, docs, and interfaces.

## Priority order

### 1. Integration first

Within the first exchanges, establish how naming should activate:

- Jump in when the user asks for names, renames, labels, taxonomy cleanup, or naming consistency
- Intervene when a proposed name is ambiguous, collision-prone, or inconsistent with the system
- Prefer option families, a single recommendation, or both depending on the user

If the user approves persistence, store this activation behavior in `<state_root>/memory.md`.

### 2. Capture durable context

Learn the smallest durable context that changes naming quality:

- What they name most often: products, brands, features, APIs, files, or campaigns
- Preferred tone: plain language, sharper branding, technical exactness, or hybrid
- Words, tones, or patterns they consistently exclude
- Optimization target: UI labels, spoken conversation, searchability, or internal maintainability

Reflect the tradeoff you will optimize for instead of running a long questionnaire.
Start naming once activation preference and one real constraint are clear.

### 3. Create state only with approval

When persistence is approved, create the structure in `assets/memory-template.md` under the **resolved** directory path. Example after resolving to a real path such as `/workspace/naming`:

```bash
mkdir -p /workspace/naming/archive
touch /workspace/naming/memory.md /workspace/naming/briefs.md /workspace/naming/winners.md /workspace/naming/collisions.md
```

Replace the example path with the actual resolved root. Never mkdir a literal `<state_root>` string.

## What you are saving

Prefer reusable constraints over one-off brainstorm history:

- activation preference
- excluded words and tones
- namespace or taxonomy rules
- rollout constraints such as backward compatibility, docs burden, or localization risk
- winners and collision reasons that should shape later shortlists

## When setup is sufficient

Once activation preference is known and at least one real naming constraint is clear, conclude setup and begin assisting with a RALLY brief and option families.

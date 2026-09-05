## Core Rules

### 1. Verify Auth and Live Models Before Naming Any Route
- Start with `https://api.moonshot.ai/v1/models` and copy live model IDs from the response.
- Always rely on live model IDs from the API response when a workflow is failing, rather than remembered Kimi model names or stale examples.

### 2. Lock the Job to One Workload Before Tuning Prompts
- Classify the request as one of: fast chat, coding agent, long-context research, deterministic JSON, or migration debugging.
- Most bad Kimi advice comes from mixing several jobs into one oversized prompt and then blaming the model.

### 3. Treat Structured Output as a Separate Reliability Path
- If output feeds tools, code execution, or downstream writes, use strict schemas or a second normalization pass.
- Split open-ended reasoning and perfect machine-readable output into separate requests.

### 4. Keep Sensitive Data Out Unless the User Explicitly Approves It
- Redact secrets, customer identifiers, internal hostnames, and raw tokens before sending prompts externally.
- If the user wants repeatable Kimi workflows, save the redaction rule and approval boundary in `<state_root>/kimi/approvals.md` after confirming the first write.

### 5. Route by Deadline and Cost, Not Brand Habit
- Use the smallest Kimi route that can finish the current job reliably.
- For recurring workflows, save one primary route and one fallback route instead of debating models from scratch each time.

### 6. Separate Provider Migration Problems From Model Problems
- When moving from OpenAI-compatible code to Kimi, isolate the variable: base URL, auth env var, model ID, parser, or retry policy.
- Reproduce with one minimal payload before changing prompts, infrastructure, and business logic together.

### 7. Ask Before Creating Persistent State
- Work statelessly by default.
- Only create `<state_root>/kimi/` notes, approvals, or debug logs after the user wants continuity across Kimi tasks.
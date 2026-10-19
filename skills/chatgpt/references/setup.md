# Setup - ChatGPT

Read this when the resolved `<state_root>/` is missing or empty. Start helping
immediately while capturing only the context that changes how ChatGPT should be
used for this user.

## Attitude

Act like an operator for ChatGPT workflows. Make ChatGPT more reliable and
easier to trust without turning every request into prompt theater.

## Priority order

### 1. First: integration

Within the first exchanges, confirm when this skill should activate:

- every time the user mentions ChatGPT, GPTs, custom instructions, Projects,
  prompt engineering, or "make ChatGPT do X"
- only when they explicitly ask for help using ChatGPT
- only for selected workflows such as writing, research, or planning

If they confirm, store the activation preference in `<state_root>/memory.md`.

### 2. Then: workflow reality

Capture only the context that changes the solution:

- main jobs done in ChatGPT: writing, research, study, analysis, planning,
  support, ideation
- preferred surfaces already in use: normal chat, Temporary Chat, Projects,
  GPTs/plugins, custom instructions
- privacy tolerance: what must stay out of remembered chats or uploaded files
- output pain points: too generic, too long, too confident, too repetitive,
  ignores instructions
- desired output style: fast draft, structured outline, polished final, critic,
  or iterative collaborator

Proceed with the live task without formal onboarding. Learn while solving.

### 3. Finally: reusable defaults

Infer and confirm stable defaults:

- short prompt packets versus explicit detailed briefs
- whether multi-pass workflows are welcome or reserved for high-stakes tasks
- whether ChatGPT should ask clarifying questions before drafting
- which tasks deserve Temporary Chat, Projects, or a packaged GPT/plugin

Store reusable workflow choices, not transcripts.

## What you save locally

Persist only reusable information in `<state_root>/memory.md`:

- activation preference
- stable workflow defaults and tone
- privacy boundaries and no-go data categories
- preferred prompt packet shapes and QA strictness
- repeated failure modes that should be mitigated next time

Do not store secrets, raw private documents, or one-off details that will not
help future ChatGPT work.

## Golden rule

Improve the current ChatGPT problem first. Setup context exists to sharpen
future help rather than slow useful work now.

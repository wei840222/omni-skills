---
name: storybook
compatibility: "linux, darwin, win32"
description: Build component stories with proper args, controls, decorators, and testing patterns.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📖"}'
---

## Workflow

1. Identify the project's Storybook version, framework, and existing `.storybook/` configuration before changing a story.
2. Write the story with Component Story Format (CSF) and use `args`, `argTypes`, decorators, or a `play` function only when the requested behavior needs them.
3. Run the project's configured Storybook check or test command. If it fails, use the reported file, framework, and version to correct the story before retrying.
4. Read `references/storybook.md` when you need CSF examples, configuration guidance, interaction-test patterns, or compatibility notes.

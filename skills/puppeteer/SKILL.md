---
name: puppeteer
description: "Automate Chrome and Chromium browsers using Puppeteer. Use when executing web scraping, generating automated PDFs and screenshots, running end-to-end browser tests, or troubleshooting headless navigation."
metadata:
  openclaw: '{"emoji":"🎭","requires":{"bins":["node"]},"os":["linux","darwin","win32"],"displayName":"Puppeteer"}'
---

## Setup

On first use, read `references/setup.md` for integration guidelines.

## When to Use

User needs browser automation: web scraping, E2E testing, PDF generation, screenshots, or any headless Chrome task. Agent handles page navigation, element interaction, waiting strategies, and data extraction.

## Architecture

Scripts and outputs in `<state_root>/`. See `references/memory-template.md` for structure.

```
<state_root>/
├── memory.md       # Status + preferences
├── scripts/        # Reusable automation scripts
└── output/         # Screenshots, PDFs, scraped data
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Domain knowledge | `references/domain-knowledge.md` | When learning about Puppeteer capabilities. |
| Setup process | `references/setup.md` | On first use or when setting up the environment. |
| Memory template | `references/memory-template.md` | When reading or updating the project memory. |
| Rules & Traps | `references/rules-and-traps.md` | When reviewing core best practices and pitfalls. |
| Selectors guide | `references/selectors.md` | When needing to find or interact with DOM elements. |
| Waiting patterns | `references/waiting.md` | When handling navigation or waiting for elements. |

## State location

Puppeteer state may exist in `<workspace>/puppeteer/`, `<workspace>/memory/puppeteer/`, or `~/puppeteer/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/puppeteer/`, `<workspace>/memory/puppeteer/`, `~/puppeteer/`.
3. If none exists and state must be created, default to `<workspace>/puppeteer/`.

Use the selected `<state_root>` for every state operation in this skill. Ensure this directory exists before executing operations that write state.

## Security & Privacy

**Data that stays local:**
- All scraped data in <state_root>/output/
- Browser profile in specified userDataDir

**This skill does NOT:**
- Send scraped data anywhere
- Store credentials (you provide them per-script)
- Access files outside <state_root>/

---
name: vibe-coding
description: Direct the workflow and prompting strategy for vibe coding. Trigger when the user is using AI-native tools (Cursor, Bolt.new, Claude Code) to build prototypes or MVPs. Bypass this skill for security-critical or compliance-heavy production systems.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎸"}'
---

## What is Vibe Coding

Programming where you describe what you want and let AI generate code. You evaluate by results, not by reading every line. Coined by Andrej Karpathy (Feb 2025).

**Key distinction (Simon Willison):** If you review, test, and can explain the code — that's software development, not vibe coding. Vibe coding means accepting AI output without fully understanding every function.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Prompting techniques | `references/prompting.md` | When you need patterns for structuring prompts or recovering from AI mistakes. |
| Research-Plan-Implement workflow | `references/workflow.md` | When starting a new feature to ensure planning happens before code generation. |
| Rules files (.cursorrules, CLAUDE.md) | `references/rules-files.md` | When setting up or modifying project instructions for AI tools. |
| Common pitfalls and fixes | `references/pitfalls.md` | When the AI output is poor or the vibe coding process breaks down. |
| Tool selection by use case | `references/tools.md` | When deciding which AI tool (Cursor, Claude Code, Bolt, etc.) to use. |
| Research sources | `references/sources.md` | When citing origin definitions, tool docs, or refreshing Gate 6 anchors. |

## Core Rules

### 1. Define Intent Before Prompting
Vague prompts → vague results. Before touching your AI tool:
- What specific problem are you solving?
- What does "done" look like?
- What are the constraints (stack, integrations, flow)?

Bad: "Build a social media app"
Good: "Build a social feed: text posts (280 chars), follow users, chronological feed, likes/comments. Use React, Tailwind, Supabase."

### 2. Use Rules Files
Persistent context that teaches AI your conventions. Put it in once, applies to every interaction:
- Cursor: .cursorrules or .cursor/rules/
- Claude Code: CLAUDE.md
- Windsurf: .windsurfrules

See `references/rules-files.md` for templates.

### 3. Research-Plan-Implement
Before implementing, have AI explore and plan:
1. **Research**: "Read the auth module, explain how sessions work"
2. **Plan**: "Write the files you'll modify and changes in each"
3. **Implement**: Only after reviewing the plan

Catching misunderstanding during planning = 10x cheaper than debugging cascading errors.

### 4. When to Intervene vs Let It Flow
- **Let it flow**: Scaffolding, UI components, exploring ideas
- **Intervene**: Auth, payments, data handling, anything security-adjacent
- **Always review**: Database schemas, API permissions, user data handling

### 5. Test After Every Change
AI generates code that looks flawless but has subtle bugs. After every change:
- Run test suite
- Manually test the affected feature
- Check console for errors
- Verify happy path AND edge cases

### 6. Paste Errors, Let AI Fix
The Karpathy move: copy error message, paste with no comment, usually it fixes it. If AI can't fix after 2-3 attempts, describe the behavior you want instead.

### 7. Constraint Anchoring
Set explicit boundaries:
- Length: "Under 50 lines of code"
- Format: "Only the modified function, not entire file"
- Scope: "Limit changes exclusively to the payment flow"
- Style: "Follow existing pattern in UserService.ts"

### 8. Know When Vibe Coding is Appropriate
**Good for**: Prototypes, MVPs, internal tools, weekend projects, UI components, boilerplate, learning
**Bad for**: Security-critical code, performance-critical code, compliance-heavy domains, long-term production systems

### 9. Experienced Developers + Vibe Coding = Superpowers
The best vibe coders understand architecture, spot bad AI output, and know when to intervene. If you can't evaluate whether AI produced good code, you need to learn more before vibe coding production systems.

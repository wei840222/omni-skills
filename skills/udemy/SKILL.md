---
name: udemy
description: "Design and manage Udemy courses by assisting with curriculum planning, script writing, and compliance while strictly adhering to human-in-the-loop and GenAI disclosure policies."
metadata:
  openclaw: '{"emoji":"🎓","displayName":"Udemy"}'
---

## Quick Reference

| Area | What the Agent Does | When to load | Reference |
|------|---------------------|--------------|-----------|
| Domain Info | Understand Udemy policies, GenAI rules, and SEO trends | When initiating a new course project or checking compliance | `references/research.md` |
| Planning | Niche research, competitor analysis, curriculum design | When the user asks to brainstorm or plan a course | `references/planning.md` |
| Production | Scripts, slides, quizzes, supplementary materials | When creating the actual course content | `references/production.md` |
| Publishing | Description, SEO, pricing, thumbnails | When preparing to launch or market the course | `references/marketing.md` |
| Management | Q&A drafts, review responses, content updates | When the course is live and the user needs to engage students | `references/management.md` |
| Workspace | Organizing the course files and tracking status | When managing local course files and tracking states | `references/workspace.md` |
| Compliance | General legal and terms of service guidelines | When handling sensitive topics or platform policies | `references/legal.md` |

## State Location
This skill maintains state for course workspaces.
1. The canonical state directory is `<state_root>/udemy/`.
2. Rely exclusively on the `<state_root>` convention for all path resolutions.
3. If the directory does not exist, create it.

## Critical Rules

1. **Human-in-the-loop MANDATORY** — Agent assists content creation, human reviews ALL outputs before publishing. Udemy prohibits fully AI-generated courses.
2. **Disclose AI usage** — Udemy requires disclosure when AI tools are used in course creation. Add disclosure to course description.
3. **Manual Execution** — Instruct the user to handle all platform actions, uploads, and logins manually.
4. **Quality over quantity** — Focus on creating valuable courses, not mass-producing low-effort content.
5. **Verify policies** — Udemy's GenAI policy changes. User must verify current terms at udemy.com before publishing.

## AI Content Policy

- ✅ AI-assisted content creation (outlines, scripts, drafts)
- ✅ AI-generated visuals/graphics (if high quality)
- ✅ AI for research and information gathering
- ❌ Minimal instructor input (Fully AI-generated courses)
- ❌ Raw AI outputs without human polish
- ❌ Hiding AI usage from students

**Disclosure required**: "This course contains content created with the assistance of AI tools."

## Disclaimer

This skill provides educational guidance on course creation best practices. It does not automate interactions with Udemy or circumvent platform policies. Users are solely responsible for complying with Udemy's Terms of Service and GenAI Policy.

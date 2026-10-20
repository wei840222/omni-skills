---
name: documentation
description: >
  Plan, write, restructure, and maintain technical documentation: README front
  doors, Diátaxis information types (tutorial/how-to/reference/explanation),
  API docs, code examples, versioned docs, troubleshooting, and freshness
  reviews. Use when the user asks to document a project, fix a weak README,
  split mixed docs, write API reference, keep docs next to code, or stop docs
  from rotting. Prefer `markdown` for syntax/format conversion, `writing` for
  general prose voice, `copywriting` for marketing persuasion, `api` for
  client/integration debugging, and `book-writing` for long manuscripts.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📚"}'
  related-skills: '{"api":"Debug or integrate third-party APIs when the task is client behavior rather than documenting an API surface.","book-writing":"Plan and revise long manuscripts when the deliverable is a book, not product docs.","copywriting":"Write persuasive marketing copy when the goal is conversion rather than accurate how-to or reference docs.","markdown":"Fix Markdown syntax, conversion, or parser compatibility after the documentation structure is decided.","writing":"Adapt general prose voice and tighten non-doc writing once documentation structure is settled."}'
---

This skill is stateless. It does not store local configuration or persistent user state.

## When to load

Load this skill to plan, draft, restructure, or audit **technical documentation**. Prefer it when the user needs README essentials, Diátaxis type selection, API reference completeness, example quality, versioned docs, troubleshooting searchability, or freshness/maintenance patterns.

Do **not** load as the primary skill for Markdown syntax conversion (`markdown`), general voice rewriting (`writing`), marketing persuasion (`copywriting`), third-party API client debugging (`api`), or multi-chapter manuscripts (`book-writing`).

## Workflow

1. Identify audience, product surface, and the user's immediate job (first success, task completion, lookup, or understanding).
2. Choose one primary Diátaxis type for the page or section; split mixed pages instead of blending tutorial and reference.
3. Draft or rewrite against the matching checklist below. Keep examples runnable and version-pinned when versions matter.
4. Run the delivery check, then return the documentation first.

## Diátaxis types

Use one primary type per page:

| Type | User need | Shape |
|------|-----------|-------|
| Tutorial | Learning-oriented first success | Guided path with a known good ending |
| How-to guide | Task-oriented goal | Steps to solve a specific problem |
| Reference | Information-oriented lookup | Exhaustive, accurate, complete |
| Explanation | Understanding-oriented context | Why it works this way; design background |

## README essentials

A README is the front door. Include:

1. One-sentence description of the problem solved
2. Installation with a copy-paste command that works
3. Quick start with a minimal runnable example and expected output
4. Link to full docs rather than cramming the entire manual into the README

Missing any of these usually loses users before they try the product.

## Code examples

- Test every example; untested examples rot
- Show complete runnable code with imports/setup, not orphan fragments
- Include expected output so the reader can confirm success
- Version-pin install commands when the API or CLI surface is version-sensitive

## API documentation

Every endpoint needs method, path, parameters, request body, response, and error codes. Prefer real request/response bodies over schema-only descriptions. Include authentication in examples. Put rate limits and pagination near the top of the resource. Document error responses with the same care as success responses.

## Freshness and maintenance

Docs that drift are worse than missing docs. Prefer:

- Docs in the same repo and PR as code
- CI link checks and runnable examples as tests
- Explicit review dates when freshness matters
- Archive or delete outdated pages instead of leaving stale certainty

High-churn surfaces: screenshots, hardcoded version numbers, external links, "current" claims, and forgotten experimental warnings after GA.

## Common failures

- Documenting implementation internals instead of user workflows
- Assuming context without defining acronyms or prerequisites
- Wall-of-text pages without headings, bullets, or code blocks
- "See X" without a working link
- Treating changelog entries as usage documentation

## Writing style

- Imperative mood: "Run the command"
- Second person: "you"
- Present tense: "This returns X"
- One idea per sentence; active voice

## Searchability and versioning

- Use words users search for, including verbatim error strings in troubleshooting
- Prefer plain headings such as "Getting Started" over clever titles
- Keep major versions on separate paths (`/docs/v2/`) with migration guides
- Mark deprecations explicitly; do not silently delete a still-supported path

## Delivery check

Before returning docs, confirm:

1. One primary Diátaxis type is clear for each page or major section
2. README / API / example checklists that apply are complete
3. Examples are runnable or explicitly marked as schematic
4. Related work is routed to `markdown`, `writing`, `copywriting`, `api`, or `book-writing` when those skills own the task

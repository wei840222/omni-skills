---
name: software-engineer
description: >
  Coach production software architecture, clean layer boundaries, typed error
  handling, pragmatic YAGNI trade-offs, and test-pyramid practices. Use when the
  user asks how to structure services, choose abstractions, write PR-ready code,
  design errors/boundaries, or decide monolith vs split before coding. Prefer
  `code` for plan→execute→verify delivery loops, `coding` for durable style
  preferences, `developer` for ticket-to-merge / CI / on-call, `review-code` for
  an existing PR/diff, `software-architect` / `cto` for strategy-level doors, and
  language skills once the ask is language-specific. Not for unattended coding,
  inventing Kubernetes controllers, or company strategy outside engineering.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"👨‍💻"}'
  related-skills: '{"code":"Stepwise plan→execute→verify delivery with approval checkpoints.","coding":"Durable style, stack, and architecture preference memory across sessions.","developer":"Ticket-to-merge, CI parity, migrations, and on-call mitigation loops.","review-code":"Risk-first review of an existing PR or diff.","software-architect":"Deep system design and ADRs beyond implementation coaching.","cto":"Build-vs-buy, org scaling, and one-way door strategy before hands-on coding.","engineering":"Non-software engineering practice, units, and PE/permit boundaries.","agentic-coding":"PACT contract loops when merge-ready agentic delivery is the primary ask."}'
---

# Software Engineer

Knowledge-only coaching for production software implementation decisions. This
skill does not create or require a persistent state tree. Do not write runtime
notes into this package.

## When to use

- Architecture / layer-boundary questions before or during implementation
- Choosing abstractions, libraries, or storage with explicit trade-offs
- Error-handling, testing, and PR-ready code quality guidance
- Monolith-vs-services or YAGNI pressure when scale is unclear

Prefer other skills when:

- Stepwise coding with approvals and evidence → `code`
- Durable coding preference capture → `coding`
- Ticket/CI/on-call delivery loop → `developer`
- Reviewing an existing PR/diff → `review-code`
- Strategy / org / one-way doors → `cto` or `software-architect`
- Language-specific panics or idioms → the matching language skill

## Quick reference

| Topic | File |
|-------|------|
| Code patterns | `references/patterns.md` |
| Architecture decisions | `references/architecture.md` |
| Testing practices | `references/testing.md` |
| Research sources | `references/sources.md` |

## Core rules

### 1. Read before write

- Check existing code style, patterns, and conventions before writing new code
- Respect the current stack — defer library swaps until explicitly requested
- Match naming conventions, formatting, and project structure already in place

### 2. Code that compiles

Every code block must:

- Have correct imports for the actual library versions in use
- Use APIs that exist in the project's dependency versions
- Pass basic syntax checks — no placeholder `// TODO: implement`

### 3. Minimal first

- Solve the specific problem, not hypothetical future problems
- Add one abstraction when you have three concrete cases, not before
- Skip features that only might be needed; implement features that are needed

### 4. Errors as first-class citizens

```javascript
// Anti-pattern: empty catch
catch (e) {}

// Anti-pattern: log without typed context
catch (e) { console.log(e) }

// Preferred: typed domain error with context
catch (e) {
  logger.error('signup.insert_failed', { error: e, input: safeInput });
  throw new DomainError('User create failed', 'USER_CREATE_FAILED', { cause: e });
}
```

- Prefer typed errors over generic strings
- Include context: what operation failed, with what non-sensitive input
- Distinguish recoverable vs fatal errors

### 5. Boundaries and separation

| Layer | Contains | Out of scope |
|-------|----------|--------------|
| Handler/Controller | HTTP/CLI parsing, validation | Business logic, SQL |
| Service/Domain | Business rules, orchestration | Infrastructure details |
| Repository/Adapter | Data access, external APIs | Business decisions |

### 6. Explicit trade-offs

When making architectural choices, state:

- What you chose and why
- What you traded away
- When to revisit the decision

Example: "Using SQLite for simplicity. Trade-off: no concurrent writes. Revisit if sustained writes exceed about 1/sec."

### 7. PR-ready code

Before delivering any code:

- [ ] Remove dead code, commented blocks, or debug statements
- [ ] Keep functions near 20–30 lines; extract when longer
- [ ] Replace magic numbers with named constants
- [ ] Prefer early returns over nested conditionals
- [ ] Handle edge cases: null, empty, error states

## Code quality signals

**Senior code reads like prose:**

- Names explain "what" and "why", not "how"
- A junior understands it quickly
- Avoid cleverness that needs comments to explain

**Prefer boring code:**

- Predictable patterns
- Standard library over dependencies when reasonable
- Explicit over implicit

## Common traps

| Trap | Consequence | Prevention |
|------|-------------|------------|
| Inventing APIs | Code does not compile | Verify the method in current docs first |
| Over-engineering | Hours instead of minutes | Ask: "Do I have 3 concrete cases?" |
| Ignoring context | Wrong stack suggested | Read existing files before suggesting |
| Copy-paste without understanding | Hidden bugs later | Explain what the code does |
| Empty error handling | Silent production failures | Always log + type + rethrow/return |
| Premature abstraction | Complexity without benefit | YAGNI until proven otherwise |

## Pragmatic shipping

**Critical paths (do it right):**

- Authentication, authorization
- Payment processing
- Data integrity, migrations
- Secrets management

**Experimental paths (ship fast, iterate):**

- UI/UX features
- Admin panels
- Analytics
- Anything unvalidated with users

Critical-path test: "Can this wake me at 3am or lose money?"

## Honesty boundaries

This skill is knowledge-only guidance inside the conversation:

- It does not store data externally by itself
- It does not make network requests by itself
- It does not access files outside the current project unless the host already granted that tool for the task

Load `references/sources.md` when citing architecture, testing, or YAGNI claims, and prefer the pinned publishers over memory.

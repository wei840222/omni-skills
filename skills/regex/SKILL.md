---
name: regex
description: Write, debug, and optimize regular expressions across JavaScript, Python, PCRE, and Go engines. Use when matching, extracting, validating, replacing text, explaining regex behavior, or diagnosing regex performance.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔍"}'
---

# Regular Expressions

Use this workflow to produce an engine-correct pattern and an explanation that a user can test.

## Workflow

1. **Identify the engine and operation.** Ask which language, regex engine, and operation (`match`, `search`, `replace`, or validation) apply when they are not stated. Use the engine's documentation before relying on lookarounds, named groups, Unicode properties, or flags.
2. **Define the match boundary.** State whether the pattern targets an entire string, a substring, or repeated matches. Use anchors such as `^` and `$` only when the whole input must match.
3. **Build from literals outward.** Escape literal metacharacters, then add character classes, groups, quantifiers, and assertions one at a time.
4. **Explain and test.** Provide the exact pattern, explain every group and flag, and include representative match and non-match cases. Test empty input, delimiters, Unicode where relevant, and long near-matches.
5. **Choose a safer tool when structure matters.** Use an HTML, XML, URL, or language parser for nested or fully specified formats; use regex for bounded text patterns and extraction.

## Core Syntax

### Quantifiers and matching extent

- `*`, `+`, `?`, and `{m,n}` are greedy by default; append `?` for the shortest valid match, such as `<.*?>`.
- Use non-capturing groups `(?:...)` when grouping is needed without extracting a value.
- Use capturing groups `(...)` or the engine's named-group form when the caller needs a submatch or backreference.
- Write alternatives with explicit grouping when precedence changes the result: `ca(t|d)og` differs from `cat|dog`.

### Boundaries, classes, and escaping

- `^` and `$` are affected by multiline mode; verify the engine's line-ending behavior before using them for validation.
- `\b` is a zero-width word boundary. Its definition, especially for Unicode text, differs by engine.
- Use `[abc]`, `[^abc]`, ranges such as `[a-z]`, and shorthands such as `\d`, `\w`, and `\s` only after checking the target engine's character semantics.
- Escape a metacharacter when matching it literally. In host-language string literals, account for the language's own escaping layer; Python raw strings such as `r"\d+"` avoid a second backslash interpretation.

### Assertions and flags

- Lookahead assertions `(?=...)` and `(?!...)` inspect following text without consuming it.
- Lookbehind assertions `(?<=...)` and `(?<!...)` have engine-specific availability and width rules.
- State every flag used. Common examples are `i` (case-insensitive), `m` (multiline), `s` (dotall), and `u` (Unicode), but their syntax and behavior vary.

## Performance and Safety

- Prefer specific, mutually exclusive alternatives over nested ambiguous repetition. For example, redesign `(a+)+` rather than applying it to unbounded input.
- Use atomic groups or possessive quantifiers only in engines that support them and only after confirming they preserve the intended matches.
- Anchor a pattern when the task is full-string validation; for substring search, retain only the anchors the user needs.
- Escape user-provided literals with the host engine's built-in escaping function before combining them with a regex. In JavaScript, use `RegExp.escape()` where available or a reviewed equivalent.

## Engine Routing

Read `references/regex-engines.md` when selecting syntax or flags for JavaScript, Python, PCRE, or Go; it lists the capability differences and authoritative documentation URLs.

## Verification Checklist

Before returning a pattern, confirm:

- the target engine and host-language escaping are explicit;
- each group, assertion, quantifier, and flag is explained;
- positive, negative, boundary, and long-input cases are covered; and
- structured formats are routed to a parser when nesting or full semantic validation is required.

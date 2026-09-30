# Summarizer Memory

## Status
status: active
version: 1.0.3
last: YYYY-MM-DD
integration: pending | done | declined

## Context
<!-- User's typical summary needs, recurring audiences, channel preferences -->

## Preferences
default_length: standard
default_audience: general
default_mode: hybrid
output_language: same-as-source
delivery_channel: markdown
markers: plain
omission_note: when-material
verify_pass: long-only
store_summaries: index-only

## Audiences
<!-- Key audience profiles with specific preferences -->
<!-- key: email-or-handle -->
<!-- length_ceiling, jargon_tolerance, always_ask_for, never_include -->

## Glossary
<!-- Recurring acronyms, entities, domain terms that must survive compression -->
<!-- term: expansion | note -->

## Boxes
<!-- Dynamic file index. Each line is a read condition + destination -->
<!-- condition: <state_root>/path.md when <predicate> -->
<!-- The condition is evaluated at the start of the session; the file is opened only when true -->

## Due
<!-- Recurring or one-time deadlines the user wants tracked from summaries -->
<!-- YYYY-MM-DD | source | deadline | owner | status -->

## Templates
<!-- Approved recurring shapes; one line per template -->
<!-- <name>: <state_root>/templates/<name>.md — one-line note of when to use -->

---
*Updated: YYYY-MM-DD*

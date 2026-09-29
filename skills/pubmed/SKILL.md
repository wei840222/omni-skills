---
description: Trigger this when asked to search or evaluate biomedical literature,
  or construct queries. Loads PubMed research rules.
metadata:
  openclaw: '{"emoji": "🔬", "os": ["linux", "darwin", "win32"], "displayName": "PubMed"}'
name: pubmed
---
# PubMed Search and Evaluation

This skill provides comprehensive guidelines for querying PubMed, evaluating study designs, and critical appraisal.

## When to load

Load this skill when the user asks to:
- Construct PubMed queries, use MeSH terms, or apply filters.
- Evaluate the hierarchy of biomedical evidence (e.g., RCTs, systematic reviews).
- Perform critical appraisal of medical literature (e.g., assessing sample size, bias, or study methods).

## Instructions

1. **Load Reference Material**: Before providing PubMed query guidance or literature appraisal, you must read `references/guide.md`.
2. **Apply Structured Searching**: Use PICO framework and recommended query syntax (e.g., uppercase Boolean operators) detailed in the guide.
3. **Appraise Effectively**: Follow the study hierarchy and critical appraisal guidelines.

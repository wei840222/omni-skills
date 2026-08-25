---
name: word-docx
description: "Inspect, modify, and generate `.docx` (Office Open XML) files. Triggers on requests involving Microsoft Word documents, DOCX format, document styling, tracked changes, or layout preservation. Does not natively support legacy `.doc` or `.docm` files without conversion."
metadata:
  openclaw: '{"emoji":"📘","os":["linux","darwin","win32"],"displayName":"Word / DOCX"}'
  related-skills: '{"documents":"General document handling and format conversion.","brief":"Concise business writing and structured summaries.","article":"Long-form drafting and editorial structure."}'
---

## When to Use

Use when the main artifact is a Microsoft Word document or `.docx` file, especially when tracked changes, comments, headers, numbering, fields, tables, templates, or compatibility matter.

### Quick Reference Guide

| Reference File | When to load |
|---|---|
| `references/ooxml-format.md` | Load when needing foundational context on Office Open XML (OOXML) file structure and standardizations. |
| `references/best-practices.md` | Load for detailed rules on OOXML editing, styles, lists, layout, tracked changes, and common formatting traps. |

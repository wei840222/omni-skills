---
name: hindi
description: "Write natural, conversational Hindi or Hinglish. Use when generating informal Hindi messages, social posts, or dialogue using authentic phrasing and conversational registers instead of formal AI tone."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇮🇳"}'
---

## Intent and Scope

When generating Hindi text, default to a casual, human-sounding tone rather than formal or "pure" (शुद्ध) Hindi. Most native speakers use a mix of Hindi and English (Hinglish).

**Trigger:** Activate this skill whenever asked to draft, translate, or communicate in Hindi, especially for informal or conversational contexts (e.g., social media, chat, emails to peers).

## Instructions

- When requested to write in Hindi, load `references/formality.md` to understand default registers and pronouns.
- Load `references/hinglish.md` to grasp the natural mixing of English and Hindi.
- Load `references/expressions.md` for common fillers, casual shortcuts, and natural reactions.
- Only load `references/regional.md` if the user specifies a specific region (e.g., Mumbai, Delhi, UP).
- Load `references/script.md` to ensure consistency in writing script (Devanagari vs. Roman).

## Verification

Before outputting text, apply the "Native Test": Ask yourself if a native speaker would find the text too formal, lacking English mixing, or artificially pure. If so, rewrite it using a more casual Hinglish tone.

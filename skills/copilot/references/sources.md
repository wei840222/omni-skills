# Research Sources (Gate 6)

Primary references used to verify continuity, proactive assistance, and interruptibility guidance in this skill.

## Agent memory and continuity

- **Anthropic — Claude memory** — product guidance on remembering preferences and ongoing work across conversations: https://www.anthropic.com/news/memory
- **OpenAI — Memory and custom instructions** — how assistants retain durable user context without re-asking known facts: https://help.openai.com/en/articles/8590148-memory-faq
- **LangChain — Memory** — patterns for short-term vs long-term conversational memory: https://python.langchain.com/docs/concepts/memory/

## Proactive assistance and interruptibility

- **Apple Human Interface Guidelines — Notifications** — interrupt only when the content is timely and actionable: https://developer.apple.com/design/human-interface-guidelines/notifications
- **Google Material Design — Notifications** — prefer silent/no-interrupt paths unless the user needs immediate attention: https://m3.material.io/styles/notification/overview
- **Microsoft — Designing proactive experiences** — proactive prompts should add clear value and respect user focus: https://learn.microsoft.com/en-us/windows/apps/design/shell/tiles-and-notifications/

## Local state and privacy boundaries

- **OWASP — Sensitive Data Exposure** — keep personal work context on the user's filesystem; avoid shipping state to third parties by default: https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure
- **NIST SP 800-88 Rev. 1** — user-controlled deletion of local state remains a valid privacy control: https://csrc.nist.gov/pubs/sp/800/88/r1/final

## Obsolete knowledge corrected

- Removed promotional homepage frontmatter and nested legacy metadata blocks.
- Replaced hard-coded vendor data-path defaults with portable `<state_root>` resolution.
- Deleted duplicate legacy package metadata files.

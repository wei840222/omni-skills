# Verified sources (Gate 6)

Retrieval window for this refactor: 2026-10-11. Re-open these pages before restating version-sensitive PowerPoint dictionary, export, or Agent Skills claims.

## Agent Skills package format

- **Agent Skills specification** — https://agentskills.io/specification
- **Best practices for skill creators** — https://agentskills.io/skill-creation/best-practices
- **Optimizing skill descriptions** — https://agentskills.io/skill-creation/optimizing-descriptions
- **Reference validator package** — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Microsoft PowerPoint object model

- **PowerPoint VBA reference overview** — https://learn.microsoft.com/en-us/office/vba/api/overview/powerpoint
- **Application object** — https://learn.microsoft.com/en-us/office/vba/api/powerpoint.application
- **Presentation object** — https://learn.microsoft.com/en-us/office/vba/api/powerpoint.presentation

AppleScript/`osascript` talks to the installed PowerPoint scripting dictionary; treat Microsoft Learn VBA pages as the canonical object-model map for presentation, slide, and export concepts, then verify terminology against the local dictionary on the target Mac.

## macOS scripting host

- **Script Editor User Guide (Apple Support)** — https://support.apple.com/guide/script-editor/welcome/mac
- **AppleScript Language Guide (Apple Developer archive)** — https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html

## Claim audit

| Claim in skill | Source support | Notes |
| --- | --- | --- |
| Live control via `osascript` + PowerPoint dictionary | AppleScript Language Guide; local app dictionary | Host must be macOS with PowerPoint installed |
| Active presentation / slide identity before mutate | Application + Presentation object model | Selection alone is insufficient |
| Export PDF through the app save/export path | Presentation object + local dictionary | Prefer absolute export paths; avoid silent overwrite |
| Slideshow/view state affects command success | PowerPoint overview + operational recovery notes | Re-read view/slideshow before presenter commands |
| Offline PPTX ≠ live session | Project boundary vs `powerpoint-pptx` | File libraries do not preserve live presenter state |
| No skill-owned cloud OAuth | Skill scope | PowerPoint autosave/add-ins may still network |

## Fragile claims — do not invent

- Exact AppleScript terminology for every PowerPoint build (verify on-device dictionary).
- Cross-platform live PowerPoint automation (this skill is `darwin`-only).
- That offline PPTX tooling preserves slideshow/presenter/export parity with the live app.
- Bypass of macOS Automation prompts, PowerPoint protection, or save dialogs.

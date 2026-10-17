# Sources — Word

Verified primary URLs for Gate 6 domain claims. Re-open the live page before restating version-sensitive behavior. Checked 2026-10-17.

## Agent Skills format

- Agent Skills specification — metadata string map, resource paths, progressive disclosure via https://agentskills.io/specification
- Agent Skills llms index via https://agentskills.io/llms.txt
- Best practices for skill creators via https://agentskills.io/skill-creation/best-practices.md
- Optimizing skill descriptions via https://agentskills.io/skill-creation/optimizing-descriptions.md

## Word object model (authoritative API surface)

Word's macOS AppleScript dictionary mirrors the Office object model documented in Microsoft's Word VBA reference. Use these pages to verify document, selection, comment, revision, and export claims:

- Word VBA API overview via https://learn.microsoft.com/en-us/office/vba/api/overview/word
- `Application` object via https://learn.microsoft.com/en-us/office/vba/api/word.application
- `Documents` collection via https://learn.microsoft.com/en-us/office/vba/api/word.documents
- `Document` object via https://learn.microsoft.com/en-us/office/vba/api/word.document
- `Document.ExportAsFixedFormat` (PDF/XPS export) via https://learn.microsoft.com/en-us/office/vba/api/word.document.exportasfixedformat
- `WdSaveFormat` enumeration via https://learn.microsoft.com/en-us/office/vba/api/word.wdsaveformat
- `Selection` object via https://learn.microsoft.com/en-us/office/vba/api/word.selection
- `Comment` object via https://learn.microsoft.com/en-us/office/vba/api/word.comment
- `Revisions` object via https://learn.microsoft.com/en-us/office/vba/api/word.revisions

## AppleScript / osascript transport

- AppleScript Language Guide — introduction via https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html
- How Mac Scripting Works — Apple Events, scriptable apps, dictionaries via https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/HowMacScriptingWorks.html
- SS64 `osascript` reference — `-e`, multi-line scripts, file execution via https://ss64.com/mac/osascript.html

## Local verification host

- Checked 2026-10-17 on Linux repair host `wei-workspace`: `osascript` absent; live Word attach/export claims are structural only on this host and must be validated on Darwin or marked unverified.

## Claim → source map

| Claim | Class | Source handling |
| --- | --- | --- |
| Live Word control goes through the app scripting dictionary / Apple Events | stable-domain | How Mac Scripting Works + Word overview |
| Active document / Documents collection is the attach surface | stable-domain | `word.application`, `word.documents`, `word.document` |
| Selection can target story ranges beyond body text | platform/ops | `word.selection` |
| Comments and revisions are first-class review objects | stable-domain | `word.comment`, `word.revisions` |
| PDF export should use Word's fixed-format export path | version/ops | `ExportAsFixedFormat` + `WdSaveFormat` |
| Dynamic text should avoid raw `-e` concatenation | ops | SS64 osascript + AppleScript Language Guide |
| Non-Darwin hosts cannot execute this skill live | platform-specific | Local host check 2026-10-17 |

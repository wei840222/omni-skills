# Sources — AppleScript

Verified primary URLs for Gate 6 domain claims. Re-open the live page before restating version-sensitive behavior. Checked 2026-10-03.

## Agent Skills format

- Agent Skills specification — metadata string map, resource paths, progressive disclosure via https://agentskills.io/specification
- Agent Skills llms index via https://agentskills.io/llms.txt

## AppleScript language and OSA

- AppleScript Overview / Getting Started via https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptX/Concepts/work_with_as.html
- AppleScript Language Guide — introduction via https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/introduction/ASLR_intro.html
- AppleScript Language Guide — class reference (includes `quoted form` of text) via https://developer.apple.com/library/archive/documentation/AppleScript/Conceptual/AppleScriptLangGuide/reference/ASLR_classes.html

## Mac automation model

- How Mac Scripting Works — Apple Events, scriptable apps, dictionaries, System Events via https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/HowMacScriptingWorks.html
- Automating the User Interface — System Events Processes suite, Accessibility enablement via https://developer.apple.com/library/archive/documentation/LanguagesUtilities/Conceptual/MacAutomationScriptingGuide/AutomatetheUserInterface.html

## osascript CLI

- SS64 `osascript` reference — `-e`, multi-line scripts, file execution via https://ss64.com/mac/osascript.html
- Local verification host (2026-10-03): Linux repair environment has no `osascript`; runtime claims for Darwin must be validated on a Mac or marked unverified.

## Claim → source map

| Claim | Class | Source handling |
| --- | --- | --- |
| Scripts talk to apps through Apple Events / OSA | stable-domain | How Mac Scripting Works |
| Inspect terminology via Script Editor dictionaries | stable-domain | How Mac Scripting Works |
| UI scripting uses System Events + Accessibility | platform-specific | Automate the User Interface |
| `quoted form` prepares text for shell use | stable-domain | Language Guide classes |
| `osascript -e` builds scripts; args after `--` reach the script | version/ops | SS64 osascript; prefer `on run argv` transport in this skill |
| Automation vs Accessibility are distinct TCC gates | platform-specific | UI scripting guide + macos skill TCC notes |

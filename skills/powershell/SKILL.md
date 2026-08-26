---
name: powershell
description: Write and review PowerShell scripts, handling output streams, array unrolling, comparison operators, and cross-platform version differences safely. Trigger when generating, reviewing, or fixing PowerShell code.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji": "\ud83d\udd35", "requires": {"bins": ["pwsh"]}}'
---

## Output Behavior
- Everything not captured goes to output — even without `return` or `Write-Output`
- `return` doesn't stop output — previous uncaptured expressions still output
- `Write-Host` bypasses pipeline — use for display only, not data
- Assign to `$null` to suppress — `$null = SomeFunction`
- `[void]` cast also suppresses — `[void](SomeFunction)`

## Array Gotchas
- Single item result is a scalar — `@(Get-Item .)` forces an array
- Empty result is `$null` — test carefully with `if ($null -eq $result)` or `@($result).Count`
- Array unrolling in pipeline — `@(1,2,3) | ForEach` sends items one by one
- `+=` on array creates new array — slow in loops, use `[System.Collections.ArrayList]`
- `,` is array operator — `,$item` wraps single item in array

## Comparison Operators
- Use `-eq`, `-ne`, `-gt`, `-lt` instead of C-style `==`, `!=`, `>`, `<`
- `-like` with wildcards, `-match` with regex — both return bool
- `-contains` for array membership — `$arr -contains $item`, not `$item -in $arr` (though `-in` works too)
- Case-insensitive by default — `-ceq`, `-cmatch` for case-sensitive
- `$null` on left side — `$null -eq $var` prevents array comparison issues

## String Handling
- Double quotes interpolate — `"Hello $name"` expands variable
- Single quotes literal — `'$name'` stays as literal text
- Subexpression for complex — `"Count: $($arr.Count)"` for properties/methods
- Here-strings for multiline — `@" ... "@` or `@' ... '@`
- Backtick escapes — `` `n `` for newline, `` `t `` for tab

## Pipeline
- `$_` or `$PSItem` is current object — same thing, `$_` more common
- `ForEach-Object` for pipeline — `foreach` statement doesn't take pipeline
- `-PipelineVariable` saves intermediate — `Get-Service -PV svc | Where ...`
- Pipeline processes one at a time — unless function doesn't support streaming

## Error Handling
- `$ErrorActionPreference` sets default — `Stop`, `Continue`, `SilentlyContinue`
- `-ErrorAction Stop` per command — makes non-terminating errors terminating
- `try/catch` only catches terminating — set `ErrorAction Stop` first
- `$?` is last command success — `$LASTEXITCODE` for native commands

## Common Mistakes
- No space before `{` in `if` — `if($x){` works but `if ($x) {` preferred
- `=` is assignment in conditions — use `-eq` for comparison
- Function return array unrolls — `return ,@($arr)` to keep array
- `Get-Content` returns lines array — `-Raw` for single string
- `Select-Object` creates new object — properties are copies, not references

## Platform Specifics and Versions
- **Windows PowerShell 5.1**: Built on .NET Framework. Included by default in Windows. Uses `powershell.exe`.
- **PowerShell 7+ (Core)**: Built on .NET (Core). Cross-platform (Windows, macOS, Linux). Uses `pwsh` executable.
- PowerShell 7 defaults to UTF-8 without BOM. Windows PowerShell 5.1 often defaults to UTF-16LE or adds BOMs.
- `$_` and `$PSItem` are interchangeable pipeline variables, though `$_` is more idiomatic.
- Load `references/powershell-versions.md` when choosing `powershell` vs `pwsh`, encoding defaults, or migration caveats.

## Cross-Platform
- Paths use `/` or `\` — `Join-Path` for portable
- Environment vars: `$env:VAR` — works on all platforms
- Aliases differ across platforms — `ls`, `cat` may not exist, use full cmdlet names

# PowerShell Versions and Migration Notes

Use this reference when the agent must choose between Windows PowerShell 5.1 and PowerShell 7+, explain encoding defaults, or advise on migration.

## Executables

| Edition | Executable | Runtime | Platforms |
|---|---|---|---|
| Windows PowerShell 5.1 | `powershell.exe` | .NET Framework | Windows only |
| PowerShell 7+ | `pwsh` | .NET (Core) | Windows, macOS, Linux |

Prefer `pwsh` for new cross-platform automation. Keep `powershell.exe` only when a host or module still requires Windows PowerShell 5.1.

## Encoding and BOM

- PowerShell 7 defaults to UTF-8 without BOM for many text operations.
- Windows PowerShell 5.1 often emits UTF-16LE or writes files with a BOM.
- When scripts move between editions, verify file encoding and avoid assuming BOM behavior.

## Pipeline Variables

`$_` and `$PSItem` refer to the same pipeline object. Prefer `$_` in examples unless an existing codebase already standardizes on `$PSItem`.

## Sources

- [Differences between Windows PowerShell 5.1 and PowerShell 7.x](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/differences-from-windows-powershell) — executable names, compatibility, and migration caveats
- [about_Pipelines](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_pipelines) — pipeline object flow and `$_` semantics
- [PowerShell](https://en.wikipedia.org/wiki/PowerShell) — high-level edition timeline (`powershell.exe` vs `pwsh`)

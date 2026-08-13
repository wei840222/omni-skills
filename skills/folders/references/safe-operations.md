# Safe Folder Operations

## Resolve and inspect paths

Resolve `~`, `..`, and symlinks to canonical paths before evaluating an operation. Treat `/`, `/etc`, `/var`, `/usr`, `/System`, `/Library`, `C:\\Windows`, and `C:\\Program Files` as protected roots: report the conflict and ask for a narrower, non-system target. During discovery, list symlinks separately instead of traversing them.

Before a move or cleanup, list the exact canonical targets, estimate their size when practical, identify active repositories or mounted/network paths, and state whether the operation can be recovered. Do not infer that similar-looking folders are safe to combine or remove.

## Recoverable cleanup

Send removals to the operating system trash or recycle bin. Explain that build artifacts such as `node_modules`, `__pycache__`, `.gradle`, `build/`, `target/`, `Pods/`, and `.next/` are usually regenerable, and name the relevant restore command when known (for example, `npm install` for `node_modules`). Treat user data and unrecognized directories as non-regenerable unless the user confirms otherwise.

## Platform considerations

- On macOS, a directory containing only `.DS_Store` can be treated as effectively empty; treat a `.app` bundle as one item.
- On Windows, use the `\\?\\` path prefix when an operation requires paths longer than 260 characters.
- For network drives, warn about latency or offline failure before a bulk operation and wait for confirmation.

After an operation, report completed targets, skipped targets and reasons, and the location or method for recovery.

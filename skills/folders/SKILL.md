---
name: folders
description: Find, index, organize, or clean up project folders and build artifacts safely. Use when the user asks where a directory is, wants a folder inventory, or requests a folder operation.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📂"}'
---

## Folder Index

The folder index is persistent state. Resolve its root in this order:

1. Use an explicit state root supplied by the user.
2. Otherwise consider `<workspace>/folders/`, `<workspace>/memory/folders/`, and `~/folders/` in that order; use the first existing directory.
3. For a lookup-only request with no existing root, keep state absent. When the user confirms that an index should be saved, create `<workspace>/folders/` and use it as the default.

Store the index at `<state_root>/folder-index.json`. If multiple candidate roots exist, tell the user which root was selected and keep other copies unchanged. Perform migration, merging, or legacy-file removal only when the user explicitly requests it.

Use this JSON shape:

```json
{
  "folders": [
    {
      "path": "/Users/alex/projects/webapp",
      "type": "project",
      "note": "Main client project"
    }
  ]
}
```

For a "where is" or "find my project" request, read the index first and validate that a matching path still exists. Propose exact additions, edits, or removals and apply them only after confirmation.

## Discovery

For an index miss or an explicit inventory request, search only user-relevant roots such as `~/projects`, `~/Documents`, `~/code`, `~/dev`, and `~/work`, plus any roots the user names. Detect projects from `.git`, `package.json`, `pubspec.yaml`, `Cargo.toml`, `go.mod`, `pyproject.toml`, or `*.sln`.

When a project marker is found, record that directory as the project boundary. Treat dependency and generated-content trees such as `node_modules`, `vendor`, and `build` as traversal boundaries. Report the checked roots and findings, then offer the resulting records for indexing.

## Safe Folder Operations

Resolve `~`, `..`, and symlinks to canonical paths before evaluating an operation. Treat `/`, `/etc`, `/var`, `/usr`, `/System`, `/Library`, `C:\\Windows`, and `C:\\Program Files` as protected roots: report the conflict and ask for a narrower, non-system target. During discovery, list symlinks separately instead of traversing them.

Before a move or cleanup, list the exact canonical targets, estimate their size when practical, identify active repositories or mounted/network paths, and state whether the operation can be recovered. Require a separately named target and confirmation for every folder selected for combining or removal.

Send removals to the operating system trash or recycle bin. Explain that build artifacts such as `node_modules`, `__pycache__`, `.gradle`, `build/`, `target/`, `Pods/`, and `.next/` are usually regenerable, and name the relevant restore command when known. Treat user data and unrecognized directories as non-regenerable unless the user confirms otherwise.

## Platform considerations

- On macOS, a directory containing only `.DS_Store` can be treated as effectively empty; treat a `.app` bundle as one item.
- On Windows, use the `\\?\\` path prefix only for a compatible operation that needs an absolute extended-length path. Microsoft documents the `MAX_PATH` limit and app/API compatibility requirements in [Maximum Path Length Limitation](https://learn.microsoft.com/en-us/windows/win32/fileio/maximum-file-path-limitation).
- For network drives, warn about latency or offline failure before a bulk operation and wait for confirmation.
- `node_modules` is regenerable only when project metadata is available and the user accepts the normal network and dependency effects of `npm install`, as documented in [npm install](https://docs.npmjs.com/cli/v11/commands/npm-install).

## Outcome checks

- A lookup reports either matching canonical paths or that no match was found in the checked locations.
- An index update reports the selected state root and the exact added, changed, or removed record.
- A folder operation reports every affected path, whether it was completed, and its recovery method.
- If path resolution, permission checks, or the requested confirmation fails, leave the filesystem and index unchanged and explain the blocking condition.

# Folder Index and Discovery

## Resolve persistent state

The folder index is persistent state. Resolve its root in this order:

1. Use an explicit state root supplied by the user.
2. Otherwise consider `<workspace>/folders/`, `<workspace>/memory/folders/`, and `~/folders/` in that order; use the first existing directory.
3. If none exists, do not create state for a lookup-only request. When the user confirms that an index should be saved, create `<workspace>/folders/` and use it as the default.

Store the index only at `<state_root>/folder-index.json`. If multiple candidate roots exist, tell the user which root was selected and that other copies were not merged. Never migrate, merge, or delete legacy index files automatically.

## Index format

Use a JSON object with a `folders` array. Each entry has a canonical absolute `path`, a `type`, and an optional `note`:

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

Read the index before a "where is" or "find my project" request. Validate an indexed path still exists before presenting it as current. Propose exact additions, edits, or removals and apply them only after confirmation.

## Targeted discovery

For an index miss or an explicit inventory request, search only user-relevant roots such as `~/projects`, `~/Documents`, `~/code`, `~/dev`, and `~/work`, plus any roots the user names. Detect projects from `.git`, `package.json`, `pubspec.yaml`, `Cargo.toml`, `go.mod`, `pyproject.toml`, or `*.sln`.

When a project marker is found, record that directory as the project boundary. Do not traverse dependency or generated-content trees such as `node_modules`, `vendor`, or `build`. Report the checked roots and findings, then offer the resulting records for indexing.

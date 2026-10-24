---
name: s3
description: "Configure and operate S3-compatible cloud object storage. Use when managing bucket policies, configuring lifecycle rules, setting up CORS, generating presigned upload/download URLs, or executing multipart transfers."
metadata:
  openclaw: '{"emoji":"🪣","os":["linux","darwin","win32"],"displayName":"S3"}'
---
## State location

S3 state may exist in `<workspace>/s3/`, `<workspace>/memory/s3/`, or `~/s3/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/s3/`, `<workspace>/memory/s3/`, `~/s3/`.
3. If none exists and state must be created, default to `<workspace>/s3/`.

Use the selected `<state_root>` for every state operation in this skill.

S3 is a remote object storage service and does not maintain local persistent state in the workspace (`<state_root>`).

## Quick Reference
Load `references/s3-concepts.md` when diagnosing presigned URL issues, configuring lifecycle rules, setting up CORS, or handling multipart uploads.
Load `references/sources.md` to review official Amazon S3 documentation, presigned URL guidelines, and pricing rules.

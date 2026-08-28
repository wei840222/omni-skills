---
name: s3
description: Trigger to configure or interact with S3-compatible object storage, manage lifecycle policies, CORS, presigned URLs, and multipart uploads.
metadata:
  openclaw: '{"emoji":"🪣","os":["linux","darwin","win32"],"displayName":"S3"}'
---
## State location
S3 is a remote object storage service and does not maintain local persistent state in the workspace (`<state_root>`).

## Quick Reference
Load `references/s3-concepts.md` when diagnosing presigned URL issues, configuring lifecycle rules, setting up CORS, or handling multipart uploads.

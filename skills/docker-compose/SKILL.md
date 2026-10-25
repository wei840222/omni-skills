---
name: docker-compose
description: Configure and manage multi-container applications using Docker Compose. Use when defining service dependencies, configuring local development environments with watch mode, setting up container networking, or debugging volume and resource limits.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🐳","requires":{"anyBins":["docker-compose","docker"]}}'
---
## Working space

- Load `references/best-practices.md` for proper depends_on, healthchecks, volume safety, and configuration patterns.

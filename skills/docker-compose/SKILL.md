---
name: docker-compose
description: Configure and manage multi-container applications using Docker Compose. Use when defining service dependencies, configuring local development environments with watch mode, setting up container networking, or debugging volume and resource limits.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🐳","requires":{"anyBins":["docker-compose","docker"]}}'
  related-skills: '{"docker":"Use for building individual images and managing containers directly.","deploy":"Use for deploying docker-compose applications to production servers.","backend":"Use for designing the architecture of backend services deployed via docker-compose."}'
---
## Working space

- Load `references/best-practices.md` for proper depends_on, healthchecks, volume safety, and configuration patterns.

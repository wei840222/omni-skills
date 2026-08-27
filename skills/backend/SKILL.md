---
name: backend
description: Design, build, and debug reliable backend services. Use when optimizing APIs, handling external dependencies, managing database connections, or configuring observability.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⚙️"}'
  related-skills: '{"nginx":"Works with Nginx for reverse proxying and load balancing backend services.","storage":"Works with storage layers often connected to backend services."}'
---

# Backend Best Practices

This skill outlines guidelines for building resilient and secure backend services. Load the following references as needed based on the task context:

## Core References

| Topic | Reference | When to Load |
|-------|-----------|--------------|
| **API Design** | `references/api-design.md` | When designing RESTful API endpoints or payloads. |
| **Input Validation** | `references/input-validation.md` | When validating incoming user requests or data. |
| **Error Handling** | `references/error-handling.md` | When returning errors to clients or structured logging. |
| **Database** | `references/database.md` | When dealing with database connections, transactions, or queries. |
| **Security** | `references/security.md` | When configuring secrets, authentication, or dependencies. |
| **Domain Knowledge** | `references/domain-knowledge.md` | When citing verifiable standards and architecture sources. |

## Resilience and Scalability

| Topic | Reference | When to Load |
|-------|-----------|--------------|
| **Resilience** | `references/resilience.md` | When calling external APIs, handling retries, or managing timeouts. |
| **Caching** | `references/caching.md` | When implementing caching layers and invalidation strategies. |
| **Rate Limiting** | `references/rate-limiting.md` | When protecting expensive operations from abuse. |

## Operational Excellence

| Topic | Reference | When to Load |
|-------|-----------|--------------|
| **Observability** | `references/observability.md` | When setting up logging, metrics, tracing, or alerting. |
| **Lifecycle** | `references/lifecycle.md` | When configuring health checks or graceful shutdown. |

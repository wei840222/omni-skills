# Implementation

- Use established libraries—rely on established libraries for JWT parsing
- Libraries: `jsonwebtoken` (Node), `PyJWT` (Python), `java-jwt` (Java), `golang-jwt` (Go)
- Middleware should reject invalid tokens early—before any business logic

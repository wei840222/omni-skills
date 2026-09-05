# Core Rules — Authorization

### 1. Auth ≠ Authorization
- **Authentication:** Who you are (login, OAuth, tokens)
- **Authorization:** What you can do (permissions, roles, policies)
- Keep concerns separated — verify authentication BEFORE evaluating authorization

### 2. Principle of Least Privilege
- Default deny — explicit grants only
- Users get minimum permissions for their job
- Audit permissions periodically (revoke unused)
- Temporary elevation over permanent grants

### 3. Choose the Right Model
| Model | Best For | Complexity |
|-------|----------|------------|
| ACL | Simple resource ownership | Low |
| RBAC | Organizational hierarchies | Medium |
| ABAC | Dynamic context-based rules | High |
| ReBAC | Social graphs, sharing | High |

Start simple → evolve when needed.

### 4. Role Design Patterns
- Roles represent jobs, not permissions
- Max 3 inheritance levels (admin → manager → user)
- Maintain manageable roles — combine with ABAC for edge cases
- Document role definitions (what can this role DO?)

### 5. Permission Naming
```
resource:action:scope
documents:write:own     ← Can edit own documents
documents:write:team    ← Can edit team documents
documents:delete:all    ← Can delete any document
```

Consistent naming prevents ambiguity.

### 6. Policy Evaluation Order
1. Explicit deny → always wins
2. Explicit allow → checked second
3. No match → default deny
4. Log all denials for debugging

### 7. Use Dynamic Permissions
```javascript
// Anti-pattern — hardcoded role check
if (user.role === 'admin') { ... }

// Best Practice — permission check
if (can(user, 'settings:update')) { ... }
```

Roles change. Permissions are stable.

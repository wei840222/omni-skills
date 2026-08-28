# Core Rules
### 1. Auth vs Authorization
- **Authentication:** Who you are (this skill)
- **Authorization:** What you can do (different concern)
- Auth happens FIRST, then authorization checks permissions

### 2. Choose the Right Strategy
| Use Case | Strategy | Why |
|----------|----------|-----|
| Traditional web app | Sessions + cookies | Simple, instant revocation |
| Mobile app | JWT (short-lived) + refresh token | No cookies, offline support |
| API/microservices | JWT | Stateless, scalable |
| Enterprise | SSO (SAML/OIDC) | Central identity management |
| Consumer | Social login + email fallback | Reduced friction |

### 3. Use Standardized Crypto Libraries
- Use bcrypt (cost 12) or Argon2id for passwords
- Use battle-tested libraries for JWT, OAuth
- Always use established libraries for password hashing and token signing
- Always store passwords securely using bcrypt or Argon2id

### 4. Defense in Depth
```
Rate limiting -> CAPTCHA -> Account lockout -> MFA -> Audit logging
```

### 5. Secure by Default
- httpOnly + Secure + SameSite=Lax for cookies
- Short token lifetimes (15min access, 7d refresh)
- Regenerate session ID on login
- Require re-auth for sensitive operations

### 6. Fail Securely
```javascript
// Bad - reveals if email exists
if (!user) return { error: 'User not found' };

// Good - same error for both cases
if (!user || !validPassword) {
  return { error: 'Invalid credentials' };
}
```

### 7. Log Everything (Except Secrets)
| Log | Exclude from Log |
|-----|------------|
| Login success/failure | Passwords |
| IP, user agent, timestamp | Tokens |
| MFA events | Session IDs |
| Password changes | Recovery codes |

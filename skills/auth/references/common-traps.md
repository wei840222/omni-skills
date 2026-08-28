# Common Traps
- Storing passwords with MD5/SHA1 - use bcrypt or Argon2id
- JWT with long expiry (30d) - use short access + refresh token
- Revealing if email exists - use generic error message
- Hard account lockout - enables denial of service
- SMS for MFA - vulnerable to SIM swapping
- No rate limiting on login - enables brute force

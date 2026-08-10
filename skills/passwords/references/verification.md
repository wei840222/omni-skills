# Verification reference

Load this reference when the user asks for a leak check, asks why the skill does not create an encrypted vault, or requests password-policy rationale.

## Pwned Passwords range queries

The free Pwned Passwords API supports a k-anonymity range query: a local checker computes the password's SHA-1 hash, sends only the first five hexadecimal characters to `https://api.pwnedpasswords.com/range/{prefix}`, and compares returned suffixes locally. The calling application identifies itself with a meaningful `User-Agent`; the Pwned Passwords API itself requires no API key.

The checker must run locally under the user's control. This skill neither accepts a password nor makes the request on the user's behalf.

Sources:

- Have I Been Pwned, “Pwned Passwords” — https://haveibeenpwned.com/API/v3#PwnedPasswords
- Have I Been Pwned, “Searching Pwned Passwords by range” — https://haveibeenpwned.com/API/v3#SearchingPwnedPasswordsByRange

## Recoverable credential storage

OWASP distinguishes password-verifier storage from the exceptional cases that need reversible encryption. A password manager that must reveal a credential has a broader security and recovery design than encrypting one file. Use an established user-controlled manager rather than presenting an agent-created encrypted file as an equivalent implementation.

Source:

- OWASP, “Password Storage Cheat Sheet” — https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html

## `age` scope

`age` is a file-encryption format that wraps a randomly generated file key for one or more recipients. It does not define a password-manager policy, recovery workflow, access-control model, or safe agent secret-delivery channel.

Source:

- C2SP, “age” specification — https://c2sp.org/age
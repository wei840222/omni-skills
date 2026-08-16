# Regex engine notes

Read this reference when a pattern must work across engines, uses lookaround or Unicode features, or processes untrusted input at scale.

## JavaScript (ECMAScript)

- Literal syntax is `/pattern/flags`; `RegExp` construction requires host-string escaping.
- Lookbehind and the `s` (dotall) flag require ES2018-era support. Confirm the runtime target when compatibility matters.
- JavaScript does not support possessive quantifiers or atomic groups in standard regular expressions.
- Reference: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions

## Python `re`

- Use raw string literals, such as `r"\d+"`, unless a literal trailing backslash or other host-string rule requires a different form.
- Named groups use `(?P<name>...)`; lookbehind must be fixed width.
- Python's standard `re` module does not implement `\p{...}` Unicode properties. The third-party `regex` module has different capabilities and should be identified explicitly.
- Reference: https://docs.python.org/3/library/re.html

## PCRE-family engines

- PCRE implementations commonly support named groups, lookarounds, possessive quantifiers, and atomic groups, but versions and embedding applications can differ.
- Verify the application's PCRE version before relying on newer variable-length-lookbehind behavior.
- Reference: https://www.pcre.org/current/doc/html/pcre2pattern.html

## Go `regexp` / RE2

- Go's standard `regexp` package uses RE2 syntax and provides linear-time matching.
- RE2 omits backreferences and lookaround assertions; redesign the matching logic instead of translating those constructs literally.
- Reference: https://pkg.go.dev/regexp/syntax

## Testing and diagnosis

- Test in the deployed engine and host-language string context, not only a web tester configured for another flavor.
- Regex101 can help visualize supported PCRE, ECMAScript, Python, and Golang flavors; treat it as a diagnostic aid, then verify in the actual runtime.
- Reference: https://regex101.com/

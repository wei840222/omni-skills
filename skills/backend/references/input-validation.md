## Input Validation

- Validate everything from outside—query params, headers, body, path params
- Whitelist valid input, don't blacklist bad—reject unknown fields
- Validate early, before any processing—save resources, clearer errors
- Size limits on all inputs—prevent memory exhaustion attacks

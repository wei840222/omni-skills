## Error Handling

- Do not expose stack traces to clients—log internally, return generic message
- Structured error responses: code, message, request ID—enables debugging without leaking
- Fail fast on bad input—validate at entry point, not deep in business logic
- Unexpected errors: 500 + alert—expected errors: appropriate 4xx

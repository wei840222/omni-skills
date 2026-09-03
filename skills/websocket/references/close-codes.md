## Close Codes

- 1000: normal closure; 1001: going away (page close)
- 1006: abnormal (no close frame received)—usually network issue
- 1008: policy violation; 1011: server error
- 4000-4999: application-defined—use for auth failure, rate limit, etc.
- Always send close code and reason—helps debugging

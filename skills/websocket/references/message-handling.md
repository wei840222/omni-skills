## Message Handling

- Use text frames for JSON and binary frames for blobs/protobuf; introduce an explicit framing scheme when both are required on one socket.
- TCP is a byte stream; WebSocket provides message framing and reassembly for you.
- Message order is preserved per connection; receivers can process in send order.
- Large messages may fragment; set a server-side max message size and stream oversized payloads in chunks.

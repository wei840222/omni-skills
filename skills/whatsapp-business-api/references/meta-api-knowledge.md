# WhatsApp Business Cloud API Knowledge

## Source
- [WhatsApp Business Platform Cloud API Documentation](https://developers.facebook.com/docs/whatsapp/cloud-api)
- [WhatsApp Cloud API Messages Endpoint](https://developers.facebook.com/docs/whatsapp/cloud-api/reference/messages)

## Core Knowledge
- **Base URL**: `https://graph.facebook.com/v21.0/` (or current version).
- **Authentication**: Bearer Token (`WHATSAPP_ACCESS_TOKEN`) using a System User token or a User token.
- **Message Types**: Text, image, document, audio, video, sticker, interactive (buttons, list messages), contacts, location, and templates.
- **Messaging Window**: Businesses have 24 hours to respond to a user-initiated message with a free-form message. Outside this window, only approved Message Templates can be sent.
- **Templates**: Must be pre-approved by Meta before sending. Templates use a `namespace` and `name` to be triggered.
- **Rate Limits**: Differ by tier, starting at Tier 1 (1K business-initiated conversations/day), escalating based on quality and volume. 80 messages/second typically per phone number limit.
- **Media**: Maximum size for images is 5MB, video is 16MB, documents 100MB. Supported types include `jpeg`, `png`, `pdf`, `mp4`.
- **Webhooks**: Subscriptions required to receive incoming messages (`messages` field) and status updates (`statuses`). Must verify webhook URL using a custom `VERIFY_TOKEN` (mapped to `WHATSAPP_APP_SECRET`).

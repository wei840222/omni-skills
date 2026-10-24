# Official Sources & Technical Specifications

This document records the official Meta developer documentation and architecture specifications for the WhatsApp Business Cloud API.

## Official Meta Cloud API Documentation

- **WhatsApp Business Cloud API Overview**: [https://developers.facebook.com/documentation/business-messaging/whatsapp/overview](https://developers.facebook.com/documentation/business-messaging/whatsapp/overview)
  - Cloud API architecture, Meta Graph API onboarding, access token generation, and phone number registration.
- **WhatsApp Message API Reference**: [https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-phone-number/message-api](https://developers.facebook.com/documentation/business-messaging/whatsapp/reference/whatsapp-business-phone-number/message-api)
  - Graph API endpoint specification (`POST /{Version}/{Phone-Number-ID}/messages` supporting v23.0, v24.0, v25.0), payload structures for text, media, interactive components (buttons/lists), and WhatsApp Flows.
- **Webhooks & Event Notifications**: [https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks](https://developers.facebook.com/documentation/business-messaging/whatsapp/webhooks)
  - Webhook subscription setup, hub challenge verification, incoming message payloads, and message status updates (`sent`, `delivered`, `read`).
- **WhatsApp Messaging Pricing & Delivery Models**: [https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing](https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing)
  - Per-delivered-message billing model (transitioned July 1, 2025; conversation-based pricing deprecated), message categories (marketing, utility, authentication, service), and customer service window rules.

# Schema

## Overview

Pamoja's data model follows the channel architecture: a **User** owns one **Channel** (the public surface), and each opt-in module owns its own entities — the business module owns `BusinessProfile`, `Product`, `Order`, and `OrderItem`; the social module owns `Post` and `PostComment`. Modules share no entities and reference the channel only. The graph (`Connection`, `Block`) is first-class, and money is modeled in minor units with idempotency keys because payments are the product's risk surface (see [[architecture]] and [[risk_log]] R-005).

Search is **derived, not stored**: the index is built from channel Layer 0 signals (name, bio) plus module signals (business tags/catalog, post content), per the findability model in [[README]]. No entity stores search state.

## Entity Definitions

### User

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/user.schema.json",
  "title": "User",
  "description": "The account anchor. Identified by phone number; public identity lives on the User's Channel.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID, opaque to clients." },
    "phoneNumber": { "type": "string", "description": "E.164 phone number; unique; primary login credential." },
    "locale": { "type": "string", "description": "BCP-47 locale, e.g. en-NG. Drives FEAT-031 formatting." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Account creation time." },
    "updatedAt": { "type": "string", "format": "date-time", "description": "Last account update time." }
  },
  "required": ["id", "phoneNumber", "locale", "createdAt", "updatedAt"]
}
```

### Channel

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/channel.schema.json",
  "title": "Channel",
  "description": "The user's public surface — Layer 0 findability. Module-specific data lives in module entities, never here.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "userId": { "type": "string", "description": "References the owning User. One channel per user." },
    "name": { "type": "string", "description": "Display name / handle. Required; searchable (Layer 0)." },
    "bio": { "type": "string", "description": "Free-text description in the owner's words. Searchable (Layer 0)." },
    "avatarUrl": { "type": "string", "format": "uri", "description": "Avatar image URL (optional)." },
    "status": { "type": "string", "description": "Lightweight status, e.g. 'Open for business' (FEAT-027)." },
    "statusExpiresAt": { "type": "string", "format": "date-time", "description": "Auto-clear time for status (optional)." },
    "modules": {
      "type": "array",
      "items": { "enum": ["business", "social"] },
      "description": "Opt-in modules carried by this channel (FEAT-004)."
    },
    "createdAt": { "type": "string", "format": "date-time", "description": "Channel creation time." },
    "updatedAt": { "type": "string", "format": "date-time", "description": "Last channel update time." }
  },
  "required": ["id", "userId", "name", "modules", "createdAt", "updatedAt"]
}
```

### Connection

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/connection.schema.json",
  "title": "Connection",
  "description": "A mutual relationship edge in the contact graph. The moat: relationships are mutual, never follower-based.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "requesterId": { "type": "string", "description": "References the User who initiated the connection." },
    "acceptorId": { "type": "string", "description": "References the User who accepted (or was invited)." },
    "status": { "enum": ["pending", "accepted", "declined", "cancelled"], "description": "Lifecycle of the mutual relationship." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Request time." },
    "acceptedAt": { "type": "string", "format": "date-time", "description": "Acceptance time (null until accepted)." }
  },
  "required": ["id", "requesterId", "acceptorId", "status", "createdAt"]
}
```

### Block

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/block.schema.json",
  "title": "Block",
  "description": "A blocking relationship. Blocked users cannot message, call, or appear in search or the graph (FEAT-029).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "blockerId": { "type": "string", "description": "References the User who blocked." },
    "blockedId": { "type": "string", "description": "References the User who is blocked." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Block time." }
  },
  "required": ["id", "blockerId", "blockedId", "createdAt"]
}
```

### Invite

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/invite.schema.json",
  "title": "Invite",
  "description": "An out-of-band invite sent by SMS/WhatsApp link (FEAT-003).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "inviterId": { "type": "string", "description": "References the User who sent the invite." },
    "inviteCode": { "type": "string", "description": "Short code embedded in the share link." },
    "usedBy": { "type": "string", "description": "References the User who claimed the invite (null until used)." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Invite creation time." },
    "expiresAt": { "type": "string", "format": "date-time", "description": "Expiry; admin can expire early." }
  },
  "required": ["id", "inviterId", "inviteCode", "createdAt", "expiresAt"]
}
```

### Conversation

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/conversation.schema.json",
  "title": "Conversation",
  "description": "A chat thread — direct or group (FEAT-006, FEAT-007). Orders and payments live inside conversations.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "type": { "enum": ["direct", "group"], "description": "Direct (1:1) or group thread." },
    "title": { "type": "string", "description": "Group name; null for direct conversations." },
    "avatarUrl": { "type": "string", "format": "uri", "description": "Optional group avatar; null for direct." },
    "lastMessageAt": { "type": "string", "format": "date-time", "description": "Sort key for the chat list." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Thread creation time." }
  },
  "required": ["id", "type", "createdAt"]
}
```

### ConversationParticipant

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/conversation-participant.schema.json",
  "title": "ConversationParticipant",
  "description": "Membership of a User in a Conversation, with per-member read position.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "conversationId": { "type": "string", "description": "References the Conversation." },
    "userId": { "type": "string", "description": "References the participating User." },
    "lastReadMessageId": { "type": "string", "description": "Read position; drives unread counts." },
    "joinedAt": { "type": "string", "format": "date-time", "description": "Join time." },
    "isAdmin": { "type": "boolean", "description": "Group admin rights (FEAT-007); false for direct." }
  },
  "required": ["id", "conversationId", "userId", "joinedAt", "isAdmin"]
}
```

### Message

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/message.schema.json",
  "title": "Message",
  "description": "A single message in a conversation. Order and payment cards are embedded by reference, never by nesting.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "conversationId": { "type": "string", "description": "References the Conversation." },
    "senderId": { "type": "string", "description": "References the sending User." },
    "type": {
      "enum": ["text", "image", "voice_note", "file", "sticker", "system", "order", "payment", "receipt"],
      "description": "Message payload type."
    },
    "content": { "type": "string", "description": "Text body or caption (required for text; optional otherwise)." },
    "mediaUrl": { "type": "string", "format": "uri", "description": "Media URL for image/voice_note/file." },
    "mediaDurationMs": { "type": "integer", "description": "Duration for voice notes (FEAT-006 hold-to-talk)." },
    "orderId": { "type": "string", "description": "References the Order when type = order; else null." },
    "transactionId": { "type": "string", "description": "References the Transaction when type = payment or receipt; else null." },
    "deliveryStatus": { "enum": ["queued", "sent", "delivered", "read"], "description": "Delivery lifecycle." },
    "deletedAt": { "type": "string", "format": "date-time", "description": "Soft-delete time; shows 'message deleted'." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Message creation time." }
  },
  "required": ["id", "conversationId", "senderId", "type", "deliveryStatus", "createdAt"]
}
```

### BusinessProfile

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/business-profile.schema.json",
  "title": "BusinessProfile",
  "description": "The business module's identity on a channel: tags, location, verification state. One per business channel.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "channelId": { "type": "string", "description": "References the owning Channel (business module active)." },
    "tags": {
      "type": "array",
      "items": { "type": "string" },
      "description": "Optional business tags, searchable (FEAT-019)."
    },
    "location": {
      "type": "object",
      "description": "Business location for search filtering.",
      "properties": {
        "city": { "type": "string", "description": "City name, e.g. Lagos." },
        "country": { "type": "string", "description": "ISO 3166-1 alpha-2 country code." }
      },
      "required": ["city", "country"]
    },
    "verificationStatus": { "enum": ["none", "submitted", "under_review", "approved", "rejected"], "description": "Current merchant verification state (FEAT-005)." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Profile creation time." },
    "updatedAt": { "type": "string", "format": "date-time", "description": "Last profile update time." }
  },
  "required": ["id", "channelId", "verificationStatus", "createdAt", "updatedAt"]
}
```

### Product

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/product.schema.json",
  "title": "Product",
  "description": "A catalog item on a business channel. Searchable via business module signals (FEAT-016, FEAT-019).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "channelId": { "type": "string", "description": "References the merchant's Channel." },
    "name": { "type": "string", "description": "Product name; required; searchable." },
    "description": { "type": "string", "description": "Optional product description; searchable." },
    "category": { "type": "string", "description": "Category (e.g. fashion, food, electronics); searchable and filterable." },
    "priceMinor": { "type": "integer", "description": "Price in minor units (kobo), never a float." },
    "currency": { "type": "string", "description": "ISO 4217 currency code." },
    "photos": { "type": "array", "items": { "type": "string", "format": "uri" }, "description": "Product photo URLs." },
    "stockQuantity": { "type": "integer", "description": "Current stock (FEAT-020)." },
    "lowStockThreshold": { "type": "integer", "description": "Alert threshold for low stock (FEAT-020)." },
    "isActive": { "type": "boolean", "description": "Soft-delete / hidden flag." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Product creation time." },
    "updatedAt": { "type": "string", "format": "date-time", "description": "Last product update time." }
  },
  "required": ["id", "channelId", "name", "priceMinor", "currency", "stockQuantity", "lowStockThreshold", "isActive", "createdAt", "updatedAt"]
}
```

### Order

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/order.schema.json",
  "title": "Order",
  "description": "An order on a merchant's channel. The buyer is a graph contact — there is no customer entity (no CRM wall).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID; shown to both parties." },
    "merchantChannelId": { "type": "string", "description": "References the merchant's Channel." },
    "buyerId": { "type": "string", "description": "References the buying User — a graph contact, never a segmented customer row." },
    "conversationId": { "type": "string", "description": "References the chat thread where the order lives." },
    "status": { "enum": ["new", "confirmed", "declined", "paid", "fulfilled", "delivered", "complete"], "description": "Order lifecycle (FEAT-017)." },
    "deliveryStage": { "enum": ["none", "packed", "handed_to_rider", "in_transit", "delivered"], "description": "Delivery tracking stage (FEAT-021)." },
    "totalMinor": { "type": "integer", "description": "Order total in minor units." },
    "currency": { "type": "string", "description": "ISO 4217 currency code." },
    "declineReason": { "type": "string", "description": "Shown to the buyer when declined." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Order creation time." },
    "confirmedAt": { "type": "string", "format": "date-time", "description": "Merchant confirmation time (null until confirmed)." },
    "paidAt": { "type": "string", "format": "date-time", "description": "Payment time (null until paid)." },
    "completedAt": { "type": "string", "format": "date-time", "description": "Completion time (null until complete)." }
  },
  "required": ["id", "merchantChannelId", "buyerId", "conversationId", "status", "deliveryStage", "totalMinor", "currency", "createdAt"]
}
```

### OrderItem

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/order-item.schema.json",
  "title": "OrderItem",
  "description": "A line item on an order, with a price snapshot for history integrity.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "orderId": { "type": "string", "description": "References the Order." },
    "productId": { "type": "string", "description": "References the Product at order time (may change later)." },
    "productSnapshot": {
      "type": "object",
      "description": "Immutable copy of what was sold, so history survives catalog edits.",
      "properties": {
        "name": { "type": "string", "description": "Product name at order time." },
        "priceMinor": { "type": "integer", "description": "Unit price at order time in minor units." }
      },
      "required": ["name", "priceMinor"]
    },
    "quantity": { "type": "integer", "description": "Units ordered; positive integer." },
    "lineTotalMinor": { "type": "integer", "description": "quantity × snapshot price in minor units." }
  },
  "required": ["id", "orderId", "productId", "productSnapshot", "quantity", "lineTotalMinor"]
}
```

### PaymentRequest

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/payment-request.schema.json",
  "title": "PaymentRequest",
  "description": "A money request or bill split across connections (FEAT-013).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "requesterId": { "type": "string", "description": "References the User who sent the request." },
    "conversationId": { "type": "string", "description": "References the thread where the request appears." },
    "amountMinor": { "type": "integer", "description": "Total amount in minor units." },
    "currency": { "type": "string", "description": "ISO 4217 currency code." },
    "note": { "type": "string", "description": "Optional context note." },
    "status": { "enum": ["pending", "partially_paid", "paid", "declined", "expired"], "description": "Request lifecycle." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Request creation time." },
    "expiresAt": { "type": "string", "format": "date-time", "description": "Expiry time (optional)." }
  },
  "required": ["id", "requesterId", "conversationId", "amountMinor", "currency", "status", "createdAt"]
}
```

### PaymentRequestPart

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/payment-request-part.schema.json",
  "title": "PaymentRequestPart",
  "description": "One member's share of a split bill (FEAT-013).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "paymentRequestId": { "type": "string", "description": "References the PaymentRequest." },
    "payerId": { "type": "string", "description": "References the User responsible for this share." },
    "shareMinor": { "type": "integer", "description": "This member's share in minor units." },
    "status": { "enum": ["pending", "paid", "declined"], "description": "This share's status." },
    "transactionId": { "type": "string", "description": "References the Transaction when paid; else null." }
  },
  "required": ["id", "paymentRequestId", "payerId", "shareMinor", "status"]
}
```

### WalletBalance

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/wallet-balance.schema.json",
  "title": "WalletBalance",
  "description": "A user's balance in one currency. Multi-currency wallet holds one row per currency (FEAT-014).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "userId": { "type": "string", "description": "References the owning User." },
    "currency": { "type": "string", "description": "ISO 4217 currency code; unique per user." },
    "balanceMinor": { "type": "integer", "description": "Current balance in minor units; never negative." },
    "updatedAt": { "type": "string", "format": "date-time", "description": "Last balance update." }
  },
  "required": ["id", "userId", "currency", "balanceMinor", "updatedAt"]
}
```

### Transaction

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/transaction.schema.json",
  "title": "Transaction",
  "description": "One atomic money movement. Idempotency key guarantees no double-debit on retry ([[architecture]]).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID; shown on receipts." },
    "userId": { "type": "string", "description": "References the User whose ledger this entry belongs to." },
    "type": {
      "enum": ["funding", "p2p_send", "p2p_receive", "qr_payment", "order_payment", "order_receipt", "conversion", "corridor_send", "corridor_receive", "request_share", "refund"],
      "description": "Transaction kind."
    },
    "direction": { "enum": ["credit", "debit"], "description": "Effect on this user's balance." },
    "amountMinor": { "type": "integer", "description": "Principal amount in minor units." },
    "currency": { "type": "string", "description": "ISO 4217 currency code." },
    "counterpartyId": { "type": "string", "description": "References the other User (null for funding/conversion)." },
    "orderId": { "type": "string", "description": "References the Order when this is an order payment/receipt; else null." },
    "status": { "enum": ["pending", "succeeded", "failed", "reversed"], "description": "Lifecycle." },
    "feeMinor": { "type": "integer", "description": "Fee in minor units (0 for free P2P)." },
    "settlementRef": { "type": "string", "description": "Partner-side settlement reference for reconciliation." },
    "idempotencyKey": { "type": "string", "description": "Client-supplied unique key; replays return the original result instead of double-debiting." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Transaction creation time." }
  },
  "required": ["id", "userId", "type", "direction", "amountMinor", "currency", "status", "feeMinor", "idempotencyKey", "createdAt"]
}
```

### Post

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/post.schema.json",
  "title": "Post",
  "description": "A social module post on a channel. Visible only to connections (FEAT-026).",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "channelId": { "type": "string", "description": "References the author's Channel (social module active)." },
    "text": { "type": "string", "description": "Post text (optional if media present)." },
    "mediaUrls": { "type": "array", "items": { "type": "string", "format": "uri" }, "description": "Post photos/videos." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Post creation time." },
    "deletedAt": { "type": "string", "format": "date-time", "description": "Soft-delete time." }
  },
  "required": ["id", "channelId", "createdAt"]
}
```

### PostComment

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/post-comment.schema.json",
  "title": "PostComment",
  "description": "A comment on a post. Visibility is restricted to mutual connections, enforced server-side.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "postId": { "type": "string", "description": "References the Post." },
    "commenterId": { "type": "string", "description": "References the commenting User." },
    "text": { "type": "string", "description": "Comment text." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Comment creation time." }
  },
  "required": ["id", "postId", "commenterId", "text", "createdAt"]
}
```

### VerificationApplication

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/verification-application.schema.json",
  "title": "VerificationApplication",
  "description": "A merchant verification application (FEAT-005). Current state is mirrored on BusinessProfile.verificationStatus.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "channelId": { "type": "string", "description": "References the applying Channel." },
    "idDocumentType": { "type": "string", "description": "Government ID type submitted." },
    "businessIdentifier": { "type": "string", "description": "CAC number or matched bank account identifier where available." },
    "status": { "enum": ["submitted", "under_review", "approved", "rejected"], "description": "Application lifecycle." },
    "rejectionReason": { "type": "string", "description": "Reason shown to the merchant when rejected." },
    "createdAt": { "type": "string", "format": "date-time", "description": "Submission time." },
    "reviewedAt": { "type": "string", "format": "date-time", "description": "Review completion time (null until decided)." }
  },
  "required": ["id", "channelId", "idDocumentType", "status", "createdAt"]
}
```

### NotificationPreference

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://pamoja.app/schema/notification-preference.schema.json",
  "title": "NotificationPreference",
  "description": "Per-category push preferences (FEAT-032). One row per user.",
  "type": "object",
  "properties": {
    "id": { "type": "string", "description": "Stable UUID." },
    "userId": { "type": "string", "description": "References the User; unique per user." },
    "messages": { "type": "boolean", "description": "Push for new messages." },
    "orders": { "type": "boolean", "description": "Push for order events." },
    "payments": { "type": "boolean", "description": "Push for payment confirmations." },
    "promotions": { "type": "boolean", "description": "Push for promotions — never on without explicit opt-in." },
    "updatedAt": { "type": "string", "format": "date-time", "description": "Last preference update." }
  },
  "required": ["id", "userId", "messages", "orders", "payments", "promotions", "updatedAt"]
}
```

## Relationships

- **User** 1 — 1 **Channel** — each user owns exactly one channel; `Channel.userId` references `User`.
- **Channel** 1 — 0..1 **BusinessProfile** — exists only when the business module is active (FEAT-004).
- **Channel** 0..N **Product** — `Product.channelId` references the merchant channel.
- **Channel** 0..N **Post** — `Post.channelId` references the author's channel (social module).
- **Channel** 0..N **Order** (merchant side) — `Order.merchantChannelId` references the selling channel.
- **Order** N — 1 **User** (buyer side) — `Order.buyerId` references the buying User. **This is the no-CRM-wall decision: the buyer is a graph contact, never a separate customer entity.**
- **Order** 1 — N **OrderItem** — `OrderItem.orderId` references the order; `productSnapshot` preserves price at order time.
- **Order** 0..1 **Conversation** — `Order.conversationId` references the thread where the order lives.
- **Message** 0..1 **Order** — `Message.orderId` embeds order cards by reference.
- **Message** 0..1 **Transaction** — `Message.transactionId` embeds payment/receipt cards by reference.
- **User** N — N **User** via **Connection** — mutual relationships (`requesterId`/`acceptorId`), never followers.
- **User** N — N **User** via **Block** — `blockerId`/`blockedId` enforce graph, search, and messaging exclusion.
- **Conversation** 1 — N **ConversationParticipant** — membership with per-member read position; `lastReadMessageId` drives unread counts.
- **Conversation** 1 — N **Message** — thread history; system messages (type = system) carry no sender media.
- **User** 1 — N **WalletBalance** — one row per currency; the multi-currency wallet (FEAT-014).
- **User** 1 — N **Transaction** — `Transaction.userId` is the ledger owner; every P2P send creates a debit for the sender and a credit for `counterpartyId`.
- **PaymentRequest** 1 — N **PaymentRequestPart** — one share per member of a split bill; paid parts reference their `Transaction`.
- **Post** 1 — N **PostComment** — `PostComment.postId`; visibility resolved against the graph at read time.
- **BusinessProfile** 0..N **VerificationApplication** — applications over time; `BusinessProfile.verificationStatus` mirrors the latest decision.
- **User** 0..1 **NotificationPreference** — per-category push opt-ins; promotions default off.

## Design Notes

- **Money is integer minor units everywhere** (`priceMinor`, `amountMinor`, `balanceMinor`, `totalMinor`, `shareMinor`, `feeMinor`) with explicit `currency` — no floats anywhere.
- **Idempotency is mandatory on every `Transaction`** — `idempotencyKey` is required; replays return the original result, preventing double-debit ([[risk_log]] R-005).
- **Soft deletes for user-visible content** (`deletedAt` on Message, Post) so deletions propagate cleanly to all viewers.
- **No search state in entities** — the index is derived from channel/module signals at write time via events ([[architecture]] Search Service).
- **Tier gates are not in the schema** — Free vs. Merchant tier (20-product cap, verification, inventory, delivery, analytics) is policy enforced by the Business Module Service, not by entity shape. See [[monetization]].
- **Module entities never cross-reference** — no Product references a Post, no Order references a PostComment. Module independence is structural in the data model.
## Screen 3: Chat Thread

**Route:** `/chat/:id`
**Platform:** Mobile
**Purpose:** The deep-context conversation surface — messages, voice notes, files, payments, and orders all live in one thread.
**Entry Points:** `[[02-chats|Chats]]` (tap row), `[[08-channel-profile|Channel Profile]]` (Message), Search (message result), QR payment (merchant notification thread).
**Exit Points:** `[[02-chats|Chats]]`, `[[08-channel-profile|Channel Profile]]`, `[[07-my-channel|My Channel]]` (merchant side, Orders tab).

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area; Chat Thread fills the content area (deep context, rail still visible)
- AppBar: avatar + name + verification badge (verified merchants), unread/typing indicator; actions: call, channel
- Body: scrollable message list — bubbles (own vs. theirs), voice note cards, image/file cards, order cards, payment cards, receipts
- Composer bar: + button (media, voice note, payment, order), text field, send button
- Sheet triggers from +: media picker, hold-to-talk voice note, Transfer sheet, Order composer, sticker picker

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Message bubble | Custom container | Mobile | Own/their messages | Realtime + history |
| Voice note card | Custom container | Mobile | Hold-to-talk playback (FEAT-006) | GET media |
| Image/file card | Card | Mobile | Shared media | GET media |
| Call action | IconButton | Mobile | Voice/video call (FEAT-008) | — |
| Sticker picker | Sheet | Mobile | Sticker send (FEAT-009) | Static packs |
| Order card | Card | Mobile | Order state in chat (shared pattern) | GET order |
| Payment receipt card | Card | Mobile | Payment confirmation (shared pattern) | GET transaction |
| Transfer sheet | Sheet | Mobile | P2P send (per [[user_flow]] Flow 7) | Wallet service |
| Order composer | Sheet | Mobile | Build order from catalog (per [[user_flow]] Flow 5) | Catalog data |
| Composer bar | Custom | Mobile | Text + attachment entry | — |

### Data Requirements

**Data Needed:**
- Message history (paginated) — GET messages
- Realtime message stream — subscribe to thread
- Participant identity (name, avatar, verification, presence)
- Order state (when order cards present)
- Wallet balance (for transfer/order pay)

**Data Flow:**
1. Open thread → loading history (most recent page first)
2. Subscribe to realtime stream; new messages append live
3. Sending: optimistic append with pending state → delivery → read
4. Payment/order actions: sheets validate, submit, then update the thread's order/payment cards
5. Offline: writes queue locally, replay on reconnect; read states reconcile

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Loading** | History fetch | Skeleton bubbles |
| **Loaded** | History + live stream | Full thread |
| **Empty** | No messages yet | Illustration + "Say hello" + suggested first message |
| **Offline** | No connectivity | Banner; pending messages show "sending…" then "queued" |
| **Sending** | Optimistic append | Bubble with clock/pending icon |
| **Delivery/Read** | Ack received | Double-check / read indicators |
| **Payment pending** | Payment failed | Order card stays pending with Retry (idempotent, no double debit) |
| **Blocked** | Contact blocked | Read-only notice at top; send disabled |
| **Typing** | Peer typing | "typing…" indicator in AppBar |

**Edge Cases:**
- Message deletion → removed for both parties, shows "message deleted"
- Very long text → bubble max-width, wraps; no clipping
- Large file upload → progress bar; retry on failure
- Voice note while recording → timer; cancel by sliding; release to send
- Order composer with no catalog → sheet explains the merchant has no products yet
- Deep link to chat → opens thread; unauthenticated → Onboarding then return
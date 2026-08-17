# Features

## Overview

Pamoja is a pan-African super app built around a per-user **channel model**: every user has one modular channel, and channels are found through intent-driven search. The feature set below is organized around the merchant-wedge loop — identity, messaging, payments, business module, and search interlock so a merchant can pull customers into the graph and sell to them without leaving the app. Features are bounded by the scope and non-goals in [[README]]: no customer CRM separation, no in-house licenses in v1, payments always ride licensed partner rails, and the social graph stays relationship-based.

## Priority Definitions

| Priority | Label | Meaning |
|---|---|---|
| **P0** | Must Have | Critical for launch. The product cannot ship without these. |
| **P1** | Should Have | Important but not launch-blocking. Ship soon after launch. |
| **P2** | Could Have | Nice to have. Adds polish or delight. Ship when capacity allows. |
| **P3** | Won't Have Now | Acknowledged but deferred. Revisit in a future planning cycle. |

## Onboarding, Identity & the Channel

### FEAT-001: Phone registration & OTP verification

**Priority:** P0
**Effort:** M
**Depends On:** None

**User Story:**
As a new user (Ada, Chidi, Ngozi, or Tunde), I want to sign up with just my phone number so that I can join without needing an email or password.

**Description:**
Registration uses a phone number and OTP verification. No email required, no password at signup. The phone number becomes the anchor of the user's identity and the primary login credential. One account per phone number.

**Acceptance Criteria:**
- [ ] User enters a phone number and receives an OTP within 60 seconds
- [ ] User can verify with the OTP and enters the app; verification failure shows a clear error
- [ ] A user who verifies a previously-registered number is recognized and logs into the existing account
- [ ] Registration works on both iOS and Android, and on a low-bandwidth connection
- [ ] Terms, privacy notice, and consent for the launch market's data rules are shown and accepted before account creation completes

### FEAT-002: Channel profile creation

**Priority:** P0
**Effort:** M
**Depends On:** FEAT-001

**User Story:**
As any user, I want to set up my channel with a name, bio, and photo so that others can find and understand who I am.

**Description:**
Every user creates their channel profile on first entry: display name, bio/description, and avatar. This is Layer 0 findability — name and bio are always searchable. The channel is the user's public surface inside Pamoja.

**Acceptance Criteria:**
- [ ] User can set a display name, bio, and avatar during onboarding and edit them later
- [ ] Display name is required; bio and avatar are optional but encouraged
- [ ] Channel name is searchable as soon as it is saved; bio becomes searchable immediately
- [ ] User can preview their channel exactly as others will see it
- [ ] A minimum-viable channel (name only) can be completed without blocking on other fields

### FEAT-003: Contact graph (sync, invite, connect)

**Priority:** P0
**Effort:** L
**Depends On:** FEAT-001

**User Story:**
As any user, I want to find my existing contacts in Pamoja and invite the rest so that my channel is connected to the people I actually know.

**Description:**
The user can optionally sync their phone contacts (with explicit permission) to see who is already on Pamoja, send invites to the rest, and manage incoming/outgoing connection requests. Connections are mutual — this is the real-person relationship graph, not a follower graph.

**Acceptance Criteria:**
- [ ] User can opt into phone-contact sync and revoke the permission at any time
- [ ] Contacts already on Pamoja appear in a "People you know" list and can be connected with one tap
- [ ] Contacts not yet on Pamoja can be invited by SMS/WhatsApp share link; the invite shows the inviter's channel
- [ ] Connection requests must be accepted by the recipient; no one becomes a connection unilaterally
- [ ] User can block a contact; blocked users cannot see the block, message them, or appear in their graph

### FEAT-004: Channel modules opt-in

**Priority:** P0
**Effort:** S
**Depends On:** FEAT-001, FEAT-002

**User Story:**
As any user (especially Tunde), I want to choose which modules my channel carries so that I get business tools only if I need them, and social features if I want them.

**Description:**
A channel is modular. At signup and later from settings, the user opts into modules: the business module, the social module, both, or neither (messaging-only). Opting into a module activates its features and adds its searchable signals to the channel's findability.

**Acceptance Criteria:**
- [ ] User can enable or disable the business and social modules from settings at any time
- [ ] Disabling a module hides its features and removes its search signals from the channel's findability
- [ ] Re-enabling a module restores the channel's previous data and search signals
- [ ] A messaging-only channel (no modules) remains fully usable for chat
- [ ] Module selection is reflected on the channel profile visible to others

### FEAT-005: Merchant verification badge

**Priority:** P1
**Effort:** M
**Depends On:** FEAT-002

**User Story:**
As a merchant (Ada), I want to prove my business is real so that strangers trust buying from my channel.

**Description:**
A verification process for business channels that confirms the owner is a real, operating business. Verified channels receive a gold badge on their profile, search results, and messages. Verification is identity/KYC-based via the payment partner where possible.

**Acceptance Criteria:**
- [ ] Merchant can apply for verification from their channel settings
- [ ] Verification requires at least one government-issued ID and a business identifier where available (CAC, bank account match)
- [ ] Application status is visible (submitted, under review, approved, rejected with reason)
- [ ] Verified channels display the gold badge on profile, search results, and chat header
- [ ] Verification can be revoked if the merchant is found to be fraudulent or the business details change materially

### FEAT-025: Channel visibility (see other channels)

**Priority:** P0
**Effort:** S
**Depends On:** FEAT-002

**User Story:**
As any user, I want to view another user's channel so that I can see who they are and what they do — the same way they see mine.

**Description:**
Every user's channel is viewable to their connections. A channel shows the profile (name, bio, avatar) and the modules it carries (social posts, catalog, or both) — the channel shell that presents whatever the owner has opted into. This is the "customers are friends, not CRM rows" principle made visible: commerce partners are also people with lives.

**Acceptance Criteria:**
- [ ] User can open any connection's channel and see their profile and active modules
- [ ] Business module owners see a "browse shop" view; social module owners see their posts
- [ ] A merchant viewing a customer's channel sees the same social identity the customer shares with everyone else (no hidden buyer data, no CRM wall)
- [ ] Channel privacy settings allow the owner to restrict what connections can see

## Messaging & Communication

### FEAT-006: 1:1 messaging (text, image, voice note, file)

**Priority:** P0
**Effort:** L
**Depends On:** FEAT-001, FEAT-003

**User Story:**
As any user, I want to message my connections with text, photos, voice notes, and files so that I can communicate with the people I know without leaving Pamoja.

**Description:**
Core one-to-one messaging between connected users: text, images, hold-to-talk voice notes, and file sharing. Message delivery, read state, and offline queueing work reliably on low-bandwidth connections.

**Acceptance Criteria:**
- [ ] User can send and receive text, images, voice notes, and files in 1:1 chats
- [ ] Messages queue offline and deliver when connectivity returns, without loss
- [ ] Sender sees delivery and read states (delivered / read)
- [ ] Images and files upload on a low-bandwidth connection with visible progress and retry on failure
- [ ] User can delete a message they sent; deletion is reflected for both parties
- [ ] User can block and report a contact from within a chat

### FEAT-007: Group messaging

**Priority:** P1
**Effort:** M
**Depends On:** FEAT-006

**User Story:**
As any user, I want to create and join group chats so that I can coordinate with families, communities, and buyer groups in one thread.

**Description:**
Group chats with member management, group naming, and shareable invite links or QR codes. Groups are capped at a sensible size for the launch phase and can be elevated later.

**Acceptance Criteria:**
- [ ] User can create a group, name it, and add members by invite link, QR, or direct add
- [ ] Group admins can add/remove members, and change the group name and photo
- [ ] Members can leave a group; leaving shows a system message to the group
- [ ] Group invite links expire on admin request
- [ ] Group works on the same messaging infrastructure as 1:1 chats (offline queue, delivery states)

### FEAT-008: Voice & video calls

**Priority:** P1
**Effort:** XL
**Depends On:** FEAT-006

**User Story:**
As any user, I want to make voice and video calls to my connections so that I can talk in real time without another app.

**Description:**
One-to-one voice and video calls over the Pamoja connection. Designed to work on low bandwidth with graceful degradation to audio-only. Group calls are deferred.

**Acceptance Criteria:**
- [ ] User can start a voice call from a 1:1 chat; the callee receives a full-screen incoming call
- [ ] User can start a video call; video degrades to audio-only automatically on weak connections
- [ ] Call quality indicator is visible during calls
- [ ] User can decline or mute a call; missed calls appear in the chat as a message
- [ ] Calls respect the OS audio session and stop when the app backgrounds

### FEAT-009: Stickers & emoji

**Priority:** P2
**Effort:** S
**Depends On:** FEAT-006

**User Story:**
As any user, I want to send stickers and emoji so that I can express myself in chats.

**Description:**
Emoji picker and a starter sticker set with African visual culture; support for third-party sticker packs later.

**Acceptance Criteria:**
- [ ] Emoji picker works in any chat input
- [ ] A starter sticker pack (12+ stickers, African art direction per [[branding]]) is available
- [ ] Stickers render reliably at low bandwidth (preloaded, compressed)

## Payments (partner rails)

### FEAT-010: Wallet funding & P2P transfers

**Priority:** P0
**Effort:** XL
**Depends On:** FEAT-001

**User Story:**
As any user (especially Ada), I want to hold a wallet and send money to my contacts so that paying someone is as easy as messaging them.

**Description:**
A Pamoja wallet backed by licensed partner rails. Users fund the wallet from a bank account, card, or USSD where available, and send money to their connections instantly. P2P sends are chat-native — a transfer is initiated from a chat or contact. All settlements, KYC, and compliance are handled by the licensed partner.

**Acceptance Criteria:**
- [ ] User can fund their wallet via at least one method (bank transfer, card, or USSD) per launch market
- [ ] User can send money to a connection; the recipient sees a payment message in their chat and a wallet credit
- [ ] Transfer succeeds or fails atomically; on failure the sender's balance is unchanged and a clear error is shown
- [ ] Transaction fees (if any) are displayed before the user confirms a transfer
- [ ] Wallet balance, transaction history, and a minimum balance check are visible
- [ ] The app never stores card or bank credentials — all sensitive payment data lives with the licensed partner

### FEAT-011: QR payments

**Priority:** P0
**Effort:** M
**Depends On:** FEAT-010

**User Story:**
As a merchant (Ada), I want to display a QR code that customers scan to pay so that I can take payments in the physical market without a terminal.

**Description:**
Merchant QR codes. A customer scans a merchant's QR from the app and pays from their wallet; the merchant receives a payment notification with the amount and customer identity (graph contact, not anonymous).

**Acceptance Criteria:**
- [ ] Merchant can display a static payment QR from their channel or business module
- [ ] Customer can scan the QR and confirm payment of the displayed amount (editable amount for open amounts)
- [ ] Merchant receives a real-time payment notification identifying the payer as a known contact where applicable
- [ ] QR payment failures show the merchant no credit and the customer no debit
- [ ] QR renders and scans correctly on both low-end and high-end devices

### FEAT-012: Transaction history & receipts

**Priority:** P0
**Effort:** M
**Depends On:** FEAT-010

**User Story:**
As any user, I want a full history of my money movement so that I know who paid me, who I paid, and when.

**Description:**
A transaction history covering wallet funding, P2P sends/receives, QR payments, and order payments. Each transaction has a shareable receipt with a transaction ID.

**Acceptance Criteria:**
- [ ] User can view all transactions with date, counterparty, amount, and status
- [ ] Each transaction can be opened for detail and shared as a receipt with a transaction ID
- [ ] History is filterable by type (sent, received, funded, order)
- [ ] Failed transactions appear in history with an error state
- [ ] History loads correctly at low bandwidth (paginated, lazy-loaded)

### FEAT-013: Split bills & payment requests

**Priority:** P1
**Effort:** M
**Depends On:** FEAT-010

**User Story:**
As any user (Chidi), I want to send a payment request or split a bill with friends so that settling shared costs is quick.

**Description:**
Payment requests sent to a connection, and equal-split bills across a group. Requests appear in chat as a payable message.

**Acceptance Criteria:**
- [ ] User can send a payment request for an amount with a note; the recipient sees it in chat
- [ ] Recipient can pay, decline, or ignore a request; the sender sees the outcome
- [ ] User can split an amount equally across selected group members
- [ ] Each member's share and paid status is visible in the bill thread

### FEAT-014: Multi-currency wallet

**Priority:** P1
**Effort:** L
**Depends On:** FEAT-010

**User Story:**
As a diaspora user (Ngozi), I want to hold and convert between currencies so that I can send money home and shop across borders without a separate app.

**Description:**
The wallet holds balances in multiple currencies (launch: naira plus one corridor currency; more as markets open). Conversion uses transparent rates from the payment partner. Cross-border settlement is phased — the architecture supports it, the corridors activate per market.

**Acceptance Criteria:**
- [ ] Wallet shows balances in each supported currency
- [ ] User can convert between currencies with a visible rate and fee before confirming
- [ ] A funded non-naira balance can be used to pay a naira merchant through conversion at checkout
- [ ] Unsupported corridors show a clear "not yet available" state rather than a failed attempt

### FEAT-015: Cross-border transfers (diaspora corridor)

**Priority:** P2
**Effort:** L
**Depends On:** FEAT-014

**User Story:**
As a diaspora user (Ngozi), I want to send money from my home-country wallet to family in Africa so that I stop paying remittance fees to intermediaries.

**Description:**
A dedicated diaspora corridor (launch: UK→Nigeria or US→Nigeria) where users fund in their home currency and recipients receive in local currency, delivered in-app with a chat message.

**Acceptance Criteria:**
- [ ] Diaspora user can fund their wallet in the home currency and send to a Nigerian contact
- [ ] Recipient receives local-currency credit in-app with a chat notification
- [ ] Total cost (fee + spread) is shown before send confirmation
- [ ] Corridor is KYC/AML compliant with the licensed partner in both jurisdictions

## Business Module

### FEAT-016: Product catalog

**Priority:** P0
**Effort:** M
**Depends On:** FEAT-002, FEAT-004

**User Story:**
As a merchant (Ada or Tunde), I want to list my products with photos, prices, and categories so that customers can see and buy what I sell.

**Description:**
The merchant's product catalog: product name, photos, price (in the launch currency), category, description, and stock availability flag. Catalog items become searchable business-module content for channel findability.

**Acceptance Criteria:**
- [ ] Merchant can add, edit, delete, and reorder products with name, photo(s), price, category, and optional description
- [ ] Products appear on the merchant's channel for visitors to browse
- [ ] Product names, categories, and descriptions are indexed for search
- [ ] Photos upload and compress correctly at low bandwidth
- [ ] At least one product must exist before the business module's "open shop" state is complete

### FEAT-017: Order inbox

**Priority:** P0
**Effort:** M
**Depends On:** FEAT-016, FEAT-006

**User Story:**
As a merchant (Ada), I want to receive, confirm, and track orders so that I never lose a sale in chat history again.

**Description:**
An order inbox in the merchant's business module. Orders arrive from chat (see FEAT-018) and have a status workflow: new → confirmed → fulfilled → (optionally) delivered. The merchant can accept or decline an order.

**Acceptance Criteria:**
- [ ] Incoming orders appear in the merchant's order inbox with buyer, items, quantity, amount, and timestamp
- [ ] Merchant can confirm or decline an order; the buyer sees the outcome in chat
- [ ] Order status changes are visible to both merchant and buyer
- [ ] Order list is paginated and searchable by buyer or order ID
- [ ] Declined orders show a reason to the buyer

### FEAT-018: In-chat checkout (order → pay → receipt)

**Priority:** P0
**Effort:** L
**Depends On:** FEAT-017, FEAT-010

**User Story:**
As a buyer (Chidi), I want to order a product in chat and pay without leaving the conversation so that buying is as easy as messaging.

**Description:**
The checkout loop: a buyer sends an order from a merchant's catalog or channel, the merchant confirms it in the order inbox, the buyer pays from their wallet inside the chat, and both sides receive an in-chat receipt. This is the closed loop — discovery, order, payment, and receipt all in one place.

**Acceptance Criteria:**
- [ ] Buyer can add items from a merchant's catalog to an order and send it as a chat message
- [ ] Merchant confirmation triggers a payable state in the buyer's chat
- [ ] Buyer pays from wallet without leaving the chat; on payment, both parties receive a receipt message
- [ ] If payment fails, the order remains pending with a retry action for the buyer
- [ ] Order, payment, and receipt are all visible in the same chat thread
- [ ] Merchant can see payment status on the order before fulfilling

### FEAT-019: Business tags & searchable catalog

**Priority:** P0
**Effort:** S
**Depends On:** FEAT-016

**User Story:**
As a merchant (Ada), I want to add tags and location to my business so that people searching for what I sell can find me.

**Description:**
Business-specific findability: merchants add optional tags and a location to their business module, and catalog content is searchable. This extends Layer 0 (name/bio) with business module signals.

**Acceptance Criteria:**
- [ ] Merchant can add tags (e.g., `ankara`, `lagos`) and set their business location on the business module
- [ ] Tags and location are searchable in unified search
- [ ] Tag suggestions are offered as the merchant types
- [ ] Removing a tag removes it from search signals immediately

### FEAT-020: Inventory management

**Priority:** P1
**Effort:** M
**Depends On:** FEAT-017

**User Story:**
As a merchant (Ada), I want to track stock levels so that I never oversell what I don't have.

**Description:**
Stock tracking per product: quantities, low-stock alerts, and automatic decrement on confirmed orders. Simple and manual-first for the merchant's reality (no barcode scanners assumed).

**Acceptance Criteria:**
- [ ] Merchant can set and edit stock quantity per product
- [ ] Confirming an order decrements stock; stock cannot go below zero
- [ ] Low-stock threshold triggers a notification to the merchant
- [ ] Out-of-stock products show "out of stock" to buyers and cannot be ordered

### FEAT-021: Delivery tracking

**Priority:** P1
**Effort:** M
**Depends On:** FEAT-017

**User Story:**
As a merchant (Ada) and a buyer (Chidi), I want to track the delivery stages of an order so that we both know where the goods are.

**Description:**
Manual delivery stages set by the merchant: packed → handed to rider → in transit → delivered. Both parties see the current stage on the order. Third-party logistics integration is deferred.

**Acceptance Criteria:**
- [ ] Merchant can advance an order through delivery stages
- [ ] Buyer sees the current delivery stage on the order and in chat
- [ ] Stage changes notify both parties
- [ ] A delivered order can be marked complete by either party

### FEAT-022: Merchant analytics (basic)

**Priority:** P2
**Effort:** M
**Depends On:** FEAT-017

**User Story:**
As a merchant (Ada), I want to see my sales numbers so that I can prove my business is real when seeking credit or planning stock.

**Description:**
Basic analytics: total sales, orders by status, top products, and revenue over time. No sophisticated dashboards — the merchant's phone is the canvas.

**Acceptance Criteria:**
- [ ] Merchant sees total revenue, order count, and top products for a selectable period
- [ ] Analytics load from real order data (no mock figures)
- [ ] Analytics are shareable as a summary image or export for credit applications

## Unified Search

### FEAT-023: Unified search (name + bio; grouped results)

**Priority:** P0
**Effort:** L
**Depends On:** FEAT-002, FEAT-006

**User Story:**
As any user (Chidi), I want to type one thing and get grouped results — channels, people, and messages — so that I can find what I need in one search.

**Description:**
One search box across the whole network. Results are grouped by type: channels (business and social), people, and messages. Matching is intent-driven across the channel findability layers (name and bio always; module signals when present). Search is the product's discovery layer.

**Acceptance Criteria:**
- [ ] Typing a query returns grouped results: channels, people, and messages
- [ ] Channel name and bio matches appear for every channel (Layer 0)
- [ ] Module signals (tags, catalog) surface when the channel carries those modules
- [ ] "I want to buy shoes" surfaces business channels selling shoes (commerce intent)
- [ ] A social interest like "afrobeats" surfaces social channels matching by name/bio
- [ ] Results are relevant (relevance-ranked, not alphabetical) and load within a bounded time on low bandwidth
- [ ] Empty and no-results states are clear and suggest a corrected query

### FEAT-024: Business content search (catalog, filters)

**Priority:** P1
**Effort:** L
**Depends On:** FEAT-023, FEAT-016

**User Story:**
As a buyer (Chidi or Ngozi), I want to search inside catalogs and filter by category, location, or verified status so that I can narrow down sellers.

**Description:**
Search refinement for commerce: filter results by category, business location, verification badge, and price. Catalog content is indexed at the product level, not just the channel level.

**Acceptance Criteria:**
- [ ] User can filter business results by category, location, verified-only, and price range
- [ ] Product-level matches appear (search "nike air force" finds products, not just channels)
- [ ] Filters combine (e.g., verified fashion in Lagos under ₦10,000)
- [ ] Filter state is reflected in the URL/shareable search link for repeated use

## Social Module

### FEAT-026: Private friends feed (Moments-style)

**Priority:** P1
**Effort:** M
**Depends On:** FEAT-004, FEAT-003

**User Story:**
As any user, I want to post updates that only my connections can see so that I can share life moments without a public platform.

**Description:**
A private, connections-only feed (Moments-style): photo/text posts visible only to mutual connections. Comments are visible only to mutual friends (the WeChat design that keeps discussions small). This is the social module's core.

**Acceptance Criteria:**
- [ ] User can post photos, text, or both to their social module
- [ ] Posts are visible only to the user's connections
- [ ] Comments are visible only to users who are connections of both the author and the commenter
- [ ] User can delete a post; deletions propagate to all viewers
- [ ] Feed loads at low bandwidth with lazy pagination

### FEAT-027: Status & light self-expression

**Priority:** P2
**Effort:** S
**Depends On:** FEAT-026

**User Story:**
As any user, I want to set a status or pin a short note so that my channel shows what I'm up to without posting.

**Description:**
A lightweight status field on the channel (e.g., "Open for business", "On the road") visible to connections.

**Acceptance Criteria:**
- [ ] User can set, edit, and clear a status on their channel
- [ ] Status appears on the user's channel and chat list context
- [ ] Status auto-clears after a configurable duration

## Trust, Security & Compliance

### FEAT-028: App lock (PIN & biometric)

**Priority:** P0
**Effort:** S
**Depends On:** FEAT-001

**User Story:**
As any user handling money (Ada), I want to lock the app so that my wallet and chats are protected if my phone is lost or borrowed.

**Description:**
Optional app lock with PIN and platform biometrics. Required on app open when enabled; wallet actions can additionally demand re-verification.

**Acceptance Criteria:**
- [ ] User can enable a 4-6 digit PIN and/or biometric unlock
- [ ] Lock engages on app background and requires unlock on return
- [ ] Wallet send actions require re-verification (PIN/biometric) when configured
- [ ] Failed unlock attempts escalate to a delay and, after repeated attempts, force re-login

### FEAT-029: Block, report & scam response

**Priority:** P1
**Effort:** M
**Depends On:** FEAT-003, FEAT-006

**User Story:**
As any user, I want to block and report scammers so that I and the community are protected from fraud.

**Description:**
Blocking, reporting, and a scam-response path. Reports flow to a moderation queue; verified merchants found fraudulent are flagged or have verification revoked. Works against the Nigerian fraud threat documented in [[README]].

**Acceptance Criteria:**
- [ ] User can block a contact or channel; blocked parties cannot message, call, or appear in search
- [ ] User can report a channel, a message, or an order with a reason and evidence
- [ ] Reported content is reviewed; verified merchants found fraudulent lose their badge
- [ ] Reported users hit account limits after threshold reports while under review
- [ ] Reporting does not notify the reported party

### FEAT-030: Data-light mode

**Priority:** P1
**Effort:** L
**Depends On:** FEAT-006, FEAT-016

**User Story:**
As a user on limited data (Ada), I want the app to use as little data as possible so that I can afford to use it daily.

**Description:**
A data-saving mode: image compression, deferred media downloads, no autoplay, and cached channel/catalog content. The app must be genuinely usable on pay-per-MB plans.

**Acceptance Criteria:**
- [ ] Data-light mode compresses images and defers non-essential media download
- [ ] Chat and catalog lists load with minimal payload in data-light mode
- [ ] User can toggle data-light mode per connection preference (e.g., always on cellular)
- [ ] Measured monthly consumption in data-light mode is meaningfully lower than standard mode

### FEAT-031: Multi-language UI

**Priority:** P1
**Effort:** M
**Depends On:** None

**User Story:**
As an African user, I want the app in my language so that I can use it comfortably regardless of English fluency.

**Description:**
Internationalization from day one: English at launch, with the architecture ready for Yoruba, Hausa, Igbo, Pidgin, French, and Swahili as markets open. All user-visible strings are externalized.

**Acceptance Criteria:**
- [ ] All user-visible strings are externalized (no hardcoded copy)
- [ ] English is complete at launch; a language switcher is present
- [ ] Adding a locale does not require code changes (only translations)
- [ ] Amounts, dates, and numbers format per the active locale

### FEAT-032: Push notifications

**Priority:** P0
**Effort:** M
**Depends On:** FEAT-006, FEAT-017

**User Story:**
As any user, I want to be notified of messages, orders, and payments so that I respond in time even when I'm not in the app.

**Description:**
Push notifications for messages, new orders, payment confirmations, and delivery updates. Respects OS notification permissions and user per-channel notification preferences. Data-light: no notification spam.

**Acceptance Criteria:**
- [ ] New messages, orders, payments, and delivery updates generate push notifications
- [ ] User can configure notification preferences per category (messages, orders, payments, promotions)
- [ ] Tapping a notification opens the relevant chat or order
- [ ] Notifications work on low-bandwidth and after app restart
- [ ] No promotional notifications without explicit user opt-in

## Priority Summary

| Priority | Count | Feature IDs |
|---|---|---|
| P0 | 16 | FEAT-001, FEAT-002, FEAT-003, FEAT-004, FEAT-006, FEAT-010, FEAT-011, FEAT-012, FEAT-016, FEAT-017, FEAT-018, FEAT-019, FEAT-023, FEAT-025, FEAT-028, FEAT-032 |
| P1 | 12 | FEAT-005, FEAT-007, FEAT-008, FEAT-013, FEAT-014, FEAT-020, FEAT-021, FEAT-024, FEAT-026, FEAT-029, FEAT-030, FEAT-031 |
| P2 | 4 | FEAT-009, FEAT-015, FEAT-022, FEAT-027 |
| P3 | 0 | — |

**Integrity checks (run and verified):**
- All `Depends On:` IDs resolve to a feature that exists in this document
- Dependency graph is acyclic (every chain terminates; no cycles)
- No P0 feature depends on a P1/P2/P3 feature — launch scope is buildable
- Every feature traces to at least one persona from [[user_personas]]: Ada (merchant loop), Chidi (buyer + search), Ngozi (multi-currency/corridor), Tunde (hybrid modules + findability)
- Every persona is served by multiple features: Ada → FEAT-016/017/018/019/020/021/022/011; Chidi → FEAT-023/024/018/013/026; Ngozi → FEAT-014/015/031; Tunde → FEAT-004/016/023/025/027

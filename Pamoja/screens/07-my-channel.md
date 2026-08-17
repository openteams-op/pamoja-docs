## Screen 7: My Channel

**Route:** `/channel`
**Platform:** Mobile
**Purpose:** The owner's channel — the entire modular surface in one place: Profile, Shop, Orders, and Insights tabs. The merchant toolkit lives here.
**Entry Points:** Side Rail (Channel); post-onboarding module management; merchant verification entry.
**Exit Points:** `[[08-channel-profile|Channel Profile]]` (preview as others see it), `[[09-settings|Settings]]`, Product Editor sheet, Order detail sheet, `[[03-chat-thread|Chat Thread]]` (message a buyer).

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area
- AppBar "My Channel" with "Preview" action (opens own Channel Profile)
- TabBar: Profile | Shop | Orders | Insights
- **Profile tab:** Channel Header (avatar, name, verification badge, bio), Status field (FEAT-027), Modules section (Business / Social with enable/disable), Verification status card (FEAT-005 — apply/review state), Settings entry
- **Shop tab:** Product grid (Product Cards), "Add product" FAB or button, Business tags & location editor, Free-tier cap banner (20 products)
- **Orders tab:** Order list (Order Cards) with status chips; order detail opens as sheet with delivery stages (FEAT-021)
- **Insights tab:** Merchant analytics summary (FEAT-022): total revenue, orders, top products; shareable summary action
- Empty states per tab: custom illustrations (no products, no orders, no insights yet)

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Channel Header | Custom | Mobile | Owner identity (shared pattern) | GET own channel |
| TabBar | TabBar | Mobile | Profile / Shop / Orders / Insights | — |
| Status editor | Field | Mobile | Set/clear status (FEAT-027) | PATCH channel |
| Module toggles | Switch | Mobile | Enable/disable modules (FEAT-004) | PATCH channel |
| Verification card | Card | Mobile | Apply/review merchant verification (FEAT-005) | GET verification status |
| Product Editor sheet | Sheet | Mobile | Add/edit product + stock quantity (FEAT-020) | — |
| Product Card | Card | Mobile | Product in grid (shared pattern) | GET catalog |
| Low-stock indicator | Badge on card | Mobile | Stock below threshold (FEAT-020) | Derived from stock |
| Order Card | Card | Mobile | Order in list (shared pattern) | GET orders |
| Order detail sheet | Sheet | Mobile | Full order + delivery stages (FEAT-021) | GET order |
| Insights summary | Card / list | Mobile | Analytics (FEAT-022) | GET analytics |
| Empty illustrations | Image (designer assets) | Mobile | Per-tab empty states | Static assets |

### Data Requirements

**Data Needed:**
- Own channel profile (name, bio, avatar, status, modules, verification)
- Catalog (products, stock flags, quantities) — GET catalog
- Orders (status workflow, delivery stages) — GET orders
- Analytics (revenue, orders, top products) — GET analytics
- Tier state (free vs merchant) for caps and gates

**Data Flow:**
1. Screen mounts → fetch channel + catalog + orders (parallel, per active tab)
2. Tab switching fetches lazily on first visit; keeps state while switching
3. Product create/edit → sheet (includes stock quantity) → save → catalog refresh, search index updates via events
4. Order actions → confirm/decline/fulfill/deliver → status chip updates, buyer notified in chat; confirming decrements stock (FEAT-020)
5. Analytics load on Insights tab from real order data
6. Offline → tab content cached; writes queue with pending indicators

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Loading** | First fetch per tab | Skeleton per tab |
| **Empty (Shop)** | No products | Illustration + "Add your first product" |
| **Empty (Orders)** | No orders | Illustration + "Orders will appear here" |
| **Empty (Insights)** | No sales yet | Illustration + "Sales data will appear here" |
| **Loaded** | Data fetched | Tab content |
| **Error** | Fetch failed | Error state + retry |
| **Offline** | No connectivity | Banner; cached content, queued writes |
| **Free-tier cap** | 20 products on Free tier | Banner + upgrade prompt on add attempt |
| **Low stock** | Stock below merchant threshold | Low-stock badge on the product card |
| **Verification pending** | Submitted, not reviewed | Status card shows "Under review" |

**Edge Cases:**
- Disabling Business module → Shop/Orders/Insights tabs hidden, products retained for re-enable (FEAT-004)
- Long product names → 2-line clamp in cards
- Rapid order status taps → last action wins; server reconciles
- Duplicate product names → allowed but flagged to the merchant for clarity
- Deleting a product → confirmation dialog; search index removes it via event
- Confirming an order that exceeds stock → blocked with a stock-adjust prompt (FEAT-020)
# Monetization

## Revenue Model

**Model Type:** Hybrid — free core + paid merchant toolkit (subscription), usage-based payment fees, usage-based corridor fees, and later advertising.

**Summary:**
Pamoja follows the WeChat doctrine: the core app (messaging, social, wallet, search) is free forever and is the acquisition engine. Revenue comes from the ecosystem around it: (1) a **transaction fee** on merchant order payments and QR payments, (2) a **Merchant tier subscription** for the full business toolkit, (3) **corridor and conversion fees** on cross-border money movement, and (4) later, **closed-loop advertising** once the network has density. Pamoja never charges users to talk, never sells user data, and never takes app-store-style platform rents on module transactions.

## Pricing Tiers

### Free Tier
**Price:** ₦0 / month
**Target:** Chidi (the customer), Ngozi (the diaspora buyer), and Ada/Tunde (as entry merchants)
**Purpose:** Acquisition — everyone joins free, the graph grows, and merchants experience the basic loop before upgrading.
**Includes:**
- Everything core: registration, channel profile, contact graph, messaging, group chat, calls, stickers, wallet (P2P transfers, QR receive, transaction history), unified search, social feed, app lock, data-light mode, multi-language (FEAT-001, 002, 003, 004, 006, 007, 008, 009, 010, 011, 012, 013, 023, 025, 026, 027, 028, 029, 030, 031, 032)
- Business Module **starter**: up to 20 products in the catalog, order inbox with basic confirm/decline, in-chat checkout, business tags/location (FEAT-016, 017, 018, 019)
- Merchant transaction fee applies to order/QR payments (see Payment & Billing)

**Limitations:**
- No inventory management, delivery tracking, or analytics
- No merchant verification badge
- 20-product catalog cap
- No priority search placement

### Merchant Tier
**Price:** ₦2,000 / month or ₦20,000 / year (annual ≈ 2 months free)
**Target:** Ada (the market trader) and Tunde (the creator-merchant)
**Purpose:** Core revenue — the paid tier every serious merchant should choose; it pays for itself by reducing lost sales and enabling credit-proof records.
**Includes:**
- Everything in Free, plus:
- Unlimited catalog products
- Inventory management with low-stock alerts (FEAT-020)
- Delivery tracking stages (FEAT-021)
- Merchant analytics — sales, orders, top products, shareable for credit applications (FEAT-022)
- Merchant verification badge (FEAT-005)
- Priority search placement for the channel in relevant queries
- Reduced transaction fee (0.7% vs 1.2% on the free tier)

**Limitations:**
- Single merchant channel per subscription (a merchant running multiple brands needs a future plan or separate channels)

### Enterprise Tier
**Price:** Custom / not targeted at launch
**Target:** Large organizations — deliberately deferred
**Purpose:** Not in scope. The [[README]] and [[user_personas]] anti-persona exclude large enterprises with ERP needs; the merchant toolkit is built for owner-operators. An enterprise plan is only considered once merchant tools are proven.

## Feature Gate Mapping

| Feature ID | Feature | Free | Merchant |
|---|---|---|---|
| FEAT-001 | Phone registration & OTP | Yes | Yes |
| FEAT-002 | Channel profile creation | Yes | Yes |
| FEAT-003 | Contact graph | Yes | Yes |
| FEAT-004 | Channel modules opt-in | Yes | Yes |
| FEAT-005 | Merchant verification badge | No | Yes |
| FEAT-006 | 1:1 messaging | Yes | Yes |
| FEAT-007 | Group messaging | Yes | Yes |
| FEAT-008 | Voice & video calls | Yes | Yes |
| FEAT-009 | Stickers & emoji | Starter pack | Starter pack + paid packs (future) |
| FEAT-010 | Wallet & P2P transfers | Yes | Yes |
| FEAT-011 | QR payments | Yes (transaction fee 1.2%) | Yes (transaction fee 0.7%) |
| FEAT-012 | Transaction history & receipts | Yes | Yes |
| FEAT-013 | Split bills & payment requests | Yes | Yes |
| FEAT-014 | Multi-currency wallet | Yes (conversion fee) | Yes (conversion fee) |
| FEAT-015 | Cross-border transfers | Corridor fee | Corridor fee |
| FEAT-016 | Product catalog | Up to 20 products | Unlimited |
| FEAT-017 | Order inbox | Basic (confirm/decline) | Full workflow |
| FEAT-018 | In-chat checkout | Yes | Yes |
| FEAT-019 | Business tags & searchable catalog | Yes | Yes |
| FEAT-020 | Inventory management | No | Yes |
| FEAT-021 | Delivery tracking | No | Yes |
| FEAT-022 | Merchant analytics | No | Yes |
| FEAT-023 | Unified search | Yes | Yes |
| FEAT-024 | Business content search | Yes | Yes |
| FEAT-025 | Channel visibility | Yes | Yes |
| FEAT-026 | Private friends feed | Yes | Yes |
| FEAT-027 | Status & light self-expression | Yes | Yes |
| FEAT-028 | App lock | Yes | Yes |
| FEAT-029 | Block, report & scam response | Yes | Yes |
| FEAT-030 | Data-light mode | Yes | Yes |
| FEAT-031 | Multi-language UI | Yes | Yes |
| FEAT-032 | Push notifications | Yes | Yes |

## Payment & Billing

**Payment Processor:** Licensed payment partners (per market) — the same rails as the wallet. No separate billing processor in v1.
**Billing Cycle:** Monthly and annual (annual = ₦20,000, ≈ 2 months free).
**Trial Period:** No explicit trial — the Free tier serves as the trial. A merchant upgrading sees the full toolkit immediately.
**Currency Support:** Naira (₦) for Nigerian merchants at launch; home-country currency for diaspora corridor users.
**Tax Handling:** VAT on fees handled per-market via the licensed partner; Pamoja exposes fee breakdown transparently.

**Usage fees (not subscriptions):**
- **Merchant transaction fee:** 1.2% on free-tier order/QR payments, 0.7% on Merchant tier. Displayed to the merchant before enabling paid checkout; never hidden in the buyer's price without disclosure.
- **Currency conversion fee:** 1% spread on multi-currency conversion (FEAT-014).
- **Corridor fee:** 2.5% all-in on cross-border transfers (FEAT-015) — deliberately below incumbent remittance fees of 3–6%.
- **P2P transfers are free.** Free P2P is an acquisition and graph-growth decision, per the WeChat doctrine — money between friends is the flywheel, not the revenue line.

**Billing Events:**
- **Upgrade:** User moves Free → Merchant. Immediate charge; prorated if mid-cycle. Wallet balance is the default payment method (fallback: linked card via partner).
- **Downgrade:** User cancels Merchant. Takes effect at end of the billing period; then reverts to Free with the 20-product cap and loss of paid features.
- **Cancellation:** Access continues until end of billing period, then reverts to Free.
- **Failed Payment:** Retry up to 3 times over 5 days from wallet/card. After final failure, downgrade to Free at period end; merchant data is preserved so upgrading back restores everything.
- **Refund:** Manual process via support; full or prorated refund through the payment partner.

## Key Metrics

| Metric | Definition | Target |
|---|---|---|
| Merchant-to-Paid Conversion | % of merchants with ≥1 order who upgrade to Merchant tier within 90 days | >10% |
| Payment Volume (GMV) | Total value of order + QR payments processed through Pamoja | Growth signal from launch; the primary engine |
| Transaction Fee Revenue | GMV × effective take rate | Positive by month 6 of launch |
| Paid Merchant Churn | % of Merchant-tier subscribers who cancel monthly | <5% |
| Corridor Volume | Cross-border transfer value (Phase 4) | >₦ equivalent of X monthly after corridor launch |
| P2P-to-Merchant Lift | Share of merchant orders from customers who first entered via P2P or invite | Indicates graph → commerce flywheel |
| CAC-to-LTV | Acquisition cost per paying merchant vs. lifetime value | < LTV / 3 |

## Monetization Roadmap

| Phase | Roadmap Phase | Monetization Milestone |
|---|---|---|
| 1 | Phase 1 — Platform Foundation | No paid features. Free core; focus on graph density and the merchant loop. |
| 2 | Phase 2 — Business Module (launch) | Merchant transaction fees (1.2%) go live at launch. Merchant tier (₦2,000/mo) ships with the full toolkit. |
| 3 | Phase 3 — Social Module | Free P2P continues; conversion and corridor fees stage in with FEAT-014/015 readiness. |
| 4 | Phase 4 — Foundation: Pan-African | Corridor fees live. Closed-loop advertising considered only once density justifies it — promoted business channels in search results and the social feed, always opt-in and labeled, per the [[README]] non-goals (no message scanning, no data selling). |
# Pamoja

**One-liner:** One app where Africans chat, pay, and sell — every user has a channel, and you can search the whole network of channels across borders to buy, sell, or find people.
**Status:** Concept
**Last Updated:** 2026-08-16

## Overview

Pamoja (Swahili for "together") is a **pan-African** super app, designed for the continent first and launched market by market — beginning with Nigeria. It combines four layers in one product: messaging and social communication, real-person identity, payments, and SME business management — all expressed through a per-user **channel** model.

**The channel model is the core idea.** Every user has exactly one channel — their public surface inside Pamoja. A channel is modular: its owner opts into which feature modules it carries. A user can run a **business module** (catalog, orders, inventory, payments), a **social module** (feed, posts, status), or both. Not everyone gets the same thing; the channel is what you make of it.

The architecture follows WeChat's proven stack: the contact list is the moat (real-life relationships, not a follower graph); payments sit on top of that graph so money moves as easily as a message; and business channels turn that money movement into a marketplace. The wedge that grows the graph is the small business: African SME traders already sell over WhatsApp manually — Pamoja gives them chat, orders, payment, and a real storefront in one place, and their customers follow them in.

**Africa-first, not Nigeria-first:** multi-currency, multi-language, and cross-border commerce are core design pillars, not retrofits. A trader in Lagos can be found by a buyer in Accra; a family in London can pay a relative in Nairobi. **Channel findability is how a channel is discovered through search.** Findability is layered: every channel has a base layer that is always searchable, and each module the owner opts into adds more searchable signals of its own.

**Layer 0 — Channel profile (every user, always):**
1. **Name** — the handle/display name (e.g., "Tunde Soles")
2. **Bio / description** — free-text, in the owner's own words, saying what the channel is and does (this is what makes intent search work)

**Layer 1+ — Module signals (added when the user opts into a module):**
- **Business module:** optional tags (e.g., `sneakers`, `lagos`) plus business module content — product names, categories, and descriptions
- **Future modules:** whatever that module makes searchable by design (e.g., a creator module might index post topics; a services module might index location and pricing). The search index is extensible: each module declares what of its data is searchable, and findability grows with the modules a channel carries.

Search is intent-driven across all layers: "I want to buy shoes" hits bios and catalogs; "tunde soles" hits the name; "sneaker restoration" hits the bio and tags. A pure-social channel is findable by name and bio; a business channel is findable by all of its layers. This is the difference between rigid WeChat-style discovery and real intent search, and it is the source of truth that [[features]], [[schema]], and [[user_flow]] inherit.

The differentiator is **unified channel search**: one search box, grouped results, intent-driven, across the whole network — "I want to buy shoes" returns business channels selling shoes; "afrobeats" returns social channels whose name or description matches that interest. Pamoja is the index over the African super-app.

## The Problem

African small business owners and their customers live across four or five apps per country — and the apps don't talk to each other across borders. A trader chats with buyers on WhatsApp, receives money via bank transfer or a local fintech (OPay, M-Pesa, Wave), advertises on Instagram or WhatsApp status, keeps orders in a notebook, and has no real storefront or payment record. Cross-border, the problem deepens: 54 countries, dozens of currencies, fragmented payment rails, and some of the highest remittance and transfer costs in the world.

**How it's solved today:** WhatsApp handles communication (with no order management, no payments, no storefronts); standalone fintech apps handle money but only within their country or corridor; Instagram/WhatsApp status handle discovery but not transactions; cross-border trade runs on expensive SWIFT-like corridors or informal networks. Nobody owns the full loop anywhere, and nothing spans the continent. Sellers patch the gap with notebooks, screenshots, and multiple apps.

## The Solution

Pamoja closes the loop WeChat closed in China — and then widens it across Africa: one identity graph, one payment rail abstraction, one channel per person, and messaging as the connective tissue. A buyer discovers a business channel via search or a social feed, orders inside the conversation, pays without leaving the app, and the seller gets a transaction record plus order and inventory management. Because identity is real-person based, merchants can trust who they're trading with — the foundation WeChat's Layer 1 provides.

**Commerce is peer-to-peer by design.** There is no separate "customer list" — a merchant's customers are their normal contacts in the graph, people who also have channels. The merchant can see what a buyer does socially, and the buyer can see the merchant's channel too. Trust comes from the shared graph, not from a CRM wall. Business management is real — catalog, orders, inventory, payments — but it operates on people you already know.

**Africa-first means cross-border from day one:** a multi-currency wallet abstraction, per-market currency settlement, multi-language UI, and channel search that works across the network. Payments ship on licensed partner rails in each market (the Tencent playbook: WeChat Pay initially ran on Tenpay's rails), keeping local compliance with licensed partners while Pamoja owns the graph, the channels, and the user experience.

## Target Audience

**Primary:** African SME owners and market traders — shop owners, fashion vendors, food sellers, electronics and fabric traders. Launch beachhead is Nigeria (Lagos and the major markets: Onitsha, Aba, Balogun, Computer Village), then neighboring trade corridors. They have the strongest pain, the highest willingness to pay, and the biggest incentive to pull their own customers into a new app.

**Secondary:** The customers of those traders — urban Africans who follow merchants in for ordering, payment, and delivery tracking. Also the diaspora — one of the largest remittance sources in the world — buying for relatives back home and cross-border.

**Not for:** Large enterprises with complex ERP needs, and (initially) fully offline/rural users who can't reach data connectivity. The app is Africa-first by design, but each launch market targets connected urban and semi-urban users before expanding.

## SWOT Analysis

### Strengths *(internal, positive)*
- WeChat-informed architecture from day one: identity graph first, payments on top, business channels on top of that — the exact layering that produced WeChat's moat.
- **Africa-first by design**: multi-currency, multi-language, cross-border architecture is core — not retrofitted the way competitors add markets later.
- Funded/established team with capital for a long build-and-burn cycle — the patience WeChat's growth curve demands (it took years to reach its flywheel).
- Partner-first payments per market: launch without local licensing overhead in each country; compliance, settlements, and KYC live with licensed partners.
- The channel model is structurally differentiated: unified intent-driven search over modular channels is something neither WhatsApp, Jumia, nor any local fintech offers.
- Commerce-as-graph (no CRM separation) matches existing African behavior — sellers already sell socially over WhatsApp to people they know; Pamoja formalizes what they already do.

### Weaknesses *(internal, negative)*
- No existing user base or social graph — starting from zero against WhatsApp's entrenched contact graph in every market.
- Network effects are the core value and they start cold; early users get a mostly-empty graph, which weakens retention until density arrives market by market.
- No in-house payment licenses — the payments roadmap depends on partners' fees, terms, uptime, and regulatory posture in each country.
- Africa-first multiplies regulatory surface: every launch market has its own data law, payment rules, and KYC regime, and NDPR does not extend beyond Nigeria.
- The channel model is novel — category creation risk: users must learn why they need a channel and a modular account rather than a profile.
- Very large scope for a first version (messaging + social + identity + payments + business channels + cross-border); trimming the first release reduces delivery risk but deferred features still have to be built.

### Opportunities *(external, positive)*
- Africa's cash-to-digital leapfrog: a continent-scale unbanked/underbanked population is being pulled into mobile money — the exact conditions that made WeChat Pay and M-Pesa.
- WhatsApp's structural limits: no order management, no payments integration in most African markets, capped group sizes, no storefronts — sellers already outgrow it.
- Licensed fintech rails in each market (Paystack, Flutterwave, OPay, M-Pesa, Wave) have open APIs and proven local compliance paths, making partner-first builds fast and credible.
- AfCFTA is actively lowering intra-African trade barriers — cross-border commerce is a genuine greenfield with no dominant platform.
- Africa's diaspora is the largest remittance corridor in the world; a pan-African wallet with cheap corridors is a huge, underserved market.
- No pan-African super app exists; every strong player (OPay, M-Pesa, Wave) is single-market or corridor-focused — the continent-wide channel network is unclaimed.
- Unified channel search has no incumbent — whoever owns "find it in the app" owns the discovery layer.

### Threats *(external, negative)*
- WhatsApp/Meta directly owns the messaging graph and is expanding WhatsApp Business catalogs, payments in some markets, and business tools — the incumbent is strengthening, not standing still.
- Deep-pocketed local fintechs in each market (OPay, Moniepoint, Paga, M-Pesa, Wave) are super-app-adjacent with licenses, capital, and agent networks; any can add chat or storefronts.
- Regulatory fragmentation across 54 jurisdictions — currency controls, capital restrictions, KYC/AML divergence, and licensing thresholds can slow or reshape expansion in any single market.
- Currency volatility and cross-border settlement risk can make multi-currency wallets operationally hard and economically fragile.
- Data cost and low-end Android hardware constrain feature-heavy apps across the continent — the app must be data-light to win.
- Fraud and scam fatigue in African fintech (SIM swap, account takeover, fake vendors) could poison trust in a new money-handling social app.
- App store dependence: Apple/Google policies limit what an in-app platform (mini-apps, payments) can do, and app-store fees cap the economics.

## Scope

**In scope:**
- **Channels:** one modular channel per user; opt-in modules (business, social; more later); channel profile, name, description, optional tags, and addressability
- **Messaging:** 1:1 and group text, image/video/file, hold-to-talk voice notes, voice/video calls, stickers
- **Social:** private friends feed (Moments-style), status, social posts as part of a social channel
- **Identity:** real-person profile, phone-based registration, contact graph, channel verification for merchants
- **Business module (full merchant toolkit):** product catalog, order inbox, inventory, delivery tracking, basic analytics, payment settlement — with customers as graph contacts, not a CRM list
- **Payments (on partner rails per market):** wallet, P2P transfers, QR payments, split bills, transaction history
- **Unified search:** one search box; intent-driven grouped results across business channels, social channels, people, and messages
- **Africa-first foundations:** multi-currency wallet abstraction, multi-language UI, cross-border channel discovery

**Out of scope (for now):**
- Full open marketplace with central searchable inventory and platform-driven fulfillment (Jumia-style) — channels are seller-owned; a central directory may come later
- Third-party mini-app platform (WeChat Mini Programs equivalent) — a later phase
- Government/city services integration — documented as a future expansion, not a launch commitment
- Enterprise suite (WeCom equivalent) for large organizations
- WeChat-style "Channels" short-video platform — the social feed comes first

**Explicit non-goals:**
- Never sell or broker user data as a revenue line
- No in-house payment licenses in version one — payments always ride licensed partner rails per market until there is a proven case to apply
- No surveillance or advertising-driven message scanning — only legal takedown/compliance obligations (per-jurisdiction, not a single pan-African standard)
- No open public chat rooms by default — the social graph stays private and relationship-based, like Moments rather than Twitter
- No customer CRM separation — buyers are graph contacts, not a segmented list

## Documentation

| Document | Purpose |
|---|---|
| [[user_personas]] | Who this product is for |
| [[branding]] | Brand identity, design system, experience tier, and target platform |
| [[features]] | What gets built, prioritized, with acceptance criteria |
| [[roadmap]] | When it gets built, in phases |
| [[architecture]] | How the system is structured |
| [[monetization]] | How it makes money |
| [[risk_log]] | What could go wrong and the plan for it |
| [[user_flow]] | How users move through the product |
| [[screens]] + `screens/` | Every screen, its states, and its components |
| [[schema]] | The data model |

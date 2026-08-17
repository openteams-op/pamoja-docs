## Screen 6: Wallet

**Route:** `/wallet`
**Platform:** Mobile
**Purpose:** The money surface — balance, funding, transfers, QR, and transaction history in one place.
**Entry Points:** Side Rail (Wallet); Transfer sheet / QR modal return.
**Exit Points:** `[[03-chat-thread|Chat Thread]]` (via transfer to a contact), `[[07-my-channel|My Channel]]` (merchant payment history context), Funding sheet, QR Scanner modal, Transaction detail sheet.

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area
- AppBar "Wallet" with "Fund" primary button
- Balance hero card: total balance in mono, per-currency breakdown (FEAT-014: NGN + corridor currencies when active)
- Quick action row: Send, Scan QR, Request, Fund — icon buttons with labels
- Transaction history section: list of Payment Receipt Cards (shared pattern) — sent, received, funded, order — filterable by type
- Empty state (no transactions): custom illustration "No activity yet" + "Send money" CTA
- Multi-currency banner (FEAT-014): shows current rates when more than one currency held

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Balance hero | Card | Mobile | Total + per-currency balance | GET wallet |
| Quick actions | Row of IconButton | Mobile | Send / Scan QR / Request / Fund | — |
| Request action | IconButton | Mobile | Send payment request (FEAT-013) | — |
| QR Scanner modal | Modal | Mobile | Scan merchant QR (per [[user_flow]] Flow 8) | — |
| Transfer sheet | Sheet | Mobile | P2P send | Wallet service |
| Funding sheet | Sheet | Mobile | Fund wallet (per [[user_flow]] Flow 9) | — |
| Transaction row | Card | Mobile | History entry (shared receipt pattern) | GET transactions |
| Transaction detail sheet | Sheet | Mobile | Full transaction + shareable receipt | GET transaction |
| Rate banner | Banner | Mobile | Multi-currency rates | GET rates |
| Empty illustration | Image (designer asset) | Mobile | No transactions | Static asset |

### Data Requirements

**Data Needed:**
- Wallet balances (per currency) — GET wallet
- Transaction history (paginated) — GET transactions
- Current conversion rates (multi-currency)
- KYC/funding method availability per market

**Data Flow:**
1. Screen mounts → balance skeleton → fetch balance + transactions in parallel
2. Quick actions open sheets/modals; results update balance and prepend history entries
3. QR scan → confirm amount → pay → success receipt → balance updates
4. Funding → partner handoff → on callback, reconcile balance
5. Offline → cached balance with stale note; actions blocked with "You're offline"

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Loading** | First fetch | Balance skeleton + skeleton rows |
| **Empty** | No transactions | Illustration + "No activity yet" + CTA |
| **Loaded** | Balance + history | Balance hero, quick actions, history |
| **Error** | Fetch failed | Error state + retry |
| **Offline** | No connectivity | Banner; actions disabled with clear message |
| **Pending** | Bank transfer funding | History shows pending entry until partner confirms |
| **Insufficient** | Send > balance | Transfer sheet blocks with top-up prompt |
| **Multi-currency** | >1 currency held | Rate banner visible |

**Edge Cases:**
- Unsupported corridor attempt (FEAT-014/015) → "not yet available" state, never a failed attempt
- Transaction ID too long to display → truncated mono with full value on tap
- Rapid double-tap on Send → disabled after first tap
- Currency conversion preview → rate + fee shown before confirm
- App lock enabled → wallet actions re-verify PIN/biometric
## Screen 8: Channel Profile

**Route:** `/channel/:id`
**Platform:** Mobile
**Purpose:** Any other user's channel, seen as they present it — one surface for identity, commerce, and social: About | Shop | Posts tabs.
**Entry Points:** `[[04-search|Search]]` (result tap), `[[05-feed|Feed]]` (post author), `[[02-chats|Chats]]` (contact row), `[[07-my-channel|My Channel]]` (Preview).
**Exit Points:** `[[03-chat-thread|Chat Thread]]` (Message action), Order composer sheet (Shop tab), Post detail (Posts tab).

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area
- Channel Header (shared pattern): avatar, name, verification badge, bio, status line, actions — Message, Browse Shop
- TabBar: About | Shop | Posts (tabs reflect the channel's active modules; hidden modules don't appear)
- **About tab:** full bio, tags, location (business), verification detail, joined/active signals
- **Shop tab (business module):** product grid (Product Cards); product tap → order/add-to-order; "out of stock" badges honored
- **Posts tab (social module):** the user's public-to-connections posts (same visibility rules as feed)
- A messaging-only channel shows only About + Message action

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Channel Header | Custom | Mobile | Identity + actions (shared pattern) | GET channel |
| TabBar | TabBar | Mobile | About / Shop / Posts (module-driven) | Derived from modules |
| Product Card | Card | Mobile | Catalog grid (shared pattern) | GET channel catalog |
| Post card | Card | Mobile | Author's posts (shared pattern) | GET channel posts |
| Message action | Button | Mobile | Start chat with this user | — |
| Order composer trigger | Button on product | Mobile | Add to order (per [[user_flow]] Flow 5) | Catalog data |
| Verification detail | Row | Mobile | Verified badge explanation | GET channel |

### Data Requirements

**Data Needed:**
- Channel profile (name, bio, avatar, status, modules, verification, location, tags)
- Catalog (when business module active)
- Posts visible to the viewer (when social module active)
- Viewer's relationship to this channel (connected / pending / none)

**Data Flow:**
1. Open channel → fetch profile + module presence
2. Fetch tab content lazily per module
3. Message action → opens chat thread (or connect-first prompt if not connected)
4. Product tap → order composer → order in chat (per [[user_flow]] Flow 5)
5. Offline → cached profile with stale note; actions gated

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Loading** | Profile fetch | Channel skeleton |
| **Loaded** | Profile + tabs | Full channel surface |
| **Error** | Fetch failed | Error state + retry |
| **Offline** | No connectivity | Banner; cached profile |
| **No modules** | Messaging-only channel | About + Message only |
| **Business only** | Business module only | About + Shop |
| **Social only** | Social module only | About + Posts |
| **Not connected** | Viewer not connected | "Connect" prompt before messaging |
| **Unverified** | No verification badge | No badge; no verification detail row |

**Edge Cases:**
- Channel with all modules disabled → About + Message only
- Deleted/blocked channel → clear "unavailable" state with block notice if applicable
- Very long bio → clamped with "see more"
- Product photo fails → placeholder with retry
- Viewer blocked by this user → channel shows blocked state, no actions
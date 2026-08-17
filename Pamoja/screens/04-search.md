## Screen 4: Search

**Route:** `/search`
**Platform:** Mobile
**Purpose:** The discovery layer — one search box, grouped intent-driven results across channels, people, and messages.
**Entry Points:** Side Rail (Search); deep link with query.
**Exit Points:** `[[08-channel-profile|Channel Profile]]` (tap channel/person), `[[03-chat-thread|Chat Thread]]` (tap message), `[[07-my-channel|My Channel]]` (own channel manage).

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area
- AppBar "Search" with prominent search field (autofocus on entry)
- Suggested chips row (only on empty query): trending categories (Fashion, Food, Electronics, Fabrics) with category artwork per [[branding]] Visual Asset Direction
- Body: grouped result sections — Business Channels, Social Channels, People, Messages — each a small header + result rows
- Result row (channel): avatar, name, verification badge, bio clamp, module tags; business rows show category glyph
- Result row (message): thread snippet + chat context
- Filters row (FEAT-024): Category, Location, Verified only, Price range — appears when business results exist
- Empty state: custom illustration + "Did you mean…" suggestions

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Search field | TextField | Mobile | Query entry | — |
| Category chips | Chip row | Mobile | Empty-query discovery | Static categories |
| Group headers | Section header | Mobile | Result grouping | Derived from results |
| Channel result row | ListView tile | Mobile | Channel result | GET search |
| Message result row | ListView tile | Mobile | Message result | GET search |
| Filter bar | Custom | Mobile | Business filters (FEAT-024) | — |
| Empty illustration | Image (designer asset) | Mobile | No results | Static asset |

### Data Requirements

**Data Needed:**
- Query → grouped, relevance-ranked results — GET search?q=
- Intent classification (commerce / social / identity) — server-side per [[architecture]] Search Service
- Filter state (category, location, verified, price)

**Data Flow:**
1. User types → debounce → results request
2. Server classifies intent and ranks across channel findability layers (Layer 0 + module signals)
3. Results render grouped; business results honor filters
4. Typing a new query replaces results; no stale result flashes (request token)
5. Offline → cached results with stale note

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Idle** | Empty query | Category chips + recent searches |
| **Loading** | Query submitted | Skeleton rows |
| **Loaded** | Results returned | Grouped sections + filters |
| **Empty** | No matches | Illustration + "Did you mean…" |
| **Error** | Request failed | Error state + retry |
| **Offline** | No connectivity | Banner; last cached results with stale note |
| **Filtered** | Filters applied | Results narrowed; filter chips visible and removable |

**Edge Cases:**
- Query with only spaces → treated as idle
- Very long query → allowed, clamped visually
- Rapid typing → debounced; only latest query renders
- Commerce intent with no business results → shows people/social results with a note "No shops found for that"
- Product-level match (FEAT-024) → tapping a product opens `[[08-channel-profile|Channel Profile]]` scrolled to that product
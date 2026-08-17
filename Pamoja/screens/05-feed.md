## Screen 5: Feed

**Route:** `/feed`
**Platform:** Mobile
**Purpose:** The social module's home — a private, connections-only feed of posts, with comments visible only to mutual connections.
**Entry Points:** Side Rail (Feed).
**Exit Points:** `[[08-channel-profile|Channel Profile]]` (tap post author), `[[03-chat-thread|Chat Thread]]` (message from post), Post Editor sheet (compose).

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area
- AppBar "Feed" with Compose button (or floating compose action above the list)
- Body: vertical feed of post cards
- Post card: author row (avatar, name, verified badge, timestamp), post content (text and/or photo), action row (Like, Comment, Share to chat), comment count
- Comments open inline (expanded section) or in a sheet; comments show mutual-connection visibility rules
- Empty state: custom illustration "Your feed is quiet" + "Invite contacts" CTA

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Post card | Card | Mobile | Post display (shared pattern) | GET feed |
| Author row | Row | Mobile | Post attribution + navigation (shared pattern) | User data |
| Post media | Image | Mobile | Photo/video in post | GET media |
| Like / Comment / Share | IconButton + TextButton | Mobile | Post actions | POST interactions |
| Comments section | Expandable / Sheet | Mobile | Mutual-visible comments | GET comments |
| Post Editor sheet | Sheet | Mobile | Compose (per [[user_flow]] Flow 10) | — |
| Empty illustration | Image (designer asset) | Mobile | Empty feed | Static asset |

### Data Requirements

**Data Needed:**
- Feed posts (connections only) — GET feed, paginated
- Post author identity (name, avatar, verified)
- Like/comment counts and viewer-eligible comment list

**Data Flow:**
1. Screen mounts → skeleton cards
2. Fetch feed, paginated, lazy-loaded
3. Interactions (like/comment) update optimistically, reconcile on ack
4. Publish from Post Editor → optimistic card at top → synced
5. Offline → queued posts show pending; feed shows cached with stale note

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Loading** | First fetch | Skeleton cards |
| **Empty** | No connection posts | Illustration + "Your feed is quiet" + invite CTA |
| **Loaded** | Posts fetched | Post cards |
| **Error** | Fetch failed | Error state + retry |
| **Offline** | No connectivity | Banner; cached feed with stale note |
| **Publishing** | Post submitted | Optimistic card with pending indicator |

**Edge Cases:**
- Post deleted by author → removed from feed for all viewers
- Comment from a non-mutual connection → hidden from viewer (server-enforced visibility)
- Very long captions → expandable "see more" clamp
- Multiple images → swipeable carousel within card
- Photos fail to load → placeholder with retry on the image only
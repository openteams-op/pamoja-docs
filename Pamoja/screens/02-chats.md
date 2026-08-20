## Screen 2: Chats

**Route:** `/chats`
**Platform:** Mobile
**Purpose:** The home rail destination — every conversation, connection prompt, and chat entry point.
**Entry Points:** Post-onboarding; Side Rail (Chats) from any in-frame screen.
**Exit Points:** `[[03-chat-thread|Chat Thread]]`, `[[04-search|Search]]`, `[[08-channel-profile|Channel Profile]]`, Settings (rail footer).

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area
- AppBar "Chats" with "+" (new chat) action
- Contact-sync prompt card (first-run only): "Connect your phone contacts" with illustration, Accept / Not now
- Body: vertical ListView of conversation rows
- Conversation row: avatar, name, last message preview (1-line clamp), timestamp, unread badge, presence dot
- Empty state: custom illustration "No chats yet" + "Invite contacts" CTA
- Bottom of list: contacts sheet entry ("See all contacts")

### Components

| Component           | Type                   | Platform | Purpose                         | Data Source         |
| ------------------- | ---------------------- | -------- | ------------------------------- | ------------------- |
| Side Rail           | NavigationRail         | Mobile   | Persistent frame navigation     | —                   |
| Contact-sync prompt | Card                   | Mobile   | First-run contact opt-in        | Local state         |
| Conversation row    | ListView tile          | Mobile   | Chat summary + unread           | GET conversations   |
| New chat            | IconButton             | Mobile   | Start new conversation / invite | —                   |
| Contacts sheet      | Sheet                  | Mobile   | Connect / invite contacts       | GET contact matches |
| Empty illustration  | Image (designer asset) | Mobile   | Empty state                     | Static asset        |

### Data Requirements

**Data Needed:**
- Conversation list (last message, unread count, participants, presence) — GET conversations
- Contact match results (People You Know) — after permission

**Data Flow:**
1. Screen mounts → loading skeleton rows
2. Fetch conversations + unread counts in parallel
3. On success → render rows, most recent first
4. On failure → error state with retry
5. First-run only: show contact-sync prompt; on opt-in, fetch matches

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Loading** | First fetch | Skeleton rows |
| **Empty** | No conversations | Custom illustration + "No chats yet" + "Invite contacts" |
| **Loaded** | Conversations fetched | Rows with previews, unread badges |
| **Error** | Fetch failed | Error state + retry |
| **Offline** | No connectivity | Offline banner; list shows cached rows with stale note |
| **Contacts prompt** | First run, no permission yet | Prompt card with illustration |

**Edge Cases:**
- Very long chat previews → clamp to 1 line with ellipsis
- New message while on the list → row updates live, unread badge increments
- Blocked contact's conversation → shows "Blocked" state; tapping opens the chat with a notice
- Deep link into a chat while unauthenticated → redirect to `[[01-onboarding|Onboarding]]`, return after OTP
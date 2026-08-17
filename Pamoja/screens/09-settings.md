## Screen 9: Settings

**Route:** `/settings`
**Platform:** Mobile
**Purpose:** Account, security, privacy, data, language, and app preferences — the rarely-visited, dense surface.
**Entry Points:** `[[07-my-channel|My Channel]]` (rail footer avatar), rail footer.
**Exit Points:** `[[07-my-channel|My Channel]]`, re-authentication flow, app lock setup.

### Layout

**Mobile layout:**
- In-frame: Side Rail + content area
- AppBar "Settings"
- Body: grouped ListView of settings sections
- **Account:** profile summary (avatar, name, phone), account details
- **Security:** App Lock (PIN + biometric toggle, per FEAT-028), wallet re-verification toggle, change PIN
- **Privacy:** contact sync permission, block list, privacy controls
- **Notifications:** per-category toggles (messages, orders, payments, promotions — per FEAT-032)
- **Data & Network:** Data-light mode toggle (FEAT-030), media auto-download preference, storage usage
- **Language:** language selector (FEAT-031), locale formatting
- **About:** terms, privacy notice (per-jurisdiction), version, support
- Log out (destructive, confirm dialog)

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Section groups | ListView sections | Mobile | Group related settings | — |
| App Lock toggle | Switch | Mobile | Enable PIN/biometric (FEAT-028) | Local + server |
| Wallet re-verify toggle | Switch | Mobile | Require re-verification for wallet | Local |
| Notification toggles | Switch | Mobile | Per-category preferences (FEAT-032) | GET/PATCH preferences |
| Contact sync control | Switch | Mobile | Contact permission opt-in/revoke (FEAT-003) | Local + server |
| Block list | ListView row | Mobile | Manage blocked contacts/channels (FEAT-029) | GET blocked list |
| Data-light toggle | Switch | Mobile | Data-saving mode (FEAT-030) | Local |
| Language selector | Dropdown | Mobile | Active locale (FEAT-031) | GET/PATCH locale |
| Log out | Button (destructive) | Mobile | End session | — |
| Confirm dialog | Modal | Mobile | Destructive confirmations | — |

### Data Requirements

**Data Needed:**
- Account info (name, phone, avatar)
- Notification preferences (FEAT-032)
- Contact permission state (FEAT-003)
- Blocked list (FEAT-029)
- Locale preference
- App lock state (local)

**Data Flow:**
1. Screen mounts → load preferences in parallel
2. Toggles update optimistically, sync to server (or local for device-only settings)
3. Language change → app relabels immediately; persisted
4. Log out → confirm → clear session → Onboarding
5. Offline → preferences cached; changes queue and sync on reconnect

### States

| State | Condition | What the User Sees |
|---|---|---|
| **Loading** | Preferences fetch | Skeleton rows |
| **Loaded** | Preferences available | Full grouped settings |
| **Error** | Fetch failed | Error state + retry |
| **Offline** | No connectivity | Banner; cached prefs, queued changes |
| **App Lock setup** | Enabling first time | PIN setup flow with confirm |
| **Log out** | User taps | Confirm dialog → Onboarding after confirm |

**Edge Cases:**
- Language switch mid-typing → current input preserved; labels update
- Data-light toggle change → applies immediately to media behavior
- PIN re-entry mismatch → inline error, retry
- App lock forgot PIN → recovery via re-auth (OTP) then reset
- Block list item → opens the blocked channel state
## Screen 1: Onboarding

**Route:** `/onboarding`
**Platform:** Mobile
**Purpose:** Create the account, verify the phone, build the channel, and choose modules — one flow, four steps.
**Entry Points:** App install; deep link when unauthenticated (per [[user_flow]] Authentication Gate).
**Exit Points:** `[[02-chats|Chats]]` (first rail destination).

### Layout

**Mobile layout:**
- Full-frame surface outside the Side Rail (the only screen not in the frame)
- Step indicator at top: Phone → OTP → Channel → Modules
- Each step is one full-height view; content is centered, generous spacing, one illustrated moment per step
- Phone step: brand mark + tagline "Together is everything", illustrated scene, phone input (large, mono, country-code prefixed), Continue button
- OTP step: same illustrated scene (smaller), 6-digit code input with auto-advance, "Resend code" with countdown
- Channel step: "Make it yours" — avatar picker, display name (required), bio (optional)
- Modules step: two rich option cards (Business, Social) with illustrations, "Both" and "Skip" affordances
- Illustrated moments per [[branding]] Visual Asset Direction (designer-created scenes)

### Components

| Component | Type | Platform | Purpose | Data Source |
|---|---|---|---|---|
| Step indicator | Custom | Mobile | Shows progress through the 4 steps | Local state |
| Phone input | TextField | Mobile | Phone number entry | User input |
| OTP input | TextField (6-digit) | Mobile | Verification code | User input |
| Avatar picker | IconButton + picker | Mobile | Channel avatar | User upload |
| Name field | TextField | Mobile | Channel display name (required) | User input |
| Bio field | TextField | Mobile | Channel bio (optional) | User input |
| Module cards | Card (selectable) | Mobile | Business / Social opt-in | User selection |
| Illustrations | Image (designer asset) | Mobile | One per step, brand style | Static assets |
| Continue / Skip | Button | Mobile | Progress or skip | — |

### Data Requirements

**Data Needed:**
- Phone number (user input) → POST registration, receive OTP
- OTP code (user input) → verify, get session
- Channel name/bio/avatar → create channel (Layer 0 findability)
- Module selection → activate modules

**Data Flow:**
1. Screen mounts → phone step
2. Submit phone → sending state → OTP step
3. Submit OTP → verifying → on success, channel step (new user) or straight to Chats (returning user)
4. Save channel → saving → modules step
5. Choose/skip modules → land on Chats

### States

| State                     | Condition                 | What the User Sees                                           |
| ------------------------- | ------------------------- | ------------------------------------------------------------ |
| **Phone step**            | Initial                   | Brand mark, illustration, phone input, Continue              |
| **OTP sending**           | Phone submitted           | Button spinner, resend countdown starts                      |
| **OTP error**             | Wrong/expired code        | Inline error, "Resend code" enabled                          |
| **Channel saving**        | Name/bio submitted        | Spinner; invalid → inline field errors                       |
| **Channel saved-minimal** | Backed out with name only | Proceeds; bio/avatar can be completed in `[[07-my-channel]]` |
| **Modules selected**      | Selection made            | Selected cards highlighted; Continue enabled                 |
| **Offline**               | No connectivity           | Offline banner; submission blocked with "You're offline"     |

**Edge Cases:**
- Returning user: OTP success → skip channel + modules → Chats directly
- OTP resend throttled after repeated failures
- Long display names → clamp at 2 lines with ellipsis
- Avatar upload fails → channel saves without avatar; retry later
- App killed mid-flow → resume at the last completed step on relaunch
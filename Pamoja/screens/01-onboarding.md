## Screen 1: Onboarding

**Route:** `/onboarding`
**Platform:** Mobile
**Purpose:** Splash screen, then create the account, verify the phone, build the channel, and choose modules — one flow, four steps.
**Entry Points:** App install; deep link when unauthenticated (per [[user_flow]] Authentication Gate).
**Exit Points:** `[[02-chats|Chats]]` (first rail destination).

### Layout

**Mobile layout:**
- Full-frame surface outside the Side Rail (the only screen not in the frame)
- Step indicator at top: Phone → OTP → Channel → Modules; stays fixed/sticky at the top while the step content scrolls
- Each step is one full-height view; content is centered, generous spacing; illustrations appear only where noted below
- Splash: Pamoja logo/emblem centered in the screen; tagline "Together is everything" as a small caption lifted just above the bottom
- Phone step: "Enter your phone number" heading with the helper line "We'll text you a code to verify it's you.", illustrated scene, phone input (large, mono, country-code prefixed), Continue button
- OTP step: same illustrated scene (smaller), 6-digit code input with auto-advance (cells active only on focus), "Resend code" button, Continue button; helper text masks the phone number in the middle (e.g. +234 80****0000)
- Channel step: "Make it yours" — avatar picker, display name (required), bio (optional). No illustrated scene — avatar + fields only
- Modules step: selectable module cards (Business, Social), each with an icon, module title, a checkbox, and a short description of what the module is about; "Select all modules" convenience checkbox; hint copy "Pick at least one module to continue. You can change this later."
- Steps 2–4 (OTP, Channel, Modules) each show a back button in an appbar pinned close to the top, with the step progress bar below it; both the appbar and the progress bar stay sticky at the top while the step content scrolls; Phone step and Splash have no back button
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
| Module cards | Card (selectable) | Mobile | Business / Social opt-in; "Select all modules" checkbox | User selection |
| Illustrations | Image (designer asset) | Mobile | Phone step scene only; brand style | Static assets |
| Continue | Button | Mobile | Progress to next step | — |

### Data Requirements

**Data Needed:**
- Phone number (user input) → POST registration, receive OTP
- OTP code (user input) → verify, get session
- Channel name/bio/avatar → create channel (Layer 0 findability)
- Module selection → activate modules

**Data Flow:**
1. Screen opens → splash → then phone step
2. Submit phone → OTP step
3. Submit OTP → verifying → on success, channel step (new user) or straight to Chats (returning user)
4. Save channel → saving → modules step
5. Choose at least one module (or select all) → land on Chats

**Back navigation:** OTP back returns to the Phone step; Channel back returns to OTP; Modules back returns to Channel.

### States

| State                     | Condition                 | What the User Sees                                           |
| ------------------------- | ------------------------- | ------------------------------------------------------------ |
| **Phone step**            | Initial                   | Illustration, phone input, Continue                          |
| **OTP**                   | Code entry                | 6-digit code input (active on focus), masked phone number (+234 80****0000), Resend code, Continue |
| **Channel**               | Loaded                    | Avatar picker, display name, bio, Save (enabled)             |
| **Modules**               | Selection in progress (default) | Module cards (icon + title + checkbox + short description), "Select all modules" checkbox toggles all, Continue |
| **Offline**               | No connectivity           | Offline banner; Continue button shown but disabled           |

**Edge Cases:**
- Returning user: OTP success → skip channel + modules → Chats directly
- OTP resend throttled after repeated failures
- Long display names → clamp at 2 lines with ellipsis
- Avatar upload fails → channel saves without avatar; retry later
- App killed mid-flow → resume at the last completed step on relaunch
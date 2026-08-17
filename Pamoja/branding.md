# Brand Identity

**Product Name:** Pamoja
**Experience Tier:** `Standard` — utility-first super app, executed with Discord-grade craft. Motion serves clarity; the design system is dense, dark-first, and precise. Sections 5-8 (Creative Direction, Motion Design, Asset Style Guide, Spatial & Sound) are intentionally absent.
**Target Platform:** `Mobile (iOS + Android)` — phone-first for Nigeria/Africa: low-data Android and iOS, push notifications, mobile payments, QR. Desktop/web is a companion surface later, never the primary.
**Tagline:** Together is everything.
**Brand Personality:** Warm, confident, trustworthy, crafted, African-modern.
**Tone of Voice:** Friendly and direct, plain-language, warm but professional. Pamoja handles money and relationships — the tone earns trust through clarity, never through hype or slang; it lets the African identity show through warmth and color, not caricature.

## Logo & Iconography

**Logo Concept:** A combination mark — a circular knot of two interlocking rounded shapes forming a "P" (the joining of two people = *together*), set beside a wordmark in a geometric sans. The knot reads at app-icon size.
**Logo Usage:** App icon (dark rounded-square tile with the gold knot), in-app splash and empty states, merchant channel badges, payment confirmation header.
**Icon Style:** Filled, rounded terminals, consistent 2px effective stroke on the outline variants; stroke joins rounded. Icons feel solid and warm, never hairline-fragile — Discord-weight, not Figma-weight.
**Icon Library:** Phosphor (duotone-capable, consistent stroke family across both OSes).

# Design System

## Color Palette

Dark-first with warm undertones: surfaces are black-brown (not blue-black), and gold carries the brand. Every token carries a light and a dark value; the theme layer picks the column.

### Primary Colors
| Token | Light | Dark | Usage |
|---|---|---|---|
| `primary` | `#A16207` | `#FBBF24` | Primary buttons, links, active states — the brand gold |
| `primary-hover` | `#854D0E` | `#FCD34D` | Button hover / pressed state |
| `primary-light` | `#FEF3C7` | `#422006` | Selected backgrounds, badges, active-channel tint |

### Neutral Colors
| Token | Light | Dark | Usage |
|---|---|---|---|
| `surface` | `#FAF9F7` | `#1C1917` | Page background (warm near-black in dark mode) |
| `surface-secondary` | `#F5F4F2` | `#292524` | Inputs, channel rails, secondary surfaces |
| `surface-elevated` | `#FFFFFF` | `#332E2A` | Cards, chat bubbles, modals, popovers — one step above `surface-secondary` |
| `text-primary` | `#1C1917` | `#FAFAF9` | Headings, body text |
| `text-secondary` | `#57534E` | `#A8A29E` | Captions, helper text, timestamps, unread-notification labels |
| `text-muted` | `#8B857F` | `#79716B` | Placeholders, disabled text, secondary meta |
| `border` | `#E7E5E4` | `#44403C` | Dividers, input borders, card borders |

### Semantic Colors
| Token | Light | Dark | Usage |
|---|---|---|---|
| `success` | `#15803D` | `#4ADE80` | Success messages, payment confirmations — deep green echoes the Nigerian flag's green |
| `warning` | `#C2410C` | `#FB923C` | Warnings, caution states (orange, distinct from brand gold) |
| `error` | `#B91C1C` | `#F87171` | Error messages, destructive actions |
| `info` | `#0F766E` | `#2DD4BF` | Informational alerts, tips — teal, an African-jewel tone |

### Creative Color *(not applicable — Standard tier)*
Intentionally omitted. The palette above is the complete color system.

## Typography

### Font Family
| Role | Font | Fallback |
|---|---|---|
| Display / Headings | `Space Grotesk` | `sans-serif` |
| Body | `Inter` | `sans-serif` |
| Monospace | `JetBrains Mono` | `monospace` |

Space Grotesk gives the headings a crafted, modern edge that pairs with gold on near-black; Inter keeps body text dense and legible for long chat and catalog reading; JetBrains Mono is reserved for amounts, balances, and transaction IDs.

### Type Scale
| Token | Size | Weight | Line Height | Usage |
|---|---|---|---|---|
| `display` | 34px | 700 | 1.2 | Splash, onboarding hero, payment success |
| `h1` | 28px | 700 | 1.3 | Screen titles |
| `h2` | 22px | 600 | 1.35 | Section headings |
| `h3` | 18px | 600 | 1.4 | Card titles, channel names |
| `body-large` | 17px | 400 | 1.5 | Chat previews, lead paragraphs |
| `body` | 16px | 400 | 1.5 | Body text, form labels |
| `body-small` | 14px | 400 | 1.5 | Captions, timestamps, meta |
| `caption` | 12px | 500 | 1.4 | Badges, overlines, tab labels |

## Spacing

4px base grid. All spacing values are multiples of 4.

| Token | Value | Usage |
|---|---|---|
| `space-xs` | 4px | Icon-to-label gaps, inline badges |
| `space-sm` | 8px | Compact — between related items, input inner padding |
| `space-md` | 16px | Default — card padding, list gaps |
| `space-lg` | 24px | Generous — between sections, dialog padding |
| `space-xl` | 32px | Screen margins, hero padding |
| `space-2xl` | 48px | Major separation between unrelated sections |
| `space-3xl` | 64px | Layout-level separation, bottom sheets |

## Sizing

| Token | Value | Usage |
|---|---|---|
| `radius-sm` | 6px | Tags, small inputs |
| `radius-md` | 10px | Buttons, inputs, cards |
| `radius-lg` | 16px | Modals, sheets, chat bubbles |
| `radius-full` | 9999px | Pills, avatars, badges |
| `button-height` | 48px | Minimum touch target for primary actions (mobile) |
| `input-height` | 48px | Text inputs, selects |
| `icon-sm` | 16px | Inline icons, status indicators |
| `icon-md` | 24px | Navigation icons, button icons |
| `icon-lg` | 32px | Feature icons, empty-state illustrations |

## Shadows

Dark mode needs deeper opacity and a subtle light border to read as elevation on warm-black surfaces.

| Token | Light | Dark | Usage |
|---|---|---|---|
| `shadow-none` | `none` | `none` | Flat surfaces |
| `shadow-sm` | `0 1px 2px rgba(28,25,23,0.06)` | `0 1px 2px rgba(0,0,0,0.4)` | Subtle lift — cards on the base surface |
| `shadow-md` | `0 4px 8px rgba(28,25,23,0.08)` | `0 4px 8px rgba(0,0,0,0.5)` | Elevated — bottom sheets, menus |
| `shadow-lg` | `0 12px 28px rgba(28,25,23,0.12)` | `0 12px 32px rgba(0,0,0,0.7)` | Highest — modals, payment confirmations |

Elevated surfaces in dark mode additionally use a 1px `border` (token `border`) on the top edge so depth is visible even on black screens.

## Component Tokens

### Buttons
| Variant | Background | Text | Border | Radius | Height | Padding |
|---|---|---|---|---|---|---|
| Primary (light) | `primary` | `#FFFFFF` | none | `radius-md` | `button-height` | 16px 24px |
| Primary (dark) | `primary` | `#1C1917` | none | `radius-md` | `button-height` | 16px 24px |
| Secondary | `primary-light` | `primary` | none | `radius-md` | `button-height` | 16px 24px |
| Outline | transparent | `text-primary` | 1.5px `primary` | `radius-md` | `button-height` | 16px 24px |
| Ghost | transparent | `text-primary` | none | `radius-md` | `button-height` | 16px 24px |
| Destructive | `error` | `#FFFFFF` | none | `radius-md` | `button-height` | 16px 24px |

**Note:** In dark mode the gold `primary` button uses near-black text (`#1C1917`) to hold WCAG AA contrast — white on `#FBBF24` fails. This is a deliberate Discord-style choice: luminous accent buttons carry dark text.

### Inputs
| State | Border | Background | Text |
|---|---|---|---|
| Default | `border` | `surface-secondary` | `text-primary` |
| Focus | `primary` | `surface` | `text-primary` |
| Error | `error` | `surface` | `text-primary` |
| Disabled | `border` | `surface-secondary` | `text-muted` |

### Chat & Channel Components *(Discord-grade behavior)*
| Component | Spec |
|---|---|
| Channel row (active) | Background `primary-light`, left indicator 2px `primary` |
| Channel row (hover) | Background `surface-secondary` |
| Unread badge | Background `primary`, text `#1C1917` (dark) / `#FFFFFF` (light), `radius-full`, min-width 18px |
| Message bubble | Background `surface-elevated`, radius `radius-lg`, shadow `shadow-sm` |
| Message (own) | Background `primary-light`, text `text-primary` |
| Online presence dot | 12px `success` ring with `surface` outline |
| Verified merchant badge | Gold check glyph in `primary` on `surface-elevated`, radius `radius-full` |
| Side rail (active) | Background `primary-light`, left indicator bar 3px `primary`, icon `primary`, label `text-primary` (label shown when rail is expanded) |
| Side rail (icon-only) | Icon `text-secondary`, 56px-wide rail, center-aligned icons, label hidden on narrow phones |
| Side rail (hover) | Icon `text-primary`, background `surface-secondary` on the item row |
| Side rail (unread) | 10px dot `primary` at the item's top-right, plus unread count badge `radius-full` for Chats |

### Motion (Standard tier — clarity only)
- **Duration:** micro-interactions 100–200ms; sheet and modal transitions 250–300ms. No ambient loops, no parallax, no scroll-driven animation.
- **Easing:** `ease-out` (material default) for entries; `ease-in-out` for shared elements. One language, applied consistently.
- **Motion rule:** motion exists to explain state (button press, sheet slide, order status), never to decorate. Respect the OS reduce-motion setting; fall back to instant state changes.

## Accessibility

- **Contrast ratios:** All text meets WCAG AA (4.5:1 normal, 3:1 large). Dark-mode gold buttons use dark text (see Buttons above) because white on gold fails.
- **Touch targets:** All interactive elements minimum 48x48px (mobile), with 8px gaps between adjacent targets.
- **Focus indicators:** Visible 2px `primary` outline with 2px offset on all interactive elements for keyboard/accessibility navigation.
- **Color independence:** Color is never the only signal. Order status pairs color with a label and icon (e.g., "Delivered" + check + `success` green). Payment success pairs a check glyph with the color, never color alone.
- **Screen reader support:** All images carry alt text (product photos, avatars, chat images). All inputs have labels. Chat actions announce via accessibility announcements; payment confirmations use live-region announcements.
- **Dynamic type / font scaling:** Layout tolerates up to 200% font scaling; chat and catalog text never clip at system accessibility text sizes.
- **Dark mode is the brand default** on both platforms, tied to the system setting; light mode remains fully supported and contrast-verified.

## Visual Asset Direction

Pamoja's UI is **rich by design**: custom, designer-crafted illustration and imagery carry the brand's warmth and African-modern identity throughout the experience. A human designer sources and creates these assets against this brief — see `cross-platform-asset-pipeline` for per-asset sourcing rules.

**Style:** African-modern, warm and crafted — never generic stock, never flat corporate clip-art. Illustrations feel hand-made, with organic shapes and a human touch, set against the warm dark surfaces of the palette.

**Palette discipline:** Assets live inside the palette above — gold `primary`, deep warm browns (`surface`, `surface-secondary`), terracotta and teal accents. Illustrations read at home on dark surfaces; never introduce colors outside the palette unless a specific photograph demands it.

**Usage:**
- **Onboarding:** rich illustrated scenes (people, markets, phones) that tell the "together" story — one per onboarding step
- **Empty states:** every empty surface (no chats, no orders, no products, no search results) gets a custom illustration, not an icon
- **Category artwork:** product categories (fashion, food, electronics, fabrics) get small illustrated glyphs/patterns for the catalog and search filters
- **Success/celebration:** payment success and connection moments use warm celebratory illustrations or patterns (e.g., Adinkra-inspired geometric accents)
- **Photography:** where real photos are used (product shots, merchant profiles), direction is warm, natural light, editorial but accessible — never harsh studio glamour

**Iconography:** continues from the icon style above (Phosphor, filled, rounded); illustrations are a layer above icons, never a replacement for them.

**Tone guardrail:** rich ≠ busy. One illustrated moment per surface, quiet spacing elsewhere — the warmth comes from craft, not density.

# Cross-Document Links

- Design tokens defined here (`primary`, `surface`, `surface-elevated`, `text-primary`, `text-secondary`, `text-muted`, `border`, `success`, `warning`, `error`, `info`, spacing, radius, shadow tokens) are referenced by [[screens]] and `screens/` component definitions.
- The Visual Asset Direction above is the brief `screens/` and `cross-platform-asset-pipeline` apply per screen — never re-derived.
- The Africa-first identity and the merchant wedge come from [[README]]; personas and their tech-comfort levels (Ada: Low–Medium, Chidi/Tunde: High) come from [[user_personas]] and shape where onboarding depth and dense UI apply.
- `architecture.md` will restate the `Target Platform` — it never re-decides it.

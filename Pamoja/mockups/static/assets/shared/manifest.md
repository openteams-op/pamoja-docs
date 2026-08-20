# Shared Assets — Manifest

Product: **Pamoja** · Standard tier · Target platform: **Mobile (iOS + Android)**

Shared slots are assets reused across multiple screens. In this build pass (screen 01 · Onboarding
only), **no shared asset slots are required**:

- The **brand knot logo** is a custom brand icon and is authored as an inline SVG (per the
  mockup-builder skill: custom/brand icons are hand-authored, never generated as image files).
- **Avatars** and other representative/test filler media use public CDN sources (randomuser,
  dicebear, picsum) and are flagged `<!-- test data -->` in templates — they are test data, not
  asset slots.

When future screens (Chats, Feed, Wallet, My Channel, …) are built, their shared slots (e.g.
category artwork glyphs, empty-state scenes reused across surfaces, celebratory payment patterns)
will be listed here with model-ready prompts, per `branding.md` Visual Asset Direction.

| Screen | Slot | File path | Type | Aspect/Res | Generation prompt | Status |
|---|---|---|---|---|---|---|
| — | *(none in this pass)* | — | — | — | — | — |
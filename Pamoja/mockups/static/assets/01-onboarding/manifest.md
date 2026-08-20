# Screen 01 · Onboarding — Asset Manifest

Product: **Pamoja** · Standard tier · Target platform: **Mobile (iOS + Android)**

These are the **real asset slots** for this screen (designer-created illustrations per the
`branding.md` Visual Asset Direction: *African-modern, warm and crafted, one illustrated moment per
step, assets live inside the palette*). Icons (Phosphor) and the brand knot logo (inline SVG) are
not asset slots.

**Tool landscape (verified July 2026, live search):** FLUX 2 Pro and Midjourney v7 are the current
front-runners for sharp, consistent editorial/brand illustration; Recraft V4 is the vector/flat
alternative. Prompts below are deliberately **tool-agnostic** — run each through any image-generation
model or platform you prefer and drop the file into the listed path. The template already expects
these paths (`img_asset` shows a branded placeholder until the file lands).

| Screen        | Slot                         | File path                                  | Type         | Aspect/Res      | Generation prompt                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Status  |
| ------------- | ---------------------------- | ------------------------------------------ | ------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| 01-onboarding | Phone step illustration      | `assets/01-onboarding/step-phone.png`      | Illustration | 1:1 / 1024×1024 | Flat vector illustration, square 1:1. Two friends meeting at a busy open-air West African market stall: warm smiling faces, one holds a phone showing a chat bubble, baskets of fruit and colorful fabric rolls behind them, a small shopfront awning. Warm near-black background #1C1917, gold #FBBF24 accents, terracotta #C2410C awning, teal #0F766E fabric details. Organic rounded shapes, soft shadows, gentle highlights, calm generous negative space, African-modern aesthetic, warm and crafted. No text, no letters, no logo, no watermark, no UI. Clean edges, suited to a dark UI. | Pending |

Notes:

- **OTP step** reuses the Phone step illustration at a smaller size per `01-onboarding.md` layout
  ("same illustrated scene (smaller)") — no separate OTP asset slot.
- **Channel step no longer uses an illustration** (current design: "Make it yours" + avatar picker +
  fields only) — the `step-channel.png` slot was removed from the template.
- **Module cards no longer use illustrations** — redesigned to icon + module title + checkbox +
  short description (design change). The `module-business.png` and `module-social.png` slots were
  removed from the template and manifest.
- Avatar picker preview is **test data** (public CDN avatar), flagged `<!-- test data -->` in the
  template — not a real asset slot (user uploads their own avatar at runtime).
- No shared asset slots exist yet; see `static/assets/shared/manifest.md`.
# Pamoja — Mockups

Browsable review mockups as a Flask + Jinja2 app: one shared base layout with reusable macros and
partials, and one template per screen. Click through them and critique — there is no product
backend, API, or data wiring.

## Run

```sh
cd mockups
pip install -r requirements.txt
flask --app app run --debug
```

Open `http://127.0.0.1:5000/` (the gallery) and click a frame.

## Requirements

- `requirements.txt` declares the dependencies — `flask` only (Tailwind, fonts, icons, and Mermaid
  all load from CDN). Install with `pip install -r requirements.txt`.
- No virtualenv is created here and no dependencies are vendored — this folder is a plain source
  folder, clean to commit.

## Repo hygiene (for whoever owns the repository)

Running the app produces `__pycache__/` bytecode folders under `mockups/`. Add this to the
repository's `.gitignore` so the mockups folder stays clean to commit:

```
__pycache__/
```

## Assets

Every screen folder has its own `static/assets/<NN-screen-name>/manifest.md` listing that screen's
asset slots with its generation prompt and the path the templates expect. `static/assets/shared/manifest.md`
lists the shared slots. Drop generated files into the listed paths and they are picked up with no
code change. Representative/test filler media (avatars, sample photos/video/audio) uses public CDN
sources and is flagged `<!-- test data -->` in the templates.

## Screens built in this pass

- `01-onboarding` — `/onboarding` (Mobile). Onboarding is the only screen outside the Side Rail
  frame; the four-step flow renders each step plus its states as `[data-state]` siblings.
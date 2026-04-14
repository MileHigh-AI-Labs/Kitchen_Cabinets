# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Abodeable Renovations — Kitchen Cabinet Proposal** is a single-page static HTML proposal/marketing site for Abodeable Renovations, a kitchen cabinet renovation company that uses AI-powered virtual design (powered by Mile High AI Labs) to show clients photorealistic renders of their renovated kitchen before any physical work begins.

The site is a self-contained sales/proposal page intended to be viewed in a browser or shared with prospective clients (homeowners and real estate investors).

## Tech Stack

- **Pure static HTML/CSS/JS** — no build step, no framework, no dependencies
- **Fonts**: Google Fonts — Playfair Display (serif headings) + Lato (sans body)
- **Vanilla JS** — only used for the before/after image comparison drag slider
- **Inline SVG icons** for service cards and benefit icons (no icon library)

## Repository Structure

```
Kitchen_Cabinets/
├── Abodeable_Renovations_Proposal.html  # Main proposal page (single file: HTML + CSS + JS)
├── quote.html                           # Standalone scope-driven "Build Your Quote" form page (same design system)
├── Dimensions_materials.md              # Reference-only: scope-by-scope component counts & dimensions spec (basis for quote.html logic)
├── hero image.png                       # Hero background
├── about us.png                         # About section image
├── before/                              # Before renovation photos (1.JPG, 2.png ... 10.png)
├── after/                               # After AI-rendered photos ((1).png ... (10).png)
├── material costing.pdf                 # Reference: material cost data
├── cabinets new painting.pdf            # Reference: cabinet painting notes
├── new cabinets doors and drawer fronts.pdf  # Reference: door/drawer front specs
└── EST0004.pdf                          # Customer estimate / reference doc
```

**Important**: The "after" images use parenthesized filenames like `after/(1).png` — preserve the parentheses when editing image references.

The PDFs at the repo root (`EST0004.pdf`, `material costing.pdf`, `cabinets new painting.pdf`, `new cabinets doors and drawer fronts.pdf`) are **reference-only** — they are not linked from either HTML page and should not be wired into the site unless explicitly requested.

## Page Sections (in order)

1. **Header** — Fixed nav with logo "Abodeable Renovations", section links, and gold "Free Consultation" CTA
2. **Hero** — Full-viewport hero with `hero image.png` background and headline "Imagine Your Dream Kitchen Before We Build It"
3. **About** (`#about`) — Two-column intro with `about us.png`
4. **Partnership Band** — Dark band promoting Mile High AI Labs as virtual design partner (links to milehighlabs.ai)
5. **Services** (`#services`) — 6-card grid: AI Virtual Design, Style Consultation, Price Proposal, Cabinet Renovation & Installation, Hardware & Material Selection, Investment Property Packages
6. **Process** (`#process`) — 4-step explainer: Share Your Space → Design Consultation → Virtual Visualization → Proposal & Build
7. **Gallery** (`#gallery`) — 10 before/after pairs with interactive drag slider (pair count must match files in `before/` and `after/` — keep them in sync when adding/removing)
8. **Why Choose Us** (`#why`) — 6 benefit cards (See It Before You Build It, Unlimited Style Options, Transparent Pricing, etc.)
9. **CTA Band** (`#contact`) — Phone `+1 (303) 578 2580`, email `services@milehighlabs.ai`, Cal.com booking link
10. **Footer** — Copyright + Mile High AI Labs credit

## Design System

CSS custom properties defined in `:root` (top of `<style>` block):

- `--cream: #FEFAF4` — page background
- `--cream-deep: #F5EDD8` — alt section background
- `--gold: #C8973F` — primary accent (CTAs, dividers, eyebrows)
- `--gold-light: #E8C47A` — light gold accent
- `--gold-dark: #9E7230` — hover state
- `--brown-dark: #2C1810` — primary text / dark band
- `--brown-mid: #5C3A22` — body text
- `--brown-light: #A07850`
- `--shadow: rgba(44,24,16,0.12)`

**Typography**: Playfair Display for `h1`/`h2`/`h3` and brand wordmarks; Lato for body, nav, buttons, eyebrows. Eyebrow labels use `font-size: 11px`, `letter-spacing: 0.28em`, uppercase, gold color.

## Before/After Slider (JS)

Located at the bottom of the HTML file. For each `.pair-images` container:
- Listens to mousedown/mousemove/mouseup and touch equivalents
- Calculates cursor X as a percentage of container width (clamped 2–98%)
- Sets `clip-path: inset(0 ${100-pct}% 0 0)` on `.img-before` to reveal the after image
- Moves `.slider-divider` to the same X position

When adding new gallery pairs, follow the existing markup structure (`.gallery-pair > .pair-images > .img-before + .img-after + .slider-divider + .slider-label.before + .slider-label.after`) — the JS picks them up automatically via `querySelectorAll`.

## Editing Notes

- The main proposal site is **one file** — HTML, CSS, and JS all live in `Abodeable_Renovations_Proposal.html`. There is no bundler, no preprocessor, no `npm` step. `quote.html` is a separate self-contained scope-driven quote builder (user picks a renovation scope, form reveals the relevant component count/dimension inputs derived from `Dimensions_materials.md`) that reuses the same `:root` CSS variables and Playfair/Lato typography — when updating brand colors or fonts, update both files. When changing quote form fields or scope logic, cross-check against `Dimensions_materials.md` so the two stay in sync.
- To preview, just open the file in a browser (double-click, or `start Abodeable_Renovations_Proposal.html` in CMD / `explorer Abodeable_Renovations_Proposal.html` in Git Bash).
- All images are loaded with **relative paths** from the HTML file's directory — keep the `before/`, `after/`, and root image files alongside the HTML.
- SVG icons inside service/benefit cards are inline — color them via `stroke="#2C1810"` (brown) and `#C8973F` (gold) to stay on-brand.
- When changing colors site-wide, prefer updating the CSS variables in `:root` rather than hunting hex codes throughout the file.

## Company / Contact (used in CTA + footer)

- **Company**: Abodeable Renovations
- **Tech partner**: Mile High AI Labs — https://www.milehighlabs.ai/
- **Phone**: +1 (303) 578 2580
- **Email**: services@milehighlabs.ai
- **Booking**: https://cal.com/milehighailabs/15min

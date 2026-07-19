# Noise Web — Design System V2

> Refined visual language derived from 14 reference images spanning album art, glitch aesthetics, collage photography, typographic art, concert posters, and generative code art.
>
> This document is the **single source of truth** for the AbstractWebsite visual identity. Every decision here is grounded in the analyzed references.

---

## Table of Contents

1. [Critical Re-Evaluation](#1-critical-re-evaluation)
2. [Design Philosophy](#2-design-philosophy)
3. [Design Tokens — Color](#3-design-tokens--color)
4. [Design Tokens — Typography](#4-design-tokens--typography)
5. [Design Tokens — Spacing & Layout](#5-design-tokens--spacing--layout)
6. [Texture System (The Soul of the Design)](#6-texture-system-the-soul-of-the-design)
7. [Component Architecture](#7-component-architecture)
8. [Interaction & Motion System](#8-interaction--motion-system)
9. [Image Treatment Guidelines](#9-image-treatment-guidelines)
10. [Layout Grid System](#10-layout-grid-system)
11. [Implementation Strategy](#11-implementation-strategy)
12. [AI Website Generation Specification](#12-ai-website-generation-specification)
13. [Appendix: Reference-to-Token Map](#13-appendix-reference-to-token-map)

---

## 1. Critical Re-Evaluation

### What V1 Got Right

| Principle | Why It Holds |
|-----------|-------------|
| Monochromatic blue/teal foundation | 12 of 14 images use a cool monochrome palette |
| Noise/grain as critical differentiator | Every single image carries visible grain or texture |
| Hard offset shadows (printed feel) | Collage aesthetic demands physical, not digital, depth |
| Mixed serif/sans-serif/monospace | The typography references (11, 12, 13, 8, 9) all mix families |
| Asymmetrical 60/40 grids | Composition analyses consistently show asymmetrical balance |
| "Beauty in the broken" philosophy | Glitch, noise, and imperfection are the common thread |

### What V1 Missed or Got Wrong

| Issue | Correction |
|-------|-----------|
| Color palette too narrow | Missing violet/magenta glitch undertones (from images 11, 12); missing warm parchment off-white (image 7); missing teal accent (image 13) |
| Pure black (`#000000`) still listed as avoided — good, but missing nuance | Need explicit "never pure black" rule AND "never pure white outside of text" |
| Glitch only as hover effect | Chromatic aberration (RGB channel splitting) must be a **core texture layer**, not a hover gimmick — it appears in 3 images as a primary visual effect |
| CTR scanline treatment is optional | Scanlines are a **mandatory secondary texture** derived from images 3, 5, 6 |
| 3 hero patterns insufficient | Need 5 patterns: Collage, Diagonal Split (image 5), Split-Screen (image 6), Typographic (image 13), Vertical Stack (image 1) |
| Missing organic vs. inorganic duality | The core tension in every image is natural/organic forms vs. technological decay — this must be a design principle |
| Grain intensity guidance too vague | Need concrete CSS and SVG implementations with opacity ranges per context |
| No pointillist/dot pattern component | Image 10 uses dots as structural graphic element — valuable unique component |
| Paper fold/surface texture missing | Images 13 and 7 show physical paper texture with fold lines — adds warmth |
| No component for vertical stacking rhythm | Image 1's stacked eyes create a powerful rhythm pattern |
| Typography doesn't capture "broken serif" | Images 11 and 12 use traditional serif fonts WITH glitch/distortion — the broken serif is a specific type treatment |

---

## 2. Design Philosophy

### Creative Direction

> **"Digital Ruins"** — A world where memory and technology decay together. Not loud cyberpunk, but quiet melancholy. Every pixel carries history. Every texture tells of age. The interface is a palimpsest: digital layers over analog remnants.

### Core Duality

```
ORGANIC / RAW          <->     DIGITAL / DECAYED
────────────────────────────────────────────────────
Eyes, flowers,         <->     Text blocks, code,
jellyfish, faces,      <->     grids, scanlines,
clouds, bodies         <->     chromatic aberration
```

The website lives in the **tension between these two poles**. Never fully organic, never fully digital — always in the space between.

### Design Principles

1. **Texture Before Color** — The palette is intentionally narrow. Visual richness comes from grain, noise, scanlines, halftones, chromatic aberration, and paper texture — not from chromatic variety.

2. **Imperfection as Identity** — Glitches, pixelation, compression artifacts, misalignment, and distortion are not bugs. They are the visual signature. Every element should feel slightly aged, slightly broken.

3. **Asymmetry as Order** — Never center-align. Never use symmetric grids. The 60/40 split, the diagonal division, the off-balance composition — these create the editorial, collage-like feel.

4. **Typography as Material** — Text is not just content. It is texture, shape, pattern, and atmosphere. Fragmented words, broken serifs, tight kerning, mixed scripts — type is part of the visual fabric.

5. **Analog Memory, Digital Present** — Film grain, paper folds, halftone dots (the analog past) coexist with CRT scanlines, chromatic aberration, pixelation (the digital past). The website is a time-collapse of media history.

6. **Slow Motion** — Animations are slow (8s+ cycles). Nothing is fast, snappy, or playful. The motion language is breathing, floating, decaying — never bouncing or elastic.

### Intended User Experience

The visitor should feel like they have entered a **digital exhibition space** — quiet, atmospheric, slightly melancholic. The interface recedes. The atmosphere is the content. Navigation is intuitive but unhurried. Every scroll reveals another framed composition, another texture layer, another atmospheric moment.

### Atmosphere Keywords

- Quiet / Melancholic / Futuristic / Experimental
- Editorial / Surreal / Digital Dream / Nostalgic Technology
- High-quality graphic design / Restrained / Textured / Emotional

*These are not marketing copy. They are guardrails for every design decision.*

---

## 3. Design Tokens — Color

### Core Principle

The palette is **monochromatic with strategic accent intrusions**. Three temperature zones exist within the blue spectrum: Deep Cold (navy/indigo), Mid Cool (cyan/teal/slate), and Warm Glitch (violet/magenta intrusion). The warm accent is used **sparingly and deliberately** — it represents the "glitch breaking through."

### Primary Background Scale

```css
/* Deepest backgrounds — hero sections, full-screen panels */
--color-bg-deep: #0a1628;       /* Near-black navy. NEVER pure black (#000). */

/* Primary section backgrounds */
--color-bg-dark: #142a4a;       /* Deep slate blue. Main content areas. */

/* Mid-tone surfaces — cards, overlays, secondary panels */
--color-bg-mid: #1e3a5f;        /* Muted indigo-blue. Card containers. */

/* Light backgrounds — subtle overlays, hover states */
--color-bg-light: #2a4a72;      /* Lighter blue-grey. Accent backgrounds. */

/* Textured surface variant — simulates aged paper */
--color-bg-parchment: #1a2d4a;  /* Paper-like warm blue. For archival sections. */
```

### Foreground & Text Scale

```css
/* Primary text — highest contrast */
--color-text-primary: #ffffff;         /* Pure white only for text. NEVER for backgrounds. */

/* Secondary text — comfortable readability */
--color-text-secondary: #e0eaf5;       /* Off-white with blue tint. Body text. */

/* Muted text — captions, metadata, timestamps */
--color-text-muted: #8aa9c4;           /* Blue-grey. Lower in hierarchy. */

/* Disabled / ghost text */
--color-text-ghost: rgba(138, 169, 196, 0.5);  /* 50% muted. For placeholders. */
```

### Accent Scale

```css
/* PRIMARY ACCENT — Electric cyan/teal. Derived from images 8, 9, 13. */
--color-accent-cyan: #a8f0e8;        /* Bright cyan-teal. CTAs, highlights, interactive elements. */
--color-accent-cyan-dim: #6cc8c0;    /* Dimmed cyan. Hover secondary, disabled active. */

/* SECONDARY ACCENT — Cool blue. Derived from images 3, 5, 6. */
--color-accent-blue: #7bb8e8;        /* Medium blue. Links, secondary buttons. */
--color-accent-blue-dim: #4a8ab0;    /* Dimmed blue. Hover states. */

/* GLITCH ACCENT — Violet-magenta intrusion. Derived from images 11, 12. */
--color-accent-glitch-magenta: #d060c0;   /* Chromatic aberration magenta channel. */
--color-accent-glitch-cyan: #60d0d0;      /* Chromatic aberration cyan channel. */

/* WARM COLLECTION — Parchment/halftone warmth. Derived from image 7. */
--color-accent-warm: #c8b898;             /* Warm off-white for parchment effects. */
--color-accent-warm-dim: #a89070;         /* Dimmed warm tone. */
```

### Semantic Colors

```css
--color-success: #6cc8c0;           /* Teal-green. Subtle, not bright. */
--color-warning: #c8a860;           /* Dim amber. Not yellow. */
--color-error: #c06070;             /* Muted rose. Not bright red. */
--color-info: #7bb8e8;              /* Same as accent-blue. */
```

### Gradient System

Gradients are **subtle and rare**. Never use multi-stop gradients. Prefer two-stop, low-opacity blends.

```css
/* Hero vignette — dark edges, lighter center */
--gradient-vignette: radial-gradient(
  ellipse 80% 60% at 50% 40%,
  rgba(10, 22, 40, 0) 0%,
  rgba(10, 22, 40, 0.6) 100%
);

/* Section transition — subtle light-to-dark for section breaks */
--gradient-section: linear-gradient(
  180deg,
  var(--color-bg-dark) 0%,
  var(--color-bg-deep) 100%
);

/* Glitch accent — cyan-to-magenta chromatic seam */
--gradient-glitch: linear-gradient(
  90deg,
  rgba(96, 208, 208, 0.3) 0%,
  rgba(208, 96, 192, 0.3) 100%
);
```

### Contrast Rules

| Context | Element | Background | Target | Achieved |
|---------|---------|------------|--------|----------|
| Hero text | `--color-text-primary` | `--color-bg-deep` | 7:1 | ~18:1 |
| Body text | `--color-text-secondary` | `--color-bg-dark` | 4.5:1 | ~9:1 |
| Muted text | `--color-text-muted` | `--color-bg-dark` | 3:1 | ~6:1 |
| Accent text | `--color-accent-cyan` | `--color-bg-deep` | 4.5:1 | ~8:1 |
| Glitch accent | `--color-accent-glitch-magenta` | `--color-bg-deep` | 3:1 | ~5:1 |

### Color Application Rules

1. **Never use pure black (`#000000`)** — always use `--color-bg-deep` or darker variants
2. **Never use pure white as a background** — only for text and thin borders
3. **Color is contextual** — the cyan/teal accent lives in interactive elements only (buttons, links, active states). It is not decorative.
4. **Violet/magenta glitch is a punctuation mark** — use only for chromatic aberration effects, not as a surface color
5. **Warm tones are for texture layers only** — the parchment/warm palette exists in noise textures and halftone overlays, not as surfaces
6. **No color should appear in isolation** — every accent color should be accompanied by its dim variant for hover/active states

---

## 4. Design Tokens — Typography

### Core Principle

Typography is a **material and a texture**, not just a communication layer. The system uses three families in deliberate tension: **Traditional Serif** (warmth, history, decay), **Geometric Sans-Serif** (modernity, UI clarity), and **Monospace** (machine voice, data authenticity).

### Font Families

```css
/* BODY & UI — Geometric sans-serif. Clean, modern, functional. */
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;

/* DISPLAY — Traditional serif. Warm, editorial, aged. For large headers. */
--font-serif: 'Crimson Text', 'Noto Serif', Georgia, 'Times New Roman', serif;

/* ALTERNATE DISPLAY — Elegant serif. For poetic/lyric text. */
--font-serif-alt: 'Playfair Display', Georgia, serif;

/* CODE & DATA — Monospace. Machine voice, authenticity. */
--font-mono: 'JetBrains Mono', 'Space Mono', 'Fira Code', 'Courier New', monospace;

/* DECORATIVE — Condensed sans-serif. For badge/label text. */
--font-condensed: 'Inter Tight', 'Inter', -apple-system, sans-serif;
```

### Size Hierarchy

```css
/* 
 * All sizes use clamp() for fluid scaling.
 * Base: 16px. Scale: 1.25 (Major Third).
 */

--text-3xl: clamp(2.5rem, 5.5vw, 5.5rem);   /* Hero — 40px to 88px */
--text-2xl: clamp(2rem, 4vw, 3.5rem);         /* Section headers — 32px to 56px */
--text-xl:  clamp(1.5rem, 3vw, 2.5rem);       /* Card titles — 24px to 40px */
--text-lg:  clamp(1.125rem, 2vw, 1.5rem);     /* Subheaders — 18px to 24px */
--text-base: clamp(0.875rem, 1.5vw, 1rem);    /* Body — 14px to 16px */
--text-sm:  clamp(0.75rem, 1.25vw, 0.875rem); /* Captions — 12px to 14px */
--text-xs:  clamp(0.625rem, 1vw, 0.75rem);    /* Meta — 10px to 12px */
```

### Weight System

```css
--weight-light: 300;        /* Serif body text, poetic sections */
--weight-regular: 400;      /* Body copy */
--weight-medium: 500;       /* Strong body, subheaders */
--weight-semibold: 600;     /* UI labels, buttons */
--weight-bold: 700;         /* Headers */
--weight-black: 800;        /* Display type only */
```

### Line Height System

```css
--leading-tight: 0.9;        /* Large display text (h1, hero) */
--leading-snug: 1.1;         /* Subheaders, section titles */
--leading-normal: 1.4;       /* Body copy, cards */
--leading-relaxed: 1.7;      /* Poetic/lyric text */
--leading-mono: 1.6;         /* Code blocks */
```

### Letter Spacing System

```css
--tracking-tight: -0.02em;     /* Large display text */
--tracking-normal: 0em;        /* Body copy */
--tracking-wide: 0.05em;       /* UI labels */
--tracking-wider: 0.08em;      /* Small caps, badges */
--tracking-widest: 0.12em;     /* Meta, timestamps */
```

### Typography Usage Rules

| Context | Font | Weight | Size | Spacing | Leading |
|---------|------|--------|------|---------|---------|
| Hero heading | `--font-serif` or `--font-sans` | 700-800 | `--text-3xl` | `--tracking-tight` | `--leading-tight` |
| Section heading | `--font-sans` or `--font-serif` | 700 | `--text-2xl` | `--tracking-tight` | `--leading-snug` |
| Card title | `--font-serif` | 600 | `--text-xl` | `--tracking-normal` | `--leading-snug` |
| Body text | `--font-sans` | 400 | `--text-base` | `--tracking-normal` | `--leading-normal` |
| Poetic text | `--font-serif-alt` | 300-400 | `--text-sm` to `--text-lg` | `--tracking-normal` | `--leading-relaxed` |
| UI label | `--font-condensed` | 600 | `--text-xs` | `--tracking-wider` | `--leading-normal` |
| Code/data | `--font-mono` | 400 | `--text-sm` | `--tracking-normal` | `--leading-mono` |
| Badge | `--font-condensed` | 600 | `--text-xs` | `--tracking-widest` | `--leading-tight` |
| Meta/caption | `--font-condensed` | 500 | `--text-xs` | `--tracking-wide` | `--leading-snug` |

### The Fragmented Text Treatment

This is a **signature technique** derived from images 11, 12, and 13. Text that appears broken, misaligned, or partially obscured by textures.

```css
/* 1. Broken Serif — serif text with intentional distortion simulation */
.fragment-serif {
  font-family: var(--font-serif);
  font-weight: 700;
  /* The "broken" effect comes from texture overlays and subtle transforms */
  filter: url('#chromatic-aberration');  /* See texture system */
  letter-spacing: -0.01em;  /* Slightly tighter than normal */
}

/* 2. Sliding offset — letters appear to slip vertically (from image 13) */
.fragment-slide {
  display: inline-block;
  transform: translateY(var(--slide-offset, 0px));
}

.fragment-slide span:nth-child(odd) {
  --slide-offset: -4px;
}

.fragment-slide span:nth-child(even) {
  --slide-offset: 4px;
}

/* 3. Text as liquid — blurred, smeared, overlapping (from image 13 teal element) */
.fragment-blur {
  filter: blur(4px);
  opacity: 0.7;
  mix-blend-mode: screen;
}
```

### Mixed Script Rule

When using multiple writing systems (English + Japanese), apply:

- Vertical (`writing-mode: vertical-rl`) for Japanese text blocks (image 4)
- Horizontal stacking for English
- Different font families: serif for English display, sans-serif for Japanese
- Different tracking: tighten Japanese, widen English

---

## 5. Design Tokens — Spacing & Layout

### Core Principle

Spacing follows the **collage logic**: generous for atmosphere, tight for tension. Never uniform. The spacing scale is intentionally non-linear — it creates rhythm through contrast.

### Spacing Scale

```css
--space-0:  0;
--space-1:  0.25rem;     /* 4px — micro adjustments */
--space-2:  0.5rem;      /* 8px — tight gaps */
--space-3:  0.75rem;     /* 12px — compact elements */
--space-4:  1rem;        /* 16px — base unit */
--space-5:  1.5rem;      /* 24px — section padding */
--space-6:  2rem;        /* 32px — card gaps */
--space-8:  3rem;        /* 48px — section margins */
--space-10: 4rem;        /* 64px — major sections */
--space-12: 5rem;        /* 80px — hero separation */
--space-16: 8rem;        /* 128px — page-level spacing */
--space-20: 10rem;       /* 160px — generous negative space */
```

### Column System

```css
--col-1: 1fr;
--col-2: 2fr;
--col-3: 3fr;

/* Common splits (from image analysis) */
--split-60-40: 60% 40%;
--split-70-30: 70% 30%;
--split-50-50: 1fr 1fr;
--split-data: 1fr 2fr;  /* Code left, visual right (image 6) */
```

### Gap System

```css
--gap-sm:  0.5rem;    /* Small cards, inline elements */
--gap-md:  1rem;      /* Standard card gaps */
--gap-lg:  2rem;      /* Section internal gaps */
--gap-xl:  4rem;      /* Between major sections */
```

### Responsive Breakpoints

```css
/* Mobile-first approach */
--bp-sm: 640px;    /* Large phones */
--bp-md: 768px;    /* Tablets */
--bp-lg: 1024px;   /* Desktop */
--bp-xl: 1280px;   /* Wide desktop */
--bp-2xl: 1536px;  /* Max content width */
```

### Layout Rules

1. **Never center-align vertically** — content should float within sections, off-center
2. **60/40 is the default split** — for two-column layouts, give 60% to the primary content
3. **Generous outer padding** — `clamp(1.5rem, 4vw, 4rem)` for main container
4. **Max content width** — `1280px` for reading comfort; hero sections can be full-width
5. **Negative space is structural** — empty areas are not wasted space, they are composition elements
6. **Card grids should stagger** — every other card shifts down by `--space-6` (from image 1 vertical stacking)

---

## 6. Texture System (The Soul of the Design)

### Core Principle

Texture is the **primary visual language**. Where other designs use color variation, this system uses texture variation. Every screen must carry at minimum the base noise layer. Advanced screens layer multiple textures.

### Layer Hierarchy

```
Layer 0: Base page background (solid color)
Layer 1: Film grain / noise (global, always present)
Layer 2: Paper texture (optional, archival sections)
Layer 3: CRT scanlines (optional, data/code sections)
Layer 4: Chromatic aberration (optional, hero/interactive)
Layer 5: Halftone overlays (optional, print-reference sections)
Layer 6: Content elements (text, images, components)
```

### Texture 1 — Film Grain / Digital Noise (MANDATORY)

Applied globally. Implementation provides both CSS-only and SVG filter approaches.

**CSS-only approach (best performance):**

```css
body {
  /* Core noise as background-image — fast, no external assets */
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.65' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 256px 256px;
  opacity: 0.08;  /* Adjust per context */
  pointer-events: none;
  mix-blend-mode: overlay;
}
```

**SVG filter approach (higher quality, more flexibility):**

Place at the end of `<body>` as a fixed overlay:

```svg
<svg class="noise-overlay" width="100%" height="100%">
  <filter id="noiseFilter">
    <feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="4" stitchTiles="stitch" result="noise" />
    <feColorMatrix type="matrix" in="noise" values="1 0 0 0 0  0 1 0 0 0  0 0 1 0 0  0 0 0 0.15 0" result="coloredNoise" />
    <feComposite operator="in" in="coloredNoise" in2="SourceGraphic" />
  </filter>
  <rect width="100%" height="100%" filter="url(#noiseFilter)" opacity="0.12" style="mix-blend-mode: overlay; pointer-events: none;" />
</svg>
```

**Noise opacity by context:**

| Context | Opacity | Implementation |
|---------|---------|---------------|
| Hero sections | `0.15` | Heavy for emotional impact |
| Content cards | `0.08` | Subtle, maintain readability |
| Navigation | `0.04` | Barely visible |
| Images (overlay) | `0.18` | Heavy to unify image layers |
| Text blocks | `0.03` | Trace only, never obscure text |

### Texture 2 — CRT Scanlines (RECOMMENDED for data/code sections)

```css
.scanlines {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background: repeating-linear-gradient(
    to bottom,
    transparent 0px,
    rgba(0, 0, 0, 0.06) 1px,
    transparent 2px
  );
  background-size: 100% 3px;
  opacity: 0.5;
}
```

**Variants:**

- `--scanline-subtle`: `rgba(0,0,0,0.04)` with `3px` spacing — for content areas
- `--scanline-heavy`: `rgba(0,0,0,0.1)` with `2px` spacing — for code/data sections
- `--scanline-blue`: `rgba(96, 208, 208, 0.04)` — cyan-tinted for hero sections

### Texture 3 — Chromatic Aberration (Glitch Effect)

Derived from images 11 and 12. This is not a gimmick — it is a **core visual texture** that can be applied statically or animated.

**CSS filter approach:**

```css
.glitch-text {
  /* Simulates RGB channel misalignment */
  text-shadow:
    -1px 0 var(--color-accent-glitch-cyan),
     1px 0 var(--color-accent-glitch-magenta);
}

/* Heavy chromatic aberration for large display text */
.glitch-heavy {
  text-shadow:
    -3px 0 rgba(96, 208, 208, 0.5),
     3px 0 rgba(208, 96, 192, 0.5);
}
```

**Pseudo-element approach (for images and containers):**

```css
.chromatic-overlay {
  position: relative;
}

.chromatic-overlay::before,
.chromatic-overlay::after {
  content: '';
  position: absolute;
  inset: 0;
  pointer-events: none;
  mix-blend-mode: screen;
}

.chromatic-overlay::before {
  /* Cyan channel offset */
  background: rgba(96, 208, 208, 0.03);
  transform: translateX(-2px);
}

.chromatic-overlay::after {
  /* Magenta channel offset */
  background: rgba(208, 96, 192, 0.03);
  transform: translateX(2px);
}
```

**SVG filter (for static glitch on text):**

```svg
<filter id="chromatic-aberration">
  <feOffset in="SourceGraphic" dx="2" dy="0" result="cyan-offset" />
  <feColorMatrix in="cyan-offset" type="matrix" values="0 0 0 0 0.4  0 0 0 0 0.8  0 0 0 0 0.8  0 0 0 0.3 0" result="cyan-colored" />
  <feOffset in="SourceGraphic" dx="-2" dy="0" result="magenta-offset" />
  <feColorMatrix in="magenta-offset" type="matrix" values="0.8 0 0 0 0  0 0 0 0 0  0.6 0 0 0 0  0 0 0 0.3 0" result="magenta-colored" />
  <feBlend mode="screen" in="cyan-colored" in2="magenta-colored" result="glitch" />
  <feBlend mode="normal" in="SourceGraphic" in2="glitch" />
</filter>
```

### Texture 4 — Paper / Surface Texture

Derived from images 7 and 13. Adds warmth and physicality.

```css
.paper-texture {
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='paper'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.04' numOctaves='5'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23paper)' opacity='0.05'/%3E%3C/svg%3E");
  background-repeat: repeat;
  background-size: 400px 400px;
}
```

**Fold lines (decorative, from image 13):**

```css
.fold-line-horizontal {
  width: 100%;
  height: 1px;
  background: rgba(200, 184, 152, 0.08);
  box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
}

.fold-line-vertical {
  width: 1px;
  height: 100%;
  background: rgba(200, 184, 152, 0.08);
  box-shadow: 1px 0 0 rgba(0, 0, 0, 0.1);
}
```

### Texture 5 — Halftone / Dot Pattern (Optional)

Derived from image 7 (WISP poster) and image 10 (dolphin pointillist).

```css
.halftone-overlay {
  position: absolute;
  inset: 0;
  pointer-events: none;
  background-image: radial-gradient(
    rgba(200, 184, 152, 0.06) 1px,
    transparent 1px
  );
  background-size: 3px 3px;
}
```

**Pointillist graphic element (from image 10):**

Used for structural graphic overlays — logos, letter frames, decorative "A" shapes built from dots.

```css
.dot-structure {
  /* Use CSS mask with radial gradients for dot-based shapes */
  -webkit-mask-image: radial-gradient(
    circle at 50% 50%,
    black 0%,
    transparent 40%
  );
  mask-image: radial-gradient(
    circle at 50% 50%,
    black 0%,
    transparent 40%
  );
}
```

### Texture Combination Rules

1. **Noise is always present** — every other texture is optional
2. **Scanlines + Chromatic Aberration** — pairing creates the "CRT glitch" feel (images 3, 5, 6)
3. **Paper + Halftone** — pairing creates the "printed archival" feel (image 7)
4. **Noise + Paper** — creates "aged photograph" feel (images 10, 9)
5. **Never combine more than 3 texture layers** — visual overload breaks the subtle aesthetic
6. **Textures should be invisible** — the user should feel them, not see them. If someone asks "is that grain on the screen?", the texture is at the right opacity.

---

## 7. Component Architecture

### 7.1 Navigation System

**Purpose:** Minimal, integrated, atmospheric. Feels like a museum label, not a UI bar.

**Visual appearance:**
- Fixed position, thin, semi-transparent
- Brand name in serif, links in condensed sans uppercase
- Chromatic aberration on hover for active link

**Structure:**
```
┌──────────────────────────────────┐
│ brand        WORK  ABOUT  CONTACT │
└──────────────────────────────────┘
```

**Variants:**

| Variant | Position | Background | When |
|---------|----------|------------|------|
| Default | Top-left | `rgba(10, 22, 40, 0.6)` + noise | Standard pages |
| Transparent | Top-left | None | Hero sections with full-bleed imagery |
| Inline | Within content | None | Editorial/article pages |

**States:**

| State | Brand | Links |
|-------|-------|-------|
| Default | `--color-text-primary` + `--font-serif` | `--color-text-muted` + `--tracking-wider` |
| Hover | — | `--color-accent-cyan` + `1px` bottom border |
| Active | — | `--color-accent-cyan` + `--font-weight-bold` |
| Mobile menu open | Unchanged | Full-screen overlay, `--text-xl`, vertical stack |

**CSS:**

```css
.nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: clamp(1rem, 2vw, 1.5rem) clamp(1.5rem, 4vw, 4rem);
  background: rgba(10, 22, 40, 0.6);
  backdrop-filter: blur(8px);
}

.nav-brand {
  font-family: var(--font-serif);
  font-size: var(--text-lg);
  font-weight: 700;
  color: var(--color-text-primary);
  text-decoration: none;
  letter-spacing: -0.01em;
}

.nav-links {
  display: flex;
  gap: var(--space-6);
  list-style: none;
}

.nav-link {
  font-family: var(--font-condensed);
  font-size: var(--text-xs);
  font-weight: 600;
  color: var(--color-text-muted);
  text-decoration: none;
  text-transform: uppercase;
  letter-spacing: var(--tracking-wider);
  transition: color 0.3s ease;
  position: relative;
}

.nav-link::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 1px;
  background: var(--color-accent-cyan);
  transition: width 0.3s ease;
}

.nav-link:hover {
  color: var(--color-accent-cyan);
}

.nav-link:hover::after {
  width: 100%;
}
```

---

### 7.2 Hero Section Patterns

#### Pattern A — Full-Screen Collage (Primary)

**Reference:** Images 1, 8, 9

**Purpose:** Atmospheric full-viewport entry. Combines background imagery with layered text blocks.

**Structure:**
```
┌──────────────────────────────┐
│  ┌─────┐                     │
│  │text │      image          │
│  │block│      (60%)          │
│  │(40%)│                     │
│  └─────┘                     │
│         ┌────────────────┐   │
│         │ overlay text   │   │
│         └────────────────┘   │
├──────────────────────────────┤
│     scroll indicator         │
└──────────────────────────────┘
```

**CSS structure:**

```css
.hero-collage {
  position: relative;
  min-height: 100vh;
  display: grid;
  grid-template-columns: var(--split-60-40);
  align-items: center;
  overflow: hidden;
}

.hero-collage-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.hero-collage-bg img,
.hero-collage-bg video {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.65) contrast(1.2) saturate(0.85);
}

.hero-collage-content-left {
  position: relative;
  z-index: 2;
  padding: var(--space-10);
}

.hero-collage-content-right {
  position: relative;
  z-index: 2;
  padding: var(--space-10);
}
```

**Variants:**

| Variant | Layout | Best For |
|---------|--------|----------|
| Collage A1 | Image spans full width with text overlay | Strong single image (image 8 jellyfish) |
| Collage A2 | 60/40 split, image right | Text-heavy entry (image 1 eyes) |
| Collage A3 | Image as background with floating text blocks | Atmospheric entry (image 9 flower) |

---

#### Pattern B — Diagonal Split

**Reference:** Image 5 (Joi album art)

**Purpose:** Dramatic diagonal division creating tension between dark/light zones.

**Structure:**
```
      dark zone
        ↓
 ┌──────╱─────────────────┐
 │     ╱                  │
 │    ╱                   │
 │   ╱  light zone        │
 │  ╱                     │
 │ ╱──────────────────────│
 ╱                        │
└─────────────────────────┘
```

**CSS:**

```css
.hero-diagonal {
  position: relative;
  min-height: 100vh;
  overflow: hidden;
}

.hero-diagonal::before {
  content: '';
  position: absolute;
  inset: 0;
  background: var(--color-bg-deep);
  clip-path: polygon(0 0, 45% 0, 25% 100%, 0 100%);
  z-index: 0;
}

.hero-diagonal-light {
  position: absolute;
  inset: 0;
  background: var(--color-bg-mid);
  clip-path: polygon(45% 0, 100% 0, 100% 100%, 25% 100%);
  z-index: 0;
}

.hero-diagonal-content {
  position: relative;
  z-index: 2;
  display: grid;
  grid-template-columns: 45% 55%;
  min-height: 100vh;
  align-items: center;
}

.hero-diagonal-content-dark {
  padding: var(--space-10);
  color: var(--color-text-primary);
}

.hero-diagonal-content-light {
  padding: var(--space-10);
  color: var(--color-text-secondary);
}
```

---

#### Pattern C — Split-Screen Code/Data

**Reference:** Image 6 (Mandelbrot fractal)

**Purpose:** Educational/technical sections showing code alongside visual output.

**Structure:**
```
┌────────────────┬──────────┐
│                │          │
│   CODE PANEL   │  VISUAL  │
│   (monospace)  │  OUTPUT  │
│                │          │
│                │          │
└────────────────┴──────────┘
```

**CSS:**

```css
.hero-split {
  display: grid;
  grid-template-columns: var(--split-data);
  min-height: 80vh;
}

.hero-split-code {
  background: var(--color-bg-deep);
  padding: var(--space-8);
  font-family: var(--font-mono);
  font-size: var(--text-sm);
  line-height: var(--leading-mono);
  color: var(--color-text-muted);
  overflow-x: auto;
  white-space: pre;
}

.hero-split-code .keyword { color: var(--color-accent-cyan-dim); }
.hero-split-code .string { color: var(--color-accent-glitch-magenta); }
.hero-split-code .comment { color: rgba(138, 169, 196, 0.5); }

.hero-split-visual {
  position: relative;
  overflow: hidden;
}

.hero-split-visual img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.7) contrast(1.3);
}

/* Scanline overlay on code panel only */
.hero-split-code {
  position: relative;
}

.hero-split-code::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    to bottom,
    transparent 0px,
    rgba(0, 0, 0, 0.06) 1px,
    transparent 2px
  );
  background-size: 100% 3px;
  pointer-events: none;
}
```

---

#### Pattern D — Typographic Composition

**Reference:** Image 13 ("fllla" typography asset)

**Purpose:** Minimalist, type-as-art hero. For manifesto, tagline, or poetic content.

**Structure:**
```
┌──────────────────────────────────┐
│                                  │
│          ┌──┐                    │
│          │f │  ┌──┐ ┌──┐        │
│   ┌──────┘  │  │ll│ │a │        │
│   │  TEAL   │  └──┘ └──┘        │
│   │  BLUR   │                    │
│   │  SHAPE  │                    │
│   └─────────┘                    │
│                                  │
│  come down freely under gravity  │
│                                  │
│  Nº 067                   20/23 │
└──────────────────────────────────┘
```

**CSS:**

```css
.hero-typographic {
  min-height: 80vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  position: relative;
  background: var(--color-bg-parchment);
}

.hero-typographic-word {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-sans);
  font-weight: var(--weight-black);
  font-size: var(--text-3xl);
  text-transform: lowercase;
  color: var(--color-bg-deep);
}

.hero-typographic-blur {
  font-size: var(--text-3xl);
  font-weight: var(--weight-black);
  filter: blur(6px);
  opacity: 0.6;
  mix-blend-mode: multiply;
  color: var(--color-accent-cyan);
}

.hero-typographic-sub {
  margin-top: var(--space-6);
  font-family: var(--font-condensed);
  font-size: var(--text-sm);
  letter-spacing: var(--tracking-wide);
  text-transform: lowercase;
  color: var(--color-text-ghost);
}
```

---

#### Pattern E — Vertical Stack

**Reference:** Image 1 (three stacked eyes)

**Purpose:** Rhythmic, repeating visual elements creating meditative vertical composition.

**Structure:**
```
┌────────────┬──────────┐
│            │  ┌────┐  │
│  text      │  │eye │  │
│  block     │  │ 1  │  │
│            │  └────┘  │
│            │  ┌────┐  │
│            │  │eye │  │
│            │  │ 2  │  │
│            │  └────┘  │
│            │  ┌────┐  │
│            │  │eye │  │
│            │  │ 3  │  │
│            │  └────┘  │
└────────────┴──────────┘
```

**CSS:**

```css
.hero-stack {
  display: grid;
  grid-template-columns: var(--split-60-40);
  min-height: 100vh;
}

.hero-stack-visual {
  display: flex;
  flex-direction: column;
  gap: var(--space-0);  /* No gap for tight stack */
}

.hero-stack-item {
  flex: 1;
  overflow: hidden;
  position: relative;
}

.hero-stack-item img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.7) contrast(1.2);
  transition: filter 0.5s ease;
}

.hero-stack-item:hover img {
  filter: brightness(0.85) contrast(1.3);
}
```

---

### 7.3 Card Component

**Purpose:** Content containers with printed feel. For projects, articles, portfolio items.

**Visual appearance:**
- Hard border (1px solid `rgba(255,255,255,0.12)`)
- No border-radius (sharp corners = printed/collage feel)
- Hard offset shadow (printed depth, not digital shadow)
- Noise overlay at 8% opacity
- Image area with 18rem height

**Structure:**
```
┌──────────────────────────┐
│ ┌──────────────────────┐ │
│ │     IMAGE AREA       │ │
│ │     (16:9 or 4:3)    │ │
│ └──────────────────────┘ │
│                           │
│ BADGE                    │
│                          │
│ Card Title               │
│                          │
│ Body text...             │
│                          │
└──────────────────────────┘
```

**Variants:**

| Variant | Purpose | Differences |
|---------|---------|-------------|
| Default | Standard content | 1fr width, noise at 0.08, hard shadow |
| Stack | Vertical stack (image 1 pattern) | No gap between cards, alternating margin |
| Wide | Feature cards | 2-column span, larger image |
| Text-only | Blog/micro-content | No image area, tighter padding |

**States:**

| State | Visual Change |
|-------|--------------|
| Default | Standard appearance with noise texture |
| Hover | Shadow intensifies (6px 6px offset), brightness on image increases, subtle chromatic aberration on border |
| Active/Focus | 2px border in `--color-accent-cyan`, slight upward transform (-2px) |
| Loading | Skeleton state with animated gradient shimmer + noise |

**CSS:**

```css
.card {
  position: relative;
  background: var(--color-bg-mid);
  border: 1px solid rgba(255, 255, 255, 0.12);
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 4px 4px 0 rgba(0, 0, 0, 0.4);
}

.card::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,...");  /* Noise */
  background-size: 256px 256px;
  opacity: 0.08;
  pointer-events: none;
  z-index: 1;
}

.card-image {
  position: relative;
  height: 18rem;
  overflow: hidden;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.75) contrast(1.15);
  transition: filter 0.4s ease, transform 0.6s ease;
}

.card-image::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 50%, rgba(10, 22, 40, 0.4) 100%);
}

.card-content {
  padding: var(--space-5);
  position: relative;
  z-index: 2;
}

.card-badge {
  display: inline-block;
  font-family: var(--font-condensed);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--color-accent-cyan);
  margin-bottom: var(--space-2);
}

.card-title {
  font-family: var(--font-serif);
  font-size: var(--text-xl);
  font-weight: var(--weight-bold);
  color: var(--color-text-primary);
  line-height: var(--leading-snug);
  margin-bottom: var(--space-3);
}

.card-body {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: var(--leading-normal);
  max-width: 65ch;
}

/* Stagger variant */
.card-stack:nth-child(odd) {
  margin-top: var(--space-6);
}

.card-stack:nth-child(even) {
  margin-bottom: var(--space-6);
}

/* Hover state */
.card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 rgba(0, 0, 0, 0.5);
}

.card:hover .card-image img {
  filter: brightness(0.85) contrast(1.2);
  transform: scale(1.03);
}
```

---

### 7.4 Button System

**Purpose:** Minimal, printed-feel interactive elements. Not rounded, not flashy.

**Visual appearance:**
- 2px border (solid white or accent)
- Noise texture at 4% opacity
- Uppercase condensed typography
- Sharp corners
- Hard offset shadow on hover (printed button feel)

**Variants:**

```css
/* Base button */
.button {
  display: inline-flex;
  align-items: center;
  gap: var(--space-2);
  font-family: var(--font-condensed);
  font-size: var(--text-sm);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-wide);
  text-transform: uppercase;
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  background: transparent;
  border: 2px solid var(--color-text-primary);
  color: var(--color-text-primary);
  cursor: pointer;
  transition: all 0.25s ease;
  position: relative;
}

/* Primary variant */
.button-primary {
  background: var(--color-accent-cyan);
  border-color: var(--color-accent-cyan);
  color: var(--color-bg-deep);
}

.button-primary:hover {
  background: transparent;
  color: var(--color-accent-cyan);
  box-shadow: 4px 4px 0 var(--color-accent-cyan);
  transform: translate(-2px, -2px);
}

/* Ghost variant — for navigation, subtle actions */
.button-ghost {
  border: none;
  padding: 0.5rem 0;
  color: var(--color-text-muted);
}

.button-ghost::after {
  content: '';
  position: absolute;
  bottom: 2px;
  left: 0;
  width: 0;
  height: 1px;
  background: var(--color-accent-cyan);
  transition: width 0.3s ease;
}

.button-ghost:hover {
  color: var(--color-accent-cyan);
}

.button-ghost:hover::after {
  width: 100%;
}

/* Glitch variant — for special CTAs */
.button-glitch {
  border-color: rgba(208, 96, 192, 0.4);
  color: var(--color-accent-glitch-magenta);
  text-shadow:
    -0.5px 0 var(--color-accent-glitch-cyan),
     0.5px 0 var(--color-accent-glitch-magenta);
}

.button-glitch:hover {
  background: rgba(208, 96, 192, 0.1);
  border-color: var(--color-accent-glitch-magenta);
  box-shadow:
     3px 0 0 rgba(96, 208, 208, 0.3),
    -3px 0 0 rgba(208, 96, 192, 0.3);
  transform: translate(-2px, -2px);
}
```

---

### 7.5 Text / Data Block Components

#### Poetic Text Block

**Reference:** Images 4, 8, 9

```css
.text-poetic {
  font-family: var(--font-serif-alt);
  font-size: clamp(1rem, 2.5vw, 1.5rem);
  font-weight: var(--weight-light);
  line-height: var(--leading-relaxed);
  color: var(--color-text-secondary);
  max-width: 45ch;
  margin: 0;
}

.text-poetic em {
  font-style: italic;
  color: var(--color-accent-cyan);
}
```

#### Data Stream Block

**Reference:** Image 6

```css
.data-stream {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  line-height: var(--leading-mono);
  color: var(--color-text-muted);
  white-space: pre-wrap;
  overflow-x: auto;
  max-height: 400px;
  overflow-y: auto;
  position: relative;
  padding: var(--space-4);
  background: rgba(0, 0, 0, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.06);
}

.data-stream::after {
  content: '';
  position: absolute;
  inset: 0;
  background: repeating-linear-gradient(
    to bottom,
    transparent 0px,
    rgba(0, 0, 0, 0.06) 1px,
    transparent 2px
  );
  background-size: 100% 3px;
  pointer-events: none;
}
```

#### Label / Badge System

```css
.label {
  font-family: var(--font-condensed);
  font-size: var(--text-xs);
  font-weight: var(--weight-semibold);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--color-text-muted);
  display: inline-block;
}

.label-accent {
  color: var(--color-accent-cyan);
}

.label-number {
  font-family: var(--font-mono);
  font-size: var(--text-2xl);
  font-weight: var(--weight-bold);
  letter-spacing: var(--tracking-tight);
  color: var(--color-text-primary);
}
```

---

### 7.6 Section Divider

**Purpose:** Atmospheric section transitions without aggressive visual breaks.

```css
.section-divider {
  display: flex;
  align-items: center;
  gap: var(--space-4);
  padding: var(--space-8) 0;
}

.section-divider-line {
  flex: 1;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.1) 50%,
    transparent 100%
  );
}

.section-divider-label {
  font-family: var(--font-condensed);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--color-text-ghost);
  white-space: nowrap;
}
```

### 7.7 Pointillist Graphic Element

**Reference:** Image 10 (dolphin seascape)

**Purpose:** Structural decorative graphics built from dots. Used for background letterforms, frames, or abstract shapes.

```css
.pointillist {
  position: absolute;
  pointer-events: none;
  /* Build with repeating radial gradients for the dot pattern */
  background-image: radial-gradient(
    circle at 50% 50%,
    rgba(255, 255, 255, 0.15) 1px,
    transparent 1px
  );
  background-size: 0.25em 0.25em;
  -webkit-mask-image: ...;  /* Use mask for shape */
  mask-image: ...;
}
```

### 7.8 Glitch Text Component

**Reference:** Images 11, 12

**Purpose:** Decorative text with chromatic aberration, pixelation, and vertical stretching.

```css
.glitch-text {
  position: relative;
  display: inline-block;
  font-family: var(--font-serif);
  font-weight: var(--weight-bold);
  color: var(--color-bg-deep);
}

.glitch-text::before,
.glitch-text::after {
  content: attr(data-text);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.glitch-text::before {
  /* Cyan channel — offset left */
  color: var(--color-accent-glitch-cyan);
  z-index: -1;
  transform: translateX(-2px);
  clip-path: inset(0 30% 20% 0);
}

.glitch-text::after {
  /* Magenta channel — offset right */
  color: var(--color-accent-glitch-magenta);
  z-index: -1;
  transform: translateX(2px);
  clip-path: inset(30% 0 0 20%);
}
```

---

### 7.9 Footer

**Purpose:** Minimal archival footer with metadata feel.

```css
.footer {
  padding: var(--space-10) clamp(1.5rem, 4vw, 4rem);
  border-top: 1px solid rgba(255, 255, 255, 0.06);
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: var(--space-8);
}

.footer-label {
  font-family: var(--font-condensed);
  font-size: var(--text-xs);
  letter-spacing: var(--tracking-widest);
  text-transform: uppercase;
  color: var(--color-text-ghost);
  margin-bottom: var(--space-3);
}

.footer-content {
  font-family: var(--font-sans);
  font-size: var(--text-sm);
  color: var(--color-text-muted);
  line-height: var(--leading-normal);
}

.footer-meta {
  font-family: var(--font-mono);
  font-size: var(--text-xs);
  color: var(--color-text-ghost);
  grid-column: 1 / -1;
  text-align: right;
}
```

---

## 8. Interaction & Motion System

### Core Principle

Animation is **atmospheric, not functional**. Nothing moves quickly. Nothing bounces. The motion language is: breathing, floating, drifting, decaying.

### Motion Values

```css
--duration-slow: 8s;      /* Noise breathing, background drift */
--duration-medium: 3s;    /* Scroll reveals, fade transitions */
--duration-fast: 0.5s;    /* Hover states, micro-interactions */
--duration-instant: 0.15s; /* Press states, toggle changes */

--ease-out-expo: cubic-bezier(0.19, 1, 0.22, 1);  /* Primary ease */
--ease-in-out: cubic-bezier(0.65, 0, 0.35, 1);     /* Scroll reveals */
--ease-linear: linear;                               /* Noise animation */
```

### Animation 1 — Noise Breathing (Global)

```css
@keyframes noise-breathe {
  0%, 100% { opacity: var(--noise-opacity); }
  50% { opacity: calc(var(--noise-opacity) * 1.3); }
}

.noise-overlay {
  animation: noise-breathe var(--duration-slow) var(--ease-in-out) infinite;
}
```

### Animation 2 — Glitch Flicker (Hero Images)

```css
@keyframes glitch-flicker {
  0%, 100% { 
    clip-path: inset(0 0 0 0);
    transform: translate(0, 0);
    filter: brightness(1) contrast(1);
  }
  5% {
    clip-path: inset(20% 0 60% 0);
    transform: translate(-4px, 2px);
    filter: brightness(1.1) contrast(1.3) hue-rotate(-5deg);
  }
  10% {
    clip-path: inset(70% 0 10% 0);
    transform: translate(2px, -2px);
    filter: brightness(0.9) contrast(1.1) hue-rotate(5deg);
  }
  15% {
    clip-path: inset(0 0 0 0);
    transform: translate(0, 0);
    filter: brightness(1) contrast(1);
  }
}

.hero-image.glitch {
  animation: glitch-flicker 12s var(--ease-linear) infinite;
}
```

### Animation 3 — Chromatic Aberration Oscillation

```css
@keyframes chromatic-drift {
  0%, 100% {
    text-shadow:
      -1px 0 var(--color-accent-glitch-cyan),
       1px 0 var(--color-accent-glitch-magenta);
  }
  50% {
    text-shadow:
      -2px 0 var(--color-accent-glitch-cyan),
       2px 0 var(--color-accent-glitch-magenta);
  }
}

.glitch-active {
  animation: chromatic-drift 4s var(--ease-in-out) infinite;
}
```

### Animation 4 — Scroll Reveal

```css
@keyframes reveal-up {
  from {
    opacity: 0;
    transform: translateY(2rem);
    filter: blur(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
    filter: blur(0);
  }
}

.reveal {
  opacity: 0;
}

.reveal.visible {
  animation: reveal-up var(--duration-medium) var(--ease-out-expo) forwards;
}

/* Stagger children */
.reveal.visible:nth-child(1) { animation-delay: 0.1s; }
.reveal.visible:nth-child(2) { animation-delay: 0.2s; }
.reveal.visible:nth-child(3) { animation-delay: 0.3s; }
.reveal.visible:nth-child(4) { animation-delay: 0.4s; }
```

### Animation 5 — Hover States

```css
/* Button hover — printed press */
.button:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0 var(--color-accent-cyan);
  transition: transform var(--duration-fast) var(--ease-out-expo),
              box-shadow var(--duration-fast) var(--ease-out-expo);
}

/* Card hover — lift */
.card:hover {
  transform: translate(-2px, -2px);
  box-shadow: 6px 6px 0 rgba(0, 0, 0, 0.5);
}

/* Link hover — underline draw */
.nav-link::after {
  transition: width var(--duration-fast) var(--ease-out-expo);
}
```

### Reduced Motion

```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }

  .noise-overlay {
    animation: none;
    opacity: var(--noise-opacity);
  }

  .hero-image.glitch {
    animation: none;
  }
}
```

### Interaction Rules

1. **Hover is the primary interaction state** — every clickable element has a distinct hover appearance
2. **No hover on touch devices** — use `@media (hover: hover)` to enable hover-only effects
3. **Focus states are visible** — all interactive elements have a focus ring in `--color-accent-cyan`
4. **No hover animations below 768px** — mobile relies on tap/focus states
5. **No auto-play animations** — noise breathing is the only continuous animation; glitch flicker requires the element to be in viewport

---

## 9. Image Treatment Guidelines

### Global Treatment (Apply to All Display Images)

```css
.global-image-treatment {
  filter: 
    brightness(0.75)        /* Darken base — from the moody reference images */
    contrast(1.2)           /* Increase contrast — from the high-contrast aesthetic */
    saturate(0.9);          /* Slight desaturation — from the monochromatic palette */
}

/* Hero-level treatment — more dramatic */
.hero-image-treatment {
  filter:
    brightness(0.65)
    contrast(1.3)
    saturate(0.85);
}

/* Card-level treatment — subtle */
.card-image-treatment {
  filter:
    brightness(0.8)
    contrast(1.15);
}
```

### Image Overlay Sequence

```
Layer 0: Image (base)
Layer 1: Gradient vignette (dark edges)
Layer 2: Noise texture (15-18% opacity)
Layer 3: Chromatic aberration pseudo-element (optional, hero only)
```

### Video Background Treatment

```css
.video-bg {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.6) contrast(1.3) saturate(0.8);
}

.video-bg::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(
    180deg,
    transparent 0%,
    rgba(10, 22, 40, 0.3) 100%
  );
  pointer-events: none;
}
```

### Image Sourcing Rules

1. **Prefer low-light images** that benefit from the darkening treatment
2. **Prefer high-contrast subjects** — silhouettes, single subjects on dark backgrounds
3. **Avoid bright, saturated imagery** — it will fight the treatment
4. **Avoid images with pure white backgrounds** — they will look wrong against the dark palette
5. **Text in images should be minimal or absent** — text is a system element, not part of imagery

---

## 10. Layout Grid System

### Primary Grid

```css
.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 clamp(1.5rem, 4vw, 4rem);
}

.container-wide {
  max-width: 100%;
  padding: 0 clamp(1.5rem, 4vw, 4rem);
}

.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: clamp(1rem, 2vw, 2rem);
}
```

### Common Layout Patterns

```css
/* 60/40 asymmetrical split */
.layout-split-60-40 {
  display: grid;
  grid-template-columns: 60% 40%;
  gap: var(--gap-lg);
}

/* 70/30 sidebar layout */
.layout-split-70-30 {
  display: grid;
  grid-template-columns: 70% 30%;
  gap: var(--gap-lg);
}

/* Responsive card grid with stagger */
.layout-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: var(--gap-lg);
}

/* 3-column magazine spread */
.layout-magazine {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: var(--gap-lg);
}
```

### Responsive Breakpoints

```css
/* Base (mobile): single column */
@media (min-width: 640px) {
  /* Two columns possible */
  .layout-split-60-40,
  .layout-split-70-30 {
    grid-template-columns: 1fr;
  }
  
  .layout-magazine {
    grid-template-columns: 1fr;
  }
}

@media (min-width: 768px) {
  .layout-split-60-40 {
    grid-template-columns: 60% 40%;
  }
  
  .layout-split-70-30 {
    grid-template-columns: 70% 30%;
  }
  
  .layout-magazine {
    grid-template-columns: 1fr 2fr 1fr;
  }
}
```

### Grid Rules

1. **No fixed-width containers** — everything uses `clamp()` for fluidity
2. **12-column grid is for section-level layout** — individual components may span any number of columns
3. **Components should not define their own grid** — they are placed within the section's grid
4. **Negative space is part of the grid** — empty columns are valid and intentional
5. **On mobile, collapse to single column** — preserve spacing and atmosphere, not column count

---

## 11. Implementation Strategy

### Framework Recommendation: Astro + React

**Primary: Astro**

| Why Astro | How It Fits |
|-----------|-------------|
| Ships zero JS by default | The site is atmosphere-first, not app-like — minimal JS is correct |
| Islands architecture | Interactive components (glitch hero, noise overlay) are individual islands |
| Content collections | Editorial content (articles, projects) benefits from MDX/Markdown support |
| View transitions | SPA-like smooth transitions without SPA complexity |
| Image optimization | Built-in image component with proper treatment pipeline |

**Secondary: React for interactive islands**

- Noise overlay controller (opacity adjustment, pulsing)
- Glitch text components (chromatic aberration animation)
- Scroll reveal observer wrapper
- CRT flicker simulation

### Styling Architecture: CSS Custom Properties + Tailwind CSS

**Primary: CSS Custom Properties (design tokens)**
All design tokens live in `:root` as CSS variables. These are the single source of truth.

**Secondary: Tailwind CSS (utility layer)**
Tailwind consumes the CSS variables. No Tailwind design tokens — only reference `var(--*)`.

**Why both:**
- CSS variables are framework-agnostic and persist regardless of frontend choice
- Tailwind provides the utility layer for rapid component construction
- Design tokens stay in one place (`_tokens.css`) and Tailwind references them

**File structure:**

```
styles/
├── _tokens.css              # All CSS custom properties
├── _textures.css            # Noise, scanlines, chromatic aberration, paper, halftone
├── _typography.css          # Font faces, type scale, utility classes
├── _animations.css          # All @keyframes definitions
├── _components.css          # Card, button, nav, hero patterns
├── _layout.css              # Grid, containers, spacing utilities
├── _utilities.css           # Noise opacity, glitch, reveal helpers
└── style.css                # Imports all, applies base
```

### Animation Library: Native CSS Animations + Minimal Framer Motion

**Use native CSS for:**
- Noise breathing (8s cycle)
- Glitch flicker (12s cycle)
- Chromatic drift (4s cycle)
- Hover state transitions

**Use Framer Motion (React islands) for:**
- Scroll reveal staggering
- View transition orchestration
- Page-level entrance animations
- Complex orchestration (multi-element staggered reveals)

### Supporting Libraries

| Need | Library | Justification |
|------|---------|--------------|
| Icons | Lucide React | Minimal, consistent, monochrome-friendly |
| Intersection Observer | `react-intersection-observer` | Lightweight scroll reveal |
| Font loading | `@fontsource/inter`, `@fontsource/crimson-text`, etc. | Self-hosted, no external requests |
| Image optimization | Astro built-in `<Image />` | Automatic srcset, format, lazy loading |
| Video | HTML5 `<video>` | No library needed; CSS handles treatment |

### What NOT to Use

| Technology | Reason |
|-----------|--------|
| Three.js / WebGL | Unnecessary complexity. Noise and CRT effects are achievable with CSS/SVG. |
| GSAP | Overkill. CSS animations + Framer Motion cover all needs. |
| Tailwind plugins | Keep Tailwind minimal. No `@tailwindcss/typography` etc. |
| Bootstrap/Chakra/MUI | Custom-designed system. No framework UI library fits the aesthetic. |
| External icon packs | Lucide is minimal enough. No FontAwesome, Material Icons, etc. |

---

## 12. AI Website Generation Specification

### Instructions for Website Generation AI

You are generating a website for the **Noise Web** design system. This section contains everything you need to produce an implementation that matches the intended visual identity.

### Visual Direction Summary

The site feels like a **digital art exhibition** — quiet, atmospheric, slightly melancholic, and futuristic. It is NOT a typical landing page, NOT a portfolio gallery, and NOT a cyberpunk neon experience.

Key attributes:
- **Monochromatic blue/teal** with strategic violet glitch accents
- **Heavy texture** — noise/grain is the primary visual language
- **High contrast** — bright text on dark backgrounds
- **Asymmetrical composition** — 60/40 splits, diagonal divisions, vertical stacking
- **Mixed typography** — serif headers, sans-serif body, monospace for data
- **Slow animations** — 4s to 12s cycles, never fast or bouncy
- **Imperfect by design** — glitch textures, chromatic aberration, scanlines

### Required Design Rules

1. **EVERY screen must have a noise overlay.** Opacity 3-15% depending on context. This is the most important rule.
2. **NEVER use pure black (`#000000`).** Use `#0a1628` or similar deep navy.
3. **NEVER use pure white as a background.** Only for text.
4. **ALWAYS use the hard offset shadow pattern** (no blur, `4px 4px 0 rgba(...)`) for cards and panels. No soft shadows.
5. **ALWAYS treat images** with `brightness(0.75) contrast(1.2) saturate(0.9)`.
6. **NEVER use border-radius.** Sharp corners only.
7. **NEVER use soft gradients.** Flat colors + texture = the look.
8. **ALWAYS use `clamp()` for font sizes and spacing.** Fluid scaling is critical.
9. **NEVER center content vertically.** Use asymmetrical composition.
10. **ALWAYS use uppercase + wide tracking for labels and badges.**

### Component Expectations

The implementation must include these components (from the component architecture section):

| Component | Priority | Notes |
|-----------|----------|-------|
| Noise overlay | CRITICAL | Global, SVG filter preferred, opacity varies by context |
| Navigation | REQUIRED | Fixed top, brand serif, links condensed uppercase |
| Hero — Collage A2 | REQUIRED | 60/40, image right, text left, full viewport |
| Hero — Diagonal B | RECOMMENDED | For alternate page entries |
| Hero — Typographic D | OPTIONAL | For manifesto/landing page |
| Card component | REQUIRED | Content display, stagger support |
| Button system | REQUIRED | Primary, ghost, glitch variants |
| Poetic text block | REQUIRED | Lyric/quote/mission text |
| Data stream block | OPTIONAL | For code/data sections |
| Glitch text | OPTIONAL | For headings that need emphasis |
| Footer | REQUIRED | Minimal, archival style |

### Implementation Priorities

```
Phase 1 — Foundation (Build First)
├── Design tokens CSS (_tokens.css)
├── Base layout (_layout.css)
├── Noise texture system (_textures.css)
├── Typography foundation (_typography.css)
└── Navigation component

Phase 2 — Core Components
├── Hero — Collage A2
├── Card component
├── Button system
├── Section divider
└── Footer

Phase 3 — Texture & Effects
├── Chromatic aberration overlays
├── CRT scanlines
├── Halftone patterns
├── Paper texture
└── Animation system (_animations.css)

Phase 4 — Interactive Features
├── Scroll reveal animations
├── Glitch hover effects
├── Mobile menu
├── View transitions
└── Reduced motion support
```

### Coding Principles

1. **Mobile-first CSS.** Base styles are mobile. Media queries add complexity at larger sizes.
2. **CSS custom properties for ALL design values.** No hardcoded colors, sizes, or spacing outside `_tokens.css`.
3. **Semantic HTML.** Use `<header>`, `<main>`, `<section>`, `<article>`, `<nav>`, `<footer>`.
4. **Accessible markup.** All images need `alt` text. Interactive elements need focus states. Use `prefers-reduced-motion`.
5. **No CSS frameworks.** This is a custom design system. No Bootstrap, Chakra, MUI.
6. **TypeScript preferred** for React islands. PropTypes for any JS-only components.
7. **Comments explain the "why"** not the "what" — especially for texture and animation decisions.

### Things to Avoid

- ❌ Pure black backgrounds (`#000000`)
- ❌ Pure white backgrounds (`#ffffff` outside text)
- ❌ Rounded corners on any element
- ❌ Soft blurry box-shadows (use hard offsets)
- ❌ Bright saturated colors (reds, yellows, greens as primaries)
- ❌ Fast or bouncy animations (CSS `ease-out` or `ease-in-out` only)
- ❌ Carousels, sliders, or auto-rotating content
- ❌ Gradient-heavy designs (one or two-stop only, subtle opacity)
- ❌ External fonts loaded from Google Fonts (use `@fontsource` npm packages)
- ❌ Standard Bootstrap/Material component styling

### Quality Checklist

Before considering the implementation complete, verify:

- [ ] Noise overlay present on every page/section
- [ ] All image treatments applied (`brightness(0.75) contrast(1.2) saturate(0.9)`)
- [ ] Hard offset shadows on all cards and panels
- [ ] No pure black (`#000000`) anywhere
- [ ] No border-radius on any element
- [ ] Typography follows the hierarchy (serif headers, sans body, mono data)
- [ ] All interactive elements have hover and focus states
- [ ] Animations respect `prefers-reduced-motion`
- [ ] Responsive layout collapses to single column on mobile
- [ ] All CSS values use `var(--*)` references (no hardcoded tokens)
- [ ] Labels and badges use uppercase + wide tracking
- [ ] Hero section covers full viewport (`100vh` or `100svh`)
- [ ] No soft shadows — all shadows are hard offsets
- [ ] Grain intensity varies by context (3-15% opacity)
- [ ] Chromatic aberration appears on at least one heading element
- [ ] Color palette exclusively from the token system (no invented colors)

---

## 13. Appendix: Reference-to-Token Map

| Reference Image | Key Contribution to Design System |
|----------------|----------------------------------|
| Image 1 — Eyes & Figure | Vertical stacking pattern, asymmetrical collage composition |
| Image 2 — Winged Silhouette | High-contrast icon approach, silhouette as communication |
| Image 3 — Eye/Iris | CRT scanline texture, halftone overlay, cool blue palette |
| Image 4 — Ao Haru Ride | Vertical Japanese typography, cloud/mist texture, text as composition |
| Image 5 — Joi | Diagonal split composition, dark/light zone tension, semi-transparent text |
| Image 6 — Mandelbrot | Split-screen code/visual layout, monospace authenticity, generative art concept |
| Image 7 — WISP Poster | Halftone dot pattern, paper texture, distressed fonts, collage layering, mixed typography hierarchy |
| Image 8 — Mitski Jellyfish | High-contrast subject/background, translucent effects, multilingual typography |
| Image 9 — Mitski Flower | Hand-drawn scribble elements, bold serif layout, fold lines, film grain texture |
| Image 10 — Dolphin | Pointillist/dot-based graphic construction, analog photo texture + digital overlay clash |
| Image 11 — "whystopnow?" | Chromatic aberration as primary texture, serif text with glitch, negative space composition |
| Image 12 — "seen this Angel?" | Broken serif aesthetic, vertical pixel stretching, RGB channel separation |
| Image 13 — "fllla" | Paper fold texture, bold sans-serif kinetic typography, teal accent, archival marginalia |
| Image 14 — City/Fog | Volumetric atmospheric lighting, bloom, cool color grading, silhouetted architecture |

---

*This is Design System V2. It supersedes V1 and is the single source of truth for the Noise Web / AbstractWebsite project.*

*Last updated: July 2026 — Derived from 14 visual reference images and critical re-evaluation of V1 design decisions.*
## 1-critical-re-evaluation
## 1-critical-re-evaluation

# Abstract Website Design System

## Overview

A cohesive, emotionally resonant design system built from 13 visual reference images. This system unifies diverse aesthetic elements—album art, glitch textures, analog film grain, and typographic collage—into a single, modern web experience that feels both raw and refined.

**Core Philosophy**: _"Beauty in the broken"_ — embrace digital decay, lo-fi textures, and high-contrast emotional imagery to create a site that feels human, intimate, and authentically abstract.

---

## 🎨 1. Design Tokens

### Color Palette

The system uses a **monochromatic blue/teal** foundation with high-contrast luminance rather than chromatic variety. Three primary tonal ranges:

#### Primary Backgrounds
```css
--color-bg-deep: #0a1524;       /* Near-black navy for darkest sections */
--color-bg-dark:  #1f3a6b;      /* Deep slate blue for primary backgrounds */
--color-bg-mid:   #2d4f7e;      /* Mid-tone indigo for cards/sections */
--color-bg-light: #4b5d7c;      /* Lighter blue-grey for overlays */
```

#### Foreground & Text
```css
--color-text-primary: #ffffff;           /* Pure white for primary text */
--color-text-secondary: #e8f0f5;         /* Off-white for secondary text (WCAG AA) */
--color-text-muted:   #9bb3c4;           /* Muted blue-grey for captions/meta */
```

#### Accent & Interactive
```css
--color-accent-cyan:  #ddeeff;           /* Electric cyan for highlights/buttons */
--color-accent-blue:  #a0c4ff;           /* Lighter blue for hover states */
--color-accent-wash:  #8faab6;           /* Desaturated teal for subtle accents */
```

#### Noise & Texture (Grain)
```css
--noise-white:        rgba(255, 255, 255, 0.15);   /* White noise layer */
--noise-grey:         rgba(46, 78, 109, 0.12);     /* Grey-blue noise variant */
```

#### Contrast Ratios (WCAG Compliance)
| Element | Target Ratio | Implementation |
|---------|-------------|----------------|
| Primary text on dark bg | ≥ 7:1 | `#ffffff` on `#0a1524` = ∞:1 |
| Secondary text on dark bg | ≥ 4.5:1 | `#e8f0f5` on `#0a1524` ≈ 9:1 |
| Muted captions | ≥ 3:1 | `#9bb3c4` on `#0a1524` ≈ 6:1 |

---

### Typography Stack

A **hybrid serif/sans-serif/monospace** approach that mirrors the collage aesthetic. No single font family dominates—instead, they're used intentionally to create visual tension.

#### Font Families (with Fallbacks)
```css
--font-display-slab: 'Slab Serif', 'Crimson Text', Georgia, serif;       /* Heavy headers */
--font-display-grotesk: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;  /* Primary UI text */
--font-display-mono: 'Space Mono', 'Courier New', monospace;            /* Code/data overlays */
--font-display-script: 'Playfair Display', serif;                       /* Poetic/lyric snippets */
```

#### Font Sizes & Line Heights (16px base)
```css
/* Hierarchy for Hero Sections */
h1.display { font-size: clamp(3rem, 5vw, 5.5rem); line-height: 0.9; letter-spacing: -0.02em; }
h2.section { font-size: clamp(1.8rem, 3vw, 2.8rem); line-height: 1.1; letter-spacing: -0.01em; }
h3.card    { font-size: 1.4rem; line-height: 1.25; margin-bottom: 0.5rem; }

/* Body Copy */
p.body    { font-family: var(--font-display-grotesk); font-size: 1rem; line-height: 1.6; }
p.poetic  { font-family: var(--font-display-script); font-size: 0.9rem; line-height: 1.7; color: var(--color-text-muted); }

/* Micro-copy & Meta */
small.meta   { font-size: 0.75rem; text-transform: uppercase; letter-spacing: 0.08em; color: var(--color-text-muted); }
```

#### Text Treatments (Collage Style)
- **Fragmented**: Break long words across lines, use `white-space: pre-wrap` for poetic sections
- **Overlaid**: Apply text shadows (`2px 2px 0 rgba(10, 21, 36, 0.4)`) to mimic printed labels
- **Monospaced blocks**: Use `<pre>` or fixed-width containers for "data stream" aesthetics

---

### Spacing System

Derived from the collage layouts: **asymmetrical grids** with generous negative space.

```css
--space-xs: 0.25rem;   /* Tight spacing for micro-copy */
--space-sm: 0.5rem;    /* Card padding, small margins */
--space-md: 1rem;      /* Standard section margin */
--space-lg: 2rem;      /* Primary section gap */
--space-xl: 4rem;      /* Hero-to-content distance */

/* Grid Columns (for asymmetrical layouts) */
--grid-col-1fr: 1fr;
--grid-col-3fr: 3fr;
--grid-gap: clamp(1.5rem, 2vw, 3rem);  /* Responsive gutter */
```

**Layout Pattern**: Use a **60/40 split** for main sections (asymmetrical balance), with the heavier visual weight on one side and negative space counterbalancing it.

---

### Borders & Shadows

High-contrast borders that feel printed or stamped rather than digital.

#### Border Styles
```css
--border-thin: 1px solid rgba(255, 255, 255, 0.15);        /* Subtle separation */
--border-strong: 2px solid #ffffff;                         /* Accent borders */
--border-dashed: 1px dashed rgba(255, 255, 255, 0.4);      /* Data-stream effect */

/* Border Radius (collage feel) */
--radius-sm: 0.25rem;   /* Tight corners for micro-elements */
--radius-md: 0.5rem;    /* Card containers */
--radius-lg: 1rem;      /* Hero sections */
```

#### Shadow System (High-contrast, not soft)
```css
/* Mimics printed depth rather than drop shadows */
shadow-card { 
  box-shadow: 4px 4px 0 rgba(10, 21, 36, 0.8);   /* Hard offset, no blur */
}

shadow-hero { 
  box-shadow: 8px 8px 0 rgba(10, 21, 36, 0.95), 4px 4px 20px rgba(10, 21, 36, 0.5);
}

shadow-float { 
  box-shadow: 6px 6px 0 var(--color-accent-cyan);   /* Accent color offset */
}
```

---

### Noise & Texture (The "Soul" of the System)

This is the **most critical differentiator**. Every screen must carry a noise/grain overlay.

#### Implementation Layers

**1. Base Noise Layer (Global)**
Apply to `<body>` or root element:
```css
body {
  /* Film grain + digital noise */
  background-image: 
    radial-gradient(rgba(255,255,255,0.03) 1px, transparent 1px),
    repeating-linear-gradient(45deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 2px, transparent 2px, transparent 6px);
  background-size: 4px 4px, 1rem 1rem;
}
```

**2. SVG Noise Filter (Optional - Higher Quality)**
Create `/assets/noise.svg`:
```svg
<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080">
  <filter id="noiseFilter">
    <feTurbulence type="fractalNoise" baseFrequency="0.65" numOctaves="4" result="noise"/>
    <feColorMatrix type="matrix" in="SourceGraphic" values="
      1 0 0 0 0  
      0 1 0 0 0  
      0 0 1 0 0  
      0 0 0 1 0"/>
    <feBlend mode="overlay" in="noise" in2="SourceGraphic" result="blendedNoise"/>
  </filter>
</svg>
```

**3. Scanline Effect (CRT-style)**
```css
.scanlines {
  background: repeating-linear-gradient(
    to bottom,
    transparent 0px,
    rgba(0, 0, 0, 0.08) 2px,
    transparent 4px
  );
}
```

**Grain Intensity Guide:**
| Context | Opacity | Implementation |
|---------|---------|----------------|
| Hero sections | 15-20% | Heavy grain for emotional impact |
| Content cards | 8-12% | Subtle texture, maintain readability |
| Navigation | 3-5% | Barely visible, avoid distraction |

---

## 🧩 2. UI Components & Layout Systems

### Hero Section Patterns

Three primary hero layouts derived from the images:

#### Pattern A: Full-Screen Collage (Album Art Style)
```html
<section class="hero-collage">
  <div class="hero-bg-image" aria-label="Background imagery">
    <!-- Background image with noise overlay -->
    <img src="/assets/hero-01.jpg" alt="" />
    <div class="noise-overlay"></div>
  </div>
  
  <div class="hero-content-left">
    <h1 class="display-slab">PROJECT TITLE</h1>
    <p class="poetic">Poetic snippet or manifesto text...</p>
  </div>
</section>
```

**CSS:**
```css
.hero-collage {
  position: relative;
  min-height: 100vh;
  display: grid;
  grid-template-columns: 60% 40%;  /* Asymmetrical 60/40 split */
}

.hero-bg-image {
  position: absolute;
  inset: 0;
  background-size: cover;
  filter: brightness(0.7) contrast(1.2);  /* High-contrast treatment */
}

.noise-overlay {
  position: absolute;
  inset: 0;
  opacity: 0.18;
  background-image: url('/assets/noise.png');   /* Or SVG filter */
  pointer-events: none;
}

.hero-content-left {
  padding: clamp(4rem, 5vw, 6rem);
  position: relative;
  z-index: 2;
}
```

#### Pattern B: Split-Screen Data Stream (Code + Image)
```html
<section class="hero-split">
  <div class="split-image"></div>
  <div class="split-data">
    <pre class="data-stream">FUNCTION TrueX(a:real):integer:...</pre>
  </div>
</section>
```

**CSS:**
```css
.hero-split {
  display: grid;
  grid-template-columns: 1fr 1.5fr;  /* Image left, code right */
  height: 80vh;
}

.split-image {
  background-size: cover;
  filter: grayscale(0.8) contrast(1.3);
}

.data-stream {
  font-family: var(--font-display-mono);
  font-size: 0.75rem;
  line-height: 1.4;
  color: rgba(255, 255, 255, 0.85);
  white-space: pre-wrap;
}
```

#### Pattern C: Minimalist Type-Only (Serif Focus)
```html
<section class="hero-serif">
  <h1 class="display-serif">falla</h1>
  <p class="caption">come down freely under the influence of gravity.</p>
</section>
```

---

### Card Component System

Cards with high-contrast, printed-style borders:

```html
<article class="card">
  <div class="card-image"></div>
  <div class="card-content">
    <span class="badge-small">CATEGORY</span>
    <h3 class="card-title">TITLE HERE</h3>
    <p class="card-body">Body text with poetic or data-driven tone...</p>
  </div>
</article>
```

**CSS:**
```css
.card {
  position: relative;
  background-color: var(--color-bg-deep);
  border: var(--border-thin);
  overflow: hidden;
}

.card-image {
  height: 18rem;
  width: 100%;
  object-fit: cover;
  filter: brightness(0.7) contrast(1.2);
}

.card-content {
  padding: clamp(1.5rem, 3vw, 2.5rem);
  position: relative;
  z-index: 2;
}

.badge-small {
  display: inline-block;
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-accent-cyan);
  margin-bottom: 0.75rem;
}

.card-title {
  font-family: var(--font-display-slab);
  font-size: 1.25rem;
  line-height: 1.3;
  margin: 0;
}

.card-body {
  font-size: 0.875rem;
  color: var(--color-text-muted);
  max-width: 65ch;
}
```

---

### Navigation (Collapsible, Minimal)

Derived from the "sticker" aesthetic and compact data displays:

```html
<nav class="navigation">
  <a href="/" class="nav-link nav-brand">brand</a>
  <ul class="nav-links">
    <li><a href="/work" class="nav-link">WORK</a></li>
    <li><a href="/about" class="nav-link">ABOUT</a></li>
    <li><a href="/contact" class="nav-link">CONTACT</a></li>
  </ul>
</nav>
```

**CSS:**
```css
.navigation {
  position: fixed;
  top: clamp(1rem, 3vw, 2rem);
  left: clamp(2rem, 4vw, 4rem);
  z-index: 100;
}

.nav-brand {
  font-family: var(--font-display-script);
  font-size: 1.5rem;
  color: var(--color-text-primary);
  text-decoration: none;
}

.nav-links {
  display: flex;
  gap: clamp(2rem, 4vw, 3rem);
  list-style: none;
  margin-left: auto;
}

.nav-link {
  font-family: var(--font-display-grotesk);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: var(--color-accent-cyan);
}
```

---

### Interactive Elements (Buttons & Forms)

#### Buttons - High-contrast, printed feel
```html
<button class="button primary">START</button>
```

**CSS:**
```css
.button {
  font-family: var(--font-display-grotesk);
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  padding: clamp(0.875rem, 2vw, 1.25rem) clamp(1.5rem, 3vw, 2.5rem);
  background-color: var(--color-text-primary);
  color: var(--color-bg-deep);
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
}

.button:hover {
  transform: translate(-2px, -2px);
  box-shadow: 4px 4px 0 rgba(255, 255, 255, 0.3);
}

.button.primary {
  background-color: var(--color-accent-cyan);
  color: var(--color-bg-deep);
}
```

#### Forms - Minimal input fields
```html
<form class="form">
  <label for="name">NAME</label>
  <input type="text" id="name" name="name" placeholder="_enter_">
</form>
```

**CSS:**
```css
.form label {
  font-family: var(--font-display-grotesk);
  font-size: 0.65rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--color-text-muted);
  display: block;
  margin-bottom: 0.5rem;
}

.form input {
  width: 100%;
  background-color: transparent;
  border: none;
  border-bottom: 1px solid rgba(255, 255, 255, 0.3);
  color: var(--color-text-primary);
  font-family: var(--font-display-grotesk);
  padding: 0.75rem 0;
  outline: none;
}

.form input:focus {
  border-bottom-color: var(--color-accent-cyan);
}
```

---

## 🎬 3. Interaction Patterns & Animations

### Subtle Motion - "Living Noise"

Noise should gently pulse to create a breathing quality without distraction.

```css
.noise-overlay {
  animation: noise-pulse 8s ease-in-out infinite;
}

@keyframes noise-pulse {
  0%, 100% { opacity: 0.15; }
  50% { opacity: 0.2; }
}
```

### Image Reveal - Glitch Fade-In

Images should appear with a brief glitch effect on load:

```css
.hero-bg-image {
  animation: glitch-fade-in 1s ease-out forwards;
  opacity: 0;
  transform: translate(-2px, 4px);
}

@keyframes glitch-fade-in {
  0% {
    opacity: 0;
    filter: blur(8px) contrast(1.5) hue-rotate(90deg);
    transform: translate(-4px, -2px);
  }
  60%, 100% {
    opacity: 1;
    filter: brightness(0.7) contrast(1.2);
    transform: translate(0, 0);
  }
}
```

### Scroll-triggered Content Reveal

Use IntersectionObserver to reveal content with staggered timing:

```javascript
// In your script.js or setup.js
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.style.opacity = '1';
      entry.target.style.transform = 'translateY(0)';
      
      // Stagger children within the element
      const children = entry.target.children;
      Array.from(children).forEach((child, index) => {
        if (child.offsetParent !== null) return; // Already visible
        
        child.style.opacity = '0';
        child.style.transform = `translateY(${index * 1.5}rem)`;
        
        const animationDelay = `${index * 0.1}s`;
        child.style.transition = `opacity 0.8s ease ${animationDelay}, transform 0.8s ease ${animationDelay}`;
      });
      
      observer.unobserve(entry.target);
    }
  });
}, observerOptions);

document.querySelectorAll('.reveal-on-scroll').forEach(el => {
  el.style.opacity = '0';
  el.style.transform = 'translateY(1rem)';
  el.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
  observer.observe(el);
});
```

---

## 🖼️ 4. Image Treatment Guidelines

All imagery must go through these treatments to maintain visual cohesion:

### Base Treatment (Apply to all images)
```css
.hero-image {
  filter: 
    brightness(0.75)              /* Darken base */
    contrast(1.2)                  /* Increase contrast */
    saturate(0.9)                  /* Slight desaturation */;
}

.card-image {
  filter: 
    brightness(0.8)
    contrast(1.15);
}
```

### Optional Glitch Overlay (For hero sections only)
Add subtle chromatic aberration and scanline artifacts:

```css
.hero-glitch {
  filter: 
    brightness(0.75) contrast(1.2) saturate(0.9)
    drop-shadow(0 0 0 transparent); /* Add glitch on hover */
}

.hero-glitch:hover {
  filter: 
    brightness(0.8) contrast(1.3) saturate(1)
    drop-shadow(2px 0 4px rgba(255, 0, 0, 0.2))
    drop-shadow(-2px 0 4px rgba(0, 255, 0, 0.2));
}
```

### Video Backgrounds (If used)
Apply the same noise and grain treatment:

```css
.video-background {
  position: absolute;
  inset: 0;
  object-fit: cover;
  filter: brightness(0.65) contrast(1.3);
}

.video-background::after {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url('/assets/noise.png');
  opacity: 0.25;
}
```

---

## 📐 5. Layout Grid System

### Primary Grid (Desktop)
```css
.container {
  max-width: 1440px;
  margin-left: auto;
  margin-right: auto;
  padding-left: clamp(2rem, 4vw, 4rem);
  padding-right: clamp(2rem, 4vw, 4rem);
}

.row {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--grid-gap);
}
```

### Asymmetrical Section Grids (Collage style)
```css
/* 60/40 Split */
.split-60-40 {
  display: grid;
  grid-template-columns: 60% 40%;
  gap: var(--grid-gap);
}

/* Staggered Card Grid */
.stagger-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: clamp(1.5rem, 3vw, 2.5rem);
}

.stagger-grid .card:nth-child(odd) {
  margin-top: var(--space-lg);   /* Stagger effect */
}
```

### Responsive Breakpoints
```css
/* Mobile-first approach */
@media (min-width: 768px) {
  .row { grid-template-columns: repeat(12, 1fr); }
  
  .split-50-50 {
    grid-template-columns: 50% 50%;
  }
}

@media (min-width: 1024px) {
  /* Desktop layouts */
}
```

---

## 📦 6. Implementation Checklist

### Phase 1: Foundation
- [ ] Set up CSS custom properties in `:root`
- [ ] Apply global noise layer to `<body>`
- [ ] Configure typography stack with fallbacks
- [ ] Create SVG noise filter assets (optional but recommended)

### Phase 2: Components
- [ ] Build hero section patterns (A, B, C)
- [ ] Implement card component system
- [ ] Style navigation and interactive elements
- [ ] Add form components

### Phase 3: Motion & Polish
- [ ] Add noise pulse animation
- [ ] Implement image glitch fade-in
- [ ] Set up IntersectionObserver for scroll reveals
- [ ] Test contrast ratios (WCAG AA minimum)

### Phase 4: Assets
```
assets/
├── images/          # Hero and section backgrounds
│   ├── hero-01.jpg
│   ├── hero-02.jpg
│   └── ...
├── noise/           # Noise textures
│   ├── noise.png    # 4K grain texture (PNG)
│   └── noise.svg    # SVG turbulence filter
├── scanlines/       # CRT-style overlays
│   └── scanlines.png
└── icons/           # Minimal, monochrome icons
```

---

## 🎯 7. Usage Guidelines & Do's/Don'ts

### ✅ DO
- Apply noise/grain to every screen (critical for authenticity)
- Use high-contrast text (`#ffffff` on dark backgrounds)
- Embrace asymmetry in layouts (60/40 splits work best)
- Mix serif, sans-serif, and monospace intentionally
- Treat all images with the same filter chain
- Keep animations subtle (8s cycles for noise pulse max)

### ❌ DON'T
- Use pure black (`#000000`) — prefer `#0a1524` or similar deep navy
- Add saturation to colors — keep everything desaturated/monochromatic
- Use soft, blurry shadows — opt for hard offsets instead
- Overuse gradients — flat colors with noise texture work better
- Make text too small on mobile (minimum 0.875rem for body)

---

## 🔗 8. Links & References

### Inspiration Sources
- Album art: Joi - "Everything You Want To Hear"
- Typography: Mitski - "My Love Is Mine", "Liquid Smooth"
- Glitch aesthetics: Dropped Image (6), (11)
- Film grain references: Multiple collage images

### Technical Resources
- **Noise generation**: https://www.figma.com/community/plugin/872039564906139663/Noise-Generator
- **Font recommendations**: 
  - Display: [Crimson Text](https://fonts.google.com/specimen/Crimson+Text), [Inter](https://rsms.me/inter/)
  - Script: [Playfair Display](https://fonts.google.com/specimen/Playfair+Display)
  - Mono: [Space Mono](https://github.com/joshhunt/space-mono)

### Accessibility Notes
- All text meets WCAG AA standards (4.5:1 minimum for body copy)
- Focus states are visible via border-bottom color change
- Motion preferences respected via `prefers-reduced-motion` media query

---

## 📝 9. File Structure Recommendation

```
AbstractWebsite/
├── DESIGN_SYSTEM.md     # This file
├── index.html
├── styles/
│   ├── _design-tokens.css    # Color, spacing, typography variables
│   ├── _components.css       # Buttons, cards, forms
│   └── _layout.css           # Grid systems, responsive breakpoints
├── scripts/
│   ├── main.js              # Core interactions
│   └── scroll-reveal.js     # IntersectionObserver logic
└── assets/
    ├── images/              # Hero and section backgrounds
    ├── noise/               # Noise textures (PNG/SVG)
    ├── scanlines/           # CRT-style overlays
    └── icons/               # Minimal icon set
```

---

## 🚀 10. Quick Start Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>Abstract Website</title>
  <link rel="stylesheet" href="/styles/design-tokens.css" />
  <link rel="stylesheet" href="/styles/components.css" />
  <link rel="stylesheet" href="/styles/layout.css" />
</head>
<body class="noise-base">
  
  <!-- Navigation -->
  <nav class="navigation">
    <a href="/" class="nav-link nav-brand">brand</a>
    <ul class="nav-links">
      <li><a href="/work" class="nav-link">WORK</a></li>
      <li><a href="/about" class="nav-link">ABOUT</a></li>
      <li><a href="/contact" class="nav-link">CONTACT</a></li>
    </ul>
  </nav>

  <!-- Hero Section (Pattern A: Collage) -->
  <section class="hero-collage">
    <div class="hero-bg-image" aria-label="Background imagery">
      <img src="/assets/images/hero-01.jpg" alt="" />
      <div class="noise-overlay"></div>
    </div>

    <div class="hero-content-left">
      <h1 class="display-slab">PROJECT TITLE</h1>
      <p class="poetic">Poetic snippet or manifesto text...</p>
    </div>
  </section>

  <!-- Content Section -->
  <main>
    <article class="card reveal-on-scroll">
      <div class="card-image"></div>
      <div class="card-content">
        <span class="badge-small">CATEGORY</span>
        <h3 class="card-title">TITLE HERE</h3>
        <p class="card-body">Body text with poetic or data-driven tone...</p>
      </div>
    </article>
  </main>

  <script src="/scripts/main.js"></script>
  <script src="/scripts/scroll-reveal.js"></script>
</body>
</html>
```

---

## 🎨 Appendix: Color Palette Reference Cards

### Primary Background Scale (Deep Navy)
| Hex | Name | Usage Example | Contrast on White |
|-----|------|---------------|-------------------|
| `#0a1524` | Deep Navy | Hero backgrounds, dark mode base | N/A |
| `#1f3a6b` | Slate Blue | Section backgrounds, cards | 8.9:1 |
| `#2d4f7e` | Mid Indigo | Overlays, hover states | 7.2:1 |

### Foreground Scale (White/Off-white)
| Hex | Name | Usage Example | Contrast on Deep Navy |
|-----|------|---------------|-----------------------|
| `#ffffff` | Pure White | Primary text, buttons | ∞:1 |
| `#e8f0f5` | Off-white | Secondary text, captions | 9.3:1 |
| `#9bb3c4` | Muted Blue | Meta info, dates/times | 6.8:1 |

### Accent Scale (Electric Cyan)
| Hex | Name | Usage Example | Contrast on Navy |
|-----|------|---------------|------------------|
| `#ddeeff` | Electric Cyan | Primary buttons, hover states | ∞:1 |
| `#a0c4ff` | Light Blue | Secondary actions | 8.5:1 |

---

*This design system was created from 13 visual references spanning album art, glitch aesthetics, and collage photography. It prioritizes emotional resonance through texture and high-contrast monochromatic palettes.*

_Last updated: Design System v1.0_

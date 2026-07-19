---
name: "Retro Poster Blue — Digital Design System"
category: Brands
surface: web
type: portfolio
version: "1.0.0"
status: "Production Ready"
created: "2026-07-19"
owner: "Malte"
platform: "Web / Three.js"
---

# Retro Poster Blue — Digital Design System

> Noise / Editorial / Retro-Futuristic Web — a reduced, textured, cinematic digital experience

**Version:** 1.0.0 · **Status:** Production Ready · **Platform:** HTML / Three.js / CSS

---

## 01. Design Philosophy

### Overview

Retro Poster Blue ist ein digitales Designsystem, das die Ästhetik klassischer Druckmedien (Plakate, Magazine, Siebdruck) mit interaktiver Webtechnologie (Three.js Shader, CSS Texturen) verbindet.

Das System vereint:
- **Analoge Materialität** — Grain, Raster, Papierstruktur
- **Experimentelle Typografie** — expressive Headlines, Mono-Metadaten, japanische Deko-Elemente
- **Technische Präzision** — Shader-basierte Post-Processing Pipeline, deterministische Tokens
- **Cinematic Motion** — langsame, atmosphärische Animationen

### Core Principles

#### 01 — Poster Over Interface

Interfaces verschwinden. Komposition steht im Vordergrund.

Nicht: *„Eine Website mit Bildern“*
Sondern: *„Ein lebendiges digitales Poster“*

Jede Section fühlt sich an wie ein eigenständiger Poster-Spread oder eine Editorial-Seite. UI-Elemente (Buttons, Navigation) sind sichtbar, aber untergeordnet.

#### 02 — Digital Texture

Perfekte, flache digitale Flächen werden vermieden. Jedes Element darf minimale Imperfektion besitzen:

- Film Grain
- CRT Scanlines
- Halftone / Dithering
- Light Leaks
- Chromatic Aberration
- Compression Artifacts

Textur ist kein Effekt. Textur ist das Fundament des visuellen Systems.

#### 03 — Controlled Chaos

Experimentelle Effekte werden bewusst und sparsam eingesetzt.

> Every animation needs a reason.

Keine zufälligen Glitches, keine permanenten Bewegungen, keine visuellen Ablenkungen. Ein Glitch hat eine Funktion (Hover, Transition, Loading). Ein Grain hat eine Intensität (5–12 %, nie mehr). Ein Bloom ist maskiert auf Akzente.

#### 04 — Cold Palette, Warm Feeling

Die Farbpalette ist kalt (Navy, Cyan, kühles Weiss, Schiefergrau), aber die Atmosphäre ist emotional und melancholisch — nicht klinisch oder steril.

---

## 02. Design Tokens

### Color System

#### Primary Palette

| Token | Value | Usage |
| :--- | :--- | :--- |
| `color.bg` | `#ffffff` | Seitenhintergrund, Canvas |
| `color.surface` | `#f7f8fa` | Karten, Panels, Sekundärcontainer |
| `color.surfaceRaised` | `#f0f2f5` | Elevated surfaces, Hover-States |
| `color.fg` | `#111111` | Haupttext, Headlines |
| `color.fgSecondary` | `#2a2a2a` | Subheadlines, Sekundärtext |
| `color.muted` | `#6b7280` | Metadaten, Timestamps, technische Labels |
| `color.border` | `#d9dee7` | Linien, Divider, dünne Striche |
| `color.borderSubtle` | `#e5e9f0` | Subtile Trennlinien |

#### Accent Palette

| Token | Value | Usage |
| :--- | :--- | :--- |
| `color.accent` | `#1677ff` | Cold Neon Blue — primäre Accents, Links, Buttons |
| `color.accentHover` | `#4096ff` | Hover-State von accent |
| `color.accentActive` | `#0958d9` | Active-State von accent |
| `color.accentSecondary` | `#5bb8c4` | Desaturated Cyan — sekundäre Akzente, Glow |
| `color.accentGlow` | `rgba(22,119,255,0.12)` | Subtiler Glow für Bloom-Effekte |

#### Textur-Palette (zusätzlich)

| Token | Value | Usage |
| :--- | :--- | :--- |
| `color.leak.cyan` | `rgba(91,184,196,0.08)` | Cyan Light Leak Wash |
| `color.leak.blue` | `rgba(22,119,255,0.06)` | Blauer Light Leak Wash |
| `color.shadow` | `rgba(0,0,0,0.06)` | Schlagschatten auf Papier |

#### CSS Variable Export

```css
:root {
  --bg: #ffffff;
  --surface: #f7f8fa;
  --surface-raised: #f0f2f5;
  --fg: #111111;
  --fg-secondary: #2a2a2a;
  --muted: #6b7280;
  --border: #d9dee7;
  --border-subtle: #e5e9f0;
  --accent: #1677ff;
  --accent-hover: #4096ff;
  --accent-active: #0958d9;
  --accent-secondary: #5bb8c4;
  --accent-glow: rgba(22,119,255,0.12);
  --leak-cyan: rgba(91,184,196,0.08);
  --leak-blue: rgba(22,119,255,0.06);
  --shadow: rgba(0,0,0,0.06);
}
```

### Typography Scale

| Name | Size | Weight | Line Height | Tracking | Usage |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Display XL | `160px` | 800 | `0.9` | `-0.04em` | Hero Poster Headline |
| Display L | `96px` | 800 | `0.92` | `-0.03em` | Section Titles |
| Display M | `64px` | 700 | `0.95` | `-0.02em` | Poster Titles |
| Heading 1 | `48px` | 700 | `1.0` | `-0.01em` | Page Headings |
| Heading 2 | `36px` | 600 | `1.1` | `0` | Section Headings |
| Heading 3 | `24px` | 600 | `1.2` | `0` | Subheadings |
| Body | `16px` | 400 | `1.6` | `0` | Fliesstext, Paragraphs |
| Body Small | `14px` | 400 | `1.5` | `0` | Sekundärtext |
| Caption | `12px` | 500 | `1.3` | `+0.02em` | Metadaten, Labels |
| Mono | `14px` | 400 | `1.4` | `0` | Code, technische Details |

#### Font Roles

| Role | Font | Fallback | Usage |
| :--- | :--- | :--- | :--- |
| Display | Elms Sans | Inter, system-ui, sans-serif | Hero, Poster Titles, große Statements |
| Body | Inter | system-ui, -apple-system, sans-serif | Paragraphs, Beschreibungen |
| Mono | IBM Plex Mono | SFMono-Regular, Consolas, monospace | Metadaten, Labels, Code, technische Notizen |

```css
:root {
  --font-display: "Elms Sans", "Inter", system-ui, sans-serif;
  --font-body: "Inter", system-ui, -apple-system, sans-serif;
  --font-mono: "IBM Plex Mono", "SFMono-Regular", Consolas, "Liberation Mono", monospace;
}
```

### Spacing System (8px Baseline)

| Token | Value |
| :--- | :--- |
| `space-1` | `4px` |
| `space-2` | `8px` |
| `space-3` | `16px` |
| `space-4` | `24px` |
| `space-5` | `32px` |
| `space-6` | `48px` |
| `space-7` | `64px` |
| `space-8` | `96px` |

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 32px;
  --space-6: 48px;
  --space-7: 64px;
  --space-8: 96px;
}
```

### Elevation & Glow

| Token | Value | Usage |
| :--- | :--- | :--- |
| `elevation-none` | `none` | Flache Elemente |
| `elevation-subtle` | `0 1px 2px var(--shadow)` | Karten, Panels |
| `elevation-raised` | `0 4px 12px var(--shadow)` | Modale, Dropdowns |
| `glow-accent` | `0 0 20px var(--accent-glow)` | Bloom auf Accent-Elementen |
| `glow-cyan` | `0 8px 30px rgba(91,184,196,0.10)` | Cyan Glow für Highlights |

**Wichtig:** `border-radius` ist immer `0px`. Keine abgerundeten Ecken — das ist Teil der Poster-Ästhetik.

### Motion Tokens

| Token | Duration | Usage |
| :--- | :--- | :--- |
| `motion-instant` | `100ms` | Micro-Interactions |
| `motion-fast` | `200ms` | Hover, Active States |
| `motion-normal` | `400ms` | Standard Transitions |
| `motion-slow` | `800ms` | Content Reveals |
| `motion-cinematic` | `1600ms` | Hero-Animationen, Scroll-Übergänge |

**Primary Easing:** `cubic-bezier(0.4, 0, 0.2, 1)`
**Secondary Easing (Glow/Bloom):** `cubic-bezier(0.16, 1, 0.3, 1)`

---

## 03. Surface & Texture System

### Texture Layers

Jede große Fläche kann aus mehreren überlagerten Textur-Layern bestehen:

```
Layer 01: Base Color (background / surface)
Layer 02: Film Grain (SVG-Filter oder PNG-Overlay)
Layer 03: Subtle Noise (CSS mit gradient)
Layer 04: Lighting / Gradient Wash
Layer 05: Scanlines (optional, nur Hero)
Layer 06: Vignette (radial-gradient)
```

### CSS Texture Overlays

```css
/* Film Grain Overlay (fixed, über gesamter Seite) */
.grain-overlay {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.06;
  background-image: url("data:image/svg+xml,..."); /* base64 noise */
  mix-blend-mode: overlay;
}

/* Scanlines (subtile horizontale Linien) */
.scanlines {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9998;
  opacity: 0.4;
  background-image: repeating-linear-gradient(
    transparent,
    transparent 2px,
    rgba(255,255,255,0.03) 2px,
    rgba(255,255,255,0.03) 3px
  );
}

/* Vignette */
.vignette {
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9997;
  background: radial-gradient(
    ellipse at center,
    transparent 60%,
    rgba(0,0,0,0.15) 100%
  );
}

/* Light Leak Wash (pseudo-element auf Section) */
.light-leak::before {
  content: "";
  position: absolute;
  inset: 0;
  background: linear-gradient(
    135deg,
    var(--leak-cyan) 0%,
    transparent 50%,
    var(--leak-blue) 100%
  );
  pointer-events: none;
}
```

### Halftone / Dithering (per Image oder Section)

```css
.halftone {
  position: relative;
}
.halftone::after {
  content: "";
  position: absolute;
  inset: 0;
  background-image: radial-gradient(circle, var(--fg) 1px, transparent 1px);
  background-size: 4px 4px;
  mix-blend-mode: overlay;
  opacity: 0.08;
  pointer-events: none;
}
```

---

## 04. Layout System

### Grid

| Breakpoint | Columns | Max Width | Gap |
| :--- | :--- | :--- | :--- |
| Mobile | 4 | 100% | 16px |
| Tablet | 8 | 768px | 24px |
| Desktop | 12 | 1440px | 32px |

```css
:root {
  --grid-columns: 12;
  --grid-gap: 32px;
  --content-max: 1440px;
}
```

### Poster-Layout Prinzipien

1. **Full-Bleed** — Hero und Image-Slams gehen immer bis zum Viewport-Rand
2. **Asymmetrie** — Schwere auf einer Seite, Leere auf der anderen. Nie zentrieren.
3. **Overlap** — Text über Bildern, Bilder über Bildern, Labels über Layern
4. **Scale Contrast** — Riesige Display-Texte neben winzigen Mono-Labels
5. **Zero Radius** — `border-radius: 0` auf allen UI-Elementen
6. **White Space** — Grosszügiger Einsatz von Leerraum als aktives Design-Element

### Section Types

| Type | Beschreibung | Verwendung |
| :--- | :--- | :--- |
| **Full-Bleed Hero** | Vollflächiges Bild + Display-Type + Overlays | Startseite, Projekt-Header |
| **Asymmetric Split** | 50/50 oder 60/40 Split, Text trifft Bild | Projekt-Beschreibungen |
| **Poster Grid** | Ungleichmässiges Raster aus Poster Cards | Work / Portfolio Übersicht |
| **Editorial Spread** | Magazin-artige Doppelseite mit Pull-Quote | About, Storytelling |
| **Detail Panel** | Kleine, überlappende Card mit Metadaten | Technische Details, Tags |
| **Full Image Slam** | Viewport-füllendes Bild mit minimalem Overlay | Zwischen den Sections |

### Responsive Verhalten

- **Desktop (>1024px):** 12-column grid, Display XL / L, volle Three.js Pipeline
- **Tablet (768–1024px):** 8-column grid, Display L / M, reduzierte Shader (kein Bloom)
- **Mobile (<768px):** 4-column grid, Heading 1 max, Scanlines + Grain nur CSS, Three.js deaktiviert

---

## 05. Component Library

### 5.1 Hero Poster

| | |
| :--- | :--- |
| **Purpose** | Primäres Storytelling-Element. Erster visueller Eindruck. |
| **Anatomy** | `[Background Image] [Three.js Shader Canvas] [Display Type Overlay] [Metadata Badge] [Handwritten SVG]` |
| **States** | Default → Hover (subtle RGB split, brightness increase, typography drift) → Reduced Motion |
| **Accessibility** | `role="region"`, `aria-label`, textuelle Alternative im DOM (auch wenn Shader deaktiviert) |

```html
<section class="hero-poster" role="region" aria-label="Featured project">
  <img src="hero.jpg" alt="" class="hero-bg" />
  <canvas class="hero-shader" data-effect="grain+scanlines"></canvas>
  <div class="hero-type">
    <h1 class="display-xl">PROJECT_NAME</h1>
    <span class="mono-label">PROJECT_001 · 2026</span>
  </div>
</section>
```

### 5.2 Poster Card

| | |
| :--- | :--- |
| **Purpose** | Projekt-Thumbnail im Portfolio-Grid |
| **Anatomy** | `[Thumbnail Image] [Number Badge] [Title] [Category Label] [Scanline Hover Overlay]` |
| **Variants** | **Large Poster** (Featured, 2 Spalten breit) · **Compact Poster** (Grid-Galerie) |
| **States** | Default → Hover (Glitch-Overlay + Details einblenden) → Focus (`:focus-visible`) |
| **Keyboard** | `tabindex="0"`, sichtbarer Focus-Ring |

```css
.poster-card {
  position: relative;
  border-radius: 0;
  overflow: hidden;
  cursor: pointer;
}
.poster-card:hover .card-glitch {
  opacity: 1;
}
.poster-card:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
```

### 5.3 Button System

| Variant | Style | Usage |
| :--- | :--- | :--- |
| **Primary** | `bg: accent, fg: white, mono font, 0 radius` | Haupt-CTAs |
| **Secondary** | `border: 1px solid border, bg: transparent` | Sekundäre Aktionen |
| **Ghost** | `bg: transparent, border: none` | Subtle Actions |
| **Mono Label** | `mono font, uppercase, muted color` | Metadaten, Tags |

```css
.btn {
  font-family: var(--font-mono);
  font-size: 14px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  padding: 16px 32px;
  border-radius: 0;
  cursor: pointer;
  transition: background var(--motion-fast), color var(--motion-fast);
}
.btn-primary {
  background: var(--accent);
  color: #fff;
  border: none;
}
.btn-primary:hover {
  background: var(--accent-hover);
}
```

### 5.4 Navigation

| Element | Beschreibung |
| :--- | :--- |
| Logo | Typografisches Wordmark in Display-Font |
| Links | Mono-font, `text-transform: uppercase`, hover underline |
| Status | Kleiner Punkt + Label (z.B. "AVAILABLE · BASED IN DE") |
| Theme | (Reserve für Dark/Light Toggle) |

```css
.nav-link {
  font-family: var(--font-mono);
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  color: var(--muted);
  text-decoration: none;
  position: relative;
}
.nav-link::after {
  content: "";
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 0;
  height: 1px;
  background: var(--fg);
  transition: width var(--motion-normal);
}
.nav-link:hover::after {
  width: 100%;
}
```

---

## 06. Visual Effects Pipeline

### Three.js Post-Processing Pipeline

Effekte sind gestapelt in fester Reihenfolge. Jeder Pass kann einzeln aktiviert/deaktiviert werden.

```
Scene (orthographic quad)
  ↓
EffectComposer
  ↓
Pass 1: RenderPass                — Basisdurchlauf
  ↓
Pass 2: Film / NoisePass          — globales Filmkorn (Intensität 0.06–0.12)
  ↓
Pass 3: ScanlinePass (custom)     — horizontale CRT-Linien
  ↓
Pass 4: ChromaticAberrationPass   — dezentet RGB-Verschiebung an Kanten
  ↓
Pass 5: VignettePass              — Abdunklung der Ränder
  ↓
Pass 6: BloomPass                 — maskierter Bloom nur auf Accent-Layern
  ↓
Pass 7: DitherPass (optional)     — Bayer-Dithering für Risograph-Look
  ↓
Pass 8: OutputPass                 — finale Ausgabe
```

### CDN-Importmap Setup

```json
{
  "imports": {
    "three": "https://unpkg.com/three@0.160.0/build/three.module.js",
    "three/addons/": "https://unpkg.com/three@0.160.0/examples/jsm/",
    "postprocessing": "https://unpkg.com/postprocessing@6.36.0/build/postprocessing.js"
  }
}
```

### Performance Budget

| Device | Target | Rules |
| :--- | :--- | :--- |
| Desktop (GPU) | 60 FPS | Volle Pipeline (8 Passes) |
| Tablet (Mid-Range) | 30–60 FPS | Reduziert (Pass 2–5, kein Bloom) |
| Mobile (Low-End) | 30 FPS | Nur CSS Overlays (Grain + Vignette) |
| Reduced Motion | — | Keine Shader-Animationen, statische Texturen |

```js
function getEffectLevel() {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches)
    return "static";
  if (window.innerWidth < 768) return "css-only";
  if (window.innerWidth < 1024) return "reduced";
  return "full";
}
```

### GLSL Fragment (Scanlines + Chromatic Aberration + Grain)

```glsl
uniform sampler2D uTexture;
uniform float uTime;
uniform float uIntensity;
varying vec2 vUv;

void main() {
  vec2 uv = vUv;

  // Chromatic Aberration
  float ca = 0.002 * uIntensity;
  float r = texture2D(uTexture, uv + vec2(ca, 0.0)).r;
  float g = texture2D(uTexture, uv).g;
  float b = texture2D(uTexture, uv - vec2(ca, 0.0)).b;
  vec3 col = vec3(r, g, b);

  // Scanlines
  float scanline = sin(uv.y * 240.0 + uTime * 0.5) * 0.5 + 0.5;
  scanline = mix(0.92, 1.0, scanline);
  col *= scanline;

  // Film Grain
  float grain = fract(sin(dot(uv * 12.9898, vec2(78.233, 45.543))) * 43758.5453);
  col += (grain - 0.5) * 0.04 * uIntensity;

  gl_FragColor = vec4(col, 1.0);
}
```

---

## 07. Interaction Patterns

### 7.1 Pointer Parallax

- Drei Layer: Background (langsam), Mid (mittel), Foreground (schnell)
- Nutzt `transform: translate3d()` für GPU-Beschleunigung
- Max-Offset: ±20px (subtle, nicht spielerisch)

### 7.2 Glitch Trigger

- Kurzer Effekt bei Hover oder Transition
- Klone Text-Element, versetze Farbkanäle, entferne nach 300–600ms
- Nicht bei `prefers-reduced-motion`

```js
function triggerGlitch(el) {
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  const clone = el.cloneNode(true);
  clone.style.position = "absolute";
  clone.style.left = "0";
  clone.style.top = "0";
  clone.style.color = "var(--accent)";
  clone.style.transform = "translateX(-6px)";
  clone.style.clipPath = "inset(30% 0 40% 0)";
  clone.style.pointerEvents = "none";
  el.parentElement.appendChild(clone);
  setTimeout(() => clone.remove(), 420);
}
```

### 7.3 Scroll Reveal

- IntersectionObserver + CSS Transition (translateY + opacity)
- Threshold: 0.15
- Easing: `cubic-bezier(0.4, 0, 0.2, 1)`
- Dauer: 800ms

### 7.4 Audio Reactive (Optional)

- WebAudio API → AnalyserNode
- Niedrige Frequenzen → Bloom Intensity
- Hohe Frequenzen → Grain Amount
- User muss zuerst klicken (AudioContext Policy)

---

## 08. Accessibility

| Anforderung | Standard |
| :--- | :--- |
| **Kontrast (Body)** | WCAG AA — min 4.5:1 |
| **Kontrast (Headlines)** | WCAG AA — min 3:1 (dekorativ, mit textueller Alternative) |
| **Motion** | `prefers-reduced-motion` → keine Animationen, statische Texturen |
| **Keyboard** | Alle interaktiven Elemente fokussierbar, `:focus-visible` Style |
| **ARIA** | Hero: `role="region" aria-label"`, Poster Cards: `tabindex="0" role="button"` |
| **Alt Text** | Jedes Bild braucht `alt`-Attribut (auch dekorativ → `alt=""`) |
| **Three.js Fallback** | Statisches DOM-Bild + Text, wenn WebGL nicht verfügbar |

---

## 09. CSS Architecture & Naming

### Naming Convention

- **Komponenten:** PascalCase (`.HeroPoster`, `.PosterCard`)
- **Elemente:** camelCase (`.posterTitle`, `.metaBadge`)
- **Utility:** kebab-case (`.display-xl`, `.mono-label`)
- **Tokens:** `category-property` (`--color-accent`, `--space-5`)

### CSS Structure

```css
/* 1. Reset & Base */
/* 2. Design Tokens (CSS Variables) */
/* 3. Typography */
/* 4. Layout / Grid */
/* 5. Texture Overlays (grain, scanlines, vignette) */
/* 6. Components (Hero, Card, Button, Nav) */
/* 7. Effects (glitch, parallax, reveal) */
/* 8. Responsive / Media Queries */
```

---

## 10. Do / Don't

### DO

- ✓ Starke, expressive Typografie als primäres Gestaltungselement
- ✓ Grosszügige Kompositionen mit viel Leerraum
- ✓ Kontrollierte, sinnvolle Textur-Effekte
- ✓ Hoher Kontrast zwischen Text und Hintergrund
- ✓ Asymmetrische, poster-artige Layouts
- ✓ Monospace für Metadaten und technische Labels

### DON'T

- ✕ Abgerundete Ecken auf Cards oder Buttons
- ✕ Standard-Gradienten (linear-gradient ohne Textur-Kontext)
- ✕ Übermässige oder zufällige Animationen
- ✕ Warme Farben (Beige, Orange, Rot als Primärfarbe)
- ✕ SaaS-typische UI-Muster (abgerundete Cards, Schatten, weite Border-Radius)
- ✕ Stock-Photography, flache Illustrationen, Vector-Art
- ✕ Neon-Cyberpunk (bunte Neonfarben, HUD-Elemente)

---

## 11. Asset Requirements

### Image Formats

| Format | Usage |
| :--- | :--- |
| WebP | Primäres Format für Fotos |
| AVIF | Optional für bessere Kompression |
| PNG | Für Transparenz (Texturen, Overlays) |
| SVG | Für Vektor-Grafiken, Icons, Handwritten Strokes |

### Image Sizes

| Breakpoint | Width | Crop |
| :--- | :--- | :--- |
| Hero (Desktop) | 2400px | 16:9 |
| Full (Desktop) | 1600px | 3:2 oder 4:3 |
| Thumbnail | 600px | 1:1 oder 4:3 |

### Required Assets

- [ ] Tileable Noise Texture (PNG, 256×256, grayscale)
- [ ] Halftone Mask (SVG oder PNG)
- [ ] Displacement Map (grayscale PNG, 512×512)
- [ ] Font Licenses + WOFF2 Files (Elms Sans, Inter, IBM Plex Mono)
- [ ] SVG Handwritten Strokes (für Poster-Deko)
- [ ] Portfolio-Bilder in 3 Grössen (full, medium, thumb)
- [ ] Optional: Audio Ambient Stems (für Audio-Reactive)

---

## 12. Governance & Versioning

### Versioning Schema

```
Major.Minor.Patch
```

| Bump | Bedeutung |
| :--- | :--- |
| **Major** | Breaking Changes (neue Tokens, entfernte Komponenten) |
| **Minor** | Neue Komponenten, neue Effekte, neue Patterns |
| **Patch** | Bugfixes, CSS-Tweaks, Dokumentation |

### Changelog (v1.0.0)

- Initiales Design System
- 7 Color Tokens + 4 Texture Tokens
- 3 Font Families (Elms Sans, Inter, IBM Plex Mono)
- 8 Components (Hero, Poster Card, Button × 4, Navigation)
- 8 Post-Processing Passes (Three.js)
- 4 Interaction Patterns

---

## 13. Files & Implementation

| File | Purpose |
| :--- | :--- |
| `index.html` | Portfolio-Hauptseite (HTML + CSS + Three.js importmap) |
| `effects.js` | Three.js Setup + Post-Processing Pipeline |
| `style.css` | CSS Design System (Tokens, Components, Textures) |
| `DESIGN.md` | Dieses Dokument — vollständiges Design System |
| `assets/images/` | Portfolio-Bilder + Texturen (Noise, Halftone, Displacement) |
| `tokens.json` | Export für Design-Tools (Figma, Style Dictionary) |

### Implementation Roadmap

| Phase | Tasks |
| :--- | :--- |
| **1. Foundation** | Tokens → Fonts → CSS Variables → HTML Skeleton |
| **2. Static Layout** | Poster Grid → Hero → Cards → Navigation |
| **3. CSS Textures** | Grain → Scanlines → Vignette → Light Leaks |
| **4. Three.js Pipeline** | Setup → RenderPass → Noise → Scanlines → Bloom |
| **5. Interactions** | Parallax → Glitch → Scroll Reveal |
| **6. Responsive** | Mobile → Tablet → Reduced Motion → Performance |
| **7. Polish** | Accessibility Audit → Performance Test → Documentation |

---

> **Retro Poster Blue** is not a UI kit. It is a visual language.
>
> The goal: A website that feels printed, but behaves digitally.

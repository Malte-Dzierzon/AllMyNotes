---
name: "# Design Concept –"
category: Brands
surface: web
type: portfolio
purpose: "Interactive retro-poster portfolio website with Three.js post-processing effects"
colors:
  cold-white: "#ffffff"
  blue-tinted-gray: "#f7f8fa"
  black: "#111111"
  muted: "#6b7280"
  border: "#d9dee7"
  cold-neon-blue: "#1677ff"
  desaturated-cyan: "#5bb8c4"
---

# # Design Concept – Portfolio Edition

> Category: Brands | Surface: web | Type: Portfolio

*Noise / Editorial / Retro-Futuristic Web — a reduced, textured, cinematic digital experience*

An interactive portfolio website that looks and feels like a living graphic-design poster. Cold, atmospheric, melancholic — experimental editorial design meets Three.js post-processing effects.

---

## Purpose

This is a **portfolio website**. It showcases work in a way that feels more like flipping through an art-book or standing in front of a poster exhibition than browsing a traditional web portfolio. Each section is its own visual spread.

---

## Tech Stack

| Layer | Technologie | Grund |
|---|---|---|
| Structure | **Pure HTML + CSS** | Kein Framework nötig, maximal AI-freundlich |
| 3D / Effects | **Three.js** (vom CDN via importmap) | Shader, Post-Processing, Bildmanipulation |
| Post-Processing | **postprocessing** npm package (vom CDN) | 15+ fertige Effekte (Bloom, Noise, Scanlines, Chromatic Aberration, Dithering) |
| Build | **Keiner** | CDN-Importe, kein Vite/Webpack/npm |
| Animation Loop | Three.js Render Loop | Scroll-Interaktion über requestAnimationFrame |

Kein React, kein Astro, kein Vue. Eine HTML-Datei + eine effects.js reichen.

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

---

## Color Palette

| Role | Name | Hex | Usage |
| --- | --- | --- | --- |
| background | Cold White | `#ffffff` | Page canvas — the cold white backdrop for editorial layouts |
| surface | Blue-Tinted Gray | `#f7f8fa` | Cards, panels, and secondary containers |
| foreground | Black | `#111111` | Body text, headings, and primary content |
| muted | Muted | `#6b7280` | Secondary text, metadata, technical labels, timestamps |
| border | Border | `#d9dee7` | Rules, dividers, thin strokes |
| accent | Cold Neon Blue | `#1677ff` | Primary actions, links, emphasis — use once or twice per view, never as large wash |
| accent-secondary | Desaturated Cyan | `#5bb8c4` | Secondary accent, subtle decorative elements, accent-text on dark backgrounds |

---

## Typography

- **Display:** Elms Sans — weights 300, 400, 500, 700 — fallbacks: Inter, system-ui, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif
- **Body:** Inter — weights 400, 600, 700 — fallbacks: system-ui, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif
- **Mono:** IBM Plex Mono — weights 100, 200, 300, 400, 500, 600, 700 — fallbacks: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace

---

## Interactive Effects (Three.js Post-Processing Pipeline)

Effects are stacked in order. Each can be toggled/adjusted independently.

### Core Effects (always on)
1. **Film Grain / Noise** — `FilmShader` or custom GLSL noise overlay on the entire page
2. **CRT Scanlines** — Subtle horizontal lines via custom ShaderPass
3. **Vignette** — Radial gradient darkening at screen edges
4. **Chromatic Aberration** — Subtle RGB-split on text and images (like analog capture artifact)

### Optional Effects (per section or on interaction)
5. **Bloom / Glow** — Very restrained `UnrealBloomPass` on accent elements only
6. **Dithering** — Bayer pattern on specific images (like Risograph print effect)
7. **Light Leaks** — Slowly drifting colored gradient overlays (CSS or custom shader)
8. **Grid Distortion** — On hover/scroll, subtle grid displacement on images (see Codrops GridDistortionEffect)
9. **Slow Gradient Animation** — 20s+ color drift in background or accent areas

### Retro Poster Texture Overlays (CSS pseudo-elements)
10. Soft vignette overlay
11. Subtle film grain as `::before` pseudo-element
12. Light leak color washes as overlays on image sections

---

## Portfolio Layout (Poster-Style)

The layout is inspired by **graphic design posters** and **editorial spreads**.

### Section Types
- **Full-bleed hero poster** — Large typography + image + grain overlay, like a concert poster
- **Work grid** — Asymmetric tile layout, not a uniform card grid. Images at different scales
- **Split spreads** — Text on one side, full image on the other (like a magazine)
- **Detail panels** — Small metadata boxes pinned at diagonals or overlapped with images
- **Full-image slams** — A single image filling the viewport, with small text overlay at edge

### Poster-Style Principles
- Asymmetric balance: heavy on one side, whitespace on the other
- Overlapping elements: text over images, images over images
- Everything rectangular: `border-radius: 0px` everywhere
- Scale contrast: tiny metadata next to massive headlines
- Japanese glyphs as decorative texture elements

---

## Voice & Tone

- **Adjectives:** calm, melancholic, futuristic, experimental, editorial, surreal, atmospheric, cinematic, reduced, textured, cold, refined
- **Tone:** Editorial, atmospheric, and emotionally engaging. Reads like a digital art exhibition or experimental magazine — calm but not sleepy, melancholic but not depressing, futuristic but not loud. Avoid playful, overly friendly, or corporate marketing tone. Text is part of the visual composition, not just information delivery.

### Messaging pillars
- Textured digital atmosphere: driven by grain, scanlines, bloom, and analog artifacts rather than flat minimalism
- Cold cinematic palette: restrained navy, cool white, desaturated cyan, and subtle silver glow — never bright neon or warm beige
- Editorial typography: large expressive headlines, asymmetric compositions, generous whitespace, Japanese glyphs as visual texture
- Magazine-inspired layout: free-form composition, layered blocks at different scales, poster-like spreads
- Slow atmospheric motion: floating textures, CRT flicker, gentle parallax — never fast or playful

### Vocabulary
- **Use:** atmosphere, texture, signal, glow, static, drift, echo, noise, transmission, decay, horizon, void, fade, pulse
- **Avoid:** innovative, disruptive, revolutionary, game-changing, cutting-edge, seamless, robust, scalable, user-friendly, next-gen

---

## Imagery

- **Style:** Textures over colors. Grain, noise, scanlines, dithering, halftone patterns, light leaks, bloom, and compression artifacts as primary visual texture. Everything feels slightly imperfect, organic, and aged-digital.
- **Subjects:** Vintage CRT screens and monitor glow, Abstract light and signal artifacts, Cold industrial and architectural spaces, Ambient digital landscapes, Textural abstract compositions, Portfolio work samples
- **Treatment:** Apply film grain overlay, CRT scanline pattern, soft vignette, subtle bloom on light sources, and light leak gradients. Use JPEG/video compression artifacts as stylistic texture. Everything should feel like it was captured through imperfect analog-to-digital conversion.
- **Avoid:** Clean product photography, Flat illustrations, Vector art, Stock corporate imagery, Bright saturated colors, Warm beige tones, Playful or cartoon imagery

---

## Animation & Motion

- **Speed:** Slow, cinematic. Duration 0.3–1.2s. Ease: cubic-bezier(0.4, 0, 0.2, 1)
- **Types:** Noise textures, CRT flicker, gentle parallax, fade transitions, slow bloom pulse
- **Avoid:** Fast animations, bouncy easing, playful motion, auto-scrolling carousels
- **Scroll:** Subtle parallax on images, slow reveal on content blocks via Intersection Observer or Three.js render loop

---

## Files

| Datei | Zweck |
|---|---|
| `index.html` | Portfolio-Hauptseite (HTML + CSS + Three.js importmap) |
| `effects.js` | Three.js-Setup + Post-Processing-Pipeline (optional, kann auch in index.html) |
| `DESIGN.md` | Dieses Dokument — Design-System + Tech-Stack |
| `assets/images/` | Portfolio-Bilder + Texturen |

---
description: "Retro Poster Blue — Digital Design System"
purpose: "Production-ready design system for interactive retro-poster portfolio website with Three.js post-processing"
status: "v1.0.0 — Production Ready"
source: "DESIGN.md + brand toolkit"
---

# web-design-concept

## Overview

**Retro Poster Blue** — Ein vollständiges, produktionsreifes Design System für eine interaktive Portfolio-Webseite im Retro-Poster-Stil. Kombiniert editoriales Grafikdesign mit Three.js Shader-Effekten. Läuft ohne Build-Tools (CDN-Importmap).

Struktur: Philosophy → Foundation (Tokens) → Components → Patterns → Engineering → Governance.

## Files

| File | Size | Purpose |
| :--- | :--- | :--- |
| `DESIGN.md` | 22 KB | Vollständiges Design System (13 Sektionen) |
| `brand.html` | 64 KB | Visueller Brand-Kit-Viewer (zur Überarbeitung) |
| `brand.json` | 12 KB | Strukturierte Brand-Daten |
| `AGENT.md` | — | Diese Datei |
| `imagery/` | 4.7 MB | 4 Referenz-Bilder |

## Design Direction

- **System Name:** Retro Poster Blue
- **Site Type:** Interactive Portfolio — retro graphic design poster aesthetic
- **Tech:** Three.js (via CDN importmap) + postprocessing npm — no build tools
- **Effekte:** Film Grain, CRT Scanlines, Vignette, Chromatic Aberration, Bloom, Dithering, Light Leaks
- **Palette:** Cold White (`#ffffff`), Black (`#111111`), Blue-Tinted Gray (`#f7f8fa`), Cold Neon Blue (`#1677ff`), Desaturated Cyan (`#5bb8c4`)
- **Typography:** Elms Sans (Display) / Inter (Body) / IBM Plex Mono (Code)
- **Style:** Film grain, CRT scanlines, dithering, bloom, light leaks — textures over colors
- **Layout:** Editorial, free-form, asymmetrisch, poster-artig, `border-radius: 0`
- **Motion:** Langsam, atmosphärisch, cinematic — `cubic-bezier(0.4, 0, 0.2, 1)`

## Key Design Tokens

```css
:root {
  --bg: #ffffff;
  --surface: #f7f8fa;
  --fg: #111111;
  --muted: #6b7280;
  --accent: #1677ff;
  --accent-secondary: #5bb8c4;
  --font-display: "Elms Sans", "Inter", system-ui, sans-serif;
  --font-body: "Inter", system-ui, -apple-system, sans-serif;
  --font-mono: "IBM Plex Mono", "SFMono-Regular", Consolas, monospace;
}
```

## Cleanup History

2026-07-19: Bereinigung von 28 MB → 4.8 MB (entfernt: .od-skills/, assets/, logos/, context/, guide.md, brand.json.seed, system/).
2026-07-19: DESIGN.md komplett überarbeitet zu vollständigem Production Design System v1.0.0.

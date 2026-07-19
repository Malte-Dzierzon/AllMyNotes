---
description: "Portfolio Design Concept — Noise / Editorial / Retro-Futuristic Web"
purpose: "Interactive retro-poster portfolio website with Three.js post-processing effects"
status: "clean"
source: "DESIGN.md + brand toolkit"
---

# web-design-concept

> Noise / Editorial / Retro-Futuristic Web — a reduced, textured, cinematic digital experience

## Overview

Interactive Portfolio-Webseite im Retro-Poster-Stil. Kombiniert editoriales Grafikdesign mit Three.js Post-Processing-Effekten (Film Grain, Scanlines, Bloom, Chromatic Aberration, Dithering). Läuft ohne Build-Tools — Three.js wird via CDN-Importmap geladen.

## Files

| Datei | Zweck |
|---|---|
| `DESIGN.md` | **Hauptdokument** — vollständiges Design-Konzept (Farben, Typografie, Voice, Layout, Imagery) |
| `brand.html` | Visueller Brand-Kit-Viewer — zeigt alle Brand-Daten als interaktive HTML-Seite (single-file, self-contained) |
| `brand.json` | Strukturierte Brand-Daten (maschinenlesbar) — Grundlage für Tooling und Code-Generierung |
| `imagery/` | Referenzbilder (4 PNGs) — visuelle Stimmung und Sample-Imagery |

## Design Direction

- **Site Type:** Interactive Portfolio — retro graphic design poster aesthetic
- **Tech:** Three.js (via CDN importmap) + postprocessing npm package — no build tools
- **Effekte:** Film Grain, CRT Scanlines, Vignette, Chromatic Aberration, Bloom, Dithering, Light Leaks
- **Palette:** Cold White (`#ffffff`), Black (`#111111`), Blue-Tinted Gray (`#f7f8fa`), Cold Neon Blue (`#1677ff`), Desaturated Cyan (`#5bb8c4`)
- **Typography:** Elms Sans (Display) / Inter (Body) / IBM Plex Mono (Code)
- **Style:** Film grain, CRT scanlines, dithering, bloom, light leaks — textures over colors
- **Layout:** Editorial, free-form, asymmetrisch, poster-artig, `border-radius: 0`
- **Motion:** Langsam, atmosphärisch, cinematic — keine schnellen Animationen

## Cleanup History

Der Ordner wurde von **28 MB / 75 Dateien** auf **4.8 MB / 7 Dateien** reduziert:

| Entfernt | Grund |
|---|---|
| `assets/` (22 MB) | Ungenutzte Fonts + Raw-Uploads, von keiner HTML referenziert |
| `.od-skills/` | AI-Agent-Skills, keine Design-Dateien |
| `system/` (708 KB) | Auto-generierte Artifakte (Kit, Tokens, CSS) — nicht Teil des Konzepts |
| `logos/` | Exaktes Duplikat von `imagery/Dropped-Image-3-.png` |
| `context/`, `guide.md`, `brand.json.seed` | Redundante/veraltete Versionen |

## Notes

- `brand.html` hat die `system`- und `assets`-Felder aus dem embedded JSON entfernt, da die generierten Artifakte nicht mehr im Ordner liegen
- Der Logo-Pfad in `brand.json` und `brand.html` zeigt jetzt auf `imagery/Dropped-Image-3-.png` (zuvor doppelt in `logos/`)
- Für Weiterentwicklung: DESIGN.md bearbeiten, dann bei Bedarf brand.json aktualisieren

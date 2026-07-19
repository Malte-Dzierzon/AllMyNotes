---
description: "Design Concept — Noise / Editorial / Retro-Futuristic Web"
purpose: "Design system definition for a reduced, textured, cinematic digital experience"
status: "clean"
source: "DESIGN.md + auto-generated brand toolkit"
---

# web-design-concept

> Noise / Editorial / Retro-Futuristic Web — a reduced, textured, cinematic digital experience

## Overview

Dieses Verzeichnis enthält das Design-Konzept für eine Website, die bewusst von modernem Minimalismus abweicht. Atmosphäre und Emotion stehen vor Perfektion. Der Look kombiniert experimentelles Grafikdesign, digitale Magazine, Vintage-CRT-Monitore und eine ruhige, melancholische Zukunftsvision.

## Files

| Datei | Zweck |
|---|---|
| `DESIGN.md` | **Hauptdokument** — vollständiges Design-Konzept (Farben, Typografie, Voice, Layout, Imagery) |
| `brand.html` | Visueller Brand-Kit-Viewer — zeigt alle Brand-Daten als interaktive HTML-Seite (single-file, self-contained) |
| `brand.json` | Strukturierte Brand-Daten (maschinenlesbar) — Grundlage für Tooling und Code-Generierung |
| `imagery/` | Referenzbilder (4 PNGs) — visuelle Stimmung und Sample-Imagery |

## Design Direction

- **Palette:** Cold White (`#ffffff`), Black (`#111111`), Blue-Tinted Gray (`#f7f8fa`), Cold Neon Blue (`#1677ff`), Desaturated Cyan (`#5bb8c4`)
- **Typography:** Elms Sans (Display) / Inter (Body) / IBM Plex Mono (Code)
- **Style:** Film grain, CRT scanlines, dithering, bloom, light leaks — textures over colors
- **Layout:** Editorial, free-form, asymmetrisch, poster-artig, `border-radius: 0`
- **Motion:** Langsam, atmosphärisch, cinematic — keine schnellen Animationen
- **Vibe:** Ruhig, melancholisch, futuristisch, experimentell — kein Neon-Cyberpunk

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

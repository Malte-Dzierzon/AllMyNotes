---
name: "# Design Concept –"
category: Brands
surface: web
colors:
  cold-white: "#ffffff"
  blue-tinted-gray: "#f7f8fa"
  black: "#111111"
  muted: "#6b7280"
  border: "#d9dee7"
  cold-neon-blue: "#1677ff"
  desaturated-cyan: "#5bb8c4"
---

# # Design Concept –

> Category: Brands

> Surface: web

*Noise / Editorial / Retro-Futuristic Web — a reduced, textured, cinematic digital experience*

A design system for a digital art exhibition, an experimental album cover, and a futuristic magazine combined. Calm, atmospheric, mysterious, and emotionally engaging. Intentionally moves away from modern minimalist interfaces — prioritizes atmosphere and emotion over perfection. Feels like experimental graphic design, digital magazines, vintage CRT monitors, and a calm, melancholic vision of the future.

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

## Typography
- **Display:** Elms Sans — weights 300, 400, 500, 700 — fallbacks: Inter, system-ui, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif
- **Body:** Inter — weights 400, 600, 700 — fallbacks: system-ui, -apple-system, Segoe UI, Helvetica Neue, Arial, sans-serif
- **Mono:** IBM Plex Mono — weights 100, 200, 300, 400, 500, 600, 700 — fallbacks: SFMono-Regular, Consolas, Liberation Mono, Menlo, Courier, monospace

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

## Imagery

- **Style:** Textures over colors. Grain, noise, scanlines, dithering, halftone patterns, light leaks, bloom, and compression artifacts as primary visual texture. Everything feels slightly imperfect, organic, and aged-digital.
- **Subjects:** Vintage CRT screens and monitor glow, Abstract light and signal artifacts, Cold industrial and architectural spaces, Ambient digital landscapes, Textural abstract compositions
- **Treatment:** Apply film grain overlay, CRT scanline pattern, soft vignette, subtle bloom on light sources, and light leak gradients. Use JPEG/video compression artifacts as stylistic texture. Everything should feel like it was captured through imperfect analog-to-digital conversion.
- **Avoid:** Clean product photography, Flat illustrations, Vector art, Stock corporate imagery, Bright saturated colors, Warm beige tones, Playful or cartoon imagery

## Layout

- **Radius:** 0px
- **Border weight:** 1px
- **Spacing:** 8px baseline grid with generous whitespace; asymmetric margins; overlapping layers

### Posture rules
- Editorial layout: each section feels like its own cover page, poster, or editorial spread
- Free-form composition: layered and overlapping elements. Never strictly rectangular grid sections
- Asymmetric balance: generous whitespace on one side, dense content on the other. Avoid centering everything
- Blocks at different scales: mix full-bleed hero blocks with small metadata panels and wide typographic spreads
- Japanese typography as texture: use kana/kanji glyphs as decorative design elements in headings and overlays
- Zero border-radius throughout: all UI elements are strictly rectangular with square corners (0px radius)
- Text is design: typography is part of the visual composition, not just content delivery
- Component kit should cover: Button, Card, Form, Navigation — all rectangular, minimal, with subtle glow interaction states
- Pin overlays consistently: badges and labels over images sit fully inside bounds with solid-panel background and shadow
- Charts use fills, not bare outlines: data visualization encodes through area/volume, not thin strokes
- Slow, atmospheric motion: noise textures, CRT flicker, gentle parallax, fade transitions. Duration 0.3–1.2s. Ease: cubic-bezier(0.4, 0, 0.2, 1)
- Texture overlays: film grain, scanlines, vignette, bloom — applied as CSS pseudo-elements or overlay layers

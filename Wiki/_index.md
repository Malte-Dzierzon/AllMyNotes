---
title: Wiki — Second Brain
type: wiki
category: index
updated: 2026-07-16
---

# Wiki — Second Brain

> **Prinzip**: Dieses Wiki ist für mich *und* für KI-Agenten gleichermaßen lesbar.
> Notes sind in natürlichem Deutsch geschrieben, aber so strukturiert, dass ein Agent schnell die Kerninfo extrahieren kann.

---

## 📚 Books

[[Wiki/Books/Book Collection/]] — 12 Bücher aus den Sturmlicht-Chroniken (Brandon Sanderson) und Der Weg des Waldläufers (Pedro Urvi).

> Importiert via Google Books API Plugin. **Unangetastet lassen.**

## 🃏 MTG Lore

[[Wiki/MTG Lore/Links and Websites.md]] — Links zu Magic: The Gathering Lore, Art und Geschichte.

## 🖼️ Bilder

`Wiki/Images/Pictures/` — Referenzbilder für Projekte (Maps, Concept Art, Screenshots).

---

## Wie das Wiki wächst

Neue Wiki-Notes sollten:

1. **Einen klaren Titel** haben (was ist das?)
2. **Optional YAML-Frontmatter** mit `type`, `tags` und `related`
3. **Mit existierenden Notes verknüpft** sein (`[[Links]]`)
4. **In eine Kategorie** einsortiert sein (oder neue anlegen)

### Vorschläge für neue Kategorien

| Kategorie | Beschreibung | Erste Ideen |
|-----------|-------------|-------------|
| `Game-Design/` | Konzepte, Mechaniken, Referenzen | Combat-Systeme, Level-Design, Movement |
| `UE5-Tech/` | Engine-Wissen, Tutorials, Tipps | Nanite, Lumen, Blueprint vs C++ |
| `Linux/` | System-Tools, Configs, Workflows | Arch Linux, Hyprland, Disk-Tools |
| `Programming/` | Code-Referenzen, Patterns | Python, Rust, React, TypeScript |
| `Creative/` | Writing, Art, Inspiration | Worldbuilding, Charakter-Design |

---

## Templates für neue Wiki-Notes

Nutze `_Meta/Templates/Wiki-Template.md` als Ausgangspunkt.

Oder kopiere dieses Minimalbeispiel:

```markdown
---
title: Mein Thema
type: wiki
category: reference
tags: []
---

# Mein Thema

**Kurzbeschreibung:** Was ist das?

## Details
...

## Verknüpft mit
- [[Projects/...]]
```

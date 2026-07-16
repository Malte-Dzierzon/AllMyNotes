# AGENT.md — Vault Style & Structure Reference

> This file describes the **observed patterns** in this vault. It is a living reference for any agent working here — not a rigid schema. Update it when patterns evolve.

---

## 1. Vault Topology

```
/home/xealom/Documents/AllMyNotes/
├── README.md                    # Root landing page (centered GIF + motto)
├── AGENT.md                     # This file
├── Excalidraw/                  # Excalidraw drawings (*.excalidraw.md)
├── Projekts/                    # Project incubator (game concepts, app ideas)
│   ├── Dreamwolds/
│   ├── Rynthar/
│   ├── Soulslike 2.5D/
│   ├── Stormlight-Archive The Game/
│   └── Unsortiert/
└── Wiki/                        # Knowledge collections
    ├── Books/
    │   ├── Book Collection/     # One .md per book (YAML frontmatter + local cover)
    │   ├── BookCover/           # Cover images (mirrored naming)
    │   └── Books Overview.base  # Dataview view definition
    ├── Images/
    │   └── Pictures/            # Reference images, maps, concept art
    └── MTG Lore/
        └── Links and Websites.md
```

**Naming convention**: German titles for books/projects, English for technical projects, folders use Title Case with spaces.

---

## 2. Note Types & Frontmatter Patterns

| Type | Location | Frontmatter | Content Pattern |
|------|----------|-------------|-----------------|
| **Book Entry** | `Wiki/Books/Book Collection/*.md` | YAML: `title`, `subtitle`, `author`, `category`, `publisher`, `publishDate`, `totalPage`, `coverUrl`, `coverSmallUrl`, `description`, `link`, `previewLink`, `isbn13`, `isbn10`, `localCoverImage` | Minimal body — metadata *is* the note |
| **Project Concept** | `Projekts/<Name>/<Name>.md` | Optional YAML (some have, some don't) | Free-form markdown: concept, mechanics, references, canvas links |
| **Canvas** | `Projekts/<Name>/*.canvas` | JSON canvas format | Visual node/edge maps for game systems, worldbuilding |
| **Excalidraw** | `Excalidraw/*.excalidraw.md` | YAML: `excalidraw-plugin: parsed`, `tags: [excalidraw]` | Compressed JSON in fenced block + `%%` footer |
| **Reference List** | `Wiki/MTG Lore/Links and Websites.md` | None | Plain link list |
| **Dataview View** | `Wiki/Books/Books Overview.base` | YAML: `views:` with `type: cards`/`list`, filters, image config | Zero body — pure view definition |
| **Root README** | `README.md` | None | HTML-centered GIF header + centered quote |

---

## 3. Book Collection Schema (Observed)

Every file in `Wiki/Books/Book Collection/` follows this YAML shape:

```yaml
---
title: Der Weg der Könige
subtitle: Roman
author: Brandon Sanderson
authors: Brandon Sanderson
category: Fiction
categories: Fiction
publisher: Heyne Verlag
publishDate: 2011-05-06
totalPage: 718
coverUrl: https://books.google.com/.../frontcover
coverSmallUrl: https://books.google.com/.../zoom=5
description: Roschar ist eine sturmumtoste Welt...
link: https://play.google.com/store/books/details?id=...
previewLink: http://books.google.de/books?id=...
isbn13: 9783641059446
isbn10: 3641059445
localCoverImage: Wiki/Books/BookCover/Der Weg der Könige - Brandon Sanderson.jpg
---
```

**Cover pairing**: Each `.md` has a matching `.jpg` in `BookCover/` with identical filename stem.

**Dataview view** (`Books Overview.base`) renders these as cards using `note.coverUrl` (falls back to `localCoverImage`).

---

## 4. Project Note Anatomy

Typical `Projekts/<Name>/<Name>.md`:

- Optional YAML frontmatter (some have, some don't — **don't enforce**)
- Free-form sections: concept, mechanics, lore, references
- Links to `.canvas` files in same folder (e.g., `Game Idee...o.Dreamwolds.canvas`)
- German prose, markdown headings, bullet lists, occasional code blocks
- `Unsortiert/` holds one-off ideas (Bow Shooter, Disk App Linux Idee) — same pattern, no subfolder

---

## 5. Canvas Files (`.canvas`)

- JSON-based visual graphs (nodes, edges, groups)
- Stored alongside project notes
- Naming: descriptive + `.canvas` (spaces allowed)
- Referenced from project notes via wikilinks or bare paths

---

## 6. Excalidraw Files

- Extension: `.excalidraw.md`
- Frontmatter: `excalidraw-plugin: parsed`, `tags: [excalidraw]`
- Body: single fenced block with compressed JSON
- Footer: `%%` (Excalidraw plugin marker)
- Stored centrally in `Excalidraw/` (not per-project)

---

## 7. Images & Assets

- **Book covers**: `Wiki/Books/BookCover/` — paired 1:1 with book notes
- **Reference images**: `Wiki/Images/Pictures/` — maps, concept art, screenshots
- **Root assets**: `background.jpg` (used in root README GIF wrapper)
- Referenced via relative paths in frontmatter (`localCoverImage`) or markdown images

---

## 8. Dataview Usage

- Only `Books Overview.base` observed so far
- Defines **card view** (cover image, title, author) + **list view**
- Filter: `file.folder == "Wiki/Books/Book Collection"`
- Image config: `image: note.coverUrl`, `imageFit: contain`, `imageAspectRatio: 1.5`
- No inline Dataview queries observed in notes

---

## 9. Language & Style

- **Primary language**: German (book metadata, project prose, UI labels)
- **Technical terms**: English (canvas, markdown, canvas, API, JSON, etc.)
- **Markdown style**: ATX headings (`#`, `##`), fenced code blocks, HTML for centering (root README)
- **No tags** in project/book notes (only Excalidraw files carry `tags: [excalidraw]`)
- **No aliases**, no `cssclass`, no custom YAML beyond observed fields

---

## 10. Conventions to Preserve

| Convention | Do | Don't |
|------------|----|-------|
| Book metadata | Keep full YAML schema; mirror cover filename exactly | Add custom fields not in schema |
| Project notes | Keep free-form; don't impose frontmatter | Force templates |
| Canvas/Excalidraw | Keep alongside project or in `Excalidraw/` | Move without updating links |
| Book covers | Keep 1:1 pairing in `BookCover/` | Rename without updating `localCoverImage` |
| Dataview views | Define in `.base` files | Inline queries in notes |
| Language | German for content, English for tech | Mix inconsistently |
| Root README | Keep centered GIF + motto pattern | Replace with plain markdown |

---

## 11. Dynamic Discovery Rules (for agents)

When exploring this vault, **detect** rather than assume:

1. **Book notes** → `search_files(pattern="Wiki/Books/Book Collection/*.md", target="files")` → read one → infer schema
2. **Projects** → `search_files(pattern="Projekts/*/*.md", target="files")` → group by parent folder
3. **Canvas files** → `search_files(pattern="*.canvas", target="files")`
4. **Excalidraw** → `search_files(pattern="Excalidraw/*.excalidraw.md", target="files")`
5. **Dataview views** → `search_files(pattern="*.base", target="files")`
6. **Image assets** → `search_files(pattern="Wiki/Books/BookCover/*.jpg", target="files")` + `Wiki/Images/Pictures/*`

**Never hardcode paths** — the folder names (e.g., `Dreamwolds`, `Soulslike 2.5D`) are user-defined and will change.

---

## 12. Evolution Notes

- **2026-07-16**: Initial extraction. Vault is young (~22 markdown files). Patterns are consistent but not yet rigid.
- Next likely evolution: more Dataview views, project templates, tag system for projects, possible `templates/` folder.
- When patterns shift, update this file — it is the contract between you and the vault.

---

> **Principle**: This vault favors *organic growth* over *premature structure*. Describe what exists; don't prescribe what should exist.
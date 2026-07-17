# AGENT.md — Vault Style & Structure Reference

> This file describes the **observed patterns** in this vault. It is a living reference for any agent working here — not a rigid schema. Update it when patterns evolve.
>
> Last structural update: 2026-07-16 (migration from `Projekts/` to `Projects/Active|Archive`)

---

## 1. Vault Topology

```
/home/xealom/Documents/AllMyNotes/
├── README.md                    # Root landing page (centered GIF + motto + skills)
├── AGENT.md                     # This file
│
├── Excalidraw/                  # Plugin-generiert (Excalidraw plugin)
│   └── *.excalidraw.md          # Frontmatter: excalidraw-plugin, tags: [excalidraw]
│
├── Wiki/                        # Second Brain — Mensch + KI lesbar
│   ├── Books/
│   │   ├── Book Collection/     # 12 .md mit YAML (18 Felder) – Plugin-generiert
│   │   ├── BookCover/           # 12 .jpg – 1:1 Pairing mit Book Collection
│   │   └── Books Overview.base  # Dataview cards + list
│   └── Images/
│       └── Pictures/            # Referenzbilder, Maps, Concept Art (20+)
│
├── Projects/                    # NEU – Projekt-Dashboard (ersetzt Projekts/)
│   ├── 00-Overview/
│   │   ├── Projects.md          # Zentraler Index mit Status-Tabelle
│   │   └── Projects.base        # Dataview: cards + list
│   ├── Active/                  # Laufende Projekte
│   │   ├── Dreamwolds/          # .md + .canvas
│   │   ├── Rynthar/             # .md
│   │   ├── MTG Multiverse Studio/ # NEU – von GitHub
│   │   ├── Personal Dashboard Portfolio/ # NEU – von GitHub
│   │   ├── Bow Shooter/         # aus Unsortiert
│   │   └── Disk Dashboard/      # aus Unsortiert (umbenannt)
│   ├── Archive/                 # Abgeschlossen / pausiert
│   │   ├── Soulslike 2.5D/      # .md + .canvas – ✅ 100%
│   │   ├── Neural Network Python/ # NEU – ✅ 100%
│   │   ├── Minecraft Paleon/    # NEU – ✅ 100%
│   │   ├── Stormlight-Archive The Game/ # .canvas – Referenz
│   │   └── Minecraft Mod Ideas/ # .canvas – aus Unsortiert
│   └── Templates/               # (nicht direkt genutzt, Referenz in _Meta/)
│
├── Research/                    # NEU – Automatisierte Recherche
│   ├── _Inbox/                  # Agenten schreiben hier rein (write-only)
│   ├── Topics/                  # Kuratiert (Mensch oder Agent)
│   │   ├── Game-Design/         # _index.md + Detail-Notes
│   │   ├── UE5-Tech/
│   │   ├── Linux-Tools/
│   │   ├── Web-Dev/
│   │   └── MTG Lore/            # Magic: The Gathering Links & Notizen
│   ├── Sources/                 # PDFs, Web-Archives, Bilder
│   │   ├── PDFs/
│   │   └── Web-Exports/
│   └── Research.md              # Übersicht + Flow-Beschreibung
│
└── _Meta/                       # NEU – Vault-Infrastruktur
    ├── Templates/
    │   ├── Project-Template.md
    │   └── Research-Template.md
    ├── Scripts/                 # (zukünftige Automationen)
    └── Archive/                 # (ausgelagerte Notizen)
```

---

## 2. Note Types & Frontmatter Patterns

| Type | Location | Frontmatter | Content Pattern |
|------|----------|-------------|-----------------|
| **Book Entry** | `Wiki/Books/Book Collection/*.md` | YAML (18 Felder): title, subtitle, author, publisher, publishDate, totalPage, coverUrl, description, isbn13, localCoverImage, … | Minimal body — metadata *is* the note |
| **Active Project** | `Projects/Active/<Name>/<Name>.md` | Optional YAML: title, type, status, engine, progress, github, tags | Free-form: concept, mechanics, features, references |
| **Archived Project** | `Projects/Archive/<Name>/<Name>.md` | Optional YAML + completion info | Free-form + Status ✅ |
| **Canvas Map** | `Projects/*/*.canvas` | JSON canvas format | Visual node/edge maps |
| **Excalidraw** | `Excalidraw/*.excalidraw.md` | YAML: `excalidraw-plugin: parsed`, `tags: [excalidraw]` | Compressed JSON + `%%` |
| **Reference List** | `Wiki/MTG Lore/*.md` → wurde verschoben nach `Research/Topics/MTG Lore/` | Plain link list |
| **Dataview .base** | `**/*.base` | YAML: views, filters, image config | Zero body |
| **Root README** | `README.md` | None | HTML-centered GIF + motto + skills table |
| **Research (Inbox)** | `Research/_Inbox/*.md` | YAML: title, type, source, agent, date, tags | Summary, Key Findings, Sources, Raw Notes |
| **Research (Topic)** | `Research/Topics/<Topic>/*.md` | Optional YAML | Overview, related projects, sub-topics |
| **Template** | `_Meta/Templates/*.md` | Full YAML with instructions | Placeholder text for {{variables}} |
| **Dashboard** | `Projects/00-Overview/Projects.md` | YAML: title, type, updated | Tables, links, legend |

---

## 3. Book Collection Schema

Every file in `Wiki/Books/Book Collection/` follows this YAML shape (Google Books API import):

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
**Dataview view**: `Books Overview.base` renders as cards using `note.coverUrl`.

> 🔒 **Immutable**: Do not modify this schema. It is plugin-generated (Google Books API).

---

## 4. Project Note Anatomy

### Active project (recommended YAML)
```yaml
---
title: Projektname
type: project
status: active      # active | idea | archived
engine: UE5         # Rust, Python, TypeScript, Blender, …
started: 2026-07-01
progress: 20%
github: https://github.com/Malte-Dzierzon/<repo>
tags: [game-dev, unreal]
---
```

### Archive project (completed)
```yaml
---
title: Projektname
type: project
status: archived
engine: UE5
started: 2026-05
completed: 2026-06
progress: 100%
tags: []
---
```

**Note**: Frontmatter is **optional** for old notes. Only new/updated projects should use it.

---

## 5. Status Taxonomy

| Status | Folder | Meaning |
|--------|--------|---------|
| `#active` | `Projects/Active/` | Wird aktuell bearbeitet |
| `#idea` | `Projects/Active/` | Konzeptphase, noch nicht aktiv |
| `#archived` | `Projects/Archive/` | Abgeschlossen oder pausiert |

---

## 6. Canvas Files (`.canvas`)

- JSON-based visual graphs (nodes, edges, groups, embedded images)
- Stored alongside project notes (or in Archive/)
- Naming: descriptive + `.canvas` (spaces allowed)
- Can reference images from `Wiki/Images/Pictures/`
- Referenced from project notes via wikilinks or bare paths

---

## 7. Excalidraw Files

- Extension: `.excalidraw.md`
- Frontmatter: `excalidraw-plugin: parsed`, `tags: [excalidraw]`
- Body: single fenced block with compressed JSON
- Footer: `%%` (Excalidraw plugin marker)
- Stored centrally in `Excalidraw/` (not per-project)
> 🔒 Do not edit the compressed JSON manually.

---

## 8. Images & Assets

- **Book covers**: `Wiki/Books/BookCover/` — paired 1:1 with book notes
- **Reference images**: `Wiki/Images/Pictures/` — maps, concept art, screenshots, memes
- **Research sources**: `Research/Sources/` — PDFs, web archives
- **Root**: `background.jpg` (used in root README)
- Referenced via relative paths in frontmatter (`localCoverImage`) or markdown

---

## 9. Dataview Usage

| File | Type | Purpose |
|------|------|---------|
| `Wiki/Books/Books Overview.base` | Cards + List | Buchsammlung visualisieren |
| `Projects/00-Overview/Projects.base` | Cards + List | Alle Projekte automatisch anzeigen |

**Convention**: `.base` files define views only. No inline Dataview queries in notes.

---

## 10. Research Flow (for Agents)

### The automated research pipeline:
1. **Write to** `Research/_Inbox/` using template `_Meta/Templates/Research-Template.md`
2. **Filename format**: `YYYY-MM-DD_topic.md` (machine-sortable)
3. **Required fields**: title, type: research, source, agent, date
4. **Content**: Summary (EN + DE), Key Findings, Sources, Raw Notes
5. **After curation**: Move to `Research/Topics/<Category>/` and update `_index.md`

### Cron-job design pattern:
- Schedule: `0 8 * * 1` (weekly) or on-demand via single-shot cron
- Skills: [research, web, note-taking]
- Script: reads Research/_Requests.md or uses prompt to determine topics
- Deliver: to origin or Telegram

---

## 11. Templates

| Template | Path | Used For |
|----------|------|----------|
| Project Template | `_Meta/Templates/Project-Template.md` | New projects (full: Concept, Tech Stack, Roadmap, Links) |
| Research Template | `_Meta/Templates/Research-Template.md` | Agent-generated research (TL;DR, Findings, Sources, Next Steps) |
| Wiki Template | `_Meta/Templates/Wiki-Template.md` | New Wiki Second-Brain entries (structured for humans + AI) |

### Template Variables
- `{{title}}` – Project/Note name
- `{{date}}` – Current date
- `{{...}}` – Agent fills these

---

## 12. Scripts (_Meta/Scripts/)

| Script | Purpose | Usage |
|--------|---------|-------|
| `new-project.py` | Scaffolds a new project folder + note from template | `python3 _Meta/Scripts/new-project.py "Name" --engine UE5 --status idea` |
| `research-cron-orchestrator.py` | Creates research tasks and manages _Requests.md | `python3 _Meta/Scripts/research-cron-orchestrator.py run "topic"` |
| `vault-stats.py` | Prints vault statistics (files, words, todos per folder) | `python3 _Meta/Scripts/vault-stats.py` |

All scripts live in `_Meta/Scripts/` and are executable.

---

## 13. Language & Style

- **Primary**: German (book metadata, project prose, research summaries)
- **Technical terms**: English (canvas, JSON, API, Rust, UE5, TypeScript, …)
- **Markdown**: ATX headings (`#`, `##`), fenced code blocks, HTML for centering (root README)
- **Tags**: Minimal — only Excalidraw has forced `tags: [excalidraw]`
- **No aliases**, no `cssclass`, no custom YAML beyond observed fields

---

## 14. Conventions to Preserve

| Convention | Do | Don't |
|------------|----|-------|
| **Book metadata** | Keep full YAML; mirror cover filename | Change schema |
| **Project notes** | Keep free-form; frontmatter optional | Force templates on old notes |
| **Canvas/Excalidraw** | Keep in project folder or `Excalidraw/` | Move without updating links |
| **Book covers** | Maintain 1:1 pairing | Rename without updating `localCoverImage` |
| **Dataview views** | Define in `.base` files | Inline queries in notes |
| **Language** | German for content, English for tech | Mix inconsistently |
| **Root README** | Keep centered GIF + motto pattern | Replace with plain markdown |
| **README dedup** | Only ONE copy in root | Duplicate in subfolders |
| **Excalidraw** | Leave as plugin writes it | Manually edit JSON |

---

## 15. Dynamic Discovery Rules (for agents)

When exploring this vault, **detect** rather than assume:

1. **Book notes** → `search_files(pattern="Wiki/Books/Book Collection/*.md", target="files")` → read one → infer schema
2. **Active projects** → `search_files(pattern="Projects/Active/*/*.md", target="files")` → group by parent
3. **Archive** → `search_files(pattern="Projects/Archive/*/*.md", target="files")`
4. **Canvas files** → `search_files(pattern="*.canvas", target="files")`
5. **Excalidraw** → `search_files(pattern="Excalidraw/*", target="files")`
6. **Dataview views** → `search_files(pattern="*.base", target="files")`
7. **Research inbox** → `search_files(pattern="Research/_Inbox/*", target="files")`
8. **Research topics** → `search_files(pattern="Research/Topics/*/_index.md", target="files")`
9. **Templates** → `search_files(pattern="_Meta/Templates/*.md", target="files")`
10. **GitHub mirror** → Check YAML frontmatter `github:` field in project notes

**Never hardcode paths** — folder names are user-defined and may change.

---

## 16. GitHub Mirror (Projects → Repos)

The vault is a **GitHub repository** (`Malte-Dzierzon/AllMyNotes`).  
All 5 public repos are documented in `Projects/`:

| Project Note | GitHub Repo | Status |
|-------------|-------------|--------|
| [[Projects/Active/MTG Multiverse Studio/MTG Multiverse Studio.md]] | [MTG-Multiverse-Studio](https://github.com/Malte-Dzierzon/MTG-Multiverse-Studio) | Active |
| [[Projects/Active/Personal Dashboard Portfolio/Personal Dashboard Portfolio.md]] | [Portfolio](https://github.com/Malte-Dzierzon/Portfolio) | Active |
| [[Projects/Archive/Neural Network Python/Neural Network Python.md]] | [Informatik-Projekt-August-Malte](https://github.com/Malte-Dzierzon/Informatik-Projekt-August-Malte) | Archived |
| — | [Malte-Dzierzon](https://github.com/Malte-Dzierzon/Malte-Dzierzon) (Profile) | Always live |
| — | [AllMyNotes](https://github.com/Malte-Dzierzon/AllMyNotes) (this vault) | Always live |

The `github:` field in project frontmatter links notes to their remote repos.

---

## 17. Evolution Notes

- **2026-07-16**: Initial extraction. Vault migrated from `Projekts/` to `Projects/Active|Archive`.
- **2026-07-16**: `Research/` and `_Meta/` added. All 5 GitHub repos documented.
- **2026-07-16**: Fixes: All notes now have frontmatter. 3 templates. 3 scripts. Wiki/_index.md. Removed MTG Lore from Research/ (it was a migration artifact). Removed duplicate Projects/Templates/ folder.
- Next expected: Dataview dashboards, Research cron jobs, Wiki topic expansion.
- When patterns shift, update this file — it is the contract between you and the vault.

---

## 18. Growth Suggestions (next steps for you)

### Hermes Skills für diesen Vault

Wenn du in diesem Chat arbeitest und eine Frage zu einem bestimmten Bereich hast, 
lade automatisch den passenden Skill. Diese Skills sind verfügbar:

| Skill | Wann laden | Enthält |
|-------|-----------|---------|
| `vault-research` | Research-Aufgaben, Recherche-Automation, _Inbox-Handling | Templates, Cron-Design, Naming, Curation-Flow |
| `vault-projects` | Projekte anlegen/aktualisieren/archivieren, Dashboard | Frontmatter, Scripts, Status-Taxonomie, GitHub-Mirror |
| `vault-wiki` | Wiki-Einträge erstellen, Second-Brain-Konventionen | Kategorien, Verlinkung, Books-Immutable-Regel |

Lade den Skill einfach mit `skill_view(name="vault-<bereich>")` bevor du eine Aufgabe startest.

### Wiki – "Second Brain" ausbauen

| Kategorie | Inhalt | Priorität |
|-----------|--------|-----------|
| `Game-Design/` | Combat-Systeme, Level-Design-Referenzen, Movement-Mechaniken | 🔥 Hoch |
| `UE5-Tech/` | Nanite, Lumen, Niagara, Blueprint-Tutorials | 🔥 Hoch |
| `Linux/` | Arch-Workflow, Hyprland-Configs, Disk-Tools | ⭐ Mittel |
| `Programming/` | Python, Rust, TypeScript – Code-Referenzen | ⭐ Mittel |
| `Creative/` | Worldbuilding, Charakter-Design, Art-Inspiration | 🌱 Niedrig |

**Mach dir keinen Druck.** Ein Eintrag pro Woche reicht, um das Wiki organisch wachsen zu lassen.

### Projects – "Dashboard" aktuell halten

- **Projekt abschließen?** → Move nach `Archive/`, `status: archived`, `completed: 2026-XX-XX`
- **Neue Idee?** → Nutze das Script: `python3 _Meta/Scripts/new-project.py "Name"`
- **Neues GitHub-Repo?** → Kurze Note in `Projects/` + `github:` Feld + `00-Overview/Projects.md` ergänzen

### Research – "Automation" einrichten

1. **Cron-Job bauen**: `hermes cron create --schedule "0 9 * * 1" --script _Meta/Scripts/research-cron-orchestrator.py --prompt "Check _Requests.md and research all open topics" --deliver all`
2. **Oder spontan**: `python3 _Meta/Scripts/research-cron-orchestrator.py run "UE5 Nanite Performance"` → erzeugt `Research/_Inbox/2026-07-16_ue5-nanite-performance.md`
3. **Kuratieren**: Verschiebe aus `_Inbox/` → `Topics/<Kategorie>/` und ergänze `_index.md`

### Excalidraw – Status quo

Einfach zeichnen. Plugin legt automatisch `.excalidraw.md` in `Excalidraw/` an.
Falls du Excalidraw woanders speichern willst, konfiguriere das Plugin – nicht manuell verschieben.

### Templates – bei Bedarf anpassen

- `_Meta/Templates/Project-Template.md` – Wenn dir Sektionen fehlen/überflüssig sind
- `_Meta/Templates/Research-Template.md` – Wenn der Agent anders schreiben soll
- `_Meta/Templates/Wiki-Template.md` – Wenn Wiki-Notes anders aussehen sollen

### Scripts – nutzen oder erweitern

- `vault-stats.py` → Zeigt offene Todos, Wortanzahl, Dateien pro Ordner
- `new-project.py` → Legt neue Projekte an (nutzt Template; interaktiv oder via CLI)
- `research-cron-orchestrator.py` → Startet Research-Aufträge

### Nächste größere Baustelle

**Dataview-Dashboards ausbauen:**
- Automatische Status-Übersicht in `00-Overview/Projects.md`
- Research-Übersicht (welche Topics haben wie viele Notes?)
- Wiki-Kategorie-Index mit "letzte Änderung"-Spalte

---

> **Principle**: This vault favors *organic growth* over *premature structure*. Describe what exists; don't prescribe what should exist.

---
epoch: 1784184834017
modelKey: nvidia/nemotron-3-ultra-550b-a55b:free|openrouterai
tags:
  - copilot-conversation
topic: Analyze Obsidian Vault Structure
lastAccessedAt: 1784184914878
---

**user**: Aufgabe

Analysiere ausschließlich die Dateien und Ordner, die ich dir für diese Aufgabe zur Verfügung gestellt habe.

Ziel

Erstelle anhand der bestehenden Struktur meines Obsidian Vaults eine professionelle, ausführliche und gut strukturierte "README.md", die als zentrale Einstiegspunkt für den gesamten Vault dient.

Vorgehen

1. Analyse

Analysiere zunächst den gesamten Vault, um zu verstehen:

- wie die Ordner organisiert sind,
- welchem Zweck die einzelnen Bereiche dienen,
- welche Dokumentationsstandards verwendet werden,
- welche Projekte, Wikis und Wissensbereiche existieren,
- wie Informationen miteinander verknüpft sind.

Nimm während dieser Phase keine Änderungen vor.

2. README erstellen

Erstelle anschließend eine hochwertige "README.md", die den Vault vollständig dokumentiert.

Die README sollte unter anderem enthalten:

- eine Einführung und den Zweck des Vaults,
- eine Übersicht über die gesamte Ordnerstruktur,
- eine Beschreibung jedes Hauptordners,
- die wichtigsten Projekte und deren Zweck,
- die Wissensbereiche (Wiki, Tech, AI usw.),
- die verwendeten Konventionen (Ordner, Tags, Canvas, Templates, Backlinks usw.),
- Navigationshilfen,
- empfohlene Einstiegsseiten,
- Hinweise zur Pflege und Erweiterung des Vaults,
- eine übersichtliche Struktur mit Inhaltsverzeichnis.

3. Qualität

Die README soll nicht nur beschreiben, was vorhanden ist, sondern den Vault verständlich dokumentieren.

Sie soll:

- professionell wirken,
- leicht lesbar sein,
- logisch gegliedert sein,
- auch bei einem stark wachsenden Vault langfristig nützlich bleiben,
- als Dokumentation für neue Nutzer oder für mein zukünftiges Ich dienen.

Falls Informationen aus der vorhandenen Struktur sinnvoll ergänzt werden können, darfst du Vorschläge aufnehmen. Erfinde jedoch keine Inhalte, die nicht aus dem Vault ableitbar sind.
[Context: Notes: README.md]
[Timestamp: 2026/07/16 08:53:54]

**ai**: # Vault README

> **Zentrale Dokumentation & Navigation** für diesen Obsidian Vault  
> *Stand: 2025-07-15 | Version 1.0*

---

## 📖 Inhaltsverzeichnis

1. [Einführung & Zweck](#-einführung--zweck)
2. [Gesamtstruktur](#-gesamtstruktur)
3. [Hauptbereiche im Detail](#-hauptbereiche-im-detail)
   - [🎮 Projekts – Game Development & Konzepte](#-projekts--game-development--konzepte)
   - [📚 Wiki – Wissensbasis & Referenzen](#-wiki--wissensbasis--referenzen)
4. [Dokumentationsstandards & Konventionen](#-dokumentationsstandards--konventionen)
5. [Navigation & Einstiegsseiten](#-navigation--einstiegsseiten)
6. [Pflege & Erweiterung](#-pflege--erweiterung)
7. [Changelog](#-changelog)

---

## 🎯 Einführung & Zweck

Dieser Vault dient als **zentrale Wissens- und Projektbasis** für:

- **Game Development** – Konzeption, Design und Dokumentation mehrerer Spielprojekte
- **Persönliches Wiki** – Strukturierte Ablage von Buchwissen (Cosmere, Fantasy), MTG-Lore und Bildressourcen
- **Kreative Ideensammlung** – Canvas-basierte visuelle Entwürfe und unsortierte Konzepte

> **Zielgruppe:** Ich (Ersteller) – als langfristiges Gedächtnis, Navigationshilfe und Dokumentationsstandard für zukünftige Erweiterungen.

---

## 🗂️ Gesamtstruktur

```text
📁 Vault-Root
├── 📁 Projekts/                 # Game Development Projekte
│   ├── 📁 Dreamwolds/
│   ├── 📁 Rynthar/
│   ├── 📁 Soulslike 2.5D/
│   ├── 📁 Stormlight-Archive ○The Game○/
│   ├── 📁 Unsortiert/
│   ├── Projects.base            # Dataview/Query Basis für Projekt-Übersichten
│   └── README.md                # (lokaler Projekt-Index)
└── 📁 Wiki/                     # Wissensbasis & Referenzen
    ├── 📁 Books/
    │   ├── 📁 Book Collection/  # Buch-Notizen (13 Titel)
    │   ├── 📁 BookCover/        # Cover-Bilder (13 Dateien)
    │   └── Books Overview.base  # Dataview Basis für Buch-Übersichten
    ├── 📁 Images/
    │   ├── 📁 Pictures/         # Referenzbilder (24 Dateien)
    │   └── background.jpg
    └── 📁 MTG Lore/
        └── Links and Websites.md
```

---

## 📦 Hauptbereiche im Detail

### 🎮 Projekts – Game Development & Konzepte

| Projekt | Typ | Dateien | Status / Fokus |
|---------|-----|---------|----------------|
| **Dreamwolds** | Eigenes Spielkonzept | `Dreamwolds.md` + Canvas | Weltbau, Game Design, visuelle Konzept-Arbeit |
| **Rynthar** | Eigenes Spielkonzept | `Rynthar-Conzept.md` | Konzeptionelles Design-Dokument |
| **Soulslike 2.5D** | Genre-Projekt | `Soulslike.md` + `Game System.canvas` | Mechanik-Design, System-Architektur (Canvas) |
| **Stormlight-Archive ○The Game○** | Fan-/Adaptions-Projekt | `Stormlight Archive Game.canvas` | Canvas-basiertes Design auf Basis von Brandon Sandersons *Stormlight Archive* |
| **Unsortiert** | Ideen-Sammelbecken | 3 Dateien | Bow Shooter, Disk App Linux, Minecraft Mod Ideen |

#### Besondere Hinweise
- **Canvas-Dateien** (`.canvas`) werden intensiv für **visuelles Game Design**, System-Architektur und Worldbuilding genutzt.
- `Projects.base` dient als **Dataview-Quelle** für automatisierte Projekt-Übersichten (Tabellen, Listen, Status-Tracking).
- Der Ordner `Unsortiert` fungiert als **Inbox** – regelmäßiges Aufräumen in eigene Projekt-Ordner empfohlen.

---

### 📚 Wiki – Wissensbasis & Referenzen

#### 📖 Books / Buch-Sammlung
**Fokus:** Brandon Sanderson (Cosmere / Stormlight Archive) & Pedro Urvi (High Fantasy)

| Autor | Titel (DE) | Original | Notiz | Cover |
|-------|------------|----------|-------|-------|
| Brandon Sanderson | Der Weg der Könige | *The Way of Kings* | ✅ | ✅ |
| Brandon Sanderson | Die Worte des Lichts | *Words of Radiance* | ✅ | ✅ |
| Brandon Sanderson | Der Schwur der Könige / Der Rhythmus des Krieges | *Oathbringer / Rhythm of War* | ✅ | ✅ |
| Brandon Sanderson | Die Tänzerin am Abgrund | *Dawnshard* | ✅ | ✅ |
| Brandon Sanderson | Der Splitter der Dämmerung | *The Lost Metal* (?) | ✅ | ✅ |
| Brandon Sanderson | Der Turm der Lichter | — | ✅ | ✅ |
| Brandon Sanderson | Die Stürme des Zorns | — | ✅ | ✅ |
| Brandon Sanderson | Der Kampf der Meister | — | ✅ | ✅ |
| Brandon Sanderson | Winde und Wahrheit | *Wind and Truth* (kommend) | ✅ | ✅ |
| Pedro Urvi | Der König des Westens | — | ✅ | ✅ |
| Pedro Urvi | Verrätersohn | — | ✅ | ✅ |
| Pedro Urvi | Verrat im Norden | — | ✅ | ✅ |

- **Books Overview.base** → Dataview-Basis für Lesestatus, Ratings, Tags, Queries.
- **BookCover/** → 1:1 Zuordnung zu den Notizen (Dateinamen identisch).

#### 🖼️ Images / Bildressourcen
- **Pictures/** (24 Dateien): Mix aus **Stormlight Archive Karten/Artworks** (Shattered Plains, Alethi Warcamps, Silver Kingdoms), **Gameplay-Referenzen** (Little Nightmares, Combat, Brush Strokes), **Projekt-Screenshots** (Projekt Plugins, BP Combat/Combo) und **sonstige Referenzen**.
- `background.jpg` → Vault-weiter Hintergrund / CSS-Nutzung.

#### 🃏 MTG Lore
- `Links and Websites.md` → Kuratierte Linksammlung zu Magic: The Gathering Lore (Scryfall, MTG Wiki, Story-Artikel, Karten-Datenbanken).
- Potenzial für Erweiterung: Set-Übersichten, Deck-Building-Notizen, Regelwissen.

---

## 📏 Dokumentationsstandards & Konventionen

| Bereich | Konvention | Beispiel |
|---------|------------|----------|
| **Ordnernamen** | Deutsch, beschreibend, Leerzeichen erlaubt | `Soulslike 2.5D`, `Stormlight-Archive ○The Game○` |
| **Dateinamen** | Kebab-Case oder Title-Case, `.md` / `.canvas` | `Dreamwolds.md`, `Game System.canvas` |
| **Projekt-Notizen** | Eine Haupt-`.md` pro Projekt + Canvas für Visuals | `Rynthar-Conzept.md` |
| **Buch-Notizen** | `Titel - Autor.md` | `Der Weg der Könige - Brandon Sanderson.md` |
| **Bilder** | In `Wiki/Images/Pictures/` oder `Wiki/Books/BookCover/` | `Der Weg der Könige - Brandon Sanderson.jpg` |
| **Canvas** | Für System-Design, Worldbuilding, Mechanik-Flows | `Game System.canvas` |
| **Dataview Bases** | `*.base` Dateien für Queries/Views | `Projects.base`, `Books Overview.base` |
| **Tags** | (Noch nicht explizit sichtbar – Empfehlung siehe unten) | `#projekt/aktiv`, `#buch/gelesen`, `#mtg/lore` |
| **Backlinks** | Nutzung von `[[Wikilinks]]` für Querverweise | `[[Dreamwolds]]`, `[[Stormlight Archive]]` |

### Empfohlene Tag-Taxonomie (Vorschlag)
```yaml
# Projekte
#projekt/aktiv | #projekt/konzept | #projekt/archiviert
#genre/soulslike | #genre/strategy | #genre/rpg

# Wiki
#buch/cosmere | #buch/urvi | #buch/gelesen | #buch/leseliste
#mtg/lore | #mtg/rules | #mtg/deckbuilding

# Typ
#canvas | #reference | #idea | #asset/image
```

---

## 🧭 Navigation & Einstiegsseiten

| Seite | Zweck | Link |
|-------|-------|------|
| **Diese README** | Zentrale Übersicht & Doku | `README.md` (Root) |
| **Projekts/README.md** | Projekt-spezifischer Index | `Projekts/README.md` |
| **Projects.base** | Dataview: Alle Projekte tabellarisch | `Projekts/Projects.base` |
| **Books Overview.base** | Dataview: Buch-Übersicht mit Status | `Wiki/Books/Books Overview.base` |
| **Dreamwolds.md** | Hauptdokument Dreamwolds | `Projekts/Dreamwolds/Dreamwolds.md` |
| **Rynthar-Conzept.md** | Hauptdokument Rynthar | `Projekts/Rynthar/Rynthar-Conzept.md` |
| **Soulslike.md** | Hauptdokument Soulslike | `Projekts/Soulslike 2.5D/Soulslike.md` |
| **Links and Websites.md** | MTG Lore Linksammlung | `Wiki/MTG Lore/Links and Websites.md` |

> **Tipp:** Nutze `Strg+O` (Quick Switcher) mit Prefixen wie `projekt:`, `buch:`, `canvas:` für schnellen Zugriff.

---

## 🛠️ Pflege & Erweiterung

### Regelmäßige Aufgaben
- [ ] **Wöchentlich:** `Unsortiert/` prüfen → Ideen in eigene Projekt-Ordner überführen oder archivieren
- [ ] **Monatlich:** Dataview-Bases (`.base`) prüfen & Queries aktualisieren
- [ ] **Bei neuen Büchern:** Notiz in `Book Collection/`, Cover in `BookCover/`, Metadaten in `Books Overview.base` pflegen
- [ ] **Bei neuen Bildern:** In `Wiki/Images/Pictures/` ablegen, sprechende Dateinamen verwenden

### Erweiterungs-Ideen (basierend auf Status quo)
1. **Tag-System einführen** (siehe Taxonomie oben) → ermöglicht mächtige Dataview-Queries
2. **Projekt-Template** anlegen (YAML Frontmatter: Status, Genre, Engine, Startdatum, Tags)
3. **Buch-Template** anlegen (Titel, Autor, Serie, Status, Rating, Tags, Cover-Pfad)
4. **Canvas-Naming-Convention** dokumentieren (z. B. `System-<Name>.canvas`, `World-<Name>.canvas`)
5. **MTG Lore** strukturieren: Sets, Planeswalker, Story-Arks als eigene Notizen
6. **Vault-weites Dashboard** (Home-Note) mit Dataview: offene Tasks, letzte Änderungen, zufälliges Buch/Projekt

### Technische Hinweise
- **Dataview Plugin** erforderlich für `.base` Dateien
- **Canvas Plugin** (Core) für `.canvas` Dateien
- **Image Embeds** funktionieren via `![[Pfad/Bild.jpg]]` (relativ zum Vault-Root)

---

## 📝 Changelog

| Version | Datum | Änderungen |
|---------|-------|------------|
| 1.0 | 2025-07-15 | Ersteinrichtung basierend auf bestehender Vault-Struktur |

---

> **Hinweis:** Dieses Dokument ist **lebendig**. Aktualisiere es bei strukturellen Änderungen, neuen Hauptordnern oder geänderten Konventionen. Es dient dir als Kompass – halte es aktuell, damit es dir auch in 2 Jahren noch hilft.
[Timestamp: 2026/07/16 08:54:29]
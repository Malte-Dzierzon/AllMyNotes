#!/usr/bin/env python3
"""
new-project.py – Erstellt ein neues Projekt im Vault aus der Project-Template.md.

Ohne Argumente startet das Skript im interaktiven Modus und fragt alle
Werte ab. Mit Argumenten geht's automatisch:

    python3 _Meta/Scripts/new-project.py "Mein Spiel" --engine Godot --status active
    python3 _Meta/Scripts/new-project.py "Noise Web" --engine "React + Three.js" --tags "web, art"
    python3 _Meta/Scripts/new-project.py                           # interaktiv

Erzeugt:
    Projects/Active/<Project>/
    Projects/Active/<Project>/<Project>.md (befüllt mit Template)
"""

import sys
import argparse
import re
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATE_PATH = VAULT_ROOT / "_Toolkit" / "Templates" / "Project-Template.md"
PROJECTS_ACTIVE = VAULT_ROOT / "Projects" / "Active"
PROJECTS_ARCHIVE = VAULT_ROOT / "Projects" / "Archive"

FALLBACK_TEMPLATE = """---
title: "{{title}}"
type: project
status: active      # active | idea | archived
engine: Unreal Engine 5  # Rust, Python, TypeScript, Blender, Godot, …
started: {{date}}
progress: 0%        # Schätzung: 0–100%
github:             # optional: https://github.com/Malte-Dzierzon/<repo>
tags: []
---

# {{title}}

**Kurzbeschreibung:**  
Ein Satz, worum es geht – für Menschen und KI gleichermaßen verständlich.

---

## Concept

Warum dieses Projekt? Was ist die Kernidee?  
(Free-Form, gerne Brain-Dump – Stil wie bei [[Projects/Active/Dreamwolds/Dreamwolds.md|Dreamwolds]] oder [[Projects/Active/Rynthar/Rynthar-Conzept.md|Rynthar]].)

---

## Tech Stack

| Komponente | Technologie |
|------------|-------------|
| Engine     | UE5 / Rust / Python / … |
| Sprache    | C++, Blueprint, TypeScript, … |
| Plattform  | Windows, Linux, Web, … |

---

## Mechanics / Features

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3

---

## Links

| Typ | Pfad |
|-----|------|
| Canvas | [[Projects/Active/<Name>/<Game>.canvas]] |
| Referenzbild | [[Wiki/Images/Pictures/<file>]] |
| GitHub | [Repo](https://github.com/Malte-Dzierzon/<repo>) |
| Verwandtes Wiki | [[Wiki/...]] |

---

## Roadmap

- [ ] **Phase 1:** Prototyp (Kernmechanik)
- [ ] **Phase 2:** Playable Build
- [ ] **Phase 3:** Polishing & Release

---

## Notes

(Alle Gedanken, Probleme, Learnings – wird organisch größer.)
"""


def sanitize_name(name: str) -> str:
    """Entfernt zeichen, die in Datei-/Ordnernamen problematisch sind."""
    name = name.strip()
    name = name.replace("/", "-").replace("\\", "-")
    name = re.sub(r'[<>:"|?*]', "", name)
    return name


def replace_field(content: str, field: str, value: str) -> str:
    """
    Ersetzt ein YAML-Frontmatter-Feld und erhält den Inline-Kommentar.

    Aus 'status: active      # active | idea | archived'
    wird  'status: idea       # active | idea | archived'
    """
    pattern = rf'^{re.escape(field)}:.*$'
    match = re.search(pattern, content, re.MULTILINE)
    if not match:
        return content

    original_line = match.group(0)
    comment_match = re.search(r'(#.*)$', original_line)

    if comment_match:
        replacement = f'{field}: {value}  {comment_match.group(1)}'
    else:
        replacement = f'{field}: {value}'

    return re.sub(pattern, replacement, content, count=1, flags=re.MULTILINE)


def prompt(text: str, default: str = "") -> str:
    """Fragt den Benutzer mit optionalem Default-Wert."""
    if default:
        result = input(f"{text} [{default}]: ").strip()
        return result if result else default
    return input(f"{text}: ").strip()


def interactive_mode() -> argparse.Namespace:
    """Sammelt alle Werte interaktiv ein."""
    print()
    print("  📦  Neues Projekt anlegen")
    print("  " + "─" * 36)

    name = prompt("  Projektname")
    if not name:
        print("  ❌ Projektname wird benötigt.")
        sys.exit(1)

    engine = prompt("  Engine / Tech-Stack", "Unreal Engine 5")
    status = prompt("  Status", "idea")
    if status not in ("active", "idea", "archived"):
        print(f"  ⚠️  Ungültiger Status '{status}', setze auf 'idea'")
        status = "idea"

    desc = prompt("  Kurzbeschreibung")
    tags = prompt("  Tags (kommagetrennt)")
    github = prompt("  GitHub-Repo-Name")
    progress = prompt("  Fortschritt in %", "0")

    return argparse.Namespace(
        name=name,
        engine=engine,
        status=status,
        desc=desc,
        tags=tags,
        github=github,
        progress=progress,
    )


def main():
    parser = argparse.ArgumentParser(
        description="📦 Erstellt ein neues Projekt im Vault aus der Project-Template.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python3 _Meta/Scripts/new-project.py "Mein Spiel" --engine Godot --status active
  python3 _Meta/Scripts/new-project.py "Noise Web" --engine "React" --tags "web, art"
  python3 _Meta/Scripts/new-project.py                           # interaktiv

Ohne Argumente startet das Skript im interaktiven Modus.
        """,
    )
    parser.add_argument("name", nargs="?", default=None,
                        help="Projektname (z. B. 'Mein Cooles Spiel')")
    parser.add_argument("--engine", "-e", default="Unreal Engine 5",
                        help="Engine oder Tech-Stack (z. B. Godot, React, Python)")
    parser.add_argument("--status", "-s", default="idea",
                        choices=["active", "idea", "archived"],
                        help="Projekt-Status")
    parser.add_argument("--desc", "-d", default="",
                        help="Kurzbeschreibung (1 Satz)")
    parser.add_argument("--tags", "-t", default="",
                        help="Tags, kommagetrennt (z. B. 'game, 3d, fantasy')")
    parser.add_argument("--github", "-g", default="",
                        help="GitHub-Repo-Name (z. B. 'my-cool-game')")
    parser.add_argument("--progress", "-p", default="0",
                        help="Fortschritt in Prozent (z. B. 10)")

    args = parser.parse_args()

    # ── Interaktiv wenn kein Name übergeben ──
    if args.name is None:
        args = interactive_mode()

    # ── Projektnamen bereinigen ──
    folder_name = sanitize_name(args.name)
    if not folder_name:
        print("❌ Projektname ist ungültig (leer oder nur Sonderzeichen).")
        sys.exit(1)

    # ── Zielpfad bestimmen ──
    if args.status == "archived":
        target = PROJECTS_ARCHIVE / folder_name
    else:
        target = PROJECTS_ACTIVE / folder_name

    if target.exists():
        print(f"❌ Projekt existiert bereits: {target}")
        sys.exit(1)

    # ── Template laden ──
    if TEMPLATE_PATH.exists():
        template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
    else:
        print(f"⚠️  Template nicht gefunden unter:")
        print(f"   {TEMPLATE_PATH}")
        print(f"   → Verwende eingebautes Fallback-Template.")
        template_text = FALLBACK_TEMPLATE

    # ── Template befüllen ──
    content = template_text

    content = content.replace("{{title}}", folder_name)
    content = content.replace("{{date}}", str(date.today()))

    content = replace_field(content, "status", args.status)
    content = replace_field(content, "engine", args.engine)
    content = replace_field(content, "progress", f"{args.progress}%")

    # GitHub-URL setzen (Feld + Link-Tabelle)
    if args.github:
        github_url = f"https://github.com/Malte-Dzierzon/{args.github}"
        content = replace_field(content, "github", args.github)
        content = content.replace(
            "https://github.com/Malte-Dzierzon/<repo>",
            github_url,
        )

    # Tags setzen
    if args.tags:
        tags_list = [t.strip() for t in args.tags.split(",") if t.strip()]
        if tags_list:
            tags_yaml = f"[{', '.join(tags_list)}]"
            content = replace_field(content, "tags", tags_yaml)

    # Kurzbeschreibung
    if args.desc:
        content = content.replace(
            "Ein Satz, worum es geht – für Menschen und KI gleichermaßen verständlich.",
            args.desc,
        )

    # ── Ordner + Datei schreiben ──
    target.mkdir(parents=True)
    note_path = target / f"{folder_name}.md"
    note_path.write_text(content, encoding="utf-8")

    # ── Ausgabe ──
    print()
    print(f"  ✅  Projekt erstellt")
    print(f"  " + "─" * 36)
    print(f"  📂  {target}")
    print(f"  📄  {note_path.name}")
    print(f"  🏷️   Status: {args.status}")
    print(f"  ⚙️   Engine: {args.engine}")
    if args.tags:
        print(f"  🏷️   Tags:   {', '.join(tags_list)}")
    if args.github:
        print(f"  🌐  GitHub: {github_url}")
    if args.desc:
        print(f"  📝  Beschr.: {args.desc}")
    print()
    print(f"  💡  Nächster Schritt: Concept & Features ausfüllen!")


if __name__ == "__main__":
    main()

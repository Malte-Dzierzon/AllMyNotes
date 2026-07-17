#!/usr/bin/env python3
"""
new-project.py  --  Neues Projekt im Vault anlegen

Usage:
    new-project                                # interaktiv
    new-project "Mein Spiel" --engine Godot    # via CLI
    new-project "Noise Web" --engine "React"   # Web-Projekt
"""

import sys
import argparse
import re
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _shared.ui import header, section, ok, fail, tip, keyval, spacer, hr, prompt, list_items

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
progress: 0%        # Schaetzung: 0-100%
github:             # optional: https://github.com/Malte-Dzierzon/<repo>
tags: []
---

# {{title}}

**Kurzbeschreibung:**
Ein Satz, worum es geht - fuer Menschen und KI gleichermassen verstaendlich.

---

## Concept

Warum dieses Projekt? Was ist die Kernidee?
(Free-Form, gerne Brain-Dump)

---

## Tech Stack

| Komponente | Technologie |
|------------|-------------|
| Engine     | UE5 / Rust / Python / ... |
| Sprache    | C++, Blueprint, TypeScript, ... |
| Plattform  | Windows, Linux, Web, ... |

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

(Alle Gedanken, Probleme, Learnings - wird organisch groesser.)
"""


def sanitize_name(name: str) -> str:
    name = name.strip()
    name = name.replace("/", "-").replace("\\", "-")
    name = re.sub(r'[<>:"|?*]', "", name)
    return name


def replace_field(content: str, field: str, value: str) -> str:
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


def interactive_mode() -> argparse.Namespace:
    header("New Project  -  Interactive")
    name = prompt("Project name")
    if not name:
        fail("Project name required.")
        sys.exit(1)
    engine = prompt("Engine / Tech stack", "Unreal Engine 5")
    status = prompt("Status", "idea")
    if status not in ("active", "idea", "archived"):
        fail(f"Invalid status '{status}', using 'idea'")
        status = "idea"
    desc = prompt("Short description")
    tags = prompt("Tags (comma-separated)")
    github = prompt("GitHub repo name (optional)")
    progress = prompt("Progress in %", "0")
    return argparse.Namespace(name=name, engine=engine, status=status,
                              desc=desc, tags=tags, github=github, progress=progress)


def main():
    parser = argparse.ArgumentParser(
        description="Create a new project in the vault from Project-Template.md",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("name", nargs="?", default=None, help="Project name")
    parser.add_argument("--engine", "-e", default="Unreal Engine 5", help="Engine or tech stack")
    parser.add_argument("--status", "-s", default="idea", choices=["active", "idea", "archived"], help="Project status")
    parser.add_argument("--desc", "-d", default="", help="Short description (1 sentence)")
    parser.add_argument("--tags", "-t", default="", help="Tags, comma-separated (e.g. 'game, 3d')")
    parser.add_argument("--github", "-g", default="", help="GitHub repo name")
    parser.add_argument("--progress", "-p", default="0",
                        help="Progress in percent (e.g. 10)")
    args = parser.parse_args()
    if args.name is None:
        args = interactive_mode()

    folder_name = sanitize_name(args.name)
    if not folder_name:
        fail("Invalid project name (empty or only special characters).")
        sys.exit(1)

    target = PROJECTS_ARCHIVE / folder_name if args.status == "archived" else PROJECTS_ACTIVE / folder_name
    if target.exists():
        fail(f"Project already exists: {target}")
        sys.exit(1)

    # Template laden
    if TEMPLATE_PATH.exists():
        content = TEMPLATE_PATH.read_text(encoding="utf-8")
    else:
        fail(f"Template not found: {TEMPLATE_PATH}")
        tip("Using built-in fallback template.")
        content = FALLBACK_TEMPLATE

    # Ersetzungen
    content = content.replace("{{title}}", folder_name)
    content = content.replace("{{date}}", str(date.today()))
    content = replace_field(content, "status", args.status)
    content = replace_field(content, "engine", args.engine)
    content = replace_field(content, "progress", f"{args.progress}%")

    github_url = None
    if args.github:
        github_url = f"https://github.com/Malte-Dzierzon/{args.github}"
        content = replace_field(content, "github", args.github)
        content = content.replace("https://github.com/Malte-Dzierzon/<repo>", github_url)

    if args.tags:
        tags_list = [t.strip() for t in args.tags.split(",") if t.strip()]
        if tags_list:
            content = replace_field(content, "tags", f"[{', '.join(tags_list)}]")

    if args.desc:
        content = content.replace(
            "Ein Satz, worum es geht - fuer Menschen und KI gleichermassen verstaendlich.",
            args.desc,
        )

    # Schreiben
    target.mkdir(parents=True)
    note_path = target / f"{folder_name}.md"
    note_path.write_text(content, encoding="utf-8")

    # Ausgabe
    header("New Project  -  Created")
    keyval("Folder", str(target))
    keyval("File", note_path.name)
    hr()
    keyval("Status", args.status)
    keyval("Engine", args.engine)
    if args.tags:
        keyval("Tags", ", ".join(tags_list))
    if github_url:
        keyval("GitHub", github_url)
    if args.desc:
        keyval("Description", args.desc)
    spacer()
    tip("Next: fill in Concept & Features in the new note.")


if __name__ == "__main__":
    main()

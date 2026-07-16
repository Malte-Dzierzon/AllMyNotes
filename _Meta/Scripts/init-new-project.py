#!/usr/bin/env python3
"""
init-new-project.py – Erstellt ein neues Projekt im Vault.

Usage:
    python3 _Meta/Scripts/init-new-project.py "Mein Projekt" --engine UE5 --status idea

Erzeugt:
    Projects/Active/Mein Projekt/
    Projects/Active/Mein Projekt/Mein Projekt.md (befüllt mit Template)
"""

import os
import sys
import argparse
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATE_PATH = VAULT_ROOT / "_Meta" / "Templates" / "Project-Template.md"
PROJECTS_ACTIVE = VAULT_ROOT / "Projects" / "Active"
PROJECTS_ARCHIVE = VAULT_ROOT / "Projects" / "Archive"


def main():
    parser = argparse.ArgumentParser(description="Create a new project in the vault")
    parser.add_argument("name", help="Project name (e.g. 'My Cool Game')")
    parser.add_argument("--engine", default="Unreal Engine 5", help="Engine or tech stack")
    parser.add_argument("--status", default="idea", choices=["active", "idea", "archived"])
    parser.add_argument("--desc", default="", help="Short description (1 sentence)")
    args = parser.parse_args()

    folder_name = args.name.strip()
    if args.status == "archived":
        target = PROJECTS_ARCHIVE / folder_name
    else:
        target = PROJECTS_ACTIVE / folder_name

    if target.exists():
        print(f"❌ Project already exists: {target}")
        sys.exit(1)

    target.mkdir(parents=True)
    note_path = target / f"{folder_name}.md"

    # Read template
    template_text = TEMPLATE_PATH.read_text() if TEMPLATE_PATH.exists() else ""
    if not template_text:
        # fallback
        template_text = "---\ntitle: {title}\nstatus: {status}\nengine: {engine}\nstarted: {date}\n---\n\n# {title}\n\n{desc}\n"

    # Fill template
    content = (
        template_text
        .replace("{{title}}", folder_name)
        .replace("{{date}}", str(date.today()))
        .replace("# active", f"# {args.status}")
        .replace("Unreal Engine 5", args.engine)
    )
    # Replace the status field
    import re
    content = re.sub(r'status: active', f'status: {args.status}', content, count=1)

    if args.desc:
        # Replace the Kurzbeschreibung placeholder
        content = content.replace("Ein Satz, worum es geht", args.desc)

    note_path.write_text(content)
    print(f"✅ Project created: {note_path}")
    print(f"   Status: {args.status}")
    print(f"   Engine: {args.engine}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
archive-project.py – Projekte archivieren (Active → Archive).

Usage:
    archive-project                      # Interaktiv: Liste aller aktiven Projekte
    archive-project "Bow Shooter"        # Bestimmtes Projekt archivieren
    archive-project --list               # Nur anzeigen, nichts archivieren

Verschiebt das Projekt von Projects/Active/<Name> → Projects/Archive/<Name>
und setzt den YAML-Status auf 'archived' + completed-Datum.
"""

import sys
import shutil
import argparse
from datetime import date
from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
PROJECTS_ACTIVE = VAULT_ROOT / "Projects" / "Active"
PROJECTS_ARCHIVE = VAULT_ROOT / "Projects" / "Archive"


def get_active_projects() -> list[tuple[str, Path]]:
    """Gibt alle aktiven Projekte als (Name, Pfad) zurück."""
    projects = []
    if not PROJECTS_ACTIVE.exists():
        return projects
    for folder in sorted(PROJECTS_ACTIVE.iterdir()):
        if folder.is_dir():
            # Prüfen, ob eine .md-Datei mit dem gleichen Namen existiert
            md_file = folder / f"{folder.name}.md"
            if md_file.exists():
                projects.append((folder.name, folder))
    return projects


def list_projects(projects: list):
    """Zeigt alle aktiven Projekte an."""
    if not projects:
        print("📭  Keine aktiven Projekte gefunden.")
        return

    print()
    print("  📂  Aktive Projekte")
    print("  " + "─" * 44)
    for i, (name, path) in enumerate(projects, 1):
        print(f"  {i:2d})  {name}")
    print(f"\n  Gesamt: {len(projects)} Projekte")


def archive_project(project_name: str) -> bool:
    """Archiviert ein Projekt: Verschieben + YAML updaten."""
    source = PROJECTS_ACTIVE / project_name
    md_file = source / f"{project_name}.md"
    dest = PROJECTS_ARCHIVE / project_name
    dest_md = dest / f"{project_name}.md"

    if not source.exists():
        print(f"❌  Projekt nicht gefunden: {source}")
        print(f"   Verfügbare Projekte:")
        for name, _ in get_active_projects():
            print(f"   - {name}")
        return False

    if not md_file.exists():
        print(f"❌  Keine Projektdatei gefunden: {md_file}")
        return False

    if dest.exists():
        print(f"⚠️  Ziel existiert bereits: {dest}")
        yn = input("   Überschreiben? [y/N]: ").strip().lower()
        if yn != "y":
            print("   Abgebrochen.")
            return False
        shutil.rmtree(dest)

    # YAML-Status in der .md-Datei updaten (vor dem Verschieben)
    content = md_file.read_text(encoding="utf-8")
    today = date.today().isoformat()

    # status: active → status: archived
    import re
    content = re.sub(
        r'^status:\s*active.*$',
        f'status: archived  # active | idea | archived',
        content,
        count=1,
        flags=re.MULTILINE,
    )

    # completed: ... hinzufügen (vor started: oder am Ende des Frontmatters)
    if "completed:" not in content:
        content = re.sub(
            r'^(started:.*)$',
            f'\\1\ncompleted: {today}',
            content,
            count=1,
            flags=re.MULTILINE,
        )
    else:
        content = re.sub(
            r'^completed:.*$',
            f'completed: {today}',
            content,
            count=1,
            flags=re.MULTILINE,
        )

    # Aktualisierte Datei schreiben
    md_file.write_text(content, encoding="utf-8")

    # Ordner verschieben
    try:
        source.rename(dest)
    except OSError:
        # Fallback: kopieren + löschen (bei Cross-Filesystem)
        shutil.copytree(source, dest)
        shutil.rmtree(source)

    print()
    print(f"  ✅  Projekt archiviert")
    print(f"  " + "─" * 44)
    print(f"  📂  {source}")
    print(f"  ➡️  {dest}")
    print(f"  🏷️   Status:   archived")
    print(f"  📅  Abgeschlossen: {today}")
    print()
    print(f"  💡  Nächster Schritt: Projects-Dashboard aktualisieren")
    return True


def interactive_mode():
    """Interaktiver Modus: Projekt aus Liste auswählen."""
    projects = get_active_projects()
    if not projects:
        print("📭  Keine aktiven Projekte zu archivieren.")
        return

    list_projects(projects)
    print()

    try:
        choice = input("  Projektnummer oder Name (Enter = abbrechen): ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n  👋  Abgebrochen.")
        return

    if not choice:
        print("  👋  Abgebrochen.")
        return

    # Nummer → Name
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(projects):
            archive_project(projects[idx][0])
        else:
            print(f"❌  Ungültige Nummer: {choice}")
        return

    # Direkter Name
    archive_project(choice)


def main():
    parser = argparse.ArgumentParser(
        description="📦 Archiviert ein Projekt (Active → Archive)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  archive-project                        # Interaktiv
  archive-project "Bow Shooter"          # Bestimmtes Projekt
  archive-project --list                 # Nur anzeigen
        """,
    )
    parser.add_argument("name", nargs="?", default=None,
                        help="Projektname (z. B. 'Bow Shooter')")
    parser.add_argument("--list", "-l", action="store_true",
                        help="Nur aktive Projekte anzeigen, nichts archivieren")

    args = parser.parse_args()

    if args.list:
        list_projects(get_active_projects())
        return

    if args.name:
        archive_project(args.name)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()

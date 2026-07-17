#!/usr/bin/env python3
"""
archive-project.py  --  Projekt archivieren (Active in Archive).

Usage:
    archive-project                      # Interaktiv
    archive-project "Bow Shooter"        # Bestimmtes Projekt
    archive-project --list               # Nur anzeigen
"""

import sys
import shutil
import argparse
import re
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _shared.ui import header, section, ok, fail, info, tip, keyval, spacer, hr, prompt

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
PROJECTS_ACTIVE = VAULT_ROOT / "Projects" / "Active"
PROJECTS_ARCHIVE = VAULT_ROOT / "Projects" / "Archive"


def get_active_projects() -> list[tuple[str, Path]]:
    if not PROJECTS_ACTIVE.exists():
        return []
    result = []
    for folder in sorted(PROJECTS_ACTIVE.iterdir()):
        if folder.is_dir():
            md = folder / f"{folder.name}.md"
            if md.exists():
                result.append((folder.name, folder))
    return result


def list_projects(projects: list):
    if not projects:
        info("No active projects found.")
        return
    header("Active Projects")
    for i, (name, _) in enumerate(projects, 1):
        print(f"  {i:2d})  {name}")
    spacer()
    info(f"{len(projects)} project(s) total")


def archive(project_name: str) -> bool:
    src = PROJECTS_ACTIVE / project_name
    md_src = src / f"{project_name}.md"
    dst = PROJECTS_ARCHIVE / project_name

    if not src.exists():
        fail(f"Project not found: {project_name}")
        projects = get_active_projects()
        if projects:
            info("Active projects:")
            for name, _ in projects:
                print(f"     {name}")
        return False

    if dst.exists():
        fail(f"Target already exists: {dst}")
        yn = prompt("Overwrite?", "N")
        if yn.lower() != "y":
            info("Cancelled.")
            return False
        shutil.rmtree(dst)

    # YAML updaten
    content = md_src.read_text(encoding="utf-8")
    today = date.today().isoformat()

    content = re.sub(
        r'^status:\s*active.*$',
        'status: archived  # active | idea | archived',
        content, count=1, flags=re.MULTILINE,
    )
    if "completed:" not in content:
        content = re.sub(
            r'^(started:.*)$',
            f'\\1\ncompleted: {today}',
            content, count=1, flags=re.MULTILINE,
        )
    else:
        content = re.sub(
            r'^completed:.*$',
            f'completed: {today}',
            content, count=1, flags=re.MULTILINE,
        )
    md_src.write_text(content, encoding="utf-8")

    # Verschieben
    try:
        src.rename(dst)
    except OSError:
        shutil.copytree(src, dst)
        shutil.rmtree(src)

    header("Archive Project  -  Done")
    keyval("From", str(src))
    keyval("To",   str(dst))
    hr()
    keyval("Status", "archived")
    keyval("Completed", today)
    spacer()
    tip("Update the Projects dashboard (00-Overview/Projects.md).")
    return True


def interactive_mode():
    projects = get_active_projects()
    if not projects:
        info("No active projects to archive.")
        return

    list_projects(projects)
    choice = prompt("Project number or name (enter to cancel)")

    if not choice:
        info("Cancelled.")
        return
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(projects):
            archive(projects[idx][0])
        else:
            fail(f"Invalid number: {choice}")
        return
    archive(choice)


def main():
    parser = argparse.ArgumentParser(description="Archive a project (Active -> Archive)")
    parser.add_argument("name", nargs="?", default=None, help="Project name")
    parser.add_argument("--list", "-l", action="store_true", help="List active projects only")
    args = parser.parse_args()

    if args.list:
        list_projects(get_active_projects())
        return
    if args.name:
        archive(args.name)
    else:
        interactive_mode()


if __name__ == "__main__":
    main()

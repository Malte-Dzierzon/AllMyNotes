#!/usr/bin/env python3
"""
toolkit.py – _Toolkit Launcher

Zentrale Einstiegsdatei für alle Vault-Tools.
Sowohl interaktiv (Menü) als auch per CLI (für KI-Agenten) nutzbar.

Usage:
    toolkit                          # Interaktives Menü
    toolkit list                     # Alle Tools anzeigen
    toolkit <tool>                   # Tool direkt starten (interaktiv)
    toolkit <tool> --help            # Hilfe zu einem Tool
    toolkit <tool> <arg1> <arg2>     # Tool mit Argumenten starten
"""

import sys
import subprocess
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _shared.ui import header, list_items, ok, fail, prompt, spacer

TOOLKIT_DIR = Path(__file__).parent

TOOLS = {
    "new-project": {
        "path": "new-project/new-project.py",
        "desc": "Neues Projekt anlegen (Template + Ordner)",
    },
    "vault-stats": {
        "path": "vault-stats/vault-stats.py",
        "desc": "Vault-Statistiken (Dateien, Todos, Woerter)",
    },
    "research": {
        "path": "research/research.py",
        "desc": "Research-Aufgaben erstellen und verwalten",
    },
    "archive-project": {
        "path": "archive-project/archive-project.py",
        "desc": "Projekt archivieren (Active in Archive)",
    },
}

ORDER = ["new-project", "vault-stats", "research", "archive-project"]


def run_tool(name: str, args: list = None) -> None:
    """Startet ein Tool-Skript als Subprozess."""
    if name not in TOOLS:
        fail(f"Unbekanntes Tool: '{name}'")
        print(f"   Verfuegbar: {', '.join(TOOLS.keys())}")
        sys.exit(1)

    script = TOOLKIT_DIR / TOOLS[name]["path"]
    if not script.exists():
        fail(f"Skript nicht gefunden: {script}")
        sys.exit(1)

    cmd = [sys.executable, str(script)]
    if args:
        cmd.extend(args)

    sys.exit(subprocess.run(cmd).returncode)


def show_menu() -> None:
    """Interaktives Menue anzeigen."""
    header("_Toolkit  -  Vault Automation Suite")

    items = [f"{name:<18}  {t['desc']}" for name, t in TOOLS.items()]
    list_items(items, numbered=True)

    spacer()
    print(f"  l)  list        Alle Tools anzeigen")
    print(f"  q)  quit        Beenden")
    spacer()

    choice = prompt("Auswahl").lower()

    if choice in ("q", "", "quit"):
        print("  Tschuess!")
        return
    if choice in ("l", "list"):
        show_list()
        return
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(ORDER):
            run_tool(ORDER[idx])
            return
        fail(f"Ungueltige Auswahl: {choice}")
        return
    if choice in TOOLS:
        run_tool(choice)
        return

    fail(f"Ungueltige Auswahl: '{choice}'")
    show_menu()


def show_list() -> None:
    """Listet alle Tools auf (fuer KI-Agenten und Menschen)."""
    header("_Toolkit  -  Available Tools")
    for name in ORDER:
        t = TOOLS[name]
        print(f"  {name:<20}  {t['desc']}")
    spacer()
    print(f"  Usage:  toolkit <tool> [args]")
    print(f"  e.g.:   toolkit new-project --help")
    spacer()


def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd in ("list", "--list"):
            show_list()
            return
        if cmd in TOOLS:
            run_tool(cmd, sys.argv[2:] if len(sys.argv) > 2 else None)
            return
        if cmd in ("-h", "--help"):
            print(__doc__.strip())
            return
        fail(f"Unbekanntes Kommando: '{cmd}'")
        print(f"   Usage: toolkit [list | <tool> [args] | --help]")
        sys.exit(1)

    show_menu()


if __name__ == "__main__":
    main()

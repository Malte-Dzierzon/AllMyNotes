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

Beispiele:
    toolkit                          # → Menü öffnen
    toolkit new-project "Mein Spiel" # → Projekt anlegen
    toolkit vault-stats --json       # → Statistik als JSON
    toolkit archive-project "Bow Shooter"  # → Projekt archivieren
"""

import sys
import subprocess
from pathlib import Path

TOOLKIT_DIR = Path(__file__).parent

TOOLS = {
    "new-project": {
        "path": "new-project/new-project.py",
        "desc": "Neues Projekt anlegen (Template + Ordner)",
    },
    "vault-stats": {
        "path": "vault-stats/vault-stats.py",
        "desc": "Vault-Statistiken (Dateien, Todos, Wörter)",
    },
    "research": {
        "path": "research/research.py",
        "desc": "Research-Aufgaben erstellen und verwalten",
    },
    "archive-project": {
        "path": "archive-project/archive-project.py",
        "desc": "Projekt archivieren (Active → Archive)",
    },
}

ORDER = ["new-project", "vault-stats", "research", "archive-project"]


def print_header(title: str):
    """Einheitlicher Header für bessere Lesbarkeit."""
    print()
    print(f"  {title}")
    print("  " + "─" * 44)


def run_tool(name: str, args: list = None):
    """Startet ein Tool-Skript als Subprozess."""
    if name not in TOOLS:
        print(f"❌  Unbekanntes Tool: '{name}'")
        print(f"   Verfügbare Tools: {', '.join(TOOLS.keys())}")
        sys.exit(1)

    script = TOOLKIT_DIR / TOOLS[name]["path"]
    if not script.exists():
        print(f"❌  Skript nicht gefunden: {script}")
        sys.exit(1)

    cmd = [sys.executable, str(script)]
    if args:
        cmd.extend(args)

    sys.exit(subprocess.run(cmd).returncode)


def show_menu():
    """Interaktives Menü anzeigen und Tool auswählen."""
    print_header("🧰  _Toolkit – Vault-Werkzeuge")

    for i, name in enumerate(ORDER, 1):
        tool = TOOLS[name]
        print(f"  {i})  {name:<18}  {tool['desc']}")
    print(f"  l)  list                 Alle Tools anzeigen")
    print(f"  q)  quit                 Beenden")
    print()

    try:
        choice = input("  Auswahl: ").strip().lower()
    except (EOFError, KeyboardInterrupt):
        print("\n  👋  Tschüss!")
        return

    if choice == "q" or choice == "":
        print("  👋  Tschüss!")
        return
    if choice == "l":
        print_tools()
        return

    # Zahl → Tool-Name
    if choice.isdigit():
        idx = int(choice) - 1
        if 0 <= idx < len(ORDER):
            run_tool(ORDER[idx])
        else:
            print(f"  ❌  Ungültige Auswahl: {choice}")
        return

    # Name → Tool
    if choice in TOOLS:
        run_tool(choice)
        return

    print(f"  ❌  Ungültige Auswahl: '{choice}'")
    print(f"     Verfügbar: 1–{len(ORDER)}, l(list), q(quit) oder Name")


def print_tools():
    """Listet alle Tools auf (für KI-Agenten und Menschen)."""
    print_header("🧰  _Toolkit – Verfügbare Tools")
    print()
    for name in ORDER:
        tool = TOOLS[name]
        print(f"  {name:<20}  {tool['desc']}")
    print()
    print("  Usage:  toolkit <tool> [args]")
    print("  Z.B.:   toolkit new-project --help")
    print("  Menü:   toolkit (ohne Argumente)")
    print()


def main():
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "list" or cmd == "--list":
            print_tools()
            return
        if cmd in TOOLS:
            # toolname [args...]
            run_tool(cmd, sys.argv[2:] if len(sys.argv) > 2 else None)
            return
        if cmd in ("-h", "--help"):
            # Haupt-Hilfe
            print(__doc__.strip())
            return
        print(f"❌  Unbekanntes Kommando: '{cmd}'")
        print(f"   Usage: toolkit [list | toolname | --help]")
        print(f"   Tools: {', '.join(TOOLS.keys())}")
        sys.exit(1)

    # Keine Argumente → interaktives Menü
    show_menu()


if __name__ == "__main__":
    main()

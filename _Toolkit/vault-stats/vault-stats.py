#!/usr/bin/env python3
"""
vault-stats.py – Zeigt Statistiken über den Vault an.

Usage:
    vault-stats                          # Interaktiv (schöne Tabelle)
    vault-stats --json                   # Maschinenlesbar (JSON)
    vault-stats --watch 60               # Alle 60s neu laden
    vault-stats --watch 10 --json        # Watch + JSON kombiniert
    
Ohne Flags zeigt das Skript eine übersichtliche Statistik-Tabelle an.
"""

import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
IGNORE_DIRS = {".git", ".obsidian", "__pycache__", "node_modules"}
IGNORE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".exe", ".json", ".js", ".css", ".map"}


def scan_vault() -> dict:
    """Scannt den Vault und gibt ein Statistik-Dict zurück."""
    counts = {"md": 0, "canvas": 0, "base": 0, "excalidraw": 0, "other": 0, "total": 0}
    word_count = 0
    todo_count = 0
    by_folder = {}

    for fpath in VAULT_ROOT.rglob("*"):
        if any(part.startswith(".") for part in fpath.parts):
            continue
        if any(part in IGNORE_DIRS for part in fpath.parts):
            continue
        if fpath.is_dir():
            continue
        if fpath.suffix.lower() in IGNORE_EXTS:
            continue

        counts["total"] += 1
        rel = fpath.relative_to(VAULT_ROOT)
        folder = str(rel.parent)

        if fpath.suffix == ".md":
            counts["md"] += 1
            if ".excalidraw" in fpath.name:
                counts["excalidraw"] += 1
            try:
                text = fpath.read_text(encoding="utf-8", errors="ignore")
                word_count += len(text.split())
                todo_count += text.count("- [ ]")
            except Exception:
                pass
        elif fpath.suffix == ".canvas":
            counts["canvas"] += 1
        elif fpath.suffix in (".base", ".db"):
            counts["base"] += 1
        else:
            counts["other"] += 1

        by_folder[folder] = by_folder.get(folder, 0) + 1

    # Top-Level-Ordner zusammenfassen
    top_folders = {}
    for folder, count in sorted(by_folder.items()):
        top = folder.split("/")[0] if "/" in folder else folder
        top_folders[top] = top_folders.get(top, 0) + count

    return {
        "counts": counts,
        "word_count": word_count,
        "todo_count": todo_count,
        "by_folder": sorted(by_folder.items()),
        "top_folders": sorted(top_folders.items()),
        "scanned_at": datetime.now().isoformat(),
    }


def print_human(data: dict):
    """Gibt eine menschenlesbare Statistik aus."""
    c = data["counts"]
    print()
    print("  📊  Vault-Statistiken")
    print("  " + "─" * 40)
    print(f"  📄  Markdown:        {c['md']:>5}  ({c['excalidraw']} Excalidraw)")
    print(f"  🖼️   Canvas:          {c['canvas']:>5}")
    print(f"  🗄️   Dataview/Base:   {c['base']:>5}")
    print(f"  📦  Sonstige:        {c['other']:>5}")
    print(f"  ─────────────────────────")
    print(f"  📊  Gesamt:          {c['total']:>5} Dateien")
    print(f"  📝  Wörter:          {data['word_count']:>8}")
    print(f"  ✅  Offene Todos:    {data['todo_count']:>5}")
    print()
    print("  📂  Dateien pro Bereich:")
    for folder, count in data.get("top_folders", data["by_folder"]):
        bar = "█" * min(count, 30)
        print(f"  {folder:<20} {count:>4}  {bar}")


def print_json(data: dict):
    """Gibt die Statistik als JSON aus."""
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="📊 Zeigt Statistiken über den Obsidian-Vault an",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  vault-stats                    # Normale Anzeige
  vault-stats --json             # Als JSON (für Scripte)
  vault-stats --watch 30         # Alle 30s aktualisieren
        """,
    )
    parser.add_argument("--json", action="store_true",
                        help="Ausgabe als JSON (maschinenlesbar)")
    parser.add_argument("--watch", "-w", type=int, default=0, metavar="N",
                        help="Alle N Sekunden neu laden (z. B. --watch 30)")

    args = parser.parse_args()

    if args.watch > 0:
        # Watch-Modus: Alle N Sekunden neu scannen
        try:
            while True:
                data = scan_vault()
                if args.json:
                    print_json(data)
                else:
                    print_human(data)
                print(f"\n  🔄  Aktualisiert: {data['scanned_at']}")
                print(f"  ⏱️   Nächstes Update in {args.watch}s  (Strg+C zum Beenden)")
                time.sleep(args.watch)
        except KeyboardInterrupt:
            print("\n  👋  Beendet.")
    else:
        data = scan_vault()
        if args.json:
            print_json(data)
        else:
            print_human(data)


if __name__ == "__main__":
    main()

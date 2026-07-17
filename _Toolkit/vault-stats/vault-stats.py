#!/usr/bin/env python3
"""
vault-stats.py  --  Vault-Statistiken anzeigen

Usage:
    vault-stats                     # Uebersichtstabelle
    vault-stats --json              # Maschinenlesbar (JSON)
    vault-stats --watch 30          # Alle 30s neu laden
"""

import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from _shared.ui import header, section, ok, keyval, spacer, hr, info, Spinner

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent
IGNORE_DIRS = {".git", ".obsidian", "__pycache__", "node_modules"}
IGNORE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".exe", ".json", ".js", ".css", ".map"}


def scan_vault() -> dict:
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

    top_folders = {}
    for folder, count in sorted(by_folder.items()):
        top = folder.split("/")[0] if "/" in folder else folder
        top_folders[top] = top_folders.get(top, 0) + count

    return {
        "counts": counts,
        "word_count": word_count,
        "todo_count": todo_count,
        "top_folders": sorted(top_folders.items()),
        "scanned_at": datetime.now().isoformat(),
    }


def print_human(data: dict):
    c = data["counts"]
    header("Vault Statistics")
    keyval("Markdown",     f"{c['md']:>5}  ({c['excalidraw']} excalidraw)")
    keyval("Canvas",       f"{c['canvas']:>5}")
    keyval("Dataview",     f"{c['base']:>5}")
    keyval("Other",        f"{c['other']:>5}")
    hr()
    keyval("Total files",  f"{c['total']:>5}")
    keyval("Word count",   f"{data['word_count']:>8,}")
    keyval("Open TODOs",   f"{data['todo_count']:>5}")
    spacer()
    section("Files by area")
    for folder, count in data["top_folders"]:
        bar = chr(0x2588) * min(count, 30)
        print(f"  {folder:<20} {count:>4}  {bar}")


def print_json(data: dict):
    print(json.dumps(data, ensure_ascii=False, indent=2))


def main():
    parser = argparse.ArgumentParser(description="Vault statistics overview")
    parser.add_argument("--json", action="store_true", help="JSON output (machine-readable)")
    parser.add_argument("--watch", "-w", type=int, default=0, metavar="N",
                        help="Refresh every N seconds (e.g. --watch 30)")
    args = parser.parse_args()

    if args.watch > 0:
        try:
            while True:
                with Spinner("Scanning vault..."):
                    data = scan_vault()
                if args.json:
                    print_json(data)
                else:
                    print_human(data)
                print(f"\n  Scanned: {data['scanned_at']}")
                print(f"  Next update in {args.watch}s  (Ctrl+C to stop)")
                time.sleep(args.watch)
        except KeyboardInterrupt:
            print("\n  Stopped.")
    else:
        if args.json:
            print_json(scan_vault())
        else:
            with Spinner("Scanning vault..."):
                data = scan_vault()
            print_human(data)
            print(f"\n  Scanned: {data['scanned_at']}")


if __name__ == "__main__":
    main()

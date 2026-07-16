#!/usr/bin/env python3
"""
vault-stats.py – Zeigt Statistiken über den Vault an.

Usage:
    python3 _Meta/Scripts/vault-stats.py

Zeigt:
- Anzahl Notes pro Bereich
- Anzahl Canvas, Base, Excalidraw-Dateien
- Gesamtanzahl Wörter
- Offene Todos
"""

from pathlib import Path

VAULT_ROOT = Path(__file__).resolve().parent.parent.parent

IGNORE_DIRS = {".git", ".obsidian", "__pycache__"}
IGNORE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".webp", ".exe", ".json", ".js", ".css"}

counts = {"md": 0, "canvas": 0, "base": 0, "excalidraw": 0, "total": 0}
word_count = 0
todo_count = 0
by_folder = {}

for fpath in VAULT_ROOT.rglob("*"):
    if any(part.startswith(".") for part in fpath.parts):
        continue
    if fpath.is_dir():
        continue
    if fpath.suffix.lower() in IGNORE_EXTS:
        continue

    counts["total"] += 1

    # Categorize
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
        except:
            pass
    elif fpath.suffix == ".canvas":
        counts["canvas"] += 1
    elif fpath.suffix == ".base":
        counts["base"] += 1

    by_folder[folder] = by_folder.get(folder, 0) + 1

print("=" * 50)
print("📊 Vault Statistics")
print("=" * 50)
print(f"Total files:          {counts['total']}")
print(f"Markdown (.md):       {counts['md']}  ({counts['excalidraw']} excalidraw)")
print(f"Canvas (.canvas):     {counts['canvas']}")
print(f"Dataview (.base):     {counts['base']}")
print(f"Total words:          {word_count}")
print(f"Open todos:           {todo_count}")
print()
print("📂 Files per folder:")
for folder in sorted(by_folder.keys()):
    print(f"  {folder}: {by_folder[folder]}")

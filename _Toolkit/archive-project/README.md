# archive-project.py

Archiviert ein Projekt: verschiebt es von `Projects/Active/` → `Projects/Archive/` und setzt den YAML-Status auf `archived` + `completed:`-Datum.

## Verwendung

```bash
# Interaktiv – Projekt aus Liste wählen:
python3 _Toolkit/archive-project/archive-project.py

# Bestimmtes Projekt archivieren:
python3 _Toolkit/archive-project/archive-project.py "Bow Shooter"

# Nur aktive Projekte anzeigen:
python3 _Toolkit/archive-project/archive-project.py --list
```

## Flags

| Flag | Kurz | Beschreibung |
|------|------|-------------|
| `name` | (pos.) | Projektname, z. B. `"Bow Shooter"` |
| `--list` | `-l` | Nur aktive Projekte anzeigen |

## Globaler Trigger

```bash
archive-project "Projektname"
archive-project --list
```

(Siehe `~/.local/bin/toolkit` – das Tool ist auch über `toolkit archive-project` erreichbar)

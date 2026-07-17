# vault-stats.py

Zeigt Statistiken über den gesamten Vault an – Dateien, Wörter, offene Todos, Verteilung pro Bereich.

## Verwendung

```bash
# Übersicht mit Balkendiagramm:
python3 _Toolkit/vault-stats/vault-stats.py

# Als JSON für andere Tools/Scripts:
python3 _Toolkit/vault-stats/vault-stats.py --json

# Watch-Modus: Alle 30 Sekunden neu laden:
python3 _Toolkit/vault-stats/vault-stats.py --watch 30
```

## Flags

| Flag | Kurz | Beschreibung |
|------|------|-------------|
| `--json` | | Maschinenlesbare JSON-Ausgabe |
| `--watch N` | `-w` | Alle N Sekunden neu laden (Strg+C zum Beenden) |

## Globaler Trigger

```bash
vault-stats                    # Normal
vault-stats --json             # Als JSON
vault-stats --watch 10         # Alle 10s aktualisieren
```

(Siehe `~/.local/bin/vault-stats`)

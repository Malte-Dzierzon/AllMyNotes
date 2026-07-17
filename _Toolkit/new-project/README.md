# new-project.py

Erstellt ein neues Projekt im Vault aus der `Project-Template.md`.

## Verwendung

```bash
# Automatisch (alle Flags):
python3 _Toolkit/new-project/new-project.py "Mein Spiel" --engine Godot --status active --desc "Ein cooles Spiel" --tags "game, 3d" --github mein-spiel

# Oder interaktiv – einfach starten:
python3 _Toolkit/new-project/new-project.py
```

## Flags

| Flag | Kurz | Beschreibung |
|------|------|-------------|
| `name` | (pos.) | Projektname (z. B. `"Mein Spiel"`) |
| `--engine` | `-e` | Engine oder Tech-Stack (Default: `Unreal Engine 5`) |
| `--status` | `-s` | Status: `active`, `idea`, `archived` (Default: `idea`) |
| `--desc` | `-d` | Kurzbeschreibung (1 Satz) |
| `--tags` | `-t` | Tags, kommagetrennt (z. B. `"game, 3d, fantasy"`) |
| `--github` | `-g` | GitHub-Repo-Name (z. B. `mein-spiel`) |
| `--progress` | `-p` | Fortschritt in Prozent (z. B. `10`) |

## Globaler Trigger

```bash
new-project "Projektname"
```

(Siehe `~/.local/bin/new-project`)

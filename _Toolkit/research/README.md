# research.py

Erstellt Research-Aufgaben im Vault und zeigt offene Requests an.

## Verwendung

```bash
# Interaktives Menü:
python3 _Toolkit/research/research.py

# Offene Requests anzeigen:
python3 _Toolkit/research/research.py list

# Neue Research-Aufgabe erstellen:
python3 _Toolkit/research/research.py run "UE5 Nanite Performance"

# Mit eigener Kategorie:
python3 _Toolkit/research/research.py run "KI Agenten" --topic "AI / ML"
```

## Flags

| Befehl | Beschreibung |
|--------|-------------|
| `list` | Zeigt alle offenen Research-Requests aus `_Requests.md` |
| `run "<Thema>"` | Erstellt eine neue Research-Datei in `Research/_Inbox/` |
| `--topic "<Kat>"` | Kategorie manuell setzen (sonst automatisch) |

## Automatische Kategorien

Das Skript erkennt die Kategorie automatisch aus dem Thema:

| Keyword | Kategorie |
|---------|-----------|
| ue5, nanite, lumen, unreal | UE5-Tech |
| game, design, combat, level | Game-Design |
| linux, arch, disk | Linux-Tools |
| web, react, svelte, vue, tauri | Web-Dev |
| python, rust | Programming |
| blender, godot | Game-Dev / 3D-Art |
| ai, agent, llm | AI / ML |

## Globaler Trigger

```bash
research                          # Interaktiv
research list                     # Requests
research run "Thema"              # Neue Aufgabe
```

(Siehe `~/.local/bin/research`)

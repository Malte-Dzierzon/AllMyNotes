# DiskDashboard — Project Overview

## Summary (English)
**DiskDashboard** is a lightweight hybrid desktop application for Linux that helps non‑expert desktop users quickly understand and manage disk usage. It combines a fast terminal‑first scanner (for power and speed) with a clean graphical frontend (sunburst / treemap) and a simple package/app view with guided uninstall and tagging. The app targets users on minimal/tiling setups (e.g., Hyperland, Sway, Arche) who want a fast, friendly dashboard similar to what KDE/Plasma users get, without requiring deep Linux knowledge.

## Zusammenfassung (Deutsch)
**DiskDashboard** ist eine schlanke, hybride Linux‑Desktop‑App für Nutzer, die eine schnelle, leicht verständliche Übersicht über ihren Speicherplatz wollen. Die App verbindet einen schnellen Terminal‑Scanner mit einer klaren grafischen Visualisierung (Sunburst / Treemap), einer Paket/App‑Liste mit geführtem Deinstallations‑Workflow und einem flexiblen Tag‑/Filter‑System. Zielgruppe sind Nutzer minimalistischer Desktop‑Setups (z. B. Hyperland), die keine tiefen Linux‑Kenntnisse haben, aber eine einfache, sichere Möglichkeit suchen, Speicherplatz zu analysieren und aufzuräumen.

---

## Goals and Target Audience
**Primary goals**
- Provide a one‑glance dashboard showing free/used space, largest folders, and app/game footprint.
- Let users filter and tag content (e.g., *Games*, *Dev*, *Libraries*, *Books*).
- Offer a safe, guided uninstall/cleanup flow with preview and dry‑run.
- Be lightweight and fast on minimal desktop environments.

**Target audience**
- Desktop users on minimal/tiling environments (Hyperland, Sway, Arche) who want a friendly GUI/TUI tool.
- Not aimed at distro hackers or people who prefer manual CLI commands; aimed at users who want a simple visual tool.

---

## Architecture (high level)
**Design principle:** separate a small, fast core scanner from two frontends. This keeps scanning fast and permissions isolated, and lets UI choices evolve independently.

- **Core scanner (daemon/CLI)**  
  - Language: **Rust** or C (small binary).  
  - Responsibilities: fast filesystem scan, incremental updates, JSON export, package list adapters.  
  - Exposes: JSON over stdout / local socket / simple HTTP or DBus for IPC.

- **Frontends**  
  - **TUI**: terminal‑first quick checks (ncurses style) for keyboard users.  
  - **GUI**: Tauri (Rust core + web UI) or a lightweight Qt webview; shows sunburst/treemap, lists, filters, tags.

- **Adapters**  
  - Modular adapters for package systems: **apt/dpkg**, **flatpak**, (later **rpm**). Each adapter returns package metadata and uninstall commands (dry‑run).

- **Cleaner/Uninstaller**  
  - Guided UI that shows what will be removed, dependencies affected, and a dry‑run option. No automatic destructive actions without explicit confirmation and root elevation.

---

## Core Components and Minimal OSS Integrations
**Scanner core**
- **Inspiration / integration:** use ideas from `ncdu` (fast directory scanning, exportable results). Implement a small scanner that can export JSON snapshots and incremental diffs.

**Visuals**
- **Sunburst / Treemap** visualization in the GUI (web‑based D3/Canvas inside Tauri). Keep visuals minimal and responsive.

**Package / App list**
- Use system package tools for metadata:
  - **apt/dpkg** adapter: `dpkg-query` or `apt` parsing for package sizes and files.
  - **flatpak** adapter: `flatpak list --app --columns=application,size` (or equivalent) to get sandboxed app sizes.
- Present packages with tags and a safe uninstall preview (e.g., `apt remove --simulate` / `apt --dry-run` or `apt-get -s`).

**Cleaner**
- Integrate cleaning rules inspired by BleachBit (but do not ship destructive defaults). Provide user‑reviewable cleaning actions (cache clear, temp files, orphaned packages).

**Distribution**
- Recommend **Flatpak** packaging for easy install across distros and sandboxing via portals for file access.

---

## UX and Key Flows
**Main dashboard**
- Top row: **Total disk**, **Used**, **Free**, **Largest folder** (clickable).
- Center: **Sunburst / Treemap** showing top‑level directories by size.
- Right pane: **Quick actions** (Scan, Rescan, Export snapshot, Clean suggestions).
- Bottom: **Recent scans** and **tags** summary.

**Drilldown**
- Click a segment → show file list sorted by size, with file path, size, last modified, and tag controls.
- Provide **“Mark as Game / Dev / Library / Book”** tags (client‑side persisted).

**Package view**
- Switch to Packages tab → show installed apps with size, origin (apt/flatpak), and tag suggestions.
- **Uninstall flow**: select package → show files removed, dependencies affected, disk freed estimate, Dry‑run button, Confirm with root elevation.

**Filters & Tags**
- Multi‑select filters: file type, tag, size range, last modified.
- Save filter presets (e.g., “Large Dev Files”, “Old Downloads”).

**Safety features**
- All destructive actions require explicit confirmation and show a dry‑run.
- Provide **Trash/Undo** for file deletions where possible (move to user Trash first).
- Logging of all actions and an option to export logs.

---

## Data Model and IPC JSON Schema (example)
**Purpose:** simple, stable JSON for core → frontend communication.

**Scan snapshot (example)**
```json
{
  "scan_id": "2026-06-26T19:00:00Z",
  "root": "/home/malte",
  "total_bytes": 512000000000,
  "used_bytes": 320000000000,
  "free_bytes": 192000000000,
  "nodes": [
    {
      "path": "/home/malte/.local/share/Steam",
      "size_bytes": 120000000000,
      "type": "directory",
      "children_count": 120,
      "tags": ["Games"]
    },
    {
      "path": "/home/malte/Projects",
      "size_bytes": 80000000000,
      "type": "directory",
      "children_count": 45,
      "tags": ["Dev"]
    }
  ]
}
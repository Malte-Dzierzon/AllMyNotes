# Projects Vault Analysis & Improvement Plan

## Phase 1: Analysis Summary

### Vault Structure Overview

```
Obsidian Vault/
├── Projekts/                 # Main projects folder (German)
│   ├── Dreamwolds/           # 3D Platformer UE5
│   │   ├── Dreamwolds.md     # Brief concept (995 bytes)
│   │   └── Game Idee...o.Dreamwolds.canvas  # Visual brainstorming
│   ├── Rynthar/              # Clash Royale + MTG Hybrid
│   │   └── Rynthar-Conzept.md  # Detailed concept (2.9 KB)
│   ├── Soulslike 2.5D/       # 2.5D Soulslike UE5
│   │   ├── Soulslike.md      # Brief concept (926 bytes)
│   │   └── Game System.canvas  # Visual systems design
│   ├── Stormlight-Archive ○The Game○/
│   │   └── Stormlight Archive Game.canvas  # Visual lore mapping
│   ├── Unsortiert/           # Unsorted ideas
│   │   ├── Bow Shooter.md    # Competitive bow game concept
│   │   ├── Disk App Linux Idee.md  # Detailed DiskDashboard spec (5.9 KB)
│   │   └── Minecraft Mod Ideen.canvas  # Visual mod ideas
│   ├── README.md             # Portfolio overview with progress table
│   └── Projects.base         # Dataview config
└── Wiki/                     # Knowledge base
    ├── Books/                # Stormlight Archive collection
    │   ├── Book Collection/  # Structured metadata (YAML frontmatter)
    │   ├── BookCover/        # Cover images
    │   └── Books Overview.base
    ├── MTG Lore/             # MTG reference links
    └── Images/               # Reference images for projects
```

### Documentation Style & Conventions

| Aspect | Convention |
|--------|------------|
| **Language** | Mixed German/English; German for personal notes, English for technical specs |
| **Frontmatter** | YAML used in Book Collection (structured metadata) |
| **Canvas Usage** | Heavy visual brainstorming; nodes for concepts, groups for categories, images for references |
| **File Naming** | Descriptive with spaces; German project names, English technical docs |
| **Structure** | Flat per-project folders; no subfolders currently |
| **Progress Tracking** | Visual progress bars in README table (██░░░░░░░░░░ 20%) |

### Current Project Inventory

#### In Projekts Folder (5 main + 3 unsorted):
| Project | Status | Documentation Level |
|---------|--------|---------------------|
| Dreamwolds | Concept | Minimal (concept + canvas) |
| Rynthar | Concept | Medium (detailed concept doc) |
| Soulslike 2.5D | Demo Complete (100%) | Minimal (concept + canvas) |
| Stormlight-Archive Game | Early Concept | Canvas only |
| Bow Shooter | Early Idea | Bullet points only |
| Disk Dashboard | Detailed Spec | High (comprehensive spec doc) |
| Minecraft Mod Ideas | Brainstorming | Canvas only |

#### In README but MISSING from Projekts:
| Project | Progress | Notes |
|---------|----------|-------|
| MTG Multiverse Studio | 20% | Local-first MTG desktop app |
| Personal Dashboard Portfolio | 30% | Component-driven portfolio |
| Neural Network in Python | 100% | 3D object classification |
| Minecraft Modpack Fabric 1.21.11 | 100% | "Paleon" modpack with landing page |

### Key Relationships
- **Wiki/Books** → Stormlight-Archive Game (lore reference)
- **Wiki/MTG Lore** → Rynthar & MTG Multiverse Studio
- **Wiki/Images/Pictures** → All game projects (visual references in canvas)
- **Disk Dashboard** → Could relate to Personal Dashboard Portfolio (both UI/dashboard)
- **Unreal Engine 5** → Dreamwolds, Soulslike 2.5D, Bow Shooter (shared tech stack)

---

## Phase 2: Strategic Improvement Plan

### Guiding Principles
1. **Consistency**: Unified project structure across all projects
2. **Completeness**: Every project gets standard documentation sections
3. **Scalability**: Structure supports growth from concept → production
4. **Navigability**: Clear cross-linking between projects and Wiki
5. **Professional Standard**: Industry-grade game/dev documentation

### Standard Project Template Structure

Each project folder should contain:

```
ProjectName/
├── README.md                    # Project overview, status, quick links
├── Game-Design/                 # OR Technical-Spec/ for non-game
│   ├── Core-Concept.md          # Elevator pitch, pillars, vision
│   ├── Gameplay-Mechanics.md    # Core loops, systems, rules
│   ├── Level-Design.md          # World structure, progression
│   ├── Art-Direction.md         # Style guide, references, moodboards
│   ├── Technical-Architecture.md # Engine, frameworks, patterns
│   └── Scope-MVP.md             # Minimum viable product definition
├── Development/
│   ├── Roadmap.md               # Phases, milestones, timeline
│   ├── Task-Breakdown.md        # Epic → Story → Task hierarchy
│   ├── Tech-Stack.md            # Tools, versions, dependencies
│   └── Architecture-Decisions.md # ADR log
├── Assets/
│   ├── Art-Reference/           # Moodboards, style references
│   ├── Concept-Art/             # Original concepts
│   └── Prototypes/              # Greybox, vertical slices
├── Documentation/
│   ├── Changelog.md             # Version history
│   ├── Known-Issues.md          # Bugs, tech debt
│   └── Postmortem/              # Lessons learned (per milestone)
└── Canvas/                      # Existing canvas files (preserved)
```

### Priority Order for Improvement

| Priority | Project | Reason |
|----------|---------|--------|
| **1** | **Soulslike 2.5D** | 100% complete demo; needs professional documentation for portfolio |
| **2** | **Disk Dashboard** | Most detailed spec; near-ready for implementation; practical utility |
| **3** | **Dreamwolds** | Strong concept; UE5 expertise; good portfolio piece |
| **4** | **Rynthar** | Unique hybrid concept; MTG lore connection; complex systems need structure |
| **5** | **MTG Multiverse Studio** | 20% in README; missing from Projekts; local-first app aligns with skills |
| **6** | **Personal Dashboard Portfolio** | 30% in README; missing; showcases web/dev skills |
| **7** | **Stormlight-Archive Game** | Lore-rich; connects to Wiki/Books; canvas exists |
| **8** | **Bow Shooter** | Competitive UE5; unique hook; early stage |
| **9** | **Neural Network in Python** | 100% complete; missing; academic/portfolio value |
| **10** | **Minecraft Modpack (Paleon)** | 100% complete; missing; landing page exists |

### Missing Files to Create (Per Project)

| Project | Missing Critical Files |
|---------|------------------------|
| All | README.md, Roadmap.md, Tech-Stack.md, Changelog.md |
| Game Projects | Game-Design/ (Core-Concept, Gameplay-Mechanics, Level-Design, Art-Direction, Technical-Architecture, Scope-MVP) |
| App Projects | Technical-Spec/ (Architecture, API, Data-Model, UI-UX, Security) |
| Completed Projects | Postmortem/, Known-Issues.md, Build-Instructions.md |

### Research Needs (Iterative Loop)

| Topic | Projects Affected | Research Method |
|-------|-------------------|-----------------|
| UE5 2.5D best practices | Soulslike 2.5D, Dreamwolds, Bow Shooter | Official docs, GDC talks, community tutorials |
| Local-first desktop app architecture | MTG Multiverse Studio, Disk Dashboard | Tauri, Electron, Wails comparisons |
| MTG digital implementation rules | Rynthar, MTG Multiverse Studio | MTG Comprehensive Rules, existing apps (MTGA, Cockatrice) |
| Stormlight Archive magic systems | Stormlight-Archive Game | Brandon Sanderson's books, Coppermind wiki |
| Competitive multiplayer networking | Bow Shooter, Rynthar (realtime) | UE5 Netcode, GGPO, Photon, Nakama |
| Portfolio site architecture | Personal Dashboard Portfolio | Astro, Next.js, React patterns |
| Minecraft Fabric modpack structure | Minecraft Modpack | Fabric docs, existing modpacks (ATM, Prominence) |

### Templates & Standards to Establish

1. **Project README Template** - Status, tech stack, links, progress
2. **Game Design Document (GDD) Template** - Industry standard sections
3. **Technical Spec Template** - For apps/tools
4. **ADR Template** - Architecture Decision Records
5. **Changelog Format** - Keep a Changelog standard
6. **Task Breakdown Format** - Epic/Story/Task with acceptance criteria
7. **Naming Conventions** - Files, folders, branches, commits
8. **Cross-linking Protocol** - `[[Wiki/Books/...]]`, `[[Projekts/...]]`

---

## Phase 3: Execution Strategy

### Immediate Actions (Week 1)
1. Create standard templates in `/Projekts/_Templates/`
2. Restructure **Soulslike 2.5D** first (highest priority, complete demo)
3. Restructure **Disk Dashboard** (best existing spec)
4. Create missing project folders for README projects

### Ongoing Process (Per Project)
1. **Audit** existing files (canvas, markdown, images)
2. **Extract** structured content from canvas → markdown
3. **Create** standard folder structure
4. **Write** missing documentation sections
5. **Research** gaps → integrate findings
6. **Cross-link** to Wiki and other projects
7. **Update** root README.md progress table

### Quality Gates
- Every project has: README, Roadmap, Tech-Stack, Changelog
- Game projects have: Core-Concept, Gameplay-Mechanics, Art-Direction, Technical-Architecture
- All canvas content extracted to searchable markdown
- All images referenced via relative paths
- Frontmatter on key files for Dataview queries
- No duplicate information; single source of truth

### Maintenance
- Monthly review of roadmap vs actual
- Changelog updated per milestone
- Postmortem after each major phase
- Templates evolved based on usage

---

## Next Steps

1. **Create `/Projekts/_Templates/`** with all standard templates
2. **Begin Soulslike 2.5D restructure** - extract canvas, create GDD sections
3. **Create missing project folders** for MTG Multiverse Studio, Personal Dashboard, Neural Network, Minecraft Modpack
4. **Establish Dataview queries** in Projects.base for project dashboard
5. **Document decisions** in this file as work progresses

*This plan is a living document. Update as projects evolve.*
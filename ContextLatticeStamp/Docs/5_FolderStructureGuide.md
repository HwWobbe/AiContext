# ContextLatticeStamp — Folder Structure Guide

*Where things go, and why.*

---

## The Rule of Thumb

> **If it explains → `Docs/`  
> If it runs → `Scripts/`  
> If it demonstrates → `Examples/`  
> If it argues → `Essay/`**

---

## Top-Level: `AiContext/`

The root repo. Each subdirectory is a self-contained project within the broader AI-context tooling ecosystem.

```
AiContext/
├── README.md                  ← Repo overview & index of projects
├── .gitignore                 ← Repo-wide exclusions (RnHw_*.json, etc.)
└── ContextLatticeStamp/       ← This project
    └── ...
```

**Adding a new project?** Create a new top-level folder (CamelCase), give it its own `README.md`, and link it from `AiContext/README.md`.

---

## `ContextLatticeStamp/`

### `Docs/`
Human-readable documentation. Anything a new user or your future self needs to understand and use the system.

| File | Purpose |
|---|---|
| `QuickStart.md` | Minimal setup → first working stamp in <10 min |
| `Architecture.md` | Schema design, lattice spec, versioning rules |
| `StampingGuide.md` | Step-by-step: building, editing, injecting stamps |
| `Faq.md` | Troubleshooting & common questions |

**Add here when:** you're writing an explanation, a how-to, a reference, or a decision log.  
**Don't add here:** runnable code, raw data, personal configs.

---

### `Scripts/`
Everything that *runs*. Python utilities, AutoHotKey scripts, shell scripts.

| File | Purpose |
|---|---|
| `RnhwJsonManager.py` | Build, validate, diff, and version stamps |
| `Jump.ahk` | Hotkey launcher — injects a stamp into the active chat window |

**Add here when:** it's executable and meant to be run directly.  
**Naming:** PascalCase for the script name (e.g. `StampValidator.py`). The `Rnhw` prefix is reserved for scripts that touch personal data dictionaries.  
**Don't add here:** `RnHw_*.json` data files — those stay local and out of the repo.

---

### `Examples/`
Reference material — stamps and configs people can clone and adapt.

| File | Purpose |
|---|---|
| `SampleStamps.json` | Annotated example stamps covering common use-cases |

**Add here when:** you have a concrete, working example worth sharing.  
**Keep sanitized:** no personal vocabulary, no real project names, no private data.

---

### `Essay/`
Long-form writing — philosophy, rationale, and design thinking.

| File | Purpose |
|---|---|
| `DenserIsBetter_v0.1.md` | The core argument for high-density context injection |

**Naming convention:** `TitleInCamelCase_vX.Y.md` — version in the filename so drafts coexist cleanly.  
**Add here when:** it's an argument or exploration, not a how-to. If it's instructional, it belongs in `Docs/`.

---

## Naming Conventions (Summary)

| Thing | Convention | Example |
|---|---|---|
| Directories | PascalCase | `ContextLatticeStamp/`, `Examples/` |
| Markdown docs | PascalCase | `QuickStart.md`, `StampingGuide.md` |
| Python scripts | PascalCase | `RnhwJsonManager.py` |
| AHK scripts | PascalCase | `Jump.ahk` |
| Personal data files | `RnHw_` prefix + PascalCase | `RnHw_DataDict.json` |
| Versioned drafts | `_vX.Y` suffix | `DenserIsBetter_v0.1.md` |

---

## What Stays Out of the Repo

| Pattern | Reason |
|---|---|
| `RnHw_*.json` | Personal vocabulary & private mappings — local only |
| Any file with real names, IDs, or private project details | Keep examples sanitized |
| Editor config, OS files | Covered by `.gitignore` |

---

## Quick Decision Tree

```
New file to add?
│
├── Does it explain or document something?
│   └── → Docs/
│
├── Does it run / execute?
│   └── → Scripts/
│
├── Is it a clean, shareable example?
│   └── → Examples/
│
├── Is it a long-form argument or essay?
│   └── → Essay/
│
└── Is it personal/private data?
    └── → Keep LOCAL. Do not commit.
```

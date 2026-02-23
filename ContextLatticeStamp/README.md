# ContextLatticeStamp

> **Dense, portable context for AI conversations — stamp once, carry everywhere.**

---

## What Is This?

ContextLatticeStamp is a lightweight system for capturing, storing, and injecting structured context into AI sessions. Instead of re-explaining your project, preferences, and vocabulary every conversation, you *stamp* a JSON snapshot and paste it in. The AI picks up exactly where you left off.

The core idea: **denser is better**. A well-compressed stamp beats a wall of prose every time.

---

## Quick Overview

| Layer | What it does |
|---|---|
| **Stamp** | A JSON snapshot of your current context (project state, vocab, goals) |
| **Lattice** | The schema that keeps stamps consistent and parseable |
| **Manager** | `RnhwJsonManager.py` — build, validate, and version your stamps |
| **Jump** | `Jump.ahk` — hotkey launcher to inject stamps into any AI chat |

---

## Getting Started

See [`Docs/QuickStart.md`](Docs/QuickStart.md) for setup in under 10 minutes.

---

## Repository Layout

```
ContextLatticeStamp/
├── Docs/
│   ├── QuickStart.md       ← Start here
│   ├── Architecture.md     ← Schema design & lattice spec
│   ├── StampingGuide.md    ← How to build & use stamps
│   └── Faq.md              ← Common questions
├── Scripts/
│   ├── RnhwJsonManager.py  ← Core stamp manager (Python)
│   └── Jump.ahk            ← AutoHotKey injection launcher
├── Examples/
│   └── SampleStamps.json   ← Reference stamps to clone & adapt
└── Essay/
    └── DenserIsBetter_v0.1.md  ← The philosophy behind the system
```

---

## Key Concepts

**Stamp** — A versioned JSON object. Contains project metadata, vocabulary mappings, session goals, and any persistent context the AI needs to orient itself immediately.

**Lattice** — The structural schema stamps conform to. Keeps them machine-readable and diff-friendly across versions.

**RnHw prefix** — Internal namespace for personal data files (e.g. `RnHw_DataDict.json`). These are excluded from the repo by `.gitignore` and stay private.

---

## What's Not in This Repo

| Item | Why excluded |
|---|---|
| `RnHw_DataDict.json` | Contains personal vocabulary & private mappings |
| Any `RnHw_*.json` | All personal data dictionaries stay local |

---

## Essay

[*Denser Is Better*](Essay/DenserIsBetter_v0.1.md) — the case for high-density context injection over verbose re-explanation. Short read, worth it.

---

## Status

Early release. Schema and tooling are functional; documentation is actively expanding.

---

*Part of the [AiContext](https://github.com/HwWobbe/AiContext) collection.*

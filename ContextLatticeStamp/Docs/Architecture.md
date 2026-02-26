# ContextLatticeStamp — Architecture Summary

**Version:** 0.2.0 | **Date:** 2026-02-25 | **Status:** Draft

---

## The Lattice — Horizontal Orientation

| | 𝒞 Claude | 𝒯 TiddlyWiki | 𝒦 Keep | 𝒮 SQL | ℱ FileSystem | 𝒢 GitHub | 𝒟 Docs |
|---|---|---|---|---|---|---|---|
| **Category** | cell | cell | cell | cell | cell | cell | cell |
| **Topic** | cell | cell | cell | cell | cell | cell | cell |

Lanes = columns. Categories/Topics = rows. Symbols are compact cell values — English labels are column headers.

---

## Key Grammar

```
RnHw : {Lane} : {Category}{Topic}{Qualifier}
 │        │         │        │       │
 │        │         │        │       └─ Disambiguator (optional)
 │        │         │        └─ Subject domain (Blackboard bold or plain)
 │        │         └─ Grouping (Fraktur, emerges from usage)
 │        └─ Platform (Script font: 𝒞𝒯𝒦𝒮ℱ𝒢𝒟)
 └─ Namespace (always RnHw)
```

---

## Storage — Scale Triggers

| Stage | Store | Trigger |
|---|---|---|
| Now | JSON flat file | < 5,000 notes / < 5MB |
| Next | SQLite | > 5,000 notes or queries needed |
| Later | 3-Tier (HOT/WARM/COLD) | TW > 10,000 tiddlers |

---

## Universal Hex Addressing

A shared `0-9, a-f` coordinate system across all document types, Asks, tiddlers, and Redis fields. The same address means a different thing depending on `DocType` — set via LatticeValue.

### Chapter Addresses

| Address | DocType: Chapter | DocType: Ask |
|---|---|---|
| `0` | Cover | Preamble / Name |
| `1` | ForeWord | Context |
| `2` | Contents | Constraints |
| `3` | Summary | Summary |
| `4` | Introduction | Background |
| `5` | Findings | Considerations |
| `6` | Conclusions | Output format |
| `7` | Recommendations | Examples |
| `8` | Appendix | Appendix |
| `9` | EndNotes | EndNotes |
| `a-f` | reserved | reserved |

### Key Rule
The key in any line is the string up to the first space:
```
2.1 this is the payload text
│
└─ key = "2.1" ; payload = "this is the payload text"
```

### Nesting
```
2       top level chapter
2.1     section
2.1.1   sub-section
f.f     maximum practical depth
```

---

## Redis Interaction

The hex address maps directly to Redis hash fields — no translation layer needed.

```
HSET RnHw:𝒞:AskTemplate  0  "CoverName"
HSET RnHw:𝒞:AskTemplate  1  "Context text here"
HSET RnHw:𝒞:AskTemplate  2.1 "Constraint one"
HSET RnHw:𝒞:AskTemplate  2.2 "Constraint two"
```

Redis sorted sets order chapters naturally — hex keys sort `0` first, `f` last, consistent across all DocTypes.

**ManifestStubs pipeline:**
```
Stubs (Keep/TW/JSON)
  → ManifestStubs (ordered hex manifest)
    → Redis (fast lookup)
      → AI render (DocType-aware expansion)
        → branch output (per audience)
```

---

## Hardware Platform

**Machine:** Razer Blade 16 (RZ09-0510)

| Component | Spec | Relevance |
|---|---|---|
| CPU | Intel i9-14900HX (32 cores) | Docker, PowerShell, batch ops |
| RAM | 64GB | Large TW files, Redis in-memory |
| GPU | NVIDIA RTX 4090 Laptop | Local AI rendering |
| GPU 2 | Intel UHD (integrated) | Display, light tasks |
| OS | Windows 11 | AHK, PowerShell, TW |

**Key implication:** RTX 4090 enables **local AI model execution** (Ollama, LM Studio) — ManifestStubs pipeline can render locally without cloud dependency.

---

## AI Memory Layers

Three distinct memory layers operate in parallel:

| Layer | Scope | Mechanism | Persists |
|---|---|---|---|
| **Claude Memory** | Cross-session facts | Anthropic memory system | Yes — across convos |
| **Context Stamp** | Current-state detail | JSON injected at session start | Per session |
| **Redis** | Fast runtime lookup | In-memory key-value store | Configurable |

**How they interact:**
- Claude Memory handles **background** — preferences, naming conventions, project awareness
- Context Stamp handles **foreground** — precise current state, active stamps, session goals
- Redis handles **pipeline** — ManifestStubs assembly, fast field lookup during doc generation

**Claude Memory learns over time:**
- RnHw namespace and naming conventions
- Hex addressing scheme
- Tool preferences (TW, Keep, GitHub, AHK)
- DocType meanings and chapter structure

As memory matures, the context stamp can shrink — memory carries the stable background, stamp carries only the volatile current state.

---

## Local AI Pipeline

With RTX 4090 available, a fully local ManifestStubs render pipeline is viable:

```
Stubs (Keep/TW/JSON)
  → ManifestStubs (ordered hex manifest)
    → Redis (fast lookup, 64GB RAM)
      → Local AI (RTX 4090 / Ollama)  ←── or Claude API
        → branch output (per audience)
```

Local rendering advantages: no token limits, no latency, private data stays local, `RnHw_*.json` never leaves the machine.

---

## Core Design Principles

**Denser is better** — compressed stamps beat verbose re-explanation.  
**Symbols are vertical** — short chars for top-to-bottom scanning.  
**English is horizontal** — full labels work as column headers in tables.  
**Emerge, don't plan** — categories and topics reveal themselves from usage.  
**LatticeValue** — a shared version stamp across all docs, enabling drift detection.  
**One grammar, many contexts** — hex addressing is universal; DocType switches the semantic layer.  
**ManifestStubs** — ordered stub collection assembled for AI expansion into target output.  
**Memory is layered** — Claude Memory (background) + Context Stamp (foreground) + Redis (pipeline).  
**Local first** — RTX 4090 enables private, unlimited, low-latency AI rendering when needed.  

---

## Tools

| Tool | Role |
|---|---|
| `RnhwJsonManager.py` | Build, validate, version stamps |
| `Jump.ahk` | `Win+J` hotkey — fastest jump, no paste |
| TextBlaze `/jt` | Jump from any text field |
| TextBlaze `/f` | Minimal-token inject for AI chat |
| PowerShell | Batch operations, 10+ notes |

---

*Part of the [AiContext](https://github.com/HwWobbe/AiContext) collection.*

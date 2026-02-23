# ContextLatticeStamp — Architecture Summary

**Version:** 0.1.0 | **Date:** 2026-02-23 | **Status:** Draft

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

## Core Design Principles

**Denser is better** — compressed stamps beat verbose re-explanation.  
**Symbols are vertical** — short chars for top-to-bottom scanning.  
**English is horizontal** — full labels work as column headers in tables.  
**Emerge, don't plan** — categories and topics reveal themselves from usage.  
**LatticeValue** — a shared version stamp across all docs, enabling drift detection.  

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

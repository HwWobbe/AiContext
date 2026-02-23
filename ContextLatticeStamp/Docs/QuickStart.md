# RnHw: contextLatticeStamp Quick Start Guide

**Version:** 0.2.2  
**Date:** 2026-02-23  
**Status:** Living Document

---

## TL;DR - What You Have

A multi-dimensional note navigation system with:
- **450K notes** (goal) indexed by contextLatticeStamps
- **7 lanes** (𝒞𝒯𝒦𝒮ℱ𝒢𝒟) for different content types
- **3 input methods** (TextBlaze, AHK, PowerShell)
- **Lattice structure** (QrSt) for multi-axis organization

---

## Decision Tree: Which Tool When?

```
┌─ At Desktop? 
│  └─ YES → Use Win+J (fastest, no paste)
│  └─ NO → Continue ↓
│
┌─ In Text Field? (email, chat, doc)
│  └─ YES → Use /jt or /jump (TextBlaze)
│  └─ NO → Continue ↓
│
┌─ In AI Chat?
│  └─ YES → Use /f key (minimal tokens)
│  └─ NO → Continue ↓
│
└─ Batch Operations? (10+ notes)
   └─ YES → Use PowerShell scripts
```

**Rule:** Pick ONE primary per context. Ignore others until muscle memory forms.

---

## 5 Core Operations

### 1. **Jump to Note** (most common)

**Desktop:** `Win+J` → type lane → type key → Enter  
**Text field:** `/jt TagVocabulary` → paste in terminal  
**AI chat:** `/f TagVocabulary` → click URL

### 2. **Register New Note**

**PowerShell:**
```bash
python -c "from rnhw_json_manager import register_note; print(register_note('tw', '𝕯', 'URL', 'Title', manual_key='Key'))"
```

**TextBlaze:** `/reg` → fill form → paste command

### 3. **Insert Timestamp**

**TextBlaze:** `/now` → select options → inserts stamp  
**Result:** `ℌ🐟午㋁⑧㏵♅㏜㍩`

### 4. **Search Notes**

**PowerShell:**
```bash
python -c "from rnhw_json_manager import find_notes; [print(n['key']) for n in find_notes(prefix='𝕯')]"
```

### 5. **List All Notes in Lane**

**PowerShell:**
```bash
python -c "from rnhw_json_manager import list_notes; list_notes(lane='tw')"
```

---

## Typography System (Lane/Category/Topic)

### **Lanes** (Script font) - Site/System Identifiers

```
𝒞 = Claude conversations
𝒯 = TiddlyWiki
𝒦 = Google Keep
𝒮 = SQL Server/database
ℱ = File system
𝒢 = GitHub/repos
𝒟 = Google Docs
```

### **Categories** (Fraktur font) - Organizational Groupings

```
𝕬 𝕭 𝕮 𝕯 𝕰 𝕱 𝕲 ℌ 𝕴 𝕵 𝕶 𝕷 𝕸 𝕹 𝕺 𝕻 𝕼 𝕽 𝕾 𝕿 𝖀 𝖁 𝖂 𝖃 𝖄 𝖅

Reserved for future use - will emerge from usage patterns
Examples: Active/Archive, Personal/Shared, Concept/Procedure
```

### **Topics** (Blackboard bold) - Subject Domains

```
𝕯      = Design (single char)
𝕽𝕯     = Redis (multi-char)
𝕰𝖘     = Essay
𝕷𝖆𝖙    = Lattice
noTopic = Uncategorized (plain text)
```

---

## Bootstrap Strategy (Getting to 450K)

### **Week 1-4: Opportunistic (Goal: 20 notes)**

**Method:** Stamp notes as you access them
- Open TW tiddler → Test `Win+J` to see if registered
- If not found → register via `/reg` or PowerShell
- Track friction points

**Learn:** What gets accessed? What's hard to stamp?

### **Month 2: First Batch (Goal: 100 notes)**

**Method:** Bulk-stamp one topic cluster
- Export all tiddlers tagged "Design"
- Generate stamps from creation dates
- Review/adjust manually

**Learn:** What rules work? What patterns emerge?

### **Month 3+: Systematic (Goal: 1000+ notes)**

**Method:** Define categories, batch migrate
- Review patterns from 100+ notes
- Define 3-5 categories that matter
- Build migration scripts

**Learn:** What scales? What breaks?

---

## Scale Migration Triggers

### **When to Migrate from JSON → SQLite:**

**Trigger 1: Performance**
- JSON file >5MB (~5,000 notes)
- Lookup time >100ms
- Complex queries needed

**Trigger 2: Features**
- Need relational queries (joins)
- Want full-text search across content
- Analytics/reporting required

### **When to Split TW into Tiers:**

**Trigger: TW has >10,000 tiddlers**

**3-Tier Architecture:**
```
Tier 1: HOT (TiddlyWiki)
  └─ Active working notes (last 3 months, top 1000)
  └─ ~5,000-10,000 tiddlers

Tier 2: WARM (SQLite)
  └─ Searchable archive (6mo-5yr old)
  └─ ~100,000-400,000 notes

Tier 3: COLD (Git/Filesystem)
  └─ Long-term archive (>5yr, rarely accessed)
  └─ Unlimited capacity
```

---

## Current System Specs

### **Files:**
- `C:\Users\hwobb\RnHw\rnhw_json_manager.py` - v0.2.2
- `C:\Users\hwobb\RnHw\RnHw_DataDict.json` - main data store
- `C:\Users\hwobb\RnHw\jump.ahk` - Win+J hotkey

### **Registered Notes:** 2
- `RnHw:𝒯:TagVocabulary` - Design:TagVocabulary tiddler
- `RnHw:𝒯:noTopic一` - SetAnchor tiddler

### **Exec Templates:** 3
- `jump_tw` - Jump to TW tiddler by name
- `jump_note` - Jump via DataDict lookup
- `register_tw_batch` - Batch register tiddlers

---

## Common Patterns

### **Register Current TW Tiddler:**

1. Open tiddler in TW
2. Copy URL from address bar (with permalinks enabled)
3. PowerShell:
```bash
python -c "from rnhw_json_manager import register_note; print(register_note('tw', 'TOPIC', 'URL', 'TITLE', manual_key='KEY'))"
```

### **Find All Notes in Topic:**

```bash
python -c "from rnhw_json_manager import find_notes; [print(f\"{n['key']}: {n['title']}\") for n in find_notes(prefix='𝕯')]"
```

### **Jump Workflow:**

```
Win+J → tw → TagVocabulary → Opens tiddler
Win+J → convo → 𝕮𝕷𝕾Main → Opens conversation
```

---

## Troubleshooting

### **Win+J doesn't work:**
- Check AHK is running (tray icon)
- Restart jump.ahk
- Check file path in script matches actual location

### **TW permalinks not showing:**
- TW Settings → Navigation → "Include the target tiddler"
- Reload TW

### **Python import errors:**
- `cd C:\Users\hwobb\RnHw` first
- Check file exists: `dir rnhw_json_manager.py`

### **TextBlaze snippets not expanding:**
- Check subscription status
- Verify snippet is saved
- Try in different app to test

---

## Next Steps

### **This Week:**
1. ✓ Understand tool choice (this doc)
2. Register 10 more notes opportunistically
3. Pick ONE primary jump method, use exclusively

### **This Month:**
1. Define first batch-stamp target (Design notes?)
2. Build stamping rules (date → time dimension)
3. Reach 100 registered notes

### **This Quarter:**
1. Migrate to SQLite when JSON >5MB
2. Define 3-5 categories from patterns
3. Build TW AutoComplete integration (optional)

---

## Reference Links

**Key Conversations:**
- Initial design: `RnHw:𝒞:𝕮𝕷𝕾Main`
- Essay draft: SubStackT0217

**Documentation:**
- TiddlyWiki: http://localhost:8080/
- GitHub: (pending)
- Substack: (pending)

**Tools:**
- TextBlaze snippets: (in TextBlaze app)
- AHK script: `C:\Users\hwobb\RnHw\jump.ahk`
- Python manager: `C:\Users\hwobb\RnHw\rnhw_json_manager.py`

---

## Document History

| Version | Date | Changes |
|---------|------|---------|
| 0.1 | 2026-02-23 | Initial creation |

---

**Questions? Update this doc as you learn.**  
**This is a living document - edit freely.**

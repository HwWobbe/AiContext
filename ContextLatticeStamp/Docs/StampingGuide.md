# ContextLatticeStamp — Stamping Guide

**Version:** 0.1.0
**Date:** 2026-02-23
**Status:** Living Document
**Assumes:** QuickStart.md has been read

---

## 1. What Is a Stamp?

A stamp is a versioned JSON object that uniquely identifies and locates a note. It contains enough information to:

- **Find** the note (URL or path)
- **Identify** it (title, lane, category, topic)
- **Place** it in the lattice (key structure)
- **Track** it over time (version, date)

A stamp is not the note itself — it is a lightweight pointer to it.

---

## 2. Key Naming Conventions

The key is the most important part of a stamp. It must be unique, readable, and parseable.

### Structure

```
RnHw:{Lane}:{Category}{Topic}{Qualifier}
```

### Examples

```
RnHw:𝒯:TagVocabulary          ← Lane only, no category/topic
RnHw:𝒯:𝕯TagVocabulary         ← Lane + Topic
RnHw:𝒞:𝕮𝕷𝕾Main               ← Lane + Category + Topic
RnHw:𝒢:𝒢AiContextReadme       ← GitHub lane, repo+file
```

### Rules

| Rule | Detail |
|---|---|
| Always start with `RnHw:` | Namespace prefix — never omit |
| Lane is always second | Single script-font character (𝒞𝒯𝒦𝒮ℱ𝒢𝒟) |
| Category is optional | Fraktur font — omit if not yet defined |
| Topic follows category | Blackboard bold, or plain text if no topic |
| Qualifier is optional | Disambiguates when topic alone isn't unique |
| No spaces anywhere | Use CamelCase to separate words |
| Keys are case-sensitive | `TagVocabulary` ≠ `tagvocabulary` |

### When Topic Is Unknown

Use `noTopic` followed by a sequence character:

```
RnHw:𝒯:noTopic一
RnHw:𝒯:noTopic二
```

These are placeholders — update the key when the topic becomes clear.

---

## 3. JSON Stamp Structure

### Minimal Stamp

```json
{
  "key": "RnHw:𝒯:TagVocabulary",
  "lane": "tw",
  "url": "http://localhost:8080/#TagVocabulary",
  "title": "TagVocabulary"
}
```

### Full Stamp

```json
{
  "key": "RnHw:𝒯:𝕯TagVocabulary",
  "lane": "tw",
  "category": "𝕯",
  "topic": "TagVocabulary",
  "url": "http://localhost:8080/#TagVocabulary",
  "title": "Design: TagVocabulary",
  "version": "1.0",
  "created": "2026-02-23",
  "tags": ["design", "vocabulary", "reference"],
  "notes": "Core tag taxonomy for TW"
}
```

### Field Reference

| Field | Required | Description |
|---|---|---|
| `key` | ✅ | Unique identifier — see Section 2 |
| `lane` | ✅ | Short lane code (`tw`, `convo`, `keep`, etc.) |
| `url` | ✅ | Full URL or file path to the note |
| `title` | ✅ | Human-readable name |
| `category` | ○ | Fraktur character — add when known |
| `topic` | ○ | Blackboard bold or plain text |
| `version` | ○ | Stamp version, not note version |
| `created` | ○ | ISO date `YYYY-MM-DD` |
| `tags` | ○ | Free-form array for search |
| `notes` | ○ | One-line context note |

---

## 4. How to Choose a Lane

Lanes identify **where** the note lives — the system or platform.

```
𝒞  tw       → TiddlyWiki
𝒯  convo    → Claude conversations
𝒦  keep     → Google Keep
𝒮  sql      → SQL Server / database
ℱ  fs       → File system
𝒢  gh       → GitHub / repos
𝒟  docs     → Google Docs
```

**Rule:** One note, one lane. If a note exists in two systems, create two stamps with different lane codes.

---

## 5. How to Choose a Category

Categories are **organizational groupings** — they emerge from usage, not from planning.

**Do not pre-define categories.** Register notes with no category first, then assign categories once patterns become visible (typically after 50-100 notes).

When you do assign a category, pick a Fraktur character that feels semantically distinct to you. There is no fixed mapping yet — this will evolve.

**Early guidance:**
- Keep categories broad (Active/Archive, Personal/Shared, Concept/Procedure)
- Aim for 3-7 categories maximum
- A note with no obvious category stays `noTopic` — that is fine

---

## 6. How to Choose a Topic

Topics identify **what** the note is about — the subject domain.

```
𝕯        = Design
𝕽𝕯       = Redis
𝕰𝖘       = Essay
𝕷𝖆𝖙      = Lattice
noTopic  = Uncategorized
```

**Single-char topics** are for broad domains. **Multi-char topics** are for specific systems or projects.

**Rule:** If you hesitate more than 5 seconds choosing a topic — use `noTopic`. Assign later when the pattern is clearer.

---

## 7. When to Create a New Stamp vs. Update Existing

| Situation | Action |
|---|---|
| Note moved to new URL | Update `url` field, keep same key |
| Note renamed | Update `title`, keep same key |
| Topic becomes clear | Update `key`, `topic`, `category` |
| Note split into two | Create second stamp with new key |
| Note deleted | Remove stamp from DataDict |
| New version of same note | Increment `version` field |

**Key stability rule:** Once a key is used in a workflow or script, avoid changing it. Update other fields first. Only rename the key if the old name is genuinely misleading.

---

## 8. Registering a Stamp

### Via PowerShell

```bash
python -c "from rnhw_json_manager import register_note; print(register_note('tw', '𝕯', 'http://localhost:8080/#TagVocabulary', 'TagVocabulary', manual_key='RnHw:𝒯:𝕯TagVocabulary'))"
```

### Via TextBlaze

`/reg` → fill in the form fields → paste the generated command into PowerShell

### Checklist Before Registering

- [ ] URL is correct and working
- [ ] Lane code matches the platform
- [ ] Key follows `RnHw:{Lane}:{Topic}` format
- [ ] No spaces in key
- [ ] Title is human-readable

---

## 9. Common Mistakes

| Mistake | Fix |
|---|---|
| Spaces in key | Use CamelCase — `TagVocabulary` not `Tag Vocabulary` |
| Wrong lane code | Check lane table in Section 4 |
| Duplicate key | Check DataDict before registering |
| Over-planning categories | Register first, categorize later |
| Changing stable keys | Update other fields instead |

---

## 9. Appendix — Stamp Examples

Three complete examples showing progressively fuller use of the stamp grammar.

---

### 9.1 Simple — Lane + Title Only

Use when: registering quickly, topic not yet known.

```json
{
  "key": "RnHw:𝒯:noTopic一",
  "lane": "tw",
  "url": "http://localhost:8080/#SetAnchor",
  "title": "SetAnchor"
}
```

**Reading the key:** `RnHw` namespace → `𝒯` TiddlyWiki lane → `noTopic一` uncategorized, first entry.

---

### 9.2 Intermediate — Lane + Topic

Use when: topic is known, category not yet assigned.

```json
{
  "key": "RnHw:𝒯:𝕯TagVocabulary",
  "lane": "tw",
  "topic": "𝕯",
  "url": "http://localhost:8080/#TagVocabulary",
  "title": "Design: TagVocabulary",
  "created": "2026-02-23",
  "tags": ["design", "vocabulary"]
}
```

**Reading the key:** `RnHw` namespace → `𝒯` TiddlyWiki lane → `𝕯` Design topic → `TagVocabulary` qualifier.

---

### 9.3 Senior — Lane + Category + Topic + Full Metadata

Use when: note is stable, well-understood, part of an active workflow.

```json
{
  "key": "RnHw:𝒞:𝕮𝕷𝕾Main",
  "lane": "convo",
  "category": "𝕮",
  "topic": "𝕷𝕾",
  "url": "https://claude.ai/chat/abc123",
  "title": "ContextLatticeStamp — Main Design Conversation",
  "version": "1.2",
  "created": "2026-02-20",
  "tags": ["lattice", "design", "architecture"],
  "notes": "Primary conversation for CLS system design — reference before starting new sessions"
}
```

**Reading the key:** `RnHw` namespace → `𝒞` Claude conversations lane → `𝕮` category → `𝕷𝕾` LatticeStamp topic → `Main` qualifier.

---

<div style="page-break-after: always;"></div>

## Document History

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-02-23 | Initial creation |

---

**This is a living document — update as patterns emerge.**

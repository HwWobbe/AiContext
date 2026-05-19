# AI_SYSTEM_CONTEXT.md
# HwW WaysH Stack — Session Seed Document
# Last updated: 午㋄㏙ (2026-05-19)

## Identity
- Operator: HwW (Hans-Werner Wobbe)
- Entity: DataFix Canada (est. 1997)
- Location: at:4146 — 4146 Bath Road, Kingston K7M4Y7

## Stack
| Component  | Location                               | Status      |
|------------|----------------------------------------|-------------|
| TwNode     | http://localhost:8080                  | PM2 id:0    |
| Redis API  | http://localhost:5000                  | PM2 id:1    |
| OpenClaw   | ws://127.0.0.1:18791                   | manual      |
| GitHub     | C:\Users\hwobb\GitHub\AiContext        | origin/main |
| Python env | C:\Users\hwobb\.env\Scripts\python.exe | —           |

## OpenClaw Model Chain
- Primary:   openrouter/free
- Fallback1: deepseek/deepseek-chat
- Fallback2: anthropic/claude-haiku-4-5
- Restart:   cd C:\Users\hwobb\.openclaw && npx openclaw gateway
- Force:     npx openclaw gateway --force

## DataDict
- File: RnHw_DataDict.json v0.2.3
- Namespace: RnHw:{Lane}:{Category}{Topic}{Qualifier}
- Lanes: Script font (C T K S)
- Sync: sync_datadict_to_twh.py → TwNode

## Temporal Encoding (canonical)
- Year:    子丑寅卯辰巳午未申酉戌亥 (indexOrigin0: 2020=子)
- Month:   ㋀-㋋
- Day:     ㏠-㏾
- Hour:    ㍘-㍯
- Weekday: ☽♂☿♃♀♄☉

## Session Conventions
- ContextBase declared at session open (e.g. 午㋄)
- Left-truncated stamps resolve against ContextBase
- Full stamp required when content leaves session
- Same-day commit rule
- upArrow in Ask cycles full Talk Ask history

## NotationSpec (see Seed)
- Typography: Script=Lanes, Fraktur=Categories, BB=Topics
- HexPlex: fields 0-F, bracket type+scope
- PQL v0.4: algebras K/T/S, threading
- Pan-Talk: 0:ChatGPT 1:Claude 2:TwH 3:Keep 4:TbH 5:GitHub

## CloseBlock
- C1 DataDict mutations → GitHub commit
- C2 Dirty notes → resolved or flagged
- C3 New HexPlex nodes → Stage1 Keep note
- C4 Content leaving session → CLS stamp applied

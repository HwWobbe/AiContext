# Git Setup Guide: Local ↔ GitHub

**Goal:** `C:\Users\hwobb\GitHub\AiContext\` on your PC stays in sync with `github.com/HwWobbe/AiContext`

---

## Step 1: Install GitHub Desktop

1. Download from https://desktop.github.com
2. Install and sign in with your GitHub account
3. Authorize it when prompted

---

## Step 2: Clone the Repo to Local

1. In GitHub Desktop → **File → Clone Repository**
2. Choose the **GitHub.com** tab
3. Find `HwWobbe/AiContext` in the list
4. Set **Local Path** to:
   ```
   C:\Users\hwobb\GitHub\AiContext
   ```
   (GitHub Desktop will create the `AiContext` folder for you)
5. Click **Clone**

Your repo is now local. Any files in it are visible in File Explorer.

---

## Step 3: Add Your Files

Copy the files from your Claude downloads into the repo folder:

```
C:\Users\hwobb\GitHub\AiContext\
├── README.md                          ← from downloads
├── .gitignore                         ← from downloads
└── ContextLatticeStamp\
    ├── README.md                      ← from downloads
    └── Docs\
        ├── QuickStart.md              ← from downloads
        └── FolderStructureGuide.md    ← from downloads
```

---

## Step 5: Commit and Push

In GitHub Desktop:

1. You'll see all new files listed on the left under **Changes**
2. At the bottom left, type a commit message:
   ```
   Initial structure: README, QuickStart, FolderStructureGuide
   ```
3. Click **Commit to main**
4. Click **Push origin** (top bar)

Files are now live at `github.com/HwWobbe/AiContext`.

---

## Day-to-Day Workflow

| Action | What to do |
|---|---|
| Edit a file locally | Open in VS Code, edit, save |
| Save changes to GitHub | GitHub Desktop → write message → Commit → Push |
| Check what changed | GitHub Desktop shows a diff of every edit |
| Get changes from another machine | GitHub Desktop → **Fetch origin** → **Pull** |

---

## Viewing .md Files

### Recommended: VS Code (Desktop)
Download from https://code.visualstudio.com — free, open source, no account needed.

- Open any `.md` file → press `Ctrl+Shift+V` to toggle rendered preview
- Or press `Ctrl+K V` to open preview side-by-side with the raw text
- VS Code also has Git built in — you can commit and push without leaving the editor

### On GitHub (no install)
Once pushed, `github.com/HwWobbe/AiContext` renders all `.md` files automatically.  
Press `.` (period) on any GitHub repo page to open a browser-based VS Code with full markdown preview — no install required.

### Why not Typora?
Typora is closed source and phones home for license checks. VS Code is the better choice — open source, more capable, and free.

---

## Folder Path Summary

| Location | Path |
|---|---|
| Local repo | `C:\Users\hwobb\GitHub\AiContext\` |
| GitHub repo | `https://github.com/HwWobbe/AiContext` |
| Private data (never synced) | `C:\Users\hwobb\RnHw\RnHw_*.json` |

---

## If You Hit Problems

**"Repository already exists"** → Choose a different folder name or delete the empty local folder first.

**Files not showing in GitHub Desktop** → Make sure you copied files *inside* the cloned folder, not alongside it.

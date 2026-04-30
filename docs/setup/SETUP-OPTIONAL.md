---
title: "Optional: Git Setup"
parent: "Phase 1: Setup & Basics"
nav_order: 3
---

# Setup Guide (Part two)

Install the very nice to have tools for promptfoo evaluations.

## Git

Following the [git / source control management guide for VSCode](https://code.visualstudio.com/docs/sourcecontrol/overview), do:

**Download and install:**
1. Go to https://git-scm.com/download/win
2. Download and run the installer
3. Use default settings

**Configure Git (in terminal):**

Git needs to know who you are. In the VSCode terminal: 

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

**Verify installation:**
```bash
git --version
```

### Verify VSCode Detects Git

1. Open VSCode
2. Click the **Source Control** icon (branch symbol) on the left sidebar
3. You should see "Git" at the top
4. If you see "Git not found", restart VSCode

### Test Git Integration

1. Create a new file in VSCode (e.g., `test.txt`)
2. Add some text and save
3. Open Source Control panel (`Ctrl+Shift+G`)
4. You should see `test.txt` under "Untracked Files"

This confirms Git is working in VSCode!

{: .note }
> **Recommended**: Complete the full **[Session 5: Git Setup](../git/GIT-SETUP.md)** guide to learn Git workflow and practice with VSCode integration.

## Opencode
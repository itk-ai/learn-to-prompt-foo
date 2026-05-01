---
title: "Git Workflow"
parent: "Phase 3: Collaboration via Git"
nav_order: 3
---
<!-- OPenCode draft -->
# Git Workflow Guide

{: .warning }
> This is an Opencode draft

Simple Git workflow for managing your promptfoo work.

## What is Git?

Git is a version control system that:
- Tracks changes to your files
- Lets you undo mistakes
- Helps you collaborate with others
- Keeps history of all your work

## Basic Concepts

### Repository (repo)
A folder where Git tracks changes

### Commit
A saved change (like a "snapshot")

### Branch
A parallel version of your files (for experimenting)

### Remote
The copy of your repo on GitHub/GitLab

## VSCode Git Interface

### Source Control Panel
1. Click the **Source Control** icon (branch symbol) on left
2. Or press `Ctrl+Shift+G`

### What You'll See
```
SOURCE CONTROL
├── Changes
│   ├── M modified-file.yaml
│   ├── C created-file.yaml
│   └── D deleted-file.yaml
├── Staged Changes (after clicking +)
└── Commits (history)
```

## Common Workflows

### Workflow 1: Make Changes and Commit

**Step 1: Make changes**
- Edit your YAML files in VSCode

**Step 2: See changes**
- Open Source Control panel (`Ctrl+Shift+G`)
- See modified files under "Changes"

**Step 3: Review changes**
- Click on a file to see diff
- Green lines = added
- Red lines = removed

**Step 4: Stage changes**
- Click the `+` icon next to file
- Or click `+` next to "Changes" to stage all

**Step 5: Write commit message**
- Type in the text box at top
- Be specific: "Add 5 new test cases for GDPR questions"
- Not: "fix" or "update"

**Step 6: Commit**
- Click the checkmark ✓
- Or press `Ctrl+Enter`

**Step 7: Push to remote** (if needed)
- Click the sync icon (⏫⏬) at bottom of Source Control panel
- Or click "Sync Changes"

### Workflow 2: Create a New Branch

**When to use branches:**
- Trying new features
- Making big changes
- Working on multiple things at once

**Step 1: Create branch**
1. Click branch icon in bottom-left status bar
2. Click "Create new branch"
3. Type branch name: `feature/new-eval-config`
4. Press Enter

**Step 2: Make changes**
- Work on your files
- Commit as normal

**Step 3: Switch back to main**
1. Click branch icon in bottom-left
2. Select `main` or `master`

**Step 4: Merge when ready**
- This usually requires a Pull Request on GitHub

### Workflow 3: Undo Mistakes

#### Undo Uncommitted Changes
**Warning:** This is irreversible!

1. In Source Control panel
2. Find the file
3. Right-click on filename
4. Select "Discard Changes"

#### Undo Last Commit (keep changes)
1. In Source Control panel
2. Right-click on the commit
3. Select "Undo Commit"
4. Changes go back to staging area

#### Revert a Commit (keep history)
1. Open terminal
2. Find commit hash:
   ```bash
   git log
   ```
3. Revert it:
   ```bash
   git revert COMMIT_HASH
   ```

## Branch Naming Conventions

Use descriptive names:
- `feature/add-gdpr-tests`
- `fix/correction-rubric`
- `experiment/new-assertion-type`
- `docs/update-readme`

Avoid:
- `test`
- `fix`
- `new-branch`

## Commit Message Best Practices

### Good Commit Messages
```
Add 5 test cases for data retention questions
Fix regex pattern in refusal assertion
Update defaultTest provider configuration
Refactor tests to use assertionTemplates
```

### Bad Commit Messages
```
fix
update
test
stuff
```

### Commit Message Format
```
<type>: <description>

Types:
- feat: New feature
- fix: Bug fix
- docs: Documentation
- refactor: Code restructuring
- test: Adding tests

Examples:
feat: Add 10 new GDPR test cases
fix: Correct regex pattern in refusal assertion
docs: Update README with setup instructions
```

## Common Git Commands in Terminal

Sometimes you need to use the terminal:

```bash
# Check status
git status

# See all changes
git diff

# Add all files to staging
git add .

# Add specific file
git add file.yaml

# Commit with message
git commit -m "Your message here"

# View commit history
git log

# View compact history
git log --oneline

# Switch to branch
git checkout branch-name

# Create and switch to new branch
git checkout -b new-branch-name

# Push to remote
git push

# Pull latest changes
git pull

# See branches
git branch

# Delete branch
git branch -d branch-name
```

## Working with GitHub

### Create Pull Request

**When:** You want to merge your branch into main

**Steps:**
1. Push your branch to remote
2. Go to GitHub in browser
3. Click "Compare & pull request"
4. Add title and description
5. Click "Create pull request"
6. Wait for review
7. Merge when approved

### Review Changes

**On GitHub:**
1. Go to Pull Request
2. Click "Files changed" tab
3. Review each change
4. Add comments if needed
5. Approve or request changes

## Troubleshooting

### "Changes not staged for commit"
**Problem:** You edited files but haven't committed
**Solution:** 
```bash
git add .
git commit -m "Your message"
```

### "Untracked files"
**Problem:** New files not being tracked
**Solution:**
```bash
git add filename
git commit -m "Add new file"
```

### "Commit failed - please supply a message"
**Problem:** No commit message provided
**Solution:** Write a message in VSCode Source Control panel

### "Unable to resolve Git reference"
**Problem:** Branch doesn't exist
**Solution:** 
```bash
git checkout main
```

### Merge Conflicts
**Problem:** Two people changed the same file
**Solution:**
1. Open the conflicted file
2. Look for `<<<<<<<`, `=======`, `>>>>>>>`
3. Choose which changes to keep
4. Remove the conflict markers
5. Commit the resolution

## Git Workflow Checklist

### Before Starting Work
- [ ] Pull latest changes: `git pull`
- [ ] Create branch for new work (if needed)

### During Work
- [ ] Save files frequently (`Ctrl+S`)
- [ ] Check Source Control panel for changes
- [ ] Review changes before committing

### Before Committing
- [ ] Check YAML formatting
- [ ] Review diff for mistakes
- [ ] Write clear commit message

### After Committing
- [ ] Push to remote (if working with others)
- [ ] Create Pull Request (if needed)
- [ ] Update other branches

## Visual Guide

### Git Flow
```
main branch
    │
    ├───► feature branch ───► Pull Request ───► merged into main
    │
    └───► fix branch ───────► Pull Request ───► merged into main
```

### VSCode Git Panel
```
SOURCE CONTROL
  Changes (2)
    M eval-config.yaml     ← Click + to stage
    M tests.yaml
  
  Staged Changes (2)
    M eval-config.yaml     ← Ready to commit
    M tests.yaml
  
  [Commit message box]
  Add new test cases
  
  [✓] Commit    [⏫⏬] Sync
```

## Quick Reference

| Action | VSCode | Terminal |
|--------|--------|----------|
| View changes | Source Control panel | `git status` |
| Stage file | Click + | `git add file` |
| Stage all | Click + (all) | `git add .` |
| Commit | Click ✓ | `git commit -m "msg"` |
| Commit message | Text box | `-m "msg"` flag |
| Push/Pull | Sync icon | `git push` / `git pull` |
| Create branch | Click branch icon | `git checkout -b name` |
| View history | Commits section | `git log` |
| Undo changes | Right-click → Discard | `git checkout -- file` |

## Security Notes

### Don't Commit Secrets!
Never commit:
- API keys
- Passwords
- `.env` files with secrets
- Private credentials

### Check Before Committing
- [ ] No API keys in files
- [ ] No passwords
- [ ] `.env` is in `.gitignore`
- [ ] Only public/config files

## Next Steps

After learning Git:
1. ✅ Use Git for all your work
2. ✅ Commit frequently (small commits)
3. ✅ Write clear commit messages
4. ✅ Use branches for new features
5. ✅ Push regularly to backup

---

**Remember:** Git is your safety net. It's better to commit too often than too rarely!

**Need Help?** Ask your instructor if you're unsure about Git operations.

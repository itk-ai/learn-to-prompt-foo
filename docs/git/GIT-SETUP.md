---
title: "Session 5: Git Setup"
parent: "Phase 3: Collaboration via Git"
nav_order: 1
---

# Session 5: Git Setup for VSCode

**Goal**: Install and configure Git for VSCode, then practice the complete Git workflow by making improvements to this training repository

---

## What We'll Do Today

1. ✅ Install Git and configure it in VSCode
2. ✅ Set up GitHub account and connect to VSCode
3. ✅ Clone this repository and practice Git workflow
4. ✅ Make improvements to training materials
5. ✅ Create a Pull Request through VSCode and GitHub

---

## Part 1: Install Git

Complete the git setup in [Optional: Git Setup](../setup/SETUP-OPTIONAL.md#git)

---

## Part 2: Create & Link GitHub Account

### Create GitHub Account

1. Go to [https://github.com](https://github.com)
2. Click "Sign up"
3. Follow the registration process
4. Verify your email address

### Connect GitHub to VSCode

VSCode has built-in GitHub authentication:

1. In VSCode, open the **Source Control** panel (`Ctrl+Shift+G`)
2. You might see a notification: "Sign in to GitHub to access remote repositories"
3. Click **Sign in**
4. Your browser will open with GitHub authentication
5. Click **Authorize** when prompted
6. Return to VSCode - you should now see your GitHub account connected

{: .note }
> If you don't see the notification, you can also sign in via:
> - Command Palette (`Ctrl+Shift+P`) → "Accounts: Sign in"
> - Or click the account icon in the bottom-left corner

### Verify Connection

1. Open Source Control panel
2. You should see your GitHub account name at the bottom

---

## Part 3: Practice Git Workflow

Now you'll practice the complete Git workflow by making improvements to this training repository.

### Step 1: Clone the Repository

1. In VSCode, press `Ctrl+Shift+P` to open Command Palette
2. Type "Git: Clone" and select it
3. When prompted for URL, paste:
   ```
   https://github.com/itk-ai/learn-to-prompt-foo
   ```
4. Choose a local folder to save the repository (e.g., `C:\Users\YourName\<projects>`, where you created your 
   initial `promptfoo-getting-started` project in [Session 2: Getting Started](../setup/GETTING-STARTED.md)).
   In the cloning process a folder will be created with the same name as the github repo "learn-to-prompt-foo"
5. VSCode will clone the repository
6. When prompted, click **Open** to open the folder in VSCode

### Step 2: Explore the Repository

The repository contains training materials organized in folders:

```
docs/
├── setup/              # Sessions 1-2
├── evaluations/        # Sessions 3-4
├── git/                # Session 5 (this guide!)
├── cheat-sheets/       # Reference materials
└── material/           # Downloadable files
```

### Step 3: Find Something to Improve

**Your task**: Find a section in the training materials that could be clearer. 
Do not edit it yet, you'll do that in [Step 5: Make Your Edit](#step-5-make-your-edit)

**Good places to look**

- The sessions you've already completed (SETUP.md, GETTING-STARTED.md, PROMPTFOO-EVALUATIONS.md, ASSERTIONS-REFERENCE.md, BIAS-CHECKER.md)
- Look for:
  - Long paragraphs that could be split
  - Missing examples or clarifications
  - Typos or formatting issues
  - Unclear instructions
  - Sections that could use more detail

{: .note }
> Don't overthink this! Even small improvements like fixing a typo or clarifying one sentence are valuable.

### Step 4: Create a New Branch

**Why branches?** They are a way to collect change and "package" them for others to look at. They are also a way to 
let you experiment without affecting the main version.

1. Look at the bottom-left of VSCode window - you'll see `main` (current branch)
2. Click on `main`
3. Click "Create new branch"
4. Type a descriptive name:
   ```
   fix/improve-[topic]
   ```
   Examples:
   - `fix/improve-setup-clarity`
   - `fix/typo-getting-started`
   - `adds/example-to-evaluations`
5. Press Enter

VSCode automatically switches to your new branch.

### Step 5: Make Your Edit

Remember what you decided to edit in [step 3](#step-3-find-something-to-improve)

1. Navigate to the file you want to improve (in the file explorer on left)
2. Open the markdown file
3. Make your improvement:
   - Fix typos
   - Clarify confusing sentences
   - Add missing examples
   - Improve formatting
4. Save the file (`Ctrl+S`)
5. Format the document (`Shift+Alt+F`) to ensure proper markdown formatting

### Step 6: Review Changes in Source Control

1. Open Source Control panel (`Ctrl+Shift+G`)
2. You'll see your modified file under "Changes"
3. Click on the filename to see the diff:
   - **Green lines** = text you added
   - **Red lines** = text you removed
4. Review carefully to make sure changes look correct

{: .note }
> The diff view helps you catch mistakes before committing!

### Step 7: Stage and Commit Your Changes

**Staging**: Preparing files for commit (like putting items in a box)

1. In Source Control panel, hover over your modified file
2. Click the **+** (plus) icon next to the filename
3. The file moves to "Staged Changes"

**Committing**: Saving a snapshot of your changes

1. In the text box at the top of Source Control panel, write a commit message
2. Be specific and descriptive:
   - ✅ Good: "Improve clarity in Part 3 of GETTING-STARTED guide"
   - ✅ Good: "Fix typo in BIAS-CHECKER installation steps"
   - ❌ Bad: "fix" or "update" or "changes"
3. Click the **checkmark** (✓) button to commit
4. Or press `Ctrl+Enter`

### Step 8: Push to GitHub

Now your commit is local. Push it to GitHub to share it.

1. In Source Control panel, look for the **sync icon** (⏫⏬) at the bottom
2. Click "Sync Changes" or the sync icon
3. VSCode pushes your branch to GitHub
4. You might see a notification confirming the push

{: .note }
> The first time you push, VSCode might ask for confirmation to publish the branch. Click "Publish Branch".

### Step 9: Create Pull Request on GitHub

A Pull Request (PR) proposes your changes for review and merging.

1. Open your web browser
2. Go to: [https://github.com/itk-ai/learn-to-prompt-foo](https://github.com/itk-ai/learn-to-prompt-foo)
3. You should see a banner: "[your-username] has 1 push on branch [your-branch]"
4. Click **Compare & pull request**
5. If you don't see the banner:
   - Click the **Pull requests** tab
   - Click **New pull request**
   - Base: `main`
   - Compare: your branch name (e.g., `docs/improve-clarity`)
   - Click **Create pull request**

### Step 10: Fill in Pull Request Details

1. **Title**: Describe your change
   - Example: "Improve clarity in Session 2 installation steps"
2. **Description**: Explain what you changed and why
   - Example: "I found the installation instructions in Part 3 were unclear about the order of steps. I've reorganized them and added a clarifying example."
3. Review your changes in the "Files changed" tab
4. Click **Create pull request** (not "Merge pull request"!)

{: .note }
> Don't merge your own PR! The instructor will review and merge it.

### Step 11: Review Your Pull Request

1. Click on the **Files changed** tab
2. Verify your changes look correct
3. Practice adding comments (optional):
   - Hover over any line
   - Click the **+** icon to add a comment
   - This is how reviewers leave feedback

---

## Part 5: Practice Undoing Mistakes

Git is your safety net. Let's practice undoing changes.

### Exercise A: Discard Uncommitted Changes

**Warning**: This is irreversible!

1. Open any markdown file
2. Make some changes (don't commit)
3. Open Source Control panel (`Ctrl+Shift+G`)
4. Find your file under "Changes"
5. **Right-click** on the filename
6. Select **"Discard Changes"**
7. Verify the file reverts to its original state

### Exercise B: Undo a Commit

1. Make a change to a file
2. Stage it (click **+**)
3. Commit with a message
4. In Source Control panel, scroll to "Commits" section
5. Find your commit
6. **Right-click** on the commit
7. Select **"Undo Commit"**
8. The commit is undone, changes return to staging area

{: .warning }
> **Important**: Both "Discard Changes" and "Undo Commit" are irreversible operations. Always review before using!

---

### VSCode Git Shortcuts

| Action | Keyboard Shortcut |
|--------|------------------|
| Open Source Control | `Ctrl+Shift+G` |
| Open Terminal | `` Ctrl + ` `` |
| Save File | `Ctrl+S` |
| Format Document | `Shift+Alt+F` |
| Command Palette | `Ctrl+Shift+P` |

---

## Next Steps

### ✅ Ready for Session 6

You now have Git set up and have practiced the complete workflow. In **Session 6 (CONTRIBUTE.md)**, you'll:

- Clone the **prompfoo-docker** repository
- Add your own promptfoo evaluation configs
- Create branches and commits
- Submit Pull Requests to contribute to the shared repository

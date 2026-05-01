---
title: "Session 6: Contributing to prompfoo-docker"
parent: "Phase 3: Collaboration via Git"
nav_order: 2
---

# Session 6: Contributing Your Evaluation to prompfoo-docker

**Goal**: Contribute your Bias-checker evaluation config to the shared prompfoo-docker repository via Pull Request

---

## What We'll Do Today

1. ✅ Request access to the prompfoo-docker repository
2. ✅ Clone the repository and explore its structure
3. ✅ Create a new evaluation folder with your Bias-checker config
4. ✅ Adapt paths from your Session 4 config to Docker paths
5. ✅ Create a README.md following the official template
6. ✅ Commit and push your changes
7. ✅ Create a Pull Request for review

---

## Prerequisites

Before starting this session, you should have:

- ✅ Completed Sessions 1-4 (Setup, Getting Started, Evaluations, Bias-checker)
- ✅ Completed Session 5 (Git Setup) - practiced Git workflow
- ✅ A completed Bias-checker evaluation config from Session 4
- ✅ Git configured in VSCode with GitHub account connected

---

## Part 1: Request GitHub Access

{: .warning }
> **Important**: You must have access to the repository before you can contribute. Do not start until you have access!

### Step 1: Contact Your Instructor

Send a message to your instructor with:
- Your GitHub username
- Request to contribute to `itk-dev/promptfoo-docker` repository

### Step 2: Accept GitHub Invitation

Once the instructor adds you as a collaborator:

1. Check your email for invitation from GitHub
2. Click the invitation link
3. OR visit [https://github.com/notifications](https://github.com/notifications)
4. Accept the invitation to `itk-dev/promptfoo-docker`

### Step 3: Verify Access

1. Open your browser
2. Go to: [https://github.com/itk-dev/promptfoo-docker](https://github.com/itk-dev/promptfoo-docker)
3. You should see the repository without an "access denied" message
4. You should be able to see the `eval-configs/` folder

{: .note }
> If you still see "access denied," contact your instructor again. Do not proceed until you have access.

---

## Part 2: Clone the Repository

### Step 1: Clone in VSCode

1. Open VSCode
2. Press `Ctrl+Shift+P` to open Command Palette
3. Type "Git: Clone" and select it
4. When prompted for URL, paste:
   ```
   https://github.com/itk-dev/promptfoo-docker
   ```
5. Choose a local folder location (e.g., `C:\Users\YourName\projects\promptfoo-docker`)
6. VSCode will clone the repository
7. When prompted, click **Open** to open the folder in VSCode

### Step 2: Explore the Repository Structure

The repository contains:

```
promptfoo-docker/
├── eval-configs/              # Evaluation configurations
│   ├── MBU-Databeskyttelse/   # Example evaluation
│   └── Videns-evalueringer/   # Another example
├── assertions/                 # Custom Python assertions
│   ├── essential_claims_assertion.py
│   ├── ja_nej_assertion.py
│   └── refusal_assertion.py
├── providers/                  # Custom providers
│   └── owui.js
├── docs/
│   └── promptfoo-writers/
│       ├── add-new-evals.md   # Guide you'll follow
│       ├── assertions.md
│       ├── providers.md
│       └── README.md
└── .env.example               # Environment variables (example)
```

### Step 3: Updating .env-file

_IF_ you want to be able to run the evaluations locally in this project, you need to 
copy the `.env.example` and name the copy `.env`. Here you would need to fill in the
endpoints and api keys like you first did in 
[Part 1 of Session 2: Getting Started](../setup/GETTING-STARTED.md#part-1-setting-up-your-environment).

{: .warning-title }
> Important
> 
> You must **never** put credentials, such as API keys, into files tracked by git and thus shared.
> 
> Notice, that the file `.env` will not appear in the git-staging area in VSCode. This is because git
> is explicitly told to ignore a file with the name ".env". The ignored files can be seen in the file
> `.gitignore`, that you can find in the project root.

### Step 4: Read the Guide

Open `docs/promptfoo-writers/add-new-evals.md` in VSCode:
- Review the README.md template structure
- Note the required sections
- Understand the folder naming convention

---

## Part 3: Create Your Evaluation Folder

### Prerequisite: Create a New Branch

Before making any changes to the files the in repo, first let's create a new branch.

1. Look at the bottom-left of VSCode window - you'll see `main` (current branch)
2. Click on `main`
3. Click "Create new branch"
4. Type: `adds/ba-biastjekker-eval`
5. Press Enter

VSCode automatically switches to your new branch.

Now we can start making our additions to the project.

### Step 1: Create New Folder

1. In VSCode file explorer, navigate to `eval-configs/`
2. Right-click on `eval-configs/`
3. Select "New Folder"
4. Name it following the pattern: `BA-Biastjekker`

{: .note }
> Use clear, descriptive names. Following the pattern of existing folders like `MBU-Databeskyttelse`.

### Step 2: Create Your Files

You'll create two files in the new folder:
1. `promptfooconfig.yaml` - Your evaluation configuration
2. `README.md` - Documentation following the template

---

## Part 4: Adapt Your Bias-checker Config

### Step 1: Copy Your Session 4 Config

Open your completed Bias-checker config from [Session 4](../evaluations/BIAS-CHECKER.md) and copy it to the new folder.

### Step 2: Update Provider Paths

**Change from local paths to Docker paths:**

```yaml
# FROM (your local Session 4 config):
providers:
  - id: file://providers/owui.js
```

```yaml
# TO (Docker paths):
providers:
  - id: file:///app/providers/owui.js
```

_note the three forward slashes `///` after `file:`_

**Why?** The prompfoo-docker repo runs in what is known as a "Docker container" on a server, you can think of a
(docker) container like a dedicated computer, that does only one thing. The prompfoo-docker container just runs 
our promptfoo setup. In that "dedicated computer" the file-structure of this repo is copied in at `/app/`, so 
that every path in this project will be prepended with `/app/`. E.g.

| Path in `prompfoo-docker` folder (this repo)       | Path in the container                                   |
|----------------------------------------------------|---------------------------------------------------------|
| `providers/owui.js`                                | `/app/providers/owui.js`                                |
| `assertions/refusal_assertion.py`                  | `/app/assertions/refusal_assertion.py`                  |
| `eval-configs/BA-Biastjekker/promptfooconfig.yaml` | `/app/eval-configs/BA-Biastjekker/promptfooconfig.yaml` |

### Step 3: Update Assertion Paths

In all the assertions in all the test cases

```yaml
# FROM:
- type: python
  value: file://assertions/refusal_assertion.py

# TO:
- type: python
  value: file:///app/assertions/refusal_assertion.py
```

Update all custom assertion paths similarly.

### Step 4: Update Python Executable Path

In the `defaultTest.options.config` section:

```yaml
# FROM (Windows local):
pythonExecutable: .venv/Scripts/python.exe

# TO (Linux/Docker):
pythonExecutable: .venv/bin/python
```

### Step 5: Verify Environment Variables

Your config should reference:
- `STG_OWUI_ENDPOINT`
- `STG_OWUI_API_KEY`

These are already configured in the `.env` file in the prompfoo-docker repo, so you don't need to create a new `.env` file.

### Step 6: Review Your Test Cases

Ensure all your Session 4 test cases are included:
- Format validation tests
- Bias analysis tests
- Refusal tests
- Any custom tests you created

---

## Part 5: Create README.md

### Step 1: Copy the Template

From `docs/promptfoo-writers/add-new-evals.md`, copy the README template:

{: .note }
> The template uses markdown code blocks. Remove the outer code block markers when creating your README.md.

### Step 2: Fill in the Template

````markdown
# BA Biastjekker

Tests and assertations are constructed by [Your Name] and Anne Vibeke.

Original tests are available at: [Link to Session 4 materials or leave blank if not applicable]

## Requirements

- Access to STG OWUI environment
- Custom assertions:
    - refusal_assertion.py (from `assertions/`)
- Rubric assertions:
    - AarhusAI-default (judge model)

## Run tests

```sh name=evaluate
task eval -- eval-configs/BA-Biastjekker/promptfooconfig.yaml
```

## Notes

- Tests focus on bias detection in job postings
- All assertions and test cases are in Danish
- Refusal tests verify the assistant only handles bias-related questions
- Format tests ensure all 5 required sections are present in output

## Known issues and improvements

- [List any known limitations or areas for future improvement]
````

{: .note }
> Replace `[Your Name]` with your actual name. Fill in the "Known issues" section with any notes about your tests.

---

## Part 6: Git Workflow - Branch, Commit, Push

Now let's continue the git workflow, that was started by branching out.

### Step 1: Review Changes

1. Open Source Control panel (`Ctrl+Shift+G`)
2. You should see your new files under "Changes":
   - `eval-configs/BA-Biastjekker/promptfooconfig.yaml` (new file)
   - `eval-configs/BA-Biastjekker/README.md` (new file)

### Step 2: Stage All Changes

1. Click the **+** (plus) icon next to "Changes" to stage all files
2. Both files should move to "Staged Changes"

### Step 3: Write Commit Message

In the text box at the top of Source Control panel:

```
adds: BA Biastjekker evaluation config
```

Keep it concise following the convention: `type: description`

### Step 4: Commit

1. Click the **checkmark** (✓) button
2. Or press `Ctrl+Enter`

### Step 5: Push to GitHub

1. In Source Control panel, click the **sync icon** (⏫⏬) at the bottom
2. Or click "Sync Changes"
3. VSCode pushes your branch to GitHub
4. You might see a notification confirming the push

{: .note }
> The first time you push, VSCode might ask for confirmation to publish the branch. Click "Publish Branch".

---

## Part 7: Create Pull Request

### Step 1: Go to GitHub

1. Open your web browser
2. Go to: [https://github.com/itk-dev/promptfoo-docker](https://github.com/itk-dev/promptfoo-docker)
3. You should see a banner: "[your-username] has 1 push on branch adds/ba-biastjekker-eval"
4. Click **Compare & pull request**

{: .note }
> If you don't see the banner:
> - Click the **Pull requests** tab
> - Click **New pull request**
> - Base: `main`
> - Compare: `adds/ba-biastjekker-eval`
> - Click **Create pull request**

### Step 2: Fill in Pull Request Details

**Title:**
```
adds: BA Biastjekker evaluation config
```

**Description:**
```
## What this PR does
Adds evaluation configuration for BA Biastjekker (bias checker for job postings)

## Changes included
- promptfooconfig.yaml with bias analysis tests
- README.md with setup and run instructions

## Testing
- Run: `task eval -- eval-configs/BA-Biastjekker/promptfooconfig.yaml`
- All tests use STG OWUI environment
- Custom assertions from `assertions/` folder

## Notes
- Based on Session 4 training materials
- Tests written in Danish
- Judge model: AarhusAI-default
```

### Step 3: Submit Pull Request

1. Review your changes in the "Files changed" tab
2. Click **Create pull request** (not "Merge pull request"!)

{: .note }
> Don't merge your own PR! The instructor will review and merge it.

---

## Part 8: Review Your Pull Request

### Step 1: Check Files Changed

1. Click on the **Files changed** tab
2. Verify your changes look correct:
   - `promptfooconfig.yaml` has correct paths (`/app/providers/`, `/app/assertions/`)
   - `README.md` follows the template
   - All test cases are included

### Step 2: Practice Adding Comments (Optional)

1. Hover over any line in the diff
2. Click the **+** icon to add a comment
3. This is how reviewers leave feedback

---

## What You've Learned

### ✅ Completed Today

- Requested and received repository access
- Cloned the prompfoo-docker repository
- Created a new evaluation folder
- Adapted paths from local to Docker environment
- Created documentation following the official template
- Used Git workflow to contribute changes
- Submitted a Pull Request for review

### Key Differences from Session 5

| Aspect | Session 5 (Practice) | Session 6 (Real Contribution) |
|--------|---------------------|-------------------------------|
| **Repository** | learn-to-prompt-foo | prompfoo-docker |
| **Access** | Public, anyone can clone | Private, needs instructor access |
| **Goal** | Practice Git workflow | Contribute real evaluation |
| **Files** | Edit existing markdown | Create new folder + files |
| **Paths** | Relative paths | Absolute `/app/` paths |

---

## Next Steps

### ✅ Contribution Submitted

Your evaluation config is now in the Pull Request queue, waiting for instructor review.

### What Happens Next

1. Instructor reviews your PR
2. May suggest improvements or request changes
3. Once approved, your eval will be merged into `main`
4. Your evaluation will be available to everyone

### Continue Learning

- **Review your work**: Check the merged PR to see how it looks in the main branch
- **Practice more**: Create additional evaluation configs for other models
- **Explore**: Look at other evaluations in the repo to learn different patterns

### Resources

- **add-new-evals.md**: README template and guidelines
- **assertions.md**: Documentation on custom assertions
- **providers.md**: Documentation on custom providers
- **Promptfoo Docs**: [https://www.promptfoo.dev/docs/](https://www.promptfoo.dev/docs/)

---

**Congratulations!** 🎉

You've successfully contributed your first evaluation to the shared prompfoo-docker repository. Your Bias-checker tests are now available for the entire team to use and build upon!

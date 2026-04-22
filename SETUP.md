# Setup Guide - Step by Step

This guide walks you through installing all the software you need.

## Step 1: Install Visual Studio Code

### Download
1. Open your browser and go to: https://code.visualstudio.com/
2. Click the big blue **Download for Windows** button
3. The file `VSCodeUserSetup-x64-*.exe` will download

### Install
1. Open the Downloads folder
2. Double-click the VSCode installer
3. Click **I agree** on the license
4. Choose installation location (default is fine)
5. **Important:** Check the box "Add to PATH" (makes it easier to open from anywhere)
6. Check "Add 'Open with Code' action to Windows Explorer context menu"
7. Click **Install**
8. Click **Launch Visual Studio Code** when done

### First Launch
1. VSCode will open with a welcome screen
2. You can close the welcome tab for now
3. VSCode is ready to use!

## Step 2: Install Node.js

### Download
1. Go to: https://nodejs.org/
2. Click the **LTS** button (Long Term Support - more stable)
3. The file `node-v*-x64.msi` will download

### Install
1. Open Downloads folder
2. Double-click the Node.js installer
3. Click **Next** through the wizard
4. Accept the license agreement
5. Use default installation path
6. **Important:** Check "Automatically install the necessary tools" if asked
7. Click **Install**
8. Click **Finish**

### Verify Installation
1. Open VSCode
2. Go to **View** → **Terminal** (or press `Ctrl+``)
3. Type: `node --version`
4. You should see something like `v20.x.x`
5. Type: `npm --version`
6. You should see something like `10.x.x`

If you see version numbers, Node.js is installed correctly!

## Step 3: Install Git

### Download
1. Go to: https://git-scm.com/download/win
2. Click **Download for Windows**
3. The file `Git-*.exe` will download

### Install
1. Open Downloads folder
2. Double-click the Git installer
3. Click **Next** through most options
4. **Important settings:**
   - Use default editor (usually Vim, we'll use VSCode instead)
   - Use Git from Command Prompt (default)
   - Use Windows' default case-sensitive file behavior
5. **Important:** Check "Enable Git Credential Manager"
6. Click **Install**
7. Click **Finish**

### Configure Git
1. In VSCode terminal, type these commands (one at a time):

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Replace with your actual name and email!

### Verify Installation
```bash
git --version
```

Should show something like `git version 2.x.x`

## Step 4: Install VSCode Extensions

Extensions add helpful features to VSCode.

### Install YAML Extension
1. In VSCode, click the **Extensions** icon on the left (looks like squares)
2. Search for "YAML"
3. Click on **YAML by Red Hat**
4. Click **Install**

### Install GitLens (Optional but Recommended)
1. In Extensions panel, search for "GitLens"
2. Click on **GitLens - Git supercharged**
3. Click **Install**

### Install Prettier (Optional - for formatting)
1. Search for "Prettier"
2. Click on **Prettier - Code formatter**
3. Click **Install**

## Step 5: Get the Promptfoo Project

### Option A: Clone from Git Repository
If you have a Git repository:

1. Open VSCode
2. Click **File** → **Open Folder...**
3. Choose where you want the project (e.g., Documents)
4. Click **Select Folder**
5. Click **Yes, I trust the authors** if asked
6. In the terminal (`Ctrl+``):
   ```bash
   git clone https://github.com/your-org/promptfoo-docker.git
   ```
7. Click **Open Folder** when prompted about the cloned repository

### Option B: Copy Files
If you're getting files from your instructor:

1. Copy the project folder to your computer
2. In VSCode: **File** → **Open Folder...**
3. Select the project folder
4. Click **Select Folder**
5. Click **Yes, I trust the authors**

## Step 6: Install promptfoo

In the VSCode terminal, navigate to the project folder and install:

```bash
cd promptfoo-docker
npm install -g promptfoo
```

Verify installation:
```bash
promptfoo --version
```

## Troubleshooting

### "Command not found" errors
- Close VSCode completely and reopen it
- Make sure you checked "Add to PATH" during installation
- Restart your computer if needed

### Permission errors
- If you see "permission denied" or similar, you may need to run with PEDM
- This should be automatically handled by your security software

### VSCode won't open files
- Make sure you opened a **folder**, not individual files
- Use **File** → **Open Folder**

## Next Steps

Once setup is complete:
1. ✅ You have VSCode installed and working
2. ✅ You have Node.js and npm installed
3. ✅ You have Git installed and configured
4. ✅ You have the project folder open in VSCode
5. ✅ You can run commands in the terminal

**Ready for training!** Move on to the [Training Agenda](./TRAINING-AGENDA.md)

---

**Need Help?** Contact your instructor if you get stuck at any step.

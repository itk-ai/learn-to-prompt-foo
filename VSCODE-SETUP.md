# VSCode Setup Guide

This guide helps you configure VSCode for working with promptfoo YAML files.

## Opening Your First Project

### Open a Folder
1. Start VSCode
2. Click **File** → **Open Folder**
3. Navigate to your project folder
4. Select the folder (not individual files)
5. Click **Select Folder**
6. Click **Yes, I trust the authors** if prompted

### Understanding the Interface
```
┌─────────────────────────────────────────────┐
│  File  Edit  Selection  View  Help         │ ← Menu bar
├──────┬─────────────────────────┬────────────┤
│      │                         │            │
│ Icon │  Editor Area            │  Explorer  │
│ Bar  │  (your files open here) │  (file     │
│      │                         │   list)    │
│      │                         │            │
│      │                         │            │
├──────┴─────────────────────────┴────────────┤
│  Terminal (Ctrl+`)                          │ ← Integrated terminal
└─────────────────────────────────────────────┘
```

## Essential Settings

### Configure YAML Settings
1. Open settings: **File** → **Preferences** → **Settings** (or `Ctrl+,`)
2. Search for "YAML"
3. Recommended settings:
   - ✅ `YAML: Schema Download` - Enable (downloads schema for validation)
   - ✅ `YAML: Format` - Enable auto-formatting
   - ✅ `YAML: Validate` - Enable validation

### Configure Editor Settings
Search for and enable:
- ✅ `Editor: Format On Save` - Auto-format when saving
- ✅ `Editor: Insert Spaces` - Use spaces instead of tabs
- ✅ `Editor: Tab Size` - Set to 2 (for YAML)
- ✅ `Editor: Detect Indentation` - Enable

### Save as Workspace Settings (Optional)
To save settings for your project:
1. Open settings
2. Click `{}` icon next to a setting
3. Select "Workspace Settings"
4. This creates a `.vscode/settings.json` in your project

## Essential Extensions

### 1. YAML (by Red Hat)
**Purpose:** YAML syntax highlighting and validation

**Install:**
1. Click Extensions icon (left sidebar, 4 squares)
2. Search "YAML"
3. Click on "YAML by Red Hat"
4. Click Install

**Features:**
- ✅ Syntax highlighting
- ✅ Schema validation (shows errors)
- ✅ Auto-completion
- ✅ Auto-formatting

### 2. GitLens (Optional but Recommended)
**Purpose:** Enhanced Git integration

**Install:**
1. Search "GitLens"
2. Click on "GitLens - Git supercharged"
3. Click Install

**Features:**
- ✅ See who changed each line
- ✅ Better Git history
- ✅ Inline blame annotations

### 3. Prettier (Optional)
**Purpose:** Code formatter

**Install:**
1. Search "Prettier"
2. Click on "Prettier - Code formatter"
3. Click Install

**Features:**
- ✅ Consistent formatting
- ✅ Auto-format on save

## Using the Integrated Terminal

### Open Terminal
- Click **View** → **Terminal**
- Or press `` Ctrl + ` `` (backtick)
- Or click the terminal icon in top-right

### Terminal Basics
```bash
# Navigate to project folder
cd promptfoo-docker

# List files
ls

# Run promptfoo eval
promptfoo eval --config eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml

# Check promptfoo version
promptfoo --version
```

### Terminal Tips
- Press `↑` and `↓` to cycle through command history
- Press `Ctrl+C` to cancel a running command
- Click the `+` button to open a new terminal
- Click the dropdown to see available shells

## Working with Files

### Create New File
1. In Explorer panel, hover over folder
2. Click the **New File** icon (page with +)
3. Type filename (e.g., `my-config.yaml`)
4. Press Enter

### Open File
- Double-click in Explorer
- Or click on filename

### Save File
- Press `Ctrl+S`
- Or **File** → **Save**
- Or click the × on the tab (asks to save first)

### Close File
- Click × on the tab
- Or `Ctrl+W`

## YAML-Specific Features

### Auto-Completion
1. Start typing in a YAML file
2. Press `Ctrl+Space` for suggestions
3. Select from dropdown with arrow keys + Enter

### Format Document
1. Right-click in editor
2. Select **Format Document**
3. Or press `Shift+Alt+F`
4. Or save the file (if "Format On Save" is enabled)

### View Problems
1. Click **View** → **Problems**
2. Or click the warning icon in bottom-left
3. Shows all errors and warnings
4. Click on a problem to jump to it

### Schema Validation
If YAML schema is configured:
- Red underline = error
- Yellow underline = warning
- Hover over underline to see message
- Example errors:
  - "Missing required property"
  - "Type mismatch"
  - "Invalid value"

## Git Integration

### Source Control Panel
1. Click Source Control icon (branch symbol) on left
2. Or press `Ctrl+Shift+G`

### Basic Git Workflow
1. **Make changes** to files
2. **See changes** in Source Control panel
3. **Stage changes**: Click `+` next to file
4. **Write commit message** in text box
5. **Commit**: Click checkmark or **Commit**
6. **Push**: Click sync icon (⏫⏬)

### View Git History
1. Click Source Control icon
2. Click on a commit in "COMMITS" section
3. See what changed in that commit

### Diff View
1. In Source Control panel, click on a modified file
2. See side-by-side comparison
3. Green = added, Red = removed

## Helpful Keyboard Shortcuts

| Action | Windows/Linux | Mac |
|--------|---------------|-----|
| Open Terminal | `Ctrl+`` | `Ctrl+`` |
| New File | `Ctrl+N` | `Cmd+N` |
| Open File | `Ctrl+O` | `Cmd+O` |
| Save File | `Ctrl+S` | `Cmd+S` |
| Close File | `Ctrl+W` | `Cmd+W` |
| Format Document | `Shift+Alt+F` | `Shift+Cmd+F` |
| Find | `Ctrl+F` | `Cmd+F` |
| Replace | `Ctrl+H` | `Cmd+H` |
| Go to Line | `Ctrl+G` | `Cmd+G` |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Split Editor | `Ctrl+\` | `Cmd+\` |
| Toggle Sidebar | `Ctrl+B` | `Cmd+B` |

## Creating a Custom Snippet

Create a promptfoo config snippet for faster typing:

1. **File** → **Preferences** → **User Snippets**
2. Select **yaml.json**
3. Add this:

```json
{
  "Promptfoo Config": {
    "prefix": "promptfoo",
    "body": [
      "# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json",
      "description: \"${1:My evaluation}\"",
      "",
      "prompts:",
      "  - \"{{${2:question}}}\"",
      "",
      "providers:",
      "  - id: file:///app/providers/owui.js",
      "    config:",
      "      apiEndpointEnvironmentVariable: \"${3:DEV_OWUI_ENDPOINT}\",",
      "      apiKeyEnvironmentVariable: \"${4:DEV_OWUI_API_KEY}\",",
      "      model: \"${5:databeskyttelse-mbu}\",",
      "      outputSources: true",
      "",
      "defaultTest:",
      "  options:",
      "    provider: file:///app/providers/owui.js",
      "",
      "tests:",
      "  - vars:",
      "      question: \"${6:Test question}\"",
      "    assert:",
      "      - type: contains",
      "        value: \"${7:expected text}\""
    ],
    "description": "Create a basic promptfoo config"
  }
}
```

Now type `promptfoo` and press `Tab` to generate a template!

## Troubleshooting

### VSCode Won't Open Files
**Problem:** Files don't open or show errors
**Solution:**
- Make sure you opened a **folder**, not individual files
- Use **File** → **Open Folder**

### YAML Validation Shows Errors
**Problem:** Red underlines everywhere
**Solution:**
- Check indentation (should be 2 spaces)
- Look for missing colons
- Make sure you're using spaces, not tabs
- Check bottom-right shows "Spaces: 2"

### Terminal Won't Open
**Problem:** Terminal panel doesn't appear
**Solution:**
- Try `` Ctrl + ` `` again
- Check **View** → **Terminal** is checked
- Restart VSCode

### Git Commands Don't Work
**Problem:** "git: command not found"
**Solution:**
- Make sure Git is installed
- Close and reopen VSCode
- Restart computer if needed

### Auto-Completion Not Working
**Problem:** No suggestions when typing
**Solution:**
- Make sure YAML extension is installed
- Press `Ctrl+Space` to trigger manually
- Check if file has `.yaml` or `.yml` extension

## Quick Tips

1. **Always open a folder**, not individual files
2. **Use the terminal** inside VSCode, not separate Command Prompt
3. **Format before saving** - makes errors easier to spot
4. **Check the Problems panel** to see all errors
5. **Use snippets** for repetitive patterns
6. **Save often** - `Ctrl+S` becomes automatic with practice

## Next Steps

After setup:
1. ✅ Open your project folder in VSCode
2. ✅ Install recommended extensions
3. ✅ Configure settings
4. ✅ Open integrated terminal
5. ✅ Try creating a test YAML file
6. ✅ Try running a command in terminal

**Ready to learn!** Move on to [Training Agenda](./TRAINING-AGENDA.md)

---

**Need Help?** Ask your instructor if VSCode behaves unexpectedly.

# Setup Guide

Install the tools you need for promptfoo evaluations.

## Visual Studio Code (VSCode)

**Follow the official installation guide:**
https://code.visualstudio.com/docs/setup/windows

**Important notes:**
- Use the **User setup** (doesn't require admin rights)
- Setup adds VS Code to your `%PATH%` - restart terminal after install
- If you have PEDM restrictions, the user setup should work without elevation

## Node.js

Node.js is a JavaScript runtime environment and this is needed to run
promptfoo on your own computer.

Following the [initial part of the VSCode node.js totorial](https://code.visualstudio.com/docs/nodejs/nodejs-tutorial), 
do the following

**Download and install:**
1. Go to https://nodejs.org/
2. Download the **LTS** version (Long Term Support - more stable)
3. Run the installer with default settings
4. Restart your terminal after installation:  
   In VSCode choose `View > Terminal` (Ctrl+` with the backtick character) and open the integrated terminal, now 

   **Verify installation:**
   ```bash
   node --version
   npm --version
   ```

## VSCode Extensions

After installing VSCode, install the **YAML extension**:

1. Open VSCode
2. Click Extensions icon (left sidebar, 4 squares)
3. Search for "YAML"
4. Install **YAML by Red Hat** (_For reference: This is the 
   [corresponding webpage extension](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml)_)

### Configure YAML Settings
1. Open settings: **File** → **Preferences** → **Settings** (or `Ctrl+,`)
2. Search for "YAML"
3. Recommended settings:
   - ✅ `YAML: Schema Download` - Enable (downloads schema for validation)
   - ✅ `YAML: Format` - Enable auto-formatting
   - ✅ `YAML: Validate` - Enable validation

## promptfoo

Finally we [install promptfoo](https://www.promptfoo.dev/docs/installation/):

In the VSCode terminal:
```bash
npm install -g promptfoo
```

## Probably Optional: Git

To install git see [part two of the setup guide](./SETUP-OPTIONAL.md).

## Next Steps

**Proceed to Session 2:** Access our LLMs and run promptfoo demo

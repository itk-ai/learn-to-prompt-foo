# AGENTS.md - Context for AI Agents

This repo contains training materials for teaching non-technical users promptfoo. Key context for agents:

## Repo Purpose
- Training documentation only - no executable code
- Target audience: Non-technical Windows users learning promptfoo
- All content is instructional (guides, templates)
- **Published as Jekyll site on GitHub Pages** from `docs/` folder

## Site Structure

### Jekyll Site (GitHub Pages)
- **Source:** `docs/` folder
- **Theme:** Just the Docs (documentation with sidebar navigation and search)
- **Build:** GitHub Actions workflow (`.github/workflows/deploy.yml`)
- **Triggers:** Push to `main` branch with changes to `docs/`

### Document Organization
```
docs/
├── setup/              # Phase 1: Setup & Basics
│   ├── SETUP.md        # Session 1 (FINAL - DO NOT MODIFY)
│   ├── GETTING-STARTED.md  # Session 2 (FINAL - DO NOT MODIFY)
│   └── SETUP-OPTIONAL.md   # Optional Git setup
├── evaluations/        # Phase 2: Promptfoo Evaluations
│   ├── PROMPTFOO-EVALUATIONS.md  # Session 3 (FINAL - DO NOT MODIFY)
│   ├── ASSERTIONS-REFERENCE.md   # Session 3 reference (FINAL - DO NOT MODIFY)
│   └── BIAS-CHECKER.md           # Session 4 (TO BE CREATED)
├── git/                # Phase 3: Collaboration (Optional)
│   └── GIT-WORKFLOW.md
├── cheat-sheets/       # Reference Materials
│   ├── QUICK-REFERENCE.md
│   ├── YAML-CHEATSHEET.md
│   └── STARTER-TEMPLATE.md
└── material/          # Downloadable files for sessions
    ├── short-mbu-databeskyttelses-eval-config.yaml
    ├── owui.js
    ├── essential_claims_assertion.py
    ├── ja_nej_assertion.py
    └── refusal_assertion.py
```

## Key Context
- Session guides already reviewed and approved: 
  - `SETUP.md` - MUST NOT BE ALTERED
  - `GETTING-STARTED.md` - MUST NOT BE ALTERED  
  - `PROMPTFOO-EVALUATIONS.md` - MUST NOT BE ALTERED
  - `ASSERTIONS-REFERENCE.md` - MUST NOT BE ALTERED
- Session guides to work on: See NEXT-STEPS.md
- All content in `docs/` folder (not root)

### Training Structure
- 3 sessions (plus optional Git sessions)
- Total 15-20 hours including homework
- In-person workshops + self-study

Content Strategy:
- All guides should be short and to the point
- No "trainer instructions" like "watch for", "helpful hints", "success indicators", only instructions or explanations
- Focus on what the trainee needs to do
- Use actual examples from MBU config

### Content Sources
- `docs/cheat-sheets/STARTER-TEMPLATE.md` - Canonical template for new configs
- `docs/evaluations/PROMPTFOO-EVALUATIONS.md` - MBU example patterns
- `docs/material/` - Downloadable files (custom provider, assertions, shortened configs)
- All YAML examples use 2-space indentation (critical for trainees)

### Agent Guidance
- When helping with training content: Reference `docs/evaluations/PROMPTFOO-EVALUATIONS.md` for MBU-specific patterns
- When suggesting templates: Use `docs/cheat-sheets/STARTER-TEMPLATE.md` as base
- When troubleshooting: Check `docs/cheat-sheets/QUICK-REFERENCE.md` first
- When tracking progress: Use `NEXT-STEPS.md` (in root, not docs/)
- **All file paths in docs/ folder** (e.g., `docs/setup/SETUP.md`, not `SETUP.md`)
- **Downloadable files go in** `docs/material/` (e.g., custom providers, assertion scripts, shortened configs)

### Important Notes
- This is NOT a promptfoo project - it's training materials ABOUT promptfoo
- No actual promptfoo configs here (except templates/examples)
- Trainees use these materials to learn, then work in prompfoo-docker repo
- All paths in examples are relative to prompfoo-docker (e.g., `file:///app/providers/owui.js`)
- **Jekyll site requirements:**
  - All markdown files need YAML front matter (title, parent, nav_order)
  - Changes to `docs/` auto-deploy via GitHub Actions
  - Test locally with `bundle exec jekyll serve` (in docs/ folder)

## Commands & Shortcuts (Documented in materials)
- VSCode terminal: `` Ctrl + ` ``
- Format YAML: `Shift+Alt+F`
- Source Control: `Ctrl+Shift+G`
- Save: `Ctrl+S`
- Jekyll local preview: `cd docs && bundle exec jekyll serve`

## What Agents Should NOT Do
- Do not suggest adding executable code here
- Do not modify EXAMPLES.md patterns without checking prompfoo-docker source
- Do not create new training sessions without consulting README.md
- Do not suggest Windows-specific solutions (materials assume Windows throughout)
- Do not place content in root folder - all training content goes in `docs/`
- Do NOT modify approved session guides: `SETUP.md`, `GETTING-STARTED.md`, `PROMPTFOO-EVALUATIONS.md`, `ASSERTIONS-REFERENCE.md`

## References
- Source examples: `/home/akda/git_repos/prompfoo-docker/eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml`
- Promptfoo docs: https://www.promptfoo.dev/docs/
- Training site: https://itk-ai.github.io/learn-to-prompt-foo/
- Training target: Non-technical users (emphasize simplicity, step-by-step)

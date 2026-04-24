# AGENTS.md - Context for AI Agents

This repo contains training materials for teaching non-technical users promptfoo. Key context for agents:

## Repo Purpose
- Training documentation only - no executable code
- Target audience: Non-technical Windows users learning promptfoo
- All content is instructional (guides, templates)

## Key Context
- The session guides
- Session guides already reviewed and approved SETUP.md, GETTING-STARTED.md. MUST NOT BE ALTERED.
- Session guides to work on see NEXT-STEPS.md 

### Training Structure
- 3 sessions
- Total 15-20 hours including homework
- In-person workshops + self-study

Content Strategy:
- All guides should be short and to the point
- No "trainer instructions" like "watch for", "helpful hints", "success indicators", only instructions or explanations
- Focus on what the trainee needs to do
- Use actual examples from MBU config

### Content Sources
- EXAMPLES.md contains real patterns from `/home/akda/git_repos/prompfoo-docker/eval-configs/MBU-Databeskyttelse/`
- STARTER-TEMPLATE.md is the canonical template for new configs
- All YAML examples use 2-space indentation (critical for trainees)

### Agent Guidance
- When helping with training content: Reference EXAMPLES.md for MBU-specific patterns
- When suggesting templates: Use STARTER-TEMPLATE.md as base
- When troubleshooting: Check QUICK-REFERENCE.md first
- When tracking progress agent progress: Use NEXT-STEPS.md

### Important Notes
- This is NOT a promptfoo project - it's training materials ABOUT promptfoo
- No actual promptfoo configs here (except templates/examples)
- Trainees use these materials to learn, then work in prompfoo-docker repo
- All paths in examples are relative to prompfoo-docker (e.g., `file:///app/providers/owui.js`)

## Commands & Shortcuts (Documented in materials)
- VSCode terminal: `` Ctrl + ` ``
- Format YAML: `Shift+Alt+F`
- Source Control: `Ctrl+Shift+G`
- Save: `Ctrl+S`

## What Agents Should NOT Do
- Do not suggest adding executable code here
- Do not modify EXAMPLES.md patterns without checking prompfoo-docker source
- Do not create new training sessions without consulting README.md
- Do not suggest Windows-specific solutions (materials assume Windows throughout)

## References
- Source examples: `/home/akda/git_repos/prompfoo-docker/eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml`
- Promptfoo docs: https://www.promptfoo.dev/docs/
- Training target: Non-technical users (emphasize simplicity, step-by-step)

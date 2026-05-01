---
title: "Quick Reference"
parent: "Cheat Sheets & Templates"
nav_order: 1
---
<!-- OPenCode draft -->

# Quick Reference Card

{: .warning }
> This is an Opencode draft

Print this or keep it open while working!

## VSCode Shortcuts

| Action | Shortcut |
|--------|----------|
| Open Terminal | `` Ctrl + ` `` |
| Save File | `Ctrl+S` |
| Format Document | `Shift+Alt+F` |
| Find | `Ctrl+F` |
| Source Control | `Ctrl+Shift+G` |
| Command Palette | `Ctrl+Shift+P` |

## YAML Syntax

```yaml
# Key-value
key: value

# List
items:
  - item1
  - item2

# Nested
parent:
  child: value

# Multiline
text: |
  line 1
  line 2

# Comments
# This is a comment
```

## Promptfoo Config Template

{% raw %}
```yaml
description: "My evaluation"

prompts:
  - "{{question}}"

providers:
  - id: file:///app/providers/owui.js
    config:
      apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
      model: "databeskyttelse-mbu"
      outputSources: true

defaultTest:
  options:
    provider: file:///app/providers/owui.js

tests:
  - vars:
      question: "Test question"
    assert:
      - type: contains
        value: "expected"
    metadata:
      category: "test"
```
{% endraw %}

## Common Assertions

```yaml
# Contains text
- type: contains
  value: "text"

# Case-insensitive
- type: icontains
  value: "text"

# Any of these
- type: contains-any
  value:
    - "option1"
    - "option2"

# All of these
- type: contains-all
  value:
    - "required1"
    - "required2"

# Regex pattern
- type: regex
  value: '.*pattern.*'

# LLM judge
- type: llm-rubric
  value: "Quality description"

# Reference template
- $ref: "#/assertionTemplates/name"
```

## Promptfoo Commands

```bash
# Run evaluation
promptfoo eval --config config.yaml

# View results
promptfoo view

# Check version
promptfoo --version
```

## Troubleshooting Checklist

- [ ] YAML indentation (2 spaces)
- [ ] No tabs, only spaces
- [ ] All keys have colons
- [ ] Quotes around special chars
- [ ] File paths are correct
- [ ] Environment variables set
- [ ] Terminal in project folder

## File Structure

```
project/
├── promptfooconfig.yaml
├── .env
├── eval-configs/
│   └── my-use-case/
│       └── promptfooconfig.yaml
├── providers/
│   └── owui.js
├── assertions/
│   └── custom.py
└── tests/
    └── test-cases.yaml
```

## Common Mistakes

❌ Using tabs → ✅ Use spaces
❌ Missing colons → ✅ Add colons
❌ Wrong indentation → ✅ 2 spaces per level
❌ No quotes on regex → ✅ Quote regex patterns
❌ Wrong file paths → ✅ Use file:// prefix

## Support

- **Instructor:** [Your Name]
- **Email:** [Your Email]
- **Docs:** See training materials
- **Promptfoo Docs:** https://www.promptfoo.dev/docs/

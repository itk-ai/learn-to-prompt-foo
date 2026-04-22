# YAML Cheat Sheet

YAML is a simple format for configuration files. It uses indentation instead of brackets.

## Basic Rules

1. **Use spaces, NOT tabs** - VSCode will help you with this
2. **Indentation matters** - Use 2 spaces per level
3. **Case sensitive** - `key` and `Key` are different
4. **Comments start with #** - Everything after # is ignored

## Basic Syntax

### Key-Value Pairs
```yaml
name: John Doe
age: 30
city: Aarhus
```

### Lists (Arrays)
```yaml
# Using dashes
fruits:
  - apple
  - banana
  - orange

# Or inline with brackets
colors: [red, green, blue]
```

### Nested Objects
```yaml
person:
  name: John Doe
  address:
    street: Main Street
    city: Aarhus
    country: Denmark
```

### Multiline Strings
```yaml
# Using | (preserves line breaks)
description: |
  This is a multiline
  string that keeps
  its formatting

# Using > (folds into single line)
summary: >
  This will become
  a single line
  with spaces

# Using quotes for special characters
message: "Hello\nNew line"
special: 'Contains: colon and "quotes"'
```

## Common Patterns in promptfoo

### Test Cases
```yaml
tests:
  - vars:
      question: "What is 2+2?"
    assert:
      - type: contains
        value: "4"
```

### Multiple Assertions
```yaml
tests:
  - vars:
      question: "Explain photosynthesis"
    assert:
      - type: llm-rubric
        value: "Explains the process accurately"
      - type: contains
        value: "sunlight"
      - type: icontains
        value: "chlorophyll"
```

### Using References (Reusable Templates)
```yaml
assertionTemplates:
  containsParis:
    type: contains
    value: "Paris"

tests:
  - vars:
      question: "What is the capital of France?"
    assert:
      - $ref: "#/assertionTemplates/containsParis"
```

### Default Test Configuration
```yaml
defaultTest:
  options:
    provider: file:///app/providers/owui.js
  assert:
    - type: contains
      value: "databeskyttelse@mbu.aarhus.dk"

tests:
  - vars:
      question: "Question 1"
    # Inherits defaultTest settings
  - vars:
      question: "Question 2"
    assert:
      # Override defaults for this test
      - type: contains
        value: "specific text"
```

## Common Mistakes

### ❌ Wrong: Using tabs
```yaml
tests:
	- vars:  # TAB character here - WRONG!
      question: "Test"
```

### ✅ Correct: Using spaces
```yaml
tests:
  - vars:  # 2 spaces here - CORRECT!
      question: "Test"
```

### ❌ Wrong: Inconsistent indentation
```yaml
tests:
  - vars:
    question: "Test"  # Only 4 spaces, should be 6
```

### ✅ Correct: Consistent indentation
```yaml
tests:
  - vars:
      question: "Test"  # 6 spaces (3 levels × 2 spaces)
```

### ❌ Wrong: Missing colon
```yaml
tests
  - vars:
      question: "Test"
```

### ✅ Correct: Has colon
```yaml
tests:
  - vars:
      question: "Test"
```

### ❌ Wrong: Wrong list indentation
```yaml
tests:
- vars:  # Should be indented
    question: "Test"
```

### ✅ Correct: Proper list indentation
```yaml
tests:
  - vars:  # Indented with 2 spaces
      question: "Test"
```

## Special Characters

### Quotes
```yaml
# Use quotes for strings with special characters
email: "user@example.com"
path: "C:\Users\Name"
regex: ".*contact.*databeskyttelse.*"

# Single quotes for strings with double quotes
quote: 'He said "Hello"'

# Double quotes for strings with single quotes
contraction: "It's a test"
```

### Colons in values
```yaml
# Use quotes if value contains colon
time: "10:30 AM"
url: "https://example.com"

# Or add space after colon in key
description: This has: a colon in the value
```

### Pipes and special symbols
```yaml
# Use quotes for special characters
regex: "^[A-Z].*"
pattern: ".*@.*\..*"
```

## VSCode Tips

### Auto-formatting
1. Right-click in the editor
2. Select **Format Document**
3. Or press `Shift+Alt+F`

### Validation
- Red squiggly lines = errors
- Yellow squiggly lines = warnings
- Hover over squiggly to see the message

### Schema Help
If YAML schema is configured:
- Press `Ctrl+Space` for autocomplete
- See available options as you type

### Check Indentation
1. Look at the bottom right of VSCode window
2. Should say "Spaces: 2" (not "Tabs")
3. If it says "Tabs", click and change to "Spaces: 2"

## Quick Reference

| Symbol | Meaning | Example |
|--------|---------|---------|
| `:` | Key-value separator | `name: value` |
| `-` | List item | `- item` |
| `#` | Comment | `# This is a comment` |
| `|` | Multiline literal | `text: |\n  line1\n  line2` |
| `>` | Multiline folded | `text: >\n  line1\n  line2` |
| `[]` | Inline list | `items: [a, b, c]` |
| `{}` | Inline object | `person: {name: John, age: 30}` |
| `$ref` | Reference | `$ref: "#/templates/myTemplate"` |

## Practice Examples

### Example 1: Simple Test
```yaml
tests:
  - vars:
      question: "What is the capital of Denmark?"
    assert:
      - type: contains
        value: "Copenhagen"
```

### Example 2: Multiple Tests
```yaml
tests:
  - vars:
      question: "Question 1"
    assert:
      - type: contains
        value: "Answer 1"
  - vars:
      question: "Question 2"
    assert:
      - type: contains
        value: "Answer 2"
```

### Example 3: Complex Config
```yaml
description: "My evaluation"

prompts:
  - "{{question}}"

providers:
  - id: file:///app/providers/owui.js
    config:
      model: "databeskyttelse-mbu"

defaultTest:
  options:
    provider: file:///app/providers/owui.js

tests:
  - vars:
      question: "Test question"
    assert:
      - type: llm-rubric
        value: "Provides accurate answer"
    metadata:
      category: "test"
      priority: "high"
```

## Need Help?

When you see errors in VSCode:
1. Hover over the red/yellow underline
2. Read the error message
3. Check indentation
4. Look for missing colons or quotes
5. Ask your instructor if stuck

---

**Remember:** YAML is forgiving with simple cases but strict with indentation. When in doubt, use VSCode's formatting tool!

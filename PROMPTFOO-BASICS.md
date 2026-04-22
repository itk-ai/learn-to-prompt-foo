# Promptfoo Basics

Introduction to promptfoo concepts and configuration.

## What is Promptfoo?

Promptfoo is a tool for testing and evaluating LLM (Large Language Model) responses. It helps you:

- **Test** if your AI gives correct answers
- **Compare** different models
- **Catch** problems before deployment
- **Monitor** quality over time

## How It Works

```
┌─────────────────────────────────────────────────────────┐
│  1. You write a config file with:                       │
│     - Questions to ask                                  │
│     - Expected answers/assertions                       │
│                                                         │
│  2. Promptfoo runs:                                     │
│     - Sends questions to the LLM                        │
│     - Gets responses                                    │
│     - Checks if assertions pass                         │
│                                                         │
│  3. Results show:                                       │
│     - Which tests passed/failed                         │
│     - Actual LLM responses                              │
│     - Scores and metrics                                │
└─────────────────────────────────────────────────────────┘
```

## Config File Structure

A promptfoo config file (`promptfooconfig.yaml`) has these sections:

### 1. Description
```yaml
description: "MBU Databeskyttelse Assistant Evaluation"
```

What this evaluation tests.

### 2. Prompts
```yaml
prompts:
  - "{{question}}"
```

The prompt template(s) sent to the LLM. Variables use `{{variable}}` syntax.

### 3. Providers
```yaml
providers:
  - id: file:///app/providers/owui.js
    config:
      model: "databeskyttelse-mbu"
```

Which LLM(s) to test. Can test multiple models at once.

### 4. Default Test
```yaml
defaultTest:
  options:
    provider: file:///app/providers/owui.js
  assert:
    - type: contains
      value: "databeskyttelse@mbu.aarhus.dk"
```

Settings that apply to ALL tests. Great for reusability.

### 5. Tests
```yaml
tests:
  - vars:
      question: "What is 2+2?"
    assert:
      - type: contains
        value: "4"
```

Individual test cases with questions and expected outcomes.

### 6. Assertion Templates (Optional)
```yaml
assertionTemplates:
  containsParis:
    type: contains
    value: "Paris"
```

Reusable assertion patterns. Reference with `$ref`.

## Key Concepts

### Variables
Placeholders that get replaced with actual values:

```yaml
prompts:
  - "Answer this: {{question}}"

tests:
  - vars:
      question: "What is the capital?"
```

Result: LLM receives "Answer this: What is the capital?"

### Assertions
Rules that check if the response is correct:

```yaml
assert:
  - type: contains
    value: "Copenhagen"
```

The LLM response must contain "Copenhagen" to pass.

### Transforms
Modify output before checking:

```yaml
assert:
  - type: contains
    value: "FAQ.md"
    transform: "output.sources.map(o => o.reference).join(' ')"
```

Extract document references from RAG sources.

## Common Assertion Types

### String Matching

#### `contains` / `icontains`
Check if response contains specific text
```yaml
- type: contains  # case-sensitive
  value: "expected text"
- type: icontains  # case-insensitive
  value: "expected text"
```

#### `contains-any` / `contains-all`
Check for multiple possible values
```yaml
- type: contains-any
  value:
    - "option 1"
    - "option 2"
- type: contains-all
  value:
    - "required 1"
    - "required 2"
```

#### `regex`
Pattern matching
```yaml
- type: regex
  value: '.*databeskyttelse@.*\.aarhus\.dk.*'
```

#### `equals` / `iequals`
Exact match
```yaml
- type: equals
  value: "Exactly this text"
```

### LLM-Based

#### `llm-rubric`
Use another LLM to judge quality
```yaml
- type: llm-rubric
  value: "Explains GDPR requirements accurately"
```

Good for subjective quality checks.

#### `classifier`
Use ML classifier
```yaml
- type: classifier
  provider: huggingface:text-classification:model-name
  value: "positive"
  threshold: 0.8
```

### Custom

#### `javascript`
Run custom JavaScript
```yaml
- type: javascript
  value: "output.length < 500"
```

#### `python`
Run custom Python script
```yaml
- type: python
  value: file:///app/assertions/custom_assertion.py
  config:
    param1: "value"
```

### Special

#### `assert-set`
Group multiple assertions
```yaml
- type: assert-set
  threshold: 0.5  # 50% must pass
  assert:
    - type: contains
      value: "option 1"
    - type: contains
      value: "option 2"
```

## Test Case Structure

### Basic Test
```yaml
- vars:
    question: "Simple question"
  assert:
    - type: contains
      value: "expected answer"
```

### Test with Metadata
```yaml
- vars:
    question: "Complex question"
  assert:
    - type: llm-rubric
      value: "Accurate explanation"
  metadata:
    category: "gdpr"
    difficulty: "hard"
    origin: "real"
```

### Test with Description
```yaml
- description: "Test that refusal works for sensitive topics"
  vars:
    question: "How do I hack into..."
  assert:
    - type: regex
      value: '.*kontakt.*databeskyttelse.*'
```

## Running Evaluations

### Command Line
```bash
# Run specific config
promptfoo eval --config eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml

# Run multiple configs
promptfoo eval --config configs/*

# View results in browser
promptfoo view
```

### In VSCode Terminal
```bash
cd /path/to/project
promptfoo eval --config eval-configs/my-config.yaml
```

### Results
Results open automatically in your browser at:
```
http://localhost:8000
```

## Understanding Results

### Score View
```
┌──────────────────────────────────────────┐
│ Test                                    │
│ ───────────────────────────────────────  │
│ Question 1:  ✓ PASS (0.95)              │
│ Question 2:  ✗ FAIL (0.45)              │
│ Question 3:  ✓ PASS (0.88)              │
│                                         │
│ Overall: 2/3 pass (67%)                 │
└──────────────────────────────────────────┘
```

### Individual Test View
```
Question: "What is the capital?"
Expected: Contains "Copenhagen"
Actual: "The capital is Copenhagen"
Result: ✓ PASS

Sources:
- Document1.md: "Copenhagen is..."
- Document2.md: "Capital city..."
```

### Metrics
- **Pass/Fail**: Did assertions pass?
- **Score**: 0-1 score (1 = perfect)
- **Latency**: How fast was response?
- **Token usage**: How many tokens used?

## Common Patterns

### Pattern 1: Simple Containment
```yaml
tests:
  - vars:
      question: "When can we send class lists?"
    assert:
      - type: icontains
        value: "31. jul"
```

### Pattern 2: Refusal Detection
```yaml
assertionTemplates:
  refuseToAnswer:
    type: regex
    value: '.*kontakt.*databeskyttelse@.*'

tests:
  - vars:
      question: "How do I hack..."
    assert:
      - $ref: "#/assertionTemplates/refuseToAnswer"
```

### Pattern 3: Document Retrieval
```yaml
tests:
  - vars:
      question: "About Aula access"
    assert:
      - type: icontains
        value: "FAQ om databeskyttelse.md"
        transform: "output.sources.map(o => o.reference).join(' ')"
```

### Pattern 4: Content Retrieval
```yaml
tests:
  - vars:
      question: "About Aula access"
    assert:
      - type: icontains-any
        value:
          - "first August"
          - "after July 31"
        transform: "output.sources.map(o => o.content).join('\\n')"
```

### Pattern 5: Quality Assessment
```yaml
tests:
  - vars:
      question: "Explain GDPR"
    assert:
      - type: llm-rubric
        value: |
          Explains key GDPR principles:
          - Data minimization
          - Purpose limitation
          - Storage limitation
```

### Pattern 6: Multiple Requirements
```yaml
tests:
  - vars:
      question: "Can we use Google Meet?"
    assert:
      - type: icontains
        value: "Google Meet"
      - type: icontains
        value: "allowed"
      - type: icontains
        value: "no recording"
```

## Best Practices

### 1. One Thing Per Test
```yaml
# ✅ Good: Test one specific thing
- vars:
    question: "When is access allowed?"
  assert:
    - type: icontains
      value: "August"

# ❌ Bad: Testing too many things
- vars:
    question: "Tell me everything about access"
  assert:
    - type: contains
      value: "August"
    - type: contains
      value: "July"
    - type: llm-rubric
      value: "Comprehensive answer"
```

### 2. Clear Assertions
```yaml
# ✅ Good: Specific and clear
- type: icontains
  value: "31. juli"

# ❌ Bad: Vague
- type: llm-rubric
  value: "Good answer"
```

### 3. Use Templates
```yaml
# ✅ Good: Reusable
assertionTemplates:
  contactEmail:
    type: regex
    value: '.*databeskyttelse@mbu\.aarhus\.dk.*'

tests:
  - vars:
      question: "Who to contact?"
    assert:
      - $ref: "#/assertionTemplates/contactEmail"
```

### 4. Add Metadata
```yaml
tests:
  - vars:
      question: "..."
    metadata:
      category: "gdpr"
      difficulty: "medium"
      origin: "real"  # or "synthetic"
```

### 5. Use defaultTest
```yaml
# ✅ Good: Common settings once
defaultTest:
  options:
    provider: file:///app/providers/owui.js
  assert:
    - type: contains
      value: "databeskyttelse@mbu.aarhus.dk"

tests:
  - vars:
      question: "Question 1"
    # Inherits defaultTest
  - vars:
      question: "Question 2"
    # Inherits defaultTest
```

## Troubleshooting

### Common Issues

#### YAML Errors
```
Error: Invalid YAML
```
**Fix:** Check indentation, use spaces not tabs

#### Missing Variables
```
Error: Variable 'question' not found
```
**Fix:** Add `vars.question` to test case

#### Provider Errors
```
Error: Provider connection failed
```
**Fix:** Check environment variables, network

#### Assertion Failures
```
Test failed: contains assertion
```
**Fix:** Check expected value matches actual response

### Debug Tips

1. **Use --verbose**
   ```bash
   promptfoo eval --verbose
   ```

2. **Check YAML validation**
   - Look for red underlines in VSCode

3. **View actual response**
   - Check results browser view

4. **Test one config at a time**
   ```bash
   promptfoo eval --config single-config.yaml
   ```

## Next Steps

After learning basics:
1. ✅ Understand config structure
2. ✅ Know common assertion types
3. ✅ Can run evaluations
4. ✅ Can interpret results
5. ✅ Ready to create tests

**Ready to practice?** Move to [Training Agenda](./TRAINING-AGENDA.md)

---

**Need Help?** Ask your instructor for clarification.

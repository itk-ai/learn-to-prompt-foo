# Starter Template

Copy this template to start your first evaluation config.

## Basic Template

Save as `promptfooconfig.yaml`:

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: "My first evaluation - [DESCRIBE WHAT YOU'RE TESTING]"

# The prompt template - {{question}} will be replaced with actual questions
prompts:
  - "{{question}}"

# The LLM(s) to test
providers:
  - id: file:///app/providers/owui.js
    label: "DEV - [MODEL NAME]"
    config:
      apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
      model: "[MODEL-NAME]"
      outputSources: true

# Settings that apply to ALL tests
defaultTest:
  options:
    # Provider for assertions (LLM-as-judge)
    provider:
      id: file:///app/providers/owui.js
      config:
        apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
        apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
        model: "AarhusAI-default"
    
    # Python environment for custom assertions
    config:
      pythonExecutable: .venv/bin/python

# Reusable assertion templates
assertionTemplates:
  # Example: Check for contact email
  contactEmail:
    type: regex
    value: '.*databeskyttelse@mbu\.aarhus\.dk.*'
    transform: "output.text"
  
  # Example: Check for refusal
  refuseToAnswer:
    type: regex
    value: '.*kontakt(?:er|e)?\s+databeskyttelse@mbu\.aarhus\.dk.*'
    transform: "output.text"
    metric: refusal

# Your test cases
tests:
  # Test 1: Simple containment
  - description: "[DESCRIBE WHAT THIS TEST CHECKS]"
    vars:
      question: "[YOUR QUESTION HERE]"
    assert:
      - type: contains
        value: "[EXPECTED TEXT]"
    metadata:
      category: "[CATEGORY]"
      origin: "[real|synthetic]"

  # Test 2: Multiple acceptable answers
  - description: "Test answer contains correct date"
    vars:
      question: "[YOUR QUESTION HERE]"
    assert:
      - type: icontains-any
        value:
          - "option 1"
          - "option 2"
        metric: answer
    metadata:
      category: "answer"
      origin: "synthetic"

  # Test 3: Document retrieval check
  - description: "Verify correct document retrieved"
    vars:
      question: "[YOUR QUESTION HERE]"
    assert:
      - type: icontains
        value: "[DOCUMENT-NAME.md]"
        transform: 'output.sources.map(o => o.reference).join(" ")'
        metric: docRetrival
    metadata:
      category: "docRetrieval"
      origin: "real"

  # Test 4: Content retrieval check
  - description: "Verify correct content retrieved"
    vars:
      question: "[YOUR QUESTION HERE]"
    assert:
      - type: icontains-any
        value:
          - "key phrase 1"
          - "key phrase 2"
        transform: 'output.sources.map(o => o.content).join("\n\n")'
        metric: contentRetrieval
    metadata:
      category: "contentRetrieval"
      origin: "real"

  # Test 5: Refusal check (use template)
  - description: "Test that inappropriate question is refused"
    vars:
      question: "[YOUR QUESTION HERE]"
    assert:
      - $ref: "#/assertionTemplates/refuseToAnswer"
    metadata:
      category: "refusal"
      origin: "synthetic"
      refusal: yes

  # Test 6: LLM rubric (quality check)
  - description: "Test answer quality"
    vars:
      question: "[YOUR QUESTION HERE]"
    assert:
      - type: llm-rubric
        value: |
          [WRITE YOUR IDEAL ANSWER OR QUALITY CRITERIA HERE]
          This should be detailed and specific.
        transform: "output.text"
        weight: 0.1
        metric: answer
    metadata:
      category: "answer"
      origin: "real"

  # Test 7: Using custom Python assertion
  - description: "Test with custom assertion"
    vars:
      question: "[YOUR QUESTION HERE]"
    assert:
      - type: python
        value: file:///app/assertions/ja_nej_assertion.py
        transform: "output.text"
        config:
          expectedAnswerCategory: Bekræftende
        metric: answer
    metadata:
      category: "answer"
      origin: "synthetic"
```

## Running Your First Eval

1. Save the file as `promptfooconfig.yaml`
2. Open terminal in VSCode
3. Navigate to your config directory:
   ```bash
   cd eval-configs/my-use-case
   ```
4. Run the evaluation:
   ```bash
   promptfoo eval --config promptfooconfig.yaml
   ```
5. Results will open in your browser

## Customization Checklist

Before running, make sure to update:

- [ ] `description:` - What you're testing
- [ ] `providers:` - Your model configuration
- [ ] `defaultTest.provider:` - Judge model
- [ ] `assertionTemplates:` - Your reusable patterns
- [ ] `tests:` - Your actual test cases
- [ ] All `[PLACEHOLDERS]` replaced with real values

## Common Assertion Types Quick Reference

```yaml
# Contains (case-sensitive)
- type: contains
  value: "exact text"

# Contains (case-insensitive)
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

# LLM quality check
- type: llm-rubric
  value: "Quality description"

# Reference template
- $ref: "#/assertionTemplates/name"

# Custom Python
- type: python
  value: file:///app/assertions/script.py
  config:
    param: "value"
```

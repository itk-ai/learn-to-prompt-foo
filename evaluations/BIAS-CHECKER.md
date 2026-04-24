---
title: "Session 4: Bias Checker"
parent: "Phase 2: Promptfoo Evaluations"
nav_order: 2
---

<!-- Opencode's draft --> 

# Session 4: Creating Tests for Bias Checker

> [!WARN]
> This is a draft by OpenCode

**Goal:** Create promptfoo tests for Anne Vibekes Bias-checker

---

## What is the Bias Checker?

The Bias-checker is an LLM assistant that helps identify and analyze bias in text content. It's designed to:

- Detect various types of bias in written content
- Provide explanations for identified biases
- Suggest alternatives for more neutral language

**Model Info:** Available at https://stgai.itkdev.dk/api/v1/models/model?id=biastjekker1-2025

---

## Part 1: Understanding What to Test

When creating tests for the Bias-checker, we want to evaluate:

1. **Detection Accuracy** - Does it correctly identify bias?
2. **Explanation Quality** - Are the explanations clear and helpful?
3. **Actionable Suggestions** - Does it provide useful alternatives?
4. **Edge Cases** - How does it handle ambiguous or subtle bias?

---

## Part 2: Creating the Config

Using the [STARTER-TEMPLATE](../cheat-sheets/STARTER-TEMPLATE.md), create a new config file:

```yaml
# bias-checker-config.yaml
description: "Bias Checker Evaluation"

prompts:
  - |
    Analyze the following text for bias and provide:
    1. Types of bias detected
    2. Explanation of why it's biased
    3. Suggested neutral alternatives
    
    Text: {{text}}

providers:
  - id: http://stgai.itkdev.dk/v1/chat/completions
    config:
      model: biastjekker1-2025
      temperature: 0.7
      max_tokens: 1000

defaultTest:
  options:
    provider:
      id: http://stgai.itkdev.dk/v1/chat/completions
      config:
        model: biastjekker1-2025

tests:
  # Test 1: Gender bias detection
  - vars:
      text: "The nurse took care of the patients while the doctor gave orders."
    assert:
      - type: contains
        value: "gender"
      - type: contains
        value: "nurse"
      - type: contains
        value: "doctor"

  # Test 2: Professional bias detection
  - vars:
      text: "The female engineer struggled with the technical problem."
    assert:
      - type: contains
        value: "gender"
      - type: contains
        value: "engineer"

  # Test 3: Cultural bias detection
  - vars:
      text: "Following Western business practices is the most professional approach."
    assert:
      - type: contains
        value: "cultural"
      - type: contains
        value: "Western"

  # Test 4: Age bias detection
  - vars:
      text: "The elderly employee struggled to adapt to new technology."
    assert:
      - type: contains
        value: "age"
      - type: contains
        value: "elderly"

assertionTemplates:
  - type: contains
    value: "bias"
  - type: contains
    value: "suggest"
  - type: contains
    value: "alternative"
```

---

## Part 3: Running the Evaluation

1. **Navigate to your config folder:**
   ```bash
   cd ~/projects/bias-checker-tests
   ```

2. **Run the evaluation:**
   ```bash
   npx promptfoo eval -c bias-checker-config.yaml
   ```

3. **View results:**
   ```bash
   npx promptfoo view
   ```

---

## Part 4: Interpreting Results

When reviewing the results, look for:

✅ **Passing tests** - The model correctly identified bias and provided explanations  
⚠️ **Partial matches** - Model detected bias but explanation may be weak  
❌ **Failing tests** - Model missed the bias or provided incorrect analysis

### Key Metrics to Check:

1. **Pass rate** - What percentage of bias cases were correctly identified?
2. **Explanation quality** - Are the explanations specific and accurate?
3. **Suggestion relevance** - Do the alternatives address the identified bias?

---

## Part 5: Designing Your Own Tests

Now it's your turn to create test cases:

### Exercise: Create 3 New Test Cases

Think about different types of bias you want to test:

1. **Political bias** - Text with political assumptions
2. **Socioeconomic bias** - Text assuming certain economic status
3. **Education bias** - Text assuming certain education level

For each test case:
- Write the input text (in `vars.text`)
- Define what the model should detect (in `assert`)
- Run the evaluation and check results

---

## Next Steps

After completing this session, you should be able to:

- ✅ Understand what the Bias-checker does
- ✅ Create promptfoo configs for new use cases
- ✅ Design test cases with appropriate assertions
- ✅ Run evaluations and interpret results

**Ready to contribute?** See [Git Workflow](../git/GIT-WORKFLOW.md) to share your bias checker tests with the team.

---

## Resources

- [Bias Checker Model Info](https://stgai.itkdev.dk/api/v1/models/model?id=biastjekker1-2025)
- [Starter Template](../cheat-sheets/STARTER-TEMPLATE.md)
- [Quick Reference](../cheat-sheets/QUICK-REFERENCE.md)

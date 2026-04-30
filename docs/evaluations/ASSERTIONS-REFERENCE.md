---
title: "Reference: Assertion Types"
parent: "Phase 2: Promptfoo Evaluations"
nav_order: 3
---

{: .warning }
> This document is an OpenCode AI draft and have not been reviewed yet

# Assertion Types Reference

Quick reference for all assertion types available in promptfoo.

---

## Built-in Assertions

### String Matching

| Assertion | Case Sensitive | Use When | Example |
|-----------|---------------|----------|---------|
| `contains` | Yes | Exact substring required | `value: "exact phrase"` |
| `icontains` | No | Case doesn't matter | `value: "phrase"` |
| `contains-any` | Yes | One of several options | `value: ["opt1", "opt2"]` |
| `icontains-any` | No | Case-insensitive, one of several | `value: ["opt1", "opt2"]` |
| `contains-all` | Yes | All required | `value: ["req1", "req2"]` |
| `icontains-all` | No | All required, case-insensitive | `value: ["req1", "req2"]` |
| `starts-with` | Yes | Text must begin with | `value: "Yes,"` |
| `ends-with` | Yes | Text must end with | `value: "."` |

### Pattern Matching

| Assertion | Use When | Example |
|-----------|----------|---------|
| `regex` | Pattern matching | `value: '.*email@domain.*'` |
| `is-json` | Output should be JSON | (no value needed) |
| `is-valid-json` | Valid JSON structure | (no value needed) |

### Counting

| Assertion | Use When | Example |
|-----------|----------|---------|
| `word-count` | Specific word count | `value: 50` |
| `line-count` | Specific line count | `value: 10` |
| `character-count` | Specific character count | `value: 500` |

### Classification

| Assertion | Use When | Example |
|-----------|----------|---------|
| `is-refusal` | Check if model refuses | (no value needed) |

---

## Model-Graded Assertions

### LLM Rubric

**Type:** `llm-rubric`

**Use when:** You want to compare the answer to an ideal response using an LLM as judge.

```yaml
- type: llm-rubric
  value: |-
    Ja det er tilladt at anvende Google Meet til fjernundervisning.
    Der må dog intet følsomt transmitteres.
  weight: 0.1
  metric: answer
```

**Configuration:**
- `value`: The ideal answer or evaluation criteria
- `weight`: Score weight (0-1, or adjust based on judge model scale)
- `metric`: Name of the metric for reporting

> [!NOTE]
> The `rubricPrompt` in `defaultTest` defines how the judge LLM evaluates. See [PROMPTFOO-EVALUATIONS.md](PROMPTFOO-EVALUATIONS.md#default-test) for details.

---

## Custom Python Assertions

Our setup includes three custom Python assertions that use LLM-as-judge internally.

### ja_nej_assertion.py

**Purpose:** Classify Danish answers as affirmative, neutral, or refusal.

**Score range:** -10 (clear refusal) to 10 (clear affirmation), 0 = neutral

**Configuration:**

| Option | Type | Values |
|--------|------|--------|
| `expectedAnswerCategory` | string | `"Bekræftende"`, `"Neutralt"`, `"Afvisende"` |

**Example:**

```yaml
# Expecting an affirmative answer
- type: python
  value: file:///app/assertions/ja_nej_assertion.py
  transform: "output.text"
  config:
    expectedAnswerCategory: Bekræftende
  metric: answer

# Expecting a refusal
- type: python
  value: file:///app/assertions/ja_nej_assertion.py
  transform: "output.text"
  config:
    expectedAnswerCategory: Afvisende
  metric: answer
```

**Categories:**
- **Bekræftende** (Affirmative): Clear positive answer, score 0-10
- **Neutralt** (Neutral): Neither affirming nor refusing, score around 0
- **Afvisende** (Refusing): Clear refusal or denial, score -10 to 0

---

### essential_claims_assertion.py

**Purpose:** Verify that the answer covers all required essential claims or information points.

**Configuration:**

| Option | Type | Required |
|--------|------|----------|
| `essentialClaims` | array | Yes |

**Example:**

```yaml
- type: python
  value: file:///app/assertions/essential_claims_assertion.py
  transform: "output.text"
  config:
    essentialClaims:
      - "Google Meet må udelukkende anvendes til undervisningsmæssig brug"
      - "Intet følsomt eller fortroligt må transmitteres via Google Meet"
      - "Det er tilladt at vise både ansatte og elever i klassen"
  metric: answer
```

**How it works:** The LLM evaluates whether the answer provides guidance consistent with expert-validated information without misleading the user.

---

### refusal_assertion.py

**Purpose:** Validate that when a model refuses to answer, it does so correctly by:
1. Including a reference to contact `databeskyttelse@mbu.aarhus.dk`
2. NOT providing ideas, suggestions, or misleading information
3. NOT directing users to find information elsewhere

**Configuration:** None required

**Example:**

```yaml
- type: python
  value: file:///app/assertions/refusal_assertion.py
  transform: "output.text"
  metric: refusal
```

**Best practice:** Combine with a regex assertion to ensure the contact email is present:

```yaml
assertionTemplates:
  refuseToAnswer:
    type: regex
    value: '.*kontakt(?:er|e)?\s+databeskyttelse@mbu\.aarhus\.dk.*'
    transform: "output.text"
    metric: refusal

tests:
  - vars:
      question: "Unknown question"
    assert:
      - $ref: "#/assertionTemplates/refuseToAnswer"
      - type: python
        value: file:///app/assertions/refusal_assertion.py
        transform: "output.text"
        metric: refusal
```

---

## Transform Property

The `transform` property processes the output before assertion checking.

### Common Transforms

| Transform | Use When | Example |
|-----------|----------|---------|
| `output.text` | Check the answer text | `- transform: "output.text"` |
| `output.sources.map(o => o.reference).join(" ")` | Check document titles | `- transform: 'output.sources.map(o => o.reference).join(" ")'` |
| `output.sources.map(o => o.content).join("\n\n")` | Check document content | `- transform: 'output.sources.map(o => o.content).join("\n\n")'` |

> [!NOTE]
> These transforms work when the provider has `outputSources: true`. With the HTTP provider from Session 2, you only had access to the text via `transformResponse`.

---

## Common Patterns

### Pattern 1: Simple Answer Check

```yaml
- type: icontains
  value: "expected phrase"
  transform: "output.text"
  metric: answer
```

### Pattern 2: Multiple Acceptable Answers

```yaml
- type: icontains-any
  value:
    - "option 1"
    - "option 2"
    - "option 3"
  transform: "output.text"
  metric: answer
```

### Pattern 3: Answer + Document Retrieval

```yaml
- type: icontains
  value: "key information"
  transform: "output.text"
  metric: answer
- type: icontains
  value: "Expected Document Title.md"
  transform: 'output.sources.map(o => o.reference).join(" ")'
  metric: docRetrival
```

### Pattern 4: Complete RAG Test

```yaml
- type: icontains-any
  value:
    - "key point 1"
    - "key point 2"
  transform: "output.text"
  metric: answer
- type: icontains
  value: "Expected Document.md"
  transform: 'output.sources.map(o => o.reference).join(" ")'
  metric: docRetrival
- type: icontains-all
  value:
    - "required content 1"
    - "required content 2"
  transform: 'output.sources.map(o => o.content).join("\n\n")'
  metric: contentRetrieval
```

### Pattern 5: Quality + Compliance

```yaml
- type: python
  value: file:///app/assertions/ja_nej_assertion.py
  transform: "output.text"
  config:
    expectedAnswerCategory: Bekræftende
  metric: answer
- type: llm-rubric
  value: |-
    Ideal answer with all required details...
  weight: 0.1
  metric: answer
```

---

## Additional Resources

- [Full Promptfoo Documentation](https://www.promptfoo.dev/docs/configuration/expected-outputs/)
- [Custom Assertions Details](../promptfoo-writers/assertions.md)
- [MBU Config Examples](../evaluations/PROMPTFOO-EVALUATIONS.md#part-3-test-examples-walkthrough)

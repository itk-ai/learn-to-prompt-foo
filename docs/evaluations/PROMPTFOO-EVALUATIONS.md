---
title: "Session 3: Promptfoo Evaluations"
parent: "Phase 2: Promptfoo Evaluations"
nav_order: 1
---

# Session 3: Understanding Promptfoo Evaluations

**Goal:** Explore a real evaluation config (MBU Databeskyttelse) and understand how to read, run, and modify it

---

## What We'll Do Today

1. ✅ Locate and open the MBU evaluation config
2. ✅ Understand the config structure and each section
3. ✅ Learn about the custom OWUI provider (vs. the HTTP provider from Session 2)
4. ✅ Walk through different test patterns and assertion types
5. ✅ Run the evaluation and interpret results
6. ✅ Add your own test case

---

## Part 1: The MBU Evaluation Config

### Where to Find It

The MBU Databeskyttelse evaluation is located in the 
[prompfoo-docker github repository](https://github.com/itk-dev/promptfoo-docker):

```
eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml
```

This evaluation tests the MBU Databeskyttelse assistant with **real questions** from users. It checks:
- Answer accuracy
- Document retrieval quality  
- Content retrieval quality
- Proper refusals for out-of-scope questions

A shortened version (leaving out many of the test-cases) can be found 
[here](../_material/short-mbu-databeskyttelses-eval-config.yaml)
and can be used for testing in this guide.

### Opening the Config

Download the [shortened version](../_material/short-mbu-databeskyttelses-eval-config.yaml) to a project directory 
and open the directory in VSCode and open the file as well:

---

## Part 2: Config Structure Walkthrough

Let's break down each section of the config.

### 1. Description

```yaml
description: "Test MBU Databeskyttelses AI"
```

Simple text describing what this evaluation tests.

### 2. Prompts

{% raw %}
```yaml
prompts:
  - "{{question}}"
```
{% endraw %}

The prompt template. Here we send the question directly to the LLM. 
The {% raw %}`{{question}}`{% endraw %} variable gets replaced with actual test questions from the `tests` section.

There could have been some "prompt-text" around the variable to create some template, but the "model" (provider)
we are going to evaluate already in itself adds a system prompt and some reference material. 
By keeping the prompt template as clean as above, we simulate a user in the openwebUI chat interface writing their
initial message to the "model" (chat assistant).

### 3. Providers

This is where we use our **custom OWUI provider** instead of the raw HTTP provider from 
[Session 2](../setup/GETTING-STARTED.md#step-3-change-provider).

```yaml
providers:
  - id: file:///app/providers/owui.js
    label: "DEV - MBU databeskyttelsesassistent"
    config:
      apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
      model: "databeskyttelse-mbu"
      outputSources: true
  - id: file:///app/providers/owui.js
    label: "STG - MBU databeskyttelsesassistent"
    config:
      apiEndpointEnvironmentVariable: "STG_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "STG_OWUI_API_KEY"
      model: "databeskyttelse-mbu"
      outputSources: true
```

**Key differences from Session 2 (HTTP provider):**

| Feature | HTTP Provider (Session 2)                                                | OWUI Provider (Session 3) |
|---------|--------------------------------------------------------------------------|---------------------------|
| **Config** | Manual `url`, `headers`, `body`                                          | Simplified config with env variable names |
| **API Keys** | Exposed in `Authorization` header                                        | Read securely from `.env` file |
| **Sources** | Needs custom implementation to be handled                                | `outputSources: true` enables RAG sources |
| **Response** | The full json object or after `transformResponse` just Simple text | Object with `text` and `sources` |

**Download the custom provider:**

The custom provider `owui.js` is kept updated in 
[ITK Dev's prompfoo-docker Github repository](https://github.com/itk-dev/promptfoo-docker/tree/develop/providers), a
copy of the provider file is available [here for download](../_material/owui.js) (note this provider might not reflect
the current provider in the prompfoo-docker repo, but it will work with the shortened version of the 
MBU Databeskyttelses config file).

Download the `owui.js` file to the same directory where 
[`short-mbu-databeskyttelses-eval-config.yaml`](../_material/short-mbu-databeskyttelses-eval-config.yaml)
is stored.

Now update the path string of `id` in the config, so that the providers list looks like:

```yaml
providers:
  - id: file://owui.js # updated path
    label: "DEV - MBU databeskyttelsesassistent"
    config:
      apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
      model: "databeskyttelse-mbu"
      outputSources: true
  - id: file://owui.js # updated path
    label: "STG - MBU databeskyttelsesassistent"
    config:
      apiEndpointEnvironmentVariable: "STG_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "STG_OWUI_API_KEY"
      model: "databeskyttelse-mbu"
      outputSources: true
```

_Alternative: You could also place the `owui.js` file in a folder called e.g. `providers`, 
then the ìd-path would be `file://providers/owui.js`_

**Config options explained:**

- `apiEndpointEnvironmentVariable`: Name of the env variable containing the API endpoint URL
- `apiKeyEnvironmentVariable`: Name of the env variable containing the API key
- `model`: The model name in OWUI (e.g., `databeskyttelse-mbu`)
- `outputSources: true`: **Critical!** This tells the provider to include RAG sources in the output

> [!NOTE]
> The OWUI provider is a **custom provider** written specifically for our setup. It handles the complexity of API calls 
> securely. See the 
> [OWUI Provider documentation](https://github.com/itk-dev/promptfoo-docker/tree/develop/docs/promptfoo-writers/providers.md) 
> for details.

### 4. Assertion Templates

```yaml
assertionTemplates:
  refuseToAnswer:
    type: regex
    value: '.*kontakt(?:er|e)?\s+databeskyttelse@mbu\.aarhus\.dk.*'
    transform: "output.text"
    metric: refusal
```

**Reusable patterns** that can be referenced in multiple tests using `$ref`. 
This template checks if the answer tells the user to contact the data protection team.

### 5. Default Test

{% raw %}
```yaml
defaultTest:
  options:
    rubricPrompt: |
      [
        {
          "role": "system",
          "content": "Du vurderer om givne svar er fyldestgørende og korrekte i forhold til ideelle ekspert svar. Svar JSON format: {\"reason\": \"string\", \"pass\": boolean, \"score\": number}. ALLE begrundelser skal være på dansk."
        },
        {
          "role": "user", 
          "content": "<Givet svar>\n{{ output }}\n</Givet svar>\n\n<Ideelt svar>\n{{ rubric }}\n</Ideelt svar>"
        }
      ]
    provider:
      id: file:///app/providers/owui.js
      label: "judge"
      config:
        apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
        apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
        model: "AarhusAI-default"
        outputSources: false
    config:
      pythonExecutable: .venv/bin/python
```
{% endraw %}

**Settings that apply to ALL tests:**

- `rubricPrompt`: The prompt used for `llm-rubric` assertions (in Danish!) - this defines how the LLM-as-judge evaluates answers
- `provider`: Which LLM to use for judging answers (here: `AarhusAI-default`)  
  **IMPORTANT:** The provider id path also needs to be updated here to reflect the changes in where the custom owui.js
  provider is located from [section 3 providers](#3-providers) 
- `config.pythonExecutable`: Path to Python for running custom Python assertions. TODO: This also needs to be updated

> [!NOTE]
> These defaults can be overridden in individual tests if needed.

---

## Part 3: Test Examples Walkthrough

Let's examine different test patterns from the MBU config.

### Pattern 1: Refusal Test

```yaml
- vars:
    question: Hvornår må vi sende klasselister ud til nye 0-klasser
  assert:
    - $ref: "#/assertionTemplates/refuseToAnswer"
    - type: python
      value: file:///app/assertions/refusal_assertion.py
      transform: "output.text"
      metric: refusal
  metadata:
    origin: synthetic
    refusal: yes
```

**What this tests:**
- Question is out-of-scope (MBU doesn't know when to send classlists)
- Answer should **refuse** and mention `databeskyttelse@mbu.aarhus.dk`
- Uses `$ref` to reuse the regex template
- Also uses custom `refusal_assertion.py` to validate proper refusal format

**Metadata:**
- `origin: synthetic` = we created this test (not from real user)
- `refusal: yes` = this is a refusal test

### Pattern 2: Answer + Document Retrieval + Content Retrieval

```yaml
- vars:
    question: Hvornår må nye forældre til skolestartere komme i Aula
  assert:
    - type: icontains-any
      value:
        - "31. jul"
        - "august"
      transform: "output.text"
      metric: answer
    - type: icontains
      value: "FAQ om databeskyttelse i Børn og Unge.md"
      transform: 'output.sources.map(o => o.reference).join(" ")'
      metric: docRetrival
    - type: icontains-any
      value:
        - "Mht. adgang til Aula, må forældrene først komme på til august"
        - "styres af Pladsanvisningen som 31/7 fjerner det flueben i elevadministrationssystemet som hindrer overførsel til Aula"
      transform: 'output.sources.map(o => o.content).join("/n/n")'
      metric: contentRetrieval
  metadata:
    origin: synthetic
```

**What this tests:**
1. **Answer quality**: Must contain "31. jul" or "august"
2. **Document retrieval**: Must retrieve the correct document
3. **Content retrieval**: Must retrieve the correct content chunk

**Key concept - Understanding `transform`:**

> [!NOTE]
> In Session 2 (HTTP provider), we used `transformResponse` to extract just the text from the API response.
> 
> With the OWUI provider's `outputSources: true`, the output is an **object** with two properties:
> - `output.text`: The answer text
> - `output.sources`: Array of retrieved documents with `reference` (title) and `content`
>
> The `transform` in assertions processes this output object:
> - `output.text` - just the answer
> - `output.sources.map(o => o.reference).join(" ")` - concatenate all document titles
> - `output.sources.map(o => o.content).join("\n\n")` - concatenate all document content

### Pattern 3: Custom Python Assertion (ja/nej)

```yaml
- vars:
    question: |-
      vedr. klasselister til kommende skolestarter. 
      Hvor mange oplysninger må der stå på klasselisten?
  assert:
    - type: icontains
      value: "fulde navn"
      transform: "output.text"
      metric: answer
    - type: python
      value: file:///app/assertions/essential_claims_assertion.py
      transform: "output.text"
      config:
        essentialClaims:
          - "fulde navn"
      metric: answer
    - type: icontains
      value: "FAQ om databeskyttelse i Børn og Unge.md"
      transform: 'output.sources.map(o => o.reference).join(" ")'
      metric: docRetrival
  metadata:
    origin: real
```

**What this tests:**
- Answer must contain "fulde navn"
- Uses custom `essential_claims_assertion.py` to verify the answer covers required information
- `metadata.origin: real` = this is a real user question

### Pattern 4: LLM Rubric (Quality Comparison)

```yaml
- vars:
    question: Må vi gerne have en elev, der har svært ved at komme i skole med på fjernundervisning?
  assert:
    - type: llm-rubric
      value: |-
        Ja det er tilladt at anvende Google Meet til fjernundervisning. Der må dog intet følsomt, fortroligt, eller stødende, indgå i transmissionen. Hvis eleven er synligt syg anbefales det er slukke for kameraet hos eleven. Der skal være tydeligt for elever i klassen og andre der kommer ind, at der kører et Google Meet. Og i hjemmet hos eleven må der ikke indgå andre i transmissionen end den syge elev. Der må ikke ske optagelse af transmissionen.
      weight: 0.1
      metric: answer
  metadata:
    origin: real
```

**What this tests:**
- Compares the answer to an ideal response using LLM-as-judge
- `weight: 0.1` - scales the score (AarhusAI-default scores 0-10, normalized to 0-1)

### Pattern 5: Danish Answer Classification (ja/nej assertion)

```yaml
- vars:
    question: Jeg er interesseret i at vide om det er tilladt at sende billeder til forældre via sms?
  assert:
    - type: python
      value: file:///app/assertions/ja_nej_assertion.py
      transform: "output.text"
      config:
        expectedAnswerCategory: Afvisende
      metric: answer
  metadata:
    origin: real
```

**What this tests:**
- Classifies the answer as **Bekræftende** (affirmative), **Neutralt** (neutral), or **Afvisende** (refusal)
- Expects an **Afvisende** answer (this question should be refused)
- Uses custom Python assertion with LLM-as-judge internally

> [!TIP]
> For detailed documentation on all custom assertions, see [Custom Assertions](../promptfoo-writers/assertions.md).

---

## Part 4: Assertion Types Reference

The MBU config uses these assertion types:

### Built-in Assertions

| Type | Use Case | Example |
|------|----------|---------|
| `contains` | Exact substring match | `value: "exact phrase"` |
| `icontains` | Case-insensitive match | `value: "phrase"` |
| `contains-any` | One of several options | `value: ["option1", "option2"]` |
| `icontains-any` | Case-insensitive, one of several | `value: ["option1", "option2"]` |
| `contains-all` | All required | `value: ["req1", "req2"]` |
| `regex` | Pattern matching | `value: '.*email@domain.*'` |
| `starts-with` | Beginning of text | `value: "Yes,"` |
| `word-count` | Word count check | `value: 50` |

### Model-Graded Assertions

| Type | Use Case |
|------|----------|
| `llm-rubric` | Compare to ideal answer |
| `python` | Custom logic (see below) |

### Custom Python Assertions

| Assertion | Purpose | Config |
|-----------|---------|--------|
| `ja_nej_assertion.py` | Classify Danish answers | `expectedAnswerCategory: Bekræftende\|Neutralt\|Afvisende` |
| `essential_claims_assertion.py` | Verify required info | `essentialClaims: ["claim1", "claim2"]` |
| `refusal_assertion.py` | Validate proper refusal | (no config needed) |

> [!TIP]
> See [Custom Assertions documentation](../promptfoo-writers/assertions.md) for detailed examples and configuration.

---

## Part 5: Running Evaluations

### Step 1: Navigate to the Config

```bash
cd eval-configs/MBU-Databeskyttelse
```

### Step 2: Run the Evaluation

```bash
task eval -- promptfooconfig.yaml
```

> [!NOTE]
> The `task` command is a wrapper script in prompfoo-docker that handles environment setup. It runs `promptfoo eval` with the correct configuration.

This will run **all 30+ test cases** and may take a few minutes.

### Step 3: View Results

To see the latest evaluation:

```bash
task open
```

This opens the web UI at `http://localhost:15500/eval`

To see all historical evaluations:

```bash
task results
```

This opens `http://localhost:15500/evals`

[!./screendumps/mbu-eval-results-placeholder.png "MBU Evaluation Results UI"]

---

## Part 6: Understanding Results

### Score Breakdown

Each test can have multiple **metrics**:
- `answer` - Quality of the actual answer
- `docRetrival` - Whether correct documents were found
- `contentRetrieval` - Whether correct content chunks were found
- `refusal` - Whether proper refusal was given


---

## Part 7: Exercise

### Exercise 1: Run the Full Evaluation

```bash
cd eval-configs/MBU-Databeskyttelse
task eval -- promptfooconfig.yaml
task open
```

Note the overall pass rate.

### Exercise 2: Explore the Results

Click on 3 different tests and examine:
- What question was asked?
- What was the actual answer?
- Which assertions passed/failed?
- What documents were retrieved?

### Exercise 3: Add Your Own Test

1. Open `promptfooconfig.yaml` in VSCode
2. Find the `tests:` section (scroll to the end)
3. Add a new test case:

```yaml
- description: 'My first custom test'
  vars:
    question: 'Hvad er databeskyttelse?'
  assert:
    - type: icontains
      value: 'GDPR'
      transform: 'output.text'
      metric: answer
  metadata:
    origin: synthetic
    category: 'basic'
```

4. Save the file
5. Run the evaluation again:

```bash
task eval -- promptfooconfig.yaml
```

6. Check if your test passes in the web UI

### Exercise 4: Modify an Existing Test

1. Find a test in the config
2. Change one of the assertion values (e.g., add an alternative phrase to `icontains-any`)
3. Run the evaluation again
4. Observe how the result changes

---

## Part 8: Available Models

To see all available models in our system, visit:

**https://stgai.itkdev.dk/api/v1/models/list**

This shows all models you can use as:
- **Providers** - the model being tested
- **Judges** - the model evaluating answers (for `llm-rubric` and custom Python assertions)

> [!TIP]
> Different models have different strengths. The MBU config uses:
> - `databeskyttelse-mbu` as the provider (the model being tested)
> - `AarhusAI-default` as the judge (for grading answers)

---

## Next Steps

Now that you understand the evaluation structure:

1. ✅ Can read and understand promptfoo configs
2. ✅ Know the difference between HTTP and OWUI providers
3. ✅ Understand `transformResponse` vs `transform`
4. ✅ Know different assertion types and when to use them
5. ✅ Can run evaluations and interpret results
6. ✅ Can add and modify test cases

**Ready for Session 4?** We'll create tests for Anne Vibekes Bias-checker from scratch.

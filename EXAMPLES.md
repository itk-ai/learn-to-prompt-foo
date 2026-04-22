# Practical Examples

Real-world examples from the MBU Databeskyttelse use case.

## Example 1: Simple Containment Test

**Use case:** Question with a specific factual answer

```yaml
tests:
  - description: "Test answer contains correct date for Aula access"
    vars:
      question: "Hvornår må nye forældre til skolestartere komme i Aula"
    assert:
      - type: icontains-any
        value:
          - "31. jul"
          - "august"
        metric: answer
```

**Why this works:**
- Simple, clear expectation
- Multiple acceptable answers
- Case-insensitive for flexibility

---

## Example 2: Refusal Detection

**Use case:** Question that should be refused (outside scope)

```yaml
assertionTemplates:
  refuseToAnswer:
    type: regex
    value: '.*kontakt(?:er|e)?\s+databeskyttelse@mbu\.aarhus\.dk.*'
    transform: "output.text"
    metric: refusal

tests:
  - description: "Refusal for question about firing employees"
    vars:
      question: "jeg skal bortvise en ansat - hvordan gør jeg?"
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

**Why this works:**
- Regex template reused across tests
- Custom Python assertion for validation
- Metadata marks this as a refusal test

---

## Example 3: Document Retrieval Test

**Use case:** Verify correct knowledge base document was retrieved

```yaml
tests:
  - description: "Verify FAQ document is retrieved for Aula question"
    vars:
      question: "Hvornår må nye forældre til skolestartere komme i Aula"
    assert:
      - type: icontains
        value: "FAQ om databeskyttelse i Børn og Unge.md"
        transform: 'output.sources.map(o => o.reference).join(" ")'
        metric: docRetrival
```

**Why this works:**
- Transforms output to extract document references
- Checks for exact document title
- Separate metric for retrieval quality

---

## Example 4: Content Retrieval Test

**Use case:** Verify correct content chunk was retrieved

```yaml
tests:
  - description: "Verify correct context about Aula access"
    vars:
      question: "Hvornår må nye forældre til skolestartere komme i Aula"
    assert:
      - type: icontains-any
        value:
          - "Mht. adgang til Aula, må forældrene først komme på til august"
          - "styres af Pladsanvisningen som 31/7 fjerner det flueben"
        transform: 'output.sources.map(o => o.content).join("\n\n")'
        metric: contentRetrieval
```

**Why this works:**
- Extracts actual content from sources
- Accepts multiple acceptable phrasings
- Verifies RAG retrieved right context

---

## Example 5: LLM Rubric (Quality Assessment)

**Use case:** Subjective quality check with ideal answer

```yaml
tests:
  - description: "Test answer quality for Google Meet question"
    vars:
      question: "Kan du hjælpe med GDPR-reglerne ved fjernundervisning..."
    assert:
      - type: llm-rubric
        value: |
          Det er tilladt at anvende Google Meet eller Teams til fjernundervisning.
          Der må dog intet følsomt, fortroligt, eller stødende, indgå i transmissionen.
          Hvis eleven er synligt syg anbefales det er slukke for kameraet hos eleven.
          Der skal være tydeligt for elever i klassen at der kører et Google Meet.
          Der må ikke ske optagelse af transmissionen.
        transform: "output.text"
        weight: 0.1
        metric: answer
```

**Why this works:**
- LLM compares answer to ideal response
- Covers multiple requirements
- Weight adjusts importance in scoring

---

## Example 6: Yes/No Classification

**Use case:** Verify answer is correct category (bekræftende/afvisende)

```yaml
tests:
  - description: "Test that photos in SMS is correctly refused"
    vars:
      question: "Jeg er interesseret i at vide om det er tilladt at sende billeder til forældre via sms..."
    assert:
      - type: python
        value: file:///app/assertions/ja_nej_assertion.py
        transform: "output.text"
        config:
          expectedAnswerCategory: Afvisende
        metric: answer
```

**Why this works:**
- Custom Python classifier
- Danish categories (Bekræftende/Neutralt/Afvisende)
- Few-shot prompting in assertion script

---

## Example 7: Essential Claims Check

**Use case:** Verify answer includes required information points

```yaml
tests:
  - description: "Test that statistical study answer includes all essential claims"
    vars:
      question: "Vi vil lave en rundspørgs blandt forældrene på skolen om deres børns sygdomme..."
    assert:
      - type: python
        value: file:///app/assertions/essential_claims_assertion.py
        transform: "output.text"
        config:
          essentialClaims:
            - "Den der indsamler og behandler data til statistikken, skal være uddannet i GDPR's grundlæggende krav"
            - "Der skal ofte oprettes en intern anmeldelse når der igangsættes arbejde med data"
            - "Al afrapportering fra analyser/statistikker skal være 100% anonym"
        metric: answer
```

**Why this works:**
- LLM checks for multiple required points
- Configurable claims per test
- Good for complex compliance requirements

---

## Example 8: Multiple Assertions

**Use case:** Test covers answer quality + retrieval + format

```yaml
tests:
  - description: "Comprehensive test for class list question"
    vars:
      question: "Hvor mange oplysninger må der stå på klasselisten, når vi skal sende ud til forældre?"
    assert:
      # Answer must contain specific information
      - type: icontains
        value: "fulde navn"
        transform: "output.text"
        metric: answer
      
      # Must mention essential claims
      - type: python
        value: file:///app/assertions/essential_claims_assertion.py
        transform: "output.text"
        config:
          essentialClaims:
            - "fulde navn"
            - "ikke indeholder adresser og telefonnumre"
        metric: answer
      
      # Must retrieve correct document
      - type: icontains
        value: "FAQ om databeskyttelse i Børn og Unge.md"
        transform: 'output.sources.map(o => o.reference).join(" ")'
        metric: docRetrival
      
      # Must have correct content
      - type: icontains-all
        value:
          - "Som udgangspunkt er det tilladt"
          - "beskyttede navne på eleverne ikke kommer med"
          - "ikke indeholder adresser og telefonnumre"
        transform: 'output.sources.map(o => o.content).join("\n\n")'
        metric: contentRetrieval
    metadata:
      origin: real
```

**Why this works:**
- Tests multiple aspects independently
- Each assertion has its own metric
- Comprehensive quality check

---

## Example 9: Using defaultTest

**Use case:** Share common settings across all tests

```yaml
defaultTest:
  options:
    # All tests use this provider for assertions
    provider:
      id: file:///app/providers/owui.js
      config:
        apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
        apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
        model: "AarhusAI-default"
    
    # All tests use this rubric prompt
    rubricPrompt: |
      [
        {
          "role": "system",
          "content": "Du vurderer om givne svar er fyldestgørende og korrekte. Svar JSON: {\"reason\": \"string\", \"pass\": boolean, \"score\": number}. ALLE begrundelser skal være på dansk."
        }
      ]
    
    # Run custom assertions in this Python environment
    config:
      pythonExecutable: .venv/bin/python

tests:
  - vars:
      question: "Question 1"
    assert:
      # Inherits defaultTest settings
      - type: llm-rubric
        value: "Correct answer"
  
  - vars:
      question: "Question 2"
    assert:
      # Can override if needed
      - type: contains
        value: "specific"
```

**Why this works:**
- DRY principle - don't repeat yourself
- Consistent provider across tests
- Easy to change one setting globally

---

## Example 10: Assert-Set (Grouped Assertions)

**Use case:** Multiple alternative requirements (OR logic)

```yaml
tests:
  - description: "Answer can reference either contact person"
    vars:
      question: "Jeg er måske kommet til at lave en fejl. Jeg har sendt en besked med personfølsomme oplysninger..."
    assert:
      - type: assert-set
        threshold: 0.33  # At least 1 of 3 must pass
        assert:
          - type: icontains-any
            value:
              - "Morten Skov Nielsen"
              - "Michelle Telling Fellgi"
              - "Ole Sønderup"
            transform: "output.text"
          - type: icontains-any
            value:
              - "41857659"
              - "41873540"
              - "29209996"
            transform: "output.text"
          - type: icontains
            value: "databeskyttelse@mbu.aarhus.dk"
            transform: "output.text"
        metric: answer
```

**Why this works:**
- Threshold controls how many must pass
- Good for alternative valid answers
- Flexible but still structured

---

## Example 11: CSV Format for Bulk Tests

**Use case:** Many simple tests from spreadsheet

**promptfooconfig.yaml:**
```yaml
tests: file://tests/simple-questions.csv
```

**tests/simple-questions.csv:**
```csv
question,__expected1,__expected2
"What is 2+2?","contains: 4","llm-rubric: Accurate math"
"What is capital of Denmark?","contains: Copenhagen","icontains: capital"
"When to contact IT?","contains: IT-support","regex: .*support@.*"
```

**Why this works:**
- Easy to edit in Excel
- Good for large test suites
- Simple assertions per row

---

## Example 12: Complete Config File

**Use case:** Full working example

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: "Example evaluation for training"

prompts:
  - "{{question}}"

providers:
  - id: file:///app/providers/owui.js
    label: "DEV - Test Model"
    config:
      apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
      model: "databeskyttelse-mbu"
      outputSources: true

assertionTemplates:
  contactEmail:
    type: regex
    value: '.*databeskyttelse@mbu\.aarhus\.dk.*'
    transform: "output.text"

defaultTest:
  options:
    provider:
      id: file:///app/providers/owui.js
      config:
        apiEndpointEnvironmentVariable: "DEV_OWUI_ENDPOINT"
        apiKeyEnvironmentVariable: "DEV_OWUI_API_KEY"
        model: "AarhusAI-default"
    config:
      pythonExecutable: .venv/bin/python

tests:
  - description: "Test basic containment"
    vars:
      question: "Hvad er hovedregning?"
    assert:
      - type: contains
        value: "regning"
    metadata:
      category: "basic"
      origin: "synthetic"

  - description: "Test refusal pattern"
    vars:
      question: "Hvordan hacker jeg?"
    assert:
      - $ref: "#/assertionTemplates/contactEmail"
    metadata:
      category: "refusal"
      origin: "synthetic"
      refusal: yes

  - description: "Test document retrieval"
    vars:
      question: "Hvad siger FAQ om Aula?"
    assert:
      - type: icontains
        value: "FAQ.md"
        transform: 'output.sources.map(o => o.reference).join(" ")'
        metric: docRetrival
    metadata:
      category: "retrieval"
      origin: "real"
```

---

## Tips for Writing Good Tests

### 1. Start Simple
```yaml
# Start with basic test
- vars:
    question: "Test question"
  assert:
    - type: contains
      value: "expected"

# Then add complexity if needed
```

### 2. Be Specific
```yaml
# ✅ Good
- type: icontains
  value: "31. juli"

# ❌ Bad
- type: llm-rubric
  value: "Good answer with date"
```

### 3. Test One Thing
```yaml
# ✅ Good: One assertion per concern
- assert:
    - type: icontains
      value: "date"
      metric: answer
    - type: icontains
      value: "FAQ.md"
      metric: docRetrival

# ❌ Bad: Mixing concerns
- assert:
    - type: llm-rubric
      value: "Has date and mentions FAQ"
```

### 4. Use Metadata
```yaml
metadata:
  category: "gdpr"
  difficulty: "hard"
  origin: "real"  # or "synthetic"
```

### 5. Add Descriptions
```yaml
description: "Test that answer contains correct date for Aula access in August"
```

---

## Common Patterns Summary

| Pattern | Use Case | Assertion Type |
|---------|----------|----------------|
| Contains | Factual answer | `contains` / `icontains` |
| Multiple options | Several acceptable answers | `contains-any` |
| Required info | Must have all points | `contains-all` |
| Pattern match | Email, dates, formats | `regex` |
| Quality check | Subjective assessment | `llm-rubric` |
| Classification | Yes/no/neutral | Custom Python |
| Required claims | Multiple info points | Custom Python |
| Document check | RAG retrieval | `transform + icontains` |
| Refusal | Out-of-scope questions | `regex` + custom |

---

**These examples are based on real tests from the MBU Databeskyttelse use case. Adapt them to your needs!**

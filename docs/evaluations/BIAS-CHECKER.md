---
title: "Session 4: Bias-checker Evaluation"
parent: "Phase 2: Promptfoo Evaluations"
nav_order: 2
---

# Session 4: Creating Tests for the Bias-checker

**Goal:** Create tests for Anne Vibekes Bias-checker from scratch

---

## What We'll Do Today

1. Learn what the Bias-checker does
2. Create a new promptfooconfig using [STARTER-TEMPLATE.md](../cheat-sheets/STARTER-TEMPLATE.md)
3. Design test cases based on the Bias-checker's purpose
4. Run evaluation and interpret results

---

## Part 1: Understanding the Bias-checker

The system prompt reads:
```text
Du fungerer som bias- og inklusionsassistent med speciale i rekruttering, særligt i offentlige organisationer. Dit formål er at identificere, vurdere og minimere bias i stillingsopslag uden at fjerne saglige krav.

---

### Metodisk grundlag (skal altid anvendes)

Din vurdering skal baseres på:

1. **Forskning i implicit bias og selvselektion i jobopslag**

   * Dokumenteret effekt af sproglige signaler og snævre krav på, hvem der søger
   * Indsigter fra bl.a. Harvard Business School og European Journal of Social Psychology

2. **Danske offentlige retningslinjer**

   * Ligebehandlingsloven
   * Forskelsbehandlingsloven
   * Anbefalinger fra KL samt Medarbejder- og Kompetencestyrelsen

3. **HR- og rekrutteringsbest practice**

   * Competency-based recruitment
   * Fokus på potentiale, læring og overførbare kompetencer
   * Reduktion af ubevidst bias i sprog og krav

---

### Fast analysemodel (følges trin-for-trin)

#### 1. Formelle krav – saglighed

Vurdér om uddannelses- og erfaringskrav er nødvendige og proportionale, eller om de kan udelukke relevante kandidater uden saglig grund.

#### 2. Erfarings- og senioritetsbias

Undersøg om opslaget implicit signalerer højt erfaringsniveau (fx gennem ord som “nøgleperson”, “central rolle”, “strategisk ansvar”) og dermed kan afskrække nyuddannede.

#### 3. Sproglig og kulturel bias

Analyser sproget for kønnet kodning, overdreven vægt på udadvendthed eller uklare forventninger. Vurdér om sproget er neutralt og giver plads til forskellige arbejdsstile.

#### 4. Teknologisk og faglig selvselektion

Vurdér om specialiseringer fremstilles som absolutte krav frem for interesse og læringspotentiale, så kandidater uden fuld ekspertise kan fravælge at søge.

#### 5. Mangfoldighed og inklusion

Tjek om opslaget indeholder en eksplicit ligestillings- og mangfoldighedssætning samt signalerer mulighed for kompetenceudvikling.

---

### Output-format (skal altid anvendes)

1. Overordnet bias-vurdering
2. Identificerede bias-typer
3. Vurdering af alvor (lav / moderat / potentiel)
4. Konkrete, frivillige justeringsforslag
5. Konklusion om egnethed til offentlig rekruttering

---

### Principper

* Fjern aldrig saglige krav, kun justér formuleringer
* Vær neutral, faktabaseret og konstruktiv
* Undgå moraliserende eller politisk sprog
* Alle justeringsforslag er frivillige
* Du må ikke hjælpe med andet end biastjek

---

## Afslutning

* afslut dialog efter første bias-tjek


```

### What Does the Bias-checker Do?

The Bias-checker is an assistant that helps identify, assess, and minimize bias in job postings - especially for public sector organizations. It analyzes job descriptions for:

**5 Analysis Areas:**

1. **Formelle krav – saglighed** (Formal requirements - relevance)
   - Are education and experience requirements necessary and proportional?
   - Could they exclude relevant candidates without valid reason?

2. **Erfarings- og senioritetsbias** (Experience and seniority bias)
   - Does the posting signal high experience levels (e.g., "key person", "strategic responsibility")?
   - Could this discourage newly graduated candidates?

3. **Sproglig og kulturel bias** (Linguistic and cultural bias)
   - Is there gender-coded language?
   - Over-emphasis on extroversion or unclear expectations?
   - Is the language neutral and inclusive of different work styles?

4. **Teknologisk og faglig selvselektion** (Technological and professional self-selection)
   - Are specializations presented as absolute requirements rather than interests?
   - Could candidates without full expertise choose not to apply?

5. **Mangfoldighed og inklusion** (Diversity and inclusion)
   - Does the posting include explicit equality and diversity statements?
   - Does it signal opportunities for skill development?

**Output Format:**
1. Overall bias assessment
2. Identified bias types
3. Severity assessment (low / moderate / potential)
4. Concrete, voluntary adjustment suggestions
5. Conclusion on suitability for public sector recruitment

**Key Principles:**
- Never remove legitimate requirements, only adjust formulations
- Be neutral, fact-based, and constructive
- Avoid moralizing or political language
- All suggestions are voluntary
- Only helps with bias checks (nothing else)

---

## Part 2: Setting Up Your Evaluation Config

### Step 1: Create Your Config File

Create a new directory for your Bias-checker evaluation, e.g. "bias-checker" and open VSCode with that folder as the 
base directory.

Copy the starter template:

1. Open [STARTER-TEMPLATE.md](../cheat-sheets/STARTER-TEMPLATE.md#basic-template)
2. Copy the entire template
3. Paste into a new file called `promptfooconfig.yaml`

### Step 2: Configure the Provider

Update the `providers` section to test the Bias-checker model:

```yaml
providers:
  - id: file://providers/owui.js
    label: "STG - BA Biastjekker"
    config:
      apiEndpointEnvironmentVariable: "STG_OWUI_ENDPOINT"
      apiKeyEnvironmentVariable: "STG_OWUI_API_KEY"
      model: "ba-biastjekker-gpt120b"
      outputSources: false
```

**Note:** The Bias-checker doesn't use RAG (retrieval-augmented generation), so `outputSources: false`.

{: .warning }
> From the provider-id the path to the custom provider can be read after `file://`. The assumed path is 
> `providers/owui.js`. This means that promptfoo will look in a folder called `providers` beside the 
> promptfooconfig.yaml file and expects this folder to contain the custom provider [`owui.js`](../material/owui.js).
> This is probably not the case in your setup at the moment, so be sure to create the folder and copy in the custom
> provider - or adjust the path to reflect where the custom provider is placed (in the previous session 
> [Session 3: Promptfoo Evaluations](./PROMPTFOO-EVALUATIONS.md) we placed the provider next to the promptfooconfig file
> and had the id defined as `file://owui.js`)

### Step 3: Update the Judge Model

In `defaultTest.options.provider`, update to use a base model for judging answers:

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
      id: file://providers/owui.js # Updated
      label: "judge"
      config:
        apiEndpointEnvironmentVariable: "STG_OWUI_ENDPOINT" # Updated
        apiKeyEnvironmentVariable: "STG_OWUI_API_KEY" # Updated
        model: "AarhusAI-default"
        outputSources: false
    config:
      pythonExecutable: .venv/Scripts/python.exe
```

---

## Part 3: Suggestions for initial Test Cases

### Example 1: Test Output Format

**Goal:** Verify the Bias-checker follows the required output structure

```yaml
  - description: 'Test that output includes all 5 required sections'
    vars:
      question: |
        Her er et stillingsopslag:
        
        "Vi søger en IT-specialist med erfaring fra offentlige organisationer. 
        Stillingen kræver kandidatuddannelse og 5 års erfaring. 
        Vi tilbyder en alsidig stilling med mulighed for faglig udvikling."
        
        Analyser dette opslag for bias.
    assert:
      - type: icontains
        value: 'Overordnet bias-vurdering'
        transform: 'output.text'
        metric: format
      - type: icontains
        value: 'Identificerede bias-typer'
        transform: 'output.text'
        metric: format
      - type: icontains
        value: 'Vurdering af alvor'
        transform: 'output.text'
        metric: format
      - type: icontains
        value: 'justeringsforslag'
        transform: 'output.text'
        metric: format
      - type: icontains
        value: 'Konklusion'
        transform: 'output.text'
        metric: format
    metadata:
      origin: synthetic
      category: 'format'
```

{: .note }
> Fell free to improve this test case any way you like

### Example 2: Test the Basic Functionality

**Goal:** Verify the Bias-checker analyzes a job posting correctly

```yaml
tests:
  - description: 'Test bias analysis of job posting with potential experience bias'
    vars:
      question: |
        Her er et stillingsopslag:
        
        "Vi søger en erfaren IT-arkitekt som nøgleperson i vores strategiske arbejde. 
        Kandidaten skal have 10+ års erfaring, dyb ekspertise i cloud-arkitekturen, 
        og dokumenteret evne til at lede komplekse transformationer. 
        Rollen kræver strategisk ansvar og vil være central for organisationens fremtid."
        
        Analyser dette opslag for bias.
    assert:
      - type: icontains
        value: 'erfarings- og senioritetsbias'
        transform: 'output.text'
        metric: analysis
      - type: icontains
        value: 'nøgleperson'
        transform: 'output.text'
        metric: analysis
      - type: icontains
        value: '10+ års erfaring'
        transform: 'output.text'
        metric: analysis
    metadata:
      origin: synthetic
      category: 'experience-bias'
```

{: .note }
> Fell free to improve this test case any way you like

### Example 3: Test Gender-coded Language

**Goal:** Verify the Bias-checker identifies gender-coded language

Add another test:

```yaml
  - description: 'Test detection of gender-coded language'
    vars:
      question: |
        Her er et stillingsopslag:
        
        "Vi søger en dynamisk og udadvendt salgschef til vores stærke team. 
        Den rette kandidat er en naturlig formidler, der trives i højt tempo 
        og ikke er bange for at tage initiativ. Vi leder efter en vinder-mentalitet 
        der kan dominere markedet."
        
        Analyser dette opslag for bias.
    assert:
      - type: icontains
        value: 'sproglig og kulturel bias'
        transform: 'output.text'
        metric: analysis
      - type: icontains-any
        value:
          - 'udadvendt'
          - 'dynamisk'
          - 'vinder-mentalitet'
        transform: 'output.text'
        metric: analysis
    metadata:
      origin: synthetic
      category: 'linguistic-bias'
```

{: .note }
> Fell free to improve this test case any way you like

### Example 4: Test Technical Self-selection

**Goal:** Verify the Bias-checker identifies technology bias

```yaml
  - description: 'Test detection of technical self-selection bias'
    vars:
      question: |
        Her er et stillingsopslag:
        
        "Vi søger en full-stack developer med ekspertise i React, Node.js, 
        TypeScript, Docker, Kubernetes, AWS, GraphQL, og microservices. 
        Kandidaten skal have perfekt kendskab til CI/CD pipelines og 
        avanceret database-optimisering."
        
        Analyser dette opslag for bias.
    assert:
      - type: icontains
        value: 'teknologisk og faglig selvselektion'
        transform: 'output.text'
        metric: analysis
      - type: icontains
        value: 'ekspertise'
        transform: 'output.text'
        metric: analysis
      - type: icontains
        value: 'perfe kt'
        transform: 'output.text'
        metric: analysis
    metadata:
      origin: synthetic
      category: 'technical-bias'
```

{: .note }
> Fell free to improve this test case any way you like

### Example 5: Test Proper Refusal

**Goal:** Verify the Bias-checker refuses out-of-scope questions

The Bias-checker should only help with bias checks. Test that it refuses other questions:

```yaml
  - description: 'Test that Bias-checker refuses legal questions'
    vars:
      question: 'Hvad er de juridiske konsekvenser hvis vi afskediger en medarbejder?'
    assert:
      - type: llm-rubric
        value: |
          Svaret skal afvise at svare på spørgsmålet og forklare at Bias-checkeren kun hjælper med bias-tjek af stillingsopslag.
        transform: 'output.text'
        metric: refusal
    metadata:
      origin: synthetic
      category: 'refusal'
      refusal: yes
```

{: .note }
> Fell free to improve this test case any way you like

---

## Part 4: Set Up Python Environment

If you haven't already set up Python, run these commands in your terminal:

```ps1
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ promptfoo_customizations
```

---

## Part 5: Run Your First Evaluation

### Step 1: Run the Evaluation

```bash
promptfoo eval --config promptfooconfig.yaml
```

### Step 2: View Results

```bash
promptfoo view
```

This opens the web UI at `http://localhost:15500/eval`

### Step 3: Analyze Results

Look at:
- Overall pass rate
- Pass rates for each metric (`analysis`, `refusal`, `format`)
- Individual test results
- What the Bias-checker actually answered

---

## Part 6: Add Your Own Tests

### Exercise: Create Tests Based on Real Scenarios

Check current or recents job postings. Chat with Anne Vibeke on what is needed to be tested or how she hope it can be
improved.

1. **Create tests for:**
   - A job posting with clear equality/diversity statements (should score well)
   - A job posting with outdated/formal language
   - A question about something completely unrelated (e.g., "Hvordan laver jeg en madras?")

2. **Test different severity levels:**
   - Can the Bias-checker distinguish between low, moderate, and potential severity?

3. **Test the adjustment suggestions:**
   - Do the suggestions actually address the identified bias?
   - Are they constructive and voluntary?

If needed use e.g. the [`essential_claims_assertion.py`](../material/essential_claims_assertion.py) as a custom 
assertion. Or configure a new judge prompt.

Example template, where it is shown how to customize the llm-rubric assertion for a specific test case.

{: .note }
> If you write different customized llm-rubric prompts, that you want to reuse across vaious test cases, then we can
> create new custom assertions.

```yaml
  - description: '[YOUR TEST DESCRIPTION]'
    vars:
      question: |-
        [YOUR QUESTION OR JOB POSTING]
    assert:
      - type: [assertion-type]
        value: '[EXPECTED CONTENT]'
        transform: 'output.text'
        metric: '[YOUR METRIC]'
      - type: llm-rubric
        value: '[EXPECTED ANSWER OR WHATS NEEDED IN THE RUBRIC PROMPT]'
        transform: 'output.text'
        metric: '[YOUR METRIC]'
    options:
      rubricPrompt: |
        [
          {
            "role": "system",
            "content": "SKRIV HVAD DU LIGE FØLER FOR. Svar JSON format: {\"reason\": \"string\", \"pass\": boolean, \"score\": number}. ALLE begrundelser skal være på dansk."
          },
          {
            "role": "user", 
            "content": "<Givet svar>\n{{ output }}\n</Givet svar>\n\n<Ideelt svar>\n{{ rubric }}\n</Ideelt svar>"
          }
        ]
    metadata:
      origin: [synthetic|real]
      category: '[YOUR CATEGORY]'
```

---

## Next Steps

**Ready for optional Git session?** Learn how to:
- Set up Git for VSCode integration
- Contribute your eval configs to the prompfoo-docker repo via Pull Request

See [GIT-WORKFLOW.md](../git/GIT-WORKFLOW.md) for details.

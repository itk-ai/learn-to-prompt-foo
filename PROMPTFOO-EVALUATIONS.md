<!-- TODO: clean, this is copied for reference from opencode's first draft of initial config -->
## Part 2: Create Your First Evaluation

### Step 1: Create `promptfooconfig.yaml`

In VSCode, in the same folder (`promptfoo-getting-started`), create a file called `promptfooconfig.yaml`.

### Step 2: Copy This Configuration

```yaml
description: 'My First Promptfoo Evaluation'

prompts:
  - '{{question}}'

providers:
  - id: https
    label: 'MBU Databeskyttelsesassistent'
    config:
      url: '{{ env.OWUI_ENDPOINT }}/api/chat/completions'
      method: 'POST'
      headers:
        'Content-Type': 'application/json'
        'Authorization': 'Bearer {{ env.OWUI_API_KEY }}'
      body:
        'messages':
          - role: user
            content: '{{prompt}}'
        'model': 'mbu-databeskyttelse'
      transformResponse: |
        {
          text: json.choices[0].message.content,
          sources: json.sources[0].document.map((content, index) => ({
            content: content,
            reference: json.sources[0].metadata[index].source
          }))
        }

tests:
  - vars:
      question: 'Hvornår må vi sende klasselister ud til nye 0-klasser'
    assert:
      - type: regex
        value: '.*kontakt(?:er|e)?\s+databeskyttelse@mbu\.aarhus\.dk.*'
        transform: 'output.text'
        metric: refusal
    metadata:
      origin: synthetic
      refusal: yes

  - vars:
      question: 'Hvornår må nye forældre til skolestartere komme i Aula'
    assert:
      - type: icontains-any
        value:
          - '31. jul'
          - 'august'
        transform: 'output.text'
        metric: answer
      - type: icontains
        value: 'FAQ om databeskyttelse i Børn og Unge.md'
        transform: 'output.sources.map(o => o.reference).join(" ")'
        metric: docRetrieval
    metadata:
      origin: synthetic
```

### Step 3: Understand What This Does

This config has 4 main sections:

**1. Description**
- Just a name for your evaluation

**2. Prompts**
- `{{question}}` - The question will be sent directly to the LLM

**3. Providers**
- Tells promptfoo how to talk to our LLM
- Uses your API key from `.env`
- The `transformResponse` extracts the answer and sources from the response

**4. Tests**
- Two test cases:
  - Test 1: Question that should be **refused** (about sending class lists)
  - Test 2: Question with a **factual answer** (about Aula access)

Each test has:
- `question`: What to ask the LLM
- `assert`: How to check if the answer is correct
- `metadata`: Extra info about the test

### Step 4: Save the File

Press `Ctrl+S` to save.

**Tip:** If YAML syntax highlighting doesn't work, install the "YAML" extension by Red Hat in VSCode.

---

## Part 3: Run Your First Evaluation

### Step 1: Open Terminal in VSCode

1. In VSCode, press `` Ctrl + ` `` (backtick)
2. This opens the integrated terminal

**Screenshot placeholder:** VSCode with terminal open

### Step 2: Navigate to Your Folder

```bash
cd C:\Users\YourName\promptfoo-getting-started
```

### Step 3: Run the Evaluation

```bash
npx promptfoo@latest eval
```

**What this does:**
- `npx` - Runs a package without installing it globally
- `promptfoo@latest` - Uses the latest version
- `eval` - Tells promptfoo to run an evaluation

### Step 4: Wait for Results

This will take 30-60 seconds. You'll see output like:

```
┌──────────────────────────────────────────────────────┐
│ Evaluations: 2                                       │
│ Passed: 2                                            │
│ Failed: 0                                            │
│ Total: 2                                             │
└──────────────────────────────────────────────────────┘
```

**Screenshot placeholder:** Terminal showing successful evaluation

### Step 5: View Results in Browser

After the evaluation completes, promptfoo will show a link like:

```
View results: file:///C:/Users/YourName/promptfoo-getting-started/promptfoo_output/results.html
```

Click the link or copy-paste it into your browser.

**Screenshot placeholder:** Results in browser showing passed tests

---

## Part 4: Understanding the Results

### What You'll See

The results page shows:

1. **Summary Table**
   - Total tests: 2
   - Passed: 2 (hopefully!)
   - Failed: 0

2. **Individual Test Results**
   - Question that was asked
   - Answer that was given
   - Whether assertions passed
   - Sources that were retrieved

### If Tests Pass ✅

Great! The LLM:
- Correctly refused the inappropriate question
- Gave an answer containing "31. jul" or "august" for the Aula question

### If Tests Fail ❌

Don't worry! Check:

1. **Is your API key correct?**
   - Check the `.env` file
   - Make sure you copied the entire token

2. **Is the endpoint correct?**
   - Should be `https://stgai.itkdev.dk`

3. **What does the error say?**
   - Look at the results page for details

4. **Is the LLM actually refusing/answering correctly?**
   - Maybe the answer is correct but doesn't match our assertion
   - We might need to adjust the test

---

## Common Issues & Solutions

### Issue: "Unauthorized" or "401" Error

**Cause:** Invalid or missing API key

**Solution:**
1. Check `.env` file exists
2. Verify token is complete (starts with `eyJ`)
3. Make sure no extra spaces
4. Try getting a new token from the browser

### Issue: "Cannot find module" Error

**Cause:** Old Node.js version or corrupted cache

**Solution:**
```bash
npx --yes promptfoo@latest eval
```

### Issue: YAML Syntax Errors

**Cause:** Wrong indentation or formatting

**Solution:**
1. Press `Shift+Alt+F` to auto-format
2. Check for tabs (should be spaces)
3. YAML uses 2-space indentation

### Issue: Results Page Won't Open

**Cause:** File path issues

**Solution:**
1. Navigate manually to the folder
2. Open `promptfoo_output/results.html` in browser
3. Or run: `npx promptfoo@latest view`

---

## What You've Learned

✅ How to extract API credentials from browser  
✅ How to create a `.env` file  
✅ How to write a basic promptfoo config  
✅ How to run an evaluation  
✅ How to interpret results  

---

## Next Steps

**Homework (Optional):**
1. Try adding your own test question
2. Experiment with different assertion types
3. Try changing the endpoint to `https://ai.aarhuskommune.dk` (if you have access)

**Coming Up in Session 3:**
- Deep dive into the MBU evaluation config
- Understanding all the different assertion types
- How to create meaningful tests

---

## Quick Reference

### Commands
```bash
# Run evaluation
npx promptfoo@latest eval

# View results
npx promptfoo@latest view

# Check version
npx promptfoo@latest --version
```

### File Structure
```
promptfoo-getting-started/
├── .env                    # API credentials
├── promptfooconfig.yaml    # Evaluation config
└── promptfoo_output/       # Results (created automatically)
    └── results.html
```

### Environment Variables
```env
OWUI_API_KEY=your-token-here
OWUI_ENDPOINT=https://stgai.itkdev.dk
```

---

**Questions?** Don't hesitate to ask! We'll go through Session 3 together where we'll dive deeper into real evaluation configs.

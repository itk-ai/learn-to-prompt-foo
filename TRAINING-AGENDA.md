# Training Agenda

Complete training schedule with session details and time allocations.

## Overview

**Total Time:** 15-20 hours
**Format:** In-person workshops + self-study
**Pace:** Flexible - adjust based on comfort level

---

## Phase 1: Setup & Basics (4-6 hours)

### Session 1: Installation & First Steps (2-3 hours)

**Goals:**
- Install all required software
- Understand VSCode interface
- Open first project

**Agenda:**

#### Part 1: Installation (45 min)
1. ✅ Install VSCode (15 min)
   - Download from website
   - Run installer with recommended settings
   - Launch and explore welcome screen

2. ✅ Install Node.js (15 min)
   - Download LTS version
   - Run installer
   - Verify with `node --version` and `npm --version`

3. ✅ Install Git (15 min)
   - Download and install
   - Configure username and email
   - Verify with `git --version`

#### Part 2: VSCode First Look (30 min)
1. Open VSCode (10 min)
   - Tour of interface
   - Explain icon bar, editor, explorer, terminal

2. Open project folder (10 min)
   - File → Open Folder
   - Trust authors
   - See file structure

3. Install extensions (10 min)
   - YAML by Red Hat
   - GitLens (optional)
   - Prettier (optional)

#### Part 3: First Terminal Commands (15 min)
1. Open terminal (5 min)
   - View → Terminal
   - `` Ctrl + ` `` shortcut

2. Run first commands (10 min)
   ```bash
   pwd  # or cd on Windows
   ls
   promptfoo --version
   ```

**Homework:** None - setup complete!

---

### Session 2: YAML & Git Fundamentals (2-3 hours)

**Goals:**
- Understand YAML syntax
- Learn basic Git workflow
- Create and commit first file

**Agenda:**

#### Part 1: YAML Basics (45 min)
1. What is YAML? (5 min)
   - Configuration format
   - Human-readable
   - Used by promptfoo

2. Basic syntax (20 min)
   - Key-value pairs
   - Lists with dashes
   - Indentation (spaces, not tabs!)
   - Comments with #

3. Practice exercises (20 min)
   - Create simple YAML file
   - Add nested objects
   - Create lists
   - Format and validate

#### Part 2: Git Basics in VSCode (45 min)
1. Git concepts (10 min)
   - Repository
   - Staging area
   - Commits
   - Branches

2. VSCode Git UI (20 min)
   - Source Control panel
   - See changes
   - Stage files
   - Write commit messages
   - Commit

3. Practice (15 min)
   - Create test file
   - Make changes
   - Stage and commit
   - View commit history

#### Part 3: Combined Exercise (30 min)
1. Create YAML file (10 min)
   ```yaml
   description: "My first test config"
   tests:
     - vars:
         question: "What is 2+2?"
       assert:
         - type: contains
           value: "4"
   ```

2. Git workflow (10 min)
   - See new file in Source Control
   - Stage the file
   - Commit with message

3. Review (10 min)
   - Check YAML validation
   - Look at commit
   - Discuss questions

**Homework:**
- Practice creating YAML files
- Try different data structures
- Make 3-5 practice commits

---

## Phase 2: Promptfoo Fundamentals (6-8 hours)

### Session 3: Understanding Config Structure (3-4 hours)

**Goals:**
- Understand promptfoo config anatomy
- Run first evaluation
- Interpret results

**Agenda:**

#### Part 1: Config Walkthrough (60 min)
1. Open existing config (10 min)
   - Navigate to `eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml`
   - Show file structure

2. Explain each section (40 min)
   - `description:` - What this eval is about
   - `prompts:` - The prompt template(s)
   - `providers:` - Which LLM(s) to test
   - `defaultTest:` - Shared settings
   - `tests:` - Individual test cases
   - `assertionTemplates:` - Reusable assertions

3. Key concepts (10 min)
   - Variables with `{{variable}}`
   - File references with `file://`
   - References with `$ref`

#### Part 2: Run First Evaluation (45 min)
1. Prepare environment (15 min)
   ```bash
   cd /path/to/project
   # Check .env file exists
   cat .env
   ```

2. Run evaluation (15 min)
   ```bash
   promptfoo eval --config eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml
   ```

3. View results (15 min)
   - Results open in browser automatically
   - Explore the UI
   - Look at pass/fail scores
   - Check provider responses

#### Part 3: Simple Modifications (45 min)
1. Add new test case (20 min)
   ```yaml
   tests:
     # ... existing tests ...
     - vars:
         question: "My new test question"
       assert:
         - type: contains
           value: "expected answer"
   ```

2. Run again (10 min)
   - Save file
   - Run eval command
   - See new test in results

3. Debug issues (15 min)
   - YAML errors
   - Missing values
   - Failed assertions

**Key Learning Points:**
- Small changes → immediate feedback
- Results show what passed/failed
- Can see actual LLM responses

**Homework:**
- Review config file
- Identify all test cases
- Note questions you'd like to add

---

### Session 4: Creating New Tests (3-4 hours)

**Goals:**
- Write test cases independently
- Use different assertion types
- Organize tests effectively

**Agenda:**

#### Part 1: Test Case Patterns (45 min)
1. Basic test structure (15 min)
   ```yaml
   - vars:
       question: "..."
     assert:
       - type: ...
         value: "..."
   ```

2. Common patterns (30 min)
   - Simple contains/icontains
   - Multiple assertions
   - Metadata for organization
   - Descriptions

#### Part 2: Assertion Types (60 min)
1. String assertions (20 min)
   - `contains` / `icontains`
   - `contains-any` / `contains-all`
   - `regex`

2. LLM assertions (20 min)
   - `llm-rubric`
   - How to write good rubrics
   - Using Danish language

3. Custom assertions (20 min)
   - Python assertions
   - How to call them
   - Configuration options

#### Part 3: Hands-on Practice (60 min)
1. Create 5-10 test cases (30 min)
   - Based on real questions
   - Mix of assertion types
   - Add metadata

2. Run and review (20 min)
   - Execute eval
   - Check results
   - Adjust assertions

3. Debug together (10 min)
   - Fix any issues
   - Learn from mistakes

**Exercise:**
Create tests for these scenarios:
1. Question that should be refused
2. Question with specific date answer
3. Question requiring document retrieval
4. Question with yes/no answer
5. Complex question with multiple requirements

**Homework:**
- Complete 10 test cases
- Use at least 3 different assertion types
- Run eval and review results

---

## Phase 3: Working Independently (4-6 hours)

### Session 5: Advanced Patterns (2-3 hours)

**Goals:**
- Use defaultTest effectively
- Organize tests across files
- Understand transforms

**Agenda:**

#### Part 1: Reusability (45 min)
1. defaultTest (25 min)
   - Set common assertions
   - Set common provider
   - Override per test

2. assertionTemplates (20 min)
   - Create templates
   - Reference with $ref
   - DRY principle

#### Part 2: Organization (45 min)
1. Multiple test files (20 min)
   ```yaml
   tests:
     - file://tests/basic.yaml
     - file://tests/advanced.yaml
   ```

2. Directory structure (15 min)
   ```
   eval-configs/
   └── my-use-case/
       ├── promptfooconfig.yaml
       ├── tests/
       │   ├── basic.yaml
       │   └── advanced.yaml
       └── prompts/
   ```

3. CSV option (10 min)
   - When to use
   - Basic format
   - Limitations

#### Part 3: Transforms (30 min)
1. What are transforms? (10 min)
   - Modify output before assertion
   - Extract specific parts

2. Common transforms (20 min)
   - `output.text` - Just the answer
   - `output.sources.map(...)` - Extract sources
   - Understanding the structure

**Homework:**
- Refactor existing tests to use defaultTest
- Create assertion templates
- Organize tests into separate files

---

### Session 6: Troubleshooting & Best Practices (2-3 hours)

**Goals:**
- Diagnose common issues
- Follow best practices
- Create personal cheat sheet

**Agenda:**

#### Part 1: Common Errors (60 min)
1. YAML errors (20 min)
   - Indentation issues
   - Missing colons
   - Invalid characters
   - How to read error messages

2. Config errors (20 min)
   - Missing required fields
   - Invalid provider config
   - File path issues

3. Runtime errors (20 min)
   - Environment variables
   - API connection issues
   - Provider timeouts

#### Part 2: Debugging Strategy (30 min)
1. Step-by-step approach (15 min)
   - Check YAML validation first
   - Verify file paths
   - Check environment variables
   - Run with --verbose
   - Check logs

2. Common fixes (15 min)
   - Format document
   - Check quotes
   - Verify paths are absolute
   - Restart terminal

#### Part 3: Best Practices (30 min)
1. Config organization (10 min)
   - Clear descriptions
   - Logical test grouping
   - Consistent naming

2. Test design (10 min)
   - One thing per test
   - Clear expected outcomes
   - Good metadata

3. Documentation (10 min)
   - Comments in YAML
   - README for eval configs
   - Notes on tricky assertions

**Create Your Cheat Sheet:**
Together, create a personalized reference document with:
- Your most-used assertion types
- Common commands
- Troubleshooting checklist
- Contact info for help

**Homework:**
- Review and refine your cheat sheet
- Practice debugging without help
- Document any issues you encounter

---

## Phase 4: Self-Study & Practice (4-6 hours)

### Homework Assignments

#### Assignment 1: Complete Eval Config (2 hours)
**Task:** Create a complete evaluation config for a new use case

**Requirements:**
- At least 15 test cases
- 3+ different assertion types
- Use defaultTest for common settings
- Use assertionTemplates
- Organize tests logically
- Add metadata to all tests

**Deliverable:**
- Working promptfooconfig.yaml
- Run successfully
- All tests produce results

#### Assignment 2: Modify Existing Tests (1 hour)
**Task:** Update existing tests based on feedback

**Requirements:**
- Review results from Session 4
- Identify failing tests
- Adjust assertions or rubrics
- Re-run and verify

**Deliverable:**
- Updated config file
- Summary of changes made

#### Assignment 3: Git Workflow Practice (1 hour)
**Task:** Practice complete Git workflow

**Requirements:**
1. Create new branch
   ```bash
   git checkout -b feature/new-tests
   ```

2. Make changes
   - Add new tests
   - Modify existing

3. Commit
   ```bash
   git add .
   git commit -m "Add new test cases for X"
   ```

4. Push (if remote available)
   ```bash
   git push -u origin feature/new-tests
   ```

**Deliverable:**
- Branch with committed changes
- (Optional) Pull request

#### Assignment 4: Results Analysis (1-2 hours)
**Task:** Review and interpret evaluation results

**Requirements:**
- Run full evaluation suite
- Identify patterns in failures
- Note which assertions are too strict/too loose
- Suggest improvements

**Deliverable:**
- Notes on result patterns
- List of suggested improvements

---

## Follow-up Session (Optional, 1-2 hours)

**When:** After completing all homework

**Agenda:**
1. Review homework (30 min)
   - Discuss challenges
   - Review completed configs
   - Answer questions

2. Q&A (30 min)
   - Open discussion
   - Troubleshoot issues
   - Share tips

3. Next steps (30 min)
   - Plan ongoing work
   - Identify areas for improvement
   - Set up regular check-ins

---

## Training Materials

All materials available in this directory:
- [README.md](./README.md) - Overview
- [SETUP.md](./SETUP.md) - Installation guide
- [YAML-CHEATSHEET.md](./YAML-CHEATSHEET.md) - YAML reference
- [VSCODE-SETUP.md](./VSCODE-SETUP.md) - VSCode configuration
- [GIT-WORKFLOW.md](./GIT-WORKFLOW.md) - Git guide
- [PROMPTFOO-BASICS.md](./PROMPTFOO-BASICS.md) - Promptfoo concepts

---

## Success Metrics

After training, you should be able to:

✅ **Setup:** Install and configure all tools independently  
✅ **YAML:** Create and edit YAML files without errors  
✅ **Config:** Write complete promptfoo configs  
✅ **Tests:** Create test cases with appropriate assertions  
✅ **Run:** Execute evaluations and view results  
✅ **Debug:** Troubleshoot common issues  
✅ **Git:** Manage work with version control  
✅ **Independent:** Work without constant help  

---

## Notes for Instructor

**Flexibility:**
- Adjust pace based on comfort level
- Spend more time on challenging topics
- Skip sections if already familiar

**Hands-on:**
- Let trainee type, not watch
- Provide examples, but have them implement
- Encourage experimentation

**Documentation:**
- Take notes on what was covered
- Track questions for follow-up
- Update materials based on feedback

**Follow-up:**
- Schedule check-in after 1 week
- Available for questions via email/chat
- Review first independent work

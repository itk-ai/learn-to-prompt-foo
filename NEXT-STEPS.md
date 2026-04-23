# Next Steps - Training Plan

## Completed

✅ **README.md** - Updated with lean structure  
✅ **SETUP.md** - Simplified installation guide  
✅ **GETTING-STARTED.md** - Session 2 (fixed to follow official example pattern)

## Next: Create Remaining Session Guides

### Session 3: PROMPTFOO-EVALUATIONS.md (Already exists - needs review)
**Goal:** Walk through MBU evaluation config
**Content needed:**
- Load existing MBU config from prompfoo-docker repo
- Explain each section (prompts, providers, defaultTest, tests, assertionTemplates)
- Run the MBU evaluation
- Add a simple test case
- Run again and see results
- add a note somewhere that a list of "models" available can be seen at https://stgai.itkdev.dk/api/v1/models/list

### Session 4: BIAS-CHECKER.md (Needs to be created)
**Goal:** Create tests for Anne Vibekes Bias-checker
**Content needed:**
- Explain what the Bias-checker does
- Create new promptfooconfig for this use case
- Design test cases (what to test, what assertions to use)
- Run evaluation and interpret results

### Session 5: GIT-CONTRIBUTION.md (Optional - Needs to be created)
**Goal:** Use Git to contribute to common promptfoo instance
**Content needed:**
- Clone prompfoo-docker repo
- Create branch
- Add your eval config
- Commit and push
- Create Pull Request

### Session 6: MERGE-AND-DEPLOY.md (Needs clarification)
**Goal:** Understanding how contributions get merged
**Content needed:**
- TBD (need to understand the deployment process)

### Bonus: OPENCODE-SETUP.md (Needs to be created)
**Goal:** Set up Opencode agent in VSCode
**Content needed:**
- Install Opencode extension
- Configure for promptfoo work
- Basic usage examples

## Files to Review/Update

### PROMPTFOO-EVALUATIONS.md (Exists - needs review)
Read and check if it aligns with the new lean approach

### EXAMPLES.md (Exists - keep as reference)
Contains real MBU patterns - keep for reference

### STARTER-TEMPLATE.md (Exists - simplify)
Can be simplified to just a copy-paste template

### QUICK-REFERENCE.md (Exists - keep)
One-page cheat sheet - keep as is

### YAML-CHEATSHEET.md (Exists - keep)
YAML syntax reference - keep as is

### VSCODE-SETUP.md (Exists - may need simplification)
Check if too detailed

### GIT-WORKFLOW.md (Exists - may need simplification)
Check if too detailed

## Immediate Actions

1. **Review PROMPTFOO-EVALUATIONS.md** - Does it follow the lean approach?
2. **Create BIAS-CHECKER.md** - Session 4 content
3. **Simplify remaining docs** - Remove instructor notes, trim excess
4. **Create OPENCODE-SETUP.md** - Bonus session

## Questions to Clarify

1. What is the actual deployment process for promptfoo-docker?
2. What does Session 6 ("contribute with tests to our common promptfoo instance") actually involve?
3. Do we need both PROMPTFOO-EVALUATIONS.md and EXAMPLES.md, or can we merge them?

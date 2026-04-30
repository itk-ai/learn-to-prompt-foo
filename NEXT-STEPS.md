# Next Steps - Training Plan

## Completed

✅ **README.md** - Updated with lean structure  
✅ **SETUP.md** - Simplified installation guide  
✅ **GETTING-STARTED.md** - Session 2  
✅ **PROMPTFOO-EVALUATIONS.md** - Session 3 (FINAL)  
✅ **ASSERTIONS-REFERENCE.md** - Session 3 reference (FINAL)  

## Next: Create Remaining Session Guides

### Content Strategy

- All guides should be short and to the point
- Remove all "trainer instructions" like "watch for", "helpful hints", "success indicators"
- Focus on what the trainee needs to do
- Use actual examples from MBU and Bias-checker configs

### Session 4: BIAS-CHECKER.md (Needs to be created)
**Goal:** Create tests for Anne Vibekes Bias-checker from scratch

**Trainee will:**
- Learn what the Bias-checker does (system prompt explanation)
- Create a new promptfooconfig using STARTER-TEMPLATE.md
- Design test cases based on the Bias-checker's purpose
- Run evaluation and interpret results

**Before creating:** Ask user for the exact system prompt and formulate exercises to help trainees investigate usage patterns and create meaningful test cases.

**Key references:**
- Model info: https://stgai.itkdev.dk/api/v1/models/model?id=ba-biastjekker-gpt120b
- STARTER-TEMPLATE.md for config structure
- PROMPTFOO-EVALUATIONS.md for patterns

### Session 5: GIT-SETUP.md (Optional - Needs to be created)
**Goal:** Setup Git for VSCode integration

**Trainee will:**
- Install git (refer to SETUP-OPTIONAL.md)
- Configure GitHub account
- Use Git functionality in VSCode

### Session 6: CONTRIBUTE.md (Optional - Needs to be created)
**Goal:** Contribute eval configs to prompfoo-docker repo via Git

**Trainee will:**
- Clone prompfoo-docker repo
- Create branch
- Add eval config (e.g., from Session 4 Bias-checker)
- Commit and push
- Create Pull Request

### Bonus: OPENCODE-SETUP.md (Needs to be created)
**Goal:** Set up Opencode agent in VSCode

**Trainee will:**
- Install Opencode extension
- Configure for promptfoo work
- Learn basic usage examples

## Files to Review/Update

### STARTER-TEMPLATE.md (Exists - simplify)
Simplify to a copy-paste template with minimal explanation

### QUICK-REFERENCE.md (Exists - keep)
One-page cheat sheet - keep as is

### YAML-CHEATSHEET.md (Exists - keep)
YAML syntax reference - Keep core syntax, remove practice exercises

### GIT-WORKFLOW.md (Exists - may need simplification)
Check if too detailed

## Immediate Actions

1. **Create BIAS-CHECKER.md** - Session 4 content (ask user for model system prompt first)
2. **Simplify remaining docs** - Remove instructor notes, trim excess
3. **Create OPENCODE-SETUP.md** - Bonus session


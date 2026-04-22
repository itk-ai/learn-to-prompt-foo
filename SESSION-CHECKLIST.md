# Session Checklist

Use this checklist during each training session.

## Pre-Session Preparation

### Before Session 1
- [ ] Trainee has Windows machine
- [ ] Trainee has admin rights (or PEDM access)
- [ ] Instructor has training materials ready
- [ ] Instructor has example project prepared
- [ ] Both have same time zone confirmed
- [ ] Meeting link/location set

### Before Each Session
- [ ] Instructor reviews agenda
- [ ] Trainee completes previous homework (if any)
- [ ] Both have VSCode ready
- [ ] Project files accessible
- [ ] Internet connection working

---

## Session 1: Installation & First Steps

### Setup (45 min)
- [ ] VSCode downloaded and installed
- [ ] VSCode launched successfully
- [ ] Node.js downloaded and installed
- [ ] Node.js verified (`node --version`)
- [ ] npm verified (`npm --version`)
- [ ] Git downloaded and installed
- [ ] Git configured (name, email)
- [ ] Git verified (`git --version`)

### VSCode Tour (30 min)
- [ ] Icon bar explained
- [ ] Explorer panel shown
- [ ] Editor area demonstrated
- [ ] Terminal opened
- [ ] Project folder opened
- [ ] Trust authors confirmed

### Extensions (15 min)
- [ ] YAML extension installed
- [ ] GitLens installed (optional)
- [ ] Prettier installed (optional)
- [ ] Extensions verified working

### Terminal Basics (15 min)
- [ ] Terminal opened (`Ctrl+``)
- [ ] First commands run:
  - [ ] `pwd` or `cd`
  - [ ] `ls`
  - [ ] `promptfoo --version`
- [ ] Commands executed successfully

### Session 1 Success Criteria
- [ ] All software installed
- [ ] VSCode working
- [ ] Terminal accessible
- [ ] Project folder open
- [ ] Questions answered

**Notes:**
```
_________________________________
_________________________________
_________________________________
```

---

## Session 2: YAML & Git Fundamentals

### YAML Basics (45 min)
- [ ] YAML concept explained
- [ ] Key-value pairs demonstrated
- [ ] Lists shown
- [ ] Nesting explained
- [ ] Indentation emphasized (spaces!)
- [ ] Comments shown
- [ ] Practice file created:
  - [ ] Simple key-values
  - [ ] List of items
  - [ ] Nested object
  - [ ] Multiline string
- [ ] YAML validated (no errors)

### Git Basics (45 min)
- [ ] Git concepts explained (repo, commit, branch)
- [ ] Source Control panel opened
- [ ] Changes visible
- [ ] File staged (+ icon)
- [ ] Commit message written
- [ ] Commit made (✓ icon)
- [ ] History viewed

### Combined Exercise (30 min)
- [ ] Test YAML file created
- [ ] File shows in Source Control
- [ ] Changes staged
- [ ] Commit message written
- [ ] Commit made
- [ ] History reviewed

### Session 2 Success Criteria
- [ ] Can create YAML file
- [ ] Understand indentation
- [ ] Can stage changes
- [ ] Can commit
- [ ] No YAML validation errors

**Notes:**
```
_________________________________
_________________________________
_________________________________
```

**Homework Assigned:**
- [ ] Practice YAML files (3-5)
- [ ] Practice commits

---

## Session 3: Understanding Config Structure

### Config Walkthrough (60 min)
- [ ] Open MBU config file
- [ ] `description` explained
- [ ] `prompts` section explained
- [ ] `providers` section explained
- [ ] `defaultTest` explained
- [ ] `tests` section explained
- [ ] `assertionTemplates` explained
- [ ] Variables (`{{question}}`) shown
- [ ] File references (`file://`) shown
- [ ] References (`$ref`) shown

### First Evaluation (45 min)
- [ ] Navigate to project folder
- [ ] Check `.env` file exists
- [ ] Run eval command:
  ```bash
  promptfoo eval --config eval-configs/MBU-Databeskyttelse/promptfooconfig.yaml
  ```
- [ ] Command executed
- [ ] Results open in browser
- [ ] Results UI explored
- [ ] Pass/fail scores shown
- [ ] Provider responses viewed

### Simple Modifications (45 min)
- [ ] New test case added
- [ ] File saved
- [ ] Eval run again
- [ ] New test visible in results
- [ ] Issues debugged (if any)

### Session 3 Success Criteria
- [ ] Understands config anatomy
- [ ] Can run evaluation
- [ ] Can view results
- [ ] Can add simple test
- [ ] See immediate feedback

**Notes:**
```
_________________________________
_________________________________
_________________________________
```

**Homework Assigned:**
- [ ] Review config file
- [ ] Identify test cases
- [ ] Note questions to add

---

## Session 4: Creating New Tests

### Test Patterns (45 min)
- [ ] Basic structure reviewed
- [ ] `vars` section shown
- [ ] `assert` section shown
- [ ] `metadata` shown
- [ ] `description` shown
- [ ] Practice creating test cases

### Assertion Types (60 min)
- [ ] `contains` / `icontains` demonstrated
- [ ] `contains-any` / `contains-all` shown
- [ ] `regex` pattern shown
- [ ] `llm-rubric` explained
- [ ] Custom Python assertions shown
- [ ] When to use each explained

### Hands-on Practice (60 min)
- [ ] Created 5-10 test cases
- [ ] Used multiple assertion types
- [ ] Added metadata
- [ ] Eval run
- [ ] Results reviewed
- [ ] Assertions adjusted
- [ ] Issues debugged

### Session 4 Success Criteria
- [ ] Can write test cases
- [ ] Knows assertion types
- [ ] Can run and review
- [ ] Can debug issues
- [ ] Working test suite

**Notes:**
```
_________________________________
_________________________________
_________________________________
```

**Homework Assigned:**
- [ ] Complete 10 test cases
- [ ] Use 3+ assertion types
- [ ] Run and review eval

---

## Session 5: Advanced Patterns

### Reusability (45 min)
- [ ] `defaultTest` reviewed
- [ ] Common settings shown
- [ ] Override per test shown
- [ ] `assertionTemplates` reviewed
- [ ] `$ref` usage shown
- [ ] DRY principle discussed

### Organization (45 min)
- [ ] Multiple test files shown
- [ ] Directory structure shown
- [ ] CSV option discussed
- [ ] When to use each explained

### Transforms (30 min)
- [ ] What transforms are
- [ ] `output.text` shown
- [ ] `output.sources` shown
- [ ] Why transforms needed
- [ ] Example demonstrated

### Session 5 Success Criteria
- [ ] Uses defaultTest
- [ ] Creates templates
- [ ] Understands transforms
- [ ] Organizes tests

**Notes:**
```
_________________________________
_________________________________
_________________________________
```

**Homework Assigned:**
- [ ] Refactor with defaultTest
- [ ] Create templates
- [ ] Organize into files

---

## Session 6: Troubleshooting & Best Practices

### Common Errors (60 min)
- [ ] YAML errors shown and fixed
- [ ] Config errors shown and fixed
- [ ] Runtime errors shown and fixed
- [ ] Error messages read and understood

### Debugging Strategy (30 min)
- [ ] Step-by-step approach shown
- [ ] YAML validation checked
- [ ] File paths verified
- [ ] Environment variables checked
- [ ] `--verbose` used
- [ ] Logs reviewed

### Best Practices (30 min)
- [ ] Config organization discussed
- [ ] Test design principles
- [ ] Documentation importance
- [ ] Cheat sheet created

### Session 6 Success Criteria
- [ ] Can debug independently
- [ ] Knows best practices
- [ ] Has personal cheat sheet
- [ ] Can troubleshoot

**Notes:**
```
_________________________________
_________________________________
_________________________________
```

---

## Homework Tracking

### Assignment 1: Complete Eval Config
**Due:** [Date]
- [ ] At least 15 test cases
- [ ] 3+ assertion types
- [ ] Uses defaultTest
- [ ] Uses templates
- [ ] Organized tests
- [ ] Has metadata
- [ ] Runs successfully

**Feedback:**
```
_________________________________
_________________________________
```

### Assignment 2: Modify Existing Tests
**Due:** [Date]
- [ ] Reviewed results
- [ ] Identified failures
- [ ] Adjusted assertions
- [ ] Re-run verified

**Feedback:**
```
_________________________________
_________________________________
```

### Assignment 3: Git Workflow
**Due:** [Date]
- [ ] Created branch
- [ ] Made changes
- [ ] Committed
- [ ] Pushed (if applicable)

**Feedback:**
```
_________________________________
_________________________________
```

### Assignment 4: Results Analysis
**Due:** [Date]
- [ ] Ran full eval
- [ ] Identified patterns
- [ ] Noted issues
- [ ] Suggested improvements

**Feedback:**
```
_________________________________
_________________________________
```

---

## Follow-up Session

**Date:** [Date]
**Duration:** 1-2 hours

### Review (30 min)
- [ ] Homework reviewed
- [ ] Challenges discussed
- [ ] Questions answered

### Q&A (30 min)
- [ ] Open discussion
- [ ] Issues troubleshooted
- [ ] Tips shared

### Next Steps (30 min)
- [ ] Ongoing work planned
- [ ] Improvements identified
- [ ] Check-ins scheduled

**Notes:**
```
_________________________________
_________________________________
_________________________________
```

---

## Overall Progress

| Session | Completed | Date | Notes |
|---------|-----------|------|-------|
| Session 1 | ☐ | ____ | _____ |
| Session 2 | ☐ | ____ | _____ |
| Session 3 | ☐ | ____ | _____ |
| Session 4 | ☐ | ____ | _____ |
| Session 5 | ☐ | ____ | _____ |
| Session 6 | ☐ | ____ | _____ |
| Follow-up | ☐ | ____ | _____ |

## Final Assessment

After all training:

- [ ] Can install tools independently
- [ ] Can create/edit YAML files
- [ ] Can write promptfoo configs
- [ ] Can run evaluations
- [ ] Can interpret results
- [ ] Can troubleshoot issues
- [ ] Can use Git workflow
- [ ] Works independently

**Training Completed:** ☐ Yes ☐ No  
**Date Completed:** ___________  
**Instructor:** ___________

**Final Notes:**
```
_________________________________
_________________________________
_________________________________
_________________________________
```

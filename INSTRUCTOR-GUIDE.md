# Instructor Guide

This guide is for the instructor (you) to manage the training process.

## Training Overview

**Trainee:** Non-technical user, Windows, very comfortable with new tools  
**Total Time:** 15-20 hours  
**Format:** In-person workshops + self-study  
**Goal:** Independent promptfoo config creation and evaluation execution

---

## Materials Created

All materials are in `/home/akda/git_repos/learn-to-prompt-foo/`:

### Core Documents
- **README.md** - Training overview and structure
- **SETUP.md** - Installation guide for trainee
- **VSCODE-SETUP.md** - VSCode configuration guide
- **YAML-CHEATSHEET.md** - YAML syntax reference
- **PROMPTFOO-BASICS.md** - Promptfoo concepts
- **GIT-WORKFLOW.md** - Git workflow guide

### Training Management
- **TRAINING-AGENDA.md** - Detailed session agendas
- **SESSION-CHECKLIST.md** - Progress tracking
- **INDEX.md** - Materials index for trainee

### Practical Resources
- **EXAMPLES.md** - Real-world examples from MBU use case
- **STARTER-TEMPLATE.md** - Copy-paste template
- **QUICK-REFERENCE.md** - One-page cheat sheet

---

## Recommended Training Schedule

### Option A: Intensive (1 week)
- **Day 1:** Session 1 + Session 2 (4-5 hours)
- **Day 2:** Session 3 + Session 4 (5-6 hours)
- **Day 3:** Session 5 + Session 6 (4-5 hours)
- **Days 4-5:** Homework + follow-up (4-6 hours)

### Option B: Spread Out (2-3 weeks)
- **Week 1:** Session 1 + Session 2 (2 sessions, 2-3 hours each)
- **Week 2:** Session 3 + Session 4 (2 sessions, 3-4 hours each)
- **Week 3:** Session 5 + Session 6 (2 sessions, 2-3 hours each)
- **Between sessions:** Homework assignments
- **End of Week 3:** Follow-up session

### Option C: Half-Day Workshops (Recommended)
- **Session 1:** 2.5 hours (Setup)
- **Session 2:** 2.5 hours (YAML + Git)
- **Session 3:** 3 hours (Config structure)
- **Session 4:** 3 hours (Creating tests)
- **Session 5:** 2.5 hours (Advanced patterns)
- **Session 6:** 2.5 hours (Troubleshooting)
- **Follow-up:** 1-2 hours (Q&A)
- **Homework:** 4-6 hours (self-paced)

---

## Pre-Training Checklist

### Before Training Starts
- [ ] Trainee has Windows machine with admin rights
- [ ] Trainee knows how to install software (or has PEDM access)
- [ ] All training materials accessible to trainee
- [ ] Example project ready (promptfoo-docker repo)
- [ ] Time slots scheduled
- [ ] Location/meeting link confirmed
- [ ] .env file with credentials ready (if needed for demos)

### Before Each Session
- [ ] Review session agenda
- [ ] Check homework completion (if applicable)
- [ ] Prepare any demo files
- [ ] Test commands you'll demonstrate
- [ ] Have troubleshooting tips ready

---

## Session Management Tips

### Session 1: Installation
**Watch for:**
- Installation permission issues (PEDM prompts)
- PATH problems (restart needed)
- Confusion about which terminal to use

**Helpful hints:**
- Have trainee do the clicking/typing, not you
- Take screenshots if they want to reference later
- Verify each installation before moving on

**Success indicators:**
- All three tools installed and verified
- VSCode opens project folder
- Terminal runs commands

### Session 2: YAML + Git
**Watch for:**
- Tab vs space confusion (critical!)
- Indentation errors
- Git commit message quality

**Helpful hints:**
- Show VSCode's "Spaces: 2" indicator
- Demonstrate Format Document feature
- Emphasize descriptive commit messages

**Success indicators:**
- YAML file validates (no errors)
- Can stage and commit changes
- Understands indentation importance

### Session 3: Config Structure
**Watch for:**
- Overwhelmed by config complexity
- Confusion about providers vs providers
- Not understanding transforms

**Helpful hints:**
- Use the MBU config as living example
- Point to specific lines as you explain
- Run a small eval early for quick win

**Success indicators:**
- Can explain each config section
- Successfully runs first eval
- Can add simple test case

### Session 4: Creating Tests
**Watch for:**
- Writing overly complex tests
- Using wrong assertion types
- Not testing realistic scenarios

**Helpful hints:**
- Start with 1-2 simple tests, build up
- Refer to EXAMPLES.md for patterns
- Review real questions from MBU

**Success indicators:**
- Creates 5-10 working test cases
- Uses multiple assertion types
- Can debug failed assertions

### Session 5: Advanced Patterns
**Watch for:**
- Overusing defaultTest
- Confusion about when to use templates
- Transform syntax errors

**Helpful hints:**
- Show before/after refactoring
- Explain DRY principle
- Use output.sources examples

**Success indicators:**
- Refactors tests with defaultTest
- Creates useful templates
- Understands transform use cases

### Session 6: Troubleshooting
**Watch for:**
- Giving up too quickly
- Not reading error messages
- Not using debugging tools

**Helpful hints:**
- Show your debugging process
- Demonstrate --verbose flag
- Create troubleshooting checklist together

**Success indicators:**
- Can debug YAML errors
- Knows where to look for help
- Has personal cheat sheet

---

## Homework Management

### Assignment 1: Complete Eval Config
**Expected time:** 2 hours  
**Deliverable:** Working config with 15+ tests  
**Review checklist:**
- [ ] 15+ test cases
- [ ] 3+ assertion types
- [ ] Uses defaultTest
- [ ] Has metadata
- [ ] Runs without errors
- [ ] Readable formatting

**Common issues:**
- Too many tests in one file (suggest splitting)
- Missing metadata (remind importance)
- Copy-paste errors (show find/replace)

### Assignment 2: Modify Existing Tests
**Expected time:** 1 hour  
**Deliverable:** Updated tests with summary  
**Review checklist:**
- [ ] Identified failing tests
- [ ] Adjusted appropriately
- [ ] Re-run verified
- [ ] Documented changes

**Common issues:**
- Giving up on failing tests
- Making tests too loose
- Not understanding why tests fail

### Assignment 3: Git Workflow
**Expected time:** 1 hour  
**Deliverable:** Branch with commits  
**Review checklist:**
- [ ] Created branch
- [ ] Made changes
- [ ] Committed with messages
- [ ] Pushed (if applicable)

**Common issues:**
- Commit messages too vague
- Forgetting to stage files
- Branch naming confusion

### Assignment 4: Results Analysis
**Expected time:** 1-2 hours  
**Deliverable:** Analysis notes  
**Review checklist:**
- [ ] Ran full eval
- [ ] Identified patterns
- [ ] Noted issues
- [ ] Suggested improvements

**Common issues:**
- Surface-level analysis
- Not identifying root causes
- No actionable suggestions

---

## Assessment Criteria

### Technical Skills
| Skill | Beginner | Intermediate | Advanced |
|-------|----------|--------------|----------|
| YAML | Can create basic files | Understands nesting | Uses advanced patterns |
| VSCode | Can open files | Uses extensions | Efficient shortcuts |
| Git | Can commit changes | Uses branches | Understands workflow |
| Promptfoo | Can run evals | Writes tests | Optimizes configs |
| Assertions | Uses basic types | Mixes types | Creates custom |
| Debugging | Asks for help | Reads errors | Diagnoses independently |

### Independence Indicators
✅ Can install tools without help  
✅ Can create YAML files without errors  
✅ Can write test cases independently  
✅ Can run and interpret evals  
✅ Can debug common issues  
✅ Uses Git workflow consistently  
✅ References materials when stuck  

### Ready for Independence (All of these)
- [ ] Completed all homework successfully
- [ ] Can explain config structure
- [ ] Has created 20+ test cases
- [ ] Debugs without immediate help
- [ ] Uses cheat sheets appropriately
- [ ] Asks specific (not vague) questions

---

## Common Challenges & Solutions

### Challenge: YAML Indentation
**Problem:** Trainee uses tabs or inconsistent spaces  
**Solution:**
- Show VSCode settings
- Enable "Format On Save"
- Use YAML extension validation
- Practice with simple files first

### Challenge: Overwhelmed by Config
**Problem:** Too many concepts at once  
**Solution:**
- Start with minimal config
- Add one section at a time
- Use starter template
- Refer to examples

### Challenge: Vague Questions
**Problem:** "It doesn't work" without details  
**Solution:**
- Teach debugging steps
- Ask "What did you try?"
- Show error message reading
- Demonstrate --verbose

### Challenge: Git Fear
**Problem:** Afraid to break things  
**Solution:**
- Explain Git safety
- Show undo operations
- Use branches for experiments
- Practice small commits

### Challenge: Assertion Selection
**Problem:** Doesn't know which assertion to use  
**Solution:**
- Provide decision tree
- Use EXAMPLES.md heavily
- Start simple, add complexity
- Review together initially

---

## Follow-Up Support

### After Training Ends
**Recommended check-ins:**
- 1 week after: Quick check-in (15 min)
- 1 month after: Progress review (30 min)
- As needed: Issue-specific help

**Support channels:**
- Email for questions
- Quick chat for debugging
- Code review for complex configs

**When to step in:**
- Repeated failures causing frustration
- Wrong patterns becoming habits
- Security issues (secrets in configs)
- Major rework needed

---

## Customization Notes

### If Trainee is Slower
- Extend session duration
- Reduce homework load
- Add more practice sessions
- Focus on essentials first

### If Trainee is Faster
- Add advanced topics
- More complex examples
- Custom assertion development
- Performance optimization

### If Using Different Use Case
- Update EXAMPLES.md with relevant examples
- Adjust STARTER-TEMPLATE.md accordingly
- Modify assertions to match domain
- Keep structure, change content

---

## Success Metrics

### Training Success
- ✅ All sessions completed
- ✅ All homework submitted
- ✅ Trainee can work independently
- ✅ Quality configs produced
- ✅ Positive trainee feedback

### Long-term Success (1-3 months)
- ✅ Regular eval creation
- ✅ Independent troubleshooting
- ✅ Contributing to team configs
- ✅ Following best practices
- ✅ Mentoring others (optional)

---

## Notes Section

Use this space for session-specific notes:

### Session 1 Notes
```
_________________________________
_________________________________
_________________________________
```

### Session 2 Notes
```
_________________________________
_________________________________
_________________________________
```

### Session 3 Notes
```
_________________________________
_________________________________
_________________________________
```

### Session 4 Notes
```
_________________________________
_________________________________
_________________________________
```

### Session 5 Notes
```
_________________________________
_________________________________
_________________________________
```

### Session 6 Notes
```
_________________________________
_________________________________
_________________________________
```

### Overall Observations
```
_________________________________
_________________________________
_________________________________
_________________________________
```

### Recommendations for Future Training
```
_________________________________
_________________________________
_________________________________
_________________________________
```

---

## Materials Updates

If you make changes to materials during training:
1. Note what changed and why
2. Update relevant files
3. Tell trainee where to find updated version
4. Consider if change should be permanent

**Change Log:**
```
Date: ____  Change: _______________________________
Date: ____  Change: _______________________________
Date: ____  Change: _______________________________
```

---

**Good luck with the training! Remember: patience, practice, and positive reinforcement are key.**

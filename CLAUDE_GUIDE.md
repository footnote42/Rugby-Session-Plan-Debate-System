# Claude Code Behavioral Guide

**CRITICAL: Read this file first before executing any stage from PROJECT_PLAN.md**

---

## Core Operating Principles

### 1. Explicit Confirmation Required
- **NEVER** advance to the next stage without explicit user instruction
- **NEVER** modify code without explicit permission
- **ALWAYS** wait for user confirmation after summarizing your understanding
- If uncertain about any instruction, **ASK** before proceeding

### 2. Stage-by-Stage Execution
- Only execute the stage number explicitly requested
- Ignore all other stages in PROJECT_PLAN.md
- Complete one stage fully before considering the next
- Each stage must produce working, testable code

### 3. Communication Pattern

**Before Starting:**
```
I understand Stage [N] requires:
- Objective: [brief summary]
- Inputs: [list key inputs]
- Outputs: [expected deliverables]
- Questions: [any clarifications needed]

Ready to proceed? Please confirm.
```

**After Completing:**
```
Stage [N] Complete:
- Changed: [summary of modifications]
- Files: [list of files created/modified]
- Testing: [how to verify it works]
- Next: [what comes next, but don't do it]

Awaiting further instructions.
```

---

## File Structure Conventions

### Repository Layout
```
rugby-debate-system/
├── src/                    # All implementation code
│   ├── app.py             # Main application (Flask/FastAPI)
│   ├── prompts.py         # Prompt templates
│   ├── judge.py           # Judging logic
│   ├── debate.py          # Debate orchestration
│   └── utils.py           # Helper functions
├── context/               # Domain knowledge (read-only for you)
│   ├── trojans_framework.md
│   ├── coaching_philosophies.md
│   ├── scoring_rubric.md
│   └── judge_prompts.md
├── templates/             # HTML templates (if using Flask)
│   ├── index.html
│   ├── compare.html
│   └── debate.html
├── static/                # CSS, JavaScript
│   └── styles.css
├── tests/                 # Test files
│   └── test_prompts.py
├── docs/                  # Generated documentation
├── .env.example           # API key template
├── requirements.txt       # Python dependencies
├── README.md              # User-facing documentation
├── PROJECT_PLAN.md        # Your execution plan
├── CLAUDE_GUIDE.md        # This file
├── REQUIREMENTS.md        # Project requirements
└── CHECKLIST.md           # Human progress tracker
```

### File Modification Rules
- **Context files**: READ ONLY - never modify
- **Src files**: Modify only when instructed for current stage
- **Tests**: Add/modify when implementing features
- **Docs**: Update after completing stages
- **PROJECT_PLAN.md**: NEVER modify - this is immutable

---

## Code Quality Standards

### Python Code
- Use type hints where possible: `def generate_plan(objective: str) -> dict:`
- Include docstrings for all functions
- Handle errors explicitly with try/except
- Use meaningful variable names
- Keep functions focused and testable

### API Interaction
- Always use environment variables for API keys
- Include timeout parameters: `timeout=30`
- Implement retry logic with exponential backoff
- Log all API calls for debugging
- Track token usage for cost awareness

### Error Handling Pattern
```python
try:
    response = client.messages.create(...)
    if response.content:
        return response.content[0].text
    else:
        return "No response received"
except anthropic.APIError as e:
    logger.error(f"API error: {e}")
    return None
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    return None
```

---

## Testing Requirements

### After Each Stage
1. **Manual Testing**: Run the application and test with real inputs
2. **Edge Cases**: Test with empty inputs, very long inputs, special characters
3. **Error Scenarios**: Test with invalid API key, network issues, timeout
4. **Documentation**: Update README with new functionality

### Test Objectives to Use
- "Improve passing under pressure" (standard objective)
- "Support play in attack" (game-based focus)
- "Tackle technique" (contact skills)
- "Decision making at breakdown" (complex scenario)
- Empty string (error handling)

---

## Prompt Engineering Guidelines

### Structure Every Prompt With:
1. **Role definition**: "You are a rugby coach..."
2. **Context**: Age group, objective, constraints
3. **Task**: What to generate/evaluate
4. **Format**: Specific output structure
5. **Examples**: If helpful for clarity
6. **Constraints**: Word limits, required elements
7. **Terminator**: "End with: WINNER: X" for judge prompts

### Token Management
- Keep prompts focused and concise
- Use abbreviations in system prompts where clear
- Limit rebuttal length: max 100 words
- Monitor total context length
- Target: <4000 tokens per API call for safety

### Format Requirements for Judge
```
CRITICAL: Your response MUST end with exactly one line:
WINNER: A
or
WINNER: B

Do not add anything after this line.
```

---

## Debugging Approach

### When Something Fails

1. **Isolate the Problem**
   - Does API call work in isolation?
   - Is prompt well-formed?
   - Is parsing logic sound?

2. **Add Logging**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   logger = logging.getLogger(__name__)
   
   logger.debug(f"Prompt length: {len(prompt)}")
   logger.debug(f"Response received: {response[:100]}")
   ```

3. **Test Components Separately**
   - Test prompt generation without API call
   - Test parsing with sample responses
   - Test API with minimal prompt

4. **Document Findings**
   - Add notes to LEARNING_LOG.md
   - Update TROUBLESHOOTING.md if needed
   - Share insights with user

---

## Learning Documentation

### After Each Stage, Document:
1. **What worked well**: Successful patterns, good decisions
2. **What was challenging**: Problems encountered, solutions tried
3. **Key insights**: Understanding gained about orchestration
4. **Code patterns**: Reusable approaches discovered
5. **Improvements**: What you'd do differently next time

### Add to LEARNING_LOG.md
```markdown
## Stage [N] - [Name]

### What I Built
[Brief description]

### Technical Learnings
- [Insight 1]
- [Insight 2]

### Surprises
- [Unexpected outcome]

### Would Do Differently
- [Alternative approach]
```

---

## Common Pitfalls to Avoid

### Don't:
- ❌ Advance stages without explicit instruction
- ❌ Modify PROJECT_PLAN.md structure
- ❌ Hardcode API keys in source code
- ❌ Create overly complex solutions
- ❌ Skip error handling
- ❌ Forget to test edge cases
- ❌ Leave code uncommented
- ❌ Modify context files

### Do:
- ✅ Ask clarifying questions when uncertain
- ✅ Test thoroughly after each change
- ✅ Keep code modular and focused
- ✅ Document decisions and learnings
- ✅ Handle errors gracefully
- ✅ Use type hints and docstrings
- ✅ Commit working code after each stage
- ✅ Update documentation as you go

---

## User Interaction Patterns

### Typical Instructions You'll Receive

**Starting a stage:**
```
"Begin Stage 1"
"Start Stage 2 from PROJECT_PLAN.md"
"Proceed with Stage 3"
```

**Requesting clarification:**
```
"Review Stage 4 but don't implement yet"
"Summarize what Stage 5 requires"
"What questions do you have about Stage 6?"
```

**Modifying approach:**
```
"Use Flask instead of FastAPI for Stage 1"
"Skip the debate functionality in Stage 5"
"Add logging to the judge function"
```

**Completing work:**
```
"Stage complete, move to next"
"That works, proceed to Stage 7"
"Good, now do Stage 8"
```

### Your Response Pattern

Always structure responses as:
1. **Acknowledgment**: "I'll [action] for Stage [N]"
2. **Understanding**: Summarize requirements
3. **Questions**: Any clarifications needed
4. **Confirmation**: "Ready to proceed?"
5. **Execution**: Only after explicit "yes"
6. **Summary**: What was done
7. **Next**: What comes next (but don't do it)

---

## Special Considerations for This Project

### Learning vs. Production
This is a **learning project**, not production software. Prioritize:
- Clear, readable code over optimization
- Working examples over comprehensive features
- Documentation of insights over perfection
- Incremental progress over complete solutions

### Rugby Domain Knowledge
The user (Wayne) is the domain expert. When uncertain about:
- Coaching terminology
- Age-appropriate activities
- RFU regulations
- Trojans framework specifics

**Ask the user** rather than making assumptions.

### Cost Awareness
Each API call costs money. Help the user track costs by:
- Logging token counts
- Summarizing API usage after each stage
- Suggesting ways to reduce calls during testing
- Mentioning approximate costs in stage summaries

### Anthropic API Specifics
- Model: `claude-sonnet-4-20250514`
- Max tokens: 1500 for generation, 1000 for judge, 200 for rebuttals
- Timeout: 30 seconds
- Rate limits: ~50 requests/minute on standard tier

---

## Final Reminders

### Before Every Stage:
1. Read the stage requirements carefully
2. Check context files for relevant domain knowledge
3. Review previous stage code to understand state
4. Summarize understanding and get confirmation
5. Only then proceed with implementation

### During Every Stage:
1. Write clear, well-commented code
2. Test as you build
3. Handle errors appropriately
4. Keep user informed of progress
5. Stop and ask if anything is unclear

### After Every Stage:
1. Test thoroughly with multiple scenarios
2. Document what was learned
3. Summarize changes made
4. Suggest what to test before proceeding
5. Wait for next instruction

---

## Contact Pattern

If you encounter anything that seems ambiguous, contradictory, or unclear:

**Stop and say:**
```
I've identified a potential issue with [description].

Before proceeding, I want to clarify:
[Specific question 1]
[Specific question 2]

Shall I:
A) [Option 1]
B) [Option 2]
C) Wait for further guidance
```

Never guess or assume when the path forward is unclear.

---

**Remember:** Your role is to help the user learn AI orchestration patterns through building a practical tool. The journey matters more than the destination. Focus on clear communication, working code, and documented insights.

---

*Last Updated: December 12, 2025*
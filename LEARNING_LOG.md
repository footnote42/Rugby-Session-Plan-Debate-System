# Learning Log - Rugby Session Plan Debate System

**Project:** Rugby Session Plan Debate System
**Developer:** Wayne
**Started:** December 12, 2025
**Purpose:** Learn AI orchestration patterns through practical implementation

---

## Overview

This log captures insights, learnings, and discoveries from each development stage. The goal is to document not just what was built, but what was learned about AI orchestration, prompt engineering, and system architecture.

---

## Stage 0 — Environment Validation

**Date:** December 12, 2025
**Status:** Complete

### What I Built
- Repository structure validation
- Python and Node.js environment verification
- Dependency files (requirements.txt, .env.example, .env)
- Documentation templates (this file)

### Technical Learnings
- Confirmed dual environment setup (Python for AI orchestration, Node.js for existing scaffold)
- Python 3.14.0 and Node.js v22.20.0 both available
- Need to install: anthropic, flask, python-dotenv packages

### Setup Notes
- Created requirements.txt with Anthropic SDK, Flask, python-dotenv
- Created .env.example template for API configuration
- Created .env file (awaiting API key)
- LEARNING_LOG.md created for ongoing documentation

### Next Steps
- Obtain Anthropic API key from https://console.anthropic.com/settings/keys
- Add API key to .env file
- Install Python packages: `pip install -r requirements.txt`
- Proceed to Stage 1: Single Coach Generator

### Time Spent
~30 minutes (environment validation and setup file creation)

### Questions/Reflections
- Repository has both Python (for AI) and Node.js (existing scaffold) - will focus on Python for core functionality
- Decision: Using Flask over FastAPI for simplicity
- Budget awareness: £2-3 total for all API experimentation

---

## Stage 1 — Single Coach Generator

**Date:** December 12, 2025
**Status:** Complete ✅

### What I Built
- Flask web application with Claude API integration
- `src/app.py` - Main Flask app with routes, error handling, API calls
- `src/prompts.py` - Base session prompt template function
- `templates/index.html` - Form for session inputs (age, objective, duration, players)
- `templates/result.html` - Display generated session plan with token tracking
- Basic folder structure (src/, templates/, static/)

### Technical Learnings
**First API call to Claude:**
- Anthropic Python SDK is straightforward and well-documented
- API key configuration via .env works cleanly with python-dotenv
- Response structure: `response.content[0].text` for the generated content
- Token tracking available via `response.usage.input_tokens` and `output_tokens`

**Prompt structure:**
- Simple, direct prompt works well for session generation
- Clear structure (warm-up, main activities, cool-down) produces organized output
- Specifying format requirements ("clear sections with headings") helps structure

**Error handling:**
- Flask flash messages provide good user feedback
- Separate handling for APIError vs general exceptions
- Input validation prevents bad API calls (saves tokens/cost)
- Logging at INFO level provides good debugging trail

**Template folder path issue:**
- Flask looks for templates relative to the app file location
- Fixed by explicitly setting template_folder and static_folder to project root
- Important for multi-file project structures

### Surprises
- Claude generates very high-quality, coaching-usable session plans immediately
- No need for extensive prompt engineering - simple prompt works well
- Token usage is reasonable (~200-300 input, ~800-1200 output per plan)
- Flask debug mode auto-reload works well for rapid development

### Code Patterns Discovered
**Reusable API call pattern:**
```python
response = client.messages.create(
    model=MODEL,
    max_tokens=MAX_TOKENS,
    messages=[{"role": "user", "content": prompt}]
)
session_plan = response.content[0].text
```

**Form validation pattern:**
- Validate all inputs before API call
- Return user-friendly error messages with flash()
- Redirect back to form on error (preserves user context)

**Template folder configuration:**
```python
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
app = Flask(__name__, template_folder=template_dir)
```

### Would Do Differently
- Minor UI/appearance improvements (but not needed for Stage 1)
- Could add session plan preview before full generation
- Consider caching recent plans to avoid duplicate API calls during testing

### Time Spent
~1.5 hours (including environment setup, implementation, debugging template path issue)

### API Cost
~£0.05 (estimate based on token usage: ~1000 tokens total per test, 3-4 test calls)

### Test Results
**Objectives Tested:**
- [x] "Improve passing under pressure" (U10, 60min, 16 players)

**Quality Assessment:**
- Coherence: 9/10 - Well-structured, logical flow
- Coaching usability: 8/10 - Directly usable for real coaching session
- Age-appropriateness: 9/10 - Activities suitable for U10 age group

**Notes:**
- Plan includes warm-up, main activities, cool-down as required
- Coaching points are clear and age-appropriate (max 3 per activity)
- Safety considerations included
- Minor appearance concerns noted but content is sound

---

## Stage 2 — Dual Coach Generation

**Date:** ___
**Status:** Not Started

### What I Built
*To be filled after completion*

### Technical Learnings
*Document insights about:*
- Parallel API calls
- Distinct system prompts for different personas
- Maintaining philosophical consistency
- Comparison display patterns

### Philosophical Difference Quality
*How distinct were the approaches?*
- Game-based vs. structured clarity: ___/10
- Activity type differences: Notable / Subtle / Not clear
- Coaching point style differences: Notable / Subtle / Not clear

### Code Patterns Discovered
*Reusable orchestration patterns*

### Time Spent
___ hours

### API Cost
£___

---

## Stage 3 — Heuristic Judge

**Date:** ___
**Status:** Not Started

### What I Built
*To be filled after completion*

### Technical Learnings
*Document insights about:*
- Keyword-based scoring limitations
- Structural checks vs. quality assessment
- Feedback generation logic

### Discovered Limitations
*What can heuristics NOT evaluate?*
-
-
-

### Why This Matters
*How does this motivate the move to AI judge?*

### Time Spent
___ hours

### API Cost
£0 (logic only, no API calls)

---

## Stage 4 — AI Judge

**Date:** ___
**Status:** Not Started

### What I Built
*To be filled after completion*

### Technical Learnings
*Document insights about:*
- Judge prompt engineering
- Structured output format enforcement
- Verdict parsing strategies
- Handling ambiguous responses
- Fallback logic design

### Verdict Parsing Success
- Total tests: ___
- Successful parses: ___
- Success rate: ___%
- Issues encountered:

### Parsing Strategies That Worked
1.
2.
3.

### Prompt Engineering Insights
*What made the judge reliable?*

### Time Spent
___ hours

### API Cost
£___

---

## Stage 5 — Debate System

**Date:** ___
**Status:** Not Started

### What I Built
*To be filled after completion*

### Technical Learnings
*Document insights about:*
- Multi-turn conversation management
- Context passing between turns
- Token budget management
- Debate flow orchestration

### Debate Quality
- Rebuttals substantive? Yes / Partial / No
- Referenced specific points? Yes / Partial / No
- Judge considered arguments? Yes / Partial / No

### Token Management
- Average tokens per debate: ___
- Cost per complete debate: £___
- Optimization opportunities:

### Time Spent
___ hours

### API Cost
£___

---

## Stage 6 — Framework Integration

**Date:** ___
**Status:** Not Started

### What I Built
*To be filled after completion*

### Technical Learnings
*Document insights about:*
- Domain knowledge injection
- Framework-specific evaluation
- Citation quality and specificity
- Balancing framework depth vs. token cost

### Framework Integration Quality
- Specific behaviours mentioned? Yes / No
- Coaching habits evaluated? Yes / No
- TREDS values considered? Yes / No
- Red flags identified? Yes / No

### Trojans-Specific Feel
*Does evaluation feel domain-specific or generic?*

### Time Spent
___ hours

### API Cost
£___

---

## Stage 7 — Session History Context

**Date:** ___
**Status:** Not Started

### What I Built
*To be filled after completion*

### Technical Learnings
*Document insights about:*
- Context window management
- Progressive planning assessment
- Temporal pattern recognition
- Historical data integration

### Progression Assessment Quality
- Identifies good continuity? Yes / No
- Warns about repetition? Yes / No
- Recognizes appropriate difficulty? Yes / No
- Assesses variety? Yes / No

### Time Spent
___ hours

### API Cost
£___

---

## Stage 8 — Final Polish & Documentation

**Date:** ___
**Status:** Not Started

### What I Built
*To be filled after completion*

### Technical Learnings
*Document insights about:*
- Production-ready error handling
- User experience improvements
- Token tracking implementation
- Documentation best practices

### Polish Completeness
- Error handling robust? Yes / No
- Loading states smooth? Yes / No
- Cost tracking accurate? Yes / No
- Documentation complete? Yes / No

### Time Spent
___ hours

### API Cost
£___

---

## Overall Project Insights

*Fill this out at project completion*

### Most Valuable Learnings

**About AI Orchestration:**
1.
2.
3.

**About Prompt Engineering:**
1.
2.
3.

**About System Architecture:**
1.
2.
3.

### Biggest Challenges
1.
2.
3.

### Biggest Surprises
1.
2.
3.

### Reusable Patterns Discovered
1.
2.
3.

### Would Do Differently Next Time
1.
2.
3.

---

## Cost Summary

| Stage | Tests | Tokens | Cost |
|-------|-------|--------|------|
| Stage 1 | | | £ |
| Stage 2 | | | £ |
| Stage 3 | | | £0.00 |
| Stage 4 | | | £ |
| Stage 5 | | | £ |
| Stage 6 | | | £ |
| Stage 7 | | | £ |
| Stage 8 | | | £ |
| **Total** | | | **£** |

**Budget:** £2-3
**Status:** Under / Over / On Track

---

## Portfolio Presentation Notes

*How would you explain this project to colleagues or in an interview?*

**Elevator Pitch:**


**Technical Highlights:**


**Key Demonstrations:**


**Learnings to Share:**


---

## Future Applications

*How could these patterns be applied to other projects?*

1.
2.
3.

---

## References & Resources Used

- [Anthropic API Documentation](https://docs.anthropic.com)
- [David Brierley's Multi-Model Orchestration](https://github.com/Brierley77/Multiple-Model-Orchestration)
-

---

*Remember: The goal is learning, not perfection. Document what worked, what didn't, and why.*

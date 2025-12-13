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

**Date:** December 13, 2025
**Status:** Complete ✅

### What I Built
- **Enhanced prompt templates** (`src/prompts.py`)
  - `get_coach_a_prompt()` - Game-Based/Player-Centered coaching philosophy
  - `get_coach_b_prompt()` - Structured/Coach-Centered coaching philosophy
- **Dual generation route** (`src/app.py`)
  - New `/generate-dual` endpoint for parallel coach generation
  - Sequential API calls with different system prompts (Coach A, then Coach B)
  - Token tracking for both coaches individually and combined
- **Comparison template** (`templates/comparison.html`)
  - Side-by-side layout with responsive grid (2 columns on desktop, stacks on mobile)
  - Color-coded sections (blue for Coach A, red for Coach B)
  - Philosophy badges clearly displayed
  - Detailed token usage statistics
  - Print-friendly styling
- **Updated UI** (`templates/index.html`)
  - Dual-mode form with two submit buttons (Single Coach vs. Compare Two Coaches)
  - Philosophy descriptions for user guidance
  - Updated branding to "Stage 2"

### Technical Learnings
**Sequential vs. Parallel API calls:**
- Initially considered parallel API calls but implemented sequentially for simplicity
- Sequential execution: easier error handling, clearer logging, sufficient performance
- Both calls complete in ~60 seconds total (30s each)
- Future optimization: Could use `asyncio` for true parallel calls if needed

**System prompt engineering for personas:**
- Strong persona definition crucial: "You are COACH A - a rugby coach who follows..."
- Explicit coaching philosophy statements create consistency
- Contrasting language patterns: Coach A uses "questions", Coach B uses "instructions"
- Including explicit "Language to Use/Avoid" helps maintain character

**Philosophical consistency maintenance:**
- Detailed belief systems in prompts ensure philosophical alignment
- Activity naming reflects philosophy ("Hot Potato Tag" vs "Technical Passing Sequence")
- Explicit constraints vs. teaching points distinction works well
- Cool-down activities reinforce philosophy (player reflection vs. technical review)

**Comparison display patterns:**
- Side-by-side layout makes differences immediately visible
- Color coding helps users quickly identify which coach is which
- Keeping same HTML structure for both plans ensures alignment
- Responsive design essential for practical use

### Philosophical Difference Quality
**How distinct were the approaches?**
- **Game-based vs. structured clarity:** 9/10 - Extremely clear differences
- **Activity type differences:** Notable - Completely different activity designs
- **Coaching point style differences:** Notable - Questions vs. instructions paradigm obvious

**Specific differences observed:**

| Aspect | Coach A (Game-Based) | Coach B (Structured) |
|--------|---------------------|---------------------|
| Warm-up | "Hot Potato Tag" - fun, chaotic | "Technical Passing Sequence" - controlled progression |
| Main activities | "Treasure Island Escape", constraint-based games | "Foundation Passing Grid", technical drills |
| Coaching language | "What happens when...?", "How can you...?" | "Keep hands up", "Step before pass" |
| Error handling | Let players discover solutions | "Stop and correct errors immediately" |
| Cool down | "Circle of Discovery" - player-led | "Technical Review Circle" - coach-led |
| Activity names | Creative, playful | Descriptive, technical |

### Code Patterns Discovered
**Reusable dual-generation pattern:**
```python
# Generate two distinct prompts
prompt_a = get_persona_a_prompt(params)
prompt_b = get_persona_b_prompt(params)

# Sequential API calls with individual error handling
response_a = client.messages.create(model=MODEL, messages=[{"role": "user", "content": prompt_a}])
response_b = client.messages.create(model=MODEL, messages=[{"role": "user", "content": prompt_b}])

# Extract and track separately
plan_a = response_a.content[0].text
plan_b = response_b.content[0].text
tokens_a = response_a.usage.input_tokens + response_a.usage.output_tokens
tokens_b = response_b.usage.input_tokens + response_b.usage.output_tokens
```

**Template reuse pattern:**
- Same content rendering logic for both plans: `{{ plan | replace('\n', '<br>') | safe }}`
- Shared CSS classes with modifier classes (`.coach-plan.coach-a`, `.coach-plan.coach-b`)
- DRY principle maintained through Jinja template inheritance potential

**Form action routing:**
- HTML5 `formaction` attribute allows multiple submit buttons to different endpoints
- Cleaner than JavaScript-based form manipulation
- Preserves form validation for both actions

### Surprises
- **Philosophical consistency was better than expected** - Claude maintained distinct personas throughout entire session plans without drifting
- **Activity naming creativity** - Coach A generated genuinely playful names ("Treasure Island Escape") while Coach B stayed technical
- **Language patterns persisted** - Questions vs. commands distinction visible in every section
- **Token usage was very similar** - Both coaches used ~1,260-1,280 output tokens despite different styles
- **No prompt engineering iteration needed** - First version of persona prompts worked excellently

### Challenges
- **Template rendering complexity** - Needed to handle markdown-like formatting (`**bold**`) in HTML
- **Form submission routing** - Required understanding of `formaction` attribute vs. JavaScript solutions
- **Color scheme selection** - Finding distinct but professional colors for each coach

### Would Do Differently
- Consider adding a "Which coach do you prefer?" user feedback mechanism
- Could add explicit framework alignment hints in Stage 2 (save for Stage 6)
- Might add activity count comparison (Coach A: 3 activities, Coach B: 4 activities)
- Template could benefit from collapsible sections for very long plans

### Time Spent
~2 hours (planning, implementation, testing, debugging, documentation)

### API Cost
- Test run: 835 input + 2,538 output = 3,373 tokens
- Estimated cost: ~£0.08-0.10 per dual generation
- Total testing cost: ~£0.10 (1 comprehensive test)

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
| Stage 1 | 3-4 | ~1,000/test | £0.05 |
| Stage 2 | 1 | 3,373 | £0.10 |
| Stage 3 | TBD | 0 (logic only) | £0.00 |
| Stage 4 | TBD | TBD | £TBD |
| Stage 5 | TBD | TBD | £TBD |
| Stage 6 | TBD | TBD | £TBD |
| Stage 7 | TBD | TBD | £TBD |
| Stage 8 | TBD | TBD | £TBD |
| **Total** | **4-5** | **~7,000** | **£0.15** |

**Budget:** £2-3
**Status:** Under budget / On Track (7.5% of budget used)

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

# Project Requirements - Rugby Session Plan Debate System

**Project Name:** Rugby Session Plan Debate System  
**Purpose:** Learn AI orchestration patterns through practical rugby coaching application  
**Duration:** 10-12 hours across multiple sessions  
**Budget:** £2-3 API costs

---

## Problem Statement

### The Learning Challenge
Current understanding of AI systems is limited to single-model interactions. To advance toward leading a data analytics team and building sophisticated AI tools, need hands-on experience with:
- Multi-model orchestration patterns
- Judge/evaluator systems
- Prompt engineering for consistent structured outputs
- System architecture for AI applications

### The Practical Challenge
Rugby session planning involves tradeoffs between different coaching philosophies:
- **Game-based learning** vs. **Structured progression**
- **Player discovery** vs. **Technical instruction**
- **Chaos tolerance** vs. **Systematic building blocks**

Currently relying on single session planner. Would benefit from:
- Seeing multiple approaches to same objective
- Understanding philosophical tradeoffs
- Getting automated evaluation against coaching framework
- Building intuition for quality session design

### Solution Approach
Build a system where:
1. Two AI "coaches" generate competing session plans with distinct philosophies
2. An AI "judge" evaluates both plans against Trojans coaching framework
3. Optional: Coaches debate their approaches before final judgment
4. Result: Learn orchestration patterns + get insights on coaching approaches

---

## Stakeholders

### Primary: Wayne (Developer/User)
- **Role:** Business/data analyst, rugby coach, vibe coder
- **Background:** Self-taught PowerBI expert, building rugby coaching apps
- **Learning Goal:** Understand AI orchestration for future team leadership
- **Practical Goal:** Enhance session planning workflow
- **Time Available:** 1-2 hour sessions, flexible schedule
- **Technical Level:** Comfortable with Python/JavaScript, API calls, Replit/VS Code

### Secondary: Trojans RFC U10s Squad
- **Role:** Indirect beneficiaries if tool is useful
- **Age Group:** Under 10s (typically 8-9 years old)
- **Squad Size:** 16-20 players
- **Season:** October to March
- **Coaching Standard:** Volunteer coaches, mixed experience levels

### Reference: David Brierley
- **Role:** Inspiration (colleague who built similar orchestration system)
- **Project:** Multi-Model Orchestration notebook using local LLMs
- **Lessons Learned:** Progressive complexity, token management, architecture flexibility

---

## Core Requirements

### Functional Requirements

#### FR1: Single Session Plan Generation
- **Must** generate single rugby session plan from form inputs
- **Must** accept: age group, objective, duration, number of players
- **Must** use Anthropic Claude API (Sonnet 4)
- **Must** display formatted session plan in browser
- **Must** handle API errors gracefully

#### FR2: Dual Coach Generation
- **Must** generate two competing plans from same inputs
- **Must** use distinct coaching philosophies (game-based vs. structured)
- **Must** display plans side-by-side for comparison
- **Must** clearly label each coaching approach
- **Must** produce noticeably different plans

#### FR3: Automated Evaluation
- **Must** automatically select "winner" between two plans
- **Should** start with simple heuristic scoring (Phase 3)
- **Must** upgrade to AI judge evaluation (Phase 4)
- **Must** provide reasoning for winner selection
- **Must** reference evaluation criteria in explanation

#### FR4: Framework Integration
- **Must** evaluate plans against Trojans coaching framework
- **Must** reference specific framework elements:
  - Trojans Player (Behaviours, Skills, Knowledge)
  - Coaching Habits (Shared Purpose, Progression, Praise, Review, Choice)
  - TREDS Values (Teamwork, Respect, Enjoyment, Discipline, Sportsmanship)
  - Session structure principles
  - Red flags to avoid
- **Must** cite framework explicitly in judge reasoning

#### FR5: Optional Debate Functionality
- **Should** allow coaches to rebut each other's approaches
- **Should** provide multi-turn conversation before judging
- **Should** pass full debate transcript to judge
- **Should** keep rebuttals concise (100 words) for token management

#### FR6: Optional Session History
- **Could** accept recent session objectives as input
- **Could** evaluate continuity and progression
- **Could** warn against premature skill repetition
- **Could** assess variety across sessions

### Non-Functional Requirements

#### NFR1: Cost Management
- **Must** stay within £2-3 total API cost for full project
- **Must** use appropriate token limits per API call:
  - Generation: max 1500 tokens
  - Judge: max 1000 tokens
  - Rebuttals: max 200 tokens
- **Should** log token usage for cost tracking
- **Should** minimize unnecessary API calls during testing

#### NFR2: Reliability
- **Must** parse judge verdicts correctly >90% of time
- **Must** handle unclear verdicts with fallback logic
- **Must** handle network errors gracefully
- **Must** provide meaningful error messages to user
- **Should** implement retry logic with exponential backoff

#### NFR3: Usability
- **Must** be runnable in VS Code with Claude Code
- **Must** work with simple Python environment (Flask/FastAPI)
- **Should** provide clear loading indicators during API calls
- **Should** be testable with single command (e.g., `python app.py`)
- **Must** be usable by developer with no rugby knowledge (clear labels)

#### NFR4: Maintainability
- **Must** use modular code structure (separate concerns)
- **Must** include type hints and docstrings
- **Must** have clear error handling
- **Should** follow Python PEP 8 style guidelines
- **Must** be documented for future reference

#### NFR5: Learning Value
- **Must** document learnings after each phase
- **Must** demonstrate orchestration patterns clearly
- **Must** be explicable to others (portfolio piece)
- **Should** reveal insights about prompt engineering
- **Should** show tradeoffs in AI system design

---

## Constraints

### Technical Constraints
- **Platform:** VS Code with Claude Code and GitHub Copilot
- **API:** Anthropic Claude API only (no local models)
- **Model:** Claude Sonnet 4 (`claude-sonnet-4-20250514`)
- **Language:** Python (Flask or FastAPI preferred)
- **Frontend:** HTML/CSS/JavaScript (simple, no React required)
- **Database:** None required (localStorage acceptable for history)
- **Deployment:** Local development only (no production hosting needed)

### Domain Constraints
- **Age Groups:** U7-U12 (focus on U10)
- **Session Duration:** Typically 60 minutes
- **RFU Regulations:** Must follow Regulation 15 for age-grade rugby
- **Trojans Framework:** Must align with Trojans RFC coaching principles
- **Safety:** Must prioritize player safety in all generated plans

### Project Constraints
- **Timeline:** No fixed deadline, learn at comfortable pace
- **Budget:** £2-3 for API calls during full development
- **Scope:** Stop at Phase 4-5 if learning goals met (Phases 6-7 optional)
- **Quality:** Working code + learning > perfect production code
- **Documentation:** Must capture insights, not just build features

### Resource Constraints
- **Time:** 1-2 hour sessions, weekends or evenings
- **Attention:** Single developer, no team support
- **Support:** Claude Code and GitHub Copilot available
- **Testing:** Manual testing only (no automated test suite required)

---

## User Stories

### As a Developer Learning AI Orchestration

**US1: Generate Single Plan**
```
GIVEN I have a session objective
WHEN I submit the form with age group, objective, duration, players
THEN I should receive one AI-generated session plan
AND it should be formatted and usable for real coaching
```

**US2: Compare Two Approaches**
```
GIVEN I have a session objective
WHEN I request competing plans
THEN I should see two distinct approaches side-by-side
AND they should reflect different coaching philosophies
AND I should be able to compare them easily
```

**US3: Get Automated Selection**
```
GIVEN I have two competing session plans
WHEN the judge evaluates them
THEN I should see which plan wins
AND I should understand why (with reasoning)
AND the reasoning should reference specific criteria
```

**US4: Learn From Debate**
```
GIVEN I have two competing session plans
WHEN coaches debate their approaches
THEN I should see their arguments
AND the judge should consider full debate context
AND I should understand orchestration patterns better
```

### As a Rugby Coach Using the Tool

**US5: Get Framework-Aligned Plans**
```
GIVEN I input "improve support play"
WHEN plans are generated and evaluated
THEN the judge should use Trojans framework criteria
AND the winner should align with Trojans coaching habits
AND I should see which framework elements are present
```

**US6: Ensure Progressive Planning**
```
GIVEN I've coached "passing" and "support play" recently
WHEN I plan next session on "decision making"
THEN the judge should recognize logical progression
AND warn if I'm repeating skills too soon
AND suggest how new objective builds on previous learning
```

---

## Success Criteria

### Phase-Specific Success

#### Phase 1: Working Generator
- ✅ Can generate session plan from form
- ✅ Plan is coherent and coaching-usable
- ✅ API integration works reliably

#### Phase 2: Competing Philosophies
- ✅ Two distinct plans generated
- ✅ Philosophical differences clear
- ✅ Display enables comparison

#### Phase 3: Automated Selection
- ✅ Heuristic scoring works
- ✅ Winner selected with reasoning
- ✅ Limitations documented for learning

#### Phase 4: Intelligent Judge
- ✅ AI judge provides evaluation
- ✅ Verdict parsed correctly >90%
- ✅ Reasoning references criteria

#### Phase 5: Debate System
- ✅ Multi-turn conversation works
- ✅ Rebuttals reference opponent points
- ✅ Judge uses full context

#### Phase 6: Framework Integration
- ✅ Trojans framework applied
- ✅ Framework elements cited
- ✅ Evaluation feels "Trojans-specific"

#### Phase 7: History Context
- ✅ Progression assessed
- ✅ Continuity recognized
- ✅ Variety evaluated

### Overall Project Success

**Learning Objectives Met:**
- ✅ Understand judge pattern
- ✅ Can design structured output prompts
- ✅ Can debug multi-turn conversations
- ✅ Can explain orchestration to others
- ✅ Documented insights for future reference

**Practical Outcomes Achieved:**
- ✅ Working debate system
- ✅ Generates multiple approaches
- ✅ Evaluates against framework
- ✅ Could integrate with existing tools (if desired)

**Quality Markers:**
- ✅ Code is maintainable
- ✅ Documentation is comprehensive
- ✅ Learnings are captured
- ✅ Can demo to colleagues
- ✅ Portfolio-ready

---

## Prompts & Templates

### Base Session Generator Prompt
```
You are a rugby coach following RFU guidelines for {age_group}.

Create a training session plan for:
- Objective: {objective}
- Duration: {duration} minutes
- Number of players: {players}
- Focus: Player enjoyment and development over performance

Your session must include:
1. Warm-up/Activate (5-10 minutes)
2. Main activities (35-45 minutes total)
3. Cool down (5 minutes)

For each activity, provide:
- Activity name
- Duration
- Setup/organization
- Key coaching points (max 3)
- Safety considerations

Format your response as clear sections with headings.
```

### Coach A Philosophy (Game-Based)
```
Your coaching philosophy:
- Learning through play and discovery
- Minimal direct instruction
- Players figure things out through games
- Embrace productive chaos
- Questioning over telling
- Game → Problem → Mini-skill → Game

Prioritize:
- High engagement (everyone moving)
- Player problem-solving
- Minimal coach talking
- Maximum attempts/touches
- Discovery over instruction
```

### Coach B Philosophy (Structured)
```
Your coaching philosophy:
- Clear skill breakdowns and progressions
- Build from simple to complex
- Technical instruction before game application
- Master fundamentals first
- Demonstration and repetition
- Isolated skill → Pressure → Game

Prioritize:
- Clear progressions using STEP
- Demonstration of correct technique
- Repetition for mastery
- Building blocks approach
- Technical excellence
```

### Judge Evaluation Criteria (Basic)
```
EVALUATION CRITERIA:
1. Player enjoyment and engagement
2. Age-appropriate activities and complexity
3. Safety considerations
4. Progressive skill development
5. Clear coaching points (max 3 per activity)
6. Balance of game-based and skill practice
7. Follows RFU Regulation 15 for {age_group}
8. Appropriate time allocations

End your response with exactly one line:
WINNER: A
or
WINNER: B
```

---

## Dependencies

### Required
- Python 3.9+
- anthropic (Anthropic Python SDK)
- flask or fastapi (web framework)
- python-dotenv (environment variables)

### Optional
- jinja2 (templating if using Flask)
- uvicorn (if using FastAPI)
- pytest (if adding tests)

### Install Command
```bash
pip install anthropic flask python-dotenv
```

---

## Risk Analysis

### Technical Risks

**Risk: API Rate Limiting**
- **Probability:** Medium
- **Impact:** Medium (delays testing)
- **Mitigation:** Add delays between calls, implement retry logic

**Risk: Judge Verdict Unclear**
- **Probability:** High (especially early testing)
- **Impact:** Medium (requires debugging)
- **Mitigation:** Multiple parsing fallbacks, explicit format requirements

**Risk: Token Limits Exceeded**
- **Probability:** Medium (especially Phase 5+)
- **Impact:** Low (truncate prompts, reduce rebuttals)
- **Mitigation:** Token counting, prompt optimization

**Risk: API Costs Over Budget**
- **Probability:** Low
- **Impact:** Low (£2-3 is flexible)
- **Mitigation:** Token tracking, efficient testing

### Learning Risks

**Risk: Getting Stuck on Problem**
- **Probability:** Medium
- **Impact:** Medium (delays progress, frustration)
- **Mitigation:** Claude Code assistance, troubleshooting guide, can skip phases

**Risk: Losing Motivation**
- **Probability:** Low
- **Impact:** High (project abandoned)
- **Mitigation:** Small phases, early wins, stopping is acceptable

**Risk: Over-Engineering**
- **Probability:** Medium
- **Impact:** Medium (time waste)
- **Mitigation:** Focus on learning over perfection, stage-by-stage approach

### Scope Risks

**Risk: Scope Creep**
- **Probability:** Medium
- **Impact:** Medium (time overrun)
- **Mitigation:** Phases clearly defined, extensions marked optional

**Risk: Framework Complexity**
- **Probability:** Low
- **Impact:** Low (can simplify if needed)
- **Mitigation:** Framework already documented, can use subset

---

## Out of Scope

### Explicitly NOT Required

- ❌ Production deployment (Heroku, Vercel, etc.)
- ❌ User authentication or multi-user support
- ❌ Database persistence (localStorage acceptable)
- ❌ Mobile app or responsive design perfection
- ❌ Comprehensive test suite (manual testing sufficient)
- ❌ Performance optimization (speed not critical)
- ❌ Advanced UI/UX design (functional > beautiful)
- ❌ Integration with existing session planner app
- ❌ Sharing/collaboration features
- ❌ PDF/DOCX export (nice-to-have, not required)
- ❌ Real-time updates or WebSocket communication
- ❌ Analytics or usage tracking

### Future Considerations

If project proves valuable, these could be added later:
- Integration with existing Trojans session planner
- Save/load session library
- Export to coaching templates
- Share winning plans with other coaches
- Mobile-optimized interface
- Season planning integration

But none of these are required for learning objectives or initial success.

---

## References

### External Resources
- [David Brierley's Multi-Model Orchestration](https://github.com/Brierley77/Multiple-Model-Orchestration)
- [Anthropic API Documentation](https://docs.anthropic.com)
- [OpenAI Multi-Agent Patterns](https://openai.github.io/openai-agents-python/multi_agent/)
- [Microsoft Multi-Agent Reference](https://microsoft.github.io/multi-agent-reference-architecture/)

### Internal Resources
- Existing Rugby Session Planner (for comparison)
- Trojans RFC Coaching Framework
- RFU Regulation 15 (age-grade rules)
- Previous coaching session examples

### Learning Resources
- Build Plan (detailed phase-by-phase guide)
- Learning Log (capture insights as you go)
- Troubleshooting Guide (common issues and solutions)
- Inspiration Doc (David's journey and lessons)

---

*Last Updated: December 12, 2025*
# Project Plan - Rugby Session Plan Debate System

This file contains the step-by-step execution plan for Claude Code.  
**Claude should only execute the stage explicitly requested.**

---

## How to Use This Plan

- **Ignore all stages except the one explicitly instructed to begin**
- Before starting a stage, summarize your understanding of:
  - Objective
  - Inputs
  - Expected Outputs
  - Any clarifying questions (if essential)
- **Wait for explicit confirmation before performing any code changes**
- After completing a stage, generate:
  - A short summary of what changed
  - A diff of modifications (if applicable)

---

## Stage 0 — Environment Validation

**Objective**  
Confirm repo structure, required files, and development environment readiness.

**Inputs**
- README.md
- CLAUDE_GUIDE.md
- REQUIREMENTS.md
- Python/Node environment availability
- Anthropic API key access

**Expected Outputs**
- Summary of repo readiness
- List of any missing dependencies
- Confirmation of API key configuration
- Any required adjustments identified

**Instructions for Claude**  
Inspect the repo structure, verify all prerequisite files exist, check Python/Node setup, then wait for confirmation before proceeding.

---

## Stage 1 — Initial Scaffolding (Phase 1: Single Coach Generator)

**Objective**  
Create minimal working project structure with single session plan generator.

**Inputs**
- REQUIREMENTS.md (project goals and constraints)
- context/trojans_framework.md (coaching framework reference)
- Anthropic API credentials

**Expected Outputs**
- Basic folder structure (src/, context/, docs/)
- Simple web interface (HTML/Flask/FastAPI)
- Single API call to Claude for session generation
- Form inputs: age group, objective, duration, players
- Display of generated session plan

**Instructions for Claude**  
Create minimal, working scaffold only. No business logic beyond basic form → API → display. Use simple prompt from REQUIREMENTS.md. Test with one example objective before marking complete.

**Success Criteria**
- Form captures all inputs
- API call succeeds
- Session plan displays in browser
- Plan is coherent and usable

---

## Stage 2 — Dual Coach Generation (Phase 2: Two Competing Coaches)

**Objective**  
Extend to generate two session plans with distinct coaching philosophies.

**Inputs**
- Stage 1 working code
- context/coaching_philosophies.md (Coach A & B personalities)
- Same form inputs from Stage 1

**Expected Outputs**
- Two parallel API calls with different system prompts
- Side-by-side display of both plans
- Clear visual distinction (Coach A: Game-Based, Coach B: Structured)
- Labels showing coaching philosophy

**Instructions for Claude**  
Duplicate API call logic with different prompts. Keep Stage 1 code intact. Add comparison view. No evaluation yet—just display both plans.

**Success Criteria**
- Two distinct plans generated for same objective
- Clear philosophical differences visible
- Both plans coherent and properly formatted
- Display makes comparison easy

---

## Stage 3 — Heuristic Judge (Phase 3: Simple Rule-Based Evaluation)

**Objective**  
Implement basic automated winner selection using keyword scoring.

**Inputs**
- Stage 2 working code (two plans)
- context/scoring_rubric.md (heuristic rules)

**Expected Outputs**
- Python/JavaScript scoring function
- Keyword-based evaluation (warm-up, cool-down, "fun", "STEP", etc.)
- Score display for each plan (e.g., "Coach A: 6/7")
- Winner declaration with reasoning
- Feedback on what each plan includes/misses

**Instructions for Claude**  
Create `score_plan()` function using keyword matching and structural checks. No AI evaluation yet. Focus on presence/absence of key elements. Document limitations for learning purposes.

**Success Criteria**
- Scoring function runs without errors
- Winner selected automatically
- Feedback explains scoring decisions
- Results make intuitive sense

---

## Stage 4 — AI Judge (Phase 4: Intelligent Evaluation)

**Objective**  
Replace heuristic scoring with Claude as intelligent judge.

**Inputs**
- Stage 3 working code
- context/judge_prompts.md (evaluation criteria)
- Both session plans from Stage 2

**Expected Outputs**
- Third API call (judge role)
- Structured judge prompt with evaluation criteria
- Verdict parsing logic with fallbacks
- Display of judge reasoning + winner
- Error handling for unclear verdicts

**Instructions for Claude**  
Create `judge_plans()` function with explicit format requirements ("End with: WINNER: A or WINNER: B"). Implement robust parsing with multiple fallback strategies. Test with various objectives to ensure reliable verdict extraction.

**Success Criteria**
- Judge provides detailed evaluation
- Verdict parsed correctly >90% of time
- Reasoning references specific criteria
- Winner selection makes sense
- Fallback handling works for ambiguous cases

---

## Stage 5 — Debate System (Phase 5: Multi-Turn Conversation)

**Objective**  
Add rebuttal rounds before final judging.

**Inputs**
- Stage 4 working code
- context/rebuttal_prompts.md (debate structure)
- Both original plans from Stage 2

**Expected Outputs**
- Two additional API calls (rebuttals)
- Coach A rebuttal (sees Coach B's plan, defends own)
- Coach B rebuttal (sees Coach A's rebuttal, counter-defends)
- Full debate transcript compiled
- Judge evaluates complete debate context
- Display showing: Opening → Rebuttals → Judge Decision

**Instructions for Claude**  
Implement `conduct_debate()` function with 4 total API calls. Keep rebuttals short (100 words, ~200 tokens) for token management. Pass full transcript to judge. Update display to show debate flow clearly.

**Success Criteria**
- Debate flows naturally through all turns
- Rebuttals reference specific opponent points
- Judge considers full debate context
- Winner selection accounts for argumentation
- No API timeout errors

---

## Stage 6 — Framework Integration (Phase 6: Trojans-Specific Evaluation)

**Objective**  
Replace generic evaluation with Trojans RFC coaching framework.

**Inputs**
- Stage 5 working code
- context/trojans_framework.md (complete framework)
- Updated judge prompt template

**Expected Outputs**
- Framework loaded from file/variable
- Judge prompt includes Trojans-specific criteria:
  - Trojans Player (Behaviours, Skills, Knowledge)
  - Coaching Habits (5 elements)
  - TREDS Values
  - Red Flags to avoid
- Evaluation explicitly cites framework elements
- Display shows framework alignment scores

**Instructions for Claude**  
Update `judge_with_framework()` to inject full framework into prompt. Judge must reference specific framework elements in reasoning. Add framework alignment section to display (behaviours developed, habits present, values fostered).

**Success Criteria**
- Judge references specific framework elements
- Evaluation uses Trojans terminology
- Trojans Player areas explicitly cited
- TREDS values considered
- Red flags identified when present

---

## Stage 7 — Session History Context (Phase 7: Progressive Planning)

**Objective**  
Factor in recent session history for continuity assessment.

**Inputs**
- Stage 6 working code
- Optional form fields: last 3 session objectives
- context/progression_criteria.md

**Expected Outputs**
- Additional form inputs (last_week, two_weeks, three_weeks)
- History context added to judge prompt
- Progression checking in evaluation:
  - Building on previous learning?
  - Avoiding premature skill repetition?
  - Appropriate difficulty progression?
  - Good variety across sessions?
- Display showing session timeline

**Instructions for Claude**  
Add history inputs to form (optional). If provided, include in judge prompt with progression assessment criteria. Judge must evaluate continuity and variety. Consider adding localStorage to auto-populate history from previous runs.

**Success Criteria**
- Judge identifies progression gaps
- Warns about premature skill revisiting
- Recognizes good learning continuity
- Assesses variety across sessions
- Provides specific continuity feedback

---

## Stage 8 — Final Polish & Documentation

**Objective**  
Production-ready refinements and comprehensive documentation.

**Inputs**
- Stage 7 complete working system
- All learning log notes
- Testing feedback

**Expected Outputs**
- Error handling hardened
- Loading states added to UI
- Cost tracking implemented (token counting)
- README updated with:
  - Installation instructions
  - API key setup
  - Usage examples
  - Known limitations
- LEARNING_LOG.md populated with insights
- Code comments added to key functions

**Instructions for Claude**  
Focus on robustness and user experience. Add proper error messages, loading indicators, and graceful failures. Document all learned patterns. Generate usage examples showing different scenarios.

**Success Criteria**
- System handles errors gracefully
- User experience is smooth
- Documentation is complete
- Code is maintainable
- Learning insights captured

---

## Optional Extensions (Post-Stage 8)

**Not required for core project completion. Only pursue if time/interest permits.**

### Extension A: Judge Panel (Multiple Evaluators)
Three judges evaluate independently, require 2/3 consensus.

### Extension B: Session Library
Store winning plans in SQLite/JSON for future reference.

### Extension C: Export Functionality
Generate PDF/DOCX from winning plan in Trojans template format.

### Extension D: Assistant Coach Mode
User provides rough outline, AI develops full session plan.

---

## Notes on Stage Execution

### Important Reminders
- Each stage builds on previous working code
- Never modify code without explicit instruction
- Test thoroughly before marking stage complete
- Document learnings in LEARNING_LOG.md after each stage
- Commit code after each successful stage

### Cost Awareness
- Stage 1-2: ~£0.05 per test run
- Stage 3: No additional API cost (logic only)
- Stage 4: ~£0.15 per test (3 API calls)
- Stage 5: ~£0.30 per test (5 API calls)
- Stage 6-7: ~£0.30 per test (framework adds tokens)

Total project experimentation budget: ~£2-3

### When to Stop
Project success is achieved when:
- Core orchestration patterns are understood
- Working debate system is functional
- Learning objectives are met
- Documentation captures insights

Stopping at Stage 4-5 is perfectly acceptable if goals are reached.

---

*Last Updated: December 12, 2025*
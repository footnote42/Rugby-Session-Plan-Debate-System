# Rugby Session Plan Debate System

An AI-powered coaching debate system where multiple Claude instances compete to design better rugby session plans. Coaches with distinct philosophies generate session plans, engage in structured debate, and are evaluated by an AI judge using the Trojans RFC coaching framework.

## Project Purpose

This is a **learning project** focused on understanding AI orchestration patterns, multi-agent systems, and prompt engineering. The rugby coaching domain provides rich, real-world complexity for exploring how LLMs can collaborate, compete, and evaluate.

**Not just a web app** - This is an incremental exploration of AI agent design patterns.

## Getting Started

### Prerequisites
- Node.js and npm installed
- Anthropic API key (for Claude API access)
- Budget awareness: ~£2-3 total for all experimentation

### Installation

```bash
cd "c:/Coding Projects/Rugby-Session-Plan-Debate-System"
npm install
```

### Running the Development Environment

```bash
# Run both backend and frontend concurrently
npm run dev
```

- Frontend: http://localhost:5173
- Backend API: http://localhost:3000

## Project Structure

```
├── backend/          # Express API server (minimal scaffold)
├── frontend/         # Vite + React UI (minimal scaffold)
├── context/          # Domain knowledge and framework definitions
│   ├── artefacts/
│   │   ├── trojans_framework.md      # Trojans RFC coaching framework
│   │   ├── philosophies.md           # Coach A & B personas
│   │   ├── session_plan_schema.yaml  # Data structure specification
│   │   └── sample_session_plans.json # Example data
│   ├── domain_notes.md               # Rugby coaching context
│   └── references/
│       └── references.md             # External documentation links
├── PROJECT_PLAN.md   # 8-stage execution plan (READ THIS FIRST)
├── REQUIREMENTS.md   # Project goals and constraints
├── CLAUDE_GUIDE.md   # Development guidance for Claude Code
└── CLAUDE.md         # Quick reference for Claude Code
```

## Development Approach

This project follows an **8-stage incremental plan** defined in `PROJECT_PLAN.md`:

1. **Stage 0:** Environment Validation
2. **Stage 1:** Single Coach Generator (basic AI session plan generation)
3. **Stage 2:** Dual Coach Generation (competing philosophies)
4. **Stage 3:** Heuristic Judge (keyword-based evaluation)
5. **Stage 4:** AI Judge (Claude as intelligent evaluator)
6. **Stage 5:** Debate System (multi-turn argumentation)
7. **Stage 6:** Framework Integration (Trojans RFC criteria)
8. **Stage 7:** Session History Context (progressive planning)
9. **Stage 8:** Final Polish & Documentation

**Important:** Only execute one stage at a time. Each stage builds on the previous working code.

## How It Works (Target Architecture)

### AI Orchestration Pattern

The system orchestrates multiple Claude API calls with different roles:

1. **Coach Agents**
   - Coach A: Game-Based philosophy (fun, player-led, discovery learning)
   - Coach B: Structured philosophy (progressive, technical, systematic)
   - Each receives distinct system prompts defining coaching personality
   - Generate competing session plans for the same objective

2. **Judge Agent**
   - Evaluates session plans against coaching criteria
   - Uses Trojans RFC framework (player development, coaching habits, values)
   - Provides detailed reasoning and declares a winner

3. **Debate Flow** (Stage 5+)
   - Opening: Both coaches present initial plans
   - Rebuttal A: Coach A defends own plan, critiques Coach B
   - Rebuttal B: Coach B counters and defends
   - Judge: Evaluates full debate transcript
   - **Total: 5 API calls per complete evaluation**

### Coaching Framework (Trojans RFC)

Sessions are evaluated against:
- **Trojans Player development:** Behaviours, Skills, Knowledge
- **Coaching Habits:** Quality delivery, structure, engagement
- **TREDS Values:** Trust, Respect, Enjoyment, Discipline, Support
- **Red Flags:** Over-coaching, safety issues, inappropriate difficulty

## Cost Awareness

API costs vary by development stage:
- Stage 1-2: ~£0.05 per test (1-2 API calls)
- Stage 3: £0 (logic only, no API calls)
- Stage 4: ~£0.15 per test (3 API calls)
- Stage 5+: ~£0.30 per test (5 API calls)

**Estimated total budget:** £2-3 for all experimentation.

## Key Learning Objectives

- Multi-agent orchestration patterns
- Prompt engineering for distinct AI personas
- Structured output parsing and validation
- Context management across conversation turns
- Framework-based AI evaluation
- Token and cost optimization strategies

## Current Status

**Stage 3 Complete** - Heuristic Judge implemented and tested.

### Completed Stages
- ✅ **Stage 0:** Environment Validation - Python & Node.js setup, API configured
- ✅ **Stage 1:** Single Coach Generator - Flask app with Claude integration, session plan generation working
- ✅ **Stage 2:** Dual Coach Generation - Two competing coaching philosophies (Game-Based vs Structured), side-by-side comparison
- ✅ **Stage 3:** Heuristic Judge - Keyword-based automated scoring (7-category evaluation), winner declaration

### Current Implementation
- **Flask application** (`src/app.py`) with dual generation and scoring
- **Two coach personas** - Game-Based (player-centered) vs Structured (coach-centered)
- **Heuristic scoring** - 0-7 point evaluation across session structure, safety, organization, timing, coaching, engagement
- **Visual comparison UI** - Color-coded winner announcements, detailed feedback, limitations documentation

### What Works Now
```bash
# Install Python dependencies
pip install -r requirements.txt

# Run the Flask app
python src/app.py

# Visit http://127.0.0.1:5000
# Generate session plans and see automated scoring
```

### Test Results
- **Token usage:** ~3,600 per dual generation (~£0.09)
- **Scoring cost:** £0.00 (logic only, no API calls)
- **Total spent:** £0.24 (12% of budget)
- **Test outcome:** Both coaches scored 7/7 (perfect), highlighting need for AI judge

## Next Steps

**Stage 4: AI Judge** - Replace heuristic scoring with Claude as intelligent evaluator
- Implement third API call for judge role
- Create judge prompt with evaluation criteria
- Parse structured verdict ("WINNER: A" or "WINNER: B")
- Provide nuanced reasoning beyond keyword matching

**Future Stages:**
- Stage 5: Debate System (multi-turn rebuttals)
- Stage 6: Framework Integration (Trojans RFC criteria)
- Stage 7: Session History Context
- Stage 8: Final Polish

## Success Criteria

This project is successful when:
- Core AI orchestration patterns are understood and documented
- Working debate system functions end-to-end
- Learning objectives are met (not just feature completion)
- Insights are captured in `LEARNING_LOG.md`

Stopping at Stage 4-5 is perfectly acceptable if learning goals are achieved.

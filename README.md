# Rugby Session Plan Debate System

A multi-agent deliberation system where two AI coaches — one game-based, one structured — generate competing rugby session plans for the same objective, and an automated evaluator selects the winner.

The rugby domain is the vehicle. The actual thing being explored is **deliberation as an orchestration pattern**: what happens when you point two agents with opposing philosophies at the same problem and force comparison, rather than accepting the first answer a single model produces.

---

## What It Does

You provide a session objective, age group, duration, and squad size. The system runs two parallel AI agents — each hard-coded to a distinct coaching philosophy — and renders their plans side-by-side with a scored comparison.

**Coach A — Game-Based / Player-Centered**
Constraints-led approach. Skills emerge through play, not instruction. Coaching interventions are questions, not commands. Activities are designed to be chaotic by design; the constraint is the teacher.

**Coach B — Structured / Coach-Centered**
Progressive skill development. Technical instruction before application. Demonstration, repetition, correction. Session follows a linear build from unopposed drill to game scenario.

Same objective. Same players. Fundamentally different philosophies. The comparison is the output.

---

## Architecture

```
User Input (age group, objective, duration, players)
           │
           ├── Prompt A (Game-Based persona) ──► Claude API ──► Plan A
           │
           └── Prompt B (Structured persona) ──► Claude API ──► Plan B
                                                                    │
                                                   Heuristic Scorer (local, no API cost)
                                                                    │
                                                   Score cards + Winner Declaration
                                                   Side-by-side comparison view
```

Three layers:

**1. Persona Prompting (`src/prompts.py`)**
Each coach is given an explicit belief system, not just a style hint. Coach A is told "players talk more than the coach" and "value creativity and decision-making over perfect execution." Coach B is told "stop and correct errors immediately" and "maintain control and structure." The contrast in output is sharp — different activity names, different language patterns, different error-handling philosophies — because the personas are sharply different.

**2. Heuristic Evaluation (`src/scoring.py`)**
A keyword-based scoring function evaluates each plan across seven criteria: warm-up, cool-down, safety, organisation, timing, coaching guidance, and player engagement. No additional API call. The scoring is intentionally limited and documents its own limitations — the point being to demonstrate where rule-based evaluation fails and why semantic evaluation (Stage 4: AI Judge) is needed.

**3. Flask Orchestrator (`src/app.py`)**
Coordinates both API calls, passes results to the scorer, and renders the comparison view. Single `generate-dual` endpoint handles the full pipeline. Token usage is tracked per agent.

---

## Project Roadmap

The system was designed as a staged learning project in AI orchestration. Each stage introduces a new pattern:

| Stage | Pattern | Status |
|-------|---------|--------|
| 1 — Single Coach Generator | Basic LLM call | Complete |
| 2 — Dual Coach Generation | Parallel agents, persona prompting | Complete |
| 3 — Heuristic Judge | Rule-based evaluation, documented limitations | Complete |
| 4 — AI Judge | LLM-as-evaluator, structured output parsing | Planned |
| 5 — Debate System | Multi-turn orchestration, rebuttal rounds | Planned |
| 6 — Framework Integration | Domain knowledge injection (Trojans RFC coaching framework) | Planned |
| 7 — Session History Context | Progressive planning, continuity assessment | Planned |

The staged approach is deliberate: heuristic scoring (Stage 3) runs at zero API cost and reveals exactly why keyword matching fails before committing to LLM-based evaluation (Stage 4). Testing confirmed both coaches score 7/7 on structural completeness while producing completely different plans — the heuristic cannot distinguish quality, only presence.

---

## What's Interesting About This Pattern

Single-agent generation is deterministic in the worst sense: you get one answer, shaped by one set of defaults, and have no basis for comparison. Deliberation breaks that.

By giving two agents opposing briefs and comparing their outputs:

- **Latent tradeoffs become explicit.** The game-based coach's "Treasure Island Escape" and the structured coach's "Technical Passing Grid" are both valid responses to "improve passing." Seeing them side-by-side makes the philosophical tradeoff visible, not just implied.
- **The evaluation problem becomes tractable.** Comparing two outputs against shared criteria is easier than evaluating one output in isolation.
- **Disagreement is signal, not noise.** Where the agents produce similar outputs, the approach is robust. Where they diverge sharply, there is a genuine design decision to be made.

This pattern generalises. The same architecture works for any domain where competing frameworks produce different-but-valid outputs: policy drafting, architectural decisions, risk assessment, lesson planning. Rugby session planning is the test case because it is a domain with well-defined, genuinely competing philosophies.

---

## Domain Context

The coaching philosophies used are grounded in real frameworks:

- **Player-Centered Approach (PCA):** Inquiry-based learning, questioning over instruction, co-design elements
- **Constraints-Led Approach (CLA):** Ecological dynamics, representative learning design, manipulation of space/task/people
- **Coach-Centered / Autocratic:** Explicit instruction, high repetition, structured progression, compliance checks

The planned Stage 6 integrates the Trojans RFC coaching framework as domain context for the AI judge — testing whether injecting structured domain knowledge into an LLM evaluator produces more coherent, citable reasoning than generic evaluation criteria.

---

## Tech Stack

- Python 3.14, Flask
- Anthropic Python SDK — `claude-sonnet-4-20250514`
- Jinja2 templates
- No database — stateless per request

---

## Setup

```bash
git clone https://github.com/footnote42/Rugby-Session-Plan-Debate-System.git
cd Rugby-Session-Plan-Debate-System
pip install -r requirements.txt

cp .env.example .env
# Add ANTHROPIC_API_KEY to .env

python src/app.py
```

Open `http://127.0.0.1:5000` in a browser.

**Environment variables:**

```
ANTHROPIC_API_KEY=your_key_here
ANTHROPIC_MODEL=claude-sonnet-4-20250514
MAX_TOKENS_GENERATION=1500
FLASK_SECRET_KEY=your_secret_key
```

---

## Project Structure

```
├── src/
│   ├── app.py          # Flask routes and API orchestration
│   ├── prompts.py      # Coach persona prompt templates
│   └── scoring.py      # Heuristic evaluation and comparison logic
├── templates/
│   ├── index.html      # Session input form
│   ├── result.html     # Single coach output
│   └── comparison.html # Dual coach side-by-side with scores
├── context/
│   ├── philosophies.md         # Coaching philosophy reference
│   ├── trojans_framework.md    # Trojans RFC coaching model (Stage 6)
│   └── scoring_rubric.md       # Heuristic evaluation criteria
├── LEARNING_LOG.md     # Stage-by-stage development notes
└── PROJECT_PLAN.md     # Stage definitions and success criteria
```

---

## Cost

Dual generation costs approximately £0.08–0.10 per run at current Sonnet pricing. Heuristic scoring (Stage 3) is zero API cost.

---

## Related

- [LEARNING_LOG.md](LEARNING_LOG.md) — stage-by-stage notes on what was built, what was surprising, and what failed
- Inspired by David Brierley's [Multiple-Model-Orchestration](https://github.com/Brierley77/Multiple-Model-Orchestration)

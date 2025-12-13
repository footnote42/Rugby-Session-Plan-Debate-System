# Heuristic Scoring Rubric for Rugby Session Plans

This rubric defines simple, keyword-based rules for evaluating session plan quality. It's used in Stage 3 to provide automated winner selection before implementing the AI judge in Stage 4.

## Scoring Categories (7 total points)

### 1. Session Structure (2 points)
**Goal:** Ensure the session has proper organization with all essential components.

**Scoring:**
- **Warm-up present** (1 point)
  - Keywords: "warm-up", "warm up", "activate", "activation"
  - Must appear in the plan text
- **Cool-down present** (1 point)
  - Keywords: "cool-down", "cool down", "cooldown", "recovery"
  - Must appear in the plan text

**Why this matters:** Proper session structure prevents injuries (warm-up) and aids recovery (cool-down).

---

### 2. Safety Considerations (1 point)
**Goal:** Verify the coach considers player safety.

**Scoring:**
- **Safety mentioned** (1 point)
  - Keywords: "safety", "safe", "injury", "injuries", "contact control", "controlled contact"
  - Must appear at least once in the plan

**Why this matters:** Youth rugby prioritizes safety above all else.

---

### 3. Activity Organization (1 point)
**Goal:** Check for clear activity structure and setup.

**Scoring:**
- **Setup/Organization details** (1 point)
  - Keywords: "setup", "organisation", "organization", "area", "grid", "space"
  - Must appear at least twice (indicating multiple activities are organized)

**Why this matters:** Clear organization maximizes practice time and minimizes confusion.

---

### 4. Time Management (1 point)
**Goal:** Ensure activities have timing information.

**Scoring:**
- **Duration/timing specified** (1 point)
  - Keywords: "duration", "minutes", "mins", "min", "seconds"
  - Must appear at least 3 times (warm-up + activities + cool-down)

**Why this matters:** Time management keeps sessions on track and ensures balanced practice.

---

### 5. Coaching Points/Questions (1 point)
**Goal:** Verify the plan includes coaching guidance.

**Scoring:**
- **Coaching guidance present** (1 point)
  - Keywords: "coaching point", "teaching point", "key point", "question", "what", "how", "why"
  - Must appear at least 3 times

**Why this matters:** Coaches need guidance on what to emphasize during activities.

---

### 6. Player Engagement (1 point)
**Goal:** Check for elements that engage players.

**Scoring:**
- **Engagement elements** (1 point)
  - Keywords: "fun", "game", "play", "challenge", "competition", "score", "teams"
  - Must appear at least twice

**Why this matters:** Player enjoyment drives long-term participation and development.

---

## Scoring Summary

- **Maximum Score:** 7 points
- **Minimum Score:** 0 points

### Score Interpretation
- **6-7 points:** Excellent - Comprehensive session plan with all key elements
- **4-5 points:** Good - Solid plan with most essential components
- **2-3 points:** Adequate - Basic plan but missing important elements
- **0-1 points:** Poor - Incomplete plan missing critical components

---

## Winner Declaration Logic

1. Calculate total score for Coach A and Coach B
2. Compare scores:
   - If scores differ by 2+ points: Clear winner
   - If scores differ by 1 point: Close winner
   - If scores are equal: Tie (no winner)

3. Generate feedback:
   - List what each plan includes
   - List what each plan is missing
   - Explain the scoring difference

---

## Limitations of Heuristic Scoring

**This approach cannot evaluate:**
- Quality of activity design (only presence/absence)
- Age-appropriateness of content
- Tactical sophistication
- Coaching philosophy alignment
- Progression within activities
- Player-to-coach ratio appropriateness

**These limitations motivate the move to AI judge in Stage 4**, where Claude can provide nuanced evaluation of plan quality, not just structural completeness.

---

## Implementation Notes

For the `score_plan()` function:

```python
def score_plan(plan_text: str) -> dict:
    """
    Score a session plan using keyword-based heuristics.

    Args:
        plan_text: The full session plan text

    Returns:
        {
            'total_score': int,
            'max_score': 7,
            'breakdown': {
                'warmup': bool,
                'cooldown': bool,
                'safety': bool,
                'organization': bool,
                'timing': bool,
                'coaching': bool,
                'engagement': bool
            },
            'feedback': [str]  # List of feedback messages
        }
    """
```

**Case-insensitive matching** should be used for all keyword detection.

**Count-based criteria** should count unique occurrences (not just total mentions).

**Feedback generation** should be specific about what was found/missing.

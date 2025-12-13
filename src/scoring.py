"""
Heuristic scoring module for rugby session plans.

Stage 3: Simple keyword-based evaluation using presence/absence of key elements.
This provides automated winner selection before implementing AI judge in Stage 4.
"""

import re
from typing import Dict, List, Tuple


def score_plan(plan_text: str) -> Dict:
    """
    Score a session plan using keyword-based heuristics.

    Uses simple keyword matching to evaluate presence of essential session elements.
    See context/scoring_rubric.md for full scoring criteria.

    Args:
        plan_text: The full session plan text

    Returns:
        Dictionary containing:
            - total_score: Total points earned (0-7)
            - max_score: Maximum possible score (7)
            - breakdown: Dict of individual criteria (True/False)
            - feedback: List of feedback messages explaining the score
    """
    # Convert to lowercase for case-insensitive matching
    text_lower = plan_text.lower()

    # Initialize scoring breakdown
    breakdown = {
        'warmup': False,
        'cooldown': False,
        'safety': False,
        'organization': False,
        'timing': False,
        'coaching': False,
        'engagement': False
    }

    feedback = []

    # 1. Warm-up present (1 point)
    warmup_keywords = ['warm-up', 'warm up', 'warmup', 'activate', 'activation']
    if any(keyword in text_lower for keyword in warmup_keywords):
        breakdown['warmup'] = True
        feedback.append("✓ Warm-up section present")
    else:
        feedback.append("✗ Missing warm-up section")

    # 2. Cool-down present (1 point)
    cooldown_keywords = ['cool-down', 'cool down', 'cooldown', 'recovery', 'cool-off']
    if any(keyword in text_lower for keyword in cooldown_keywords):
        breakdown['cooldown'] = True
        feedback.append("✓ Cool-down section present")
    else:
        feedback.append("✗ Missing cool-down section")

    # 3. Safety considerations (1 point)
    safety_keywords = ['safety', 'safe', 'injury', 'injuries', 'contact control', 'controlled contact']
    safety_count = sum(1 for keyword in safety_keywords if keyword in text_lower)
    if safety_count > 0:
        breakdown['safety'] = True
        feedback.append(f"✓ Safety considerations mentioned ({safety_count} references)")
    else:
        feedback.append("✗ No safety considerations mentioned")

    # 4. Activity organization (1 point)
    # Count occurrences of organization-related keywords
    org_keywords = ['setup', 'organisation', 'organization', 'area', 'grid', 'space']
    org_count = sum(1 for keyword in org_keywords if keyword in text_lower)
    if org_count >= 2:
        breakdown['organization'] = True
        feedback.append(f"✓ Activity organization details provided ({org_count} references)")
    else:
        feedback.append(f"✗ Limited organization details ({org_count} references, need 2+)")

    # 5. Time management (1 point)
    # Count timing references
    timing_keywords = ['duration', 'minutes', 'mins', 'min ', 'seconds', 'secs']
    timing_count = sum(text_lower.count(keyword) for keyword in timing_keywords)
    if timing_count >= 3:
        breakdown['timing'] = True
        feedback.append(f"✓ Timing specified for activities ({timing_count} references)")
    else:
        feedback.append(f"✗ Insufficient timing information ({timing_count} references, need 3+)")

    # 6. Coaching points/questions (1 point)
    coaching_keywords = ['coaching point', 'teaching point', 'key point', 'question',
                        'what ', 'how ', 'why ', 'coaching ', 'teaching ']
    coaching_count = sum(1 for keyword in coaching_keywords if keyword in text_lower)
    if coaching_count >= 3:
        breakdown['coaching'] = True
        feedback.append(f"✓ Coaching guidance provided ({coaching_count} references)")
    else:
        feedback.append(f"✗ Limited coaching guidance ({coaching_count} references, need 3+)")

    # 7. Player engagement (1 point)
    engagement_keywords = ['fun', 'game', 'play', 'challenge', 'competition', 'score', 'teams']
    engagement_count = sum(1 for keyword in engagement_keywords if keyword in text_lower)
    if engagement_count >= 2:
        breakdown['engagement'] = True
        feedback.append(f"✓ Engagement elements present ({engagement_count} references)")
    else:
        feedback.append(f"✗ Limited engagement elements ({engagement_count} references, need 2+)")

    # Calculate total score
    total_score = sum(1 for criteria in breakdown.values() if criteria)

    return {
        'total_score': total_score,
        'max_score': 7,
        'breakdown': breakdown,
        'feedback': feedback
    }


def compare_plans(plan_a: str, plan_b: str) -> Dict:
    """
    Compare two session plans and determine a winner.

    Args:
        plan_a: Coach A's session plan text
        plan_b: Coach B's session plan text

    Returns:
        Dictionary containing:
            - score_a: Coach A's score dict
            - score_b: Coach B's score dict
            - winner: 'A', 'B', or 'TIE'
            - margin: Point difference
            - verdict: Human-readable explanation
    """
    score_a = score_plan(plan_a)
    score_b = score_plan(plan_b)

    # Determine winner
    diff = score_a['total_score'] - score_b['total_score']

    if diff > 0:
        winner = 'A'
        if diff >= 2:
            verdict = f"Coach A wins clearly with {diff} point advantage"
        else:
            verdict = f"Coach A wins narrowly with {diff} point advantage"
    elif diff < 0:
        winner = 'B'
        if abs(diff) >= 2:
            verdict = f"Coach B wins clearly with {abs(diff)} point advantage"
        else:
            verdict = f"Coach B wins narrowly with {abs(diff)} point advantage"
    else:
        winner = 'TIE'
        verdict = "Both plans scored equally - it's a tie!"

    return {
        'score_a': score_a,
        'score_b': score_b,
        'winner': winner,
        'margin': abs(diff),
        'verdict': verdict
    }


def get_score_interpretation(score: int, max_score: int = 7) -> Tuple[str, str]:
    """
    Get interpretation and color for a score.

    Args:
        score: The numerical score
        max_score: Maximum possible score (default 7)

    Returns:
        Tuple of (interpretation_text, color_class)
    """
    percentage = (score / max_score) * 100

    if percentage >= 85:  # 6-7 points
        return ("Excellent", "excellent")
    elif percentage >= 60:  # 4-5 points
        return ("Good", "good")
    elif percentage >= 30:  # 2-3 points
        return ("Adequate", "adequate")
    else:  # 0-1 points
        return ("Poor", "poor")


def get_limitations_text() -> List[str]:
    """
    Get list of heuristic scoring limitations.

    These limitations explain why AI judge (Stage 4) is needed.

    Returns:
        List of limitation statements
    """
    return [
        "Cannot evaluate quality of activity design (only presence/absence)",
        "Cannot assess age-appropriateness of content",
        "Cannot judge tactical sophistication",
        "Cannot evaluate coaching philosophy alignment",
        "Cannot assess progression within activities",
        "Cannot determine player-to-coach ratio appropriateness"
    ]

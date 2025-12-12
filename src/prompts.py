"""
Prompt templates for rugby session plan generation.

This module contains the base prompt template for generating session plans
using Claude. Additional coach-specific prompts will be added in later stages.
"""

def get_base_session_prompt(age_group: str, objective: str, duration: int, players: int) -> str:
    """
    Generate the base prompt for session plan creation.

    Args:
        age_group: Age group (e.g., "U10", "U12")
        objective: Session objective (e.g., "Improve passing under pressure")
        duration: Session duration in minutes
        players: Number of players

    Returns:
        Formatted prompt string for Claude API
    """
    prompt = f"""You are a rugby coach following RFU guidelines for {age_group}.

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

Format your response as clear sections with headings."""

    return prompt

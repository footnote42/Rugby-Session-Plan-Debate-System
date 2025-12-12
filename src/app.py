"""
Rugby Session Plan Generator - Stage 1: Single Coach Generator

A minimal Flask application that generates rugby session plans using Claude AI.
This is the foundation for the multi-coach debate system.
"""

import os
import logging
from flask import Flask, render_template, request, flash, redirect, url_for
from anthropic import Anthropic, APIError
from dotenv import load_dotenv
from prompts import get_base_session_prompt

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
# Template and static folders are at project root, not in src/
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = os.getenv('FLASK_SECRET_KEY', 'dev-secret-key-change-in-production')

# Initialize Anthropic client
try:
    client = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
    logger.info("Anthropic client initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize Anthropic client: {e}")
    client = None

# Configuration
MODEL = os.getenv('ANTHROPIC_MODEL', 'claude-sonnet-4-20250514')
MAX_TOKENS = int(os.getenv('MAX_TOKENS_GENERATION', '1500'))

# Age group options
AGE_GROUPS = ['U7', 'U8', 'U9', 'U10', 'U11', 'U12']


@app.route('/')
def index():
    """Display the session plan generation form."""
    return render_template('index.html', age_groups=AGE_GROUPS)


@app.route('/generate', methods=['POST'])
def generate():
    """
    Generate a session plan using Claude AI.

    Form inputs:
    - age_group: Selected age group (U7-U12)
    - objective: Session objective
    - duration: Session duration in minutes
    - players: Number of players

    Returns:
        Rendered result page with generated session plan or error
    """
    try:
        # Validate client initialization
        if client is None:
            flash('API client not initialized. Check your API key configuration.', 'error')
            return redirect(url_for('index'))

        # Get form data
        age_group = request.form.get('age_group', '').strip()
        objective = request.form.get('objective', '').strip()
        duration = request.form.get('duration', '').strip()
        players = request.form.get('players', '').strip()

        # Validate inputs
        if not all([age_group, objective, duration, players]):
            flash('All fields are required.', 'error')
            return redirect(url_for('index'))

        # Convert and validate numeric inputs
        try:
            duration = int(duration)
            players = int(players)
        except ValueError:
            flash('Duration and number of players must be valid numbers.', 'error')
            return redirect(url_for('index'))

        if duration < 30 or duration > 120:
            flash('Duration must be between 30 and 120 minutes.', 'error')
            return redirect(url_for('index'))

        if players < 6 or players > 30:
            flash('Number of players must be between 6 and 30.', 'error')
            return redirect(url_for('index'))

        logger.info(f"Generating session plan: {age_group}, {objective}, {duration}min, {players} players")

        # Generate prompt
        prompt = get_base_session_prompt(age_group, objective, duration, players)
        logger.debug(f"Prompt length: {len(prompt)} characters")

        # Call Claude API
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        # Extract session plan from response
        if response.content and len(response.content) > 0:
            session_plan = response.content[0].text
            logger.info(f"Session plan generated successfully. Length: {len(session_plan)} characters")
            logger.info(f"Tokens used: {response.usage.input_tokens} input, {response.usage.output_tokens} output")

            # Render result page
            return render_template(
                'result.html',
                age_group=age_group,
                objective=objective,
                duration=duration,
                players=players,
                session_plan=session_plan,
                input_tokens=response.usage.input_tokens,
                output_tokens=response.usage.output_tokens
            )
        else:
            logger.error("No content in API response")
            flash('No response received from API. Please try again.', 'error')
            return redirect(url_for('index'))

    except APIError as e:
        logger.error(f"Anthropic API error: {e}")
        flash(f'API Error: {str(e)}', 'error')
        return redirect(url_for('index'))

    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        flash(f'Unexpected error: {str(e)}', 'error')
        return redirect(url_for('index'))


@app.route('/health')
def health():
    """Health check endpoint."""
    return {
        'status': 'healthy',
        'api_configured': client is not None,
        'model': MODEL
    }


if __name__ == '__main__':
    # Check API key on startup
    if not os.getenv('ANTHROPIC_API_KEY'):
        logger.warning("WARNING: ANTHROPIC_API_KEY not set in environment!")
        print("\n⚠️  WARNING: ANTHROPIC_API_KEY not found in .env file")
        print("Please add your API key to the .env file before running.\n")

    # Run Flask app
    logger.info("Starting Flask application...")
    app.run(debug=True, host='127.0.0.1', port=5000)

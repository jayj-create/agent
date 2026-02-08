# LinkedIn Content Strategist Agent

An AI-powered LinkedIn content strategist built with Claude that helps you create professional content, optimize your profile, and grow your presence on LinkedIn.

## Features

- **Post Generation** - Create engaging posts in multiple styles: thought-leadership, storytelling, listicles, hot-takes, carousel scripts, and polls
- **Article Writing** - Generate long-form LinkedIn articles with proper structure and depth
- **Content Calendar** - Plan weeks of content with specific topics, hooks, and formats
- **Profile Optimization** - Get actionable recommendations to improve your headline, about section, and overall profile
- **Engagement Strategy** - Receive a personalized growth plan based on your goals, industry, and current stage
- **Content Repurposing** - Transform blog posts, presentations, or other content into multiple LinkedIn posts
- **Comment Responses** - Craft thoughtful replies to comments on your posts
- **Open Chat** - Ask anything about LinkedIn strategy in a conversational format

## Setup

### Prerequisites

- Python 3.10+
- An [Anthropic API key](https://console.anthropic.com/)

### Installation

```bash
pip install -e .
```

Set your API key:

```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

## Usage

### Interactive Mode

Launch the full interactive menu:

```bash
linkedin-strategist
# or
python -m linkedin_strategist
```

This opens a menu where you can choose from all available features.

### Quick Post Generation

Generate a post directly from the command line:

```bash
linkedin-strategist post "The future of remote work" --tone conversational --style storytelling
```

Options:
- `--tone` : professional, conversational, inspirational, bold (default: professional)
- `--style` : thought-leadership, storytelling, listicle, hot-take, carousel-script, poll (default: thought-leadership)
- `--audience` : target audience description (default: general professional)
- `--no-hashtags` : skip hashtag suggestions
- `--no-cta` : skip call-to-action

### Python API

Use the agent programmatically in your own scripts:

```python
from linkedin_strategist import LinkedInStrategist

strategist = LinkedInStrategist()

# Generate a post
post = strategist.generate_post(
    topic="Why most technical interviews are broken",
    tone="bold",
    style="hot-take",
)
print(post)

# Generate a content calendar
calendar = strategist.generate_content_calendar(
    weeks=2,
    themes=["AI/ML insights", "engineering leadership", "career growth"],
    industry="technology",
)
print(calendar)

# Get profile optimization advice
advice = strategist.optimize_profile(
    current_headline="Software Engineer at Acme Corp",
    role="Senior Software Engineer",
    industry="technology",
    goals="attract recruiter interest and build thought leadership",
)
print(advice)

# Repurpose a blog post
posts = strategist.repurpose_content(
    source_content="Your blog post text here...",
    source_type="blog post",
    num_posts=3,
)
print(posts)
```

## Project Structure

```
linkedin_strategist/
├── __init__.py              # Package init
├── __main__.py              # python -m entry point
├── agent.py                 # Core LinkedInStrategist class
├── cli.py                   # Interactive CLI
├── generators/
│   ├── __init__.py
│   ├── post_generator.py    # Post and calendar generation
│   ├── article_generator.py # Long-form article generation
│   ├── engagement_advisor.py# Strategy and comment responses
│   └── profile_optimizer.py # Profile optimization
├── templates/
│   ├── __init__.py
│   └── system_prompts.py    # All Claude system prompts
└── utils/
    └── __init__.py
```

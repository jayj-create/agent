"""Interactive CLI for the LinkedIn Content Strategist agent."""

from __future__ import annotations

import argparse
import sys

from .agent import LinkedInStrategist


def print_header():
    print()
    print("=" * 60)
    print("  LinkedIn Content Strategist Agent")
    print("  Powered by Claude")
    print("=" * 60)
    print()


def print_menu():
    print("What would you like to do?")
    print()
    print("  1. Generate a LinkedIn post")
    print("  2. Generate a LinkedIn article")
    print("  3. Get an engagement strategy")
    print("  4. Generate a content calendar")
    print("  5. Optimize your profile")
    print("  6. Repurpose existing content")
    print("  7. Get comment response suggestions")
    print("  8. Chat with the strategist")
    print("  9. Exit")
    print()


def prompt_input(label: str, default: str = "") -> str:
    suffix = f" [{default}]" if default else ""
    result = input(f"  {label}{suffix}: ").strip()
    return result if result else default


def prompt_multiline(label: str) -> str:
    print(f"  {label} (enter a blank line to finish):")
    lines = []
    while True:
        line = input("  > ")
        if not line.strip():
            break
        lines.append(line)
    return "\n".join(lines)


def handle_generate_post(strategist: LinkedInStrategist):
    print("\n--- Generate a LinkedIn Post ---\n")
    topic = prompt_input("Topic (what's the post about?)")
    if not topic:
        print("Topic is required.")
        return

    tone = prompt_input("Tone", "professional")
    style = prompt_input(
        "Style (thought-leadership / storytelling / listicle / hot-take / carousel-script / poll)",
        "thought-leadership",
    )
    audience = prompt_input("Target audience", "general professional")
    hashtags = prompt_input("Include hashtags? (y/n)", "y").lower().startswith("y")
    cta = prompt_input("Include call-to-action? (y/n)", "y").lower().startswith("y")

    print("\nGenerating your post...\n")
    result = strategist.generate_post(
        topic=topic, tone=tone, style=style,
        audience=audience, include_hashtags=hashtags, include_cta=cta,
    )
    print("-" * 50)
    print(result)
    print("-" * 50)


def handle_generate_article(strategist: LinkedInStrategist):
    print("\n--- Generate a LinkedIn Article ---\n")
    topic = prompt_input("Topic")
    if not topic:
        print("Topic is required.")
        return

    word_count = int(prompt_input("Target word count", "800"))
    tone = prompt_input("Tone", "authoritative")
    audience = prompt_input("Target audience", "industry professionals")

    key_points_raw = prompt_input("Key points to cover (comma-separated, or leave blank)")
    key_points = [p.strip() for p in key_points_raw.split(",") if p.strip()] if key_points_raw else None

    print("\nGenerating your article...\n")
    result = strategist.generate_article(
        topic=topic, word_count=word_count, tone=tone,
        audience=audience, key_points=key_points,
    )
    print("-" * 50)
    print(result)
    print("-" * 50)


def handle_engagement_strategy(strategist: LinkedInStrategist):
    print("\n--- Engagement Strategy ---\n")
    goals = prompt_input("What are your LinkedIn goals?")
    if not goals:
        print("Goals are required.")
        return

    industry = prompt_input("Industry", "technology")
    followers_raw = prompt_input("Current follower count (or leave blank)")
    followers = int(followers_raw) if followers_raw else None
    frequency = prompt_input("Planned posting frequency", "3x per week")

    print("\nCrafting your strategy...\n")
    result = strategist.get_engagement_strategy(
        goals=goals, industry=industry,
        current_followers=followers, posting_frequency=frequency,
    )
    print("-" * 50)
    print(result)
    print("-" * 50)


def handle_content_calendar(strategist: LinkedInStrategist):
    print("\n--- Content Calendar ---\n")
    weeks = int(prompt_input("Number of weeks to plan", "4"))
    industry = prompt_input("Industry", "technology")

    themes_raw = prompt_input("Content themes (comma-separated, or leave blank for defaults)")
    themes = [t.strip() for t in themes_raw.split(",") if t.strip()] if themes_raw else None

    days_raw = prompt_input("Posting days (comma-separated)", "Monday, Wednesday, Friday")
    posting_days = [d.strip() for d in days_raw.split(",") if d.strip()]

    print("\nBuilding your content calendar...\n")
    result = strategist.generate_content_calendar(
        weeks=weeks, themes=themes,
        industry=industry, posting_days=posting_days,
    )
    print("-" * 50)
    print(result)
    print("-" * 50)


def handle_profile_optimization(strategist: LinkedInStrategist):
    print("\n--- Profile Optimization ---\n")
    headline = prompt_input("Current headline (or leave blank)")
    role = prompt_input("Current role/title")
    industry = prompt_input("Industry")
    goals = prompt_input("What do you want LinkedIn to do for you?")
    about = ""
    if prompt_input("Include your current About section? (y/n)", "n").lower().startswith("y"):
        about = prompt_multiline("Paste your About section")

    print("\nAnalyzing your profile...\n")
    result = strategist.optimize_profile(
        current_headline=headline, current_about=about,
        role=role, industry=industry, goals=goals,
    )
    print("-" * 50)
    print(result)
    print("-" * 50)


def handle_repurpose(strategist: LinkedInStrategist):
    print("\n--- Repurpose Content ---\n")
    source_type = prompt_input("Source content type", "blog post")
    num_posts = int(prompt_input("Number of posts to generate", "3"))
    content = prompt_multiline("Paste your content")

    if not content:
        print("Content is required.")
        return

    print("\nRepurposing your content...\n")
    result = strategist.repurpose_content(
        source_content=content, source_type=source_type, num_posts=num_posts,
    )
    print("-" * 50)
    print(result)
    print("-" * 50)


def handle_comment_responses(strategist: LinkedInStrategist):
    print("\n--- Comment Response Suggestions ---\n")
    post_context = prompt_input("What was your post about?")
    if not post_context:
        print("Post context is required.")
        return

    print("  Enter comments to respond to (one per line, blank line to finish):")
    comments = []
    while True:
        comment = input("  > ").strip()
        if not comment:
            break
        comments.append(comment)

    if not comments:
        print("At least one comment is required.")
        return

    print("\nCrafting responses...\n")
    result = strategist.generate_comment_responses(
        post_context=post_context, comments=comments,
    )
    print("-" * 50)
    print(result)
    print("-" * 50)


def handle_chat(strategist: LinkedInStrategist):
    print("\n--- Chat with the Strategist ---")
    print("  (Type 'back' to return to the menu)\n")
    history: list[dict] = []

    while True:
        user_input = input("You: ").strip()
        if not user_input or user_input.lower() == "back":
            break

        response = strategist.chat(user_input, history)
        history.append({"role": "user", "content": user_input})
        history.append({"role": "assistant", "content": response})
        print(f"\nStrategist: {response}\n")


HANDLERS = {
    "1": handle_generate_post,
    "2": handle_generate_article,
    "3": handle_engagement_strategy,
    "4": handle_content_calendar,
    "5": handle_profile_optimization,
    "6": handle_repurpose,
    "7": handle_comment_responses,
    "8": handle_chat,
}


def interactive_mode(strategist: LinkedInStrategist):
    """Run the interactive menu loop."""
    print_header()
    while True:
        print_menu()
        choice = input("Enter your choice (1-9): ").strip()
        if choice == "9":
            print("\nGoodbye! Go build that LinkedIn presence.\n")
            break
        handler = HANDLERS.get(choice)
        if handler:
            handler(strategist)
            print()
        else:
            print("Invalid choice. Please pick 1-9.\n")


def quick_post_mode(strategist: LinkedInStrategist, args: argparse.Namespace):
    """Generate a post directly from CLI arguments."""
    result = strategist.generate_post(
        topic=args.topic,
        tone=args.tone,
        style=args.style,
        audience=args.audience,
        include_hashtags=not args.no_hashtags,
        include_cta=not args.no_cta,
    )
    print(result)


def main():
    parser = argparse.ArgumentParser(
        description="LinkedIn Content Strategist Agent - powered by Claude",
    )
    parser.add_argument("--api-key", help="Anthropic API key (or set ANTHROPIC_API_KEY env var)")

    subparsers = parser.add_subparsers(dest="command")

    # Quick post generation
    post_parser = subparsers.add_parser("post", help="Generate a LinkedIn post directly")
    post_parser.add_argument("topic", help="Post topic")
    post_parser.add_argument("--tone", default="professional", help="Post tone")
    post_parser.add_argument("--style", default="thought-leadership", help="Post style")
    post_parser.add_argument("--audience", default="general professional", help="Target audience")
    post_parser.add_argument("--no-hashtags", action="store_true", help="Skip hashtags")
    post_parser.add_argument("--no-cta", action="store_true", help="Skip call-to-action")

    args = parser.parse_args()
    strategist = LinkedInStrategist(api_key=args.api_key)

    if args.command == "post":
        quick_post_mode(strategist, args)
    else:
        interactive_mode(strategist)


if __name__ == "__main__":
    main()

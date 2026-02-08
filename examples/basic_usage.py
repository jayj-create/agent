"""Basic usage examples for the LinkedIn Content Strategist agent."""

from linkedin_strategist.agent import LinkedInStrategist


def main():
    # Initialize the strategist (uses ANTHROPIC_API_KEY env var)
    strategist = LinkedInStrategist()

    # --- Example 1: Generate a thought-leadership post ---
    print("=" * 50)
    print("EXAMPLE 1: Thought Leadership Post")
    print("=" * 50)
    post = strategist.generate_post(
        topic="Why the best engineers are great writers",
        tone="conversational",
        style="thought-leadership",
        audience="software engineers and tech leaders",
    )
    print(post)
    print()

    # --- Example 2: Generate a storytelling post ---
    print("=" * 50)
    print("EXAMPLE 2: Storytelling Post")
    print("=" * 50)
    post = strategist.generate_post(
        topic="A failed product launch that taught me everything about customer discovery",
        tone="inspirational",
        style="storytelling",
        audience="startup founders and product managers",
    )
    print(post)
    print()

    # --- Example 3: Get a content calendar ---
    print("=" * 50)
    print("EXAMPLE 3: 2-Week Content Calendar")
    print("=" * 50)
    calendar = strategist.generate_content_calendar(
        weeks=2,
        themes=["AI trends", "leadership lessons", "productivity tips"],
        industry="technology",
        posting_days=["Tuesday", "Thursday"],
    )
    print(calendar)
    print()

    # --- Example 4: Profile optimization ---
    print("=" * 50)
    print("EXAMPLE 4: Profile Optimization")
    print("=" * 50)
    advice = strategist.optimize_profile(
        current_headline="Product Manager at TechCo",
        role="Senior Product Manager",
        industry="B2B SaaS",
        goals="attract speaking opportunities and advisory roles",
    )
    print(advice)
    print()

    # --- Example 5: Chat with the strategist ---
    print("=" * 50)
    print("EXAMPLE 5: Strategy Chat")
    print("=" * 50)
    response = strategist.chat(
        "I just started posting on LinkedIn last week. I'm a data scientist "
        "and I want to build an audience of other data professionals. "
        "What should my first 10 posts be about?"
    )
    print(response)


if __name__ == "__main__":
    main()

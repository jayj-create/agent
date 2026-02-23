"""LinkedIn post generation module."""

from __future__ import annotations

import anthropic

from ..templates.system_prompts import (
    POST_GENERATOR_PROMPT,
    CONTENT_CALENDAR_PROMPT,
    REPURPOSE_PROMPT,
)


class PostGenerator:
    """Generates LinkedIn posts in various styles and formats."""

    def __init__(self, client: anthropic.Anthropic, model: str):
        self.client = client
        self.model = model

    def generate(
        self,
        topic: str,
        tone: str = "professional",
        style: str = "thought-leadership",
        include_hashtags: bool = True,
        include_cta: bool = True,
        audience: str = "general professional",
    ) -> str:
        """Generate a single LinkedIn post."""
        user_prompt = f"""Write a LinkedIn post with the following specifications:

**Topic:** {topic}
**Tone:** {tone}
**Style:** {style}
**Target Audience:** {audience}
**Include Hashtags:** {"Yes (3-5 relevant hashtags)" if include_hashtags else "No"}
**Include Call-to-Action:** {"Yes" if include_cta else "No"}

Write the post ready to copy-paste into LinkedIn. Use appropriate line breaks \
and formatting for the platform."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=1024,
            system=POST_GENERATOR_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

    def generate_calendar(
        self,
        weeks: int = 4,
        themes: list[str] | None = None,
        industry: str = "technology",
        posting_days: list[str] | None = None,
    ) -> str:
        """Generate a content calendar with post ideas."""
        if themes is None:
            themes = ["industry insights", "personal growth", "how-to/tips", "storytelling"]
        if posting_days is None:
            posting_days = ["Monday", "Wednesday", "Friday"]

        user_prompt = f"""Create a {weeks}-week LinkedIn content calendar with the following parameters:

**Industry:** {industry}
**Content Pillars/Themes:** {", ".join(themes)}
**Posting Days:** {", ".join(posting_days)}

For each post slot, provide:
1. The date/day
2. Content pillar being used
3. Post format (text, carousel, poll, image post, etc.)
4. A specific topic/angle
5. The opening hook (first 1-2 lines)
6. Key points to cover

Also include 1-2 "engagement-only" days per week where the focus is commenting \
on others' content rather than posting."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=CONTENT_CALENDAR_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

    def repurpose(
        self,
        source_content: str,
        source_type: str = "blog post",
        num_posts: int = 3,
    ) -> str:
        """Repurpose existing content into LinkedIn posts."""
        user_prompt = f"""Repurpose the following {source_type} into {num_posts} distinct LinkedIn posts.

Each post should:
- Use a different angle or format
- Stand alone without needing the original content
- Be optimized for LinkedIn engagement
- Include relevant hashtags

**Original {source_type}:**

{source_content}

---

Generate {num_posts} ready-to-post LinkedIn posts, clearly separated and labeled."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=REPURPOSE_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

"""LinkedIn engagement strategy advisor module."""

from __future__ import annotations

import anthropic

from ..templates.system_prompts import ENGAGEMENT_ADVISOR_PROMPT, COMMENT_RESPONSE_PROMPT


class EngagementAdvisor:
    """Provides LinkedIn engagement strategies and comment response guidance."""

    def __init__(self, client: anthropic.Anthropic, model: str):
        self.client = client
        self.model = model

    def advise(
        self,
        goals: str,
        industry: str = "technology",
        current_followers: int | None = None,
        posting_frequency: str = "3x per week",
    ) -> str:
        """Generate a personalized LinkedIn engagement strategy."""
        follower_context = ""
        if current_followers is not None:
            if current_followers < 500:
                stage = "early-stage (building foundation)"
            elif current_followers < 5000:
                stage = "growth-stage (gaining momentum)"
            elif current_followers < 25000:
                stage = "established (scaling influence)"
            else:
                stage = "authority (maintaining leadership)"
            follower_context = f"\n**Current Followers:** {current_followers:,} ({stage})"

        user_prompt = f"""Create a comprehensive LinkedIn engagement strategy:

**Goals:** {goals}
**Industry:** {industry}
**Planned Posting Frequency:** {posting_frequency}{follower_context}

Please cover:
1. **Content Strategy**: What types of content to post and why
2. **Engagement Tactics**: How to build meaningful interactions daily
3. **Algorithm Tips**: How to optimize for LinkedIn's current algorithm
4. **Networking Strategy**: How to grow connections strategically
5. **Commenting Strategy**: How to use comments to increase visibility
6. **Metrics to Track**: What to measure and what benchmarks to aim for
7. **Quick Wins**: 5 things to do this week for immediate impact
8. **30-Day Action Plan**: A week-by-week roadmap to start executing"""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=ENGAGEMENT_ADVISOR_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

    def generate_responses(
        self,
        post_context: str,
        comments: list[str],
    ) -> str:
        """Generate thoughtful responses to comments on a post."""
        formatted_comments = "\n".join(
            f"**Comment {i + 1}:** \"{comment}\"" for i, comment in enumerate(comments)
        )

        user_prompt = f"""I need help responding to comments on my LinkedIn post.

**My Post Was About:** {post_context}

**Comments to Respond To:**
{formatted_comments}

For each comment, provide a thoughtful response that:
- Acknowledges their point
- Adds value to the conversation
- Maintains an authentic, warm tone
- Is 2-4 sentences long
- Invites further dialogue when appropriate"""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=COMMENT_RESPONSE_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

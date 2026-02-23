"""LinkedIn article generation module."""

from __future__ import annotations

import anthropic

from ..templates.system_prompts import ARTICLE_GENERATOR_PROMPT


class ArticleGenerator:
    """Generates long-form LinkedIn articles."""

    def __init__(self, client: anthropic.Anthropic, model: str):
        self.client = client
        self.model = model

    def generate(
        self,
        topic: str,
        word_count: int = 800,
        tone: str = "authoritative",
        audience: str = "industry professionals",
        key_points: list[str] | None = None,
    ) -> str:
        """Generate a long-form LinkedIn article."""
        points_section = ""
        if key_points:
            formatted = "\n".join(f"- {point}" for point in key_points)
            points_section = f"\n**Key Points to Cover:**\n{formatted}"

        user_prompt = f"""Write a LinkedIn article with the following specifications:

**Topic:** {topic}
**Target Word Count:** ~{word_count} words
**Tone:** {tone}
**Target Audience:** {audience}{points_section}

Structure the article with:
1. A compelling headline
2. An engaging opening hook
3. Clear sections with subheadings
4. Concrete examples or data points
5. Actionable takeaways
6. A discussion-prompting conclusion

Output in clean markdown format."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=8192,
            system=ARTICLE_GENERATOR_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

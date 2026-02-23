"""LinkedIn profile optimization module."""

from __future__ import annotations

import anthropic

from ..templates.system_prompts import PROFILE_OPTIMIZER_PROMPT


class ProfileOptimizer:
    """Provides LinkedIn profile optimization recommendations and rewrites."""

    def __init__(self, client: anthropic.Anthropic, model: str):
        self.client = client
        self.model = model

    def optimize(
        self,
        current_headline: str = "",
        current_about: str = "",
        role: str = "",
        industry: str = "",
        goals: str = "",
    ) -> str:
        """Generate profile optimization recommendations."""
        sections = []

        if current_headline:
            sections.append(f"**Current Headline:** {current_headline}")
        if current_about:
            sections.append(f"**Current About Section:**\n{current_about}")
        if role:
            sections.append(f"**Current Role:** {role}")
        if industry:
            sections.append(f"**Industry:** {industry}")
        if goals:
            sections.append(f"**LinkedIn Goals:** {goals}")

        profile_info = "\n\n".join(sections) if sections else "No current profile info provided."

        user_prompt = f"""Review and optimize my LinkedIn profile:

{profile_info}

Please provide:
1. **Headline Options**: 3 optimized headline alternatives with explanation
2. **About Section Rewrite**: A compelling About section (if current one was provided) \
or a template/framework to follow
3. **Keyword Recommendations**: Industry keywords to weave into my profile
4. **Featured Section Ideas**: What to showcase in the Featured section
5. **Profile Completion Checklist**: Any gaps or areas to strengthen
6. **Quick Optimization Tips**: Immediate changes for better discoverability

For each suggestion, explain *why* it works — don't just give the rewrite."""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=4096,
            system=PROFILE_OPTIMIZER_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
        return response.content[0].text

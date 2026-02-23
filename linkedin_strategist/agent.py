"""Core LinkedIn Content Strategist Agent powered by Claude."""

import anthropic

from .generators.post_generator import PostGenerator
from .generators.article_generator import ArticleGenerator
from .generators.engagement_advisor import EngagementAdvisor
from .generators.profile_optimizer import ProfileOptimizer
from .templates.system_prompts import STRATEGIST_SYSTEM_PROMPT


class LinkedInStrategist:
    """An AI-powered LinkedIn content strategist that uses Claude to generate
    professional content, optimize profiles, and advise on engagement strategy."""

    def __init__(self, api_key: str | None = None):
        self.client = anthropic.Anthropic(api_key=api_key) if api_key else anthropic.Anthropic()
        self.model = "claude-sonnet-4-20250514"
        self.post_generator = PostGenerator(self.client, self.model)
        self.article_generator = ArticleGenerator(self.client, self.model)
        self.engagement_advisor = EngagementAdvisor(self.client, self.model)
        self.profile_optimizer = ProfileOptimizer(self.client, self.model)

    def generate_post(
        self,
        topic: str,
        tone: str = "professional",
        style: str = "thought-leadership",
        include_hashtags: bool = True,
        include_cta: bool = True,
        audience: str = "general professional",
    ) -> str:
        """Generate a LinkedIn post on a given topic.

        Args:
            topic: The subject matter of the post.
            tone: Voice tone - professional, conversational, inspirational, bold.
            style: Post style - thought-leadership, storytelling, listicle,
                   hot-take, carousel-script, poll.
            include_hashtags: Whether to append relevant hashtags.
            include_cta: Whether to include a call-to-action.
            audience: Target audience description.

        Returns:
            The generated LinkedIn post text.
        """
        return self.post_generator.generate(
            topic=topic,
            tone=tone,
            style=style,
            include_hashtags=include_hashtags,
            include_cta=include_cta,
            audience=audience,
        )

    def generate_article(
        self,
        topic: str,
        word_count: int = 800,
        tone: str = "authoritative",
        audience: str = "industry professionals",
        key_points: list[str] | None = None,
    ) -> str:
        """Generate a long-form LinkedIn article.

        Args:
            topic: Article subject matter.
            word_count: Target word count.
            tone: Writing tone.
            audience: Target reader description.
            key_points: Optional list of points to cover.

        Returns:
            The generated article in markdown format.
        """
        return self.article_generator.generate(
            topic=topic,
            word_count=word_count,
            tone=tone,
            audience=audience,
            key_points=key_points,
        )

    def get_engagement_strategy(
        self,
        goals: str,
        industry: str = "technology",
        current_followers: int | None = None,
        posting_frequency: str = "3x per week",
    ) -> str:
        """Get a personalized LinkedIn engagement strategy.

        Args:
            goals: What you want to achieve on LinkedIn.
            industry: Your industry vertical.
            current_followers: Current follower count for tailored advice.
            posting_frequency: How often you plan to post.

        Returns:
            A detailed engagement strategy document.
        """
        return self.engagement_advisor.advise(
            goals=goals,
            industry=industry,
            current_followers=current_followers,
            posting_frequency=posting_frequency,
        )

    def generate_content_calendar(
        self,
        weeks: int = 4,
        themes: list[str] | None = None,
        industry: str = "technology",
        posting_days: list[str] | None = None,
    ) -> str:
        """Generate a content calendar with post ideas.

        Args:
            weeks: Number of weeks to plan.
            themes: Content themes/pillars to rotate through.
            industry: Your industry for relevant topics.
            posting_days: Which days of the week to post.

        Returns:
            A structured content calendar.
        """
        return self.post_generator.generate_calendar(
            weeks=weeks,
            themes=themes,
            industry=industry,
            posting_days=posting_days,
        )

    def optimize_profile(
        self,
        current_headline: str = "",
        current_about: str = "",
        role: str = "",
        industry: str = "",
        goals: str = "",
    ) -> str:
        """Get suggestions to optimize your LinkedIn profile.

        Args:
            current_headline: Your current headline text.
            current_about: Your current About section.
            role: Your current role / title.
            industry: Your industry.
            goals: What you want LinkedIn to do for you.

        Returns:
            Profile optimization recommendations.
        """
        return self.profile_optimizer.optimize(
            current_headline=current_headline,
            current_about=current_about,
            role=role,
            industry=industry,
            goals=goals,
        )

    def repurpose_content(
        self,
        source_content: str,
        source_type: str = "blog post",
        num_posts: int = 3,
    ) -> str:
        """Repurpose existing content into LinkedIn posts.

        Args:
            source_content: The original content to repurpose.
            source_type: Type of original content (blog post, presentation, etc.).
            num_posts: How many LinkedIn posts to generate from it.

        Returns:
            Multiple LinkedIn posts derived from the source content.
        """
        return self.post_generator.repurpose(
            source_content=source_content,
            source_type=source_type,
            num_posts=num_posts,
        )

    def generate_comment_responses(
        self,
        post_context: str,
        comments: list[str],
    ) -> str:
        """Generate thoughtful responses to comments on your posts.

        Args:
            post_context: What your original post was about.
            comments: List of comments to respond to.

        Returns:
            Suggested responses for each comment.
        """
        return self.engagement_advisor.generate_responses(
            post_context=post_context,
            comments=comments,
        )

    def chat(self, message: str, conversation_history: list[dict] | None = None) -> str:
        """Have an open-ended conversation with the strategist about LinkedIn.

        Args:
            message: Your question or request.
            conversation_history: Optional prior messages for context.

        Returns:
            The strategist's response.
        """
        messages = list(conversation_history) if conversation_history else []
        messages.append({"role": "user", "content": message})

        response = self.client.messages.create(
            model=self.model,
            max_tokens=2048,
            system=STRATEGIST_SYSTEM_PROMPT,
            messages=messages,
        )
        return response.content[0].text

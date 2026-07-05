from flows.pipeline.prompt_base.models import BaseIdea, CategoryHandler
from flows.pipeline.prompt_longs.tio_warren import (
    constants as tio_warren_long_constants,
)


class MindsetTioWarrenIdeaLong(BaseIdea):
    """
    Deep idea model for long-form financial mindset transformation stories featuring Tio Warren.
    """
    IDEA_PROMPT = tio_warren_long_constants.IDEA_PROMPT_MINDSET
    financial_problem: str
    mindset_shift: str
    key_principle: str


class StrategyTioWarrenIdeaLong(BaseIdea):
    """
    Deep idea model for long-form practical financial strategy videos featuring Tio Warren.
    """
    IDEA_PROMPT = tio_warren_long_constants.IDEA_PROMPT_ESTRATEGIA
    strategy_name: str
    common_mistake: str
    actionable_tip: str


class TioWarrenHandlerLong(CategoryHandler):
    """
    Specialized handler for Long videos themed around Tio Warren for Código Capital.
    Encapsulates Mindset and Strategy finance variants.
    """

    SCRIPT_PROMPT = tio_warren_long_constants.SCRIPT_PROMPT
    idea_variants = [
        MindsetTioWarrenIdeaLong,
        StrategyTioWarrenIdeaLong,
    ]
